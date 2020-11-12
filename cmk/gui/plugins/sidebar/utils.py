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
"""Module to hold shared code for module internals and the plugins"""

import abc
import traceback
import json
<<<<<<< HEAD
import six

import cmk.utils.plugin_registry

import cmk.gui.pages
import cmk.gui.config as config
from cmk.gui.i18n import _, _u
from cmk.gui.globals import html
=======
from typing import Optional, Any, Dict, List, Tuple, Type

import cmk.utils.plugin_registry

from cmk.gui.sites import SiteId
import cmk.gui.pages
import cmk.gui.config as config
import cmk.gui.escaping as escaping
import cmk.gui.pagetypes as pagetypes
from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.type_defs import Choices
from cmk.gui.type_defs import RoleName, PermissionName, Visual
>>>>>>> upstream/master
from cmk.gui.permissions import (
    permission_section_registry,
    PermissionSection,
    declare_permission,
)
<<<<<<< HEAD
=======
from cmk.gui.type_defs import (
    TopicMenuTopic,
    TopicMenuItem,
)

# TODO: Actually this is cmk.gui.sidebar.CustomSnapins, but we run into a hell
# of cycles and untyped dependencies. So for now this is just a reminder.
CustomSnapins = Any
>>>>>>> upstream/master

# Constants to be used in snapins
snapin_width = 230

<<<<<<< HEAD
search_plugins = []
=======
search_plugins: List = []

PageHandlers = Dict[str, "cmk.gui.pages.PageHandlerFunc"]
>>>>>>> upstream/master


@permission_section_registry.register
class PermissionSectionSidebarSnapins(PermissionSection):
    @property
<<<<<<< HEAD
    def name(self):
        return "sidesnap"

    @property
    def title(self):
        return _("Sidebar snapins")

    @property
    def do_sort(self):
=======
    def name(self) -> str:
        return "sidesnap"

    @property
    def title(self) -> str:
        return _("Sidebar snapins")

    @property
    def do_sort(self) -> bool:
>>>>>>> upstream/master
        return True


# TODO: Transform methods to class methods
<<<<<<< HEAD
class SidebarSnapin(six.with_metaclass(abc.ABCMeta, object)):
    """Abstract base class for all sidebar snapins"""
    @classmethod
    @abc.abstractmethod
    def type_name(cls):
=======
class SidebarSnapin(metaclass=abc.ABCMeta):
    """Abstract base class for all sidebar snapins"""
    @classmethod
    @abc.abstractmethod
    def type_name(cls) -> str:
>>>>>>> upstream/master
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
<<<<<<< HEAD
    def title(cls):
=======
    def title(cls) -> str:
>>>>>>> upstream/master
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
<<<<<<< HEAD
    def description(cls):
        raise NotImplementedError()

    @abc.abstractmethod
    def show(self):
        raise NotImplementedError()

    @classmethod
    def refresh_regularly(cls):
        return False

    @classmethod
    def refresh_on_restart(cls):
        return False

    @classmethod
    def is_customizable(cls):
        """Whether or not a snapin type can be used for custom snapins"""
        return False

    @classmethod
    def is_custom_snapin(cls):
=======
    def description(cls) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def show(self) -> None:
        raise NotImplementedError()

    @classmethod
    def has_show_more_items(cls) -> bool:
        return False

    @classmethod
    def refresh_regularly(cls) -> bool:
        return False

    @classmethod
    def refresh_on_restart(cls) -> bool:
        return False

    @classmethod
    def is_custom_snapin(cls) -> bool:
>>>>>>> upstream/master
        """Whether or not a snapin type is a customized snapin"""
        return False

    @classmethod
<<<<<<< HEAD
    def permission_name(cls):
        return "sidesnap.%s" % cls.type_name()

    @classmethod
    def allowed_roles(cls):
        return ["admin", "user", "guest"]

    def styles(self):
        return None

    def page_handlers(self):
        return {}


class CustomizableSidebarSnapin(six.with_metaclass(abc.ABCMeta, SidebarSnapin)):
=======
    def permission_name(cls) -> PermissionName:
        return "sidesnap.%s" % cls.type_name()

    @classmethod
    def allowed_roles(cls) -> List[RoleName]:
        return ["admin", "user", "guest"]

    def styles(self) -> Optional[str]:
        return None

    def page_handlers(self) -> PageHandlers:
        return {}


