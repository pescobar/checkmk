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
# | Copyright Mathias Kettner 2019             mk@mathias-kettner.de |
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

from typing import Tuple as _Tuple
>>>>>>> upstream/master

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Alternative,
    Dictionary,
    FixedValue,
    Float,
    TextAscii,
    Tuple,
    ListChoice,
)
from cmk.gui.plugins.wato import (
    HostRulespec,
    RulespecGroupCheckParametersDiscovery,
    RulespecGroupCheckParametersEnvironment,
    CheckParameterRulespecWithItem,
    rulespec_registry,
)


<<<<<<< HEAD
def _vs_cisco_dom(which_levels):
    def _button_text_warn(which_levels):
        if which_levels == "upper":
            text = "Warning at"
        elif which_levels == "lower":
            text = "Warning below"
        else:
            raise ValueError
        return text

    def _button_text_crit(which_levels):
        if which_levels == "upper":
            text = "Critical at"
        elif which_levels == "lower":
            text = "Critical below"
        else:
            raise ValueError
=======
def _vs_cisco_dom(which_levels: str) -> _Tuple[str, Alternative]:
    def _button_text_warn(which_levels: str) -> str:
        if which_levels == "upper":
            text = _("Warning at")
        elif which_levels == "lower":
            text = _("Warning below")
        else:
            raise ValueError()
        return text

    def _button_text_crit(which_levels: str) -> str:
        if which_levels == "upper":
            text = _("Critical at")
        elif which_levels == "lower":
            text = _("Critical below")
        else:
            raise ValueError()
>>>>>>> upstream/master
        return text

    return (
        "power_levels_%s" % which_levels,
        Alternative(
            title="%s levels for the signal power" % which_levels.title(),
<<<<<<< HEAD
            style="dropdown",
=======
>>>>>>> upstream/master
            default_value=True,  # use device levels
            elements=[
                FixedValue(
                    True,
                    title=_("Use device levels"),
                    totext="",
                ),
                Tuple(title=_("Use the following levels"),
                      elements=[
<<<<<<< HEAD
                          Float(title=_(_button_text_warn(which_levels)), unit=_("dBm")),
                          Float(title=_(_button_text_crit(which_levels)), unit=_("dBm")),
=======
                          Float(title=_button_text_warn(which_levels), unit=_("dBm")),
                          Float(title=_button_text_crit(which_levels), unit=_("dBm")),
>>>>>>> upstream/master
                      ]),
                FixedValue(
                    False,
                    title=_("No levels"),
                    totext="",
                ),
            ]))


<<<<<<< HEAD
def _item_spec_cisco_dom():
    return TextAscii(title=_("Sensor description if present, sensor index otherwise"))


def _parameter_valuespec_cisco_dom():
=======
def _item_spec_cisco_dom() -> TextAscii:
    return TextAscii(title=_("Sensor description if present, sensor index otherwise"))


def _parameter_valuespec_cisco_dom() -> Dictionary:
>>>>>>> upstream/master
    return Dictionary(elements=[
        (_vs_cisco_dom("upper")),
        (_vs_cisco_dom("lower")),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="cisco_dom",
        group=RulespecGroupCheckParametersEnvironment,
        item_spec=_item_spec_cisco_dom,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_cisco_dom,
        title=lambda: _("CISCO Digital Optical Monitoring (DOM)"),
    ))


def _valuespec_discovery_cisco_dom_rules():
<<<<<<< HEAD
    return Dictionary(title=_("Cisco DOM Discovery"),
=======
    return Dictionary(title=_("Cisco DOM discovery"),
>>>>>>> upstream/master
                      elements=[
                          ("admin_states",
                           ListChoice(
                               title=_("Admin states to discover"),
                               choices={
                                   1: _("up"),
                                   2: _("down"),
                                   3: _("testing"),
                               },
                               toggle_all=True,
                               default_value=['1', '2', '3'],
                           )),
                      ])


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupCheckParametersDiscovery,
        match_type="dict",
        name="discovery_cisco_dom_rules",
        valuespec=_valuespec_discovery_cisco_dom_rules,
    ))
