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
"""Module for managing the new rule based notifications"""

import cmk.utils.store as store

import cmk.gui.config as config
from cmk.gui.watolib.utils import wato_root_dir


def load_notification_rules(lock=False):
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Module for managing the new rule based notifications"""

from typing import Dict, List
import cmk.utils.store as store
from cmk.utils.type_defs import UserId, EventRule

import cmk.gui.config as config
import cmk.gui.userdb as userdb
from cmk.gui.watolib.utils import wato_root_dir


def load_notification_rules(lock: bool = False) -> List[Dict]:
>>>>>>> upstream/master
    filename = wato_root_dir() + "notifications.mk"
    notification_rules = store.load_from_mk_file(filename, "notification_rules", [], lock=lock)

    # Convert to new plugin configuration format
    for rule in notification_rules:
        if "notify_method" in rule:
            method = rule["notify_method"]
            plugin = rule["notify_plugin"]
            del rule["notify_method"]
            rule["notify_plugin"] = (plugin, method)

    return notification_rules


<<<<<<< HEAD
def save_notification_rules(rules):
=======
def save_notification_rules(rules: List[Dict]) -> None:
>>>>>>> upstream/master
    store.mkdir(wato_root_dir())
    store.save_to_mk_file(wato_root_dir() + "notifications.mk",
                          "notification_rules",
                          rules,
                          pprint_value=config.wato_pprint_config)
<<<<<<< HEAD
=======


def load_user_notification_rules() -> Dict[UserId, List[EventRule]]:
    rules = {}
    for user_id, user in userdb.load_users().items():
        user_rules = user.get("notification_rules")
        if user_rules:
            rules[user_id] = user_rules
    return rules
>>>>>>> upstream/master
