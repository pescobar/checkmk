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
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersStorage,
)


<<<<<<< HEAD
def _parameter_valuespec_ddn_s2a_port_errors():
    return Dictionary(elements=[
        ("link_failure_errs",
         Tuple(
             title=_(u"Link failure errors"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
def _parameter_valuespec_ddn_s2a_port_errors() -> Dictionary:
    return Dictionary(elements=[
        ("link_failure_errs",
         Tuple(
             title=_("Link failure errors"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("lost_sync_errs",
         Tuple(
<<<<<<< HEAD
             title=_(u"Lost synchronization errors"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("Lost synchronization errors"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("loss_of_signal_errs",
         Tuple(
<<<<<<< HEAD
             title=_(u"Loss of signal errors"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("Loss of signal errors"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("prim_seq_errs",
         Tuple(
<<<<<<< HEAD
             title=_(u"PrimSeq erros"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("PrimSeq erros"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("crc_errs",
         Tuple(
<<<<<<< HEAD
             title=_(u"CRC errors"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("CRC errors"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("receive_errs",
         Tuple(
<<<<<<< HEAD
             title=_(u"Receive errors"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("Receive errors"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("ctio_timeouts",
         Tuple(
<<<<<<< HEAD
             title=_(u"CTIO timeouts"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("CTIO timeouts"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("ctio_xmit_errs",
         Tuple(
<<<<<<< HEAD
             title=_(u"CTIO transmission errors"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("CTIO transmission errors"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
        ("ctio_other_errs",
         Tuple(
<<<<<<< HEAD
             title=_(u"other CTIO errors"),
             elements=[
                 Integer(title=_(u"Warning at")),
                 Integer(title=_(u"Critical at")),
=======
             title=_("other CTIO errors"),
             elements=[
                 Integer(title=_("Warning at")),
                 Integer(title=_("Critical at")),
>>>>>>> upstream/master
             ],
         )),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="ddn_s2a_port_errors",
        group=RulespecGroupCheckParametersStorage,
        item_spec=lambda: TextAscii(title="Port index"),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_ddn_s2a_port_errors,
<<<<<<< HEAD
        title=lambda: _("Port errors of DDN S2A devices"),
=======
        title=lambda: _("DDN S2A port errors"),
>>>>>>> upstream/master
    ))
