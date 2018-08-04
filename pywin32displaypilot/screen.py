# -*- encoding: utf-8 -*-
import logging
import win32api as win32

import pywintypes
import win32con

L = logging.getLogger(__name__)


def get_monitors(device):
    ans = []
    while True:
        try:
            monitor = win32.EnumDisplayDevices(device.DeviceName, len(ans))
            ans.append(monitor)
            L.debug("+-- %s (%s) 0x%08x", monitor.DeviceString, monitor.DeviceName, monitor.StateFlags)
        except pywintypes.error:
            break
    return ans


def all_screens(filter_connected=True):
    ans = []
    i = 0
    while True:
        try:
            device = win32.EnumDisplayDevices(None, i)

            L.debug("[%d] %s (%s) 0x%08x", i, device.DeviceString, device.DeviceName, device.StateFlags)
            if not filter_connected or bool(device.StateFlags & win32con.DISPLAY_DEVICE_ATTACHED_TO_DESKTOP):
                if device.StateFlags & win32con.DISPLAY_DEVICE_PRIMARY_DEVICE:
                    ans.insert(0, (device, get_monitors(device)))
                else:
                    ans.append((device, get_monitors(device)))
            i += 1
        except pywintypes.error:
            break
    return ans

