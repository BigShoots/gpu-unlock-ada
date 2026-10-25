/* SPDX-License-Identifier: GPL-2.0-only */
/* Copy to local/boot_profile.h and replace with the reviewed ESP partition and
 * boot manager of this PC. All-zero is deliberately not a usable configuration.
 * GPU, ROM and driver-code guards still have to match the exact profile.
 * Do not remove or widen those guards to make another machine boot. */
#define GU_WINDOWS_PARTITION_INITIALIZER {0,0,0,{0,0,0,0,0,0,0,0}}
#define GU_WINDOWS_PARTITION_NUMBER 0
#define GU_WINDOWS_PARTITION_START 0ULL
#define GU_WINDOWS_PARTITION_SIZE 0ULL
#define GU_WINDOWS_BOOTMGR_BYTES 0
#define GU_WINDOWS_BOOTMGR_SHA256 ""
