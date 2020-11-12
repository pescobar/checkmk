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

import os
import copy
import sys
import traceback
import json
<<<<<<< HEAD
from typing import Dict, List, Type, Callable  # pylint: disable=unused-import
=======
from contextlib import contextmanager
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Tuple, Union

from livestatus import SiteId

import cmk.utils.version as cmk_version
import cmk.utils.store as store
from cmk.utils.type_defs import UserId
>>>>>>> upstream/master

import cmk.gui.pages
import cmk.gui.utils as utils
from cmk.gui.log import logger
from cmk.gui.exceptions import HTTPRedirect, MKGeneralException, MKAuthException, MKUserError
from cmk.gui.permissions import declare_permission
from cmk.gui.pages import page_registry
<<<<<<< HEAD
from cmk.gui.valuespec import (
    Dictionary,
    ListChoice,
=======
from cmk.gui.type_defs import (
    FilterHTTPVariables,
    FilterName,
    HTTPVariables,
    InfoName,
    SingleInfos,
    Visual,
    VisualContext,
    VisualTypeName,
)
from cmk.gui.valuespec import (
    Dictionary,
    DualListChoice,
>>>>>>> upstream/master
    ValueSpec,
    ListOfMultiple,
    ABCPageListOfMultipleGetChoice,
    FixedValue,
    IconSelector,
    Checkbox,
    TextUnicode,
    TextAscii,
    TextAreaUnicode,
<<<<<<< HEAD
)
=======
    DropdownChoice,
    Integer,
    ListOfMultipleChoiceGroup,
    GroupedListOfMultipleChoices,
)

>>>>>>> upstream/master
import cmk.gui.config as config
import cmk.gui.forms as forms
from cmk.gui.table import table_element
import cmk.gui.userdb as userdb
import cmk.gui.pagetypes as pagetypes
<<<<<<< HEAD
import cmk.utils.store as store
import cmk.gui.metrics as metrics
import cmk.gui.i18n
from cmk.gui.i18n import _u, _
from cmk.gui.globals import html
=======
import cmk.gui.i18n
from cmk.gui.i18n import _u, _
from cmk.gui.globals import html, request as global_request
from cmk.gui.breadcrumb import make_main_menu_breadcrumb, Breadcrumb, BreadcrumbItem
from cmk.gui.page_menu import (
    PageMenuDropdown,
    PageMenuTopic,
    PageMenuEntry,
    PageMenuLink,
    make_javascript_link,
    make_simple_link,
    make_simple_form_page_menu,
)
from cmk.gui.main_menu import mega_menu_registry
>>>>>>> upstream/master

from cmk.gui.plugins.visuals.utils import (
    visual_info_registry,
    visual_type_registry,
    filter_registry,
)

<<<<<<< HEAD
# Needed for legacy (pre 1.6) plugins
from cmk.gui.plugins.visuals.utils import (  # pylint: disable=unused-import
    Filter, FilterTime, FilterTristate, FilterUnicodeFilter,
)
from cmk.gui.permissions import permission_registry

if not cmk.is_raw_edition():
    import cmk.gui.cee.plugins.visuals

if cmk.is_managed_edition():
    import cmk.gui.cme.plugins.visuals
=======
from cmk.gui.utils.urls import makeuri, makeuri_contextless, make_confirm_link

# Needed for legacy (pre 1.6) plugins
from cmk.gui.plugins.visuals.utils import (  # noqa: F401 # pylint: disable=unused-import
    Filter, FilterTime, FilterTristate,
)
from cmk.gui.permissions import permission_registry

if not cmk_version.is_raw_edition():
    import cmk.gui.cee.plugins.visuals  # pylint: disable=no-name-in-module

if cmk_version.is_managed_edition():
    import cmk.gui.cme.plugins.visuals  # pylint: disable=no-name-in-module
>>>>>>> upstream/master

#   .--Plugins-------------------------------------------------------------.
#   |                   ____  _             _                              |
#   |                  |  _ \| |_   _  __ _(_)_ __  ___                    |
#   |                  | |_) | | | | |/ _` | | '_ \/ __|                   |
#   |                  |  __/| | |_| | (_| | | | | \__ \                   |
#   |                  |_|   |_|\__,_|\__, |_|_| |_|___/                   |
#   |                                 |___/                                |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'

<<<<<<< HEAD
loaded_with_language = False
title_functions = []  # type: List[Callable]
=======
loaded_with_language: Union[bool, None, str] = False
title_functions: List[Callable] = []
>>>>>>> upstream/master


def load_plugins(force):
    global loaded_with_language, title_functions
    if loaded_with_language == cmk.gui.i18n.get_current_language() and not force:
        return

    title_functions = []

    utils.load_web_plugins('visuals', globals())

    loaded_with_language = cmk.gui.i18n.get_current_language()


# TODO: This has been obsoleted by pagetypes.py
def declare_visual_permissions(what, what_plural):
    declare_permission(
        "general.edit_" + what,
        _("Customize %s and use them") % what_plural,
        _("Allows to create own %s, customize builtin %s and use them.") %
        (what_plural, what_plural),
        ["admin", "user"],
    )

    declare_permission(
        "general.publish_" + what,
        _("Publish %s") % what_plural,
        _("Make %s visible and usable for other users.") % what_plural,
        ["admin", "user"],
    )

    declare_permission(
        "general.publish_" + what + "_to_foreign_groups",
        _("Publish %s to foreign contact groups") % what_plural,
        _("Make %s visible and usable for users of contact groups the publishing user is not a member of."
         ) % what_plural,
        ["admin"],
    )

    declare_permission(
        "general.see_user_" + what,
        _("See user %s") % what_plural,
        _("Is needed for seeing %s that other users have created.") % what_plural,
        ["admin", "user", "guest"],
    )

    declare_permission(
        "general.force_" + what,
        _("Modify builtin %s") % what_plural,
        _("Make own published %s override builtin %s for all users.") % (what_plural, what_plural),
        ["admin"],
    )

    declare_permission(
        "general.edit_foreign_" + what,
        _("Edit foreign %s") % what_plural,
        _("Allows to edit %s created by other users.") % what_plural,
        ["admin"],
    )

    declare_permission(
        "general.delete_foreign_" + what,
        _("Delete foreign %s") % what_plural,
        _("Allows to delete %s created by other users.") % what_plural,
        ["admin"],
    )


#.
#   .--Save/Load-----------------------------------------------------------.
#   |          ____                     ___                    _           |
#   |         / ___|  __ ___   _____   / / |    ___   __ _  __| |          |
#   |         \___ \ / _` \ \ / / _ \ / /| |   / _ \ / _` |/ _` |          |
#   |          ___) | (_| |\ V /  __// / | |__| (_) | (_| | (_| |          |
#   |         |____/ \__,_| \_/ \___/_/  |_____\___/ \__,_|\__,_|          |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
class UserVisualsCache(object):
=======
class UserVisualsCache:
>>>>>>> upstream/master
    """Realizes a in memory cache (per apache process). This has been introduced to improve the
    situation where there are hundreds of custom visuals (views here). These visuals are rarely
    changed, but read and evaluated(!) during each page request which costs a lot of time."""
    def __init__(self):
        super(UserVisualsCache, self).__init__()
        self._cache = {}

    def get(self, path):
        try:
            cached_mtime, cached_user_visuals = self._cache[path]
            current_mtime = os.stat(path).st_mtime
            return cached_user_visuals if current_mtime <= cached_mtime else None
        except (KeyError, IOError):
            return None

    def add(self, path, modification_timestamp, user_visuals):
        self._cache[path] = modification_timestamp, user_visuals


_user_visuals_cache = UserVisualsCache()


def save(what, visuals, user_id=None):
    if user_id is None:
        user_id = config.user.id

    uservisuals = {}
    for (owner_id, name), visual in visuals.items():
        if user_id == owner_id:
            uservisuals[name] = visual
    config.save_user_file('user_' + what, uservisuals, user_id=user_id)


# FIXME: Currently all user visual files of this type are locked. We could optimize
# this not to lock all files but only lock the files the user is about to modify.
<<<<<<< HEAD
def load(what, builtin_visuals, skip_func=None, lock=False):
    visuals = {}
=======
def load(what: str,
         builtin_visuals: Dict[Any, Any],
         skip_func: Optional[Callable[[Dict[Any, Any]], bool]] = None,
         lock: bool = False) -> Dict[Tuple[UserId, str], Dict[str, Any]]:
    visuals: Dict[Tuple[UserId, str], Dict[str, Any]] = {}
>>>>>>> upstream/master

    # first load builtins. Set username to ''
    for name, visual in builtin_visuals.items():
        visual["owner"] = ''  # might have been forgotten on copy action
        visual["public"] = True
        visual["name"] = name

        # Dashboards had not all COMMON fields in previous versions. Add them
        # here to be compatible for a specific time. Seamless migration, yeah.
        visual.setdefault('description', '')
        visual.setdefault('hidden', False)

<<<<<<< HEAD
        visuals[('', name)] = visual
=======
        visuals[(UserId(''), name)] = visual
>>>>>>> upstream/master

    # Now scan users subdirs for files "user_*.mk"
    visuals.update(load_user_visuals(what, builtin_visuals, skip_func, lock))

    return visuals


# This is currently not called by load() because some visual type (e.g. view) specific transform
# needs to be executed in advance. This should be cleaned up.
def transform_old_visual(visual):
    """Prepare visuals for working with them. Migrate old formats or add default settings, for example"""
    visual.setdefault('single_infos', [])
    visual.setdefault('context', {})
<<<<<<< HEAD
=======
    visual.setdefault('link_from', {})
    visual.setdefault('topic', '')
    visual.setdefault("icon", None)
>>>>>>> upstream/master

    # 1.6 introduced this setting: Ensure all visuals have it set
    visual.setdefault("add_context_to_title", True)

<<<<<<< HEAD

def load_user_visuals(what, builtin_visuals, skip_func, lock):
    visuals = {}
=======
    # 1.7 introduced these settings for the new mega menus
    visual.setdefault("sort_index", 99)
    visual.setdefault("is_show_more", False)


def load_user_visuals(what: str, builtin_visuals: Dict[Any, Any],
                      skip_func: Optional[Callable[[Dict[Any, Any]],
                                                   bool]], lock: bool) -> Dict[Any, Any]:
    visuals: Dict[Any, Any] = {}
>>>>>>> upstream/master

    subdirs = os.listdir(config.config_dir)
    for user in subdirs:
        try:
            dirpath = config.config_dir + "/" + user
            if not os.path.isdir(dirpath):
                continue

            # Be compatible to old views.mk. The views.mk contains customized views
            # in an old format which will be loaded, transformed and when saved stored
            # in users_views.mk. When this file exists only this file is used.
            path = "%s/user_%s.mk" % (dirpath, what)
            if what == 'views' and not os.path.exists(path):
                path = "%s/%s.mk" % (dirpath, what)

            if not os.path.exists(path):
                continue

<<<<<<< HEAD
            if not userdb.user_exists(user):
=======
            if not userdb.user_exists(UserId(user)):
>>>>>>> upstream/master
                continue

            user_visuals = _user_visuals_cache.get(path)
            if user_visuals is None:
                modification_timestamp = os.stat(path).st_mtime
                user_visuals = load_visuals_of_a_user(what, builtin_visuals, skip_func, lock, path,
                                                      user)
                _user_visuals_cache.add(path, modification_timestamp, user_visuals)

            visuals.update(user_visuals)

        except SyntaxError as e:
            raise MKGeneralException(_("Cannot load %s from %s: %s") % (what, path, e))

    return visuals


