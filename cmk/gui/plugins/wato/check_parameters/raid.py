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
from cmk.gui.valuespec import TextAscii
from cmk.gui.plugins.wato import (
<<<<<<< HEAD
    RulespecGroupManualChecksStorage,
=======
    RulespecGroupEnforcedServicesStorage,
>>>>>>> upstream/master
    ManualCheckParameterRulespec,
    rulespec_registry,
)


def _item_spec_raid():
    return TextAscii(
        title=_("Name of the device"),
        help=_("For Linux MD specify the device name without the "
               "<tt>/dev/</tt>, e.g. <tt>md0</tt>, for hardware raids "
               "please refer to the manual of the actual check being used."),
    )


rulespec_registry.register(
    ManualCheckParameterRulespec(
        check_group_name="raid",
<<<<<<< HEAD
        group=RulespecGroupManualChecksStorage,
=======
        group=RulespecGroupEnforcedServicesStorage,
>>>>>>> upstream/master
        item_spec=_item_spec_raid,
        title=lambda: _("RAID: overall state"),
    ))
