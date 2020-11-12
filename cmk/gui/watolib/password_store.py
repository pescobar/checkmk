<<<<<<< HEAD
#!/usr/bin/env python
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

from pathlib2 import Path
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from pathlib import Path
>>>>>>> upstream/master

import cmk.gui.config as config
import cmk.gui.userdb as userdb
from cmk.gui.watolib.simple_config_file import WatoSimpleConfigFile
from cmk.gui.watolib.utils import wato_root_dir


class PasswordStore(WatoSimpleConfigFile):
    def __init__(self):
        super(PasswordStore, self).__init__(config_file_path=Path(wato_root_dir()) / "passwords.mk",
                                            config_variable="stored_passwords")

    def filter_usable_entries(self, entries):
        if config.user.may("wato.edit_all_passwords"):
            return entries

<<<<<<< HEAD
        user_groups = userdb.contactgroups_of_user(config.user.id)

        passwords = self.filter_editable_entries(entries)
        passwords.update(
            dict([(k, v) for k, v in entries.items() if v["shared_with"] in user_groups]))
=======
        assert config.user.id is not None
        user_groups = userdb.contactgroups_of_user(config.user.id)

        passwords = self.filter_editable_entries(entries)
        passwords.update({k: v for k, v in entries.items() if v["shared_with"] in user_groups})
>>>>>>> upstream/master
        return passwords

    def filter_editable_entries(self, entries):
        if config.user.may("wato.edit_all_passwords"):
            return entries

<<<<<<< HEAD
        user_groups = userdb.contactgroups_of_user(config.user.id)
        return dict([(k, v) for k, v in entries.items() if v["owned_by"] in user_groups])
=======
        assert config.user.id is not None
        user_groups = userdb.contactgroups_of_user(config.user.id)
        return {k: v for k, v in entries.items() if v["owned_by"] in user_groups}
>>>>>>> upstream/master
