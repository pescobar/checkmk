<<<<<<< HEAD
# yapf: disable
checkname = 'df'

info = [
    [u'/dev/sda4', u'ext4', u'143786696', u'101645524', u'34814148', u'75%', u'/'],
    [u'/dev/sda2', u'ext4', u'721392', u'151120', u'517808', u'23%', u'/boot'],
    [u'[df_inodes_start]'],
    [u'/dev/sda4', u'ext4', u'9142272', u'1654272', u'7488000', u'19%', u'/'],
    [u'/dev/sda2', u'ext4', u'46848', u'304', u'46544', u'1%', u'/boot'],
    [u'[df_inodes_end]'],
]

discovery = {'': [(u'/', {}), (u'/boot', {})]}


checks = {
    '': [
         (u'/', {'trend_range': 24, 'show_levels': 'onmagic', 'inodes_levels': (10.0, 5.0), 'magic_normsize': 20, 'show_inodes': 'onlow', 'levels': (80.0, 90.0), 'show_reserved': False, 'levels_low': (50.0, 60.0), 'trend_perfdata': True},
             [(0, '75.79% used (103.92 of 137.13 GB), trend: 0.00 B / 24 hours',
                 [(u'/', 106418.50390625, 112333.35625, 126375.02578125, 0, 140416.6953125),
                  ('fs_size', 140416.6953125, None, None, None, None),
                  ('growth', 0.0, None, None, None, None),
                  ('trend', 0, None, None, 0, 5850.695638020833),
                  ('inodes_used', 1654272, 8228044.8, 8685158.4, 0, 9142272),
                 ]
              ),
             ]
         ),
         (u'/dev/sda4 /', {'trend_range': 24, 'show_levels': 'onmagic', 'inodes_levels': (10.0, 5.0), 'magic_normsize': 20, 'show_inodes': 'onlow', 'levels': (80.0, 90.0), 'show_reserved': False, 'levels_low': (50.0, 60.0), 'trend_perfdata': True},
             [(0, '75.79% used (103.92 of 137.13 GB), trend: 0.00 B / 24 hours',
                 [(u'/', 106418.50390625, 112333.35625, 126375.02578125, 0, 140416.6953125),
                  ('fs_size', 140416.6953125, None, None, None, None),
                  ('growth', 0.0, None, None, None, None),
                  ('trend', 0, None, None, 0, 5850.695638020833),
                  ('inodes_used', 1654272, 8228044.8, 8685158.4, 0, 9142272),
                 ]
              ),
             ]
         ),
         (u'/dev/sda4 /', {'trend_range': 24, 'show_levels': 'onmagic', 'inodes_levels': (10.0, 5.0), 'magic_normsize': 20, 'show_inodes': 'onlow', 'levels': (80.0, 90.0), 'show_reserved': True, 'subtract_reserved': True, 'levels_low': (50.0, 60.0), 'trend_perfdata': True,},
             [(0, '74.49% used (96.94 of 130.14 GB), additionally reserved for root: 6.99 GB,' \
                  ' trend: 0.00 B / 24 hours',
                 [(u'/', 99263.20703125, 112333.35625, 126375.02578125, 0, 140416.6953125),
                  ('fs_size', 140416.6953125, None, None, None, None),
                  ('fs_free', 33998.19140625, None, None, 0, 140416.6953125),
                  ('reserved', 7155.296875, None, None, None, None),
                  ('growth', 0.0, None, None, None, None),
                  ('trend', 0, None, None, 0, 5850.695638020833),
                  ('inodes_used', 1654272, 8228044.8, 8685158.4, 0, 9142272),
                 ]
              ),
             ]
         ),
         (u'/', {'trend_range': 24, 'show_levels': 'onmagic', 'inodes_levels': (10.0, 5.0), 'magic_normsize': 20, 'show_inodes': 'onlow', 'levels': (80.0, 90.0), 'show_reserved': True, 'levels_low': (50.0, 60.0), 'trend_perfdata': True},
             [(0, '75.79% used (103.92 of 137.13 GB), therein reserved for root: 5.1% (6.99 GB),' \
                  ' trend: 0.00 B / 24 hours',
                 [(u'/', 106418.50390625, 112333.35625, 126375.02578125, 0, 140416.6953125),
                  ('fs_size', 140416.6953125, None, None, None, None),
                  ('reserved', 7155.296875, None, None, None, None),
                  ('growth', 0.0, None, None, None, None),
                  ('trend', 0, None, None, 0, 5850.695638020833),
                  ('inodes_used', 1654272, 8228044.8, 8685158.4, 0, 9142272),
                 ]
              ),
             ]
         ),
         (u'/dev/sda4 /', {'trend_range': 24, 'show_levels': 'onmagic', 'inodes_levels': (10.0, 5.0), 'magic_normsize': 20, 'show_inodes': 'onlow', 'levels': (80.0, 90.0), 'show_reserved': True, 'levels_low': (50.0, 60.0), 'trend_perfdata': True},
             [(0, '75.79% used (103.92 of 137.13 GB), therein reserved for root: 5.1% (6.99 GB),' \
                  ' trend: 0.00 B / 24 hours',
                 [(u'/', 106418.50390625, 112333.35625, 126375.02578125, 0, 140416.6953125),
                  ('fs_size', 140416.6953125, None, None, None, None),
                  ('reserved', 7155.296875, None, None, None, None),
                  ('growth', 0.0, None, None, None, None),
                  ('trend', 0, None, None, 0, 5850.695638020833),
                  ('inodes_used', 1654272, 8228044.8, 8685158.4, 0, 9142272),
                 ]
              ),
             ]
         ),
         (u'/home', {'trend_range': 24, 'show_levels': 'onmagic', 'inodes_levels': (10.0, 5.0), 'magic_normsize': 20, 'show_inodes': 'onlow', 'levels': (80.0, 90.0), 'show_reserved': False, 'levels_low': (50.0, 60.0), 'trend_perfdata': True},
             []
         ),
         (u'/', {'inodes_levels': (90.0, 5.0), 'show_inodes': 'onlow'},
             [(1, '75.79% used (103.92 of 137.13 GB), trend: 0.00 B / 24 hours, ' \
                  'Inodes Used: 18.09% (warn/crit at 10.0%/95.0%), inodes available: 7.49 M/81.91%',
                 [(u'/', 106418.50390625, 112333.35625, 126375.02578125, 0, 140416.6953125),
                  ('fs_size', 140416.6953125, None, None, None, None),
                  ('growth', 0.0, None, None, None, None),
                  ('trend', 0, None, None, 0, 5850.695638020833),
                  ('inodes_used', 1654272, 914227.2000000001, 8685158.4, 0, 9142272),
                 ]
              ),
             ]
         ),
         (u'/', {'inodes_levels': (8542272, 8142272), 'show_inodes': 'onlow'},
             [(2, '75.79% used (103.92 of 137.13 GB), trend: 0.00 B / 24 hours, ' \
                  'Inodes Used: 1.65 M (warn/crit at 600.00 k/1.00 M), inodes available: 7.49 M/81.91%',
                 [(u'/', 106418.50390625, 112333.35625, 126375.02578125, 0, 140416.6953125),
                  ('fs_size', 140416.6953125, None, None, None, None),
                  ('growth', 0.0, None, None, None, None),
                  ('trend', 0, None, None, 0, 5850.695638020833),
                  ('inodes_used', 1654272, 600000.0, 1000000.0, 0, 9142272),
                 ]
              ),
             ]
         ),
         (u'all', {"patterns": ['*']},
          [(0, '75.55% used (104.12 of 137.81 GB), trend: 0.00 B / 24 hours (2 filesystems)',
            [(u'all', 106617.31640625, 112896.94375, 127009.06171875, 0, 141121.1796875),
             ('fs_size', 141121.1796875, None, None, None, None),
             ('growth', 0.0, None, None, None, None),
             ('trend', 0, None, None, 0, 5880.049153645833),
             ('inodes_used', 1654576, None, None, 0, 9189120)])]
         ),
         (u'parts', {"patterns": ['*oot', '/']},
          [(0, '75.55% used (104.12 of 137.81 GB), trend: 0.00 B / 24 hours (2 filesystems)',
            [(u'parts', 106617.31640625, 112896.94375, 127009.06171875, 0, 141121.1796875),
             ('fs_size', 141121.1796875, None, None, None, None),
             ('growth', 0.0, None, None, None, None),
             ('trend', 0, None, None, 0, 5880.049153645833),
             ('inodes_used', 1654576, None, None, 0, 9189120)])]
         ),
        ]
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore
checkname = 'df'

info = [
    ['/dev/sda4', 'ext4', '143786696', '101645524', '34814148', '75%', '/'],
    ['/dev/sda2', 'ext4', '721392', '151120', '517808', '23%', '/boot'],
    ['[df_inodes_start]'],
    ['/dev/sda4', 'ext4', '9142272', '1654272', '7488000', '19%', '/'],
    ['/dev/sda2', 'ext4', '46848', '304', '46544', '1%', '/boot'],
    ['[df_inodes_end]'],
]

discovery = {
    '': [
        (
            '/',
            {
                'include_volume_name': False
            },
        ),
        (
            '/boot',
            {
                'include_volume_name': False
            },
        ),
    ]
}

checks = {
    '': [
        (
            '/',
            {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            },
            [
                (
                    0,
                    '75.79% used (103.92 of 137.13 GB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 75.78764310712029, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/dev/sda4 /',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': False,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    '75.79% used (103.92 of 137.13 GB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 75.78764310712029, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/dev/sda4 /',
            {
                'show_inodes': 'onlow',
                'subtract_reserved': True,
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': True,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    '74.49% used (96.94 of 130.14 GB), additionally reserved for root: 6.99 GB',
                    [
                        ('fs_used', 99263.20703125, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 70.69188376092876, None, None, None, None),
                        ('fs_free', 33998.19140625, None, None, 0, 140416.6953125),
                        ('reserved', 7155.296875, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': True,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    '75.79% used (103.92 of 137.13 GB), therein reserved for root: 5.1% (6.99 GB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 75.78764310712029, None, None, None, None),
                        ('reserved', 7155.296875, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/dev/sda4 /',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': True,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [
                (
                    0,
                    '75.79% used (103.92 of 137.13 GB), therein reserved for root: 5.1% (6.99 GB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 75.78764310712029, None, None, None, None),
                        ('reserved', 7155.296875, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/home',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (10.0, 5.0),
                'trend_range': 24,
                'show_reserved': False,
                'show_levels': 'onmagic',
                'trend_perfdata': True,
                'levels_low': (50.0, 60.0),
                'levels': (80.0, 90.0),
                'magic_normsize': 20
            },
            [],
        ),
        (
            '/',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (90.0, 5.0)
            },
            [
                (
                    0,
                    '75.79% used (103.92 of 137.13 GB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 75.78764310712029, None, None, None, None),
                    ],
                ),
                (
                    1,
                    'Inodes used: 18.1% (warn/crit at 10.0%/95.0%), Inodes available: 7,488,000 (81.9%)',
                    [
                        ('inodes_used', 1654272, 914227.2000000001, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/',
            {
                'show_inodes': 'onlow',
                'inodes_levels': (8542272, 8142272)
            },
            [
                (
                    0,
                    '75.79% used (103.92 of 137.13 GB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 75.78764310712029, None, None, None, None),
                    ],
                ),
                (
                    2,
                    'Inodes used: 1,654,272 (warn/crit at 600,000/1,000,000), Inodes available: 7,488,000 (81.9%)',
                    [
                        ('inodes_used', 1654272, 600000.0, 1000000.0, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            'all',
            {
                'patterns': (['*'], []),
            },
            [
                (
                    0,
                    '75.55% used (104.12 of 137.81 GB)',
                    [
                        ('fs_used', 106617.31640625, 112896.94375, 127009.06171875, 0,
                         141121.1796875),
                        ('fs_size', 141121.1796875, None, None, None, None),
                        ('fs_used_percent', 75.55018788982939, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654576, None, None, 0.0, 9189120.0),
                    ],
                ),
                (
                    0,
                    '2 filesystems',
                    [],
                ),
            ],
        ),
        (
            'parts',
            {
                'patterns': (['*oot', '/'], []),
            },
            [
                (
                    0,
                    '75.55% used (104.12 of 137.81 GB)',
                    [
                        ('fs_used', 106617.31640625, 112896.94375, 127009.06171875, 0,
                         141121.1796875),
                        ('fs_size', 141121.1796875, None, None, None, None),
                        ('fs_used_percent', 75.55018788982939, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654576, None, None, 0.0, 9189120.0),
                    ],
                ),
                (
                    0,
                    '2 filesystems',
                    [],
                ),
            ],
        ),
        (
            '/boot',
            {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            },
            [
                (
                    0,
                    '28.22% used (198.81 of 704.48 MB)',
                    [
                        ('fs_used', 198.8125, 563.5875, 634.0359375, 0, 704.484375),
                        ('fs_size', 704.484375, None, None, None, None),
                        ('fs_used_percent', 28.22099496528933, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 304, 42163.200000000004, 44505.6, 0.0, 46848.0),
                    ],
                ),
            ],
        ),
        (
            '/',
            {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'show_inodes': 'onlow',
                'show_reserved': False,
                'include_volume_name': False
            },
            [
                (
                    0,
                    '75.79% used (103.92 of 137.13 GB)',
                    [
                        ('fs_used', 106418.50390625, 112333.35625, 126375.02578125, 0,
                         140416.6953125),
                        ('fs_size', 140416.6953125, None, None, None, None),
                        ('fs_used_percent', 75.78764310712029, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 1654272, 8228044.8, 8685158.4, 0.0, 9142272.0),
                    ],
                ),
            ],
        ),
        (
            '/boot',
            {
                'levels': (80.0, 90.0),
                'magic_normsize': 20,
                'levels_low': (50.0, 60.0),
                'trend_range': 24,
                'trend_perfdata': True,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'show_inodes': 'onlow',
                'show_reserved': False,
                'include_volume_name': False
            },
            [
                (
                    0,
                    '28.22% used (198.81 of 704.48 MB)',
                    [
                        ('fs_used', 198.8125, 563.5875, 634.0359375, 0, 704.484375),
                        ('fs_size', 704.484375, None, None, None, None),
                        ('fs_used_percent', 28.22099496528933, None, None, None, None),
                    ],
                ),
                (
                    0,
                    '',
                    [
                        ('inodes_used', 304, 42163.200000000004, 44505.6, 0.0, 46848.0),
                    ],
                ),
            ],
        )
    ]
>>>>>>> upstream/master
}
