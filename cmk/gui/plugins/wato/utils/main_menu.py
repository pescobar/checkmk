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

import abc
import re
from typing import Optional, Text  # pylint: disable=unused-import
import six

import cmk.gui.config as config
import cmk.gui.watolib as watolib
import cmk.utils.plugin_registry
from cmk.gui.globals import html


class MainMenu(object):
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import re
from typing import List

from cmk.gui.i18n import _l
from cmk.gui.globals import html
from cmk.gui.watolib.main_menu import (
    ABCMainModule,
    MainModuleTopic,
    MenuItem,
    main_module_registry,
    main_module_topic_registry,
)


class MainMenu:
>>>>>>> upstream/master
    def __init__(self, items=None, columns=2):
        self._items = items or []
        self._columns = columns

    def add_item(self, item):
        self._items.append(item)

    def show(self):
        html.open_div(class_="mainmenu")
        for item in self._items:
            if not item.may_see():
                continue

            html.open_a(href=item.get_url(), onfocus="if (this.blur) this.blur();")
<<<<<<< HEAD
            html.icon(item.title, item.icon)
=======
            html.icon(item.icon, item.title)
>>>>>>> upstream/master
            html.div(item.title, class_="title")
            html.div(item.description, class_="subtitle")
            html.close_a()

        html.close_div()


<<<<<<< HEAD
class MenuItem(object):
    def __init__(self, mode_or_url, title, icon, permission, description, sort_index=20):
        self._mode_or_url = mode_or_url
        self._title = title
        self._icon = icon
        self._permission = permission
        self._description = description
        self._sort_index = sort_index

    @property
    def mode_or_url(self):
        return self._mode_or_url

    @property
    def title(self):
        return self._title

    @property
    def icon(self):
        return self._icon

    @property
    def permission(self):
        return self._permission

    @property
    def description(self):
        return self._description

    @property
    def sort_index(self):
        return self._sort_index

    @property
    def enabled(self):
        # type: () -> bool
        return True

    def may_see(self):
        """Whether or not the currently logged in user is allowed to see this module"""
        if not self.enabled:
            return False

        if self.permission is None:
            return True

        if "." not in self.permission:
            permission = "wato." + self.permission
        else:
            permission = self.permission

        return config.user.may(permission) or config.user.may("wato.seeall")

    def get_url(self):
        mode_or_url = self.mode_or_url
        if '?' in mode_or_url or '/' in mode_or_url or mode_or_url.endswith(".py"):
            return mode_or_url
        return watolib.folder_preserving_link([("mode", mode_or_url)])

    def __repr__(self):
        return "%s(mode_or_url=%r, title=%r, icon=%r, permission=%r, description=%r, sort_index=%r)" % \
            (self.__class__.__name__, self.mode_or_url, self.title, self.icon, self.permission, self.description, self.sort_index)


class MainModule(six.with_metaclass(abc.ABCMeta, MenuItem)):
    def __init__(self):
        # TODO: Cleanup hierarchy
        super(MainModule, self).__init__(mode_or_url=None,
                                         title=None,
                                         icon=None,
                                         permission=None,
                                         description=None,
                                         sort_index=None)

    @abc.abstractproperty
    def mode_or_url(self):
        # type: () -> str
        raise NotImplementedError()

    @abc.abstractproperty
    def title(self):
        # type: () -> Text
        raise NotImplementedError()

    @abc.abstractproperty
    def icon(self):
        # type: () -> str
        raise NotImplementedError()

    @abc.abstractproperty
    def permission(self):
        # type: () -> Optional[str]
        raise NotImplementedError()

    @abc.abstractproperty
    def description(self):
        # type: () -> Text
        raise NotImplementedError()

    @abc.abstractproperty
    def sort_index(self):
        # type: () -> int
        raise NotImplementedError()


class ModuleRegistry(cmk.utils.plugin_registry.ClassRegistry):
    def plugin_base_class(self):
        return MainModule

    def plugin_name(self, plugin_class):
        return plugin_class().mode_or_url


main_module_registry = ModuleRegistry()


