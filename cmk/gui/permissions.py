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
from typing import Text, Type, List  # pylint: disable=unused-import
import six
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import abc
from typing import Type, List

from six import ensure_str
>>>>>>> upstream/master

import cmk.utils.plugin_registry


<<<<<<< HEAD
class PermissionSection(six.with_metaclass(abc.ABCMeta, object)):
    @abc.abstractproperty
    def name(self):
        # type: () -> str
=======
class PermissionSection(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def name(self) -> str:
>>>>>>> upstream/master
        """The identity of a permission section.
        One word, may contain alpha numeric characters"""
        raise NotImplementedError()

    @abc.abstractproperty
<<<<<<< HEAD
    def title(self):
        # type: () -> Text
=======
    def title(self) -> str:
>>>>>>> upstream/master
        """Display name representing the section"""
        raise NotImplementedError()

    @property
<<<<<<< HEAD
    def sort_index(self):
        # type: () -> int
=======
    def sort_index(self) -> int:
>>>>>>> upstream/master
        """Number to sort the sections with"""
        return 50

    # TODO: Is this still needed?
    @property
<<<<<<< HEAD
    def do_sort(self):
        # type: () -> bool
=======
    def do_sort(self) -> bool:
>>>>>>> upstream/master
        """Whether or not to sort the permissions by title in this section"""
        return False


<<<<<<< HEAD
class PermissionSectionRegistry(cmk.utils.plugin_registry.ClassRegistry):
    def plugin_base_class(self):
        return PermissionSection

    def plugin_name(self, plugin_class):
        return plugin_class().name
=======
class PermissionSectionRegistry(cmk.utils.plugin_registry.Registry[Type[PermissionSection]]):
    def plugin_name(self, instance):
        return instance().name
>>>>>>> upstream/master

    def get_sorted_sections(self):
        return sorted([s() for s in self.values()], key=lambda s: (s.sort_index, s.title))


permission_section_registry = PermissionSectionRegistry()


<<<<<<< HEAD
class Permission(six.with_metaclass(abc.ABCMeta, object)):
    _sort_index = 0

    @abc.abstractproperty
    def section(self):
        # type: () -> Type[PermissionSection]
        raise NotImplementedError()

    @abc.abstractproperty
    def permission_name(self):
        # type: () -> str
        """The identity of a permission (without it's section identity).
        One word, may contain alpha numeric characters"""
        raise NotImplementedError()

    @abc.abstractproperty
    def title(self):
        # type: () -> Text
        """Display name representing the permission"""
        raise NotImplementedError()

    @abc.abstractproperty
    def description(self):
        # type: () -> Text
        """Text to explain the purpose of this permission"""
        raise NotImplementedError()

    @abc.abstractproperty
    def defaults(self):
        # type: () -> List[str]
        """List of role IDs that have this permission by default"""
        raise NotImplementedError()

    @property
    def name(self):
        # type: () -> str
=======
class Permission(metaclass=abc.ABCMeta):
    _sort_index = 0

    def __init__(self, section: Type[PermissionSection], name: str, title: str, description: str,
                 defaults: List[str]) -> None:
        self._section = section
        self._name = name
        self._title = title
        self._description = description
        self._defaults = defaults
        self._sort_index = 0

    @property
    def section(self) -> Type[PermissionSection]:
        return self._section

    @property
    def permission_name(self) -> str:
        """The identity of a permission (without it's section identity).
        One word, may contain alpha numeric characters"""
        return self._name

    @property
    def title(self) -> str:
        """Display name representing the permission"""
        return self._title

    @property
    def description(self) -> str:
        """Text to explain the purpose of this permission"""
        return self._description

    @property
    def defaults(self) -> List[str]:
        """List of role IDs that have this permission by default"""
        return self._defaults

    @property
    def name(self) -> str:
>>>>>>> upstream/master
        """The full identity of a permission (including the section identity)."""
        return ".".join((self.section().name, self.permission_name))

    @property
<<<<<<< HEAD
    def sort_index(self):
        # type: () -> int
        """Number to sort the permission with"""
        return self._sort_index


class PermissionRegistry(cmk.utils.plugin_registry.ClassRegistry):
=======
    def sort_index(self) -> int:
        """Number to sort the permission with"""
        return self._sort_index

    @sort_index.setter
    def sort_index(self, value: int) -> None:
        self._sort_index = value


class PermissionRegistry(cmk.utils.plugin_registry.Registry[Permission]):
>>>>>>> upstream/master
    def __init__(self):
        super(PermissionRegistry, self).__init__()
        # TODO: Better make the sorting explicit in the future
        # used as auto incrementing counter to numerate the permissions in
        # the order they have been added.
        self._index_counter = 0

<<<<<<< HEAD
    def plugin_base_class(self):
        return Permission

    def plugin_name(self, plugin_class):
        return plugin_class().name

    def registration_hook(self, plugin_class):
        plugin_class._sort_index = self._index_counter
=======
    def plugin_name(self, instance):
        return instance.name

    def registration_hook(self, instance):
        instance._sort_index = self._index_counter
>>>>>>> upstream/master
        self._index_counter += 1

    def get_sorted_permissions(self, section):
        """Returns the sorted permissions of a section respecting the sorting config of the section"""
<<<<<<< HEAD
        permissions = [
            p for p in [p_class() for p_class in self.values()] if p.section == section.__class__
        ]
=======
        permissions = [p for p in self.values() if p.section == section.__class__]
>>>>>>> upstream/master

        if section.do_sort:
            return sorted(permissions, key=lambda p: (p.title, p.sort_index))
        return sorted(permissions, key=lambda p: p.sort_index)


permission_registry = PermissionRegistry()


# Kept for compatibility with pre 1.6 GUI plugins
def declare_permission_section(name, title, prio=50, do_sort=False):
    cls = type("LegacyPermissionSection%s" % name.title(), (PermissionSection,), {
        "name": name,
        "title": title,
        "sort_index": prio,
        "do_sort": do_sort,
    })
    permission_section_registry.register(cls)


# Kept for compatibility with pre 1.6 GUI plugins
# Some dynamically registered permissions still use this
def declare_permission(name, title, description, defaults):
<<<<<<< HEAD
    if isinstance(name, six.text_type):
        name = name.encode("utf-8")

    section_name, permission_name = name.split(".", 1)

    cls = type(
        "LegacyPermission%s%s" % (section_name.title(), permission_name.title()), (Permission,), {
            "_section_name": section_name,
            "section": property(lambda s: permission_section_registry[s._section_name]),
            "permission_name": permission_name,
            "name": name,
            "title": title,
            "description": description,
            "defaults": defaults,
        })
    permission_registry.register(cls)
=======
    if not isinstance(name, str):
        name = ensure_str(name, encoding="ascii")

    section_name, permission_name = name.split(".", 1)

    permission_registry.register(
        Permission(
            section=permission_section_registry[section_name],
            name=permission_name,
            title=title,
            description=description,
            defaults=defaults,
        ))
>>>>>>> upstream/master
