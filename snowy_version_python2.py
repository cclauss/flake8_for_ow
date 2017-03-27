#!/usr/bin/env python2
import sys

if __name__ == '__main__':
    s = ' '.join((u'❄ ☃ ❄', sys.version.split()[0], u'❄ ☃ ❄'))
    print(type(s))
    print({'snowy_version': s})
