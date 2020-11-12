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

import cmk.gui.config as config
from cmk.gui.i18n import _
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import cmk.gui.config as config
from cmk.gui.i18n import _, _l
>>>>>>> upstream/master
from cmk.gui.permissions import (
    permission_section_registry,
    PermissionSection,
    permission_registry,
    Permission,
)

#   .----------------------------------------------------------------------.
#   |        ____                     _         _                          |
<<<<<<< HEAD
#   |       |  _ \ ___ _ __ _ __ ___ (_)___ ___(_) ___  _ __  ___          |
=======
#   |       |  _ \ ___ _ __ _ __ ___ (_)___ ___l(_) ___  _ __  ___          |
>>>>>>> upstream/master
#   |       | |_) / _ \ '__| '_ ` _ \| / __/ __| |/ _ \| '_ \/ __|         |
#   |       |  __/  __/ |  | | | | | | \__ \__ \ | (_) | | | \__ \         |
#   |       |_|   \___|_|  |_| |_| |_|_|___/___/_|\___/|_| |_|___/         |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Declare general permissions for Multisite                            |
#   '----------------------------------------------------------------------'


@permission_section_registry.register
class PermissionSectionGeneral(PermissionSection):
    @property
    def name(self):
        return "general"

    @property
    def title(self):
        return _('General Permissions')

    @property
    def sort_index(self):
        return 10


