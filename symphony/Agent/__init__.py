#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'


import symphony

from base import Realtime
from base import Messaging


class Agent(Realtime, Messaging):

    def __init__(self, url, session, keymngr):
        self.__url__ = url
        self.__session__ = session
        self.__keymngr__ = keymngr
        self.__rest__ = symphony.RESTful(self.__url__, self.__session__, self.__keymngr__)
