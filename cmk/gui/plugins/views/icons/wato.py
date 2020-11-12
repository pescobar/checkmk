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

import cmk.gui.config as config
from cmk.gui.globals import html
from cmk.gui.i18n import _
from cmk.gui.plugins.views import display_options
from cmk.gui.plugins.views.icons import Icon, icon_and_action_registry
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import cmk.gui.config as config
from cmk.gui.globals import html, request
from cmk.gui.i18n import _
from cmk.gui.plugins.views import display_options
from cmk.gui.plugins.views.icons import Icon, icon_and_action_registry
from cmk.gui.utils.urls import makeuri, makeuri_contextless
>>>>>>> upstream/master


@icon_and_action_registry.register
class WatoIcon(Icon):
    @classmethod
    def ident(cls):
        return "wato"

    def host_columns(self):
        return ['filename']

    def render(self, what, row, tags, custom_vars):
        def may_see_hosts():
            return config.user.may("wato.use") and \
              (config.user.may("wato.seeall") or config.user.may("wato.hosts"))

        if not may_see_hosts() or html.mobile:
<<<<<<< HEAD
            return

        wato_folder = _wato_folder_from_filename(row["host_filename"])
        if wato_folder is not None:
            if what == "host":
                return self._wato_link(wato_folder, row["site"], row["host_name"], "edithost")
            elif row["service_description"] in ["Check_MK inventory", "Check_MK Discovery"]:
                return self._wato_link(wato_folder, row["site"], row["host_name"], "inventory")

    def _wato_link(self, folder, site, hostname, where):
        if not config.wato_enabled:
            return
=======
            return None

        wato_folder = _wato_folder_from_filename(row["host_filename"])
        if wato_folder is None:
            return None

        if what == "host":
            return self._wato_link(wato_folder, row["site"], row["host_name"], "edithost")

        if row["service_description"] in ["Check_MK inventory", "Check_MK Discovery"]:
            return self._wato_link(wato_folder, row["site"], row["host_name"], "inventory")

    def _wato_link(self, folder, site, hostname, where):
        if not config.wato_enabled:
            return None
>>>>>>> upstream/master

        if display_options.enabled(display_options.X):
            url = "wato.py?folder=%s&host=%s" % \
              (html.urlencode(folder), html.urlencode(hostname))
            if where == "inventory":
                url += "&mode=inventory"
                help_txt = _("Edit services")
                icon = "services"
            else:
                url += "&mode=edit_host"
                help_txt = _("Edit this host")
                icon = "wato"
            return icon, help_txt, url
<<<<<<< HEAD
        else:
            return
=======

        return None
>>>>>>> upstream/master


@icon_and_action_registry.register
class DownloadAgentOutputIcon(Icon):
    """Action for downloading the current agent output."""
    @classmethod
    def ident(cls):
        return "download_agent_output"

    def default_sort_index(self):
        return 50

    def host_columns(self):
        return ["filename", "check_type"]

    def render(self, what, row, tags, custom_vars):
        return _paint_download_host_info(what, row, tags, custom_vars, ty="agent")  # pylint: disable=no-value-for-parameter


@icon_and_action_registry.register
class DownloadSnmpWalkIcon(Icon):
    """Action for downloading the current snmp output."""
    @classmethod
    def ident(cls):
        return "download_snmp_walk"

    def host_columns(self):
        return ["filename", "check_type"]

    def default_sort_index(self):
        return 50

    def render(self, what, row, tags, custom_vars):
        return _paint_download_host_info(what, row, tags, custom_vars, ty="walk")  # pylint: disable=no-value-for-parameter


def _paint_download_host_info(what, row, tags, host_custom_vars, ty):
    if (what == "host" or (what == "service" and row["service_description"] == "Check_MK")) \
       and config.user.may("wato.download_agent_output") \
<<<<<<< HEAD
       and not row["host_check_type"] == 2: # Not for shadow hosts
=======
       and not row["host_check_type"] == 2:  # Not for shadow hosts
>>>>>>> upstream/master

        # Not 100% acurate to use the tags here, but this is the best we can do
        # with the available information.
        # Render "download agent output" for non agent hosts, because there might
        # be piggyback data available which should be downloadable.
        if ty == "walk" and "snmp" not in tags:
            return
<<<<<<< HEAD
        elif ty == "agent" and "snmp" in tags and "tcp" not in tags:
=======

        if ty == "agent" and "snmp" in tags and "tcp" not in tags:
>>>>>>> upstream/master
            return

        params = [
            ("host", row["host_name"]),
            ("folder", _wato_folder_from_filename(row["host_filename"])),
            ("type", ty),
            ("_start", "1"),
        ]

        # When the download icon is part of the host/service action menu, then
        # the _back_url set in paint_action_menu() needs to be used. Otherwise
<<<<<<< HEAD
        # html.makeuri([]) (not html.requested_uri()) is the right choice.
        back_url = html.get_url_input("_back_url", html.makeuri([]))
=======
        # makeuri(request, []) (not html.requested_uri()) is the right choice.
        back_url = html.get_url_input("_back_url", makeuri(request, []))
>>>>>>> upstream/master
        if back_url:
            params.append(("back_url", back_url))

        if ty == "agent":
            title = _("Download agent output")
        else:
            title = _("Download SNMP walk")

<<<<<<< HEAD
        url = html.makeuri_contextless(params, filename="fetch_agent_output.py")
=======
        url = makeuri_contextless(request, params, filename="fetch_agent_output.py")
>>>>>>> upstream/master
        return "agent_output", title, url


def _wato_folder_from_filename(filename):
    if filename.startswith("/wato/") and filename.endswith("hosts.mk"):
        return filename[6:-8].rstrip("/")
