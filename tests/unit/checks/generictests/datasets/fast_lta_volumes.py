<<<<<<< HEAD
# -*- encoding: utf-8
# yapf: disable


checkname = 'fast_lta_volumes'


info = [[u'Archiv_Test', u'1000000000000', u'10000000000'],
        [u'Archiv_Test_1', u'', u'']]


discovery = {'': [(u'Archiv_Test', {})]}


checks = {'': [(u'Archiv_Test',
                {},
                [(0,
                  '1.0% used (9.31 of 931.32 GB), trend: 0.00 B / 24 hours',
                  [(u'Archiv_Test',
                    9536.7431640625,
                    762939.453125,
                    858306.884765625,
                    0,
                    953674.31640625),
                   ('fs_size', 953674.31640625, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 39736.429850260414)])])]}
=======
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore
checkname = 'fast_lta_volumes'

info = [
    ['Archiv_Test', '1000000000000', '10000000000'], ['Archiv_Test_1', '', '']
]

discovery = {'': [('Archiv_Test', {})]}

checks = {
    '': [
        (
            'Archiv_Test', {}, [
                (
                    0, '1.0% used (9.31 of 931.32 GB)', [
                        (
                            'fs_used', 9536.7431640625, 762939.453125,
                            858306.884765625, 0, 953674.31640625
                        ),
                        ('fs_size', 953674.31640625, None, None, None, None),
                        ('fs_used_percent', 1.0, None, None, None, None)
                    ]
                )
            ]
        )
    ]
}
>>>>>>> upstream/master