def load_visuals_of_a_user(what, builtin_visuals, skip_func, lock, path, user):
    user_visuals = {}
<<<<<<< HEAD
    for name, visual in store.load_data_from_file(path, {}, lock).items():
=======
    for name, visual in store.load_object_from_file(path, default={}, lock=lock).items():
>>>>>>> upstream/master
        visual["owner"] = user
        visual["name"] = name

        if skip_func and skip_func(visual):
            continue

        # Maybe resolve inherited attributes. This was a feature for several versions
        # to make the visual texts localizable. This has been removed because the visual
        # texts can now be localized using the custom localization strings.
        # This is needed for backward compatibility to make the visuals without these
        # attributes get the attributes from their builtin visual.
        builtin_visual = builtin_visuals.get(name)
        if builtin_visual:
<<<<<<< HEAD
            for attr in ['title', 'linktitle', 'topic', 'description']:
=======
            for attr in ['title', 'topic', 'description']:
>>>>>>> upstream/master
                if attr not in visual and attr in builtin_visual:
                    visual[attr] = builtin_visual[attr]

        # Repair visuals with missing 'title' or 'description'
        visual.setdefault("title", name)
        visual.setdefault("description", "")

        # Declare custom permissions
        declare_visual_permission(what, name, visual)

        user_visuals[(user, name)] = visual

    return user_visuals


def declare_visual_permission(what, name, visual):
    permname = "%s.%s" % (what[:-1], name)
    if visual["public"] and permname not in permission_registry:
        declare_permission(permname, visual["title"], visual["description"],
                           ['admin', 'user', 'guest'])


# Load all users visuals just in order to declare permissions of custom visuals
def declare_custom_permissions(what):
    subdirs = os.listdir(config.config_dir)
    for user in subdirs:
        try:
            dirpath = config.config_dir + "/" + user
            if os.path.isdir(dirpath):
                path = "%s/%s.mk" % (dirpath, what)
                if not os.path.exists(path):
                    continue
<<<<<<< HEAD
                visuals = store.load_data_from_file(path, {})
=======
                visuals = store.load_object_from_file(path, default={})
>>>>>>> upstream/master
                for name, visual in visuals.items():
                    declare_visual_permission(what, name, visual)
        except Exception:
            if config.debug:
                raise


# Get the list of visuals which are available to the user
# (which could be retrieved with get_visual)
def available(what, all_visuals):
    user = config.user.id
    visuals = {}
    permprefix = what[:-1]

    def published_to_user(visual):
        if visual["public"] is True:
            return True

        if isinstance(visual["public"], tuple) and visual["public"][0] == "contact_groups":
<<<<<<< HEAD
            user_groups = set(userdb.contactgroups_of_user(user))
=======
            user_groups = set([] if user is None else userdb.contactgroups_of_user(user))
>>>>>>> upstream/master
            if user_groups.intersection(visual["public"][1]):
                return True

        return False

    # 1. user's own visuals, if allowed to edit visuals
    if config.user.may("general.edit_" + what):
        for (u, n), visual in all_visuals.items():
            if u == user:
                visuals[n] = visual

    # 2. visuals of special users allowed to globally override builtin visuals
    for (u, n), visual in all_visuals.items():
        if n not in visuals and published_to_user(visual) and config.user_may(
                u, "general.force_" + what):
            # Honor original permissions for the current user
            permname = "%s.%s" % (permprefix, n)
            if permname in permission_registry \
<<<<<<< HEAD
                and not config.user.may(permname):
=======
                    and not config.user.may(permname):
>>>>>>> upstream/master
                continue
            visuals[n] = visual

    # 3. Builtin visuals, if allowed.
    for (u, n), visual in all_visuals.items():
        if u == '' and n not in visuals and config.user.may("%s.%s" % (permprefix, n)):
            visuals[n] = visual

    # 4. other users visuals, if public. Sill make sure we honor permission
    #    for builtin visuals. Also the permission "general.see_user_visuals" is
    #    necessary.
    if config.user.may("general.see_user_" + what):
        for (u, n), visual in all_visuals.items():
            if n not in visuals and published_to_user(visual) and config.user_may(
                    u, "general.publish_" + what):
                # Is there a builtin visual with the same name? If yes, honor permissions.
                permname = "%s.%s" % (permprefix, n)
                if permname in permission_registry \
<<<<<<< HEAD
                    and not config.user.may(permname):
=======
                        and not config.user.may(permname):
>>>>>>> upstream/master
                    continue
                visuals[n] = visual

    return visuals


#.
#   .--Listing-------------------------------------------------------------.
#   |                    _     _     _   _                                 |
#   |                   | |   (_)___| |_(_)_ __   __ _                     |
#   |                   | |   | / __| __| | '_ \ / _` |                    |
#   |                   | |___| \__ \ |_| | | | | (_| |                    |
#   |                   |_____|_|___/\__|_|_| |_|\__, |                    |
#   |                                            |___/                     |
#   +----------------------------------------------------------------------+
#   | Show a list of all visuals with actions to delete/clone/edit         |
#   '----------------------------------------------------------------------'


# TODO: This code has been copied to a new live into htdocs/pagetypes.py
# We need to convert all existing page types (views, dashboards, reports)
# to pagetypes.py and then remove this function!
def page_list(what,
              title,
              visuals,
              custom_columns=None,
              render_custom_buttons=None,
              render_custom_columns=None,
<<<<<<< HEAD
              render_custom_context_buttons=None,
=======
              custom_page_menu_entries=None,
>>>>>>> upstream/master
              check_deletable_handler=None):

    if custom_columns is None:
        custom_columns = []

    what_s = what[:-1]
    if not config.user.may("general.edit_" + what):
        raise MKAuthException(_("Sorry, you lack the permission for editing this type of visuals."))

<<<<<<< HEAD
    html.header(title)

    html.begin_context_buttons()
    html.context_button(_('New'), 'create_%s.py' % what_s, "new")
    if render_custom_context_buttons:
        render_custom_context_buttons()

    for plugin_class in visual_type_registry.values():
        plugin = plugin_class()
        if what != plugin.ident:
            html.context_button(plugin.plural_title.title(), 'edit_%s.py' % plugin.ident,
                                plugin.ident[:-1])

    # TODO: We hack in those visuals that already have been moved to pagetypes here
    if pagetypes.has_page_type("graph_collection"):
        html.context_button(_("Graph collections"), "graph_collections.py", "graph_collection")
    if pagetypes.has_page_type("custom_graph"):
        html.context_button(_("Custom graphs"), "custom_graphs.py", "custom_graph")
    if pagetypes.has_page_type("forecast_graph"):
        html.context_button(_("Forecast Graphs"), "forecast_graphs.py", "forecast_graph")
    if pagetypes.has_page_type("graph_tuning"):
        html.context_button(_("Graph tunings"), "graph_tunings.py", "graph_tuning")
    if pagetypes.has_page_type("sla_configuration"):
        html.context_button(_("SLAs"), "sla_configurations.py", "sla_configuration")
    if pagetypes.has_page_type("custom_snapin"):
        html.context_button(_("Custom snapins"), "custom_snapins.py", "custom_snapin")
    html.context_button(_("Bookmark lists"), "bookmark_lists.py", "bookmark_list")

    html.end_context_buttons()

    # Deletion of visuals
    delname = html.request.var("_delete")
    if delname and html.transaction_valid():
        if config.user.may('general.delete_foreign_%s' % what):
            user_id = html.request.var('_user_id', config.user.id)
        else:
            user_id = config.user.id

        deltitle = visuals[(user_id, delname)]['title']

=======
    breadcrumb = visual_page_breadcrumb(what, title, "list")

    visual_type = visual_type_registry[what]()
    current_type_dropdown = PageMenuDropdown(
        name=what,
        title=visual_type.plural_title.title(),
        topics=[
            PageMenuTopic(
                title=visual_type.plural_title.title(),
                entries=[
                    PageMenuEntry(
                        title=_('Add %s') % visual_type.title,
                        icon_name="new",
                        item=make_simple_link("create_%s.py" % what_s),
                        is_shortcut=True,
                        is_suggested=True,
                    ),
                ] + (list(custom_page_menu_entries()) if custom_page_menu_entries else []),
            ),
        ],
    )

    page_menu = pagetypes.customize_page_menu(breadcrumb, current_type_dropdown, what)
    html.header(title, breadcrumb, page_menu)

    # Deletion of visuals
    delname = html.request.var("_delete")
    if delname and html.check_transaction():
        if config.user.may('general.delete_foreign_%s' % what):
            user_id_str = html.request.get_unicode_input('_user_id', config.user.id)
            user_id = None if user_id_str is None else UserId(user_id_str)
        else:
            user_id = config.user.id

>>>>>>> upstream/master
        try:
            if check_deletable_handler:
                check_deletable_handler(visuals, user_id, delname)

<<<<<<< HEAD
            c = html.confirm(_("Please confirm the deletion of \"%s\".") % deltitle)
            if c:
                del visuals[(user_id, delname)]
                save(what, visuals, user_id)
                html.reload_sidebar()
            elif c is False:
                html.footer()
                return
=======
            del visuals[(user_id, delname)]
            save(what, visuals, user_id)
            html.reload_sidebar()
>>>>>>> upstream/master
        except MKUserError as e:
            html.user_error(e)

    keys_sorted = sorted(sorted(visuals.keys(), key=lambda x: x[1]),
                         key=lambda x: x[0],
                         reverse=True)

    my_visuals, foreign_visuals, builtin_visuals = [], [], []
    for (owner, visual_name) in keys_sorted:
        if owner == "" and not config.user.may("%s.%s" % (what_s, visual_name)):
            continue  # not allowed to see this view

        visual = visuals[(owner, visual_name)]
        if visual["public"] and owner == "":
            builtin_visuals.append((owner, visual_name, visual))
        elif owner == config.user.id:
            my_visuals.append((owner, visual_name, visual))
        elif (visual["public"] and owner != '' and config.user_may(owner, "general.publish_%s" % what)) or \
                config.user.may("general.edit_foreign_%s" % what):
            foreign_visuals.append((owner, visual_name, visual))

    for title1, items in [(_('Customized'), my_visuals),
                          (_("Owned by other users"), foreign_visuals),
                          (_('Builtin'), builtin_visuals)]:
        html.open_h3()
        html.write(title1)
        html.close_h3()

        with table_element(css='data', limit=None) as table:

            for owner, visual_name, visual in items:
                table.row(css='data')

                # Actions
                table.cell(_('Actions'), css='buttons visuals')

                # Clone / Customize
                buttontext = _("Create a customized copy of this")
<<<<<<< HEAD
                backurl = html.urlencode(html.makeuri([]))
=======
                backurl = html.urlencode(makeuri(global_request, []))
>>>>>>> upstream/master
                clone_url = "edit_%s.py?load_user=%s&load_name=%s&back=%s" \
                            % (what_s, owner, visual_name, backurl)
                html.icon_button(clone_url, buttontext, "clone")

                # Delete
                if owner and (owner == config.user.id or
                              config.user.may('general.delete_foreign_%s' % what)):
                    add_vars = [('_delete', visual_name)]
                    if owner != config.user.id:
                        add_vars.append(('_user_id', owner))
