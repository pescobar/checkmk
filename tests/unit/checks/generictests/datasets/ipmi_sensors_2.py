<<<<<<< HEAD
# -*- encoding: utf-8
# yapf: disable

checkname = 'ipmi_sensors'

info = [
    [u'1', u'Temperature_Inlet_Temp', u'21.00_C_(NA/48.00)', u'[OK]'],
    [u'59', u'M2_Temp0(PCIe1)_(Temperature)', u'NA/79.00_41.00_C', u'[OK]'],
    [u'20', u'Fan_FAN1_F_Speed', u'7200.00_RPM_(NA/NA)', u'[OK]'],
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore
checkname = 'ipmi_sensors'

info = [
    ['1', 'Temperature_Inlet_Temp', '21.00_C_(NA/48.00)', '[OK]'],
    ['59', 'M2_Temp0(PCIe1)_(Temperature)', 'NA/79.00_41.00_C', '[OK]'],
    ['20', 'Fan_FAN1_F_Speed', '7200.00_RPM_(NA/NA)', '[OK]']
>>>>>>> upstream/master
]

discovery = {
    '': [
<<<<<<< HEAD
        (u'Fan_FAN1_F_Speed', {}),
        (u'M2_Temp0(PCIe1)_(Temperature)', {}),
        (u'Temperature_Inlet_Temp', {}),
=======
        ('Fan_FAN1_F_Speed', {}), ('M2_Temp0(PCIe1)_(Temperature)', {}),
        ('Temperature_Inlet_Temp', {})
>>>>>>> upstream/master
    ]
}

checks = {
    '': [
        (
<<<<<<< HEAD
            u'Fan_FAN1_F_Speed',
            {},
            [(0, u'Status: OK, 7200.0 RPM', [])],
        ),
        (
            u'M2_Temp0(PCIe1)_(Temperature)',
            {},
            [(0, u'Status: OK, 41.0 C', [('value', 41.0, None, 79.0, None, None)])],
        ),
        (
            u'Temperature_Inlet_Temp',
            {},
            [(0, u'Status: OK, 21.0 C', [('value', 21.0, None, 48.0, None, None)])],
        ),
=======
            'Fan_FAN1_F_Speed', {}, [
                (0, 'Status: OK', []), (0, '7200.00 RPM', [])
            ]
        ),
        (
            'M2_Temp0(PCIe1)_(Temperature)', {}, [
                (0, 'Status: OK', []),
                (0, '41.00 C', [('value', 41.0, None, 79.0, None, None)])
            ]
        ),
        (
            'Temperature_Inlet_Temp', {}, [
                (0, 'Status: OK', []),
                (0, '21.00 C', [('value', 21.0, None, 48.0, None, None)])
            ]
        )
>>>>>>> upstream/master
    ]
}