class CustomizableSidebarSnapin(SidebarSnapin, metaclass=abc.ABCMeta):
>>>>>>> upstream/master
    """Parent for all user configurable sidebar snapins

    Subclass this class in case you want to implement a sidebar snapin type that can
    be customized by the user"""
    @classmethod
<<<<<<< HEAD
    def is_customizable(cls):
        """Whether or not a snapin type can be used for custom snapins"""
        return True

    @classmethod
=======
>>>>>>> upstream/master
    @abc.abstractmethod
    def vs_parameters(cls):
        """The Dictionary() elements to be used for configuring the parameters"""
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def parameters(cls):
        """Default set of parameters to be used for the uncustomized snapin"""
        raise NotImplementedError()


<<<<<<< HEAD
class SnapinRegistry(cmk.utils.plugin_registry.ClassRegistry):
    """The management object for all available plugins."""
    def plugin_base_class(self):
        return SidebarSnapin

    def plugin_name(self, plugin_class):
        return plugin_class.type_name()

    def registration_hook(self, plugin_class):
        declare_permission(
            "sidesnap.%s" % self.plugin_name(plugin_class),
            plugin_class.title(),
            plugin_class.description(),
            plugin_class.allowed_roles(),
        )

        for path, page_func in plugin_class().page_handlers().items():
            cmk.gui.pages.register_page_handler(path, page_func)

    def get_customizable_snapin_types(self):
        return [(snapin_type_id, snapin_type)
                for snapin_type_id, snapin_type in self.items()
                if snapin_type.is_customizable() and not snapin_type.is_custom_snapin()]

    def register_custom_snapins(self, custom_snapins):
=======
# TODO: We should really register instances instead of classes here... :-/ Using
# classes obfuscates the code and makes typing a nightmare.
class SnapinRegistry(cmk.utils.plugin_registry.Registry[Type[SidebarSnapin]]):
    """The management object for all available plugins."""
    def plugin_name(self, instance):
        return instance.type_name()

    def registration_hook(self, instance: Type[SidebarSnapin]) -> None:
        declare_permission(
            "sidesnap.%s" % self.plugin_name(instance),
            instance.title(),
            instance.description(),
            instance.allowed_roles(),
        )

        for path, page_func in instance().page_handlers().items():
            cmk.gui.pages.register_page_handler(path, page_func)

    def get_customizable_snapin_types(self) -> List[Tuple[str, Type[CustomizableSidebarSnapin]]]:
        return [(snapin_type_id, snapin_type)
                for snapin_type_id, snapin_type in self.items()
                if (issubclass(snapin_type, CustomizableSidebarSnapin) and
                    not snapin_type.is_custom_snapin())]

    def register_custom_snapins(self, custom_snapins: List[CustomSnapins]) -> None:
>>>>>>> upstream/master
        """Extends the snapin registry with the ones configured in the site (for the current user)"""
        self._clear_custom_snapins()
        self._add_custom_snapins(custom_snapins)

<<<<<<< HEAD
    def _clear_custom_snapins(self):
        for snapin_type_id, snapin_type in self.items():
            if snapin_type.is_custom_snapin():
                del self[snapin_type_id]

    def _add_custom_snapins(self, custom_snapins):
=======
    def _clear_custom_snapins(self) -> None:
        for snapin_type_id, snapin_type in list(self.items()):
            if snapin_type.is_custom_snapin():
                self.unregister(snapin_type_id)

    def _add_custom_snapins(self, custom_snapins: List[CustomSnapins]) -> None:
>>>>>>> upstream/master
        for custom_snapin in custom_snapins:
            base_snapin_type_id = custom_snapin._["custom_snapin"][0]

            try:
                base_snapin_type = self[base_snapin_type_id]
            except KeyError:
                continue

<<<<<<< HEAD
            if not base_snapin_type.is_customizable():
                continue

            @self.register
            class CustomSnapin(base_snapin_type):
=======
            # TODO: This is just our assumption, can we enforce this via
            # typing? Probably not in the current state of affairs where things
            # which should be instances are classes... :-/
            if not issubclass(base_snapin_type, SidebarSnapin):
                raise ValueError("invalid snapin type %r" % base_snapin_type)

            if not issubclass(base_snapin_type, CustomizableSidebarSnapin):
                continue

            # TODO: The stuff below is completely untypeable... :-P * * *
            @self.register
            class CustomSnapin(base_snapin_type):  # type: ignore[valid-type,misc]
