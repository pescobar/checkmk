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
    Transform,
<<<<<<< HEAD
    Age,
    Dictionary,
    MonitoringState,
    TextAscii,
    Tuple,
=======
    Dictionary,
    MonitoringState,
    TextAscii,
>>>>>>> upstream/master
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


def _oracle_instance_transform_oracle_instance_params(p):
    if "ignore_noarchivelog" in p:
        if p["ignore_noarchivelog"]:
            p["noarchivelog"] = 0
        del p["ignore_noarchivelog"]
<<<<<<< HEAD
=======
    if "uptime_min" in p:
        del p["uptime_min"]
>>>>>>> upstream/master
    return p


def _parameter_valuespec_oracle_instance():
    return Transform(Dictionary(
        title=_("Consider state of Archivelogmode: "),
        elements=[
            ('archivelog',
             MonitoringState(
                 default_value=0,
                 title=_("State in case of Archivelogmode is enabled: "),
             )),
            (
                'noarchivelog',
                MonitoringState(
                    default_value=1,
                    title=_("State in case of Archivelogmode is disabled: "),
                ),
            ),
            (
                'forcelogging',
                MonitoringState(
                    default_value=0,
                    title=_("State in case of Force Logging is enabled: "),
                ),
            ),
            (
                'noforcelogging',
                MonitoringState(
                    default_value=1,
                    title=_("State in case of Force Logging is disabled: "),
                ),
            ),
            (
                'logins',
                MonitoringState(
                    default_value=2,
                    title=_("State in case of logins are not possible: "),
                ),
            ),
            (
                'primarynotopen',
                MonitoringState(
                    default_value=2,
                    title=_("State in case of Database is PRIMARY and not OPEN: "),
                ),
            ),
<<<<<<< HEAD
            ('uptime_min',
             Tuple(
                 title=_("Minimum required uptime"),
                 elements=[
                     Age(title=_("Warning if below")),
                     Age(title=_("Critical if below")),
                 ],
             )),
=======
>>>>>>> upstream/master
        ],
    ),
                     forth=_oracle_instance_transform_oracle_instance_params)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="oracle_instance",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextAscii(title=_("Database SID"), size=12, allow_empty=False),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_oracle_instance,
        title=lambda: _("Oracle Instance"),
    ))
