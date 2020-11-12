<<<<<<< HEAD
# -*- encoding: utf-8
# yapf: disable

checkname = 'ceph_df'

info = [
    [u'GLOBAL:'],
    [u'SIZE', u'AVAIL', u'RAW', u'USED', u'%RAW', u'USED', u'OBJECTS'],
    [u'200T', u'186T', u'13808G', u'6.74', u'8774k'], [u'POOLS:'],
    [
        u'NAME', u'ID', u'CATEGORY', u'QUOTA', u'OBJECTS', u'QUOTA', u'BYTES',
        u'USED', u'%USED', u'MAX', u'AVAIL', u'OBJECTS', u'DIRTY', u'READ',
        u'WRITE', u'RAW', u'USED'
    ],
    [
        u'seafile-commits', u'33', u'-', u'N/A', u'N/A', u'276M', u'0.04',
        u'744G', u'506506', u'494k', u'315k', u'496k', u'829M'
    ],
    [
        u'seafile-blocks', u'35', u'-', u'N/A', u'N/A', u'685G', u'0.56',
        u'119T', u'879162', u'858k', u'891k', u'1168k', u'1027G'
    ],
    [
        u'seafile-fs', u'36', u'-', u'N/A', u'N/A', u'11412M', u'1.47',
        u'744G', u'2502095', u'2443k', u'5782k', u'2660k', u'34237M'
    ],
    [
        u'seafile-blocks-cache', u'37', u'-', u'N/A', u'200G', u'149G',
        u'16.69', u'744G', u'198252', u'96433', u'5105k', u'1944k', u'447G'
    ],
    [
        u'rbd', u'49', u'-', u'N/A', u'N/A', u'3106G', u'2.47', u'119T',
        u'795700', u'777k', u'16212k', u'14942k', u'4660G'
    ],
    [
        u'rbd-cache', u'50', u'-', u'N/A', u'N/A', u'40652M', u'5.06', u'744G',
        u'10173', u'3565', u'50513k', u'558M', u'119G'
    ],
    [
        u'cephfs01_meta', u'53', u'-', u'N/A', u'N/A', u'131M', u'0.02',
        u'744G', u'24170', u'24170', u'30172', u'14199k', u'393M'
    ],
    [
        u'cephfs01', u'54', u'-', u'N/A', u'N/A', u'4643G', u'3.65', u'119T',
        u'4046530', u'3951k', u'72301', u'4396k', u'6965G'
    ],
    [
        u'cephfs01-cache', u'55', u'-', u'N/A', u'N/A', u'81681M', u'9.67',
        u'744G', u'22523', u'11189', u'86325', u'16059k', u'239G'
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
    ['200T', '186T', '13808G', '6.74', '8774k'], ['POOLS:'],
    [
        'NAME', 'ID', 'CATEGORY', 'QUOTA', 'OBJECTS', 'QUOTA', 'BYTES', 'USED',
        '%USED', 'MAX', 'AVAIL', 'OBJECTS', 'DIRTY', 'READ', 'WRITE', 'RAW',
        'USED'
    ],
    [
        'seafile-commits', '33', '-', 'N/A', 'N/A', '276M', '0.04', '744G',
        '506506', '494k', '315k', '496k', '829M'
    ],
    [
        'seafile-blocks', '35', '-', 'N/A', 'N/A', '685G', '0.56', '119T',
        '879162', '858k', '891k', '1168k', '1027G'
    ],
    [
        'seafile-fs', '36', '-', 'N/A', 'N/A', '11412M', '1.47', '744G',
        '2502095', '2443k', '5782k', '2660k', '34237M'
    ],
    [
        'seafile-blocks-cache', '37', '-', 'N/A', '200G', '149G', '16.69',
        '744G', '198252', '96433', '5105k', '1944k', '447G'
    ],
    [
        'rbd', '49', '-', 'N/A', 'N/A', '3106G', '2.47', '119T', '795700',
        '777k', '16212k', '14942k', '4660G'
    ],
    [
        'rbd-cache', '50', '-', 'N/A', 'N/A', '40652M', '5.06', '744G',
        '10173', '3565', '50513k', '558M', '119G'
    ],
    [
        'cephfs01_meta', '53', '-', 'N/A', 'N/A', '131M', '0.02', '744G',
        '24170', '24170', '30172', '14199k', '393M'
    ],
    [
        'cephfs01', '54', '-', 'N/A', 'N/A', '4643G', '3.65', '119T',
        '4046530', '3951k', '72301', '4396k', '6965G'
    ],
    [
        'cephfs01-cache', '55', '-', 'N/A', 'N/A', '81681M', '9.67', '744G',
        '22523', '11189', '86325', '16059k', '239G'
>>>>>>> upstream/master
    ]
]

discovery = {
    '': [
<<<<<<< HEAD
        ('SUMMARY', {}), (u'cephfs01', {}), (u'cephfs01-cache', {}),
        (u'cephfs01_meta', {}), (u'rbd', {}), (u'rbd-cache', {}),
        (u'seafile-blocks', {}), (u'seafile-blocks-cache', {}),
        (u'seafile-commits', {}), (u'seafile-fs', {})
=======
        ('SUMMARY', {}), ('cephfs01', {}), ('cephfs01-cache', {}),
        ('cephfs01_meta', {}), ('rbd', {}), ('rbd-cache', {}),
        ('seafile-blocks', {}), ('seafile-blocks-cache', {}),
        ('seafile-commits', {}), ('seafile-fs', {})
>>>>>>> upstream/master
    ]
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
                    '7.0% used (14.00 of 200.00 TB), trend: 0.00 B / 24 hours',
                    [
                        (
                            'SUMMARY', 14680064.0, 167772160.0, 188743680.0, 0,
                            209715200.0
                        ), ('fs_size', 209715200.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 8738133.333333334)
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
                    0, '7.0% used (14.00 of 200.00 TB)', [
                        (
                            'fs_used', 14680064.0, 167772160.0, 188743680.0, 0,
                            209715200.0
                        ), ('fs_size', 209715200.0, None, None, None, None),
                        ('fs_used_percent', 7.0, None, None, None, None)
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'cephfs01', {
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
                    '3.67% used (4.53 of 123.53 TB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'cephfs01', 4754432.0, 103627980.8, 116581478.4,
                            0, 129534976.0
                        ), ('fs_size', 129534976.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 5397290.666666667)
=======
            'cephfs01', {
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
                    0, '3.67% used (4.53 of 123.53 TB)', [
                        (
                            'fs_used', 4754432.0, 103627980.8, 116581478.4, 0,
                            129534976.0
                        ), ('fs_size', 129534976.0, None, None, None, None),
                        (
                            'fs_used_percent', 3.6703847461244754, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'cephfs01-cache', {
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
                    '9.68% used (79.77 of 823.77 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'cephfs01-cache', 81681.0, 674829.6, 759183.3, 0,
                            843537.0
                        ), ('fs_size', 843537.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 35147.375)
=======
            'cephfs01-cache', {
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
                    0, '9.68% used (79.77 of 823.77 GB)', [
                        ('fs_used', 81681.0, 674829.6, 759183.3, 0, 843537.0),
                        ('fs_size', 843537.0, None, None, None, None),
                        (
                            'fs_used_percent', 9.683155569939434, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'cephfs01_meta', {
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
                    '0.02% used (131.00 MB of 744.13 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'cephfs01_meta', 131.0, 609589.6, 685788.3, 0,
                            761987.0
                        ), ('fs_size', 761987.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 31749.458333333332)
=======
            'cephfs01_meta', {
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
                    0, '0.02% used (131.00 MB of 744.13 GB)', [
                        ('fs_used', 131.0, 609589.6, 685788.3, 0, 761987.0),
                        ('fs_size', 761987.0, None, None, None, None),
                        (
                            'fs_used_percent', 0.01719189434990361, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'rbd', {
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
                    '2.49% used (3.03 of 122.03 TB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'rbd', 3180544.0, 102368870.4, 115164979.2, 0,
                            127961088.0
                        ), ('fs_size', 127961088.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 5331712.0)
=======
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
                    0, '2.49% used (3.03 of 122.03 TB)', [
                        (
                            'fs_used', 3180544.0, 102368870.4, 115164979.2, 0,
                            127961088.0
                        ), ('fs_size', 127961088.0, None, None, None, None),
                        (
                            'fs_used_percent', 2.485555608905107, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'rbd-cache', {
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
                    '5.07% used (39.70 of 783.70 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'rbd-cache', 40652.0, 642006.4, 722257.2, 0,
                            802508.0
                        ), ('fs_size', 802508.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 33437.833333333336)
=======
            'rbd-cache', {
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
                    0, '5.07% used (39.70 of 783.70 GB)', [
                        ('fs_used', 40652.0, 642006.4, 722257.2, 0, 802508.0),
                        ('fs_size', 802508.0, None, None, None, None),
                        (
                            'fs_used_percent', 5.065619283546083, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'seafile-blocks', {
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
                    '0.56% used (685.00 GB of 119.67 TB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'seafile-blocks', 701440.0, 100385587.2,
                            112933785.6, 0, 125481984.0
                        ), ('fs_size', 125481984.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 5228416.0)
=======
            'seafile-blocks', {
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
                    0, '0.56% used (685.00 GB of 119.67 TB)', [
                        (
                            'fs_used', 701440.0, 100385587.2, 112933785.6, 0,
                            125481984.0
                        ), ('fs_size', 125481984.0, None, None, None, None),
                        (
                            'fs_used_percent', 0.5589965807362434, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'seafile-blocks-cache', {
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
                    '16.69% used (149.00 of 893.00 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'seafile-blocks-cache', 152576.0, 731545.6,
                            822988.8, 0, 914432.0
                        ), ('fs_size', 914432.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 38101.333333333336)
=======
            'seafile-blocks-cache', {
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
                    0, '16.69% used (149.00 of 893.00 GB)', [
                        ('fs_used', 152576.0, 731545.6, 822988.8, 0, 914432.0),
                        ('fs_size', 914432.0, None, None, None, None),
                        (
                            'fs_used_percent', 16.685330347144458, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'seafile-commits', {
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
                    '0.04% used (276.00 MB of 744.27 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'seafile-commits', 276.0, 609705.6, 685918.8, 0,
                            762132.0
                        ), ('fs_size', 762132.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 31755.5)
=======
            'seafile-commits', {
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
                    0, '0.04% used (276.00 MB of 744.27 GB)', [
                        ('fs_used', 276.0, 609705.6, 685918.8, 0, 762132.0),
                        ('fs_size', 762132.0, None, None, None, None),
                        (
                            'fs_used_percent', 0.036214199115113914, None,
                            None, None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        ),
        (
<<<<<<< HEAD
            u'seafile-fs', {
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
                    '1.48% used (11.14 of 755.14 GB), trend: 0.00 B / 24 hours',
                    [
                        (
                            u'seafile-fs', 11412.0, 618614.4, 695941.2, 0,
                            773268.0
                        ), ('fs_size', 773268.0, None, None, None, None),
                        ('growth', 0.0, None, None, None, None),
                        ('trend', 0, None, None, 0, 32219.5)
=======
            'seafile-fs', {
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
                    0, '1.48% used (11.14 of 755.14 GB)', [
                        ('fs_used', 11412.0, 618614.4, 695941.2, 0, 773268.0),
                        ('fs_size', 773268.0, None, None, None, None),
                        (
                            'fs_used_percent', 1.4758143360387344, None, None,
                            None, None
                        )
>>>>>>> upstream/master
                    ]
                )
            ]
        )
    ]
}