>>>>>>> upstream/master
                _custom_snapin = custom_snapin

                @classmethod
                def is_custom_snapin(cls):
                    return True

                @classmethod
                def type_name(cls):
                    return cls._custom_snapin.name()

                @classmethod
                def title(cls):
                    return cls._custom_snapin.title()

                @classmethod
                def description(cls):
                    return cls._custom_snapin.description()

                @classmethod
                def parameters(cls):
                    return cls._custom_snapin._["custom_snapin"][1]

<<<<<<< HEAD
            _it_is_really_used = CustomSnapin  # help pylint (unused-variable)
=======
            _it_is_really_used = CustomSnapin  # noqa: F841
>>>>>>> upstream/master


snapin_registry = SnapinRegistry()

#.
#   .--Helpers-------------------------------------------------------------.
#   |                  _   _      _                                        |
#   |                 | | | | ___| |_ __   ___ _ __ ___                    |
#   |                 | |_| |/ _ \ | '_ \ / _ \ '__/ __|                   |
#   |                 |  _  |  __/ | |_) |  __/ |  \__ \                   |
#   |                 |_| |_|\___|_| .__/ \___|_|  |___/                   |
#   |                              |_|                                     |
#   '----------------------------------------------------------------------'
# TODO: Move these to a class


def render_link(text, url, target="main", onclick=None):
    # Convert relative links into absolute links. We have three kinds
    # of possible links and we change only [3]
    # [1] protocol://hostname/url/link.py
    # [2] /absolute/link.py
    # [3] relative.py
    if not (":" in url[:10]) and not url.startswith("javascript") and url[0] != '/':
        url = config.url_prefix() + "check_mk/" + url
<<<<<<< HEAD
    return html.render_a(text, href=url, class_="link", target=target or '',\
                         onfocus = "if (this.blur) this.blur();",\
                         onclick = onclick or None)
=======
    return html.render_a(text,
                         href=url,
                         class_="link",
                         target=target or '',
                         onfocus="if (this.blur) this.blur();",
                         onclick=onclick or None)
>>>>>>> upstream/master


def link(text, url, target="main", onclick=None):
    return html.write(render_link(text, url, target=target, onclick=onclick))


def simplelink(text, url, target="main"):
    link(text, url, target)
    html.br()


def bulletlink(text, url, target="main", onclick=None):
    html.open_li(class_="sidebar")
    link(text, url, target, onclick)
    html.close_li()


def iconlink(text, url, icon):
    html.open_a(class_=["iconlink", "link"], target="main", href=url)
<<<<<<< HEAD
    html.icon(icon=icon, title=None, cssclass="inline")
=======
    html.icon(icon, cssclass="inline")
>>>>>>> upstream/master
    html.write_text(text)
    html.close_a()
    html.br()


def write_snapin_exception(e):
    html.open_div(class_=["snapinexception"])
    html.h2(_('Error'))
    html.p(e)
    html.div(traceback.format_exc().replace('\n', '<br>'), style="display:none;")
    html.close_div()


def heading(text):
<<<<<<< HEAD
    html.write("<h3>%s</h3>\n" % html.attrencode(text))
=======
    html.write("<h3>%s</h3>\n" % escaping.escape_attribute(text))
>>>>>>> upstream/master


# TODO: Better change to context manager?
def begin_footnote_links():
    html.open_div(class_="footnotelink")


def end_footnote_links():
    html.close_div()


def footnotelinks(links):
    begin_footnote_links()
    for text, target in links:
        link(text, target)
    end_footnote_links()


def nagioscgilink(text, target):
    html.open_li(class_="sidebar")
    html.a(text,
           class_="link",
           target="main",
           href="%snagios/cgi-bin/%s" % (config.url_prefix(), target))
    html.close_li()


<<<<<<< HEAD
def snapin_site_choice(ident, choices):
=======
def snapin_site_choice(ident: SiteId, choices: List[Tuple[SiteId, str]]) -> Optional[List[SiteId]]:
>>>>>>> upstream/master
    sites = config.user.load_file("sidebar_sites", {})
    site = sites.get(ident, "")
    if site == "":
        only_sites = None
    else:
        only_sites = [site]

    if len(choices) <= 1:
        return None

