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

from cmk.utils.plugin_loader import load_plugins

#.
#   .--Plugin API----------------------------------------------------------.
#   |           ____  _             _            _    ____ ___             |
#   |          |  _ \| |_   _  __ _(_)_ __      / \  |  _ \_ _|            |
#   |          | |_) | | | | |/ _` | | '_ \    / _ \ | |_) | |             |
#   |          |  __/| | |_| | (_| | | | | |  / ___ \|  __/| |             |
#   |          |_|   |_|\__,_|\__, |_|_| |_| /_/   \_\_|  |___|            |
#   |                         |___/                                        |
#   '----------------------------------------------------------------------'

<<<<<<< HEAD
from cmk.gui.plugins.sidebar.utils import (
    SidebarSnapin,
    CustomizableSidebarSnapin,
    snapin_registry,
    snapin_width,
    snapin_site_choice,
    visuals_by_topic,
    render_link,
    heading,
    link,
    simplelink,
    bulletlink,
    iconlink,
    nagioscgilink,
    footnotelinks,
    begin_footnote_links,
    end_footnote_links,
    write_snapin_exception,
=======
from cmk.gui.plugins.sidebar.utils import (  # noqa: F401 # pylint: disable=unused-import
    SidebarSnapin, PageHandlers, CustomizableSidebarSnapin, snapin_registry, snapin_width,
    snapin_site_choice, make_topic_menu, render_link, heading, link, simplelink, bulletlink,
    iconlink, nagioscgilink, footnotelinks, begin_footnote_links, end_footnote_links,
    write_snapin_exception, show_topic_menu,
>>>>>>> upstream/master
)

#.
#   .--Plugins-------------------------------------------------------------.
#   |                   ____  _             _                              |
#   |                  |  _ \| |_   _  __ _(_)_ __  ___                    |
#   |                  | |_) | | | | |/ _` | | '_ \/ __|                   |
#   |                  |  __/| | |_| | (_| | | | | \__ \                   |
#   |                  |_|   |_|\__,_|\__, |_|_| |_|___/                   |
#   |                                 |___/                                |
#   '----------------------------------------------------------------------'

load_plugins(__file__, __package__)
