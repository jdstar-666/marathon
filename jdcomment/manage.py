#!/usr/bin/env python
#-*- coding:utf8 -*-
# @Author: lisnb
# @Date:   2016-07-27T13:54:19+08:00
# @Email:  lisnb.h@hotmail.com
# @Last modified by:   lisnb
# @Last modified time: 2016-07-27T18:32:45+08:00



#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jdcomment.settings")
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
