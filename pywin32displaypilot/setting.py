# -*- encoding: utf-8 -*-
import logging
import win32api as win32
import win32con

from pywin32displaypilot.screen import all_screens

L = logging.getLogger(__name__)


def get_display_setting(device):
    dm = win32.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)

    L.debug("Rotate device %s (%s) -> %d %dx%d",
            device.DeviceString, device.DeviceName, dm.DisplayOrientation, dm.PelsWidth, dm.PelsHeight)
    return dm


def need_swap_pels(previous_orientation, next_orientation):
    landscape = [win32con.DMDO_DEFAULT, win32con.DMDO_180]
    portrait = [win32con.DMDO_90, win32con.DMDO_270]

    return (previous_orientation in landscape and next_orientation in portrait) or \
           (previous_orientation in portrait and next_orientation in landscape)


def set_display_orientation(device, orientation):
    dm = get_display_setting(device)
    if need_swap_pels(dm.DisplayOrientation, orientation):
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    dm.DisplayOrientation = orientation
    dm.Fields = win32con.DM_DISPLAYORIENTATION | win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    result = win32.ChangeDisplaySettingsEx(device.DeviceName, dm)
    return result
