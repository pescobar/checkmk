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
    Integer,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
    Levels,
)


def _parameter_valuespec_safenet_hsm_operstats():
    return Dictionary(elements=[
        ("error_rate",
         Tuple(
<<<<<<< HEAD
             title=_(u"Error rate"),
=======
             title=_("Error rate"),
>>>>>>> upstream/master
             elements=[
                 Float(title=_("Warning at"), default_value=0.01, unit=_("1/s")),
                 Float(title=_("Critical at"), default_value=0.05, unit=_("1/s")),
             ],
         )),
        ("request_rate", Levels(
<<<<<<< HEAD
            title=_(u"Request rate"),
=======
            title=_("Request rate"),
>>>>>>> upstream/master
            unit=_("1/s"),
            default_value=None,
        )),
        ("operation_errors",
         Tuple(
             title=_("Operation errors"),
             help=_("Sets levels on total operation errors since last counter reset."),
             elements=[
                 Integer(title=_("Warning at"), default_value=0),
                 Integer(title=_("Critical at"), default_value=1),
             ],
         )),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="safenet_hsm_operstats",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_safenet_hsm_operstats,
        title=lambda: _("Safenet HSM Operation Stats"),
    ))
