# -*- encoding: utf-8 -*-
import argparse
import sys
import win32con

from pywin32displaypilot.screen import all_screens
from pywin32displaypilot.setting import set_display_orientation

DEGREE_TO_ENUM = {
    '0': win32con.DMDO_DEFAULT,
    '90': win32con.DMDO_90,
    '180': win32con.DMDO_180,
    '270': win32con.DMDO_270,
}


def degree_enum(d):
    if not d:
        return None

    try:
        return DEGREE_TO_ENUM[d.strip()]
    except KeyError:
        raise ValueError('degree must be 0, 90, 180 or 270')


def get_parser():
    parser = argparse.ArgumentParser(
        'displaypilot',
        description='change windows monitor orientation'
    )
    parser.add_argument('-d', '--debug', action='store_true', help='show debug loggings')
    parser.add_argument('-l', '--list', action='store_true', help='list connected monitors then exit')
    parser.add_argument('-s', '--screen', type=int, default=0,
                        help='monitor to be set, omit to set the primary monitor')
    parser.add_argument('orientation', type=degree_enum, help='orientation to be set', nargs='?')
    return parser


def main(args):
    parser = get_parser()
    args = parser.parse_args(args)

    if args.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)

    screens = all_screens()

    if args.list:
        for idx, s in enumerate(screens):
            print('%d - %s connected to %s' % (idx, s[1][0].DeviceString, s[0].DeviceString))

        return 0

    if args.orientation is None:
        print('argument ORIENTATION is required unless in list mode', file=sys.stderr)
        parser.print_usage(sys.stderr)
        return 1

    result = set_display_orientation(screens[args.screen][0], orientation=args.orientation)
    if result < 0:
        result = 100 + abs(result)
    return result


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
