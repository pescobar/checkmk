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

import sys
import errno
import os
import copy
import json
<<<<<<< HEAD
from typing import Any, Callable, Dict, List, NewType, Optional, Tuple, Union  # pylint: disable=unused-import
import six
from pathlib2 import Path

import cmk
import cmk.gui.utils as utils
import cmk.utils.tags
import cmk.gui.i18n
from cmk.gui.i18n import _
import cmk.gui.log as log
import cmk.utils.paths
import cmk.utils.store as store
=======
from types import ModuleType
from typing import Set, Any, AnyStr, Callable, Dict, List, Optional, Tuple, Union
from pathlib import Path
import time

from six import ensure_str

from livestatus import SiteId, SiteConfiguration, SiteConfigurations

import cmk.utils.version as cmk_version
import cmk.utils.tags
import cmk.utils.paths
import cmk.utils.store as store
from cmk.utils.type_defs import UserId

# TODO: Nuke the 'user' import and simply use cmk.gui.globals.user. Currently
# this is a bit difficult due to our beloved circular imports. :-/ Or should we
# do this the other way round? Anyway, we will know when the cycle has been
# broken...
from cmk.gui.globals import local, user
import cmk.gui.utils as utils
import cmk.gui.i18n
from cmk.gui.i18n import _
import cmk.gui.log as log
>>>>>>> upstream/master
from cmk.gui.exceptions import MKConfigError, MKAuthException
import cmk.gui.permissions as permissions

import cmk.gui.plugins.config

# This import is added for static analysis tools like pylint to make them
# know about all shipped config options. The default config options are
# later handled with the default_config dict and _load_default_config()
from cmk.gui.plugins.config.base import *  # pylint: disable=wildcard-import,unused-wildcard-import

<<<<<<< HEAD
if not cmk.is_raw_edition():
    from cmk.gui.cee.plugins.config.cee import *  # pylint: disable=wildcard-import,unused-wildcard-import

if cmk.is_managed_edition():
    from cmk.gui.cme.plugins.config.cme import *  # pylint: disable=wildcard-import,unused-wildcard-import
=======
if not cmk_version.is_raw_edition():
    from cmk.gui.cee.plugins.config.cee import *  # pylint: disable=wildcard-import,unused-wildcard-import,no-name-in-module

if cmk_version.is_managed_edition():
    from cmk.gui.cme.plugins.config.cme import *  # pylint: disable=wildcard-import,unused-wildcard-import,no-name-in-module
>>>>>>> upstream/master

#   .--Declarations--------------------------------------------------------.
#   |       ____            _                 _   _                        |
#   |      |  _ \  ___  ___| | __ _ _ __ __ _| |_(_) ___  _ __  ___        |
#   |      | | | |/ _ \/ __| |/ _` | '__/ _` | __| |/ _ \| '_ \/ __|       |
#   |      | |_| |  __/ (__| | (_| | | | (_| | |_| | (_) | | | \__ \       |
#   |      |____/ \___|\___|_|\__,_|_|  \__,_|\__|_|\___/|_| |_|___/       |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Declarations of global variables and constants                      |
#   '----------------------------------------------------------------------'

<<<<<<< HEAD
SiteId = NewType('SiteId', str)
SiteConfiguration = NewType('SiteConfiguration', Dict[str, Any])
SiteConfigurations = NewType('SiteConfigurations', Dict[SiteId, SiteConfiguration])

=======
>>>>>>> upstream/master
multisite_users = {}
admin_users = []
tags = cmk.utils.tags.TagConfig()

# hard coded in various permissions
builtin_role_ids = ["user", "admin", "guest"]

# Base directory of dynamic configuration
config_dir = cmk.utils.paths.var_dir + "/web"

# Stores the initial configuration values
<<<<<<< HEAD
default_config = {}  # type: Dict[str, Any]
=======
default_config: Dict[str, Any] = {}
# Needed as helper to determine the builtin variables
_vars_before_plugins: Set[str] = set()
>>>>>>> upstream/master

# TODO: Clean this up
permission_declaration_functions = []

# Constants for BI
ALL_HOSTS = '(.*)'
HOST_STATE = ('__HOST_STATE__',)
HIDDEN = ('__HIDDEN__',)


<<<<<<< HEAD
class FOREACH_HOST(object):
    pass


class FOREACH_CHILD(object):
    pass


class FOREACH_CHILD_WITH(object):
    pass


class FOREACH_PARENT(object):
    pass


class FOREACH_SERVICE(object):
    pass


class REMAINING(object):
    pass


class DISABLED(object):
    pass


class HARD_STATES(object):
    pass


class DT_AGGR_WARN(object):
=======
class FOREACH_HOST:
    pass


class FOREACH_CHILD:
    pass


class FOREACH_CHILD_WITH:
    pass


class FOREACH_PARENT:
    pass


class FOREACH_SERVICE:
    pass


class REMAINING:
    pass


class DISABLED:
    pass


class HARD_STATES:
    pass


class DT_AGGR_WARN:
>>>>>>> upstream/master
    pass


# Has to be declared here once since the functions can be assigned in
# bi.py and also in multisite.mk. "Double" declarations are no problem
# here since this is a dict (List objects have problems with duplicate
# definitions).
<<<<<<< HEAD
aggregation_functions = {}  # type: Dict[str, Callable]
=======
aggregation_functions: Dict[str, Callable] = {}
>>>>>>> upstream/master

#.
#   .--Functions-----------------------------------------------------------.
#   |             _____                 _   _                              |
#   |            |  ___|   _ _ __   ___| |_(_) ___  _ __  ___              |
#   |            | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|             |
#   |            |  _|| |_| | | | | (__| |_| | (_) | | | \__ \             |
#   |            |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/             |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Helper functions for config parsing, login, etc.                    |
#   '----------------------------------------------------------------------'


def initialize():
<<<<<<< HEAD
=======
    # type () -> None
>>>>>>> upstream/master
    clear_user_login()
    load_config()
    log.set_log_levels(log_levels)
    cmk.gui.i18n.set_user_localizations(user_localizations)


<<<<<<< HEAD
def _load_config_file(path):
    # type: (str) -> None
    """Load the given GUI configuration file"""
    try:
        exec (open(path).read(), globals(), globals())
=======
def _load_config_file(path: str) -> None:
    """Load the given GUI configuration file"""
    try:
        # TODO: Can be changed to text IO with Python 3
        with Path(path).open("rb") as f:
            exec(f.read(), globals(), globals())  # yapf: disable
>>>>>>> upstream/master
    except IOError as e:
        if e.errno != errno.ENOENT:  # No such file or directory
            raise
    except Exception as e:
        raise MKConfigError(_("Cannot read configuration file %s: %s:") % (path, e))


# Load multisite.mk and all files in multisite.d/. This will happen
# for *each* HTTP request.
# FIXME: Optimize this to cache the config etc. until either the config files or plugins
# have changed. We could make this being cached for multiple requests just like the
# plugins of other modules. This may save significant time in case of small requests like
# the graph ajax page or similar.
<<<<<<< HEAD
def load_config():
    # type: () -> None