<<<<<<< HEAD
                    html.icon_button(html.makeactionuri(add_vars), _("Delete!"), "delete")
=======
                    html.icon_button(
                        make_confirm_link(
                            url=html.makeactionuri(add_vars),
                            message=_("Please confirm the deletion of \"%s\".") % visual['title'],
                        ), _("Delete!"), "delete")
>>>>>>> upstream/master

                # Edit
                if owner == config.user.id or (owner != "" and
                                               config.user.may("general.edit_foreign_%s" % what)):
                    edit_vars = [("load_name", visual_name)]
                    if owner != config.user.id:
                        edit_vars.append(("owner", owner))
<<<<<<< HEAD
                    edit_url = html.makeuri_contextless(edit_vars, filename="edit_%s.py" % what_s)
=======
                    edit_url = makeuri_contextless(
                        global_request,
                        edit_vars,
                        filename="edit_%s.py" % what_s,
                    )
>>>>>>> upstream/master
                    html.icon_button(edit_url, _("Edit"), "edit")

                # Custom buttons - visual specific
                if render_custom_buttons:
                    render_custom_buttons(visual_name, visual)

                # visual Name
                table.cell(_('ID'), visual_name)

                # Title
                table.cell(_('Title'))
                title2 = _u(visual['title'])
                if _visual_can_be_linked(what, visual_name, visuals, visual, owner):
                    html.a(title2,
                           href="%s.py?%s=%s" %
                           (what_s, visual_type_registry[what]().ident_attr, visual_name))
                else:
                    html.write_text(title2)
                html.help(_u(visual['description']))

                # Custom cols
                for title3, renderer in custom_columns:
                    table.cell(title3, renderer(visual))

                # Owner
                if owner == "":
                    ownertxt = "<i>" + _("builtin") + "</i>"
                else:
                    ownertxt = owner
                table.cell(_('Owner'), ownertxt)
                table.cell(_('Public'), visual["public"] and _("yes") or _("no"))
                table.cell(_('Hidden'), visual["hidden"] and _("yes") or _("no"))

                if render_custom_columns:
                    render_custom_columns(table, visual_name, visual)

    html.footer()


def _visual_can_be_linked(what, visual_name, all_visuals, visual, owner):
<<<<<<< HEAD
    if visual["hidden"]:
=======
    if what != "dashboards" and visual["hidden"]:
>>>>>>> upstream/master
        return False  # don't link to hidden visuals

    if owner == config.user.id:
        return True

    # Is this the visual which would be shown to the user in case the user
    # requests a visual with the current name?
    user_visuals = available(what, all_visuals)
    if user_visuals.get(visual_name) != visual:
        return False

    return visual["public"]


#.
#   .--Create Visual-------------------------------------------------------.
#   |      ____                _        __     ___                 _       |
#   |     / ___|_ __ ___  __ _| |_ ___  \ \   / (_)___ _   _  __ _| |      |
#   |    | |   | '__/ _ \/ _` | __/ _ \  \ \ / /| / __| | | |/ _` | |      |
#   |    | |___| | |  __/ (_| | ||  __/   \ V / | \__ \ |_| | (_| | |      |
#   |     \____|_|  \___|\__,_|\__\___|    \_/  |_|___/\__,_|\__,_|_|      |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Realizes the steps before getting to the editor (context type)       |
#   '----------------------------------------------------------------------'


def page_create_visual(what, info_keys, next_url=None):
<<<<<<< HEAD
    title = visual_type_registry[what]().title
    what_s = what[:-1]

    # FIXME: Sort by (assumed) common usage
    info_choices = []
    for key in info_keys:
        info_choices.append(
            (key, _('Show information of a single %s') % visual_info_registry[key]().title))

    vs_infos = SingleInfoSelection(info_keys)

    html.header(_('Create %s') % title)
    html.begin_context_buttons()
    html.context_button(_("Back"), html.get_url_input("back", "edit_%s.py" % what), "back")
    html.end_context_buttons()
=======
    title = _('Create %s') % visual_type_registry[what]().title
    what_s = what[:-1]

    vs_infos = SingleInfoSelection(info_keys)

    breadcrumb = visual_page_breadcrumb(what, title, "create")
    html.header(
        title, breadcrumb,
        make_simple_form_page_menu(breadcrumb,
                                   form_name="create_visual",
                                   button_name="save",
                                   save_title=_("Continue")))
>>>>>>> upstream/master

    html.open_p()
    html.write(
        _('Depending on the choosen datasource a %s can list <i>multiple</i> or <i>single</i> objects. '
          'For example the <i>services</i> datasource can be used to simply create a list '
          'of <i>multiple</i> services, a list of <i>multiple</i> services of a <i>single</i> host or even '
          'a list of services with the same name on <i>multiple</i> hosts. When you just want to '
          'create a list of objects, you do not need to make any selection in this dialog. '
          'If you like to create a view for one specific object of a specific type, select the '
          'object type below and continue.') % what_s)
    html.close_p()

    if html.request.var('save') and html.check_transaction():
        try:
            single_infos = vs_infos.from_html_vars('single_infos')
            vs_infos.validate_value(single_infos, 'single_infos')

            if not next_url:
                next_url = 'edit_' + what_s + '.py?mode=create&single_infos=%s' % ','.join(
                    single_infos)
            else:
                next_url += '&single_infos=%s' % ','.join(single_infos)
            raise HTTPRedirect(next_url)
        except MKUserError as e:
            html.user_error(e)

    html.begin_form('create_visual')
    html.hidden_field('mode', 'create')

    forms.header(_('Select specific object type'))
    forms.section(vs_infos.title())
    vs_infos.render_input('single_infos', '')
    html.help(vs_infos.help())
    forms.end()

<<<<<<< HEAD
    html.button('save', _('Continue'), 'submit')

=======
>>>>>>> upstream/master
    html.hidden_fields()
    html.end_form()
    html.footer()


#.
#   .--Edit Visual---------------------------------------------------------.
#   |           _____    _ _ _    __     ___                 _             |
#   |          | ____|__| (_) |_  \ \   / (_)___ _   _  __ _| |            |
#   |          |  _| / _` | | __|  \ \ / /| / __| | | |/ _` | |            |
#   |          | |__| (_| | | |_    \ V / | \__ \ |_| | (_| | |            |
#   |          |_____\__,_|_|\__|    \_/  |_|___/\__,_|\__,_|_|            |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Edit global settings of the visual                                   |
#   '----------------------------------------------------------------------'


def get_context_specs(visual, info_handler):
<<<<<<< HEAD
    info_keys = []
    if info_handler:
        info_keys = info_handler(visual)

    if not info_keys:
        info_keys = visual_info_registry.keys()
=======
    info_keys = list(visual_info_registry.keys())
    if info_handler:
        handler_keys = info_handler(visual)
        if handler_keys is not None:
            info_keys = handler_keys
>>>>>>> upstream/master

    single_info_keys = [key for key in info_keys if key in visual['single_infos']]
    multi_info_keys = [key for key in info_keys if key not in single_info_keys]

<<<<<<< HEAD
    def visual_spec_single(info_key):
        info = visual_info_registry[info_key]()
        params = info.single_spec
        optional = True
        isopen = True
        return Dictionary(
            title=info.title,
            form_isopen=isopen,
            optional_keys=optional,
            elements=params,
        )

    def visual_spec_multi(info_key):
        info = visual_info_registry[info_key]()
        filter_list = VisualFilterList([info_key], title=info.title, ignore=set(single_info_keys))
        filter_names = filter_list.filter_names()
        # Skip infos which have no filters available
        return filter_list if filter_names else None

    # single infos first, the rest afterwards
    return [(info_key, visual_spec_single(info_key))
            for info_key in single_info_keys] + \
           [(info_key, visual_spec_multi(info_key))
            for info_key in multi_info_keys
            if visual_spec_multi(info_key)]


def process_context_specs(context_specs):
    context = {}
=======
    def host_service_lead(val):
        # Sort is stable in python, thus only prioritize host>service>rest
        if val[0] == "host":
            return 0
        if val[0] == "service":
            return 1
        return 2

    # single infos first, the rest afterwards
    context_specs = [(info_key, visual_spec_single(info_key))
                     for info_key in single_info_keys] + \
                    [(info_key, visual_spec_multi(info_key, single_info_keys))
                     for info_key in multi_info_keys
                     if visual_spec_multi(info_key, single_info_keys)]

    return sorted(context_specs, key=host_service_lead)


def visual_spec_single(info_key):
    info = visual_info_registry[info_key]()
    params = info.single_spec
    optional = True
    isopen = True
    return Dictionary(
        title=info.title,
        form_isopen=isopen,
        optional_keys=optional,
        elements=params,
    )


def visual_spec_multi(info_key, single_info_keys):
    info = visual_info_registry[info_key]()
    filter_list = VisualFilterList([info_key], title=info.title, ignore=set(single_info_keys))
    filter_names = filter_list.filter_names()
    # Skip infos which have no filters available
    return filter_list if filter_names else None


def process_context_specs(context_specs):
    context: Dict[Any, Any] = {}
>>>>>>> upstream/master
    for info_key, spec in context_specs:
        ident = 'context_' + info_key

        attrs = spec.from_html_vars(ident)
        spec.validate_value(attrs, ident)
        context.update(attrs)
    return context


def render_context_specs(visual, context_specs):
<<<<<<< HEAD
    forms.header(_("Context / Search Filters"))
    for info_key, spec in context_specs:
        forms.section(spec.title())
        ident = 'context_' + info_key
        # Trick: the field "context" contains a dictionary with
        # all filter settings, from which the value spec will automatically
        # extract those that it needs.
        value = visual.get('context', {})
=======
    if not context_specs:
        return

    forms.header(_("Context / Search Filters"))
    # Trick: the field "context" contains a dictionary with
    # all filter settings, from which the value spec will automatically
    # extract those that it needs.
    value = visual.get('context', {})
    for info_key, spec in context_specs:
        forms.section(spec.title())
        ident = 'context_' + info_key
>>>>>>> upstream/master
        spec.render_input(ident, value)


def page_edit_visual(what,
                     all_visuals,
                     custom_field_handler=None,
                     create_handler=None,
                     load_handler=None,
                     info_handler=None,
<<<<<<< HEAD
                     sub_pages=None):
=======
                     sub_pages: pagetypes.SubPagesSpec = None):
>>>>>>> upstream/master
    if sub_pages is None:
        sub_pages = []

    visual_type = visual_type_registry[what]()
    if not config.user.may("general.edit_" + what):
        raise MKAuthException(_("You are not allowed to edit %s.") % visual_type.plural_title)
<<<<<<< HEAD
    visual = {}
=======
    visual: Dict[str, Any] = {
        'link_from': {},
    }
>>>>>>> upstream/master

    # Load existing visual from disk - and create a copy if 'load_user' is set
    visualname = html.request.var("load_name")
    oldname = visualname
<<<<<<< HEAD
    mode = html.request.var('mode', 'edit')
=======
    mode = html.request.get_ascii_input_mandatory('mode', 'edit')
>>>>>>> upstream/master
    owner_user_id = config.user.id
    if visualname:
        cloneuser = html.request.var("load_user")
        if cloneuser is not None:
            mode = 'clone'
            visual = copy.deepcopy(all_visuals.get((cloneuser, visualname), None))
            if not visual:
                raise MKUserError('cloneuser', _('The %s does not exist.') % visual_type.title)

            # Make sure, name is unique
