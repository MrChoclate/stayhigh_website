#!/usr/bin/env python
# coding: utf-8

import os, errno
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hoc.settings")

from subprocess import call

from index.models import *

from django.contrib.auth.models import User

import django


def main():
    call(["./manage.py", "syncdb"])
    django.setup()
    createTestUser()

def createTestUser():
    User.objects.create_superuser(username="admin", email="admin@private.fr", password="tmp")

if __name__ == '__main__':
    main()
