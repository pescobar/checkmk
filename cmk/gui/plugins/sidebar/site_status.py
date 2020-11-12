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
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

import json

from cmk.gui.i18n import _
from cmk.gui.globals import html
import cmk.gui.sites as sites
import cmk.gui.config as config

<<<<<<< HEAD
from . import (
=======
from cmk.gui.plugins.sidebar import (
>>>>>>> upstream/master
    SidebarSnapin,
    snapin_registry,
    render_link,
)


@snapin_registry.register
class SiteStatus(SidebarSnapin):
    @staticmethod
    def type_name():
        return "sitestatus"

    @classmethod
    def refresh_regularly(cls):
        return True

    @classmethod
    def title(cls):
        return _("Site Status")

    @classmethod
    def description(cls):
        return _("Connection state of each site and button for enabling "
                 "and disabling the site connection")

<<<<<<< HEAD
    def show(self):
        html.open_table(cellspacing=0, class_="sitestate")
=======
    def show(self) -> None:
        html.open_table(cellspacing="0", class_="sitestate")
>>>>>>> upstream/master

        sites.update_site_states_from_dead_sites()

        for sitename, _sitealias in config.sorted_sites():
            site = config.site(sitename)

<<<<<<< HEAD
            state = sites.states().get(sitename, {}).get("state")
=======
            state = sites.states().get(sitename, sites.SiteStatus({})).get("state")
>>>>>>> upstream/master

            if state is None:
                state = "missing"
                switch = "missing"
                text = sitename

            else:
                if state == "disabled":
                    switch = "on"
                    text = site["alias"]
                else:
                    switch = "off"
                    text = render_link(site["alias"],
                                       "view.py?view_name=sitehosts&site=%s" % sitename)

            html.open_tr()
            html.open_td(class_="left")
            html.write(text)
            html.close_td()
            html.open_td(class_="state")
            if switch == "missing":
                html.status_label(content=state, status=state, title=_("Site is missing"))
            else:
                url = html.makeactionuri_contextless([
                    ("_site_switch", "%s:%s" % (sitename, switch)),
                ],
                                                     filename="switch_site.py")
                html.status_label_button(
                    content=state,
                    status=state,
                    title=_("enable this site") if state == "disabled" else _("disable this site"),
                    onclick="cmk.sidebar.switch_site(%s)" % (json.dumps(url)))
            html.close_tr()
        html.close_table()

    @classmethod
    def allowed_roles(cls):
        return ["user", "admin"]

    def page_handlers(self):
        return {
            "switch_site": self._ajax_switch_site,
        }

    def _ajax_switch_site(self):
        html.set_output_format("json")
        # _site_switch=sitename1:on,sitename2:off,...
        if not config.user.may("sidesnap.sitestatus"):
            return

        if not html.check_transaction():
            return

        switch_var = html.request.var("_site_switch")
        if switch_var:
            for info in switch_var.split(","):
                sitename, onoff = info.split(":")
                if sitename not in config.sitenames():
                    continue

<<<<<<< HEAD
                d = config.user.siteconf.get(sitename, {})
                d["disabled"] = onoff != "on"
                config.user.siteconf[sitename] = d
=======
                if onoff == "on":
                    config.user.enable_site(sitename)
                else:
                    config.user.disable_site(sitename)

>>>>>>> upstream/master
            config.user.save_site_config()