<<<<<<< HEAD
            if cloneuser == owner_user_id:  # Clone own visual
=======
            if UserId(cloneuser) == owner_user_id:  # Clone own visual
>>>>>>> upstream/master
                newname = visualname + "_clone"
            else:
                newname = visualname
            # Name conflict -> try new names
            n = 1
            while (owner_user_id, newname) in all_visuals:
                n += 1
                newname = visualname + "_clone%d" % n
            visual["name"] = newname
            visual["public"] = False
            visualname = newname
            oldname = None  # Prevent renaming
<<<<<<< HEAD
            if cloneuser == owner_user_id:
                visual["title"] += _(" (Copy)")
        else:
            owner_user_id = html.request.var("owner", config.user.id)
=======
            if UserId(cloneuser) == owner_user_id:
                visual["title"] += _(" (Copy)")
        else:
            user_id_str = html.request.get_unicode_input("owner", config.user.id)
            owner_user_id = None if user_id_str is None else UserId(user_id_str)
>>>>>>> upstream/master
            visual = all_visuals.get((owner_user_id, visualname))
            if not visual:
                visual = all_visuals.get(('', visualname))  # load builtin visual
                mode = 'clone'
                if not visual:
                    raise MKUserError(None,
                                      _('The requested %s does not exist.') % visual_type.title)
                visual["public"] = False

        single_infos = visual['single_infos']

        if load_handler:
            load_handler(visual)

    else:
        mode = 'create'
        single_infos = []
        single_infos_raw = html.request.var('single_infos')
        if single_infos_raw:
            single_infos = single_infos_raw.split(',')
            for key in single_infos:
                if key not in visual_info_registry:
                    raise MKUserError('single_infos', _('The info %s does not exist.') % key)
        visual['single_infos'] = single_infos

    if mode == 'clone':
        title = _('Clone %s') % visual_type.title
    elif mode == 'create':
        title = _('Create %s') % visual_type.title
    else:
        title = _('Edit %s') % visual_type.title

<<<<<<< HEAD
    html.header(title)
    html.begin_context_buttons()
    back_url = html.get_url_input("back", "edit_%s.py" % what)
    html.context_button(_("Back"), back_url, "back")

    # Extra buttons to sub modules. These are used for things to edit about
    # this visual that are more complex to be done in one value spec.
    if mode not in ["clone", "create"]:
        for title, pagename, icon in sub_pages:
            uri = html.makeuri_contextless([(visual_type.ident_attr, visualname)],
                                           filename=pagename + '.py')
            html.context_button(title, uri, icon)
    html.end_context_buttons()
=======
    back_url = html.get_url_input("back", "edit_%s.py" % what)

    breadcrumb = visual_page_breadcrumb(what, title, mode)
    page_menu = pagetypes.make_edit_form_page_menu(
        breadcrumb,
        dropdown_name=what[:-1],
        mode=mode,
        type_title=visual_type.title,
        ident_attr_name=visual_type.ident_attr,
        sub_pages=sub_pages,
        form_name="visual",
        visualname=visualname,
    )
    html.header(title, breadcrumb, page_menu)
>>>>>>> upstream/master

    # A few checkboxes concerning the visibility of the visual. These will
    # appear as boolean-keys directly in the visual dict, but encapsulated
    # in a list choice in the value spec.
