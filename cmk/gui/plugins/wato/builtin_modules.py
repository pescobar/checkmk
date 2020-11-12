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

# List of modules for main menu and WATO snapin. These modules are
# defined in a plugin because they contain cmk.gui.i18n strings.
# fields: mode, title, icon, permission, help

<<<<<<< HEAD
import cmk

from cmk.gui.i18n import _

from cmk.gui.plugins.wato import (
    main_module_registry,
    MainModule,
=======
import time
import cmk.utils.version as cmk_version

from cmk.gui.i18n import _
from cmk.gui.globals import request
from cmk.gui.utils.urls import makeuri_contextless_ruleset_group

from cmk.gui.plugins.wato import (
    main_module_registry,
    ABCMainModule,
    MainModuleTopicHosts,
    MainModuleTopicServices,
    MainModuleTopicUsers,
    MainModuleTopicAgents,
    MainModuleTopicEvents,
    MainModuleTopicGeneral,
    MainModuleTopicMaintenance,
>>>>>>> upstream/master
)


@main_module_registry.register
<<<<<<< HEAD
class MainModuleFolder(MainModule):
=======
class MainModuleFolder(ABCMainModule):
>>>>>>> upstream/master
    @property
    def mode_or_url(self):
        return "folder"

    @property
<<<<<<< HEAD
=======
    def topic(self):
        return MainModuleTopicHosts

    @property
>>>>>>> upstream/master
    def title(self):
        return _("Hosts")

    @property
    def icon(self):
        return "folder"

    @property
    def permission(self):
        return "hosts"

    @property
    def description(self):
        return _("Manage monitored hosts and services and the hosts' folder structure.")

    @property
    def sort_index(self):
        return 10

<<<<<<< HEAD

@main_module_registry.register
class MainModuleTags(MainModule):
=======
    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleTags(ABCMainModule):
>>>>>>> upstream/master
    @property
    def mode_or_url(self):
        return "tags"

    @property
<<<<<<< HEAD
=======
    def topic(self):
        return MainModuleTopicHosts

    @property
>>>>>>> upstream/master
    def title(self):
        return _("Tags")

    @property
    def icon(self):
        return "tag"

    @property
    def permission(self):
        # The module was renamed from hosttags to tags during 1.6 development. The permission can not
        # be changed easily for compatibility reasons. Leave old internal name for simplicity.
        return "hosttags"

    @property
    def description(self):
        return _("Tags can be used to classify hosts and services in a flexible way.")

    @property
    def sort_index(self):
<<<<<<< HEAD
        return 15


@main_module_registry.register
class MainModuleGlobalSettings(MainModule):
=======
        return 30

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleGlobalSettings(ABCMainModule):
>>>>>>> upstream/master
    @property
    def mode_or_url(self):
        return "globalvars"

    @property
<<<<<<< HEAD
    def title(self):
        return _("Global Settings")
=======
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Global settings")
>>>>>>> upstream/master

    @property
    def icon(self):
        return "configuration"

    @property
    def permission(self):
        return "global"

    @property
    def description(self):
<<<<<<< HEAD
        return _("Global settings for Check_MK, Multisite and the monitoring core.")
=======
        return _("Global settings for Checkmk, Multisite and the monitoring core.")

    @property
    def sort_index(self):
        return 10

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleReadOnly(ABCMainModule):
    @property
    def mode_or_url(self):
        return "read_only"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Read only mode")

    @property
    def icon(self):
        return "read_only"

    @property
    def permission(self):
        return "read_only"

    @property
    def description(self):
        return _("Set the Checkmk configuration interface to read only mode for maintenance.")
>>>>>>> upstream/master

    @property
    def sort_index(self):
        return 20

<<<<<<< HEAD

@main_module_registry.register
class MainModuleHostAndServiceParameters(MainModule):
    @property
    def mode_or_url(self):
        return "ruleeditor"

    @property
    def title(self):
        return _("Host & Service Parameters")

    @property
    def icon(self):
        return "rulesets"
=======
    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleRuleSearch(ABCMainModule):
    @property
    def mode_or_url(self):
        return "rule_search"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Rule search")

    @property
    def icon(self):
        return "search"
>>>>>>> upstream/master

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
<<<<<<< HEAD
        return _("Check parameters and other configuration variables on hosts and services")

    @property
    def sort_index(self):
        return 25


@main_module_registry.register
class MainModuleStaticChecks(MainModule):
    @property
    def mode_or_url(self):
        return "static_checks"

    @property
    def title(self):
        return _("Manual Checks")

    @property
    def icon(self):
        return "static_checks"
=======
        return _("Search all rules and rulesets")

    @property
    def sort_index(self):
        return 5

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModulePredefinedConditions(ABCMainModule):
    @property
    def mode_or_url(self):
        return "predefined_conditions"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Predefined conditions")

    @property
    def icon(self):
        return "predefined_conditions"
>>>>>>> upstream/master

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
<<<<<<< HEAD
        return _("Configure fixed checks without using service discovery")
=======
        return _("Use predefined conditions to centralize the coniditions of your rulesets.")
>>>>>>> upstream/master

    @property
    def sort_index(self):
        return 30

<<<<<<< HEAD

@main_module_registry.register
class MainModuleCheckPlugins(MainModule):
    @property
    def mode_or_url(self):
        return "check_plugins"

    @property
    def title(self):
        return _("Check Plugins")

    @property
    def icon(self):
        return "check_plugins"

    @property
    def permission(self):
        return None

    @property
    def description(self):
        return _("Browse the catalog of all check plugins, create static checks")

    @property
    def sort_index(self):
        return 35


@main_module_registry.register
class MainModuleHostAndServiceGroups(MainModule):
    @property
    def mode_or_url(self):
        return "host_groups"

    @property
    def title(self):
        return _("Host & Service Groups")

    @property
    def icon(self):
        return "hostgroups"

    @property
    def permission(self):
        return "groups"

    @property
    def description(self):
        return _("Organize your hosts and services in groups independent of the tree structure.")

    @property
    def sort_index(self):
        return 40


@main_module_registry.register
class MainModuleUsers(MainModule):
    @property
    def mode_or_url(self):
        return "users"

    @property
    def title(self):
        return _("Users")

    @property
    def icon(self):
        return "users"

    @property
    def permission(self):
        return "users"

    @property
    def description(self):
        return _("Manage users of the monitoring system.")

    @property
    def sort_index(self):
        return 45


@main_module_registry.register
class MainModuleRoles(MainModule):
    @property
    def mode_or_url(self):
        return "roles"

    @property
    def title(self):
        return _("Roles & Permissions")

    @property
    def icon(self):
        return "roles"

    @property
    def permission(self):
        return "users"

    @property
    def description(self):
        return _("User roles are configurable sets of permissions.")

    @property
    def sort_index(self):
        return 50


@main_module_registry.register
class MainModuleContactGroups(MainModule):
    @property
    def mode_or_url(self):
        return "contact_groups"

    @property
    def title(self):
        return _("Contact Groups")

    @property
    def icon(self):
        return "contactgroups"

    @property
    def permission(self):
        return "users"

    @property
    def description(self):
        return _("Contact groups are used to assign persons to hosts and services")

    @property
    def sort_index(self):
        return 55


@main_module_registry.register
class MainModuleNotifications(MainModule):
    @property
    def mode_or_url(self):
        return "notifications"

    @property
    def title(self):
        return _("Notifications")

    @property
    def icon(self):
        return "notifications"

    @property
    def permission(self):
        return "notifications"

    @property
    def description(self):
        return _("Rules for the notification of contacts about host and service problems")

    @property
    def sort_index(self):
        return 60


@main_module_registry.register
class MainModuleTimeperiods(MainModule):
    @property
    def mode_or_url(self):
        return "timeperiods"

    @property
    def title(self):
        return _("Time Periods")

    @property
    def icon(self):
        return "timeperiods"

    @property
    def permission(self):
        return "timeperiods"

    @property
    def description(self):
        return _(
            "Timeperiods restrict notifications and other things to certain periods of the day.")

    @property
    def sort_index(self):
        return 65


@main_module_registry.register
class MainModuleSites(MainModule):
    @property
    def mode_or_url(self):
        return "sites"

    @property
    def title(self):
        return _("Distributed Monitoring")

    @property
    def icon(self):
        return "sites"

    @property
    def permission(self):
        return "sites"

    @property
    def description(self):
        return _("Distributed monitoring using multiple Check_MK sites")

    @property
    def sort_index(self):
        return 75


@main_module_registry.register
class MainModuleBackup(MainModule):
    @property
    def mode_or_url(self):
        return "backup"

    @property
    def title(self):
        return _("Backup")

    @property
    def icon(self):
        return "backup"

    @property
    def permission(self):
        return "backups"

    @property
    def description(self):
        return _("Make backups of your whole site and restore previous backups.")

    @property
    def sort_index(self):
        return 80


@main_module_registry.register
class MainModulePasswords(MainModule):
    @property
    def mode_or_url(self):
        return "passwords"

    @property
    def title(self):
        return _("Passwords")

    @property
    def icon(self):
        return "passwords"

    @property
    def permission(self):
        return "passwords"

    @property
    def description(self):
        return _("Store and share passwords for later use in checks.")

    @property
    def sort_index(self):
        return 85


@main_module_registry.register
class MainModuleAnalyzeConfig(MainModule):
    @property
    def mode_or_url(self):
        return "analyze_config"

    @property
    def title(self):
        return _("Analyze configuration")

    @property
    def icon(self):
        return "analyze_config"

    @property
    def permission(self):
        return "analyze_config"

    @property
    def description(self):
        return _("See hints how to improve your Check_MK installation")

    @property
    def sort_index(self):
        return 90


@main_module_registry.register
class MainModulePatternEditor(MainModule):
    @property
    def mode_or_url(self):
        return "pattern_editor"

    @property
    def title(self):
        return _("Logfile Pattern Analyzer")

    @property
    def icon(self):
        return "analyze"

    @property
    def permission(self):
        return "pattern_editor"

    @property
    def description(self):
        return _("Analyze logfile pattern rules and validate logfile patterns against custom text.")

    @property
    def sort_index(self):
        return 95


@main_module_registry.register
class MainModuleIcons(MainModule):
    @property
    def mode_or_url(self):
        return "icons"

    @property
    def title(self):
        return _("Custom Icons")

    @property
    def icon(self):
        return "icons"

    @property
    def permission(self):
        return "icons"

    @property
    def description(self):
        return _("Upload your own icons that can be used in views or custom actions")

    @property
    def sort_index(self):
        return 100


class MainModuleDownloadAgents(MainModule):
    @property
    def mode_or_url(self):
        return "download_agents"

    @property
    def title(self):
        return _("Monitoring Agents")

    @property
    def icon(self):
        return "download_agents"

    @property
    def permission(self):
        return "download_agents"

    @property
    def description(self):
        return _("Downloads the Check_MK monitoring agents")

    @property
    def sort_index(self):
        return 5


# Register the builtin agent download page on the top level of WATO only when the agent bakery
# does not exist (e.g. when using CRE)
if cmk.is_raw_edition():
    main_module_registry.register(MainModuleDownloadAgents)
=======
    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleHostAndServiceParameters(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'host_monconf')

    @property
    def topic(self):
        return MainModuleTopicHosts

    @property
    def title(self):
        return _("Monitoring rules")

    @property
    def icon(self):
        return {"icon": "folder", "emblem": "settings"}

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Check parameters and other configuration variables on hosts and services")

    @property
    def sort_index(self):
        return 20

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleHWSWInventory(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'inventory')

    @property
    def topic(self):
        return MainModuleTopicHosts

    @property
    def title(self):
        return _("HW/SW inventory rules")

    @property
    def icon(self):
        return "inventory"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Manage Hard- and software inventory related rulesets")

    @property
    def sort_index(self):
        return 60

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleNetworkingServices(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'activechecks')

    @property
    def topic(self):
        return MainModuleTopicServices

    @property
    def title(self):
        return _("HTTP, TCP, Email, ...")

    @property
    def icon(self):
        return "network_services"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Configure monitoring of networking services using classical nagios plugins"
                 " (so called active checks)")

    @property
    def sort_index(self):
        return 30

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleOtherServices(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'custom_checks')

    @property
    def topic(self):
        return MainModuleTopicServices

    @property
    def title(self):
        return _("Other Services")

    @property
    def icon(self):
        return "nagios"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Integrate [cms_active_checks#mrpe|custom nagios plugins] into the "
                 "monitoring as active checks.")

    @property
    def sort_index(self):
        return 40

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleCheckPlugins(ABCMainModule):
    @property
    def mode_or_url(self):
        return "check_plugins"

    @property
    def topic(self):
        return MainModuleTopicServices

    @property
    def title(self):
        return _("Catalog of check plugins")

    @property
    def icon(self):
        return "check_plugins"

    @property
    def permission(self):
        return None

    @property
    def description(self):
        return _("Browse the catalog of all check plugins, create static checks")

    @property
    def sort_index(self):
        return 70

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleHostGroups(ABCMainModule):
    @property
    def mode_or_url(self):
        return "host_groups"

    @property
    def topic(self):
        return MainModuleTopicHosts

    @property
    def title(self):
        return _("Groups")

    @property
    def icon(self):
        return "hostgroups"

    @property
    def permission(self):
        return "groups"

    @property
    def description(self):
        return _("Organize your hosts in groups independent of the tree structure.")

    @property
    def sort_index(self):
        return 50

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleHostCustomAttributes(ABCMainModule):
    @property
    def mode_or_url(self):
        return "host_attrs"

    @property
    def topic(self):
        return MainModuleTopicHosts

    @property
    def title(self):
        return _("Custom attributes")

    @property
    def icon(self):
        return "custom_attr"

    @property
    def permission(self):
        return "custom_attributes"

    @property
    def description(self):
        return _("Create your own host related attributes")

    @property
    def sort_index(self):
        return 55

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleServiceGroups(ABCMainModule):
    @property
    def mode_or_url(self):
        return "service_groups"

    @property
    def topic(self):
        return MainModuleTopicServices

    @property
    def title(self):
        return _("Groups")

    @property
    def icon(self):
        return "servicegroups"

    @property
    def permission(self):
        return "groups"

    @property
    def description(self):
        return _("Organize your services in groups")

    @property
    def sort_index(self):
        return 60

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleUsers(ABCMainModule):
    @property
    def mode_or_url(self):
        return "users"

    @property
    def topic(self):
        return MainModuleTopicUsers

    @property
    def title(self):
        return _("Users")

    @property
    def icon(self):
        return "users"

    @property
    def permission(self):
        return "users"

    @property
    def description(self):
        return _("Manage users of the monitoring system.")

    @property
    def sort_index(self):
        return 20

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleRoles(ABCMainModule):
    @property
    def mode_or_url(self):
        return "roles"

    @property
    def topic(self):
        return MainModuleTopicUsers

    @property
    def title(self):
        return _("Roles & permissions")

    @property
    def icon(self):
        return "roles"

    @property
    def permission(self):
        return "users"

    @property
    def description(self):
        return _("User roles are configurable sets of permissions.")

    @property
    def sort_index(self):
        return 40

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleLDAP(ABCMainModule):
    @property
    def mode_or_url(self):
        return "ldap_config"

    @property
    def topic(self):
        return MainModuleTopicUsers

    @property
    def title(self):
        return _("LDAP & Active Directory")

    @property
    def icon(self):
        return "roles"

    @property
    def permission(self):
        return "users"

    @property
    def description(self):
        return _("Connect Checkmk with your LDAP or Active Directory to create users in Checkmk.")

    @property
    def sort_index(self):
        return 50

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleUserCustomAttributes(ABCMainModule):
    @property
    def mode_or_url(self):
        return "user_attrs"

    @property
    def topic(self):
        return MainModuleTopicUsers

    @property
    def title(self):
        return _("Custom attributes")

    @property
    def icon(self):
        return "custom_attr"

    @property
    def permission(self):
        return "custom_attributes"

    @property
    def description(self):
        return _("Create your own user related attributes")

    @property
    def sort_index(self):
        return 55

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleContactGroups(ABCMainModule):
    @property
    def mode_or_url(self):
        return "contact_groups"

    @property
    def topic(self):
        return MainModuleTopicUsers

    @property
    def title(self):
        return _("Groups")

    @property
    def icon(self):
        return "contactgroups"

    @property
    def permission(self):
        return "users"

    @property
    def description(self):
        return _("Contact groups are used to assign users to hosts and services")

    @property
    def sort_index(self):
        return 30

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleNotifications(ABCMainModule):
    @property
    def mode_or_url(self):
        return "notifications"

    @property
    def topic(self):
        return MainModuleTopicEvents

    @property
    def title(self):
        return _("Notifications")

    @property
    def icon(self):
        return "notifications"

    @property
    def permission(self):
        return "notifications"

    @property
    def description(self):
        return _("Rules for the notification of contacts about host and service problems")

    @property
    def sort_index(self):
        return 10

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleTimeperiods(ABCMainModule):
    @property
    def mode_or_url(self):
        return "timeperiods"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Time periods")

    @property
    def icon(self):
        return "timeperiods"

    @property
    def permission(self):
        return "timeperiods"

    @property
    def description(self):
        return _(
            "Timeperiods restrict notifications and other things to certain periods of the day.")

    @property
    def sort_index(self):
        return 40

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleSites(ABCMainModule):
    @property
    def mode_or_url(self):
        return "sites"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Distributed monitoring")

    @property
    def icon(self):
        return "sites"

    @property
    def permission(self):
        return "sites"

    @property
    def description(self):
        return _("Distributed monitoring using multiple Checkmk sites")

    @property
    def sort_index(self):
        return 70

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleBackup(ABCMainModule):
    @property
    def mode_or_url(self):
        return "backup"

    @property
    def topic(self):
        return MainModuleTopicMaintenance

    @property
    def title(self):
        return _("Backups")

    @property
    def icon(self):
        return "backup"

    @property
    def permission(self):
        return "backups"

    @property
    def description(self):
        return _("Make backups of your whole site and restore previous backups.")

    @property
    def sort_index(self):
        return 10

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModulePasswords(ABCMainModule):
    @property
    def mode_or_url(self):
        return "passwords"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Passwords")

    @property
    def icon(self):
        return "passwords"

    @property
    def permission(self):
        return "passwords"

    @property
    def description(self):
        return _("Store and share passwords for later use in checks.")

    @property
    def sort_index(self):
        return 50

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleAuditLog(ABCMainModule):
    @property
    def mode_or_url(self):
        return "auditlog"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Audit log")

    @property
    def icon(self):
        return "auditlog"

    @property
    def permission(self):
        return "auditlog"

    @property
    def description(self):
        return _("Examine the change history of the configuration")

    @property
    def sort_index(self):
        return 80

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleIcons(ABCMainModule):
    @property
    def mode_or_url(self):
        return "icons"

    @property
    def topic(self):
        return MainModuleTopicGeneral

    @property
    def title(self):
        return _("Custom icons")

    @property
    def icon(self):
        return "icons"

    @property
    def permission(self):
        return "icons"

    @property
    def description(self):
        return _("Extend the Checkmk GUI with your custom icons")

    @property
    def sort_index(self):
        return 85

    @property
    def is_show_more(self):
        return True


