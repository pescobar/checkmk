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
    Checkbox,
    Dictionary,
    Integer,
    TextAscii,
    Tuple,
<<<<<<< HEAD
=======
    Transform,
>>>>>>> upstream/master
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersEnvironment,
)


def _parameter_valuespec_hw_fans():
<<<<<<< HEAD
    return Dictionary(
=======
    hw_fans_dict = Dictionary(
>>>>>>> upstream/master
        elements=[
            (
                "lower",
                Tuple(
                    help=_("Lower levels for the fan speed of a hardware device"),
                    title=_("Lower levels"),
                    elements=[
                        Integer(title=_("warning if below"), unit=u"rpm"),
                        Integer(title=_("critical if below"), unit=u"rpm"),
                    ],
                ),
            ),
            (
                "upper",
                Tuple(
                    help=_("Upper levels for the fan speed of a hardware device"),
                    title=_("Upper levels"),
                    elements=[
<<<<<<< HEAD
                        Integer(title=_("warning at"), unit=u"rpm", default_value=8000),
                        Integer(title=_("critical at"), unit=u"rpm", default_value=8400),
=======
                        Integer(title=_("warning at"), unit=u"rpm"),
                        Integer(title=_("critical at"), unit=u"rpm"),
>>>>>>> upstream/master
                    ],
                ),
            ),
            ("output_metrics",
             Checkbox(title=_("Performance data"), label=_("Enable performance data"))),
        ],
        optional_keys=["upper", "output_metrics"],
    )
<<<<<<< HEAD
=======
    return Transform(
        hw_fans_dict,
        forth=lambda spec: spec if isinstance(spec, dict) else {"lower": spec},
    )
>>>>>>> upstream/master


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="hw_fans",
        group=RulespecGroupCheckParametersEnvironment,
        item_spec=lambda: TextAscii(title=_("Fan Name"), help=_("The identificator of the fan.")),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_hw_fans,
        title=lambda: _("FAN speed of Hardware devices"),
    ))
