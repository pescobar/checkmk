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
    Float,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersStorage,
)


<<<<<<< HEAD
def _item_spec_ddn_s2a_wait():
    return DropdownChoice(title=_(u"Host or Disk"),
                          choices=[
                              ("Disk", _(u"Disk")),
                              ("Host", _(u"Host")),
                          ])


def _parameter_valuespec_ddn_s2a_wait():
    return Dictionary(elements=[
        ("read_avg",
         Tuple(
             title=_(u"Read wait average"),
             elements=[
                 Float(title=_(u"Warning at"), unit="s"),
                 Float(title=_(u"Critical at"), unit="s"),
=======
def _item_spec_ddn_s2a_wait() -> DropdownChoice:
    return DropdownChoice(title=_("Host or Disk"),
                          choices=[
                              ("Disk", _("Disk")),
                              ("Host", _("Host")),
                          ])


def _parameter_valuespec_ddn_s2a_wait() -> Dictionary:
    return Dictionary(elements=[
        ("read_avg",
         Tuple(
             title=_("Read wait average"),
             elements=[
                 Float(title=_("Warning at"), unit="s"),
                 Float(title=_("Critical at"), unit="s"),
>>>>>>> upstream/master
             ],
         )),
        ("read_min",
         Tuple(
<<<<<<< HEAD
             title=_(u"Read wait minimum"),
             elements=[
                 Float(title=_(u"Warning at"), unit="s"),
                 Float(title=_(u"Critical at"), unit="s"),
=======
             title=_("Read wait minimum"),
             elements=[
                 Float(title=_("Warning at"), unit="s"),
                 Float(title=_("Critical at"), unit="s"),
>>>>>>> upstream/master
             ],
         )),
        ("read_max",
         Tuple(
<<<<<<< HEAD
             title=_(u"Read wait maximum"),
             elements=[
                 Float(title=_(u"Warning at"), unit="s"),
                 Float(title=_(u"Critical at"), unit="s"),
=======
             title=_("Read wait maximum"),
             elements=[
                 Float(title=_("Warning at"), unit="s"),
                 Float(title=_("Critical at"), unit="s"),
>>>>>>> upstream/master
             ],
         )),
        ("write_avg",
         Tuple(
<<<<<<< HEAD
             title=_(u"Write wait average"),
             elements=[
                 Float(title=_(u"Warning at"), unit="s"),
                 Float(title=_(u"Critical at"), unit="s"),
=======
             title=_("Write wait average"),
             elements=[
                 Float(title=_("Warning at"), unit="s"),
                 Float(title=_("Critical at"), unit="s"),
>>>>>>> upstream/master
             ],
         )),
        ("write_min",
         Tuple(
<<<<<<< HEAD
             title=_(u"Write wait minimum"),
             elements=[
                 Float(title=_(u"Warning at"), unit="s"),
                 Float(title=_(u"Critical at"), unit="s"),
=======
             title=_("Write wait minimum"),
             elements=[
                 Float(title=_("Warning at"), unit="s"),
                 Float(title=_("Critical at"), unit="s"),
>>>>>>> upstream/master
             ],
         )),
        ("write_max",
         Tuple(
<<<<<<< HEAD
             title=_(u"Write wait maximum"),
             elements=[
                 Float(title=_(u"Warning at"), unit="s"),
                 Float(title=_(u"Critical at"), unit="s"),
=======
             title=_("Write wait maximum"),
             elements=[
                 Float(title=_("Warning at"), unit="s"),
                 Float(title=_("Critical at"), unit="s"),
>>>>>>> upstream/master
             ],
         )),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="ddn_s2a_wait",
        group=RulespecGroupCheckParametersStorage,
        item_spec=_item_spec_ddn_s2a_wait,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_ddn_s2a_wait,
<<<<<<< HEAD
        title=lambda: _("Read/write wait for DDN S2A devices"),
=======
        title=lambda: _("DDN S2A read/write wait"),
>>>>>>> upstream/master
    ))
