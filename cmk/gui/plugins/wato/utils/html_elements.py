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

from cmk.gui.i18n import _
from cmk.gui.globals import html
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import Optional

from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.breadcrumb import Breadcrumb
# TODO: Change all call sites to directly import from cmk.gui.page_menu
from cmk.gui.page_menu import PageMenu, search_form  # noqa: F401 # pylint: disable=unused-import
from cmk.gui.page_state import PageState
from cmk.gui.watolib.activate_changes import get_pending_changes_info
>>>>>>> upstream/master

# TODO: Refactor to context handler or similar?
_html_head_open = False


<<<<<<< HEAD
# Show confirmation dialog, send HTML-header if dialog is shown.
def wato_confirm(html_title, message):
    if not html.request.has_var("_do_confirm") and not html.request.has_var("_do_actions"):
        wato_html_head(html_title)
    return html.confirm(message)


=======
>>>>>>> upstream/master
def initialize_wato_html_head():
    global _html_head_open
    _html_head_open = False


<<<<<<< HEAD
def wato_html_head(title, *args, **kwargs):
=======
def wato_html_head(*,
                   title: str,
                   breadcrumb: Breadcrumb,
                   page_menu: Optional[PageMenu] = None,
                   show_body_start: bool = True,
                   show_top_heading: bool = True) -> None:
>>>>>>> upstream/master
    global _html_head_open

    if _html_head_open:
        return

    _html_head_open = True
<<<<<<< HEAD
    html.header(title, *args, **kwargs)
    html.open_div(class_="wato")


def wato_html_footer(*args, **kwargs):
=======
    html.header(title=title,
                breadcrumb=breadcrumb,
                page_menu=page_menu,
                page_state=_make_wato_page_state(),
                show_body_start=show_body_start,
                show_top_heading=show_top_heading)
    html.open_div(class_="wato")


def wato_html_footer(show_footer: bool = True, show_body_end: bool = True) -> None:
>>>>>>> upstream/master
    if not _html_head_open:
        return

    html.close_div()
<<<<<<< HEAD
    html.footer(*args, **kwargs)


# TODO: Cleanup all calls using title and remove the argument
def search_form(title=None, mode=None, default_value=""):
    html.begin_form("search", add_transid=False)
    if title:
        html.write_text(title + ' ')
    html.text_input("search", size=32, default_value=default_value)
    html.hidden_fields()
    if mode:
        html.hidden_field("mode", mode, add_var=True)
    html.set_focus("search")
    html.write_text(" ")
    html.button("_do_seach", _("Search"))
    html.end_form()
=======
    html.footer(show_footer, show_body_end)


def _make_wato_page_state() -> PageState:
    changes_info = get_pending_changes_info()
    return PageState(
        top_line=changes_info or _("No pending changes"),
        bottom_line=html.render_a(_("View changes"), href="wato.py?mode=changelog"),
        icon_name="wato_changes" if changes_info else "wato_nochanges",
    )
>>>>>>> upstream/master
