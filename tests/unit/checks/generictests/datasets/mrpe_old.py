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


checkname = 'mrpe'


info = [
    ['Foo_Application', '0', 'OK', '-', 'Foo', 'server', 'up', 'and', 'running'],
    ['Bar_Extender', '1', 'WARN', '-', 'Bar', 'extender', 'overload', '6.012|bar_load=6.012'],
<<<<<<< HEAD
    ['Mutliliner', '\xc2\xa7$%', 'M\xc3\x96\xc3\x96P', '-', 'Output1|the_foo=1;2;3;4;5\x01more',
     'output|the_bar=42\x01the_gee=23'],
=======
    ['Mutliliner', u'§$%', u'MÖÖP', '-', u'Output1|the_foo=1;2;3;4;5\x01more',
     u'output|the_bar=42\x01the_gee=23'],
>>>>>>> upstream/master
]


discovery = {
    '': [
        ('Bar_Extender', {}),
        ('Foo_Application', {}),
        ('Mutliliner', {}),
    ],
}


checks = {
    '': [
        ('Bar_Extender', {}, [
            (1, 'WARN - Bar extender overload 6.012', [
                ('bar_load', 6.012, None, None, None, None),
            ])
        ]),
        ('Foo_Application', {}, [
            (0, 'OK - Foo server up and running', [])]),
        ('Mutliliner', {}, [
<<<<<<< HEAD
            (3, 'Invalid plugin status \'\\xc2\\xa7$%\'. Output is: M\xc3\x96\xc3\x96P - Output1\nmore output', [
=======
            (3, u'Invalid plugin status \'§$%\'. Output is: MÖÖP - Output1\nmore output', [
>>>>>>> upstream/master
                ('the_foo', 1, 2, 3, 4, 5),
                ('the_bar', 42, None, None, None, None),
                ('the_gee', 23, None, None, None, None),
            ]),
        ]),
    ],
}
