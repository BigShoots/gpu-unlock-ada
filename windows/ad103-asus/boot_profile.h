/* SPDX-License-Identifier: GPL-2.0-only */
/* Keep the local ESP layout and boot manager pin out of the public source tree. */
#pragma once
#include "local/boot_profile.h"
#if !defined(GU_WINDOWS_PARTITION_INITIALIZER) || !defined(GU_WINDOWS_PARTITION_NUMBER) || \
    !defined(GU_WINDOWS_PARTITION_START) || !defined(GU_WINDOWS_PARTITION_SIZE) || \
    !defined(GU_WINDOWS_BOOTMGR_BYTES) || !defined(GU_WINDOWS_BOOTMGR_SHA256)
#error "Configure the reviewed ESP layout and boot manager in local/boot_profile.h before building."
#endif
/* Host tests keep a fake ESP GUID but the real layout and boot manager pin,
 * so the private copy of bootmgfw.efi is checked against the same values. */
#if defined(GU_HOST_TEST_PROFILE)
#undef GU_WINDOWS_PARTITION_INITIALIZER
#define GU_WINDOWS_PARTITION_INITIALIZER {0x11111111,0x2222,0x3333,{0x84,0x44,0x55,0x66,0x77,0x88,0x99,0xaa}}
#endif
