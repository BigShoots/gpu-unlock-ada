# AD103/ASUS AM5 port - 2026-10-25

- Retarget the AD104 profile to one MSI RTX 4070 Ti SUPER (AD103) on an ASUS ROG STRIX B650E-I from a read-only probe capture.
- Port the ownership adapter: two outputs, EDID consumer detached first, five-stage release, four AMD xHCI hosts, four pinned driver code ranges.
- Handle the firmware's stale PCI IO attribute without changing config space; restore memory decode only.
- Move the ESP layout and boot manager pin into the ignored local profile.
- Replay the real captured graph in the ownership test; log each preflight step.
- First hardware run: transaction completed and Windows returned. FP16/BF16 GEMM +73%, FP32 unchanged, numerical checks passed.

# Latence.app AD104 Windows changes — 2026-10-24

- Adapt the pinned Ada transaction to checked UEFI PCI I/O, DMA and explicit error/retention state for the captured AD104 profile.
- Add MSI console/GOP ownership capture/validation and callback-based release, exclusive PCI claim and IO/MEM-only restoration.
- Preload a pinned Windows manager from a read-only ESP, require U for one attempt and contain all post-mutation failures.
- Handle periodic USB additions/removals within bounded preflight-classified USB ownership, while preserving GPU/display/console and host ownership invariants.
- Require payload marker, HALT, permission and selector/readout checks before/after one FLR; free DMA only after verified quiescence.
- Record one successful Windows handoff and three numerical/throughput runs; retain exact scope and pending A/B/A/long-duration qualification.
- Publish source-only with an ignored local ESP header, synthetic mock-test GUID, configurable compiler paths, diagnostic source and sanitized evidence. The configured public source rebuilds the historical hardware EFI byte-for-byte; 177 scenarios freshly pass.

Upstream commits and full notices remain in provenance.json and licence files. No Linux target admission changes.