<<<<<<< HEAD
    visibility_elements = [
        ('hidden',
         FixedValue(
             True,
             title=_('Hide this %s from the sidebar') % visual_type.title,
=======
    visibility_elements: List[Tuple[str, ValueSpec]] = [
        ('hidden',
         FixedValue(
             True,
             title=_('Hide this %s in the monitor menu') % visual_type.title,
>>>>>>> upstream/master
             totext="",
         )),
        ('hidebutton',
         FixedValue(
             True,
<<<<<<< HEAD
             title=_('Do not show a context button to this %s') % visual_type.title,
=======
             title=_('Hide this %s in dropdown menus') % visual_type.title,
>>>>>>> upstream/master
             totext="",
         )),
    ]
    if config.user.may("general.publish_" + what):
        with_foreign_groups = config.user.may("general.publish_" + what + "_to_foreign_groups")
        visibility_elements.append(('public',
                                    pagetypes.PublishTo(
                                        type_title=visual_type.title,
                                        with_foreign_groups=with_foreign_groups,
                                    )))

    vs_general = Dictionary(
        title=_("General Properties"),
        render='form',
<<<<<<< HEAD
        optional_keys=None,
=======
        optional_keys=False,
        show_more_keys=["description", "add_context_to_title", "sort_index", "is_show_more"],
>>>>>>> upstream/master
        elements=[
            single_infos_spec(single_infos),
            ('name',
             TextAscii(
                 title=_('Unique ID'),
                 help=_("The ID will be used in URLs that point to a view, e.g. "
                        "<tt>view.py?view_name=<b>myview</b></tt>. It will also be used "
                        "internally for identifying a view. You can create several views "
                        "with the same title but only one per view name. If you create a "
                        "view that has the same view name as a builtin view, then your "
                        "view will override that (shadowing it)."),
                 regex='^[a-zA-Z0-9_]+$',
                 regex_error=_(
                     'The name of the view may only contain letters, digits and underscores.'),
                 size=50,
                 allow_empty=False)),
            ('title', TextUnicode(title=_('Title') + '<sup>*</sup>', size=50, allow_empty=False)),
<<<<<<< HEAD
            ('add_context_to_title',
             Checkbox(
                 title=_('Add context information to title'),
                 help=_("Whether or not additional information from the page context "
                        "(filters) should be added to the title given above."),
             )),
            ('topic', TextUnicode(title=_('Topic') + '<sup>*</sup>', size=50)),
            ('description', TextAreaUnicode(title=_('Description') + '<sup>*</sup>',
                                            rows=4,
                                            cols=50)),
            ('linktitle',
             TextUnicode(title=_('Button Text') + '<sup>*</sup>',
                         help=_('If you define a text here, then it will be used in '
                                'context buttons linking to the %s instead of the regular title.') %
                         visual_type.title,
                         size=26)),
            ('icon', IconSelector(title=_('Button Icon'),)),
=======
            ('description',
             TextAreaUnicode(
                 title=_('Description') + '<sup>*</sup>',
                 rows=4,
                 cols=50,
             )),
            ('add_context_to_title',
             Checkbox(
                 title=_('Context information'),
                 label=_('Add context information to title'),
                 help=_("Whether or not additional information from the page context "
                        "(filters) should be added to the title given above."),
             )),
            ('topic', DropdownChoice(
                title=_('Topic'),
                choices=pagetypes.PagetypeTopics.choices(),
            )),
            ("sort_index",
             Integer(
                 title=_("Sort index"),
                 default_value=99,
                 help=_("You can customize the order of the %s by changing "
                        "this number. Lower numbers will be sorted first. "
                        "Topics with the same number will be sorted alphabetically.") %
                 visual_type.title,
             )),
            ("is_show_more",
             Checkbox(
                 title=_("Show more"),
                 label=_("Only show the %s if show more is active" % visual_type.title),
                 default_value=99,
                 help=_("The navigation allows to hide items based on a show "
                        "less / show more toggle. You can specify here whether or "
                        "not this %s should only be shown with show more %s.") %
                 (visual_type.title, visual_type.title),
             )),
            ('icon', IconSelector(title=_('Icon'))),
>>>>>>> upstream/master
            ('visibility', Dictionary(
                title=_('Visibility'),
                elements=visibility_elements,
            )),
        ],
    )

    context_specs = get_context_specs(visual, info_handler)

    # handle case of save or try or press on search button
    save_and_go = None
<<<<<<< HEAD
    for nr, (title, pagename, icon) in enumerate(sub_pages):
=======
    for nr, (title, pagename, _icon) in enumerate(sub_pages):
>>>>>>> upstream/master
        if html.request.var("save%d" % nr):
            save_and_go = pagename

    if save_and_go or html.request.var("save") or html.request.var("search"):
        try:
            general_properties = vs_general.from_html_vars('general')
<<<<<<< HEAD
            vs_general.validate_value(general_properties, 'general')

            if not general_properties['linktitle']:
                general_properties['linktitle'] = general_properties['title']
            if not general_properties['topic']:
                general_properties['topic'] = _("Other")

            old_visual = visual
            visual = {}
=======

            vs_general.validate_value(general_properties, 'general')

            if not general_properties['topic']:
                general_properties['topic'] = "other"

            old_visual = visual
            # TODO: Currently not editable, but keep settings
            visual = {'link_from': old_visual['link_from']}
>>>>>>> upstream/master

            # The dict of the value spec does not match exactly the dict
            # of the visual. We take over some keys...
            for key in [
                    'single_infos',
                    'name',
                    'title',
                    'topic',
<<<<<<< HEAD
                    'description',
                    'linktitle',
=======
                    'sort_index',
                    'is_show_more',
                    'description',
>>>>>>> upstream/master
                    'icon',
                    'add_context_to_title',
            ]:
                visual[key] = general_properties[key]

            # ...and import the visibility flags directly into the visual
            for key, _value in visibility_elements:
                visual[key] = general_properties['visibility'].get(key, False)

            if not config.user.may("general.publish_" + what):
                visual['public'] = False

            if create_handler:
                visual = create_handler(old_visual, visual)

            visual['context'] = process_context_specs(context_specs)

            if html.request.var("save") or save_and_go:
                if save_and_go:
<<<<<<< HEAD
                    back_url = html.makeuri_contextless([(visual_type.ident_attr, visual['name'])],
                                                        filename=save_and_go + '.py')
=======
                    back_url = makeuri_contextless(
                        global_request,
                        [(visual_type.ident_attr, visual['name'])],
                        filename=save_and_go + '.py',
                    )
>>>>>>> upstream/master

                if html.check_transaction():
                    all_visuals[(owner_user_id, visual["name"])] = visual
                    # Handle renaming of visuals
                    if oldname and oldname != visual["name"]:
                        # -> delete old entry
                        if (owner_user_id, oldname) in all_visuals:
                            del all_visuals[(owner_user_id, oldname)]
                        # -> change visual_name in back parameter
                        if back_url:
                            varstring = visual_type.ident_attr + "="
                            back_url = back_url.replace(varstring + oldname,
                                                        varstring + visual["name"])
                    save(what, all_visuals, owner_user_id)

                html.immediate_browser_redirect(1, back_url)
<<<<<<< HEAD
                html.message(_('Your %s has been saved.') % visual_type.title)
=======
                html.show_message(_('Your %s has been saved.') % visual_type.title)
>>>>>>> upstream/master
                html.reload_sidebar()
                html.footer()
                return

        except MKUserError as e:
            html.user_error(e)

    html.begin_form("visual", method="POST")
    html.hidden_field("back", back_url)
    html.hidden_field("mode", mode)
    if html.request.has_var("load_user"):
        html.hidden_field("load_user",
                          html.request.var("load_user"))  # safe old name in case user changes it
    html.hidden_field("load_name", oldname)  # safe old name in case user changes it

    # FIXME: Hier werden die Flags aus visibility nicht korrekt geladen. Wäre es nicht besser,
    # diese in einem Unter-Dict zu lassen, anstatt diese extra umzukopieren?
    visib = {}
    for key, _vs in visibility_elements:
        if visual.get(key):
            visib[key] = visual[key]
    visual["visibility"] = visib

    vs_general.render_input("general", visual)

    if custom_field_handler:
        custom_field_handler(visual)

    render_context_specs(visual, context_specs)

    forms.end()
    html.show_localization_hint()

<<<<<<< HEAD
    html.button("save", _("Save"))

    for nr, (title, pagename, icon) in enumerate(sub_pages):
        html.button("save%d" % nr, _("Save and go to ") + title)

=======
>>>>>>> upstream/master
    html.hidden_fields()
    html.end_form()
    html.footer()


#.
#   .--Filters-------------------------------------------------------------.
#   |                     _____ _ _ _                                      |
#   |                    |  ___(_) | |_ ___ _ __ ___                       |
#   |                    | |_  | | | __/ _ \ '__/ __|                      |
#   |                    |  _| | | | ||  __/ |  \__ \                      |
#   |                    |_|   |_|_|\__\___|_|  |___/                      |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def show_filter(f):
    html.open_div(class_=["floatfilter", "double" if f.double_height() else "single", f.ident])
    html.div(f.title, class_="legend")
=======
def show_filter(f: Filter) -> None:
    html.open_div(class_=["floatfilter", f.ident])
    html.open_div(class_="legend")
    html.span(f.title)
    html.close_div()
>>>>>>> upstream/master
    html.open_div(class_="content")
    try:
        with html.plugged():
            f.display()
            html.write(html.drain())
    except Exception as e:
        logger.exception("error showing filter")
        tb = sys.exc_info()[2]
        tbs = ['Traceback (most recent call last):\n']
        tbs += traceback.format_tb(tb)
<<<<<<< HEAD
        html.icon(_("This filter cannot be displayed") + " (%s)\n%s" % (e, "".join(tbs)), "alert")
=======
        html.icon("alert", _("This filter cannot be displayed") + " (%s)\n%s" % (e, "".join(tbs)))
>>>>>>> upstream/master
        html.write_text(_("This filter cannot be displayed"))
    html.close_div()
    html.close_div()


<<<<<<< HEAD
def get_filter(name):
    # type: (str) -> Type[Filter]
    """Returns the filter object identified by the given name
    Raises a KeyError in case a not existing filter is requested."""
    return filter_registry[name]()


def filters_allowed_for_info(info):
    # type: (str) -> Dict[str, Type[Filter]]
    """Returns a map of filter names and filter objects that are registered for the given info"""
    allowed = {}
    for fname, filter_class in filter_registry.items():
        filt = filter_class()
=======
def get_filter(name: str) -> Filter:
    """Returns the filter object identified by the given name
    Raises a KeyError in case a not existing filter is requested."""
    return filter_registry[name]


def filters_allowed_for_info(info: str) -> Dict[str, Filter]:
    """Returns a map of filter names and filter objects that are registered for the given info"""
    allowed = {}
    for fname, filt in filter_registry.items():
>>>>>>> upstream/master
        if filt.info is None or info == filt.info:
            allowed[fname] = filt
    return allowed


<<<<<<< HEAD
def filters_allowed_for_infos(info_list):
    # type: (List[str]) -> Dict[str, Type[Filter]]
=======
def filters_allowed_for_infos(info_list: List[str]) -> Dict[str, Filter]:
>>>>>>> upstream/master
    """Same as filters_allowed_for_info() but for multiple infos"""
    filters = {}
    for info in info_list:
        filters.update(filters_allowed_for_info(info))
    return filters


# For all single_infos which are configured for a view which datasource
# does not provide these infos, try to match the keys of the single_info
# attributes to a filter which can then be used to filter the data of
# the available infos.
# This is needed to make the "hostgroup" single_info possible on datasources
# which do not have the "hostgroup" info, but the "host" info. This
# is some kind of filter translation between a filter of the "hostgroup" info
# and the "hosts" info.
<<<<<<< HEAD
def get_link_filter_names(visual, info_keys, link_filters):
    names = []
=======
def get_link_filter_names(
        visual: Visual, info_keys: List[InfoName],
        link_filters: Dict[FilterName, FilterName]) -> List[Tuple[FilterName, FilterName]]:
    names: List[Tuple[FilterName, FilterName]] = []
>>>>>>> upstream/master
    for info_key in visual['single_infos']:
        if info_key not in info_keys:
            for key in info_params(info_key):
                if key in link_filters:
                    names.append((key, link_filters[key]))
    return names


<<<<<<< HEAD
# Collects all filters to be used for the given visual
def filters_of_visual(visual, info_keys, link_filters=None):
    if link_filters is None:
        link_filters = []

    filters = {}
=======
def filters_of_visual(visual: Visual,
                      info_keys: List[InfoName],
                      link_filters: Optional[Dict[FilterName, FilterName]] = None) -> List[Filter]:
    """Collects all filters to be used for the given visual"""
    if link_filters is None:
        link_filters = {}

    filters: Dict[FilterName, Filter] = {}
>>>>>>> upstream/master

    for info_key in info_keys:
        if info_key in visual['single_infos']:
            for key in info_params(info_key):
                filters[key] = get_filter(key)
            continue

        for key, val in visual['context'].items():
            if isinstance(val, dict):  # this is a real filter
                try:
                    filters[key] = get_filter(key)
                except KeyError:
                    pass  # Silently ignore not existing filters

    # See get_link_filter_names() comment for details
    for key, dst_key in get_link_filter_names(visual, info_keys, link_filters):
        filters[dst_key] = get_filter(dst_key)

    # add ubiquitary_filters that are possible for these infos
    for fn in get_ubiquitary_filters():
        # Disable 'wato_folder' filter, if WATO is disabled or there is a single host view
        filter_ = get_filter(fn)

        if fn == "wato_folder" and (not filter_.available() or 'host' in visual['single_infos']):
            continue
        if not filter_.info or filter_.info in info_keys:
            filters[fn] = filter_

<<<<<<< HEAD
    return filters.values()


# TODO: Cleanup this special case
def get_ubiquitary_filters():
=======
    return list(filters.values())


# TODO: Cleanup this special case
def get_ubiquitary_filters() -> List[FilterName]:
>>>>>>> upstream/master
    return ["wato_folder"]


# Reduces the list of the visuals used filters. The result are the ones
# which are really presented to the user later.
# For the moment we only remove the single context filters which have a
# hard coded default value which is treated as enforced value.
<<<<<<< HEAD
def visible_filters_of_visual(visual, use_filters):
    show_filters = []

    single_keys = get_single_info_keys(visual)
=======
def visible_filters_of_visual(visual: Visual, use_filters: List[Filter]) -> List[Filter]:
    show_filters = []

    single_keys = get_single_info_keys(visual["single_infos"])
>>>>>>> upstream/master

    for f in use_filters:
        if f.ident not in single_keys or \
           not visual['context'].get(f.ident):
            show_filters.append(f)

    return show_filters


<<<<<<< HEAD
def add_context_to_uri_vars(visual, only_count=False):
    # Populate the HTML vars with missing context vars. The context vars set
    # in single context are enforced (can not be overwritten by URL). The normal
    # filter vars in "multiple" context are not enforced.
    for key in get_single_info_keys(visual):
        if key in visual['context']:
            html.request.set_var(key, "%s" % visual['context'][key])

    # Now apply the multiple context filters
    for filter_vars in visual['context'].itervalues():
        if isinstance(filter_vars, dict):  # this is a multi-context filter
            # We add the filter only if *none* of its HTML variables are present on the URL
            # This important because checkbox variables are not present if the box is not checked.
            skip = any(html.request.has_var(uri_varname) for uri_varname in filter_vars.iterkeys())
            if not skip or only_count:
                for uri_varname, value in filter_vars.items():
                    html.request.set_var(uri_varname, "%s" % value)
=======
def add_context_to_uri_vars(context: VisualContext, single_infos: SingleInfos) -> None:
    """Populate the HTML vars with missing context vars

    The context vars set in single context are enforced (can not be overwritten by URL). The normal
    filter vars in "multiple" context are not enforced."""
    uri_vars = dict(get_context_uri_vars(context, single_infos))
    single_info_keys = get_single_info_keys(single_infos)

    for filter_name, filter_vars in context.items():
        # Enforce the single context variables that are available in the visual context
        if filter_name in single_info_keys:
            html.request.set_var(filter_name, "%s" % uri_vars[filter_name])
            continue

        if not isinstance(filter_vars, dict):
            continue  # Skip invalid filter values

        # This is a multi-context filter
        # We add the filter only if *none* of its HTML variables are present on the URL. This is
        # important because checkbox variables are not present if the box is not checked.
        if any(html.request.has_var(uri_varname) for uri_varname in filter_vars):
            continue

        for uri_varname in filter_vars.keys():
            html.request.set_var(uri_varname, "%s" % uri_vars[uri_varname])


def get_context_uri_vars(context: VisualContext, single_infos: SingleInfos) -> HTTPVariables:
    """Produce key/value tuples for HTTP variables from the visual context"""
    uri_vars: HTTPVariables = []
    single_info_keys = get_single_info_keys(single_infos)

    for filter_name, filter_vars in context.items():
        # Enforce the single context variables that are available in the visual context
        if filter_name in single_info_keys:
            uri_vars.append((filter_name, "%s" % context[filter_name]))

        if not isinstance(filter_vars, dict):
            continue  # Skip invalid filter values

        # This is a multi-context filter
        for uri_varname, value in filter_vars.items():
            uri_vars.append((uri_varname, "%s" % value))

    return uri_vars


@contextmanager
def context_uri_vars(context: VisualContext, single_infos: SingleInfos) -> Iterator[None]:
    """Updates the current HTTP variable context"""
    with html.stashed_vars():
        add_context_to_uri_vars(context, single_infos)
        yield
>>>>>>> upstream/master


# Vice versa: find all filters that belong to the current URI variables
# and create a context dictionary from that.
<<<<<<< HEAD
def get_context_from_uri_vars(only_infos=None, single_infos=None):
    if single_infos is None:
        single_infos = []

    context = {}
    for filter_name, filter_class in filter_registry.items():
        filter_object = filter_class()
        if only_infos is None or filter_object.info in only_infos:
            this_filter_vars = {}
            for varname in filter_object.htmlvars:
                if html.request.has_var(varname):
                    if filter_object.info in single_infos:
                        context[filter_name] = html.request.var(varname)
                        break
                    else:
                        this_filter_vars[varname] = html.request.var(varname)
            if this_filter_vars:
                context[filter_name] = this_filter_vars
    return context


# Compute Livestatus-Filters based on a given context. Returns
# the only_sites list and a string with the filter headers
# TODO: Untangle only_sites and filter headers
def get_filter_headers(table, infos, context):
    # Prepare Filter headers for Livestatus
    filter_headers = ""
=======
def get_context_from_uri_vars(only_infos: Optional[List[InfoName]] = None,
                              single_infos: Optional[SingleInfos] = None) -> VisualContext:
    if single_infos is None:
        single_infos = []

    single_info_keys = set(get_single_info_keys(single_infos))

    context: VisualContext = {}
    for filter_name, filter_object in filter_registry.items():
        if only_infos is not None and filter_object.info not in only_infos:
            continue  # Skip filters related to not relevant infos

        this_filter_vars: FilterHTTPVariables = {}
        for varname in filter_object.htmlvars:
            if not html.request.has_var(varname):
                continue  # Variable to set in environment

            filter_value = html.request.get_str_input_mandatory(varname)
            if not filter_value:
                continue

            if varname in single_info_keys:
                context[filter_name] = filter_value
                break

            this_filter_vars[varname] = filter_value

        if this_filter_vars:
            context[filter_name] = this_filter_vars

    return context


def get_merged_context(*contexts: VisualContext) -> VisualContext:
    """Merges multiple filter contexts to a single one

    The last context that sets a filter wins. The intended order is to provide contexts in
    "descending order", e.g. like this for dashboards:

    1. URL context
    2. Dashboard context
    3. Dashlet context
    """
    merged_context = {}
    for c in contexts:
        merged_context.update(c)
    return merged_context


# Compute Livestatus-Filters based on a given context. Returns
# the only_sites list and a string with the filter headers
# TODO: Untangle only_sites and filter headers
# TODO: Reduce redundancies with filters_of_visual()
def get_filter_headers(table, infos, context):
>>>>>>> upstream/master
    with html.stashed_vars():
        for filter_name, filter_vars in context.items():
            # first set the HTML variables. Sorry - the filters need this
            if isinstance(filter_vars, dict):  # this is a multi-context filter
                for uri_varname, value in filter_vars.items():
                    html.request.set_var(uri_varname, value)
            else:
                html.request.set_var(filter_name, filter_vars)

<<<<<<< HEAD
        # Apply the site hint / filter (Same logic as in views.py)
        if html.request.var("site"):
            only_sites = [html.request.var("site")]
        else:
            only_sites = None

        # Now compute filter headers for all infos of the used datasource
        for filter_name, filter_class in filter_registry.items():
            filter_object = filter_class()
            if filter_object.info in infos:
                header = filter_object.filter(table)
                filter_headers += header
    return filter_headers, only_sites
=======
        filter_headers = "".join(collect_filter_headers(infos, table))
    return filter_headers, get_only_sites_from_context(context)


def get_only_sites_from_context(context: dict) -> Optional[List[SiteId]]:
    """Gather possible existing "only sites" information from context

      We need to deal with

      a) all possible site filters (sites, site and siteopt).
      b) with single and multiple contexts

      Single contexts are structured like this:

      {"site": "sitename"}
      {"sites": "sitename|second"}

      Multiple contexts are structured like this:

      {"site": {"site": "sitename"}}
      {"sites": {"sites": "sitename|second"}}

      The difference is no fault or "old" data structure. We can have both kind of structures.
      These are the data structure the visuals work with.

      "site" and "sites" are conflicting filters. The new optional filter
      "sites" for many sites filter is only used if the view is configured
      to only this filter.
      """

    if "sites" in context and "site" not in context:
        only_sites = context["sites"]
        if isinstance(only_sites, dict):
            only_sites = only_sites["sites"]
        only_sites = [SiteId(site) for site in only_sites.strip().split("|") if site]
        return only_sites if only_sites else None

    for var in ["site", "siteopt"]:
        if var in context:
            if isinstance(context[var], dict):
                site_name = context[var].get("site")
                if site_name:
                    return [SiteId(site_name)]
                return None
            return [SiteId(context[var])]

    return None


def collect_filter_headers(info_keys, table):
    # Collect all available filters for these infos
    for filter_obj in filter_registry.values():
        if filter_obj.info in info_keys and filter_obj.available():
            yield filter_obj.filter(table)
>>>>>>> upstream/master


#.
#   .--ValueSpecs----------------------------------------------------------.
#   |        __     __    _            ____                                |
#   |        \ \   / /_ _| |_   _  ___/ ___| _ __   ___  ___ ___           |
#   |         \ \ / / _` | | | | |/ _ \___ \| '_ \ / _ \/ __/ __|          |
#   |          \ V / (_| | | |_| |  __/___) | |_) |  __/ (__\__ \          |
#   |           \_/ \__,_|_|\__,_|\___|____/| .__/ \___|\___|___/          |
#   |                                       |_|                            |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
=======
def FilterChoices(infos: List[InfoName], title: str, help: str):  # pylint: disable=redefined-builtin
    """Select names of filters for the given infos"""
    return DualListChoice(
        choices=[(x[0], x[1].title()) for x in VisualFilterList.get_choices(infos, ignore=set())],
        title=title,
        help=help,
    )


>>>>>>> upstream/master
class VisualFilterList(ListOfMultiple):
    """Implements a list of available filters for the given infos. By default no
    filter is selected. The user may select a filter to be activated, then the
    filter is rendered and the user can provide a default value.
    """
    @classmethod
<<<<<<< HEAD
    def get_choices(cls, infos, ignore):
        return sorted(cls._get_filter_specs(infos, ignore).items(),
=======
    def get_choices(cls, info, ignore):
        return sorted(cls._get_filter_specs([info], ignore).items(),
>>>>>>> upstream/master
                      key=lambda x: (x[1]._filter.sort_index, x[1].title()))

    @classmethod
    def _get_filters(cls, infos, ignore):
        return {
<<<<<<< HEAD
            fname: fspec._filter
            for fname, fspec in cls._get_filter_specs(infos, ignore).iteritems()
=======
            fname: fspec._filter for fname, fspec in cls._get_filter_specs(infos, ignore).items()
>>>>>>> upstream/master
        }

    @classmethod
    def _get_filter_specs(cls, infos, ignore):
<<<<<<< HEAD
        fspecs = {}
        for info in infos:
            for fname, filter_ in filters_allowed_for_info(info).items():
                if fname not in fspecs and fname not in ignore:
                    fspecs[fname] = VisualFilter(
                        fname,
                        title=filter_.title,
                    )
        return fspecs

    def __init__(self, info_list, **kwargs):
        ignore = kwargs.pop("ignore", set())
=======
        fspecs: Dict[str, VisualFilter] = {}
        for info in infos:
            for fname, filter_ in filters_allowed_for_info(info).items():
                if fname not in fspecs and fname not in ignore:
                    fspecs[fname] = VisualFilter(fname, title=filter_.title)
        return fspecs

    def __init__(self, info_list, **kwargs):
        ignore: Set[str] = kwargs.pop("ignore", set())
>>>>>>> upstream/master
        self._filters = self._get_filters(info_list, ignore)

        kwargs.setdefault('title', _('Filters'))
        kwargs.setdefault('add_label', _('Add filter'))
        kwargs.setdefault('del_label', _('Remove filter'))
        kwargs["delete_style"] = "filter"

<<<<<<< HEAD
        super(VisualFilterList, self).__init__(self.get_choices(info_list, ignore),
=======
        grouped: GroupedListOfMultipleChoices = [
            ListOfMultipleChoiceGroup(title=visual_info_registry[info]().title,
                                      choices=self.get_choices(info, ignore)) for info in info_list
        ]
        super(VisualFilterList, self).__init__(grouped,
>>>>>>> upstream/master
                                               "ajax_visual_filter_list_get_choice",
                                               page_request_vars={
                                                   "infos": info_list,
                                                   "ignore": list(ignore),
                                               },
                                               **kwargs)

    def filter_names(self):
        return self._filters.keys()


<<<<<<< HEAD
@page_registry.register_page("ajax_visual_filter_list_get_choice")
class PageAjaxVisualFilterListGetChoice(ABCPageListOfMultipleGetChoice):
    def _get_choices(self, request):
        return VisualFilterList.get_choices(request["infos"], set(request["ignore"]))
=======
class VisualFilterListWithAddPopup(VisualFilterList):
    """Special form of the visual filter list to be used in the views and dashboards"""
    @staticmethod
    def filter_list_id(varprefix: str) -> str:
        return "%s_popup_filter_list" % varprefix

    def _show_add_elements(self, varprefix: str) -> None:
        filter_list_id = VisualFilterListWithAddPopup.filter_list_id(varprefix)
        filter_list_selected_id = filter_list_id + "_selected"

        html.open_div(id_=filter_list_id, class_="popup_filter_list")
        html.more_button(filter_list_id, 1)
        for group in self._grouped_choices:
            if not group.choices:
                continue

            group_id = "filter_group_" + "".join(group.title.split()).lower()

            html.open_div(id_=group_id, class_="filter_group")
            # Show / hide all entries of this group
            html.a(group.title,
                   href="",
                   class_="filter_group_title",
                   onclick="cmk.page_menu.toggle_filter_group_display(this.nextSibling)")

            # Display all entries of this group
            html.open_ul(class_="active")
            for choice in group.choices:
                filter_name = choice[0]

                filter_obj = filter_registry[filter_name]
                html.open_li(class_="show_more_mode" if filter_obj.is_show_more else "basic")

                html.a(choice[1].title() or filter_name,
                       href="javascript:void(0)",
                       onclick="cmk.valuespecs.listofmultiple_add(%s, %s, %s, this);"
                       "cmk.page_menu.update_filter_list_scroll(%s)" %
                       (json.dumps(varprefix), json.dumps(self._choice_page_name),
                        json.dumps(self._page_request_vars), json.dumps(filter_list_selected_id)),
                       id_="%s_add_%s" % (varprefix, filter_name))

                html.close_li()
            html.close_ul()

            html.close_div()
        html.close_div()
        filters_applied = html.request.get_ascii_input("filled_in") == "filter"
        html.javascript('cmk.valuespecs.listofmultiple_init(%s, %s);' %
                        (json.dumps(varprefix), json.dumps(filters_applied)))
        html.javascript("cmk.utils.add_simplebar_scrollbar(%s);" % json.dumps(filter_list_id))


@page_registry.register_page("ajax_visual_filter_list_get_choice")
class PageAjaxVisualFilterListGetChoice(ABCPageListOfMultipleGetChoice):
    def _get_choices(self, request):
        infos, ignore = request["infos"], request["ignore"]
        return [
            ListOfMultipleChoiceGroup(title=visual_info_registry[info]().title,
                                      choices=VisualFilterList.get_choices(info, ignore))
            for info in infos
        ]


def render_filter_form(info_list: List[InfoName], mandatory_filters: List[Tuple[str, ValueSpec]],
                       context: VisualContext, page_name: str, reset_ajax_page: str) -> str:
    with html.plugged():
        show_filter_form(info_list, mandatory_filters, context, page_name, reset_ajax_page)
        return html.drain()


def show_filter_form(info_list: List[InfoName], mandatory_filters: List[Tuple[str, ValueSpec]],
                     context: VisualContext, page_name: str, reset_ajax_page: str) -> None:
    html.show_user_errors()
    html.begin_form("filter", method="GET", add_transid=False)
    varprefix = ""
    mandatory_filter_names = [f[0] for f in mandatory_filters]
    vs_filters = VisualFilterListWithAddPopup(info_list=info_list, ignore=mandatory_filter_names)

    filter_list_id = VisualFilterListWithAddPopup.filter_list_id(varprefix)
    filter_list_selected_id = filter_list_id + "_selected"
    _show_filter_form_buttons(varprefix, filter_list_id, vs_filters._page_request_vars, page_name,
                              reset_ajax_page)

    html.open_div(id_=filter_list_selected_id, class_="side_popup_content")
    try:
        # Configure required single info keys (the ones that are not set by the config)
        if mandatory_filters:
            html.h2(_("Mandatory context"))
            for filter_name, valuespec in mandatory_filters:
                html.h3(valuespec.title())
                valuespec.render_input(filter_name, None)

        # Give the user the option to redefine filters configured in the dashboard config
        # and also give the option to add some additional filters
        if mandatory_filters:
            html.h3(_("Additional context"))

        vs_filters.render_input(varprefix, context)
    except Exception:
        # TODO: Analyse possible cycle
        import cmk.gui.crash_reporting as crash_reporting
        crash_reporting.handle_exception_as_gui_crash_report()
    html.close_div()

    forms.end()

    html.hidden_fields()
    html.end_form()
    html.javascript("cmk.utils.add_simplebar_scrollbar(%s);" % json.dumps(filter_list_selected_id))

    # The filter popup is shown automatically when it has been submitted before on page reload. To
    # know that the user closed the popup after filtering, we have to hook into the close_popup
    # function.
    html.final_javascript(
        "cmk.page_menu.register_on_open_handler('popup_filters', cmk.page_menu.on_filter_popup_open);"
        "cmk.page_menu.register_on_close_handler('popup_filters', cmk.page_menu.on_filter_popup_close);"
    )


def _show_filter_form_buttons(varprefix: str, filter_list_id: str,
                              page_request_vars: Optional[Dict[str, Any]], view_name: str,
                              reset_ajax_page: str) -> None:
    html.open_div(class_="side_popup_controls")

    html.open_a(href="javascript:void(0);",
                onclick="cmk.page_menu.toggle_popup_filter_list(this, %s)" %
                json.dumps(filter_list_id),
                class_="add")
    html.icon("add")
    html.div(html.render_text("Add filter"), class_="description")
    html.close_a()

    html.open_div(class_="update_buttons")
    html.jsbutton("%s_reset" % varprefix,
                  _("Reset"),
                  cssclass="reset",
                  onclick="cmk.valuespecs.visual_filter_list_reset(%s, %s, %s, %s)" %
                  (json.dumps(varprefix), json.dumps(page_request_vars), json.dumps(view_name),
                   json.dumps(reset_ajax_page)))
    html.button("%s_apply" % varprefix, _("Apply filters"), cssclass="apply hot")
    html.close_div()
    html.close_div()
>>>>>>> upstream/master


# Realizes a Multisite/visual filter in a valuespec. It can render the filter form, get
# the filled in values and provide the filled in information for persistance.
class VisualFilter(ValueSpec):
    def __init__(self, name, **kwargs):
        self._name = name
<<<<<<< HEAD
        self._filter = filter_registry[name]()
=======
        self._filter = filter_registry[name]
>>>>>>> upstream/master

        ValueSpec.__init__(self, **kwargs)

    def title(self):
        return self._filter.title

    def canonical_value(self):
        return {}

    def render_input(self, varprefix, value):
        # kind of a hack to make the current/old filter API work. This should
        # be cleaned up some day
        if value is not None:
<<<<<<< HEAD
            self._filter.set_value(value)
=======
            self.set_value(value)
>>>>>>> upstream/master

        # A filter can not be used twice on a page, because the varprefix is not used
        show_filter(self._filter)

    def value_to_text(self, value):
        # FIXME: optimize. Needed?
        return repr(value)

    def from_html_vars(self, varprefix):
        # A filter can not be used twice on a page, because the varprefix is not used
        return self._filter.value()

    def validate_datatype(self, value, varprefix):
        if not isinstance(value, dict):
            raise MKUserError(varprefix,
                              _("The value must be of type dict, but it has type %s") % type(value))

<<<<<<< HEAD

def SingleInfoSelection(info_keys, **args):
    info_choices = []
    for key in info_keys:
        info_choices.append(
            (key, _('Show information of a single %s') % visual_info_registry[key]().title))

    args.setdefault("title", _('Specific objects'))
    args["choices"] = info_choices
    return ListChoice(**args)
=======
    def validate_value(self, value, varprefix):
        self._filter.validate_value(value)

    def set_value(self, value):
        """Is used to populate a value, for example loaded from persistance, into
        the HTML context where it can be used by e.g. the display() method."""
        if isinstance(value, str):
            html.request.set_var(self._filter.htmlvars[0], value)
            return

        for varname in self._filter.htmlvars:
            var_value = value.get(varname)
            if var_value is not None:
                html.request.set_var(varname, var_value)


def SingleInfoSelection(info_keys: List[InfoName]) -> DualListChoice:
    infos = [visual_info_registry[key]() for key in info_keys]
    choices = [(i.ident, _('Show information of a single %s') % i.title)
               for i in sorted(infos, key=lambda inf: (inf.sort_index, inf.title))]

    return DualListChoice(
        title=_('Specific objects'),
        choices=choices,
        rows=10,
    )
>>>>>>> upstream/master


# Converts a context from the form { filtername : { ... } } into
# the for { infoname : { filtername : { } } for editing.
<<<<<<< HEAD
def pack_context_for_editing(visual, info_handler):
=======
def pack_context_for_editing(visual: Visual,
                             info_handler: Optional[Callable[[Visual], List[InfoName]]]) -> Dict:
>>>>>>> upstream/master
    # We need to pack all variables into dicts with the name of the
    # info. Since we have no mapping from info the the filter variable,
    # we pack into every info every filter. The dict valuespec will
    # pick out what it needs. Yurks.
    packed_context = {}
    info_keys = info_handler(visual) if info_handler else visual_info_registry.keys()
    for info_name in info_keys:
        packed_context[info_name] = visual.get('context', {})
    return packed_context


<<<<<<< HEAD
def unpack_context_after_editing(packed_context):
    context = {}
=======
def unpack_context_after_editing(packed_context: Dict) -> VisualContext:
    context: VisualContext = {}
>>>>>>> upstream/master
    for _info_type, its_context in packed_context.items():
        context.update(its_context)
    return context


#.
#   .--Misc----------------------------------------------------------------.
#   |                          __  __ _                                    |
#   |                         |  \/  (_)___  ___                           |
#   |                         | |\/| | / __|/ __|                          |
#   |                         | |  | | \__ \ (__                           |
#   |                         |_|  |_|_|___/\___|                          |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def is_single_site_info(info_key):
    return visual_info_registry[info_key]().single_site


def single_infos_spec(single_infos):
    return ('single_infos', FixedValue(single_infos,
        title = _('Show information of single'),
        totext = single_infos and ', '.join(single_infos) \
                    or _('Not restricted to showing a specific object.'),
    ))


def verify_single_contexts(what, visual, link_filters):
    for k, v in get_singlecontext_html_vars(visual).items():
        if v is None and k not in link_filters:
            raise MKUserError(
                k,
                _('This %s can not be displayed, because the '
                  'necessary context information "%s" is missing.') %
                (visual_type_registry[what]().title, k))


def visual_title(what, visual):
=======
def visual_page_breadcrumb(what: str, title: str, page_name: str) -> Breadcrumb:
    breadcrumb = make_main_menu_breadcrumb(mega_menu_registry.menu_customize())

    list_title = visual_type_registry[what]().plural_title
    breadcrumb.append(BreadcrumbItem(title=list_title.title(), url="edit_%s.py" % what))

    if page_name == "list":  # The list is the parent of all others
        return breadcrumb

    breadcrumb.append(BreadcrumbItem(title=title, url=makeuri(global_request, [])))
    return breadcrumb


def is_single_site_info(info_key: InfoName) -> bool:
    return visual_info_registry[info_key]().single_site


def single_infos_spec(single_infos: SingleInfos) -> Tuple[str, FixedValue]:
    return ('single_infos',
            FixedValue(
                single_infos,
                title=_('Show information of single'),
                totext=single_infos and ', '.join(single_infos) or
                _('Not restricted to showing a specific object.'),
            ))


def verify_single_infos(visual: Visual, context: VisualContext) -> None:
    """Check if all single infos from the element are known"""

    missing_single_infos = get_missing_single_infos(visual["single_infos"], context)

    # Special hack for the situation where hostgroup views link to host views: The host view uses
    # the datasource "hosts" which does not have the "hostgroup" info, but is configured to have a
    # single_info "hostgroup". To make this possible there exists a feature in
    # (ABCDataSource.link_filters, views._patch_view_context) which is a very specific hack. Have a
    # look at the description there.  We workaround the issue here by allowing this specific
    # situation but validating all others.
    #
    # The more correct approach would be to find a way which allows filters of different datasources
    # to have equal names. But this would need a bigger refactoring of the filter mechanic. One
    # day...
    if (visual.get("datasource") in ["hosts", "services"] and
            missing_single_infos == {'hostgroup'} and "opthostgroup" in context):
        return
    if (visual.get("datasource") == "services" and missing_single_infos == {"servicegroup"} and
            "optservicegroup" in context):
        return

    if missing_single_infos:
        raise MKUserError(
            None,
            _("Missing context information: %s. You can either add this as a fixed "
              "setting, or call the with the missing HTTP variables.") %
            (", ".join(missing_single_infos)))


def get_missing_single_infos(single_infos: SingleInfos, context: VisualContext) -> Set[FilterName]:
    single_info_keys = get_single_info_keys(single_infos)
    return set(single_info_keys).difference(context)


def visual_title(what: VisualTypeName, visual: Visual) -> str:
>>>>>>> upstream/master
    title = _u(visual["title"])

    if visual["add_context_to_title"]:
        title = _add_context_title(visual, title)

    # Execute title plugin functions which might be added by the user to
    # the visuals plugins. When such a plugin function returns None, the regular
    # title of the page is used, otherwise the title returned by the plugin
    # function is used.
    for func in title_functions:
        result = func(what, visual, title)
        if result is not None:
            return result

    return title


<<<<<<< HEAD
def _add_context_title(visual, title):
    # Beware: if a single context visual is being visited *without* a context, then
    # the value of the context variable(s) is None. In order to avoid exceptions,
    # we simply drop these here.
    extra_titles = [v for v in get_singlecontext_html_vars(visual).itervalues() if v is not None]
=======
def _add_context_title(visual: Visual, title: str) -> str:
    extra_titles = list(
        get_singlecontext_html_vars(visual["context"], visual["single_infos"]).values())
>>>>>>> upstream/master

    # FIXME: Is this really only needed for visuals without single infos?
    if not visual['single_infos']:
        used_filters = []
        for fn in visual["context"].keys():
            try:
                used_filters.append(get_filter(fn))
            except KeyError:
                pass  # silently ignore not existing filters

        for filt in used_filters:
            heading = filt.heading_info()
            if heading:
                extra_titles.append(heading)

    if extra_titles:
        title += " " + ", ".join(extra_titles)

    for fn in get_ubiquitary_filters():
        # Disable 'wato_folder' filter, if WATO is disabled or there is a single host view
        if fn == "wato_folder" and (not config.wato_enabled or 'host' in visual['single_infos']):
            continue

        heading = get_filter(fn).heading_info()
        if heading:
            title = heading + " - " + title

    return title


# Determines the names of HTML variables to be set in order to
# specify a specify row in a datasource with a certain info.
# Example: the info "history" (Event Console History) needs
# the variables "event_id" and "history_line" to be set in order
# to exactly specify one history entry.
<<<<<<< HEAD
def info_params(info_key):
    single_spec = visual_info_registry[info_key]().single_spec
    if single_spec is None:
        return []
    return dict(single_spec).keys()


def get_single_info_keys(visual):
    keys = []
    for info_key in visual.get('single_infos', []):
        keys += info_params(info_key)
    return list(set(keys))


def get_singlecontext_vars(visual):
    vars_ = {}
    for key in get_single_info_keys(visual):
        vars_[key] = visual['context'].get(key)
    return vars_


def get_singlecontext_html_vars(visual):
    vars_ = get_singlecontext_vars(visual)
    for key in get_single_info_keys(visual):
        val = html.get_unicode_input(key)
=======
def info_params(info_key: InfoName) -> List[FilterName]:
    single_spec = visual_info_registry[info_key]().single_spec
    if single_spec is None:
        return []
    return list(dict(single_spec).keys())


def get_single_info_keys(single_infos: SingleInfos) -> List[FilterName]:
    keys: List[FilterName] = []
    for info_key in single_infos:
        keys.extend(info_params(info_key))
    return list(set(keys))


def get_singlecontext_vars(context: VisualContext, single_infos: SingleInfos) -> Dict[str, str]:
    return {
        key: val  #
        for key in get_single_info_keys(single_infos)
        for val in [context.get(key)]
        if isinstance(val, str)
    }


def get_singlecontext_html_vars(context: VisualContext,
                                single_infos: SingleInfos) -> Dict[str, str]:
    vars_ = get_singlecontext_vars(context, single_infos)
    for key in get_single_info_keys(single_infos):
        val = html.request.get_unicode_input(key)
>>>>>>> upstream/master
        if val is not None:
            vars_[key] = val
    return vars_


<<<<<<< HEAD
# Collect all visuals that share a context with visual. For example
# if a visual has a host context, get all relevant visuals.
def collect_context_links(this_visual, mobile=False, only_types=None):
    if only_types is None:
        only_types = []

    # compute list of html variables needed for this visual
    active_filter_vars = set([])
    for var in get_singlecontext_html_vars(this_visual).iterkeys():
        if html.request.has_var(var):
            active_filter_vars.add(var)

    context_links = []
    for what in visual_type_registry.keys():
        if not only_types or what in only_types:
            context_links += collect_context_links_of(what, this_visual, active_filter_vars, mobile)
    return context_links


def collect_context_links_of(visual_type_name, this_visual, active_filter_vars, mobile):
    context_links = []

    visual_type = visual_type_registry[visual_type_name]()
    visual_type.load_handler()
    available_visuals = visual_type.permitted_visuals

    # sort buttons somehow
    visuals = available_visuals.values()
    visuals.sort(key=lambda x: x.get('icon'))

    for visual in visuals:
        name = visual["name"]
        linktitle = visual.get("linktitle")
        if not linktitle:
            linktitle = visual["title"]
        if visual == this_visual:
            continue
        if visual.get("hidebutton", False):
            continue  # this visual does not want a button to be displayed

        if not mobile and visual.get('mobile') \
           or mobile and not visual.get('mobile'):
            continue

        # For dashboards and views we currently only show a link button,
        # if the target dashboard/view shares a single info with the
        # current visual.
        if not visual['single_infos'] and not visual_type.multicontext_links:
            continue  # skip non single visuals for dashboard, views

        # We can show a button only if all single contexts of the
        # target visual are known currently
        needed_vars = get_singlecontext_html_vars(visual).items()
        skip = False
        vars_values = []
        for var, val in needed_vars:
            if var not in active_filter_vars:
                skip = True  # At least one single context missing
                break
            vars_values.append((var, val))

        add_site_hint = may_add_site_hint(name,
                                          info_keys=visual_info_registry.keys(),
                                          single_info_keys=visual["single_infos"],
                                          filter_names=dict(vars_values).keys())

        if add_site_hint and html.request.var('site'):
            vars_values.append(('site', html.request.var('site')))

        # Optional feature of visuals: Make them dynamically available as links or not.
        # This has been implemented for HW/SW inventory views which are often useless when a host
        # has no such information available. For example the "Oracle Tablespaces" inventory view
        # is useless on hosts that don't host Oracle databases.
        if not skip:
            skip = not visual_type.is_enabled_for(this_visual, visual, vars_values)

        if not skip:
            # add context link to this visual. For reports we put in
            # the *complete* context, even the non-single one.
            if visual_type.multicontext_links:
                uri = html.makeuri([(visual_type.ident_attr, name)], filename=visual_type.show_url)

            # For views and dashboards currently the current filter
            # settings
            else:
                uri = html.makeuri_contextless(vars_values + [(visual_type.ident_attr, name)],
                                               filename=visual_type.show_url)
            icon = visual.get("icon")
            buttonid = "cb_" + name
            context_links.append((_u(linktitle), uri, icon, buttonid))

    return context_links


def may_add_site_hint(visual_name, info_keys, single_info_keys, filter_names):
=======
def may_add_site_hint(visual_name: str, info_keys: List[InfoName], single_info_keys: SingleInfos,
                      filter_names: List[FilterName]) -> bool:
>>>>>>> upstream/master
    """Whether or not the site hint may be set when linking to a visual with the given details"""
    # When there is one non single site info used don't add the site hint
    if [info_key for info_key in single_info_keys if not is_single_site_info(info_key)]:
        return False

    # Alternatively when the infos allow a site hint it is also needed to skip the site hint based
    # on the filters used by the target visual
    for info_key in info_keys:
        for filter_key in visual_info_registry[info_key]().multiple_site_filters:
            if filter_key in filter_names:
                return False

    # Hack for servicedesc view which is meant to show all services with the given
    # description: Don't add the site filter for this view.
    if visual_name in ["servicedesc", "servicedescpnp"]:
        return False

    return True


#.
#   .--Popup Add-----------------------------------------------------------.
#   |          ____                              _       _     _           |
#   |         |  _ \ ___  _ __  _   _ _ __      / \   __| | __| |          |
#   |         | |_) / _ \| '_ \| | | | '_ \    / _ \ / _` |/ _` |          |
#   |         |  __/ (_) | |_) | |_| | |_) |  / ___ \ (_| | (_| |          |
#   |         |_|   \___/| .__/ \__,_| .__/  /_/   \_\__,_|\__,_|          |
#   |                    |_|         |_|                                   |
#   +----------------------------------------------------------------------+
<<<<<<< HEAD
#   |  Handling of popup for adding a visual element to a dashboard, etc.  |
#   '----------------------------------------------------------------------'


# TODO: Remove this code as soon as everything is moved over to pagetypes.py
@cmk.gui.pages.register("ajax_popup_add_visual")
def ajax_popup_add():
    add_type = html.request.var("add_type")

    html.open_ul()

    pagetypes.render_addto_popup(add_type)

    for visual_type_name, visual_type_class in visual_type_registry.items():
        visual_type = visual_type_class()
        visuals = visual_type.popup_add_handler(add_type)
        if not visuals:
            continue

        html.open_li()
        html.open_span()
        html.write("%s %s:" % (_('Add to'), visual_type.title))
        html.close_span()
        html.close_li()

        for name, title in sorted(visuals, key=lambda x: x[1]):
            html.open_li()
            html.open_a(href="javascript:void(0)",
                        onclick="cmk.popup_menu.add_to_visual(\'%s\', \'%s\')" %
                        (visual_type_name, name))
            html.icon(None, visual_type_name.rstrip('s'))
            html.write(title)
            html.close_a()
            html.close_li()

    # TODO: Find a good place for this special case. This needs to be modularized.
    if add_type == "pnpgraph" and metrics.cmk_graphs_possible():
        html.open_li()
        html.open_span()
        html.write("%s:" % _("Export"))
        html.close_span()
        html.close_li()

        html.open_li()
        html.open_a(href="javascript:cmk.popup_menu.graph_export(\"graph_export\")")
        html.icon(None, "download")
        html.write(_("Export as JSON"))
        html.close_a()
        html.open_a(href="javascript:cmk.popup_menu.graph_export(\"graph_image\")")
        html.icon(None, "download")
        html.write(_("Export as PNG"))
        html.close_a()
        html.close_li()

    html.close_ul()


@cmk.gui.pages.register("ajax_add_visual")
def ajax_add_visual():
    visual_type_name = html.request.var('visual_type')  # dashboards / views / ...
    visual_type = visual_type_registry[visual_type_name]()

    visual_name = html.request.var("visual_name")  # add to this visual

    # type of the visual to add (e.g. view)
    element_type = html.request.var("type")

    create_info = json.loads(html.request.var("create_info"))
=======
#   |  Handling of adding a visual element to a dashboard, etc.            |
#   '----------------------------------------------------------------------'


@cmk.gui.pages.register("ajax_popup_add_visual")
def ajax_popup_add() -> None:
    # name is unused at the moment in this, hand over as empty name
    page_menu_dropdown = page_menu_dropdown_add_to_visual(
        add_type=html.request.get_ascii_input_mandatory("add_type"), name="")[0]

    html.open_ul()

    for topic in page_menu_dropdown.topics:
        html.open_li()
        html.open_span()
        html.write(topic.title)
        html.close_span()
        html.close_li()

        for entry in topic.entries:
            html.open_li()

            if not isinstance(entry.item, PageMenuLink):
                html.write_text("Unhandled entry type '%s': %s" % (type(entry.item), entry.name))
                continue

            html.open_a(href=entry.item.link.url,
                        onclick=entry.item.link.onclick,
                        target=entry.item.link.target)
            html.icon(entry.icon_name or "trans")
            html.write(entry.title)
            html.close_a()
            html.close_li()

    html.close_ul()


def page_menu_dropdown_add_to_visual(add_type: str, name: str) -> List[PageMenuDropdown]:
    """Create the dropdown menu for adding a visual to other visuals / pagetypes

    Please not that this data structure is not only used for rendering the dropdown
    in the page menu. There is also the case of graphs which open a popup menu to
    show these entries.
    """

    visual_topics = []

    for visual_type_class in visual_type_registry.values():
        visual_type = visual_type_class()

        entries = list(visual_type.page_menu_add_to_entries(add_type))
        if not entries:
            continue

        visual_topics.append(
            PageMenuTopic(
                title=_("Add to %s") % visual_type.title,
                entries=entries,
            ))

    if add_type == "pnpgraph" and not cmk_version.is_raw_edition():
        visual_topics.append(
            PageMenuTopic(
                title=_("Export"),
                entries=[
                    PageMenuEntry(
                        title=_("Export as JSON"),
                        icon_name="download",
                        item=make_javascript_link("cmk.popup_menu.graph_export('graph_export')"),
                    ),
                    PageMenuEntry(
                        title=_("Export as PNG"),
                        icon_name="download",
                        item=make_javascript_link("cmk.popup_menu.graph_export('graph_image')"),
                    ),
                ],
            ))

    return [
        PageMenuDropdown(
            name="add_to",
            title=_("Add to"),
            topics=pagetypes.page_menu_add_to_topics(add_type) + visual_topics,
            popup_data=[add_type,
                        _encode_page_context(html.page_context), {
                            "name": name,
                        }],
        )
    ]


def _encode_page_context(page_context: VisualContext) -> VisualContext:
    return {k: "" if v is None else v for k, v in page_context.items()}


@cmk.gui.pages.register("ajax_add_visual")
def ajax_add_visual() -> None:
    visual_type_name = html.request.get_str_input_mandatory(
        'visual_type')  # dashboards / views / ...
    visual_type = visual_type_registry[visual_type_name]()

    visual_name = html.request.get_str_input_mandatory("visual_name")  # add to this visual

    # type of the visual to add (e.g. view)
    element_type = html.request.get_str_input_mandatory("type")

    create_info_raw = html.request.get_str_input_mandatory("create_info")

    create_info = json.loads(create_info_raw)
>>>>>>> upstream/master
    visual_type.add_visual_handler(visual_name, element_type, create_info["context"],
                                   create_info["params"])