=======
def load_config() -> None:
>>>>>>> upstream/master
    global sites

    # Set default values for all user-changable configuration settings
    _initialize_with_default_config()

    # Initialze sites with default site configuration. Need to do it here to
    # override possibly deleted sites
    sites = default_single_site_configuration()

    # First load main file
    _load_config_file(cmk.utils.paths.default_config_dir + "/multisite.mk")

    # Load also recursively all files below multisite.d
    conf_dir = cmk.utils.paths.default_config_dir + "/multisite.d"
    filelist = []
    if os.path.isdir(conf_dir):
        for root, _directories, files in os.walk(conf_dir):
            for filename in files:
                if filename.endswith(".mk"):
                    filelist.append(root + "/" + filename)

    filelist.sort()
    for p in filelist:
        _load_config_file(p)

    if sites:
        sites = migrate_old_site_config(sites)
    else:
        sites = default_single_site_configuration()

    _prepare_tag_config()
    execute_post_config_load_hooks()


<<<<<<< HEAD
def _prepare_tag_config():
    # type: () -> None
=======
def _prepare_tag_config() -> None:
>>>>>>> upstream/master
    global tags

    # When the user config does not contain "tags" a pre 1.6 config is loaded. Convert
    # the wato_host_tags and wato_aux_tags to the new structure
    tag_config = wato_tags
    if not any(tag_config.values()) and (wato_host_tags or wato_aux_tags):
        tag_config = cmk.utils.tags.transform_pre_16_tags(wato_host_tags, wato_aux_tags)

    tags = cmk.utils.tags.get_effective_tag_config(tag_config)


<<<<<<< HEAD
def execute_post_config_load_hooks():
    # type: () -> None
=======
def execute_post_config_load_hooks() -> None:
>>>>>>> upstream/master
    for func in _post_config_load_hooks:
        func()


<<<<<<< HEAD
_post_config_load_hooks = []  # type: List[Callable[[], None]]


def register_post_config_load_hook(func):
    # type: (Callable[[], None]) -> None
    _post_config_load_hooks.append(func)


def _initialize_with_default_config():
    # type: () -> None
    vars_before_plugins = all_nonfunction_vars(globals())
    load_plugins(True)
    vars_after_plugins = all_nonfunction_vars(globals())
    _load_default_config(vars_before_plugins, vars_after_plugins)
=======
_post_config_load_hooks: List[Callable[[], None]] = []


def register_post_config_load_hook(func: Callable[[], None]) -> None:
    _post_config_load_hooks.append(func)


def _initialize_with_default_config() -> None:
    # Since plugin loading changes the global namespace and these changes are kept
    # for the whole module lifetime, the "vars before plugins" can only be determined
    # once before the first plugin loading
    if not _vars_before_plugins:
        _vars_before_plugins.update(all_nonfunction_vars(globals()))

    load_plugins(True)
    vars_after_plugins = all_nonfunction_vars(globals())
    _load_default_config(_vars_before_plugins, vars_after_plugins)
>>>>>>> upstream/master

    _apply_default_config()


<<<<<<< HEAD
def _apply_default_config():
    # type: () -> None
=======
def _apply_default_config() -> None:
>>>>>>> upstream/master
    for k, v in default_config.items():
        if isinstance(v, (dict, list)):
            v = copy.deepcopy(v)
        globals()[k] = v


<<<<<<< HEAD
def _load_default_config(vars_before_plugins, vars_after_plugins):
=======
def _load_default_config(vars_before_plugins: Set[str], vars_after_plugins: Set[str]) -> None:
>>>>>>> upstream/master
    default_config.clear()
    _load_default_config_from_module_plugins()
    _load_default_config_from_legacy_plugins(vars_before_plugins, vars_after_plugins)


<<<<<<< HEAD
def _load_default_config_from_module_plugins():
    # TODO: Find a better solution for this. Probably refactor declaration of default
    # config option.
    config_plugin_vars = {}
=======
def _load_default_config_from_module_plugins() -> None:
    # TODO: Find a better solution for this. Probably refactor declaration of default
    # config option.
    config_plugin_vars: Dict = {}
>>>>>>> upstream/master
    for module in _config_plugin_modules():
        config_plugin_vars.update(module.__dict__)

    for k, v in config_plugin_vars.items():
        if k[0] == "_":
            continue

        if isinstance(v, (dict, list)):
            v = copy.deepcopy(v)

        default_config[k] = v


<<<<<<< HEAD
def _load_default_config_from_legacy_plugins(vars_before_plugins, vars_after_plugins):
    new_vars = vars_after_plugins.difference(vars_before_plugins)
    default_config.update(dict([(k, copy.deepcopy(globals()[k])) for k in new_vars]))


def _config_plugin_modules():
=======
def _load_default_config_from_legacy_plugins(vars_before_plugins: Set[str],
                                             vars_after_plugins: Set[str]) -> None:
    new_vars = vars_after_plugins.difference(vars_before_plugins)
    default_config.update({k: copy.deepcopy(globals()[k]) for k in new_vars})


def _config_plugin_modules() -> List[ModuleType]:
>>>>>>> upstream/master
    return [
        module for name, module in sys.modules.items()
        if (name.startswith("cmk.gui.plugins.config.") or name.startswith(
            "cmk.gui.cee.plugins.config.") or name.startswith("cmk.gui.cme.plugins.config.")) and
        module is not None
    ]


<<<<<<< HEAD
def reporting_available():
    try:
        # Check the existance of one arbitrary config variable from the
        # reporting module
        _dummy = reporting_filename
        return True
    except NameError:
        return False


def combined_graphs_available():
    try:
        _dummy = have_combined_graphs
        return True
    except NameError:
        return False


def hide_language(lang):
    return lang in hide_languages


def all_nonfunction_vars(var_dict):
=======
def reporting_available() -> bool:
    # Check the existance of one arbitrary config variable from the reporting module
    return 'reporting_filename' in globals()


def combined_graphs_available() -> bool:
    return 'have_combined_graphs' in globals()


def hide_language(lang: str) -> bool:
    return lang in hide_languages


def all_nonfunction_vars(var_dict: Dict[str, Any]) -> Set[str]:
>>>>>>> upstream/master
    return {
        name for name, value in var_dict.items()
        if name[0] != '_' and not hasattr(value, '__call__')
    }


<<<<<<< HEAD
def get_language(default=None):
    if default is None:
        return default_language
    return default
=======
def get_language() -> Optional[str]:
    return default_language
>>>>>>> upstream/master


#.
#   .--Permissions---------------------------------------------------------.
#   |        ____                     _         _                          |
#   |       |  _ \ ___ _ __ _ __ ___ (_)___ ___(_) ___  _ __  ___          |
#   |       | |_) / _ \ '__| '_ ` _ \| / __/ __| |/ _ \| '_ \/ __|         |
#   |       |  __/  __/ |  | | | | | | \__ \__ \ | (_) | | | \__ \         |
#   |       |_|   \___|_|  |_| |_| |_|_|___/___/_|\___/|_| |_|___/         |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Declarations of permissions and roles                                |
#   '----------------------------------------------------------------------'

