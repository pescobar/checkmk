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

# TODO: Split this file into single snapin or topic files

# TODO: Refactor all snapins to the new snapin API and move page handlers
#       from sidebar.py to the snapin objects that need these pages.
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import List, Tuple
>>>>>>> upstream/master

import cmk.gui.config as config
import cmk.gui.views as views
import cmk.gui.dashboard as dashboard
import cmk.gui.pagetypes as pagetypes
<<<<<<< HEAD
from cmk.gui.plugins.sidebar import (
    SidebarSnapin,
    snapin_registry,
    visuals_by_topic,
    bulletlink,
    footnotelinks,
)
from cmk.gui.i18n import _
from cmk.gui.globals import html
=======
from cmk.gui.main_menu import mega_menu_registry
from cmk.gui.type_defs import MegaMenu, TopicMenuTopic, Visual
from cmk.gui.plugins.sidebar import (
    SidebarSnapin,
    snapin_registry,
    footnotelinks,
    make_topic_menu,
    show_topic_menu,
    search,
)
from cmk.gui.i18n import _, _l
from cmk.gui.node_visualization import ParentChildTopologyPage
>>>>>>> upstream/master


@snapin_registry.register
class Views(SidebarSnapin):
    @staticmethod
    def type_name():
        return "views"

    @classmethod
    def title(cls):
        return _("Views")

    @classmethod
    def description(cls):
        return _("Links to global views and dashboards")

    def show(self):
<<<<<<< HEAD
        dashboard.load_dashboards()

        def render_topic(topic, entries):
            first = True
            for t, title, name, is_view in entries:
                if is_view and config.visible_views and name not in config.visible_views:
                    continue
                if is_view and config.hidden_views and name in config.hidden_views:
                    continue
                if t == topic:
                    if first:
                        html.begin_foldable_container("views", topic, False, topic, indent=True)
                        first = False
                    if is_view:
                        bulletlink(title,
                                   "view.py?view_name=%s" % name,
                                   onclick="return cmk.sidebar.wato_views_clicked(this)")
                    elif "?name=" in name:
                        bulletlink(title, name)
                    else:
                        bulletlink(title,
                                   'dashboard.py?name=%s' % name,
                                   onclick="return cmk.sidebar.wato_views_clicked(this)")

            # TODO: One day pagestypes should handle the complete snapin.
            # for page_type in pagetypes.all_page_types().values():
            #     if issubclass(page_type, pagetypes.PageRenderer):
            #         for t, title, url in page_type.sidebar_links():
            #             if t == topic:
            #                 bulletlink(title, url)

            if not first:  # at least one item rendered
                html.end_foldable_container()

        # TODO: One bright day drop this whole visuals stuff and only use page_types
        page_type_topics = {}
        for page_type in pagetypes.all_page_types().values():
            if issubclass(page_type, pagetypes.PageRenderer):
                for t, title, url in page_type.sidebar_links():
                    page_type_topics.setdefault(t, []).append((t, title, url, False))

        visuals_topics_with_entries = visuals_by_topic(views.get_permitted_views().items() +
                                                       dashboard.permitted_dashboards().items())
        all_topics_with_entries = []
        for topic, entries in visuals_topics_with_entries:
            if topic in page_type_topics:
                entries = entries + page_type_topics[topic]
                del page_type_topics[topic]
            all_topics_with_entries.append((topic, entries))

        all_topics_with_entries += sorted(page_type_topics.items())

        for topic, entries in all_topics_with_entries:
            render_topic(topic, entries)
=======
        show_topic_menu(treename="views", menu=get_view_menu_items())
>>>>>>> upstream/master

        links = []
        if config.user.may("general.edit_views"):
            if config.debug:
                links.append((_("Export"), "export_views.py"))
            links.append((_("Edit"), "edit_views.py"))
            footnotelinks(links)
<<<<<<< HEAD
=======


def get_view_menu_items() -> List[TopicMenuTopic]:
    # The page types that are implementing the PageRenderer API should also be
    # part of the menu. Bring them into a visual like structure to make it easy to
    # integrate them.
    page_type_items: List[Tuple[str, Tuple[str, Visual]]] = []
    for page_type in pagetypes.all_page_types().values():
        if not issubclass(page_type, pagetypes.PageRenderer):
            continue

        for page in page_type.pages():
            if page._show_in_sidebar():
                visual = page.internal_representation().copy()
                visual["hidden"] = False  # Is currently to configurable for pagetypes
                visual["icon"] = None  # Is currently to configurable for pagetypes

                page_type_items.append((page_type.type_name(), (page.name(), visual)))

    # Apply some view specific filters
    views_to_show = [(name, view)
                     for name, view in views.get_permitted_views().items()
                     if (not config.visible_views or name in config.visible_views) and
                     (not config.hidden_views or name not in config.hidden_views)]

    network_topology_visual_spec = ParentChildTopologyPage.visual_spec()
    pages_to_show = [(network_topology_visual_spec["name"], network_topology_visual_spec)]

    visuals_to_show = [("views", e) for e in views_to_show]
    visuals_to_show += [("dashboards", e) for e in dashboard.get_permitted_dashboards().items()]
    visuals_to_show += [("pages", e) for e in pages_to_show]
    visuals_to_show += page_type_items

    return make_topic_menu(visuals_to_show)


mega_menu_registry.register(
    MegaMenu(
        name="monitoring",
        title=_l("Monitor"),
        icon="main_monitoring",
        sort_index=5,
        topics=get_view_menu_items,
        search=search.MonitoringSearch("monitoring_search"),
    ))
>>>>>>> upstream/master
