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
"""Mode for searching hosts"""

=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Mode for searching hosts"""

from typing import Optional, Type

>>>>>>> upstream/master
import cmk.gui.watolib as watolib
import cmk.gui.forms as forms
from cmk.gui.valuespec import TextAscii

from cmk.gui.plugins.wato.utils import mode_registry, configure_attributes
<<<<<<< HEAD
from cmk.gui.plugins.wato.utils.base_modes import WatoMode
from cmk.gui.plugins.wato.utils.context_buttons import global_buttons
=======
from cmk.gui.plugins.wato.utils.base_modes import WatoMode, ActionResult, redirect, mode_url
from cmk.gui.wato.pages.folders import ModeFolder
from cmk.gui.breadcrumb import Breadcrumb
from cmk.gui.page_menu import (
    PageMenu,
    make_simple_form_page_menu,
)
>>>>>>> upstream/master

from cmk.gui.globals import html
from cmk.gui.i18n import _


@mode_registry.register
class ModeSearch(WatoMode):
    @classmethod
    def name(cls):
        return "search"

    @classmethod
    def permissions(cls):
        return ["hosts"]

<<<<<<< HEAD
=======
    @classmethod
    def parent_mode(cls) -> Optional[Type[WatoMode]]:
        return ModeFolder

>>>>>>> upstream/master
    def __init__(self):
        super(ModeSearch, self).__init__()
        self._folder = watolib.Folder.current()

<<<<<<< HEAD
    def title(self):
        return _("Search for hosts below %s") % self._folder.title()

    def buttons(self):
        global_buttons()
        html.context_button(_("Folder"), self._folder.url(), "back")

    def action(self):
        return "folder"

    def page(self):
        self._folder.show_breadcrump()

        # Show search form
        html.begin_form("edit_host", method="GET")
=======
    def page_menu(self, breadcrumb: Breadcrumb) -> PageMenu:
        return make_simple_form_page_menu(breadcrumb,
                                          form_name="edit_host",
                                          button_name="_local",
                                          save_title=_("Search"),
                                          save_icon="search",
                                          save_is_enabled=True)

    def title(self):
        return _("Search for hosts below %s") % self._folder.title()

    def action(self) -> ActionResult:
        self._remove_unused_search_vars()
        return redirect(mode_url("folder", folder=self._folder.path()))

    def _remove_unused_search_vars(self):
        """Reduce the HTTP vars (html.request.vars) to the amount of necessary attributes

        The form submits all variables which may result in a too big collection for being
        used as URL variables. Once we are here we can analyze the attribute checkboxes and
        remove all HTTP variables that are related to not checked checkboxes for preventing
        the too long URLs.
        """
        keep_vars = {}

        if html.request.has_var("host_search_host"):
            keep_vars["host_search_host"] = html.request.get_ascii_input_mandatory(
                "host_search_host")

        for varname, value in html.request.itervars(prefix="host_search_change_"):
            if html.get_checkbox(varname) is False:
                continue

            keep_vars[varname] = value

            attr_ident = varname.split("host_search_change_", 1)[1]

            # The URL variable naming scheme is not clear. Try to match with "attr_" prefix
            # and without. We should investigate and clean this up.
            attr_prefix = "host_search_attr_%s" % attr_ident
            keep_vars.update(html.request.itervars(prefix=attr_prefix))
            attr_prefix = "host_search_%s" % attr_ident
            keep_vars.update(html.request.itervars(prefix=attr_prefix))

        html.request.del_vars("host_search_")
        for varname, value in keep_vars.items():
            html.request.set_var(varname, value)

    def page(self):
        # Show search form
        html.begin_form("edit_host", method="POST")
>>>>>>> upstream/master
        html.prevent_password_auto_completion()

        basic_attributes = [
            ("host_search_host", TextAscii(title=_("Hostname",)), ""),
        ]
        html.set_focus("host_search_host")

        # Attributes
        configure_attributes(
            new=False,
            hosts={},
            for_what="host_search",
            parent=None,
            varprefix="host_search_",
            basic_attributes=basic_attributes,
        )

<<<<<<< HEAD
        # Button
        forms.end()
        html.button("_local", _("Search in %s") % self._folder.title(), "submit")
=======
        forms.end()
>>>>>>> upstream/master
        html.hidden_field("host_search", "1")
        html.hidden_fields()
        html.end_form()
