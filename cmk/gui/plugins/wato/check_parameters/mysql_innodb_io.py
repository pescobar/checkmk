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
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


def _item_spec_mysql_innodb_io():
    return TextAscii(
        title=_("Instance"),
        help=_("Only needed if you have multiple MySQL Instances on one server"),
    )


def _parameter_valuespec_mysql_innodb_io():
    return Dictionary(elements=[
        ("read",
         Tuple(
             title=_("Read throughput"),
             elements=[
                 Float(title=_("warning at"), unit=_("MB/s")),
                 Float(title=_("critical at"), unit=_("MB/s"))
             ],
         )),
        ("write",
         Tuple(
             title=_("Write throughput"),
             elements=[
                 Float(title=_("warning at"), unit=_("MB/s")),
                 Float(title=_("critical at"), unit=_("MB/s"))
             ],
         )),
        ("average",
         Integer(title=_("Average"),
                 help=_("When averaging is set, a floating average value "
                        "of the disk throughput is computed and the levels for read "
                        "and write will be applied to the average instead of the current "
                        "value."),
                 minvalue=1,
                 default_value=5,
                 unit=_("minutes")))
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="mysql_innodb_io",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_mysql_innodb_io,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_mysql_innodb_io,
        title=lambda: _("MySQL InnoDB Throughput"),
    ))