@main_module_registry.register
class MainModuleAnalyzeConfig(ABCMainModule):
    @property
    def mode_or_url(self):
        return "analyze_config"

    @property
    def topic(self):
        return MainModuleTopicMaintenance

    @property
    def title(self):
        return _("Analyze configuration")

    @property
    def icon(self):
        return "analyze_config"

    @property
    def permission(self):
        return "analyze_config"

    @property
    def description(self):
        return _("See hints how to improve your Checkmk installation")

    @property
    def sort_index(self):
        return 40

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleReleaseNotes(ABCMainModule):
    @property
    def mode_or_url(self):
        return "version.py"

    @property
    def topic(self):
        return MainModuleTopicMaintenance

    @property
    def title(self):
        return _("Release notes")

    @property
    def icon(self):
        return "release_notes"

    @property
    def permission(self):
        return None

    @property
    def description(self):
        return _("Learn something about what changed at Checkmk.")

    @property
    def sort_index(self):
        return 60

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleDiagnostics(ABCMainModule):
    @property
    def mode_or_url(self):
        return "diagnostics"

    @property
    def topic(self):
        return MainModuleTopicMaintenance

    @property
    def title(self):
        return _("Support diagnostics")

    @property
    def icon(self):
        loc_time = time.localtime()
        if loc_time.tm_hour == 13 and loc_time.tm_min == 37:
            return "d146n0571c5"
        return "diagnostics"

    @property
    def permission(self):
        return "diagnostics"

    @property
    def description(self):
        return _("Collect information of Checkmk sites for diagnostic analysis.")

    @property
    def sort_index(self):
        return 30

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleMonitoringRules(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'monconf')

    @property
    def topic(self):
        return MainModuleTopicServices

    @property
    def title(self):
        return _("Monitoring rules")

    @property
    def icon(self):
        return {"icon": "services", "emblem": "settings"}

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Monitoring rules")

    @property
    def sort_index(self):
        return 10

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleDiscoveryRules(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'checkparams')

    @property
    def topic(self):
        return MainModuleTopicServices

    @property
    def title(self):
        return _("Discovery rules")

    @property
    def icon(self):
        return "service_discovery"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Discovery settings")

    @property
    def sort_index(self):
        return 20

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleEnforcedServices(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'static')

    @property
    def topic(self):
        return MainModuleTopicServices

    @property
    def title(self):
        return _("Enforced services")

    @property
    def icon(self):
        return "static_checks"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Configure enforced checks without using service discovery")

    @property
    def sort_index(self):
        return 25

    @property
    def is_show_more(self):
        return True


