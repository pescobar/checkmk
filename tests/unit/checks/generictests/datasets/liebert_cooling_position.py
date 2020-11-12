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


checkname = 'liebert_cooling_position'


info = [
    [u'Free Cooling Valve Open Position', u'42', u'%'],
    [u'This is ignored', u'42', u'%'],
]


discovery = {
    '': [
        (u'Free Cooling Valve Open Position', {}),
    ],
}


checks = {
    '': [
<<<<<<< HEAD
        (u'Free Cooling Valve Open Position', {"levels": (23, 50)}, [
            (1, "42.00 % (warn/crit at 23.00 %/50.00 %)", [
                ('filehandler_perc', 42.0, 23.0, 50.0, None, None),
=======
        (u'Free Cooling Valve Open Position', {"min_capacity": (50, 45)}, [
            (2, "42.00 % (warn/crit below 50.00 %/45.00 %)", [
                ('capacity_perc', 42.0, None, None, None, None),
>>>>>>> upstream/master
            ]),
        ]),
    ],
}
