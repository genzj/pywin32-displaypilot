# -*- encoding: utf-8 -*-
import sys


def has_pywin32():
    try:
        import win32api
        import win32con
    except ImportError:
        ok = False
    else:
        ok = True
    if not ok:
        print('pywin32 must be installed to use displaypilot', file=sys.stderr)
        sys.exit(99)


has_pywin32()
