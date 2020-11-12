<<<<<<< HEAD
# -*- encoding: utf-8
# yapf: disable


checkname = 'ceph_df'


info = [[u'GLOBAL:'],
        [u'SIZE', u'AVAIL', u'RAW', u'USED', u'%RAW', u'USED', u'OBJECTS'],
        [u'873TiB', u'779TiB', u'94.2TiB', u'10.79', u'11.26M'],
        [u'POOLS:'],
        [u'NAME',
         u'ID',
         u'QUOTA',
         u'OBJECTS',
         u'QUOTA',
         u'BYTES',
         u'USED',
         u'%USED',
         u'MAX',
         u'AVAIL',
         u'OBJECTS',
         u'DIRTY',
         u'READ',
         u'WRITE',
         u'RAW',
         u'USED'],
        [u'.rgw.root',
         u'1',
         u'N/A',
         u'N/A',
         u'11.1KiB',
         u'0',
         u'242TiB',
         u'61',
         u'61',
         u'11.7KiB',
         u'219B',
         u'33.4KiB'],
        [u'default.rgw.control',
         u'2',
         u'N/A',
         u'N/A',
         u'0B',
         u'0',
         u'242TiB',
         u'8',
         u'8',
         u'0B',
         u'0B',
         u'0B'],
        [u'default.rgw.meta',
         u'3',
         u'N/A',
         u'N/A',
         u'73.6KiB',
         u'0',
         u'242TiB',
         u'252',
         u'252',
         u'257KiB',
         u'6.96KiB',
         u'221KiB'],
        [u'default.rgw.log',
         u'4',
         u'N/A',
         u'N/A',
         u'149B',
         u'0',
         u'242TiB',
         u'406',
         u'406',
         u'19.0MiB',
         u'12.7MiB',
         u'447B'],
        [u'rbd-rub.ec',
         u'5',
         u'N/A',
         u'N/A',
         u'19.4TiB',
         u'3.43',
         u'544TiB',
         u'5086154',
         u'5.09M',
         u'12B',
         u'292MiB',
         u'25.8TiB'],
        [u'rbd',
         u'6',
         u'N/A',
         u'N/A',
         u'21.5TiB',
         u'8.17',
         u'242TiB',
         u'5695802',
         u'5.70M',
         u'42.9MiB',
         u'403MiB',
         u'64.6TiB'],
        [u'ceph-bench',
         u'7',
         u'N/A',
         u'N/A',
         u'6.21GiB',
         u'0',
         u'242TiB',
         u'1591',
         u'1.59k',
         u'0B',
         u'3.11KiB',
         u'18.6GiB'],
        [u'rados-bench.ec',
         u'8',
         u'N/A',
         u'N/A',
         u'6.59GiB',
         u'0',
         u'544TiB',
         u'1684',
         u'1.68k',
         u'0B',
         u'3.29KiB',
         u'8.78GiB'],
        [u'rados-bench-ude.ec',
         u'9',
         u'N/A',
         u'N/A',
         u'6.60GiB',
         u'0',
         u'544TiB',
         u'1687',
         u'1.69k',
         u'0B',
         u'3.29KiB',
         u'8.80GiB'],
        [u'default.rgw.buckets.index',
         u'10',
         u'N/A',
         u'N/A',
         u'0B',
         u'0',
         u'242TiB',
         u'589',
         u'589',
         u'4.37MiB',
         u'59.4MiB',
         u'0B'],
        [u'default.rgw.buckets.data',
         u'11',
         u'N/A',
         u'N/A',
         u'425GiB',
         u'0.17',
         u'242TiB',
         u'465820',
         u'465.82k',
         u'420KiB',
         u'1.40MiB',
         u'1.25TiB'],
        [u'default.rgw.buckets.non-ec',
         u'12',
         u'N/A',
         u'N/A',
         u'0B',
         u'0',
         u'242TiB',
         u'5',
         u'5',
         u'339KiB',
         u'368KiB',
         u'0B'],
        [u'scbench',
         u'13',
         u'N/A',
         u'N/A',
         u'2.32GiB',
         u'0',
         u'242TiB',
         u'596',
         u'596',
         u'1B',
         u'2.05KiB',
         u'6.97GiB'],
        [u'rub-s3.ec',
         u'16',
         u'N/A',
         u'N/A',
         u'4.88KiB',
         u'0',
         u'272TiB',
         u'1000',
         u'1k',
         u'0B',
         u'1002B',
         u'6.51KiB']]


