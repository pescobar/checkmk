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
    Integer,
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersNetworking,
)


def _item_spec_cisco_ip_sla():
    return TextAscii(
        title=_("RTT row index of the service"),
        allow_empty=True,
    )


def _parameter_valuespec_cisco_ip_sla():
    return Dictionary(elements=[
        ("rtt_type",
         DropdownChoice(
             title=_("RTT type"),
             choices=[
                 ('echo', _("echo")),
                 ('path echo', _("path echo")),
                 ('file IO', _("file IO")),
                 ('UDP echo', _("UDP echo")),
                 ('TCP connect', _("TCP connect")),
                 ('HTTP', _("HTTP")),
                 ('DNS', _("DNS")),
                 ('jitter', _("jitter")),
                 ('DLSw', _("DLSw")),
                 ('DHCP', _("DHCP")),
                 ('FTP', _("FTP")),
                 ('VoIP', _("VoIP")),
                 ('RTP', _("RTP")),
                 ('LSP group', _("LSP group")),
                 ('ICMP jitter', _("ICMP jitter")),
                 ('LSP ping', _("LSP ping")),
                 ('LSP trace', _("LSP trace")),
                 ('ethernet ping', _("ethernet ping")),
                 ('ethernet jitter', _("ethernet jitter")),
                 ('LSP ping pseudowire', _("LSP ping pseudowire")),
             ],
             default_value="echo",
         )),
        ("threshold",
         Integer(
             title=_("Treshold"),
             help=_("Depending on the precision the unit can be "
                    "either milliseconds or micoseconds."),
             unit=_("ms/us"),
             minvalue=1,
             default_value=5000,
         )),
        ("state",
         DropdownChoice(
             title=_("State"),
             choices=[
                 ('active', _("active")),
                 ('inactive', _("inactive")),
                 ('reset', _("reset")),
                 ('orderly stop', _("orderly stop")),
                 ('immediate stop', _("immediate stop")),
                 ('pending', _("pending")),
                 ('restart', _("restart")),
             ],
             default_value="active",
         )),
        ("connection_lost_occured",
         DropdownChoice(
             title=_("Connection lost occured"),
             choices=[
                 ("yes", _("yes")),
                 ("no", _("no")),
             ],
             default_value="no",
         )),
        ("timeout_occured",
         DropdownChoice(
             title=_("Timeout occured"),
             choices=[
                 ("yes", _("yes")),
                 ("no", _("no")),
             ],
             default_value="no",
         )),
        ("completion_time_over_treshold_occured",
         DropdownChoice(
             title=_("Completion time over treshold occured"),
             choices=[
                 ("yes", _("yes")),
                 ("no", _("no")),
             ],
             default_value="no",
         )),
        ("latest_rtt_completion_time",
         Tuple(
             title=_("Latest RTT completion time"),
             help=_("Depending on the precision the unit can be "
                    "either milliseconds or micoseconds."),
             elements=[
                 Integer(
                     title=_("Warning at"),
                     unit=_("ms/us"),
                     minvalue=1,
                     default_value=100,
                 ),
                 Integer(
                     title=_("Critical at"),
                     unit=_("ms/us"),
                     minvalue=1,
                     default_value=200,
                 ),
             ],
         )),
        ("latest_rtt_state",
         DropdownChoice(
             title=_("Latest RTT state"),
             choices=[
                 ('ok', _("OK")),
                 ('disconnected', _("disconnected")),
                 ('over treshold', _("over treshold")),
                 ('timeout', _("timeout")),
                 ('other', _("other")),
             ],
             default_value="ok",
         )),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="cisco_ip_sla",
        group=RulespecGroupCheckParametersNetworking,
        item_spec=_item_spec_cisco_ip_sla,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_cisco_ip_sla,
        title=lambda: _("Cisco IP SLA"),
    ))
