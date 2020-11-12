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
    DropdownChoice,
    TextAscii,
<<<<<<< HEAD
    Transform,
=======
>>>>>>> upstream/master
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


<<<<<<< HEAD
def _parameter_valuespec_hacmp_resources():
    return Transform(
        Dictionary(
            elements=[
                ("expect_online_on",
                 DropdownChoice(
                     title=_(u"Expect resource to be online on"),
                     choices=[
                         ("first", _(u"the first node")),
                         ("any", _(u"any node")),
                     ],
                 )),
            ],
            optional_keys=[],
        ),
        forth=lambda x: {"expect_online_on": "first"},
=======
def _parameter_valuespec_hacmp_resources() -> Dictionary:
    return Dictionary(
        elements=[
            ("expect_online_on",
             DropdownChoice(
                 title=_("Expect resource to be online on"),
                 choices=[
                     ("first", _("the first node")),
                     ("any", _("any node")),
                 ],
             )),
        ],
        optional_keys=[],
>>>>>>> upstream/master
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="hacmp_resources",
        group=RulespecGroupCheckParametersApplications,
<<<<<<< HEAD
        item_spec=lambda: TextAscii(title=_(u"Resource Group")),
=======
        item_spec=lambda: TextAscii(title=_("Resource Group")),
>>>>>>> upstream/master
        parameter_valuespec=_parameter_valuespec_hacmp_resources,
        title=lambda: _("AIX HACMP Resource Groups"),
    ))