# Kept for compatibility with pre 1.6 GUI plugins
declare_permission = permissions.declare_permission
declare_permission_section = permissions.declare_permission_section


# Some module have a non-fixed list of permissions. For example for
# each user defined view there is also a permission. This list is
# not known at the time of the loading of the module - though. For
# that purpose module can register functions. These functions should
# just call declare_permission(). They are being called in the correct
# situations.
# TODO: Clean this up
<<<<<<< HEAD
def declare_dynamic_permissions(func):
=======
def declare_dynamic_permissions(func: Callable) -> None:
>>>>>>> upstream/master
    permission_declaration_functions.append(func)


# This function needs to be called by all code that needs access
# to possible dynamic permissions
# TODO: Clean this up
<<<<<<< HEAD
def load_dynamic_permissions():
=======
def load_dynamic_permissions() -> None:
>>>>>>> upstream/master
    for func in permission_declaration_functions:
        func()


<<<<<<< HEAD
def get_role_permissions():
    """Returns the set of permissions for all roles"""
    role_permissions = {}
    roleids = roles.keys()
    for perm_class in permissions.permission_registry.values():
        perm = perm_class()
        for role_id in roleids:
            if not role_id in role_permissions:
=======
def get_role_permissions() -> Dict[str, List[str]]:
    """Returns the set of permissions for all roles"""
    role_permissions: Dict[str, List[str]] = {}
    roleids = set(roles.keys())
    for perm in permissions.permission_registry.values():
        for role_id in roleids:
            if role_id not in role_permissions:
>>>>>>> upstream/master
                role_permissions[role_id] = []

            if _may_with_roles([role_id], perm.name):
                role_permissions[role_id].append(perm.name)
    return role_permissions


<<<<<<< HEAD
def _may_with_roles(some_role_ids, pname):
=======
def _may_with_roles(some_role_ids: List[str], pname: str) -> bool:
>>>>>>> upstream/master
    # If at least one of the given roles has this permission, it's fine
    for role_id in some_role_ids:
        role = roles[role_id]

        he_may = role.get("permissions", {}).get(pname)
        # Handle compatibility with permissions without "general." that
        # users might have saved in their own custom roles.
        if he_may is None and pname.startswith("general."):
            he_may = role.get("permissions", {}).get(pname[8:])

        if he_may is None:  # not explicitely listed -> take defaults
            if "basedon" in role:
                base_role_id = role["basedon"]
            else:
                base_role_id = role_id
            if pname not in permissions.permission_registry:
                return False  # Permission unknown. Assume False. Functionality might be missing
<<<<<<< HEAD
            perm = permissions.permission_registry[pname]()
=======
            perm = permissions.permission_registry[pname]
>>>>>>> upstream/master
            he_may = base_role_id in perm.defaults
        if he_may:
            return True
    return False


#.
#   .--User Login----------------------------------------------------------.
#   |           _   _                 _                _                   |
#   |          | | | |___  ___ _ __  | |    ___   __ _(_)_ __              |
#   |          | | | / __|/ _ \ '__| | |   / _ \ / _` | | '_ \             |
#   |          | |_| \__ \  __/ |    | |__| (_) | (_| | | | | |            |
#   |           \___/|___/\___|_|    |_____\___/ \__, |_|_| |_|            |
#   |                                            |___/                     |
#   +----------------------------------------------------------------------+
#   | Managing the currently logged in user                                |
#   '----------------------------------------------------------------------'
# TODO: Shouldn't this be moved to e.g. login.py or userdb.py?


<<<<<<< HEAD
# This objects intention is currently only to handle the currently logged in user after authentication.
# But maybe this can be used for managing all user objects in future.
# TODO: Cleanup accesses to module global vars and functions
class LoggedInUser(object):
    def __init__(self, user_id):
        self.id = user_id

        self._load_confdir()
        self._load_roles()
        self._load_attributes()
        self._load_permissions()
        self._load_site_config()
        self._button_counts = None

    # TODO: Clean up that baserole_* stuff?
    def _load_roles(self):
        # Determine the roles of the user. If the user is listed in
        # users, admin_users or guest_users in multisite.mk then we
        # give him the according roles. If the user has an explicit
        # profile in multisite_users (e.g. due to WATO), we rather
        # use that profile. Remaining (unknown) users get the default_user_role.
        # That can be set to None -> User has no permissions at all.
        self.role_ids = self._gather_roles()

        # Get base roles (admin/user/guest)
        self._load_base_roles()

        # Get best base roles and use as "the" role of the user
        if "admin" in self.baserole_ids:
            self.baserole_id = "admin"
        elif "user" in self.baserole_ids:
            self.baserole_id = "user"
        else:
            self.baserole_id = "guest"

    def _gather_roles(self):
        return roles_of_user(self.id)

    def _load_base_roles(self):
        base_roles = set([])
        for r in self.role_ids:
            if r in builtin_role_ids:
                base_roles.add(r)
            else:
                base_roles.add(roles[r]["basedon"])

        self.baserole_ids = list(base_roles)

    def _load_attributes(self):
        self.attributes = self.load_file("cached_profile", None)
        if self.attributes is None:
            if self.id in multisite_users:
                self.attributes = multisite_users[self.id]
            else:
                self.attributes = {
                    "roles": self.role_ids,
                }

        self.alias = self.attributes.get("alias", self.id)
        self.email = self.attributes.get("email", self.id)

    def _load_permissions(self):
        # Prepare cache of already computed permissions
        # Make sure, admin can restore permissions in any case!
        if self.id in admin_users:
            self.permissions = {
                "general.use": True,  # use Multisite
                "wato.use": True,  # enter WATO
                "wato.edit": True,  # make changes in WATO...
                "wato.users": True,  # ... with access to user management
            }
        else:
            self.permissions = {}

    def _load_confdir(self):
        self.confdir = config_dir + "/" + self.id.encode("utf-8")
        store.mkdir(self.confdir)

    def _load_site_config(self):
        self.siteconf = self.load_file("siteconfig", {})

    def get_button_counts(self):
        if not self._button_counts:
            self._button_counts = self.load_file("buttoncounts", {})
        return self._button_counts

    def save_site_config(self):
        self.save_file("siteconfig", self.siteconf)

    def get_attribute(self, key, deflt=None):
        return self.attributes.get(key, deflt)

    def set_attribute(self, key, value):
        self.attributes[key] = value

    def unset_attribute(self, key):
        try:
            del self.attributes[key]
        except KeyError:
            pass

    def language(self, default=None):
        return self.get_attribute("language", get_language(default))

    def contact_groups(self):
        return self.get_attribute("contactgroups", [])

    def load_stars(self):
        return set(self.load_file("favorites", []))

    def save_stars(self, stars):
        self.save_file("favorites", list(stars))

    def is_site_disabled(self, site_id):
        # type: (SiteId) -> bool
        siteconf = self.siteconf.get(site_id, {})
        return siteconf.get("disabled", False)

    def authorized_sites(self, unfiltered_sites=None):
        # type: (Optional[SiteConfigurations]) -> SiteConfigurations
