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
    Alternative,
    Dictionary,
    Filesize,
    Percentage,
<<<<<<< HEAD
    TextAscii,
=======
>>>>>>> upstream/master
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)

<<<<<<< HEAD
=======
from cmk.gui.plugins.wato.check_parameters.utils import mssql_item_spec_instance_tablespace

>>>>>>> upstream/master

def _parameter_valuespec_mssql_file_sizes():
    return Dictionary(
        title=_("File Size Levels"),
        elements=[
            ("data_files",
             Tuple(
                 title=_("Total data file size: Absolute upper levels"),
                 elements=[
                     Filesize(title=_("Warning at")),
                     Filesize(title=_("Critical at")),
                 ],
             )),
            ("log_files",
             Tuple(
                 title=_("Total log file size: Absolute upper levels"),
                 elements=[Filesize(title=_("Warning at")),
                           Filesize(title=_("Critical at"))],
             )),
            ("log_files_used",
             Alternative(
                 title=_("Used log files: Absolute or relative upper levels"),
                 elements=[
                     Tuple(
                         title=_("Upper absolute levels"),
                         elements=[
                             Filesize(title=_("Warning at")),
                             Filesize(title=_("Critical at"))
                         ],
                     ),
                     Tuple(
                         title=_("Upper percentage levels"),
                         elements=[
                             Percentage(title=_("Warning at")),
                             Percentage(title=_("Critical at"))
                         ],
                     ),
                 ],
             )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="mssql_file_sizes",
        group=RulespecGroupCheckParametersApplications,
<<<<<<< HEAD
        item_spec=lambda: TextAscii(title=_("Service descriptions"), allow_empty=False),
=======
        item_spec=mssql_item_spec_instance_tablespace,
>>>>>>> upstream/master
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_mssql_file_sizes,
        title=lambda: _("MSSQL Log and Data File Sizes"),
    ))
