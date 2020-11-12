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
"""Manage roles and permissions

In order to make getting started easier - Check_MK Multisite comes with three
builtin-roles: admin, user and guest. These roles have predefined permissions.
The builtin roles cannot be deleted. Users listed in admin_users in
multisite.mk automatically get the role admin - even if no such user or contact
has been configured yet. By that way an initial login - e.g. as omdamin - is
possible. The admin role cannot be removed from that user as long as he is
listed in admin_users. Also the variables guest_users, users and default_user_
role still work. That way Multisite is fully operable without WATO and also
backwards compatible.  In WATO you can create further roles and also edit the
permissions of the existing roles. Users can be assigned to builtin and custom
roles.  This modes manages the creation of custom roles and the permissions
configuration of all roles.
"""

import re
<<<<<<< HEAD
=======
from typing import Optional, Type
>>>>>>> upstream/master

import cmk.utils.store as store

import cmk.gui.userdb as userdb
<<<<<<< HEAD
=======
import cmk.gui.plugins.userdb.utils as userdb_utils
>>>>>>> upstream/master
import cmk.gui.config as config
import cmk.gui.watolib as watolib
import cmk.gui.forms as forms
import cmk.gui.hooks as hooks
from cmk.gui.table import table_element
from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.exceptions import MKUserError
<<<<<<< HEAD
from cmk.gui.htmllib import HTML
=======
from cmk.gui.htmllib import HTML, Choices
from cmk.gui.breadcrumb import Breadcrumb
from cmk.gui.page_menu import (
    PageMenu,
    PageMenuDropdown,
    PageMenuTopic,
    PageMenuEntry,
    PageMenuSearch,
    make_simple_link,
    make_simple_form_page_menu,
)
>>>>>>> upstream/master
from cmk.gui.permissions import (
    permission_section_registry,
    permission_registry,
)

<<<<<<< HEAD
from cmk.gui.plugins.wato.utils.html_elements import (
    search_form,)

from cmk.gui.plugins.wato import (
    WatoMode,
    mode_registry,
    wato_confirm,
    global_buttons,
    make_action_link,
    get_search_expression,
)


class RoleManagement(object):
    def __init__(self):
        self._roles = userdb.load_roles()
=======
from cmk.gui.plugins.wato import (
    WatoMode,
    ActionResult,
    mode_registry,
    make_action_link,
    make_confirm_link,
    get_search_expression,
    redirect,
    mode_url,
)


class RoleManagement:
    def __init__(self):
        self._roles = userdb_utils.load_roles()
>>>>>>> upstream/master
        super(RoleManagement, self).__init__()

    def _save_roles(self):
        # Reflect the data in the roles dict kept in the config module Needed
        # for instant changes in current page while saving modified roles.
        # Otherwise the hooks would work with old data when using helper
        # functions from the config module
        config.roles.update(self._roles)

        store.mkdir(watolib.multisite_dir())
        store.save_to_mk_file(watolib.multisite_dir() + "roles.mk",
                              "roles",
                              self._roles,
                              pprint_value=config.wato_pprint_config)

        hooks.call("roles-saved", self._roles)

    # Adapt references in users. Builtin rules cannot
    # be renamed and are not handled here. If new_id is None,
    # the role is being deleted
    def _rename_user_role(self, uid, new_id):
        users = userdb.load_users(lock=True)
        for user in users.values():
<<<<<<< HEAD
            if id in user["roles"]:
=======
            if uid in user["roles"]:
>>>>>>> upstream/master
                user["roles"].remove(uid)
                if new_id:
                    user["roles"].append(new_id)
        userdb.save_users(users)


@mode_registry.register
class ModeRoles(RoleManagement, WatoMode):
    @classmethod
    def name(cls):
        return "roles"

    @classmethod
    def permissions(cls):
        return ["users"]

    def title(self):
<<<<<<< HEAD
        return _("Roles & Permissions")

    def buttons(self):
        global_buttons()
        html.context_button(_("Matrix"), watolib.folder_preserving_link([("mode", "role_matrix")]),
                            "matrix")

    def action(self):
        if html.request.var("_delete"):
            delid = html.request.var("_delete")