=======
def _baserole_ids_from_role_ids(role_ids: List[str]) -> List[str]:
    base_roles = set()
    for r in role_ids:
        if r in builtin_role_ids:
            base_roles.add(r)
        else:
            base_roles.add(roles[r]["basedon"])
    return list(base_roles)


def _most_permissive_baserole_id(baserole_ids: List[str]) -> str:
    if "admin" in baserole_ids:
        return "admin"
    if "user" in baserole_ids:
        return "user"
    return "guest"


def _initial_permission_cache(user_id: Optional[UserId]) -> Dict[str, bool]:
    # Prepare cache of already computed permissions
    # Make sure, admin can restore permissions in any case!
    if user_id in [ensure_str(u) for u in admin_users]:
        return {
            "general.use": True,  # use Multisite
            "wato.use": True,  # enter WATO
            "wato.edit": True,  # make changes in WATO...
            "wato.users": True,  # ... with access to user management
        }
    return {}


def _confdir_for_user_id(user_id: Optional[UserId]) -> Optional[str]:
    if user_id is None:
        return None

    confdir = config_dir + "/" + ensure_str(user_id)
    store.mkdir(confdir)
    return confdir


# This objects intention is currently only to handle the currently logged in user after authentication.
# But maybe this can be used for managing all user objects in future.
# TODO: Cleanup accesses to module global vars and functions
class LoggedInUser:
    def __init__(self, user_id: Optional[str]) -> None:
        self.id = UserId(user_id) if user_id else None

        self.confdir = _confdir_for_user_id(self.id)
        self.role_ids = self._gather_roles(self.id)
        baserole_ids = _baserole_ids_from_role_ids(self.role_ids)
        self.baserole_id = _most_permissive_baserole_id(baserole_ids)
        self._attributes = self._load_attributes(self.id, self.role_ids)
        self.alias = self._attributes.get("alias", self.id)
        self.email = self._attributes.get("email", self.id)

        self._permissions = _initial_permission_cache(self.id)
        self._siteconf = self.load_file("siteconfig", {})
        self._button_counts: Dict[str, float] = {}
        self._stars: Set[str] = set()
        self._tree_states: Dict = {}
        self._bi_assumptions: Dict[Union[Tuple[str, str], Tuple[str, str, str]], int] = {}
        self._tableoptions: Dict[str, Dict[str, Any]] = {}

    @property
    def ident(self) -> str:
        """Return the user-id as a string, or crash.

        Returns:
            The user_id as a string.

        Raises:
            ValueError: whenever there is no user_id.

        """
        if self.id is None:
            raise AttributeError("No user_id on this instance.")
        return self.id

    def _gather_roles(self, user_id: Optional[UserId]) -> List[str]:
        return roles_of_user(user_id)

    def _load_attributes(self, user_id: Optional[UserId], role_ids: List[str]) -> Any:
        attributes = self.load_file("cached_profile", None)
        if attributes is None:
            attributes = multisite_users.get(user_id, {
                "roles": role_ids,
            })
        return attributes

    def get_attribute(self, key: str, deflt: Any = None) -> Any:
        return self._attributes.get(key, deflt)

    def _set_attribute(self, key: str, value: Any) -> None:
        self._attributes[key] = value

    def _unset_attribute(self, key: str) -> None:
        try:
            del self._attributes[key]
        except KeyError:
            pass

    @property
    def language(self) -> Optional[str]:
        return self.get_attribute("language", get_language())

    @language.setter
    def language(self, value: Optional[str]) -> None:
        self._set_attribute("language", value)

    def reset_language(self) -> None:
        self._unset_attribute("language")

    @property
    def customer_id(self) -> Optional[str]:
        return self.get_attribute("customer")

    @property
    def contact_groups(self) -> List:
        return self.get_attribute("contactgroups", [])

    @property
    def show_help(self) -> bool:
        return self.load_file("help", False)

    @show_help.setter
    def show_help(self, value: bool) -> None:
        self.save_file("help", value)

    @property
    def acknowledged_notifications(self) -> int:
        return self.load_file("acknowledged_notifications", 0)

    @acknowledged_notifications.setter
    def acknowledged_notifications(self, value: int) -> None:
        self.save_file("acknowledged_notifications", value)

    @property
    def discovery_checkboxes(self) -> bool:
        return self.load_file("discovery_checkboxes", False)

    @discovery_checkboxes.setter
    def discovery_checkboxes(self, value: bool) -> None:
        self.save_file("discovery_checkboxes", value)

    @property
    def parameter_column(self) -> bool:
        return self.load_file("parameter_column", False)

    @parameter_column.setter
    def parameter_column(self, value: bool) -> None:
        self.save_file("parameter_column", value)

    @property
    def discovery_show_discovered_labels(self) -> bool:
        return self.load_file("discovery_show_discovered_labels", False)

    @discovery_show_discovered_labels.setter
    def discovery_show_discovered_labels(self, value: bool) -> None:
        self.save_file("discovery_show_discovered_labels", value)

    @property
    def discovery_show_plugin_names(self) -> bool:
        return self.load_file("discovery_show_plugin_names", False)

    @discovery_show_plugin_names.setter
    def discovery_show_plugin_names(self, value: bool) -> None:
        self.save_file("discovery_show_plugin_names", value)

    @property
    def wato_folders_show_tags(self) -> bool:
        return self.load_file("wato_folders_show_tags", False)

    @wato_folders_show_tags.setter
    def wato_folders_show_tags(self, value: bool) -> None:
        self.save_file("wato_folders_show_tags", value)

    @property
    def wato_folders_show_labels(self) -> bool:
        return self.load_file("wato_folders_show_labels", False)

    @wato_folders_show_labels.setter
    def wato_folders_show_labels(self, value: bool) -> None:
        self.save_file("wato_folders_show_labels", value)

    @property
    def bi_expansion_level(self) -> int:
        return self.load_file("bi_treestate", (None,))[0]

    @bi_expansion_level.setter
    def bi_expansion_level(self, value: int) -> None:
        self.save_file("bi_treestate", (value,))

    @property
    def stars(self) -> Set[str]:
        if not self._stars:
            self._stars = set(self.load_file("favorites", []))
        return self._stars

    def save_stars(self) -> None:
        self.save_file("favorites", list(self._stars))

    @property
    def tree_states(self) -> Dict:
        if not self._tree_states:
            self._tree_states = self.load_file("treestates", {})
        return self._tree_states

    def get_tree_states(self, tree):
        return self.tree_states.get(tree, {})

    def set_tree_state(self, tree, key, val):
        if tree not in self.tree_states:
            self.tree_states[tree] = {}

        self.tree_states[tree][key] = val

    def set_tree_states(self, tree, val):
        self.tree_states[tree] = val

    def save_tree_states(self) -> None:
        self.save_file("treestates", self._tree_states)

    @property
    def bi_assumptions(self):
        if not self._bi_assumptions:
            self._bi_assumptions = self.load_file("bi_assumptions", {})
        return self._bi_assumptions

    def save_bi_assumptions(self):
        self.save_file("bi_assumptions", self._bi_assumptions)

    @property
    def tableoptions(self) -> Dict[str, Dict[str, Any]]:
        if not self._tableoptions:
            self._tableoptions = self.load_file("tableoptions", {})
        return self._tableoptions

    def save_tableoptions(self) -> None:
        self.save_file("tableoptions", self._tableoptions)

    def get_rowselection(self, selection_id: str, identifier: str) -> List[str]:
        vo = self.load_file("rowselection/%s" % selection_id, {})
        return vo.get(identifier, [])

    def set_rowselection(self, selection_id: str, identifier: str, rows: List[str],
                         action: str) -> None:
        vo = self.load_file("rowselection/%s" % selection_id, {}, lock=True)

        if action == 'set':
            vo[identifier] = rows

        elif action == 'add':
            vo[identifier] = list(set(vo.get(identifier, [])).union(rows))

        elif action == 'del':
            vo[identifier] = list(set(vo.get(identifier, [])) - set(rows))

        elif action == 'unset':
            del vo[identifier]

        self.save_file("rowselection/%s" % selection_id, vo)

    def cleanup_old_selections(self) -> None:
        # Delete all selection files older than the defined livetime.
        if self.confdir is None:
            return

        path = self.confdir + '/rowselection'
        try:
            for f in os.listdir(path):
                if f[1] != '.' and f.endswith('.mk'):
                    p = path + '/' + f
                    if time.time() - os.stat(p).st_mtime > selection_livetime:
                        os.unlink(p)
        except OSError:
            pass  # no directory -> no cleanup

    def get_sidebar_configuration(self, default: Dict[str, Any]) -> Dict[str, Any]:
        return self.load_file("sidebar", default)

    def set_sidebar_configuration(self, configuration: Dict[str, Any]) -> None:
        self.save_file("sidebar", configuration)

    def is_site_disabled(self, site_id: SiteId) -> bool:
        return self._siteconf.get(site_id, {}).get("disabled", False)

    def disable_site(self, site_id: SiteId) -> None:
        self._siteconf.setdefault(site_id, {})["disabled"] = True

    def enable_site(self, site_id: SiteId) -> None:
        self._siteconf.setdefault(site_id, {}).pop("disabled", None)

    def save_site_config(self) -> None:
        self.save_file("siteconfig", self._siteconf)

    def transids(self, lock: bool = False) -> List[str]:
        return self.load_file("transids", [], lock=lock)

    def save_transids(self, transids: List[str]) -> None:
        if self.id:
            self.save_file("transids", transids)

    def authorized_sites(self,
                         unfiltered_sites: Optional[SiteConfigurations] = None
                        ) -> SiteConfigurations:
