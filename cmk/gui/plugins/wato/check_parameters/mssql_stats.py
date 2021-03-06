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
    RulespecGroupCheckParametersApplications,
)


def _parameter_valuespec_mssql_stats():
    return Dictionary(elements=[
        ("batch_requests/sec",
         Tuple(
             title=_("Batch Requests/sec"),
             elements=[
                 Float(title=_("warning at"), unit=_("/sec"), default_value=100000.0),
                 Float(title=_("critical at"), unit=_("/sec"), default_value=200000.0),
             ],
         )),
        ("sql_compilations/sec",
         Tuple(
             title=_("SQL Compilations/sec"),
             elements=[
                 Float(title=_("warning at"), unit=_("/sec"), default_value=10000.0),
                 Float(title=_("critical at"), unit=_("/sec"), default_value=20000.0),
             ],
         )),
        ("sql_re-compilations/sec",
         Tuple(
             title=_("SQL Re-Compilations/sec"),
             elements=[
                 Float(title=_("warning at"), unit=_("/sec"), default_value=10000.0),
                 Float(title=_("critical at"), unit=_("/sec"), default_value=200.0),
             ],
         )),
        ("locks_per_batch",
         Tuple(
             title=_("Locks/Batch"),
             elements=[
                 Float(title=_("warning at"), default_value=1000.0),
                 Float(title=_("critical at"), default_value=3000.0),
             ],
         )),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="mssql_stats",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextAscii(title=_("Counter ID"),),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_mssql_stats,
        title=lambda: _("MSSQL Statistics"),
    ))