class WatoModule(MenuItem):
    """Used with register_modules() in pre 1.6 versions to register main modules"""
    pass
=======
class WatoModule(MenuItem):
    """Used with register_modules() in pre 1.6 versions to register main modules"""
>>>>>>> upstream/master


def register_modules(*args):
    """Register one or more top level modules to Check_MK WATO.
    The registered modules are displayed in the navigation of WATO."""
    for wato_module in args:
        assert isinstance(wato_module, WatoModule)

        internal_name = re.sub("[^a-zA-Z]", "", wato_module.mode_or_url)

        cls = type(
<<<<<<< HEAD
            "LegacyMainModule%s" % internal_name.title(), (MainModule,), {
                "mode_or_url": wato_module.mode_or_url,
=======
            "LegacyMainModule%s" % internal_name.title(), (ABCMainModule,), {
                "mode_or_url": wato_module.mode_or_url,
                "topic": MainModuleTopicCustom,
>>>>>>> upstream/master
                "title": wato_module.title,
                "icon": wato_module.icon,
                "permission": wato_module.permission,
                "description": wato_module.description,
                "sort_index": wato_module.sort_index,
<<<<<<< HEAD
=======
                "is_show_more": False,
>>>>>>> upstream/master
            })
        main_module_registry.register(cls)


<<<<<<< HEAD
def get_modules():
    return sorted([m() for m in main_module_registry.values()],
                  key=lambda m: (m.sort_index, m.title))
=======
def get_modules() -> List[ABCMainModule]:
    return sorted([m() for m in main_module_registry.values()],
                  key=lambda m: (m.sort_index, m.title))


#   .--Topics--------------------------------------------------------------.
#   |                     _____           _                                |
#   |                    |_   _|__  _ __ (_) ___ ___                       |
#   |                      | |/ _ \| '_ \| |/ __/ __|                      |
#   |                      | | (_) | |_) | | (__\__ \                      |
#   |                      |_|\___/| .__/|_|\___|___/                      |
#   |                              |_|                                     |
#   +----------------------------------------------------------------------+
#   | Register the builtin topics. These are the ones that may be          |
#   | referenced by different WATO plugins. Additional individual plugins  |
#   | are allowed to create their own topics.                              |
#   '----------------------------------------------------------------------'
#.

MainModuleTopicHosts = main_module_topic_registry.register(
    MainModuleTopic(
        name="hosts",
        title=_l("Hosts"),
        icon_name="topic_hosts",
        sort_index=10,
    ))

MainModuleTopicServices = main_module_topic_registry.register(
    MainModuleTopic(
        name="services",
        title=_l("Services"),
        icon_name="topic_services",
        sort_index=20,
    ))

MainModuleTopicBI = main_module_topic_registry.register(
    MainModuleTopic(
        name="bi",
        title=_l("Business Intelligence"),
        icon_name="topic_bi",
        sort_index=30,
    ))

MainModuleTopicAgents = main_module_topic_registry.register(
    MainModuleTopic(
        name="agents",
        title=_l("Agents"),
        icon_name="topic_agents",
        sort_index=40,
    ))

MainModuleTopicEvents = main_module_topic_registry.register(
    MainModuleTopic(
        name="events",
        title=_l("Events"),
        icon_name="topic_events",
        sort_index=50,
    ))

MainModuleTopicUsers = main_module_topic_registry.register(
    MainModuleTopic(
        name="users",
        title=_l("Users"),
        icon_name="topic_users",
        sort_index=60,
    ))

MainModuleTopicGeneral = main_module_topic_registry.register(
    MainModuleTopic(
        name="general",
        title=_l("General"),
        icon_name="topic_general",
        sort_index=70,
    ))

MainModuleTopicMaintenance = main_module_topic_registry.register(
    MainModuleTopic(
        name="maintenance",
        title=_l("Maintenance"),
        icon_name="topic_maintenance",
        sort_index=80,
    ))

MainModuleTopicCustom = main_module_topic_registry.register(
    MainModuleTopic(
        name="custom",
        title=_l("Custom"),
        icon_name="topic_custom",
        sort_index=150,
    ))
>>>>>>> upstream/master
