<<<<<<< HEAD
# -*- encoding: utf-8
# yapf: disable

checkname = 'ceph_df'

info = [
    [u'GLOBAL:'],
    [u'SIZE', u'AVAIL', u'RAW', u'USED', u'%RAW', u'USED', u'OBJECTS'],
    [u'253', u'GiB', u'245', u'GiB', u'7.8', u'GiB', u'3.10', u'839'],
    [u'POOLS:'],
    [
        u'NAME', u'ID', u'QUOTA', u'OBJECTS', u'QUOTA', u'BYTES', u'USED',
        u'%USED', u'MAX', u'AVAIL', u'OBJECTS', u'DIRTY', u'READ', u'WRITE',
        u'RAW', u'USED'
    ],
    [
        u'cephfs_data', u'1', u'N/A', u'N/A', u'1.6', u'GiB', u'1.97', u'77',
        u'GiB', u'809', u'809', u'33', u'B', u'177', u'KiB', u'4.7', u'GiB'
    ],
    [
        u'cephfs_metadata', u'2', u'N/A', u'N/A', u'32', u'MiB', u'0.04',
        u'77', u'GiB', u'30', u'30', u'407', u'B', u'14', u'KiB', u'95', u'MiB'
=======
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore
checkname = 'ceph_df'

info = [
    ['GLOBAL:'], ['SIZE', 'AVAIL', 'RAW', 'USED', '%RAW', 'USED', 'OBJECTS'],
    ['253', 'GiB', '245', 'GiB', '7.8', 'GiB', '3.10', '839'], ['POOLS:'],
    [
        'NAME', 'ID', 'QUOTA', 'OBJECTS', 'QUOTA', 'BYTES', 'USED', '%USED',
        'MAX', 'AVAIL', 'OBJECTS', 'DIRTY', 'READ', 'WRITE', 'RAW', 'USED'
    ],
    [
        'cephfs_data', '1', 'N/A', 'N/A', '1.6', 'GiB', '1.97', '77', 'GiB',
        '809', '809', '33', 'B', '177', 'KiB', '4.7', 'GiB'
    ],
    [
        'cephfs_metadata', '2', 'N/A', 'N/A', '32', 'MiB', '0.04', '77', 'GiB',
        '30', '30', '407', 'B', '14', 'KiB', '95', 'MiB'
>>>>>>> upstream/master
    ]
]

discovery = {
<<<<<<< HEAD
    '': [('SUMMARY', {}), (u'cephfs_data', {}), (u'cephfs_metadata', {})]
=======
    '': [('SUMMARY', {}), ('cephfs_data', {}), ('cephfs_metadata', {})]
>>>>>>> upstream/master
}

checks = {
    '': [
        (
            'SUMMARY', {
<<<<<<< HEAD
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0,
                    '3.16% used (8.00 of 253.00 GB), trend: 0.00 B / 24 hours',
                    [
                        ('SUMMARY', 8192.0, 207257.6, 233164.8, 0, 259072.0),
                        ('fs_size', 259072.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 10794.666666666666)
=======
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'show_inodes': 'onlow',
                'show_reserved': False
            }, [
                (
                    0, '3.16% used (8.00 of 253.00 GB)', [
                        ('fs_used', 8192.0, 207257.6, 233164.8, 0, 259072.0),
                        ('fs_size', 259072.0, None, None, None, None),
                        (
                            'fs_used_percent', 3.1620553359683794, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'cephfs_data', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0,
                    '2.04% used (1.60 of 78.60 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'cephfs_data', 1638.3999999999942, 64389.12,
                            72437.76, 0, 80486.4
                        ), ('fs_size', 80486.4, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 3353.6)
=======
            'cephfs_data', {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'show_inodes': 'onlow',
                'show_reserved': False
            }, [
                (
                    0, '2.04% used (1.60 of 78.60 GB)', [
                        (
                            'fs_used', 1638.3999999999942, 64389.12, 72437.76,
                            0, 80486.4
                        ), ('fs_size', 80486.4, None, None, None, None),
                        (
                            'fs_used_percent', 2.035623409669204, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'cephfs_metadata', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (
                    0,
                    '0.04% used (32.00 MB of 77.03 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'cephfs_metadata', 32.0, 63104.0, 70992.0, 0,
                            78880.0
                        ), ('fs_size', 78880.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 3286.6666666666665)
=======
            'cephfs_metadata', {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'show_inodes': 'onlow',
                'show_reserved': False
            }, [
                (
                    0, '0.04% used (32.00 MB of 77.03 GB)', [
                        ('fs_used', 32.0, 63104.0, 70992.0, 0, 78880.0),
                        ('fs_size', 78880.0, None, None, None, None),
                        (
                            'fs_used_percent', 0.04056795131845842, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        )
    ]
}