>>>>>>> upstream/master
        if unfiltered_sites is None:
            unfiltered_sites = allsites()

        authorized_sites = self.get_attribute("authorized_sites")
        if authorized_sites is None:
<<<<<<< HEAD
            return SiteConfigurations(dict(unfiltered_sites))

        return SiteConfigurations({
            site_id: s  #
            for site_id, s in unfiltered_sites.iteritems()
            if site_id in authorized_sites
        })

    def authorized_login_sites(self):
        # type: () -> SiteConfigurations
        login_site_ids = get_login_slave_sites()
        return self.authorized_sites(
            SiteConfigurations({
                site_id: s  #
                for site_id, s in allsites().items()
                if site_id in login_site_ids
            }))

    def may(self, pname):
        # type: (str) -> bool
        if pname in self.permissions:
            return self.permissions[pname]
        he_may = _may_with_roles(user.role_ids, pname)
        self.permissions[pname] = he_may
        return he_may

    def need_permission(self, pname):
        if not self.may(pname):
            perm = permissions.permission_registry[pname]()
            raise MKAuthException(
                _("We are sorry, but you lack the permission "
                  "for this operation. If you do not like this "
                  "then please ask you administrator to provide you with "
                  "the following permission: '<b>%s</b>'.") % perm.title)

    def load_file(self, name, deflt, lock=False):
        # In some early error during login phase there are cases where it might
        # happen that a user file is requested but the user is not yet
        # set. We have all information to set it, then do it.
        if not user:
            return deflt  # No user known at this point of time

        path = self.confdir + "/" + name + ".mk"
        return store.load_data_from_file(path, deflt, lock)

    def save_file(self, name, content, unlock=False):
        save_user_file(name, content, self.id, unlock)

    def file_modified(self, name):
=======
            return dict(unfiltered_sites)

        return {
            site_id: s  #
            for site_id, s in unfiltered_sites.items()
            if site_id in authorized_sites
        }

    def authorized_login_sites(self) -> SiteConfigurations:
        login_site_ids = get_login_slave_sites()
        return self.authorized_sites(
            {site_id: s for site_id, s in allsites().items() if site_id in login_site_ids})

    def may(self, pname: str) -> bool:
        if pname in self._permissions:
            return self._permissions[pname]
        he_may = _may_with_roles(self.role_ids, pname)
        self._permissions[pname] = he_may
        return he_may

    def need_permission(self, pname: str) -> None:
        if not self.may(pname):
            perm = permissions.permission_registry[pname]
            raise MKAuthException(
                _("We are sorry, but you lack the permission "
                  "for this operation. If you do not like this "
                  "then please ask your administrator to provide you with "
                  "the following permission: '<b>%s</b>'.") % perm.title)

    def load_file(self, name: str, deflt: Any, lock: bool = False) -> Any:
        if self.confdir is None:
            return deflt

        path = self.confdir + "/" + name + ".mk"

        # The user files we load with this function are mostly some kind of persisted states.  In
        # case a file is corrupted for some reason we rather start over with the default instead of
        # failing at some random places.
        try:
            return store.load_object_from_file(path, default=deflt, lock=lock)
        except (ValueError, SyntaxError):
            return deflt

    def save_file(self, name: str, content: Any) -> None:
        save_user_file(name, content, self.id)

    def file_modified(self, name: str) -> float:
>>>>>>> upstream/master
        if self.confdir is None:
            return 0

        try:
            return os.stat(self.confdir + "/" + name + ".mk").st_mtime
        except OSError as e:
            if e.errno == errno.ENOENT:
                return 0
<<<<<<< HEAD
            else:
                raise
=======
            raise
>>>>>>> upstream/master


# Login a user that has all permissions. This is needed for making
# Livestatus queries from unauthentiated page handlers
# TODO: Can we somehow get rid of this?
class LoggedInSuperUser(LoggedInUser):
<<<<<<< HEAD
    def __init__(self):
=======
    def __init__(self) -> None:
>>>>>>> upstream/master
        super(LoggedInSuperUser, self).__init__(None)
        self.alias = "Superuser for unauthenticated pages"
        self.email = "admin"

<<<<<<< HEAD
    def _gather_roles(self):
        return ["admin"]

    def _load_confdir(self):
        self.confdir = None

    def _load_site_config(self):
        self.siteconf = {}

    def load_file(self, name, deflt, lock=False):
        return deflt


class LoggedInNobody(LoggedInUser):
    def __init__(self):
=======
    def _gather_roles(self, _user_id: Optional[UserId]) -> List[str]:
        return ["admin"]


