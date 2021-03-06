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
    Age,
    Dictionary,
    DropdownChoice,
    TextAscii,
    Tuple,
<<<<<<< HEAD
=======
    ListOf,
    Integer,
    MonitoringState,
>>>>>>> upstream/master
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


def _parameter_valuespec_job():
    return Dictionary(elements=[
        ("age",
         Tuple(
             title=_("Maximum time since last start of job execution"),
             elements=[
                 Age(title=_("Warning at"), default_value=0),
                 Age(title=_("Critical at"), default_value=0)
             ],
         )),
<<<<<<< HEAD
=======
        ("exit_code_to_state_map",
         ListOf(
             Tuple(orientation="horizontal",
                   elements=[
                       Integer(title=_("Exit code")),
                       MonitoringState(title=_("Resulting state"),),
                   ],
                   default_value=(0, 0)),
             title=_("Explicit mapping of job exit codes to states"),
             help=
             _("Here you can define a mapping between possible exit codes and service states. "
               "If no mapping is defined, the check becomes CRITICAL when the exit code is not 0. "
               "If an exit code occurs that is not defined in this mapping, the check becomes CRITICAL. "
               "If you happen to define the same exit code multiple times the first entry will be used."
              ),
             allow_empty=False,
         )),
>>>>>>> upstream/master
        ("outcome_on_cluster",
         DropdownChoice(
             title=_("Clusters: Prefered check result of local checks"),
             help=_("If you're running local checks on clusters via clustered services rule "
                    "you can influence the check result with this rule. You can choose between "
                    "best or worst state. Default setting is worst state."),
             choices=[
                 ("worst", _("Worst state")),
                 ("best", _("Best state")),
             ],
             default_value="worst")),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="job",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextAscii(title=_("Job name"),),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_job,
<<<<<<< HEAD
        title=lambda: _("Age of jobs controlled by mk-job"),
=======
        title=lambda: _("mk-job job age"),
>>>>>>> upstream/master
    ))
