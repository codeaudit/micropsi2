#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
Contains basic configuration information, especially path names to resource files
"""

__author__ = 'joscha'
__date__ = '03.12.12'

import os

VERSION = "0.2"

APPTITLE = "PSI Cortex"

RESOURCE_PATH = os.path.join(os.path.dirname(__file__), "resources")
DATA_PATH = os.path.join(os.path.dirname(__file__), "var")
USERMANAGER_PATH = os.path.join(RESOURCE_PATH, "user-db.json")

DEFAULT_PORT = 6543
DEFAULT_ADMIN_PORT = 6543
DEFAULT_API_PORT = 8080
DEFAULT_HOST = "localhost"