<<<<<<< HEAD
    choices = [
        ("", _("All sites")),
    ] + choices
    onchange = "cmk.sidebar.set_snapin_site(event, %s, this)" % json.dumps(ident)
    html.dropdown("site", choices, deflt=site, onchange=onchange)
=======
    dropdown_choices: Choices = [
        ("", _("All sites")),
    ]
    dropdown_choices += choices

    onchange = "cmk.sidebar.set_snapin_site(event, %s, this)" % json.dumps(ident)
    html.dropdown("site", dropdown_choices, deflt=site, onchange=onchange)
>>>>>>> upstream/master

    return only_sites


<<<<<<< HEAD
def visuals_by_topic(permitted_visuals, default_order=None):
    if default_order is None:
        default_order = [
            _("Overview"),
            _("Hosts"),
            _("Host Groups"),
            _("Services"),
            _("Service Groups"),
            _("Metrics"),
            _("Business Intelligence"),
            _("Problems"),
        ]

    s = sorted([(_u(visual.get("topic") or
                    _("Other")), _u(visual.get("title")), name, 'painters' in visual)
                for name, visual in permitted_visuals
                if not visual["hidden"] and not visual.get("mobile")])

    result = []
    for topic in default_order:
        result.append((topic, s))

    rest = sorted({t for (t, _t, _v, _i) in s if t not in default_order})
    for topic in rest:
        if topic:
            result.append((topic, s))

    return result
=======
def make_topic_menu(visuals: List[Tuple[str, Tuple[str, Visual]]]) -> List[TopicMenuTopic]:
    pagetypes.PagetypeTopics.load()
    topics = pagetypes.PagetypeTopics.get_permitted_instances()

    by_topic: Dict[pagetypes.PagetypeTopics, TopicMenuTopic] = {}

    for visual_type_name, (name, visual) in visuals:
        if visual["hidden"] or visual.get("mobile"):
            continue  # Skip views not inteded to be shown in the menus

        topic_id = visual["topic"]
        try:
            topic = topics[topic_id]
        except KeyError:
            topic = topics["other"]

        url = _visual_url(visual_type_name, name)

        topic = by_topic.setdefault(
            topic,
            TopicMenuTopic(
                name=topic.name(),
                title=topic.title(),
                items=[],
                icon=topic.icon_name(),
                hide=topic.hide(),
            ))
        topic.items.append(
            TopicMenuItem(
                name=name,
                title=visual["title"],
                url=url,
                sort_index=visual["sort_index"],
                is_show_more=visual["is_show_more"],
                icon=visual["icon"],
            ))

    # Sort the items of all topics
    for topic in by_topic.values():
        topic.items.sort(key=lambda i: (i.sort_index, i.title))

    # Return the sorted topics
    return [
        v for k, v in sorted(by_topic.items(), key=lambda e: (e[0].sort_index(), e[0].title()))
        if not v.hide
    ]


def _visual_url(visual_type_name: str, name: str) -> str:
    if visual_type_name == "views":
        return "view.py?view_name=%s" % name

    if visual_type_name == "dashboards":
        return "dashboard.py?name=%s" % name

    # Note: This is no real visual type like the others here. This is just a hack to make top level
    # pages work with this function.
    if visual_type_name == "pages":
        return name if name.endswith(".py") else "%s.py" % name

    if visual_type_name == "reports":
        return "report.py?name=%s" % name

    # Handle page types
    if visual_type_name in ["custom_graph", "graph_collection", "forecast_graph"]:
        return "%s.py?name=%s" % (visual_type_name, name)

    raise NotImplementedError("Unknown visual type: %s" % visual_type_name)


def show_topic_menu(treename: str,
                    menu: List[TopicMenuTopic],
                    show_item_icons: bool = False) -> None:
    for topic in menu:
        _show_topic(treename, topic, show_item_icons)


def _show_topic(treename: str, topic: TopicMenuTopic, show_item_icons: bool) -> None:
    if not topic.items:
        return

    html.begin_foldable_container(treename=treename,
                                  id_=topic.name,
                                  isopen=False,
                                  title=topic.title,
                                  indent=True)

    for item in topic.items:
        if show_item_icons:
            html.open_li(class_=["sidebar", "show_more_mode" if item.is_show_more else None])
            iconlink(item.title, item.url, item.icon)
            html.close_li()
        else:
            bulletlink(item.title, item.url, onclick="return cmk.sidebar.wato_views_clicked(this)")

    html.end_foldable_container()
>>>>>>> upstream/master