=======
        return _("Roles & permissions")

    def page_menu(self, breadcrumb: Breadcrumb) -> PageMenu:
        menu = PageMenu(
            dropdowns=[
                PageMenuDropdown(
                    name="roles",
                    title=_("Roles"),
                    topics=[
                        PageMenuTopic(
                            title=_("Overview"),
                            entries=[
                                PageMenuEntry(
                                    title=_("Permission matrix"),
                                    icon_name="matrix",
                                    item=make_simple_link(
                                        watolib.folder_preserving_link([("mode", "role_matrix")])),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            breadcrumb=breadcrumb,
        )
        return menu

    def action(self) -> ActionResult:
        if not html.check_transaction():
            return redirect(self.mode_url())

        if html.request.var("_delete"):
            delid = html.request.get_ascii_input_mandatory("_delete")
>>>>>>> upstream/master

            if delid not in self._roles:
                raise MKUserError(None, _("This role does not exist."))

            if html.transaction_valid() and self._roles[delid].get('builtin'):
                raise MKUserError(None, _("You cannot delete the builtin roles!"))

<<<<<<< HEAD
            c = wato_confirm(
                _("Confirm deletion of role %s") % delid,
                _("Do you really want to delete the role %s?") % delid)
            if c:
                self._rename_user_role(delid, None)  # Remove from existing users
                del self._roles[delid]
                self._save_roles()
                watolib.add_change("edit-roles",
                                   _("Deleted role '%s'") % delid,
                                   sites=config.get_login_sites())
            elif c is False:
                return ""

        elif html.request.var("_clone"):
            if html.check_transaction():
                cloneid = html.request.var("_clone")

                try:
                    cloned_role = self._roles[cloneid]
                except KeyError:
                    raise MKUserError(None, _("This role does not exist."))

                newid = cloneid
                while newid in self._roles:
                    newid += "x"

                new_role = {}
                new_role.update(cloned_role)

                new_alias = new_role["alias"]
                while not watolib.is_alias_used("roles", newid, new_alias)[0]:
                    new_alias += _(" (copy)")
                new_role["alias"] = new_alias

                if cloned_role.get("builtin"):
                    new_role["builtin"] = False
                    new_role["basedon"] = cloneid

                self._roles[newid] = new_role
                self._save_roles()
                watolib.add_change("edit-roles",
                                   _("Created new role '%s'") % newid,
                                   sites=config.get_login_sites())
=======
            users = userdb.load_users()
            for user in users.values():
                if delid in user["roles"]:
                    raise MKUserError(
                        None, _("You cannot delete roles, that are still in use (%s)!" % delid))

            self._rename_user_role(delid, None)  # Remove from existing users
            del self._roles[delid]
            self._save_roles()
            watolib.add_change("edit-roles",
                               _("Deleted role '%s'") % delid,
                               sites=config.get_login_sites())

        elif html.request.var("_clone"):
            cloneid = html.request.get_ascii_input_mandatory("_clone")

            try:
                cloned_role = self._roles[cloneid]
            except KeyError:
                raise MKUserError(None, _("This role does not exist."))

            newid = cloneid
            while newid in self._roles:
                newid += "x"

            new_role = {}
            new_role.update(cloned_role)

            new_alias = new_role["alias"]
            while not watolib.is_alias_used("roles", newid, new_alias)[0]:
                new_alias += _(" (copy)")
            new_role["alias"] = new_alias

            if cloned_role.get("builtin"):
                new_role["builtin"] = False
                new_role["basedon"] = cloneid

            self._roles[newid] = new_role
            self._save_roles()
            watolib.add_change("edit-roles",
                               _("Created new role '%s'") % newid,
                               sites=config.get_login_sites())

        return redirect(self.mode_url())
>>>>>>> upstream/master

    def page(self):
        with table_element("roles") as table:

            users = userdb.load_users()
            for rid, role in sorted(self._roles.items(), key=lambda a: (a[1]["alias"], a[0])):
                table.row()

                # Actions
                table.cell(_("Actions"), css="buttons")
                edit_url = watolib.folder_preserving_link([("mode", "edit_role"), ("edit", rid)])
                clone_url = make_action_link([("mode", "roles"), ("_clone", rid)])
<<<<<<< HEAD
                delete_url = make_action_link([("mode", "roles"), ("_delete", rid)])
=======
                delete_url = make_confirm_link(
                    url=make_action_link([("mode", "roles"), ("_delete", rid)]),
                    message=_("Do you really want to delete the role %s?") % rid,
                )
>>>>>>> upstream/master
                html.icon_button(edit_url, _("Properties"), "edit")
                html.icon_button(clone_url, _("Clone"), "clone")
                if not role.get("builtin"):
                    html.icon_button(delete_url, _("Delete this role"), "delete")

                # ID
                table.text_cell(_("Name"), rid)

                # Alias
                table.text_cell(_("Alias"), role["alias"])

                # Type
                table.cell(_("Type"), _("builtin") if role.get("builtin") else _("custom"))

                # Modifications
                table.cell(
                    _("Modifications"), "<span title='%s'>%s</span>" %
                    (_("That many permissions do not use the factory defaults."),
                     len(role["permissions"])))

                # Users
                table.cell(
                    _("Users"),
                    HTML(", ").join([
                        html.render_a(
                            user.get("alias", user_id),
                            watolib.folder_preserving_link([("mode", "edit_user"),
                                                            ("edit", user_id)]))
                        for (user_id, user) in users.items()
                        if rid in user["roles"]
                    ]))

        # Possibly we could also display the following information
        # - number of set permissions (needs loading users)
        # - number of users with this role


@mode_registry.register
class ModeEditRole(RoleManagement, WatoMode):
    @classmethod
    def name(cls):
        return "edit_role"

    @classmethod
    def permissions(cls):
        return ["users"]

<<<<<<< HEAD
=======
    @classmethod
    def parent_mode(cls) -> Optional[Type[WatoMode]]:
        return ModeRoles

>>>>>>> upstream/master
    def __init__(self):
        super(ModeEditRole, self).__init__()

        # Make sure that all dynamic permissions are available (e.g. those for custom
        # views)
        config.load_dynamic_permissions()

    def _from_vars(self):
<<<<<<< HEAD
        self._role_id = html.request.var("edit")
=======
        self._role_id = html.request.get_ascii_input_mandatory("edit")
>>>>>>> upstream/master

        try:
            self._role = self._roles[self._role_id]
        except KeyError:
            raise MKUserError("edit", _("This role does not exist."))

    def title(self):
<<<<<<< HEAD
        return _("Edit user role %s") % self._role_id

    def buttons(self):
        html.context_button(_("All Roles"), watolib.folder_preserving_link([("mode", "roles")]),
                            "back")

    def action(self):
        if html.form_submitted("search"):
            return

        alias = html.get_unicode_input("alias")
=======
        return _("Edit role %s") % self._role_id

    def page_menu(self, breadcrumb: Breadcrumb) -> PageMenu:
        menu = make_simple_form_page_menu(
            breadcrumb,
            form_name="role",
            button_name="save",
        )
        menu.inpage_search = PageMenuSearch(placeholder=_("Filter permissions"))
        return menu

    def action(self) -> ActionResult:
        if html.form_submitted("search"):
            return None

        alias = html.request.get_unicode_input("alias")
>>>>>>> upstream/master

        unique, info = watolib.is_alias_used("roles", self._role_id, alias)
        if not unique:
            raise MKUserError("alias", info)

<<<<<<< HEAD
        new_id = html.request.var("id")
        if len(new_id) == 0:
            raise MKUserError("id", _("Please specify an ID for the new role."))
=======
        new_id = html.request.get_ascii_input_mandatory("id")
>>>>>>> upstream/master
        if not re.match("^[-a-z0-9A-Z_]*$", new_id):
            raise MKUserError(
                "id", _("Invalid role ID. Only the characters a-z, A-Z, 0-9, _ and - are allowed."))
        if new_id != self._role_id:
            if new_id in self._roles:
                raise MKUserError("id", _("The ID is already used by another role"))

        self._role["alias"] = alias

        # based on
        if not self._role.get("builtin"):
<<<<<<< HEAD
            basedon = html.request.var("basedon")
=======
            basedon = html.request.get_ascii_input_mandatory("basedon")
>>>>>>> upstream/master
            if basedon not in config.builtin_role_ids:
                raise MKUserError("basedon",
                                  _("Invalid valid for based on. Must be id of builtin rule."))
            self._role["basedon"] = basedon

        # Permissions
        permissions = self._role["permissions"]
        for var_name, value in html.request.itervars(prefix="perm_"):
            try:
<<<<<<< HEAD
                perm = permission_registry[var_name[5:]]()
=======
                perm = permission_registry[var_name[5:]]
>>>>>>> upstream/master
            except KeyError:
                continue

            if value == "yes":
                permissions[perm.name] = True
            elif value == "no":
                permissions[perm.name] = False
            elif value == "default":
                try:
                    del permissions[perm.name]
                except KeyError:
                    pass  # Already at defaults

        if self._role_id != new_id:
            self._roles[new_id] = self._role
            del self._roles[self._role_id]
            self._rename_user_role(self._role_id, new_id)

        self._save_roles()
        watolib.add_change("edit-roles",
                           _("Modified user role '%s'") % new_id,
                           sites=config.get_login_sites())
<<<<<<< HEAD
        return "roles"

    def page(self):
        search = get_search_expression()
        search_form(_("Search for permissions: "), "edit_role")
=======
        return redirect(mode_url("roles"))

    def page(self):
        search = get_search_expression()
>>>>>>> upstream/master

        html.begin_form("role", method="POST")

        # ID
        forms.header(_("Basic Properties"))
        forms.section(_("Internal ID"), simple="builtin" in self._role)
        if self._role.get("builtin"):
            html.write_text("%s (%s)" % (self._role_id, _("builtin role")))
            html.hidden_field("id", self._role_id)
        else:
            html.text_input("id", self._role_id)
            html.set_focus("id")

        # Alias
        forms.section(_("Alias"))
        html.help(_("An alias or description of the role"))
        html.text_input("alias", self._role.get("alias", ""), size=50)

        # Based on
        if not self._role.get("builtin"):
            forms.section(_("Based on role"))
            html.help(
                _("Each user defined role is based on one of the builtin roles. "
                  "When created it will start with all permissions of that role. When due to a software "
                  "update or installation of an addons new permissions appear, the user role will get or "
                  "not get those new permissions based on the default settings of the builtin role it's "
                  "based on."))
<<<<<<< HEAD
            choices = [(i, r["alias"]) for i, r in self._roles.items() if r.get("builtin")]
            html.dropdown("basedon", choices, deflt=self._role.get("basedon", "user"), ordered=True)
=======
            role_choices: Choices = [
                (i, r["alias"]) for i, r in self._roles.items() if r.get("builtin")
            ]
            html.dropdown("basedon",
                          role_choices,
                          deflt=self._role.get("basedon", "user"),
                          ordered=True)
>>>>>>> upstream/master

        forms.end()

        html.h2(_("Permissions"))

        # Permissions
        base_role_id = self._role.get("basedon", self._role_id)

        html.help(
            _("When you leave the permissions at &quot;default&quot; then they get their "
              "settings from the factory defaults (for builtin roles) or from the "
              "factory default of their base role (for user define roles). Factory defaults "
              "may change due to software updates. When choosing another base role, all "
              "permissions that are on default will reflect the new base role."))

        for section in permission_section_registry.get_sorted_sections():
            # Now filter by the optional search term
            filtered_perms = []
            for perm in permission_registry.get_sorted_permissions(section):
                if search and (search not in perm.title.lower() and
                               search not in perm.name.lower()):
                    continue

                filtered_perms.append(perm)

            if not filtered_perms:
                continue

            forms.header(section.title, isopen=search is not None)
            for perm in filtered_perms:
                forms.section(perm.title)

                pvalue = self._role["permissions"].get(perm.name)
                def_value = base_role_id in perm.defaults

<<<<<<< HEAD
                choices = [("yes", _("yes")), ("no", _("no")),
                           ("default", _("default (%s)") % (def_value and _("yes") or _("no")))]
=======
                choices: Choices = [
                    ("yes", _("yes")),
                    ("no", _("no")),
                    ("default", _("default (%s)") % (def_value and _("yes") or _("no"))),
                ]
>>>>>>> upstream/master
                deflt = {True: "yes", False: "no"}.get(pvalue, "default")

                html.dropdown("perm_" + perm.name, choices, deflt=deflt, style="width: 130px;")
                html.help(perm.description)

        forms.end()
<<<<<<< HEAD
        html.button("save", _("Save"))
=======
>>>>>>> upstream/master
        html.hidden_fields()
        html.end_form()


@mode_registry.register
class ModeRoleMatrix(WatoMode):
    @classmethod
    def name(cls):
        return "role_matrix"

    @classmethod
    def permissions(cls):
        return ["users"]

<<<<<<< HEAD
    def title(self):
        return _("Role & Permission Matrix")

    def buttons(self):
        global_buttons()
        html.context_button(_("Back"), watolib.folder_preserving_link([("mode", "roles")]), "back")

    def page(self):
        role_list = sorted(userdb.load_roles().items(), key=lambda a: (a[1]["alias"], a[0]))
=======
    @classmethod
    def parent_mode(cls) -> Optional[Type[WatoMode]]:
        return ModeRoles

    def title(self):
        return _("Permission matrix")

    def page(self):
        role_list = sorted(userdb_utils.load_roles().items(), key=lambda a: (a[1]["alias"], a[0]))
>>>>>>> upstream/master

        for section in permission_section_registry.get_sorted_sections():
            html.begin_foldable_container("perm_matrix",
                                          section.name,
                                          section.name == "general",
                                          section.title,
                                          indent=True)

            with table_element(section.name) as table:

                for perm in permission_registry.get_sorted_permissions(section):
                    table.row()
                    table.cell(_("Permission"), perm.title, css="wide")
                    html.help(perm.description)
                    for role_id, role in role_list:
                        base_on_id = role.get('basedon', role_id)
                        pvalue = role["permissions"].get(perm.name)
                        if pvalue is None:
                            if base_on_id in perm.defaults:
<<<<<<< HEAD
                                icon_name = "perm_yes_default"
=======
                                icon_name: Optional[str] = "perm_yes_default"
>>>>>>> upstream/master
                            else:
                                icon_name = None
                        else:
                            icon_name = "perm_%s" % (pvalue and "yes" or "no")

                        table.cell(role_id, css="center")
                        if icon_name:
<<<<<<< HEAD
                            html.icon(None, icon_name)
=======
                            html.icon(icon_name)
>>>>>>> upstream/master

            html.end_foldable_container()

        html.close_table()