class LoggedInNobody(LoggedInUser):
    def __init__(self) -> None:
>>>>>>> upstream/master
        super(LoggedInNobody, self).__init__(None)
        self.alias = "Unauthenticated user"
        self.email = "nobody"

<<<<<<< HEAD
    def _gather_roles(self):
        return []

    def _load_confdir(self):
        self.confdir = None

    def _load_site_config(self):
        self.siteconf = {}

    def load_file(self, name, deflt, lock=False):
        return deflt


def clear_user_login():
    _set_user(LoggedInNobody())


def set_user_by_id(user_id):
    _set_user(LoggedInUser(user_id))


def set_super_user():
    _set_user(LoggedInSuperUser())


def _set_user(_user):
    global user
    user = _user


# This holds the currently logged in user object
user = LoggedInNobody()
=======
    def _gather_roles(self, _user_id: Optional[UserId]) -> List[str]:
        return []


def clear_user_login() -> None:
    _set_user(LoggedInNobody())


def set_user_by_id(user_id: UserId) -> None:
    _set_user(LoggedInUser(user_id))


def set_super_user() -> None:
    _set_user(LoggedInSuperUser())


def _set_user(_user: LoggedInUser) -> None:
    """Set the currently logged in user (thread safe).

    local.user will set the current RequestContext to _user and it will be accessible via
    cmk.gui.globals.user directly. This is imported here."""
    local.user = _user

>>>>>>> upstream/master

#.
#   .--User Handling-------------------------------------------------------.
#   |    _   _                 _   _                 _ _ _                 |
#   |   | | | |___  ___ _ __  | | | | __ _ _ __   __| | (_)_ __   __ _     |
#   |   | | | / __|/ _ \ '__| | |_| |/ _` | '_ \ / _` | | | '_ \ / _` |    |
#   |   | |_| \__ \  __/ |    |  _  | (_| | | | | (_| | | | | | | (_| |    |
#   |    \___/|___/\___|_|    |_| |_|\__,_|_| |_|\__,_|_|_|_| |_|\__, |    |
#   |                                                            |___/     |
#   +----------------------------------------------------------------------+
#   | General user handling of all users, not only the currently logged    |
#   | in user. These functions are mostly working with the loaded multisite|
#   | configuration data (multisite_users, admin_users, ...), so they are  |
#   | more related to this module than to the userdb module.               |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def roles_of_user(user_id):
=======
def roles_of_user(user_id: Optional[UserId]) -> List[str]:
>>>>>>> upstream/master
    def existing_role_ids(role_ids):
        return [role_id for role_id in role_ids if role_id in roles]

    if user_id in multisite_users:
        return existing_role_ids(multisite_users[user_id]["roles"])
<<<<<<< HEAD
    elif user_id in admin_users:
        return ["admin"]
    elif user_id in guest_users:
        return ["guest"]
    elif users is not None and user_id in users:
        return ["user"]
    elif os.path.exists(config_dir + "/" + user_id.encode("utf-8") + "/automation.secret"):
        return ["guest"]  # unknown user with automation account
    elif 'roles' in default_user_profile:
        return existing_role_ids(default_user_profile['roles'])
    elif default_user_role:
=======
    if user_id in [ensure_str(u) for u in admin_users]:
        return ["admin"]
    if user_id in [ensure_str(u) for u in guest_users]:
        return ["guest"]
    if users is not None and user_id in [ensure_str(u) for u in users]:
        return ["user"]
    if user_id is not None and os.path.exists(config_dir + "/" + ensure_str(user_id) +
                                              "/automation.secret"):
        return ["guest"]  # unknown user with automation account
    if 'roles' in default_user_profile:
        return existing_role_ids(default_user_profile['roles'])
    if default_user_role:
>>>>>>> upstream/master
        return existing_role_ids([default_user_role])
    return []


<<<<<<< HEAD
def alias_of_user(user_id):
=======
def alias_of_user(user_id: Optional[UserId]) -> Optional[UserId]:
>>>>>>> upstream/master
    if user_id in multisite_users:
        return multisite_users[user_id].get("alias", user_id)
    return user_id


<<<<<<< HEAD
def user_may(user_id, pname):
=======
def user_may(user_id: Optional[UserId], pname: str) -> bool:
>>>>>>> upstream/master
    return _may_with_roles(roles_of_user(user_id), pname)


# TODO: Check all calls for arguments (changed optional user to 3rd positional)
<<<<<<< HEAD
def save_user_file(name, data, user_id, unlock=False):
    path = config_dir + "/" + user_id.encode("utf-8") + "/" + name + ".mk"
    store.mkdir(os.path.dirname(path))
    store.save_data_to_file(path, data)


def migrate_old_site_config(site_config):
    # type: (SiteConfigurations) -> SiteConfigurations
=======
def save_user_file(name: str, data: Any, user_id: Optional[UserId]) -> None:
    if user_id is None:
        raise TypeError("The profiles of LoggedInSuperUser and LoggedInNobody cannot be saved")

    path = config_dir + "/" + ensure_str(user_id) + "/" + name + ".mk"
    store.mkdir(os.path.dirname(path))
    store.save_object_to_file(path, data)


def migrate_old_site_config(site_config: SiteConfigurations) -> SiteConfigurations:
>>>>>>> upstream/master
    if not site_config:
        # Prevent problem when user has deleted all sites from his
        # configuration and sites is {}. We assume a default single site
        # configuration in that case.
        return default_single_site_configuration()

<<<<<<< HEAD
    for site_id, site_cfg in site_config.iteritems():
=======
    for site_id, site_cfg in site_config.items():
>>>>>>> upstream/master
        # Until 1.6 "replication" could be not present or
        # set to "" instead of None
        if site_cfg.get("replication", "") == "":
            site_cfg["replication"] = None

        # Until 1.6 "url_prefix" was an optional attribute
        if "url_prefix" not in site_cfg:
            site_cfg["url_prefix"] = "/%s/" % site_id

        site_cfg.setdefault("proxy", None)

        _migrate_pre_16_socket_config(site_cfg)

    return site_config


# During development of the 1.6 version the site configuration has been cleaned up in several ways:
# 1. The "socket" attribute could be "disabled" to disable a site connection. This has already been
<<<<<<< HEAD
#    deprecated long time ago and was not configurable in WATO. This has now been superceeded by
=======
#    deprecated long time ago and was not configurable in WATO. This has now been superseded by
>>>>>>> upstream/master
#    the dedicated "disabled" attribute.
# 2. The "socket" attribute was optional. A not present socket meant "connect to local unix" socket.
#    This is now replaced with a value like this ("local", None) to reflect the generic
#    CascadingDropdown() data structure of "(type, attributes)".
# 3. The "socket" attribute was stored in the livestatus.py socketurl encoded format, at least when
#    livestatus proxy was not used. This is now stored in the CascadingDropdown() native format and
#    converted here to the correct format.
# 4. When the livestatus proxy was enabled for a site, the settings were stored in the "socket"
#    attribute. The proxy settings were an additional dict which also held a "socket" key containing
#    the final socket connection properties.
#    This has now been split up. The top level socket settings are now used independent of the proxy.
#    The proxy options are stored in the separate key "proxy" which is a mandatory key.
<<<<<<< HEAD
def _migrate_pre_16_socket_config(site_cfg):
    if site_cfg.get("socket") is None:
        site_cfg["socket"] = ("local", None)
        return

    socket = site_cfg["socket"]
