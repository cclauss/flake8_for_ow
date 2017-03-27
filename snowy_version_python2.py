#!/usr/bin/env python2
# coding: utf-8

import sys

def main():
    s = ' '.join((u'❄ ☃ ❄', sys.version.split()[0], u'❄ ☃ ❄'))
    print(type(s))
    return {'snowy_version': s}

if __name__ == '__main__':
    main()
