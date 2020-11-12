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

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Percentage,
    TextAscii,
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Percentage,
    TextAscii,
    Transform,
>>>>>>> upstream/master
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersEnvironment,
)


<<<<<<< HEAD
def _parameter_valuespec_smoke():
    return Tuple(
        help=_("For devices which measure smoke in percent"),
        elements=[
            Percentage(title=_("Warning at"), allow_int=True, default_value=1),
            Percentage(title=_("Critical at"), allow_int=True, default_value=5),
        ],
=======
def _transform_smoke_detection_params(params):
    if isinstance(params, tuple):
        return {'levels': params}
    return params


def _parameter_valuespec_smoke():
    return Transform(
        Dictionary(
            help=_("For devices that measure smoke in percent"),
            elements=[
                (
                    'levels',
                    Tuple(
                        title=_('Upper limits in percent'),
                        elements=[
                            Percentage(title=_("Warning at"), allow_int=True, default_value=1),
                            Percentage(title=_("Critical at"), allow_int=True, default_value=5),
                        ],
                    ),
                ),
            ],
        ),
        forth=_transform_smoke_detection_params,
>>>>>>> upstream/master
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="smoke",
        group=RulespecGroupCheckParametersEnvironment,
        item_spec=lambda: TextAscii(title=_("Sensor ID"), help=_("The identifier of the sensor.")),
        parameter_valuespec=_parameter_valuespec_smoke,
        title=lambda: _("Smoke Detection"),
    ))
