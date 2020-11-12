<<<<<<< HEAD
# yapf: disable
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

>>>>>>> upstream/master


checkname = 'ibm_svc_portfc'


info = [[u'0',
         u'1',
         u'1',
         u'fc',
         u'8Gb',
         u'1',
         u'node1',
         u'5005076803042126',
         u'030400',
         u'active',
         u'switch'],
        [u'1',
         u'2',
         u'2',
         u'fc',
         u'8Gb',
         u'1',
         u'node1',
         u'5005076803082126',
         u'040400',
         u'active',
         u'switch',
         u'local_partner'],
        [u'2',
         u'3',
         u'3',
         u'fc',
         u'N/A',
         u'1',
         u'node1',
         u'50050768030C2126',
         u'000000',
         u'inactive_unconfigured',
         u'none'],
        [u'3',
         u'4',
         u'4',
         u'fc',
         u'N/A',
         u'1',
         u'node1',
         u'5005076803102126',
         u'000000',
         u'inactive_unconfigured',
         u'none'],
        [u'8',
         u'1',
         u'1',
         u'fc',
         u'8Gb',
         u'2',
         u'node2',
         u'5005076803042127',
         u'030500',
         u'active',
         u'switch',
         u'local_partner'],
        [u'9',
         u'2',
         u'2',
         u'fc',
         u'8Gb',
         u'2',
         u'node2',
         u'5005076803082127',
         u'040500',
         u'active',
         u'switch'],
        [u'10',
         u'3',
         u'3',
         u'fc',
         u'N/A',
         u'2',
         u'node2',
         u'50050768030C2127',
         u'000000',
         u'inactive_unconfigured',
         u'none'],
        [u'11',
         u'4',
         u'4',
         u'fc',
         u'N/A',
         u'2',
         u'node2',
         u'5005076803102127',
         u'000000',
         u'inactive_unconfigured',
         u'none',
         u'local_partner']]


discovery = {'': [(u'Port 0', None),
                  (u'Port 1', None),
                  (u'Port 8', None),
                  (u'Port 9', None)]}


checks = {'': [(u'Port 0',
                {},
                [(0, u'Status: active, Speed: 8Gb, WWPN: 5005076803042126', [])]),
               (u'Port 1',
                {},
                [(0, u'Status: active, Speed: 8Gb, WWPN: 5005076803082126', [])]),
               (u'Port 8',
                {},
                [(0, u'Status: active, Speed: 8Gb, WWPN: 5005076803042127', [])]),
               (u'Port 9',
                {},
<<<<<<< HEAD
                [(0, u'Status: active, Speed: 8Gb, WWPN: 5005076803082127', [])])]}
=======
                [(0, u'Status: active, Speed: 8Gb, WWPN: 5005076803082127', [])])]}
>>>>>>> upstream/master