<<<<<<< HEAD
@permission_registry.register
class PermissionGeneralUse(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "use"

    @property
    def title(self):
        return _("Use the GUI at all")

    @property
    def description(self):
        return _("Users without this permission are not let in at all")

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralSeeAll(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "see_all"

    @property
    def title(self):
        return _("See all host and services")

    @property
    def description(self):
        return _("See all objects regardless of contacts and contact groups. "
                 "If combined with 'perform commands' then commands may be done on all objects.")

    @property
    def defaults(self):
        return ["admin", "guest"]


@permission_registry.register
class PermissionGeneralChangeViewDisplayColumns(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "view_option_columns"

    @property
    def title(self):
        return _("Change view display columns")

    @property
    def description(self):
        return _(
            "Interactively change the number of columns being displayed by a view (does not edit or customize the view)"
        )

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralChangeViewColumns(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "view_option_refresh"

    @property
    def title(self):
        return _("Change view display refresh")

    @property
    def description(self):
        return _(
            "Interactively change the automatic browser reload of a view being displayed (does not edit or customize the view)"
        )

    @property
    def defaults(self):
        return ["admin", "user"]


@permission_registry.register
class PermissionGeneralChangeViewPainterOptions(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "painter_options"

    @property
    def title(self):
        return _("Change column display options")

    @property
    def description(self):
        return _("Some of the display columns offer options for customizing their output. "
                 "For example time stamp columns can be displayed absolute, relative or "
                 "in a mixed style. This permission allows the user to modify display options")

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralPerformCommands(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "act"

    @property
    def title(self):
        return _("Perform commands in views")

    @property
    def description(self):
        return _(
            "Allows users to perform commands on hosts and services in the views. If "
            "no further permissions are granted, actions can only be done on objects one is a contact for"
        )

    @property
    def defaults(self):
        return ["admin", "user"]


@permission_registry.register
class PermissionGeneralSeeSidebar(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "see_sidebar"

    @property
    def title(self):
        return _("Use Check_MK sidebar")

    @property
    def description(self):
        return _("Without this permission the Check_MK sidebar will be invisible")

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralConfigureSidebar(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "configure_sidebar"

    @property
    def title(self):
        return _("Configure sidebar")

    @property
    def description(self):
        return _("This allows the user to add, move and remove sidebar snapins.")

    @property
    def defaults(self):
        return ["admin", "user"]


@permission_registry.register
class PermissionGeneralEditProfile(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "edit_profile"

    @property
    def title(self):
        return _('Edit the user profile')

    @property
    def description(self):
        return _('Permits the user to change the user profile settings.')

    @property
    def defaults(self):
        return ["admin", "user"]


@permission_registry.register
class PermissionGeneralSeeAvailability(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "see_availability"

    @property
    def title(self):
        return _("See the availability")

    @property
    def description(self):
        return _("See the availability views of hosts and services")

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralCSVExport(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "csv_export"

    @property
    def title(self):
        return _("Use CSV export")

    @property
    def description(self):
        return _("Export data of views using the CSV export")

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralEditNotifications(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "edit_notifications"

    @property
    def title(self):
        return _('Edit personal notification settings')

    @property
    def description(self):
        return _(
            'This allows a user to edit his personal notification settings. You also need the permission '
            '<i>Edit the user profile</i> in order to do this.')

    @property
    def defaults(self):
        return ['admin', 'user']


@permission_registry.register
class PermissionGeneralDisableNotifications(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "disable_notifications"

    @property
    def title(self):
        return _('Disable all personal notifications')

    @property
    def description(self):
        return _(
            'This permissions provides a checkbox and timerange in the personal settings of the user that '
            'allows him to completely disable all of his notifications. Use with caution.')

    @property
    def defaults(self):
        return ['admin']


@permission_registry.register
class PermissionGeneralEditUserAttributes(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "edit_user_attributes"

    @property
    def title(self):
        return _('Edit personal user attributes')

    @property
    def description(self):
        return _(
            'This allows a user to edit his personal user attributes. You also need the permission '
            '<i>Edit the user profile</i> in order to do this.')

    @property
    def defaults(self):
        return ['admin', 'user']


@permission_registry.register
class PermissionGeneralChangePassword(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "change_password"

    @property
    def title(self):
        return _('Edit the user password')

    @property
    def description(self):
        return _('Permits the user to change the password.')

    @property
    def defaults(self):
        return ['admin', 'user']


@permission_registry.register
class PermissionGeneralLogout(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "logout"

    @property
    def title(self):
        return _('Logout')

    @property
    def description(self):
        return _('Permits the user to logout.')

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralIgnoreSoftLimit(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "ignore_soft_limit"

    @property
    def title(self):
        return _("Ignore soft query limit")

    @property
    def description(self):
        return _(
            "Allows to ignore the soft query limit imposed upon the number of datasets returned by a query"
        )

    @property
    def defaults(self):
        return ["admin", "user"]


@permission_registry.register
class PermissionGeneralIgnoreHardLimit(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "ignore_hard_limit"

    @property
    def title(self):
        return _("Ignore hard query limit")

    @property
    def description(self):
        return _(
            "Allows to ignore the hard query limit imposed upon the number of datasets returned by a query"
        )

    @property
    def defaults(self):
        return ["admin"]


@permission_registry.register
class PermissionGeneralAcknowledgeWerks(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "acknowledge_werks"

    @property
    def title(self):
        return _("Acknowledge Incompatible Werks")

    @property
    def description(self):
        return _(
            "In the change log of the Check_MK software version the administrator can manage change log entries "
            "(Werks) that requrire user interaction. These <i>incompatible Werks</i> can be acknowledged only "
            "if the user has this permission.")

    @property
    def defaults(self):
        return ["admin"]


@permission_registry.register
class PermissionGeneralSeeFailedNotifications24h(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "see_failed_notifications_24h"

    @property
    def title(self):
        return _("See failed Notifications (last 24 hours)")

    @property
    def description(self):
        return _(
            "If Check_MK is unable to notify users about problems, the site will warn about this situation "
            "very visibly inside the UI (both in the Tactical Overview and the Dashboard). This affects only "
            "users with this permission. Users with this permission will only see failed notifications "
            "that occured within the last 24 hours.")

    @property
    def defaults(self):
        return ["user"]


@permission_registry.register
class PermissionGeneralSeeFailedNotifications(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "see_failed_notifications"

    @property
    def title(self):
        return _("See failed Notifications (all)")

    @property
    def description(self):
        return _(
            "If Check_MK is unable to notify users about problems, the site will warn about this situation "
            "very visibly inside the UI (both in the Tactical Overview and the Dashboard). This affects only "
            "users with this permission. Users with this permission will see failed notifications between now "
            "and the configured <a href=\"wato.py?mode=edit_configvar&varname=failed_notification_horizon\">Failed notification horizon</a>."
        )

    @property
    def defaults(self):
        return ["admin"]


@permission_registry.register
class PermissionGeneralSeeStalesInTacticalOverview(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "see_stales_in_tactical_overview"

    @property
    def title(self):
        return _("See stale objects in tactical overview snapin")

    @property
    def description(self):
        return _(
            "Show the column for stale host and service checks in the tactical overview snapin.")

    @property
    def defaults(self):
        return config.builtin_role_ids


@permission_registry.register
class PermissionGeneralSeeCrashReports(Permission):
    @property
    def section(self):
        return PermissionSectionGeneral

    @property
    def permission_name(self):
        return "see_crash_reports"

    @property
    def title(self):
        return _("See crash reports")

    @property
    def description(self):
        return _(
            "In case an exception happens while Check_MK is running it may produce crash reports that you can "
            "use to track down the issues in the code or send it as report to the Check_MK team to fix this issue "
            "Only users with this permission are able to see the reports in the GUI.")

    @property
    def defaults(self):
        return ["admin"]
=======
PermissionGeneralUse = permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="use",
        title=_l("Use the GUI at all"),
        description=_l("Users without this permission are not let in at all"),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="see_all",
        title=_l("See all host and services"),
        description=_l(
            "See all objects regardless of contacts and contact groups. "
            "If combined with 'perform commands' then commands may be done on all objects."),
        defaults=["admin", "guest"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="view_option_columns",
        title=_l("Change view display columns"),
        description=_l(
            "Interactively change the number of columns being displayed by a view (does not edit or customize the view)"
        ),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="view_option_refresh",
        title=_l("Change view display refresh"),
        description=_l(
            "Interactively change the automatic browser reload of a view being displayed (does not edit or customize the view)"
        ),
        defaults=["admin", "user"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="painter_options",
        title=_l("Change column display options"),
        description=_l(
            "Some of the display columns offer options for customizing their output. "
            "For example time stamp columns can be displayed absolute, relative or "
            "in a mixed style. This permission allows the user to modify display options"),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="act",
        title=_l("Perform commands in views"),
        description=_l(
            "Allows users to perform commands on hosts and services in the views. If "
            "no further permissions are granted, actions can only be done on objects one is a contact for"
        ),
        defaults=["admin", "user"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="see_sidebar",
        title=_l("Use Checkmk sidebar"),
        description=_l("Without this permission the Checkmk sidebar will be invisible"),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="configure_sidebar",
        title=_l("Configure sidebar"),
        description=_l("This allows the user to add, move and remove sidebar snapins."),
        defaults=["admin", "user"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="edit_profile",
        title=_l('Edit the user profile'),
        description=_l('Permits the user to change the user profile settings.'),
        defaults=["admin", "user"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="see_availability",
        title=_l("See the availability"),
        description=_l("See the availability views of hosts and services"),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="csv_export",
        title=_l("Use CSV export"),
        description=_l("Export data of views using the CSV export"),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="edit_notifications",
        title=_l('Edit personal notification settings'),
        description=_l(
            'This allows a user to edit his personal notification settings. You also need the permission '
            '<i>Edit the user profile</i> in order to do this.'),
        defaults=['admin', 'user'],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="disable_notifications",
        title=_l('Disable all personal notifications'),
        description=_l(
            'This permissions provides a checkbox and timerange in the personal settings of the user that '
            'allows him to completely disable all of his notifications. Use with caution.'),
        defaults=['admin'],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="edit_user_attributes",
        title=_l('Edit personal user attributes'),
        description=_l(
            'This allows a user to edit his personal user attributes. You also need the permission '
            '<i>Edit the user profile</i> in order to do this.'),
        defaults=['admin', 'user'],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="change_password",
        title=_l('Edit the user password'),
        description=_l('Permits the user to change the password.'),
        defaults=['admin', 'user'],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="logout",
        title=_l('Logout'),
        description=_l('Permits the user to logout.'),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="ignore_soft_limit",
        title=_l("Ignore soft query limit"),
        description=_l(
            "Allows to ignore the soft query limit imposed upon the number of datasets returned by a query"
        ),
        defaults=["admin", "user"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="ignore_hard_limit",
        title=_l("Ignore hard query limit"),
        description=_l(
            "Allows to ignore the hard query limit imposed upon the number of datasets returned by a query"
        ),
        defaults=["admin"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="acknowledge_werks",
        title=_l("Acknowledge Incompatible Werks"),
        description=_l(
            "In the change log of the Checkmk software version the administrator can manage change log entries "
            "(Werks) that requrire user interaction. These <i>incompatible Werks</i> can be acknowledged only "
            "if the user has this permission."),
        defaults=["admin"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="see_failed_notifications_24h",
        title=_l("See failed Notifications (last 24 hours)"),
        description=
        _l("If Checkmk is unable to notify users about problems, the site will warn about this situation "
           "very visibly inside the UI (both in the Tactical Overview and the Dashboard). This affects only "
           "users with this permission. Users with this permission will only see failed notifications "
           "that occured within the last 24 hours."),
        defaults=["user"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="see_failed_notifications",
        title=_l("See failed Notifications (all)"),
        description=
        _l("If Checkmk is unable to notify users about problems, the site will warn about this situation "
           "very visibly inside the UI (both in the Tactical Overview and the Dashboard). This affects only "
           "users with this permission. Users with this permission will see failed notifications between now "
           "and the configured <a href=\"wato.py?mode=edit_configvar&varname=failed_notification_horizon\">Failed notification horizon</a>."
          ),
        defaults=["admin"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="see_stales_in_tactical_overview",
        title=_l("See stale objects in tactical overview snapin"),
        description=_l(
            "Show the column for stale host and service checks in the tactical overview snapin."),
        defaults=config.builtin_role_ids,
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="see_crash_reports",
        title=_l("See crash reports"),
        description=_l(
            "In case an exception happens while Checkmk is running it may produce crash reports that you can "
            "use to track down the issues in the code or send it as report to the Checkmk team to fix this issue "
            "Only users with this permission are able to see the reports in the GUI."),
        defaults=["admin"],
    ))

permission_registry.register(
    Permission(
        section=PermissionSectionGeneral,
        name="parent_child_topology",
        title=_l("Network Topology"),
        description=_l("This dashboard uses the parent relationships of your hosts to "
                       "display a hierarchical map."),
        defaults=config.builtin_role_ids,
    ))
>>>>>>> upstream/master