class MainModuleAgentsWindows(ABCMainModule):
    @property
    def mode_or_url(self):
        return "download_agents_windows"

    @property
    def topic(self):
        return MainModuleTopicAgents

    @property
    def title(self):
        return _("Windows")

    @property
    def icon(self):
        return "download_agents_windows"

    @property
    def permission(self):
        return "download_agents"

    @property
    def description(self):
        return _("Downloads Checkmk agent and plugins for Windows")

    @property
    def sort_index(self):
        return 15

    @property
    def is_show_more(self):
        return False


class MainModuleAgentsLinux(ABCMainModule):
    @property
    def mode_or_url(self):
        return "download_agents_linux"

    @property
    def topic(self):
        return MainModuleTopicAgents

    @property
    def title(self):
        return _("Linux")

    @property
    def icon(self):
        return "download_agents_linux"

    @property
    def permission(self):
        return "download_agents"

    @property
    def description(self):
        return _("Downloads Checkmk agent and plugins for Linux")

    @property
    def sort_index(self):
        return 10

    @property
    def is_show_more(self):
        return False


# Register the builtin agent download page on the top level of WATO only when the agent bakery
# does not exist (e.g. when using CRE)
if cmk_version.is_raw_edition():
    main_module_registry.register(MainModuleAgentsWindows)
    main_module_registry.register(MainModuleAgentsLinux)


