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
    Integer,
    Percentage,
    TextAscii,
<<<<<<< HEAD
=======
    Transform,
>>>>>>> upstream/master
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


<<<<<<< HEAD
def _parameter_valuespec_db_connections():
    return Dictionary(
        help=_("This rule allows you to configure the number of maximum concurrent "
               "connections for a given database."),
=======
def _transform_connection_type(params):
    # The old WATO rule did not differentiate between "active" and "idle"
    # The old levels were refering to the "active" type
    for metric_type in ("perc", "abs"):
        if "levels_%s" % metric_type in params.keys():
            params["levels_%s_active" % metric_type] = params["levels_%s" % metric_type]
            params.pop("levels_%s" % metric_type)

    return params


def _parameter_valuespec_db_connections():
    return Transform(
        Dictionary(
            help=_("This rule allows you to configure the number of maximum concurrent "
                   "connections for a given database."),
            elements=[
                ("levels_perc_active",
                 Tuple(
                     title=_("Percentage of maximum available active connections"),
                     elements=[
                         Percentage(title=_("Warning at"),
                                    unit=_("% of maximum active connections")),
                         Percentage(title=_("Critical at"),
                                    unit=_("% of maximum active connections")),
                     ],
                 )),
                ("levels_abs_active",
                 Tuple(
                     title=_("Absolute number of active connections"),
                     elements=[
                         Integer(title=_("Warning at"), minvalue=0, unit=_("connections")),
                         Integer(title=_("Critical at"), minvalue=0, unit=_("connections")),
                     ],
                 )),
                ("levels_perc_idle",
                 Tuple(
                     title=_("Percentage of maximum available idle connections"),
                     elements=[
                         Percentage(title=_("Warning at"), unit=_("% of maximum idle connections")),
                         Percentage(title=_("Critical at"),
                                    unit=_("% of maximum idle connections")),
                     ],
                 )),
                ("levels_abs_idle",
                 Tuple(
                     title=_("Absolute number of idle connections"),
                     elements=[
                         Integer(title=_("Warning at"), minvalue=0, unit=_("idle connections")),
                         Integer(title=_("Critical at"), minvalue=0, unit=_("idle connections")),
                     ],
                 )),
            ],
        ),
        forth=_transform_connection_type,
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="db_connections",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextAscii(title=_("Name of the database"),),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_db_connections,
        title=lambda: _("PostgreSQL database connections"),
    ))


def _parameter_valuespec_db_connections_mongodb():
    return Dictionary(
        help=_("This rule allows you to configure the number of incoming connections from clients "
               "to the database server."),
>>>>>>> upstream/master
        elements=[
            ("levels_perc",
             Tuple(
                 title=_("Percentage of maximum available connections"),
                 elements=[
                     Percentage(title=_("Warning at"), unit=_("% of maximum connections")),
                     Percentage(title=_("Critical at"), unit=_("% of maximum connections")),
                 ],
             )),
            ("levels_abs",
             Tuple(
<<<<<<< HEAD
                 title=_("Absolute number of connections"),
=======
                 title=_("Absolute number of incoming connections"),
>>>>>>> upstream/master
                 elements=[
                     Integer(title=_("Warning at"), minvalue=0, unit=_("connections")),
                     Integer(title=_("Critical at"), minvalue=0, unit=_("connections")),
                 ],
             )),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
<<<<<<< HEAD
        check_group_name="db_connections",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextAscii(title=_("Name of the database"),),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_db_connections,
        title=lambda: _("Database Connections (PostgreSQL/MongoDB)"),
=======
        check_group_name="db_connections_mongodb",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextAscii(title=_("Name of the database"),),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_db_connections_mongodb,
        title=lambda: _("MongoDB database connections"),
>>>>>>> upstream/master
    ))
