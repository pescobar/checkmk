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
"""Register general nagvis permissions"""

from cmk.gui.i18n import _
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Register general nagvis permissions"""

from cmk.gui.i18n import _, _l
>>>>>>> upstream/master
from cmk.gui.permissions import (
    permission_section_registry,
    PermissionSection,
    permission_registry,
    Permission,
)


@permission_section_registry.register
class PermissionSectionNagVis(PermissionSection):
    @property
    def name(self):
        return "nagvis"

    @property
    def title(self):
        return _('NagVis')


<<<<<<< HEAD
@permission_registry.register
class PermissionNagVisFull(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "*_*_*"

    @property
    def title(self):
        return _('Full access')

    @property
    def description(self):
        return _('This permission grants full access to NagVis.')

    @property
    def defaults(self):
        return ["admin"]


@permission_registry.register
class PermissionNagVisRotations(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "Rotation_view_*"

    @property
    def title(self):
        return _('Use all map rotations')

    @property
    def description(self):
        return _('Grants read access to all rotations.')

    @property
    def defaults(self):
        return ["guest"]


@permission_registry.register
class PermissionNagVisMapsViewAll(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "Map_view_*"

    @property
    def title(self):
        return _('View all maps')

    @property
    def description(self):
        return _('Grants read access to all maps.')

    @property
    def defaults(self):
        return ["guest"]


@permission_registry.register
class PermissionNagVisMapsEditAll(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "Map_edit_*"

    @property
    def title(self):
        return _('Edit all maps')

    @property
    def description(self):
        return _('Grants modify access to all maps.')

    @property
    def defaults(self):
        return []


@permission_registry.register
class PermissionNagVisMapsDeleteAll(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "Map_delete_*"

    @property
    def title(self):
        return _('Delete all maps')

    @property
    def description(self):
        return _('Permits to delete all maps.')

    @property
    def defaults(self):
        return []


@permission_registry.register
class PermissionNagVisPermittedMapsView(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "Map_view"

    @property
    def title(self):
        return _('View permitted maps')

    @property
    def description(self):
        return _('Grants read access to all maps the user is a contact for.')

    @property
    def defaults(self):
        return ['user']


@permission_registry.register
class PermissionNagVisPermittedMapsEdit(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "Map_edit"

    @property
    def title(self):
        return _('Edit permitted maps')

    @property
    def description(self):
        return _('Grants modify access to all maps the user is contact for.')

    @property
    def defaults(self):
        return ['user']


@permission_registry.register
class PermissionNagVisPermittedMapsDelete(Permission):
    @property
    def section(self):
        return PermissionSectionNagVis

    @property
    def permission_name(self):
        return "Map_delete"

    @property
    def title(self):
        return _('Delete permitted maps')

    @property
    def description(self):
        return _('Permits to delete all maps the user is contact for.')

    @property
    def defaults(self):
        return ['user']
=======
permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="*_*_*",
        title=_l('Full access'),
        description=_l('This permission grants full access to NagVis.'),
        defaults=["admin"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="Rotation_view_*",
        title=_l('Use all map rotations'),
        description=_l('Grants read access to all rotations.'),
        defaults=["guest"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="Map_view_*",
        title=_l('View all maps'),
        description=_l('Grants read access to all maps.'),
        defaults=["guest"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="Map_edit_*",
        title=_l('Edit all maps'),
        description=_l('Grants modify access to all maps.'),
        defaults=[],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="Map_delete_*",
        title=_l('Delete all maps'),
        description=_l('Permits to delete all maps.'),
        defaults=[],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="Map_view",
        title=_l('View permitted maps'),
        description=_l('Grants read access to all maps the user is a contact for.'),
        defaults=['user'],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="Map_edit",
        title=_l('Edit permitted maps'),
        description=_l('Grants modify access to all maps the user is contact for.'),
        defaults=['user'],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionNagVis,
        name="Map_delete",
        title=_l('Delete permitted maps'),
        description=_l('Permits to delete all maps the user is contact for.'),
        defaults=['user'],
    ))
>>>>>>> upstream/master