=======
def _migrate_pre_16_socket_config(site_cfg: Dict[str, Any]) -> None:
    socket = site_cfg.get("socket")
    if socket is None:
        site_cfg["socket"] = ("local", None)
        return

>>>>>>> upstream/master
    if isinstance(socket, tuple) and socket[0] == "proxy":
        site_cfg["proxy"] = socket[1]

        # "socket" of proxy could either be None or two element tuple for "tcp"
        proxy_socket = site_cfg["proxy"].pop("socket", None)
        if proxy_socket is None:
            site_cfg["socket"] = ("local", None)

        elif isinstance(socket, tuple):
            site_cfg["socket"] = ("tcp", {
                "address": proxy_socket,
                "tls": ("plain_text", {}),
            })

        else:
            raise NotImplementedError("Unhandled proxy socket: %r" % proxy_socket)

        return

    if socket == 'disabled':
        site_cfg['disabled'] = True
        site_cfg['socket'] = ("local", None)
        return

<<<<<<< HEAD
    if isinstance(socket, six.string_types):
        site_cfg["socket"] = _migrate_string_encoded_socket(socket)


def _migrate_string_encoded_socket(value):
    # type: (str) -> Tuple[str, Union[Dict]]
    family_txt, address = value.split(":", 1)  # pylint: disable=no-member

    if family_txt == "unix":
        return "unix", {
            "path": value.split(":", 1)[1],
=======
    if isinstance(socket, str):
        site_cfg["socket"] = _migrate_string_encoded_socket(socket)


def _migrate_string_encoded_socket(value: AnyStr) -> Tuple[str, Union[Dict]]:
    str_value = ensure_str(value)
    family_txt, address = str_value.split(":", 1)

    if family_txt == "unix":
        return "unix", {
            "path": str_value.split(":", 1)[1],
>>>>>>> upstream/master
        }

    if family_txt in ["tcp", "tcp6"]:
        host, port = address.rsplit(":", 1)
        return family_txt, {
            "address": (host, int(port)),
            "tls": ("plain_text", {}),
        }

    raise NotImplementedError()


#.
#   .--Sites---------------------------------------------------------------.
#   |                        ____  _ _                                     |
#   |                       / ___|(_) |_ ___  ___                          |
#   |                       \___ \| | __/ _ \/ __|                         |
#   |                        ___) | | ||  __/\__ \                         |
#   |                       |____/|_|\__\___||___/                         |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  The config module provides some helper functions for sites.         |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def omd_site():
    # type: () -> SiteId
    return cmk.omd_site()


def url_prefix():
    # type: () -> str
    return "/%s/" % cmk.omd_site()


use_siteicons = False


def default_single_site_configuration():
    # type: () -> SiteConfigurations
    return SiteConfigurations({
        omd_site(): SiteConfiguration({
=======
def omd_site() -> SiteId:
    return SiteId(cmk_version.omd_site())


def url_prefix() -> str:
    return "/%s/" % cmk_version.omd_site()


def default_single_site_configuration() -> SiteConfigurations:
    return {
        omd_site(): {
>>>>>>> upstream/master
            'alias': _("Local site %s") % omd_site(),
            'socket': ("local", None),
            'disable_wato': True,
            'disabled': False,
            'insecure': False,
            'url_prefix': "/%s/" % omd_site(),
            'multisiteurl': '',
            'persist': False,
            'replicate_ec': False,
            'replication': None,
            'timeout': 5,
            'user_login': True,
            'proxy': None,
<<<<<<< HEAD
        })
    })


sites = SiteConfigurations({})


def sitenames():
    # () -> List[SiteId]
    return sites.keys()
=======
        }
    }


sites: SiteConfigurations = {}


def sitenames() -> List[SiteId]:
    return list(sites)
>>>>>>> upstream/master


# TODO: Cleanup: Make clear that this function is used by the status GUI (and not WATO)
# and only returns the currently enabled sites. Or should we redeclare the "disabled" state
# to disable the sites at all?
# TODO: Rename this!
<<<<<<< HEAD
def allsites():
    # type: () -> SiteConfigurations
    return SiteConfigurations({
        name: site(name)  #
        for name in sitenames()
        if not site(name).get("disabled", False)
    })


def configured_sites():
    # type: () -> SiteConfigurations
    return SiteConfigurations({site_id: site(site_id) for site_id in sitenames()})


def has_wato_slave_sites():
    return bool(wato_slave_sites())


def is_wato_slave_site():
    return _has_distributed_wato_file() and not has_wato_slave_sites()


def _has_distributed_wato_file():
=======
def allsites() -> SiteConfigurations:
    return {
        name: site(name)  #
        for name in sitenames()
        if not site(name).get("disabled", False)
    }


def configured_sites() -> SiteConfigurations:
    return {site_id: site(site_id) for site_id in sitenames()}


def has_wato_slave_sites() -> bool:
    return bool(wato_slave_sites())


def is_wato_slave_site() -> bool:
    return _has_distributed_wato_file() and not has_wato_slave_sites()


def _has_distributed_wato_file() -> bool:
>>>>>>> upstream/master
    return os.path.exists(cmk.utils.paths.check_mk_config_dir + "/distributed_wato.mk") \
        and os.stat(cmk.utils.paths.check_mk_config_dir + "/distributed_wato.mk").st_size != 0


<<<<<<< HEAD
def get_login_sites():
    # type: () -> List[SiteId]
=======
def get_login_sites() -> List[SiteId]:
>>>>>>> upstream/master
    """Returns the WATO slave sites a user may login and the local site"""
    return get_login_slave_sites() + [omd_site()]


# TODO: All site listing functions should return the same data structure, e.g. a list of
#       pairs (site_id, site)
<<<<<<< HEAD
def get_login_slave_sites():
    # type: () -> List[SiteId]
    """Returns a list of site ids which are WATO slave sites and users can login"""
    login_sites = []
    for site_id, site_spec in wato_slave_sites().iteritems():
=======
def get_login_slave_sites() -> List[SiteId]:
    """Returns a list of site ids which are WATO slave sites and users can login"""
    login_sites = []
    for site_id, site_spec in wato_slave_sites().items():
>>>>>>> upstream/master
        if site_spec.get('user_login', True) and not site_is_local(site_id):
            login_sites.append(site_id)
    return login_sites


<<<<<<< HEAD
def wato_slave_sites():
    # type: () -> SiteConfigurations
    return SiteConfigurations({
        site_id: s  #
        for site_id, s in sites.items()
        if s.get("replication")
    })


def sorted_sites():
    # type: () -> List[Tuple[SiteId, str]]
    return sorted([(site_id, s['alias']) for site_id, s in user.authorized_sites().iteritems()],
                  key=lambda k: k[1].lower())


def site(site_id):
    # type: (SiteId) -> SiteConfiguration
    s = SiteConfiguration(dict(sites.get(site_id, {})))
=======
def wato_slave_sites() -> SiteConfigurations:
    return {
        site_id: s  #
        for site_id, s in sites.items()
        if s.get("replication")
    }


def sorted_sites() -> List[Tuple[SiteId, str]]:
    return sorted([(site_id, s['alias']) for site_id, s in user.authorized_sites().items()],
                  key=lambda k: k[1].lower())


def site(site_id: SiteId) -> SiteConfiguration:
    s = dict(sites.get(site_id, {}))
>>>>>>> upstream/master
    # Now make sure that all important keys are available.
    # Add missing entries by supplying default values.
    s.setdefault("alias", site_id)
    s.setdefault("socket", ("local", None))
    s.setdefault("url_prefix", "../")  # relative URL from /check_mk/
    s["id"] = site_id
    return s


<<<<<<< HEAD
def site_is_local(site_id):
    # type: (SiteId) -> bool
=======
def site_is_local(site_id: SiteId) -> bool:
>>>>>>> upstream/master
    family_spec, address_spec = site(site_id)["socket"]
    return _is_local_socket_spec(family_spec, address_spec)


<<<<<<< HEAD
def _is_local_socket_spec(family_spec, address_spec):
    # type: (str, Dict[str, Any]) -> bool
=======
def _is_local_socket_spec(family_spec: str, address_spec: Dict[str, Any]) -> bool:
>>>>>>> upstream/master
    if family_spec == "local":
        return True

    if family_spec == "unix" and address_spec["path"] == cmk.utils.paths.livestatus_unix_socket:
        return True

    return False


<<<<<<< HEAD
def default_site():
    # type: () -> Optional[SiteId]
=======
def default_site() -> Optional[SiteId]:
>>>>>>> upstream/master
    for site_name, _site in sites.items():
        if site_is_local(site_name):
            return site_name
    return None


<<<<<<< HEAD
def is_single_local_site():
    # type: () -> bool
    if len(sites) > 1:
        return False
    elif len(sites) == 0:
        return True

    # Also use Multisite mode if the one and only site is not local
    sitename = sites.keys()[0]
    return site_is_local(sitename)


def site_attribute_default_value():
    # type: () -> Optional[SiteId]
=======
def is_single_local_site() -> bool:
    if len(sites) > 1:
        return False
    if len(sites) == 0:
        return True

    # Also use Multisite mode if the one and only site is not local
    sitename = list(sites.keys())[0]
    return site_is_local(sitename)


def site_attribute_default_value() -> Optional[SiteId]:
>>>>>>> upstream/master
    def_site = default_site()
    authorized_site_ids = user.authorized_sites(unfiltered_sites=configured_sites()).keys()
    if def_site and def_site in authorized_site_ids:
        return def_site
    return None


<<<<<<< HEAD
def site_attribute_choices():
    # () -> List[Tuple[SiteId, str]]
=======
def site_attribute_choices() -> List[Tuple[SiteId, str]]:
>>>>>>> upstream/master
    authorized_site_ids = user.authorized_sites(unfiltered_sites=configured_sites()).keys()
    return site_choices(filter_func=lambda site_id, site: site_id in authorized_site_ids)


<<<<<<< HEAD
def site_choices(filter_func=None):
    # (Optional[Callable[[SiteId, SiteConfiguration], bool]]) -> List[Tuple[SiteId, str]]
=======
def site_choices(
    filter_func: Optional[Callable[[SiteId, SiteConfiguration], bool]] = None
) -> List[Tuple[SiteId, str]]:
>>>>>>> upstream/master
    choices = []
    for site_id, site_spec in sites.items():
        if filter_func and not filter_func(site_id, site_spec):
            continue

        title = site_id
        if site_spec.get("alias"):
            title += " - " + site_spec["alias"]

        choices.append((site_id, title))

    return sorted(choices, key=lambda s: s[1])


<<<<<<< HEAD
def get_event_console_site_choices():
    # () -> List[Tuple[SiteId, str]]
    return site_choices(
        filter_func=lambda site_id, site: site_is_local(site_id) or site.get("replicate_ec"))
=======
def get_event_console_site_choices() -> List[Tuple[SiteId, str]]:
    return site_choices(
        filter_func=lambda site_id, site: site_is_local(site_id) or site.get("replicate_ec", False))


def get_wato_site_choices() -> List[Tuple[SiteId, str]]:
    return site_choices(filter_func=lambda site_id, site: site_is_local(site_id) or site.get(
        "replication") is not None)
>>>>>>> upstream/master


#.
#   .--Plugins-------------------------------------------------------------.
#   |                   ____  _             _                              |
#   |                  |  _ \| |_   _  __ _(_)_ __  ___                    |
#   |                  | |_) | | | | |/ _` | | '_ \/ __|                   |
#   |                  |  __/| | |_| | (_| | | | | \__ \                   |
#   |                  |_|   |_|\__,_|\__, |_|_| |_|___/                   |
#   |                                 |___/                                |
#   +----------------------------------------------------------------------+
#   |  Handling of our own plugins. In plugins other software pieces can   |
#   |  declare defaults for configuration variables.                       |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def load_plugins(force):
=======
def load_plugins(force: bool) -> None:
>>>>>>> upstream/master
    utils.load_web_plugins("config", globals())

    # Make sure, builtin roles are present, even if not modified and saved with WATO.
    for br in builtin_role_ids:
        roles.setdefault(br, {})


<<<<<<< HEAD
def theme_choices():
=======
def theme_choices() -> List[Tuple[str, str]]:
>>>>>>> upstream/master
    themes = {}

    for base_dir in [Path(cmk.utils.paths.web_dir), cmk.utils.paths.local_web_dir]:
        if not base_dir.exists():
            continue

<<<<<<< HEAD
        for theme_dir in (base_dir / "htdocs" / "themes").iterdir():  # pylint: disable=no-member
=======
        theme_base_dir = base_dir / "htdocs" / "themes"
        if not theme_base_dir.exists():
            continue

        for theme_dir in theme_base_dir.iterdir():
>>>>>>> upstream/master
            meta_file = theme_dir / "theme.json"
            if not meta_file.exists():
                continue

            try:
                theme_meta = json.loads(meta_file.open(encoding="utf-8").read())
            except ValueError:
                # Ignore broken meta files and show the directory name as title
                theme_meta = {
                    "title": theme_dir.name,
                }

<<<<<<< HEAD
=======
            assert isinstance(theme_meta["title"], str)
>>>>>>> upstream/master
            themes[theme_dir.name] = theme_meta["title"]

    return sorted(themes.items())


<<<<<<< HEAD
def get_page_heading():
    if "%s" in page_heading:
        return page_heading % (site(omd_site()).get('alias', _("GUI")))
    return page_heading
=======
def get_page_heading() -> str:
    if "%s" in page_heading:
        return ensure_str(page_heading % (site(omd_site()).get('alias', _("GUI"))))
    return ensure_str(page_heading)
>>>>>>> upstream/master
