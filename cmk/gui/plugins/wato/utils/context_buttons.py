<<<<<<< HEAD
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

import cmk.gui.watolib as watolib
from cmk.gui.i18n import _
from cmk.gui.globals import html


def global_buttons():
    changelog_button()
    home_button()


def home_button():
    html.context_button(_("Main Menu"), watolib.folder_preserving_link([("mode", "main")]), "home")


def changelog_button():
    pending_info = watolib.get_pending_changes_info()
    if pending_info:
        hot = True
        icon = "wato_changes"
        buttontext = pending_info
    else:
        hot = False
        icon = "wato_nochanges"
        buttontext = _("No changes")
    html.context_button(buttontext, watolib.folder_preserving_link([("mode", "changelog")]), icon,
                        hot)


def host_status_button(hostname, viewname):
    html.context_button(
        _("Status"), "view.py?" + html.urlencode_vars([
            ("view_name", viewname),
            ("filename", watolib.Folder.current().path() + "/hosts.mk"),
            ("host", hostname),
            ("site", ""),
        ]), "status")


def service_status_button(hostname, servicedesc):
    html.context_button(
        _("Status"), "view.py?" + html.urlencode_vars([
            ("view_name", "service"),
            ("host", hostname),
            ("service", servicedesc),
        ]), "status")


def folder_status_button(viewname="allhosts"):
    html.context_button(
        _("Status"), "view.py?" + html.urlencode_vars([
            ("view_name", viewname),
            ("wato_folder", watolib.Folder.current().path()),
        ]), "status")
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import cmk.gui.watolib as watolib
from cmk.gui.i18n import _
from cmk.gui.globals import request
from cmk.gui.page_menu import PageMenuEntry, make_simple_link
from cmk.gui.utils.urls import makeuri_contextless


def make_host_status_link(host_name: str, view_name: str) -> PageMenuEntry:
    return PageMenuEntry(
        title=_("Monitoring status"),
        icon_name="status",
        item=make_simple_link(
            makeuri_contextless(
                request,
                [
                    ("view_name", view_name),
                    ("filename", watolib.Folder.current().path() + "/hosts.mk"),
                    ("host", host_name),
                    ("site", ""),
                ],
                filename="view.py",
            )),
    )


def make_service_status_link(host_name: str, service_name: str) -> PageMenuEntry:
    return PageMenuEntry(
        title=_("Monitoring status"),
        icon_name="status",
        item=make_simple_link(
            makeuri_contextless(
                request,
                [
                    ("view_name", "service"),
                    ("host", host_name),
                    ("service", service_name),
                ],
                filename="view.py",
            )),
    )


def make_folder_status_link(folder: watolib.CREFolder, view_name: str) -> PageMenuEntry:
    return PageMenuEntry(
        title=_("Status"),
        icon_name="status",
        item=make_simple_link(
            makeuri_contextless(
                request,
                [
                    ("view_name", view_name),
                    ("wato_folder", folder.path()),
                ],
                filename="view.py",
            )),
    )
>>>>>>> upstream/master