discovery = {'': [('SUMMARY', {}),
                  (u'.rgw.root', {}),
                  (u'ceph-bench', {}),
                  (u'default.rgw.buckets.data', {}),
                  (u'default.rgw.buckets.index', {}),
                  (u'default.rgw.buckets.non-ec', {}),
                  (u'default.rgw.control', {}),
                  (u'default.rgw.log', {}),
                  (u'default.rgw.meta', {}),
                  (u'rados-bench-ude.ec', {}),
                  (u'rados-bench.ec', {}),
                  (u'rbd', {}),
                  (u'rbd-rub.ec', {}),
                  (u'rub-s3.ec', {}),
                  (u'scbench', {})]}


checks = {'': [('SUMMARY',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '10.77% used (94.00 of 873.00 TB), trend: 0.00 B / 24 hours',
                  [('SUMMARY',
                    98566144.0,
                    732325478.4,
                    823866163.2,
                    0,
                    915406848.0),
                   ('fs_size', 915406848.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 38141952.0)])]),
               (u'.rgw.root',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0% used (11.10 kB of 242.00 TB), trend: 0.00 B / 24 hours',
                  [(u'.rgw.root',
                    0.010839849710464478,
                    203004313.60867187,
                    228379852.80975586,
                    0,
                    253755392.01083985),
                   ('fs_size', 253755392.01083985, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573141.333784994)])]),
               (u'ceph-bench',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0.003% used (6.21 GB of 242.01 TB), trend: 0.00 B / 24 hours',
                  [(u'ceph-bench',
                    6359.039999991655,
                    203009400.83200002,
                    228385575.936,
                    0,
                    253761751.04),
                   ('fs_size', 253761751.04, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573406.293333333)])]),
               (u'default.rgw.buckets.data',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0.17% used (425.00 GB of 242.42 TB), trend: 0.00 B / 24 hours',
                  [(u'default.rgw.buckets.data',
                    435200.0,
                    203352473.6,
                    228771532.8,
                    0,
                    254190592.0),
                   ('fs_size', 254190592.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10591274.666666666)])]),
               (u'default.rgw.buckets.index',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0% used (0.00 B of 242.00 TB), trend: 0.00 B / 24 hours',
                  [(u'default.rgw.buckets.index',
                    0.0,
                    203004313.6,
                    228379852.8,
                    0,
                    253755392.0),
                   ('fs_size', 253755392.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573141.333333334)])]),
               (u'default.rgw.buckets.non-ec',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0% used (0.00 B of 242.00 TB), trend: 0.00 B / 24 hours',
                  [(u'default.rgw.buckets.non-ec',
                    0.0,
                    203004313.6,
                    228379852.8,
                    0,
                    253755392.0),
                   ('fs_size', 253755392.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573141.333333334)])]),
               (u'default.rgw.control',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0% used (0.00 B of 242.00 TB), trend: 0.00 B / 24 hours',
                  [(u'default.rgw.control',
                    0.0,
                    203004313.6,
                    228379852.8,
                    0,
                    253755392.0),
                   ('fs_size', 253755392.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573141.333333334)])]),
               (u'default.rgw.log',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0% used (149.00 B of 242.00 TB), trend: 0.00 B / 24 hours',
                  [(u'default.rgw.log',
                    0.00014209747314453125,
                    203004313.6001137,
                    228379852.80012786,
                    0,
                    253755392.0001421),
                   ('fs_size', 253755392.0001421, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573141.333339253)])]),
               (u'default.rgw.meta',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0% used (73.60 kB of 242.00 TB), trend: 0.00 B / 24 hours',
                  [(u'default.rgw.meta',
                    0.07187500596046448,
                    203004313.6575,
                    228379852.8646875,
                    0,
                    253755392.071875),
                   ('fs_size', 253755392.071875, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573141.336328125)])]),
               (u'rados-bench-ude.ec',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0.001% used (6.60 GB of 544.01 TB), trend: 0.00 B / 24 hours',
                  [(u'rados-bench-ude.ec',
                    6758.399999976158,
                    456345681.92,
                    513388892.16,
                    0,
                    570432102.4),
                   ('fs_size', 570432102.4, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 23768004.266666666)])]),
               (u'rados-bench.ec',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0.001% used (6.59 GB of 544.01 TB), trend: 0.00 B / 24 hours',
                  [(u'rados-bench.ec',
                    6748.159999966621,
                    456345673.7279999,
                    513388882.94399995,
                    0,
                    570432092.16),
                   ('fs_size', 570432092.16, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 23768003.84)])]),
               (u'rbd',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '8.16% used (21.50 of 263.50 TB), trend: 0.00 B / 24 hours',
                  [(u'rbd', 22544384.0, 221039820.8, 248669798.4, 0, 276299776.0),
                   ('fs_size', 276299776.0, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 11512490.666666666)])]),
               (u'rbd-rub.ec',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '3.44% used (19.40 of 563.40 TB), trend: 0.00 B / 24 hours',
                  [(u'rbd-rub.ec',
                    20342374.399999976,
                    472614174.72,
                    531690946.56,
                    0,
                    590767718.4),
                   ('fs_size', 590767718.4, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 24615321.599999998)])]),
               (u'rub-s3.ec',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0% used (4.88 kB of 272.00 TB), trend: 0.00 B / 24 hours',
                  [(u'rub-s3.ec',
                    0.004765629768371582,
                    228170137.6038125,
                    256691404.80428904,
                    0,
                    285212672.0047656),
                   ('fs_size', 285212672.0047656, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 11883861.333531901)])]),
               (u'scbench',
                {'inodes_levels': (10.0, 5.0),
                 'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'show_inodes': 'onlow',
                 'show_levels': 'onmagic',
                 'show_reserved': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '0.0009% used (2.32 GB of 242.00 TB), trend: 0.00 B / 24 hours',
                  [(u'scbench',
                    2375.6800000071526,
                    203006214.14400002,
                    228381990.912,
                    0,
                    253757767.68),
                   ('fs_size', 253757767.68, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 10573240.32)])])]}
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
    ['873TiB', '779TiB', '94.2TiB', '10.79', '11.26M'], ['POOLS:'],
    [
        'NAME', 'ID', 'QUOTA', 'OBJECTS', 'QUOTA', 'BYTES', 'USED', '%USED',
        'MAX', 'AVAIL', 'OBJECTS', 'DIRTY', 'READ', 'WRITE', 'RAW', 'USED'
    ],
    [
        '.rgw.root', '1', 'N/A', 'N/A', '11.1KiB', '0', '242TiB', '61', '61',
        '11.7KiB', '219B', '33.4KiB'
    ],
    [
        'default.rgw.control', '2', 'N/A', 'N/A', '0B', '0', '242TiB', '8',
        '8', '0B', '0B', '0B'
    ],
    [
        'default.rgw.meta', '3', 'N/A', 'N/A', '73.6KiB', '0', '242TiB', '252',
        '252', '257KiB', '6.96KiB', '221KiB'
    ],
    [
        'default.rgw.log', '4', 'N/A', 'N/A', '149B', '0', '242TiB', '406',
        '406', '19.0MiB', '12.7MiB', '447B'
    ],
    [
        'rbd-rub.ec', '5', 'N/A', 'N/A', '19.4TiB', '3.43', '544TiB',
        '5086154', '5.09M', '12B', '292MiB', '25.8TiB'
    ],
    [
        'rbd', '6', 'N/A', 'N/A', '21.5TiB', '8.17', '242TiB', '5695802',
        '5.70M', '42.9MiB', '403MiB', '64.6TiB'
    ],
    [
        'ceph-bench', '7', 'N/A', 'N/A', '6.21GiB', '0', '242TiB', '1591',
        '1.59k', '0B', '3.11KiB', '18.6GiB'
    ],
    [
        'rados-bench.ec', '8', 'N/A', 'N/A', '6.59GiB', '0', '544TiB', '1684',
        '1.68k', '0B', '3.29KiB', '8.78GiB'
    ],
    [
        'rados-bench-ude.ec', '9', 'N/A', 'N/A', '6.60GiB', '0', '544TiB',
        '1687', '1.69k', '0B', '3.29KiB', '8.80GiB'
    ],
    [
        'default.rgw.buckets.index', '10', 'N/A', 'N/A', '0B', '0', '242TiB',
        '589', '589', '4.37MiB', '59.4MiB', '0B'
    ],
    [
        'default.rgw.buckets.data', '11', 'N/A', 'N/A', '425GiB', '0.17',
        '242TiB', '465820', '465.82k', '420KiB', '1.40MiB', '1.25TiB'
    ],
    [
        'default.rgw.buckets.non-ec', '12', 'N/A', 'N/A', '0B', '0', '242TiB',
        '5', '5', '339KiB', '368KiB', '0B'
    ],
    [
        'scbench', '13', 'N/A', 'N/A', '2.32GiB', '0', '242TiB', '596', '596',
        '1B', '2.05KiB', '6.97GiB'
    ],
    [
        'rub-s3.ec', '16', 'N/A', 'N/A', '4.88KiB', '0', '272TiB', '1000',
        '1k', '0B', '1002B', '6.51KiB'
    ]
]

