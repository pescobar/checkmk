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
"""This module allows the creation of large numbers of random hosts
for test and development."""

import random

=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""This module allows the creation of large numbers of random hosts
for test and development."""

from typing import List, Tuple, Dict, Optional, Type

import random

from cmk.utils.type_defs import HostName

>>>>>>> upstream/master
import cmk.gui.watolib as watolib
import cmk.gui.forms as forms
from cmk.gui.i18n import _
from cmk.gui.globals import html
<<<<<<< HEAD

from cmk.gui.plugins.wato import (
    WatoMode,
    mode_registry,
)
=======
from cmk.gui.breadcrumb import Breadcrumb
from cmk.gui.page_menu import PageMenu, make_simple_form_page_menu
from cmk.gui.wato.pages.folders import ModeFolder
from cmk.gui.plugins.wato import (WatoMode, ActionResult, mode_registry, flash, redirect, mode_url)
>>>>>>> upstream/master


@mode_registry.register
class ModeRandomHosts(WatoMode):
    @classmethod
    def name(cls):
        return "random_hosts"

    @classmethod
    def permissions(cls):
        return ["hosts", "random_hosts"]

    def title(self):
<<<<<<< HEAD
        return _("Random Hosts")

    def buttons(self):
        html.context_button(_("Folder"), watolib.Folder.current().url(), "back")

    def action(self):
        if not html.check_transaction():
            return "folder"

        count = int(html.request.var("count"))
        folders = int(html.request.var("folders"))
        levels = int(html.request.var("levels"))
        created = self._create_random_hosts(watolib.Folder.current(), count, folders, levels)
        return "folder", _("Created %d random hosts.") % created

    def page(self):
        html.begin_form("random")
        forms.header(_("Create Random Hosts"))
        forms.section(_("Number to create"))
        html.write_text("%s: " % _("Hosts to create in each folder"))
        html.number_input("count", 10)
        html.set_focus("count")
        html.br()
        html.write_text("%s: " % _("Number of folders to create in each level"))
        html.number_input("folders", 10)
        html.br()
        html.write_text("%s: " % _("Levels of folders to create"))
        html.number_input("levels", 1)

        forms.end()
        html.button("start", _("Start!"), "submit")
=======
        return _("Add random hosts")

    @classmethod
    def parent_mode(cls) -> Optional[Type[WatoMode]]:
        return ModeFolder

    def page_menu(self, breadcrumb: Breadcrumb) -> PageMenu:
        return make_simple_form_page_menu(
            breadcrumb,
            form_name="random",
            button_name="start",
            save_title=_("Start!"),
        )

    def action(self) -> ActionResult:
        if not html.check_transaction():
            return redirect(mode_url("folder", folder=watolib.Folder.current().path()))

        count = html.request.get_integer_input_mandatory("count")
        folders = html.request.get_integer_input_mandatory("folders")
        levels = html.request.get_integer_input_mandatory("levels")
        created = self._create_random_hosts(watolib.Folder.current(), count, folders, levels)
        flash(_("Added %d random hosts.") % created)
        return redirect(mode_url("folder", folder=watolib.Folder.current().path()))

    def page(self):
        html.begin_form("random")
        forms.header(_("Add random hosts"))
        forms.section(_("Number to create"))
        html.write_text("%s: " % _("Hosts to create in each folder"))
        html.text_input("count", default_value="10", cssclass="number")
        html.set_focus("count")
        html.br()
        html.write_text("%s: " % _("Number of folders to create in each level"))
        html.text_input("folders", default_value="10", cssclass="number")
        html.br()
        html.write_text("%s: " % _("Levels of folders to create"))
        html.text_input("levels", default_value="1", cssclass="number")

        forms.end()
>>>>>>> upstream/master
        html.hidden_fields()
        html.end_form()

    def _create_random_hosts(self, folder, count, folders, levels):
        if levels == 0:
<<<<<<< HEAD
            hosts_to_create = []
=======
            hosts_to_create: List[Tuple[HostName, Dict, None]] = []
>>>>>>> upstream/master
            while len(hosts_to_create) < count:
                host_name = "random_%010d" % int(random.random() * 10000000000)
                hosts_to_create.append((host_name, {"ipaddress": "127.0.0.1"}, None))
            folder.create_hosts(hosts_to_create)
            return count

        total_created = 0
        created = 0
        while created < folders:
            created += 1
            i = 1
            while True:
                folder_name = "folder_%02d" % i
                if not folder.has_subfolder(folder_name):
                    break
                i += 1

            subfolder = folder.create_subfolder(folder_name, "Subfolder %02d" % i, {})
            total_created += self._create_random_hosts(subfolder, count, folders, levels - 1)
        return total_created
