#
# Copyright (C) 2024-2026 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from the proprietary version
$(call inherit-product, vendor/xiaomi/miuicamera-surya/surya/surya-vendor.mk)

# Overlays
PRODUCT_PACKAGES += \
    MiuiCameraOverlay

# Priv-app permissions
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/privapp-permissions-miuicamera.xml:$(TARGET_COPY_OUT_SYSTEM_EXT)/etc/permissions/privapp-permissions-miuicamera.xml \
    $(LOCAL_PATH)/configs/privapp-permissions-miuiextraphoto.xml:$(TARGET_COPY_OUT_SYSTEM_EXT)/etc/permissions/privapp-permissions-miuiextraphoto.xml

# Default permissions
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/configs/default-permissions-miuicamera.xml:$(TARGET_COPY_OUT_SYSTEM_EXT)/etc/default-permissions/default-permissions-miuicamera.xml

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