@main_module_registry.register
class MainModuleOtherAgents(ABCMainModule):
    @property
    def mode_or_url(self):
        return "download_agents"

    @property
    def topic(self):
        return MainModuleTopicAgents

    @property
    def title(self):
        return _("Other operating systems")

    @property
    def icon(self):
        return "os_other"

    @property
    def permission(self):
        return "download_agents"

    @property
    def description(self):
        return _("Downloads Checkmk agents for other operating systems")

    @property
    def sort_index(self):
        return 20

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleAgentAccessRules(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'agent')

    @property
    def topic(self):
        return MainModuleTopicAgents

    @property
    def title(self):
        return _("Agent access rules")

    @property
    def icon(self):
        return {"icon": "agents", "emblem": "settings"}

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Configure agent access related settings using rulesets")

    @property
    def sort_index(self):
        return 60

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleSNMPRules(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'snmp')

    @property
    def topic(self):
        return MainModuleTopicAgents

    @property
    def title(self):
        return _("SNMP rules")

    @property
    def icon(self):
        return "snmp"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Configure SNMP related settings using rulesets")

    @property
    def sort_index(self):
        return 70

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleVMCloudContainer(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'vm_cloud_container')

    @property
    def topic(self):
        return MainModuleTopicAgents

    @property
    def title(self):
        return _("VM, Cloud, Container")

    @property
    def icon(self):
        return "cloud"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Integrate with VM, cloud or container platforms")

    @property
    def sort_index(self):
        return 30

    @property
    def is_show_more(self):
        return False


@main_module_registry.register
class MainModuleOtherIntegrations(ABCMainModule):
    @property
    def mode_or_url(self):
        return makeuri_contextless_ruleset_group(request, 'datasource_programs')

    @property
    def topic(self):
        return MainModuleTopicAgents

    @property
    def title(self):
        return _("Other integrations")

    @property
    def icon(self):
        return "integrations_other"

    @property
    def permission(self):
        return "rulesets"

    @property
    def description(self):
        return _("Monitoring of applications such as processes, services or databases")

    @property
    def sort_index(self):
        return 40

    @property
    def is_show_more(self):
        return False
>>>>>>> upstream/master
