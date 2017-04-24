#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Agent API Methods
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2016, Symphony Communication Services LLC'

import unicodedata


class Messaging(object):

    def __init__(self, *args, **kwargs):
        super(Messaging, self).__init__(*args, **kwargs)

    def remove_control_characters(self, s):
        return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

    def messages(self, stream_id, since=1000000000):
        ''' get messages from stream_id '''
        req_hook = 'agent/v2/stream/' + stream_id + '/message?since=' + str(since)
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def get_attachment(self, stream_id, message_id, file_id):
        ''' get attachement '''
        req_hook = 'agent/v1/stream/' + str(stream_id) + '/attachment?\
                    messageId=' + str(message_id) + '&\
                    fileId=' + str(file_id)
        req_args = None
        status_code, response = self.__rest__.GET_query(req_hook, req_args)
        return status_code, response

    def create_attachment(self, stream_id):
        ''' create attachment '''
        req_hook = 'agent/v1/stream/' + str(stream_id) + '/attachment/create'
        req_args = None
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response

    def send_message(self, stream_id, msgFormat, message):
        ''' send message to threadid/stream '''
        req_hook = 'agent/v2/stream/' + stream_id + '/message/create'
        req_args = '{ "format": "%s", "message": "'"%s"'" }' % (msgFormat, message)
        status_code, response = self.__rest__.POST_query(req_hook, req_args)
        return status_code, response
