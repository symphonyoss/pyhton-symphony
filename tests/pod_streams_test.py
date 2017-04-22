#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Purpose:
        Unit Tests for Pod Methods related to Streams
            - adduser_to_stream
'''

__author__ = 'Matt Joyce'
__email__ = 'matt@joyce.nyc'
__copyright__ = 'Copyright 2017, Symphony Communication Services LLC'

import httpretty
import json
import unittest
import symphony


@httpretty.activate
class Pod_Users_tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Pod_Users_tests, self).__init__(*args, **kwargs)
        self.__uri__ = "http://fake.pod/"
        self.__session__ = "sessions"
        self.__keymngr__ = "keys"
        self.pod = symphony.Pod(self.__uri__, self.__session__, self.__keymngr__)

    def test_adduser_to_stream(self):
        ''' test adduser_to_stream '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + "pod/v1/room/stream_id/membership/add",
                               body='{ "format": "TEXT", "message": "Member added" }',
                               status=200,
                               content_type='text/json')
        # run test query
        status_code, response = self.pod.adduser_to_stream('stream_id', '123456')
        # verify return
        assert status_code == 200

    def test_create_stream(self):
        ''' test create_stream '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + 'pod/v1/im/create',
                               body='{ "id": "xhGxbTcvTDK6EIMMrwdOrX___quztr2HdA" }',
                               status=200,
                               content_type='text/json')
        status_code, response = self.pod.create_stream()
        assert status_code == 200
        response = json.loads(response)
        assert response['id'] == 'xhGxbTcvTDK6EIMMrwdOrX___quztr2HdA'

    def test_create_stream_ni(self):
        ''' test create_stream_ni '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + 'pod/v1/admin/im/create',
                               body='{ "id": "xhGxbTcvTDK6EIMMrwdOrX___quztr2HdA" }',
                               status=200,
                               content_type='text/json')
        userids = [123456, 567890]
        status_code, response = self.pod.create_stream_ni(userids)
        assert status_code == 200
        response = json.loads(response)
        assert response['id'] == 'xhGxbTcvTDK6EIMMrwdOrX___quztr2HdA'

    def test_create_room(self):
        ''' test create_room '''
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + 'pod/v2/room/create',
                               body='{ \
                                       "roomAttributes": { \
                                         "name": "API room", \
                                         "keywords": [ \
                                           { \
                                             "key": "region", \
                                             "value": "EMEA" \
                                           }, \
                                           { \
                                             "key": "lead", \
                                             "value": "Bugs Bunny" \
                                           } \
                                         ], \
                                         "description": "Created via the API", \
                                         "membersCanInvite": true, \
                                         "discoverable": true, \
                                         "readOnly": false, \
                                         "copyProtected": false, \
                                         "public": false \
                                       }, \
                                       "roomSystemInfo": { \
                                         "id": "w7-C9e34O4EqJJoXnyXLMH___qsIFLKEdA", \
                                         "creationDate": 1464448273802, \
                                         "createdByUserId": 7215545078229, \
                                         "active": true \
                                       } \
                                     }',
                               status=200,
                               content_type='text/json')
        room_data = {
                      "name": "API room",
                      "description": "Created via the API",
                      "keywords": [
                                     {"key": "region", "value": "EMEA"},
                                     {"key": "lead", "value": "Bugs Bunny"}
                      ],
                      "membersCanInvite": True,
                      "discoverable": True,
                      "public": False,
                      "readOnly": False,
                      "copyProtected": False
                    }
        status_code, response = self.pod.create_room(room_data)
        assert status_code == 200
        response = json.loads(response)
        assert response['id'] == 'xhGxbTcvTDK6EIMMrwdOrX___quztr2HdA'

    def test_update_room(self):
        ''' test update_room '''
        stream_id = 'w7-C9e34O4EqJJoXnyXLMH___qsIFLKEdA'
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + 'pod/v2/room/' + stream_id + '/update',
                               body='{ \
                                       "roomAttributes": { \
                                         "name": "API room v2", \
                                         "keywords": [ \
                                           { \
                                             "key": "region", \
                                             "value": "EMEA" \
                                           }, \
                                           { \
                                             "key": "lead", \
                                             "value": "Daffy Duck" \
                                           } \
                                         ], \
                                         "description": "Updated via the API", \
                                         "membersCanInvite": true, \
                                         "discoverable": true, \
                                         "readOnly": false, \
                                         "copyProtected": true, \
                                         "public": false \
                                       }, \
                                       "roomSystemInfo": { \
                                         "id": "w7-C9e34O4EqJJoXnyXLMH___qsIFLKEdA", \
                                         "creationDate": 1464448273802, \
                                         "createdByUserId": 7215545078229, \
                                         "active": true \
                                       } \
                                     }',
                               status=200,
                               content_type='text/json')
        room_data = {
                       "description": "Updated via the API",
                       "keywords": [
                                      {"key": "region", "value": "EMEA"},
                                      {"key": "lead", "value": "Daffy Duck"}
                                   ],
                       "copyProtected": True
                    }
        status_code, response = self.pod.update_room(stream_id, room_data)
        assert status_code == 200
        response = json.loads(response)
        assert response['id'] == 'xhGxbTcvTDK6EIMMrwdOrX___quztr2HdA'

    def test_room_info(self):
        ''' test room_info '''
        stream_id = 'w7-C9e34O4EqJJoXnyXLMH___qsIFLKEdA'
        # register response
        httpretty.register_uri(httpretty.GET, self.__uri__ + 'pod/v2/room/' + stream_id + '/info',
                               body='{ \
                                       "roomAttributes": { \
                                         "name": "API room v2", \
                                         "keywords": [ \
                                           { \
                                             "key": "region", \
                                             "value": "EMEA" \
                                           }, \
                                           { \
                                             "key": "lead", \
                                             "value": "Daffy Duck" \
                                           } \
                                         ], \
                                         "description": "Updated via the API", \
                                         "membersCanInvite": true, \
                                         "discoverable": true, \
                                         "readOnly": false, \
                                         "copyProtected": true, \
                                         "public": false \
                                       }, \
                                       "roomSystemInfo": { \
                                         "id": "w7-C9e34O4EqJJoXnyXLMH___qsIFLKEdA", \
                                         "creationDate": 1464448273802, \
                                         "createdByUserId": 7215545078229, \
                                         "active": true \
                                       } \
                                     }',
                               status=200,
                               content_type='text/json')
        status_code, response = self.pod.room_info(stream_id)
        response = json.loads(response)
        assert status_code == 200
        assert response['roomSystemInfo']['id'] == "w7-C9e34O4EqJJoXnyXLMH___qsIFLKEdA"

    def test_activate_room(self):
        ''' test activate_info '''
        stream_id = 'HNmksPVAR6-f14WqKXmqHX___qu8LMLgdA'
        status = False
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + 'pod/v1/room/' + stream_id + '/setActive',
                               body='{ \
                                       "roomAttributes": { \
                                         "name": "API room", \
                                         "description": "Updated via the API", \
                                         "membersCanInvite": true, \
                                         "discoverable": true \
                                       }, \
                                       "roomSystemInfo": { \
                                         "id": "HNmksPVAR6-f14WqKXmqHX___qu8LMLgdA", \
                                         "creationDate": 1461426797875, \
                                         "createdByUserId": 7078106103809, \
                                         "active": false \
                                       }, \
                                       "immutableRoomAttributes": { \
                                         "readOnly": false, \
                                         "copyProtected": false, \
                                         "public": false \
                                       } \
                                     }',
                               status=200,
                               content_type='text/json')
        status_code, response = self.pod.activate_room(stream_id, status)
        assert status_code == 200
        response = json.loads(response)
        assert response['roomSystemInfo']['id'] == "HNmksPVAR6-f14WqKXmqHX___qu8LMLgdA"
        assert response['roomSystemInfo']['active'] is False

    def test_room_members(self):
        ''' test room members '''
        stream_id = 'HNmksPVAR6-f14WqKXmqHX___qu8LMLgdA'
        # register response
        httpretty.register_uri(httpretty.POST, self.__uri__ + 'pod/v2/room/' + str(stream_id) + '/membership/list',
                               body='[ \
                                       { \
                                         "id": 7078106103900, \
                                         "owner": false, \
                                         "joinDate": 1461430710531 \
                                       }, \
                                       { \
                                         "id": 7078106103809, \
                                         "owner": true, \
                                         "joinDate": 1461426797875 \
                                       } \
                                     ]',
                               status=200,
                               content_type='text/json')
        status_code, response = self.pod.room_members(stream_id)
        assert status_code == 200
        response = json.loads(response)
        for member in response:
            if member['id'] == 7078106103900:
                assert member['owner'] is False


if __name__ == '__main__':
    unittest.main()