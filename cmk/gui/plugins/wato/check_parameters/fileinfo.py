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
    Age,
    Dictionary,
    Filesize,
    ListOfTimeRanges,
    MonitoringState,
    TextAscii,
    Tuple,
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    ListOfTimeRanges,
    MonitoringState,
    TextAscii,
>>>>>>> upstream/master
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersStorage,
)

<<<<<<< HEAD

def _parameter_valuespec_fileinfo():
    return Dictionary(elements=[
        ("minage",
         Tuple(
             title=_("Minimal age"),
             elements=[
                 Age(title=_("Warning if younger than")),
                 Age(title=_("Critical if younger than")),
             ],
         )),
        ("maxage",
         Tuple(
             title=_("Maximal age"),
             elements=[
                 Age(title=_("Warning if older than")),
                 Age(title=_("Critical if older than")),
             ],
         )),
        ("minsize",
         Tuple(
             title=_("Minimal size"),
             elements=[
                 Filesize(title=_("Warning if below")),
                 Filesize(title=_("Critical if below")),
             ],
         )),
        ("maxsize",
         Tuple(
             title=_("Maximal size"),
             elements=[
                 Filesize(title=_("Warning at")),
                 Filesize(title=_("Critical at")),
             ],
         )),
=======
from cmk.gui.plugins.wato.check_parameters.file_attributes_utils import (
    min_age_levels,
    max_age_levels,
    min_size_levels,
    max_size_levels,
)


def _parameter_valuespec_fileinfo():
    return Dictionary(elements=[
        ("minage", min_age_levels()),
        ("maxage", max_age_levels()),
        ("minsize", min_size_levels()),
        ("maxsize", max_size_levels()),
>>>>>>> upstream/master
        ("timeofday",
         ListOfTimeRanges(
             title=_("Only check during the following times of the day"),
             help=_("Outside these ranges the check will always be OK"),
         )),
        ("state_missing", MonitoringState(default_value=3, title=_("State when file is missing"))),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="fileinfo",
        group=RulespecGroupCheckParametersStorage,
        item_spec=lambda: TextAscii(title=_("File name"), allow_empty=True),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_fileinfo,
        title=lambda: _("Size and age of single files"),
    ))
