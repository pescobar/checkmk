<<<<<<< HEAD
#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Float,
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersEnvironment,
)


def _parameter_valuespec_ucs_bladecenter_chassis_voltage():
    return Dictionary(
        help=_("Here you can configure the 3.3V and 12V voltage levels for each chassis."),
        elements=[("levels_3v_lower",
                   Tuple(
                       title=_("3.3 Volt Output Lower Levels"),
                       elements=[
                           Float(title=_("warning if below or equal"), unit="V",
                                 default_value=3.25),
                           Float(title=_("critical if below or equal"),
                                 unit="V",
                                 default_value=3.20),
                       ],
                   )),
                  ("levels_3v_upper",
                   Tuple(
                       title=_("3.3 Volt Output Upper Levels"),
                       elements=[
                           Float(title=_("warning if above or equal"), unit="V", default_value=3.4),
                           Float(title=_("critical if above or equal"),
                                 unit="V",
                                 default_value=3.45),
                       ],
                   )),
                  ("levels_12v_lower",
                   Tuple(
                       title=_("12 Volt Output Lower Levels"),
                       elements=[
                           Float(title=_("warning if below or equal"), unit="V",
                                 default_value=11.9),
                           Float(title=_("critical if below or equal"),
                                 unit="V",
                                 default_value=11.8),
                       ],
                   )),
                  ("levels_12v_upper",
                   Tuple(
                       title=_("12 Volt Output Upper Levels"),
                       elements=[
                           Float(title=_("warning if above or equal"), unit="V",
                                 default_value=12.1),
                           Float(title=_("critical if above or equal"),
                                 unit="V",
                                 default_value=12.2),
                       ],
                   ))],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="ucs_bladecenter_chassis_voltage",
        group=RulespecGroupCheckParametersEnvironment,
        item_spec=lambda: TextAscii(title=_("Chassis"), help=_("The identifier of the chassis.")),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_ucs_bladecenter_chassis_voltage,
        title=lambda: _("UCS Bladecenter Chassis Voltage Levels"),
    ))
