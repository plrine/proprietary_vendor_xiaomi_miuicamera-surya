#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024-2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/xiaomi/miuicamera-surya',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/priv-app/MiuiCamera/MiuiCamera.apk': blob_fixup()
        .apktool_patch('patches'),
    # Replace the S-era Surface vtable connect() call with ANativeWindow perform(NATIVE_WINDOW_API_CONNECT, NATIVE_WINDOW_API_CPU)
    ('system_ext/lib64/libcamera_algoup_jni.xiaomi.so', 'system_ext/lib64/libcamera_mianode_jni.xiaomi.so'): blob_fixup()
        .sig_replace('a8 02 40 f9 e2 03 00 91 41 00 80 52 e0 03 15 aa 08 a9 40 f9 e3 03 1f 2a 00 01 3f d6', 'a0 42 00 91 08 4c 40 f9 a1 01 80 52 42 00 80 52 00 01 3f d6 1f 20 03 d5 1f 20 03 d5'),
}  # fmt: skip

module = ExtractUtilsModule(
    'surya',
    'xiaomi/miuicamera-surya',
    device_rel_path='vendor/xiaomi/miuicamera-surya',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
