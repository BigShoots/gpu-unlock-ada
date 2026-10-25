#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only
"""Extract matching private test inputs; no firmware execution or GPU access."""
import argparse
import hashlib
import json
from pathlib import Path

PROM = '17137e23c4949913e634bd0d309321648ff5ac7ac48f4eb37c0cc91d61f96add'
CODE = {
    '53ef1716fa7a8cf866c986e85dd8412185a9fd58dd89e90202f97cb0997c96a6': (158, 14584),
    'b689e24eb05256b38eb1ad2e5544c5b8f1b6e59409bfd13d2bee7be5a95211a1': (451, 24961),
    '6702c960bb457e20a93174ada93444d1e1a87d2858caac23878255516248b8e8': (456, 10525),
    '216c7270fa08ad9e4c3694d34d825e9e904554a1af5ffa2aeead4317c5537b37': (554, 138183),
}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('capture', type=Path)
    p.add_argument('--out', required=True, type=Path, help='New private destination')
    a = p.parse_args()
    if a.capture.stat().st_size > 16 * 1024 * 1024:
        p.error('Capture exceeds the bounded schema-4 input size')
    j = json.loads(a.capture.read_text(encoding='utf-8-sig'))
    if j.get('schema') != 4 or not j['physical_prom'].get('complete'):
        p.error('Requires a complete schema-4 PROM capture')
    rom = bytes.fromhex(j['physical_prom']['hex'])
    if len(rom) != 1048576 or hashlib.sha256(rom).hexdigest() != PROM:
        p.error('ROM differs from the reviewed profile; do not bypass admission')
    files = {'ad103-physical-prom.bin': rom}
    for agent in j['platform']['gpu_agents']:
        code = agent['code']
        data = bytes.fromhex(code['hex'])
        digest = hashlib.sha256(data).hexdigest()
        if digest not in CODE or digest != code['loaded_sha256']:
            p.error('Loaded driver code differs from the reviewed profile')
        label, size = CODE[digest]
        name = f'driver-{label}.bin'  # Stable fixture labels, not current handles.
        if len(data) != size or name in files:
            p.error('Duplicate or truncated code snapshot')
        files[name] = data
    if len(files) != 5:
        p.error('All four reviewed driver profiles are required')
    a.out.mkdir(parents=True, exist_ok=False)
    for name, data in files.items():
        (a.out / name).write_bytes(data)
    print('Extracted 5 private files. Keep them out of Git and public uploads.')

if __name__ == '__main__':
    main()
