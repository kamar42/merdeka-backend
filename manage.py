#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # get environment
    if os.environ.has_key('LOCAL_DEV'):
        setting = "merdeka.settings.local"
    else:
        setting = "merdeka.settings.production"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
