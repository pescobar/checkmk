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

import cmk.gui.pages
import cmk.gui.config as config
import cmk.gui.utils as utils
<<<<<<< HEAD
from cmk.gui.globals import html


@cmk.gui.pages.register("index")
def page_index():
    html.write(
        '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">\n'
        '<html><head>\n')
    html.default_html_headers()
    html.write("""<title>%s</title>
</head>
<frameset cols="280,*" frameborder="0" framespacing="0" border="0">
    <frame src="side.py" name="side" noresize scrolling="no">
    <frame src="%s" name="main" noresize>
</frameset>
</html>
""" % (html.attrencode(config.get_page_heading()), html.attrencode(_get_start_url())))


def _get_start_url():
=======
from cmk.gui.globals import html, request
from cmk.gui.sidebar import SidebarRenderer
from cmk.gui.exceptions import HTTPRedirect
from cmk.gui.utils.urls import makeuri


@cmk.gui.pages.register("index")
def page_index() -> None:
    # Redirect to mobile GUI if we are a mobile device and the index is requested
    if html.is_mobile():
        raise HTTPRedirect(makeuri(request, [], filename="mobile.py"))

    title = config.get_page_heading()
    content = html.render_iframe("", src=_get_start_url(), name="main")
    SidebarRenderer().show(title, content)


def _get_start_url() -> str:
>>>>>>> upstream/master
    default_start_url = config.user.get_attribute("start_url", config.start_url) or config.start_url
    if not utils.is_allowed_url(default_start_url):
        default_start_url = "dashboard.py"

    return html.get_url_input("start_url", default_start_url)
