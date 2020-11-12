<<<<<<< HEAD
# -*- encoding: utf-8
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


checkname = 'aws_glacier_limits'


<<<<<<< HEAD
info = [[u'[["number_of_vaults",',
         u'"Vaults",',
         u'1000,',
         u'0,',
         u'"ap-northeast-2"]]'],
        [u'[["number_of_vaults",',
         u'"Vaults",',
         u'1000,',
         u'0,',
         u'"ca-central-1"]]'],
        [u'[["number_of_vaults",',
         u'"Vaults",',
         u'1000,',
         u'2,',
         u'"eu-central-1"]]'],
        [u'[["number_of_vaults",', u'"Vaults",', u'1000,', u'0,', u'"us-east-1"]]']]


discovery = {'': [(None, {})]}


checks = {'': [(None,
                {'number_of_vaults': (None, 80.0, 90.0)},
                [(0,
                  'No levels reached',
                  [(u'aws_glacier_number_of_vaults', 0, None, None, None, None),
                   (u'aws_glacier_number_of_vaults', 0, None, None, None, None),
                   (u'aws_glacier_number_of_vaults', 2, None, None, None, None),
                   (u'aws_glacier_number_of_vaults', 0, None, None, None, None)]),
                 (0,
                  u'\nVaults: 0 (of max. 1000) (Region ap-northeast-2)\nVaults: 0 (of max. 1000) (Region ca-central-1)\nVaults: 0 (of max. 1000) (Region us-east-1)\nVaults: 2 (of max. 1000) (Region eu-central-1)',
                  [])])]}
=======
info = [['[["number_of_vaults",',
         '"Vaults",',
         '1000,',
         '0,',
         '"ap-northeast-2"]]'],
        ['[["number_of_vaults",',
         '"Vaults",',
         '1000,',
         '0,',
         '"ca-central-1"]]'],
        ['[["number_of_vaults",',
         '"Vaults",',
         '1000,',
         '2,',
         '"eu-central-1"]]'],
        ['[["number_of_vaults",',
         '"Vaults",',
         '1000,',
         '0,',
         '"us-east-1"]]']]


discovery = {'': [("ap-northeast-2", {}),
                  ("ca-central-1", {}),
                  ("eu-central-1", {}),
                  ("us-east-1", {})]}


checks = {'': [("ap-northeast-2",
                {'number_of_vaults': (None, 80.0, 90.0)},
                [(0,
                  'No levels reached',
                  [('aws_glacier_number_of_vaults', 0, None, None, None, None)]),
                 (0,
                  '\nVaults: 0 (of max. 1000)')]),
               ("ca-central-1",
                {'number_of_vaults': (None, 80.0, 90.0)},
                [(0,
                  'No levels reached',
                  [('aws_glacier_number_of_vaults', 0, None, None, None, None)]),
                 (0,
                  '\nVaults: 0 (of max. 1000)')]),
               ("eu-central-1",
                {'number_of_vaults': (None, 80.0, 90.0)},
                [(0,
                  'No levels reached',
                  [('aws_glacier_number_of_vaults', 2, None, None, None, None)]),
                 (0,
                  '\nVaults: 2 (of max. 1000)')]),
               ("us-east-1",
                {'number_of_vaults': (None, 80.0, 90.0)},
                [(0,
                  'No levels reached',
                  [('aws_glacier_number_of_vaults', 0, None, None, None, None)]),
                 (0,
                  '\nVaults: 0 (of max. 1000)')])
               ]}
>>>>>>> upstream/master