discovery = {
    '': [
        ('.rgw.root', {}), ('SUMMARY', {}), ('ceph-bench', {}),
        ('default.rgw.buckets.data', {}), ('default.rgw.buckets.index', {}),
        ('default.rgw.buckets.non-ec', {}), ('default.rgw.control', {}),
        ('default.rgw.log', {}), ('default.rgw.meta', {}),
        ('rados-bench-ude.ec', {}), ('rados-bench.ec', {}), ('rbd', {}),
        ('rbd-rub.ec', {}), ('rub-s3.ec', {}), ('scbench', {})
    ]
}

checks = {
    '': [
        (
            'SUMMARY', {
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
                    0, '10.77% used (94.00 of 873.00 TB)', [
                        (
                            'fs_used', 98566144.0, 732325478.4, 823866163.2, 0,
                            915406848.0
                        ), ('fs_size', 915406848.0, None, None, None, None),
                        (
                            'fs_used_percent', 10.767468499427263, None, None,
                            None, None
                        )
                    ]
                )
            ]
        ),
        (
            '.rgw.root', {
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
                    0, '0% used (11.10 kB of 242.00 TB)', [
                        (
                            'fs_used', 0.010839849710464478,
                            203004313.60867187, 228379852.80975586, 0,
                            253755392.01083985
                        ),
                        (
                            'fs_size', 253755392.01083985, None, None, None,
                            None
                        ),
                        (
                            'fs_used_percent', 4.271771182699213e-09, None,
                            None, None, None
                        )
                    ]
                )
            ]
        ),
        (
            'ceph-bench', {
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
                    0, '0.003% used (6.21 GB of 242.01 TB)', [
                        (
                            'fs_used', 6359.039999991655, 203009400.83200002,
                            228385575.936, 0, 253761751.04
                        ), ('fs_size', 253761751.04, None, None, None, None),
                        (
                            'fs_used_percent', 0.0025059095682979, None, None,
                            None, None
                        )
                    ]
                )
            ]
        ),
        (
            'default.rgw.buckets.data', {
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
                    0, '0.17% used (425.00 GB of 242.42 TB)', [
                        (
                            'fs_used', 435200.0, 203352473.6, 228771532.8, 0,
                            254190592.0
                        ), ('fs_size', 254190592.0, None, None, None, None),
                        (
                            'fs_used_percent', 0.1712101130792441, None, None,
                            None, None
                        )
                    ]
                )
            ]
        ),
        (
            'default.rgw.buckets.index', {
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
                    0, '0% used (0.00 B of 242.00 TB)', [
                        (
                            'fs_used', 0.0, 203004313.6, 228379852.8, 0,
                            253755392.0
                        ), ('fs_size', 253755392.0, None, None, None, None),
                        ('fs_used_percent', 0.0, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            'default.rgw.buckets.non-ec', {
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
                    0, '0% used (0.00 B of 242.00 TB)', [
                        (
                            'fs_used', 0.0, 203004313.6, 228379852.8, 0,
                            253755392.0
                        ), ('fs_size', 253755392.0, None, None, None, None),
                        ('fs_used_percent', 0.0, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            'default.rgw.control', {
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
                    0, '0% used (0.00 B of 242.00 TB)', [
                        (
                            'fs_used', 0.0, 203004313.6, 228379852.8, 0,
                            253755392.0
                        ), ('fs_size', 253755392.0, None, None, None, None),
                        ('fs_used_percent', 0.0, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            'default.rgw.log', {
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
                    0, '0% used (149.00 B of 242.00 TB)', [
                        (
                            'fs_used', 0.00014209747314453125,
                            203004313.6001137, 228379852.80012786, 0,
                            253755392.0001421
                        ),
                        ('fs_size', 253755392.0001421, None, None, None, None),
                        (
                            'fs_used_percent', 5.5997814282681994e-11, None,
                            None, None, None
                        )
                    ]
                )
            ]
        ),
        (
            'default.rgw.meta', {
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
                    0, '0% used (73.60 kB of 242.00 TB)', [
                        (
                            'fs_used', 0.07187500596046448, 203004313.6575,
                            228379852.8646875, 0, 253755392.071875
                        ),
                        ('fs_size', 253755392.071875, None, None, None, None),
                        (
                            'fs_used_percent', 2.832452361844048e-08, None,
                            None, None, None
                        )
                    ]
                )
            ]
        ),
        (
            'rados-bench-ude.ec', {
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
                    0, '0.001% used (6.60 GB of 544.01 TB)', [
                        (
                            'fs_used', 6758.399999976158, 456345681.92,
                            513388892.16, 0, 570432102.4
                        ), ('fs_size', 570432102.4, None, None, None, None),
                        (
                            'fs_used_percent', 0.0011847860545613218, None,
                            None, None, None
                        )
                    ]
                )
            ]
        ),
        (
            'rados-bench.ec', {
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
                    0, '0.001% used (6.59 GB of 544.01 TB)', [
                        (
                            'fs_used', 6748.159999966621, 456345673.7279999,
                            513388882.94399995, 0, 570432092.16
                        ), ('fs_size', 570432092.16, None, None, None, None),
                        (
                            'fs_used_percent', 0.0011829909454101745, None,
                            None, None, None
                        )
                    ]
                )
            ]
        ),
        (
            'rbd', {
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
                    0, '8.16% used (21.50 of 263.50 TB)', [
                        (
                            'fs_used', 22544384.0, 221039820.8, 248669798.4, 0,
                            276299776.0
                        ), ('fs_size', 276299776.0, None, None, None, None),
                        (
                            'fs_used_percent', 8.159392789373815, None, None,
                            None, None
                        )
                    ]
                )
            ]
        ),
        (
            'rbd-rub.ec', {
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
                    0, '3.44% used (19.40 of 563.40 TB)', [
                        (
                            'fs_used', 20342374.399999976, 472614174.72,
                            531690946.56, 0, 590767718.4
                        ), ('fs_size', 590767718.4, None, None, None, None),
                        (
                            'fs_used_percent', 3.443379481718136, None, None,
                            None, None
                        )
                    ]
                )
            ]
        ),
        (
            'rub-s3.ec', {
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
                    0, '0% used (4.88 kB of 272.00 TB)', [
                        (
                            'fs_used', 0.004765629768371582, 228170137.6038125,
                            256691404.80428904, 0, 285212672.0047656
                        ),
                        ('fs_size', 285212672.0047656, None, None, None, None),
                        (
                            'fs_used_percent', 1.6709039380592294e-09, None,
                            None, None, None
                        )
                    ]
                )
            ]
        ),
        (
            'scbench', {
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
                    0, '0.0009% used (2.32 GB of 242.00 TB)', [
                        (
                            'fs_used', 2375.6800000071526, 203006214.14400002,
                            228381990.912, 0, 253757767.68
                        ), ('fs_size', 253757767.68, None, None, None, None),
                        (
                            'fs_used_percent', 0.0009361999129039439, None,
                            None, None, None
                        )
                    ]
                )
            ]
        )
    ]
}
>>>>>>> upstream/master
