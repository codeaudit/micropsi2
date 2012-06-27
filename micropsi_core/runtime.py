#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MicroPsi runtime component;
maintains a set of users, worlds (up to one per user), and agents, and provides an interface to external clients
"""

__author__ = 'joscha'
__date__ = '10.05.12'

# import nodenet
import world
import os

RESOURCE_PATH = os.path.join(os.path.dirname(__file__),"..","resources")

class MicroPsiRuntime(object):
    """The central component of the MicroPsi installation.

    The runtime instantiates a user manager, an agent manager and a world manager and coordinates the interaction
    between them. It must be a singleton, otherwise competing instances might conflict over the resource files.
    """

    def __init__(self):
        pass








def main():
    run = MicroPsiRuntime()

if __name__ == '__main__':
    main()