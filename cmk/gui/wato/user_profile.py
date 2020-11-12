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
"""Page user can change several aspects of it's own profile"""

import time
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Page user can change several aspects of it's own profile"""

import time
import abc
from typing import Iterator, List, Optional, Union
from cmk.utils.type_defs import UserId
>>>>>>> upstream/master

import cmk.gui.i18n
import cmk.gui.sites
import cmk.gui.userdb as userdb
import cmk.gui.config as config
import cmk.gui.watolib as watolib
import cmk.gui.forms as forms
import cmk.gui.login as login
<<<<<<< HEAD
from cmk.gui.plugins.userdb.htpasswd import hash_password
from cmk.gui.exceptions import HTTPRedirect, MKUserError, MKGeneralException, MKAuthException
from cmk.gui.i18n import _, _u
from cmk.gui.globals import html
from cmk.gui.pages import page_registry, AjaxPage
=======

from cmk.gui.breadcrumb import make_simple_page_breadcrumb
from cmk.gui.main_menu import mega_menu_registry
from cmk.gui.type_defs import MegaMenu, TopicMenuItem, TopicMenuTopic
from cmk.gui.config import SiteId, SiteConfiguration
from cmk.gui.plugins.userdb.htpasswd import hash_password
from cmk.gui.plugins.userdb.utils import get_user_attributes_by_topic
from cmk.gui.exceptions import HTTPRedirect, MKUserError, MKGeneralException, MKAuthException
from cmk.gui.i18n import _, _l, _u
from cmk.gui.globals import html, request as global_request
from cmk.gui.pages import page_registry, AjaxPage, Page
from cmk.gui.page_menu import (
    PageMenu,
    PageMenuDropdown,
    PageMenuTopic,
    PageMenuEntry,
    make_simple_link,
    make_simple_form_page_menu,
)
>>>>>>> upstream/master

from cmk.gui.watolib.changes import add_change
from cmk.gui.watolib.activate_changes import ACTIVATION_TIME_PROFILE_SYNC
from cmk.gui.wato.pages.users import select_language

<<<<<<< HEAD
from cmk.gui.watolib.user_profile import push_user_profiles_to_site_transitional_wrapper


def user_profile_async_replication_page():
    html.header(_('Replicate new User Profile'))

    html.begin_context_buttons()
    html.context_button(_('User Profile'), 'user_profile.py', 'back')
    html.end_context_buttons()

    sites = config.user.authorized_login_sites().keys()
=======
from cmk.gui.watolib.global_settings import rulebased_notifications_enabled
from cmk.gui.watolib.user_profile import push_user_profiles_to_site_transitional_wrapper

from cmk.gui.utils.urls import makeuri


def _get_current_theme_titel() -> str:
    return [titel for theme_id, titel in config.theme_choices() if theme_id == html.get_theme()][0]


def _get_sidebar_position() -> str:
    assert config.user.id is not None
    sidebar_position = userdb.load_custom_attr(config.user.id, 'ui_sidebar_position', lambda x: None
                                               if x == "None" else "left")

    return _get_sidebar_position_title(sidebar_position or "right")


def _get_sidebar_position_title(value: str) -> str:
    return {
        "left": _("left"),
        "right": _("right"),
    }[value]


def _user_menu_topics() -> List[TopicMenuTopic]:
    quick_items = [
        TopicMenuItem(
            name="ui_theme",
            title=_("Interface theme"),
            url="javascript:cmk.sidebar.toggle_user_attribute(\"ajax_ui_theme.py\")",
            target="",
            sort_index=10,
            icon="color_mode",
            button_title=_get_current_theme_titel(),
        ),
        TopicMenuItem(
            name="sidebar_position",
            title=_("Sidebar position"),
            url="javascript:cmk.sidebar.toggle_user_attribute(\"ajax_sidebar_position.py\")",
            target="",
            sort_index=20,
            icon="sidebar_position",
            button_title=_get_sidebar_position(),
        ),
    ]

    items = [
        TopicMenuItem(
            name="change_password",
            title=_("Change password"),
            url="user_change_pw.py",
            sort_index=10,
            icon="topic_change_password",
        ),
        TopicMenuItem(
            name="user_profile",
            title=_("Edit profile"),
            url="user_profile.py",
            sort_index=20,
            icon="topic_profile",
        ),
        TopicMenuItem(
            name="logout",
            title=_("Logout"),
            url="logout.py",
            sort_index=30,
            icon="sidebar_logout",
        ),
    ]

    if rulebased_notifications_enabled() and config.user.may('general.edit_notifications'):
        items.insert(
            1,
            TopicMenuItem(
                name="notification_rules",
                title=_("Notification rules"),
                url="wato.py?mode=user_notifications_p",
                sort_index=30,
                icon="topic_events",
            ))

    return [
        TopicMenuTopic(
            name="user",
            title=_("Quick toggle"),
            # TODO(rb): set correct icon
            icon="topic_profile",
            items=quick_items,
        ),
        TopicMenuTopic(
            name="user",
            title=_("Profile"),
            icon="topic_profile",
            items=items,
        )
    ]


mega_menu_registry.register(
    MegaMenu(
        name="user",
        title=_l("User"),
        icon="main_user",
        sort_index=20,
        topics=_user_menu_topics,
    ))


@page_registry.register_page("ajax_ui_theme")
class ModeAjaxCycleThemes(AjaxPage):
    """AJAX handler for quick access option 'Interface theme" in user menu"""
    def page(self):
        themes = [theme for theme, _title in cmk.gui.config.theme_choices()]
        current_theme = html.get_theme()
        try:
            theme_index = themes.index(current_theme)
        except ValueError:
            raise MKUserError(None, _("Could not determine current theme."))

        if len(themes) == theme_index + 1:
            new_theme = themes[0]
        else:
            new_theme = themes[theme_index + 1]

        _set_user_attribute("ui_theme", new_theme)


@page_registry.register_page("ajax_sidebar_position")
class ModeAjaxCycleSidebarPosition(AjaxPage):
    """AJAX handler for quick access option 'Sidebar position" in user menu"""
    def page(self):
        _set_user_attribute("ui_sidebar_position",
                            None if _get_sidebar_position() == "left" else "left")


def _set_user_attribute(key: str, value: Optional[str]):
    assert config.user.id is not None
    user_id = config.user.id

    if value is None:
        userdb.remove_custom_attr(user_id, key)
    else:
        userdb.save_custom_attr(user_id, key, value)


def user_profile_async_replication_page() -> None:
    sites = list(config.user.authorized_login_sites().keys())
>>>>>>> upstream/master
    user_profile_async_replication_dialog(sites=sites)

    html.footer()


<<<<<<< HEAD
def user_profile_async_replication_dialog(sites):
=======
def user_profile_async_replication_dialog(sites: List[SiteId]) -> None:
>>>>>>> upstream/master
    html.p(
        _('In order to activate your changes available on all remote sites, your user profile needs '
          'to be replicated to the remote sites. This is done on this page now. Each site '
          'is being represented by a single image which is first shown gray and then fills '
          'to green during synchronisation.'))

    html.h3(_('Replication States'))
    html.open_div(id_="profile_repl")
    num_replsites = 0
    for site_id in sites:
        site = config.sites[site_id]
<<<<<<< HEAD
        if not "secret" in site:
=======
        if "secret" not in site:
>>>>>>> upstream/master
            status_txt = _('Not logged in.')
            start_sync = False
            icon = 'repl_locked'
        else:
            status_txt = _('Waiting for replication to start')
            start_sync = True
            icon = 'repl_pending'

        html.open_div(class_="site", id_="site-%s" % site_id)
        html.div("", title=status_txt, class_=["icon", "repl_status", icon])
        if start_sync:
            changes_manager = watolib.ActivateChanges()
            changes_manager.load()
            estimated_duration = changes_manager.get_activation_time(site_id,
                                                                     ACTIVATION_TIME_PROFILE_SYNC,
                                                                     2.0)
            html.javascript(
                'cmk.profile_replication.start(\'%s\', %d, \'%s\');' %
                (site_id, int(estimated_duration * 1000.0), _('Replication in progress')))
            num_replsites += 1
        else:
            _add_profile_replication_change(site_id, status_txt)
        html.span(site.get('alias', site_id))

        html.close_div()

    html.javascript('cmk.profile_replication.prepare(%d);\n' % num_replsites)

    html.close_div()


<<<<<<< HEAD
def _add_profile_replication_change(site_id, result):
=======
def _add_profile_replication_change(site_id: SiteId, result: Union[bool, str]) -> None:
>>>>>>> upstream/master
    """Add pending change entry to make sync possible later for admins"""
    add_change("edit-users",
               _('Profile changed (sync failed: %s)') % result,
               sites=[site_id],
               need_restart=False)


<<<<<<< HEAD
@cmk.gui.pages.register("user_change_pw")
def page_change_own_password():
    _show_page_user_profile(change_pw=True)


@cmk.gui.pages.register("user_profile")
def page_user_profile():
    _show_page_user_profile(change_pw=False)


# TODO: Refactor this to page classes
def _show_page_user_profile(change_pw):
    start_async_replication = False

    if not config.user.id:
        raise MKUserError(None, _('Not logged in.'))

    if not config.user.may('general.edit_profile') and not config.user.may(
            'general.change_password'):
        raise MKAuthException(_("You are not allowed to edit your user profile."))

    if not config.wato_enabled:
        raise MKAuthException(_('User profiles can not be edited (WATO is disabled).'))

    success = None
    if html.request.has_var('_save') and html.check_transaction():
        users = userdb.load_users(lock=True)

        try:
            # Profile edit (user options like language etc.)
            if config.user.may('general.edit_profile'):
                if not change_pw:
                    set_lang = html.get_checkbox('_set_lang')
                    language = html.request.var('language')
                    # Set the users language if requested
                    if set_lang:
                        if language == '':
                            language = None
                        # Set custom language
                        users[config.user.id]['language'] = language
                        config.user.set_attribute("language", language)
                        html.set_language_cookie(language)

                    else:
                        # Remove the customized language
                        if 'language' in users[config.user.id]:
                            del users[config.user.id]['language']
                        config.user.unset_attribute("language")

                    # load the new language
                    cmk.gui.i18n.localize(config.user.language())

                    user = users.get(config.user.id)
                    if config.user.may('general.edit_notifications') and user.get(
                            "notifications_enabled"):
                        value = forms.get_input(watolib.get_vs_flexible_notifications(),
                                                "notification_method")
                        users[config.user.id]["notification_method"] = value

                    # Custom attributes
                    if config.user.may('general.edit_user_attributes'):
                        for name, attr in userdb.get_user_attributes():
                            if attr.user_editable():
                                if not attr.permission() or config.user.may(attr.permission()):
                                    vs = attr.valuespec()
                                    value = vs.from_html_vars('ua_' + name)
                                    vs.validate_value(value, "ua_" + name)
                                    users[config.user.id][name] = value

            # Change the password if requested
            password_changed = False
            if config.user.may('general.change_password'):
                cur_password = html.request.var('cur_password')
                password = html.request.var('password')
                password2 = html.request.var('password2', '')

                if change_pw:
                    # Force change pw mode
                    if not cur_password:
                        raise MKUserError("cur_password",
                                          _("You need to provide your current password."))
                    if not password:
                        raise MKUserError("password", _("You need to change your password."))
                    if cur_password == password:
                        raise MKUserError("password",
                                          _("The new password must differ from your current one."))

                if cur_password and password:
                    if userdb.hook_login(config.user.id, cur_password) in [None, False]:
                        raise MKUserError("cur_password", _("Your old password is wrong."))
                    if password2 and password != password2:
                        raise MKUserError("password2", _("The both new passwords do not match."))

                    watolib.verify_password_policy(password)
                    users[config.user.id]['password'] = hash_password(password)
                    users[config.user.id]['last_pw_change'] = int(time.time())

                    if change_pw:
                        # Has been changed, remove enforcement flag
                        del users[config.user.id]['enforce_pw_change']

                    # Increase serial to invalidate old cookies
                    if 'serial' not in users[config.user.id]:
                        users[config.user.id]['serial'] = 1
                    else:
                        users[config.user.id]['serial'] += 1

                    password_changed = True

            # Now, if in distributed environment where users can login to remote sites,
            # set the trigger for pushing the new auth information to the slave sites
            # asynchronous
            if config.user.authorized_login_sites():
                start_async_replication = True

            userdb.save_users(users)

            if password_changed:
                # Set the new cookie to prevent logout for the current user
                login.set_auth_cookie(config.user.id)

            success = True
        except MKUserError as e:
            html.add_user_error(e.varname, e)
    else:
        users = userdb.load_users()

    watolib.init_wato_datastructures(with_wato_lock=True)

    # When in distributed setup, display the replication dialog instead of the normal
    # profile edit dialog after changing the password.
    if start_async_replication:
        user_profile_async_replication_page()
        return

    if change_pw:
        title = _("Change Password")
    else:
        title = _("Edit User Profile")

    html.header(title)

    # Rule based notifications: The user currently cannot simply call the according
    # WATO module due to WATO permission issues. So we cannot show this button
    # right now.
    if not change_pw:
        rulebased_notifications = watolib.load_configuration_settings().get(
            "enable_rulebased_notifications")
        if rulebased_notifications and config.user.may('general.edit_notifications'):
            html.begin_context_buttons()
            url = "wato.py?mode=user_notifications_p"
            html.context_button(_("Notifications"), url, "notifications")
            html.end_context_buttons()
    else:
        reason = html.request.var('reason')
        if reason == 'expired':
            html.p(_('Your password is too old, you need to choose a new password.'))
        else:
            html.p(_('You are required to change your password before proceeding.'))

    if success:
        html.reload_sidebar()
        if change_pw:
            html.message(_("Your password has been changed."))
            raise HTTPRedirect(html.request.var('_origtarget', 'index.py'))
        else:
            html.message(_("Successfully updated user profile."))
            # Ensure theme changes are applied without additional user interaction
            html.immediate_browser_redirect(0.5, html.makeuri([]))

    if html.has_user_errors():
        html.show_user_errors()

    user = users.get(config.user.id)
    if user is None:
        html.show_warning(_("Sorry, your user account does not exist."))
        html.footer()
        return

    # Returns true if an attribute is locked and should be read only. Is only
    # checked when modifying an existing user
    locked_attributes = userdb.locked_attributes(user.get('connector'))

    def is_locked(attr):
        return attr in locked_attributes

    html.begin_form("profile", method="POST")
    html.prevent_password_auto_completion()
    html.open_div(class_="wato")
    forms.header(_("Personal Settings"))

    if not change_pw:
        forms.section(_("Name"), simple=True)
        html.write_text(user.get("alias", config.user.id))

    if config.user.may('general.change_password') and not is_locked('password'):
=======
class ABCUserProfilePage(Page):
    @abc.abstractmethod
    def _page_title(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def _action(self) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def _show_form(self, profile_changed: bool) -> None:
        raise NotImplementedError()

    def __init__(self, permission: str) -> None:
        super().__init__()
        self._verify_requirements(permission)

    @staticmethod
    def _verify_requirements(permission: str) -> None:
        if not config.user.id:
            raise MKUserError(None, _('Not logged in.'))

        if not config.user.may(permission):
            raise MKAuthException(_("You are not allowed to edit your user profile."))

        if not config.wato_enabled:
            raise MKAuthException(_('User profiles can not be edited (WATO is disabled).'))

    def _page_menu(self, breadcrumb) -> PageMenu:
        menu = make_simple_form_page_menu(breadcrumb, form_name="profile", button_name="_save")
        menu.dropdowns.insert(1, page_menu_dropdown_user_related(html.myfile))
        return menu

    def page(self) -> None:
        watolib.init_wato_datastructures(with_wato_lock=True)

        profile_changed = False
        if html.request.has_var('_save') and html.check_transaction():
            try:
                profile_changed = self._action()
            except MKUserError as e:
                html.add_user_error(e.varname, e)

        if profile_changed and config.user.authorized_login_sites():
            title = _('Replicate new user profile')
        else:
            title = self._page_title()

        breadcrumb = make_simple_page_breadcrumb(mega_menu_registry.menu_user(), title)
        html.header(title, breadcrumb, self._page_menu(breadcrumb))

        # Now, if in distributed environment where users can login to remote sites, set the trigger for
        # pushing the new user profile to the remote sites asynchronously
        if profile_changed and config.user.authorized_login_sites():
            user_profile_async_replication_page()
            return

        self._show_form(profile_changed)


@page_registry.register_page("user_change_pw")
class UserChangePasswordPage(ABCUserProfilePage):
    def _page_title(self) -> str:
        return _("Change password")

    def __init__(self) -> None:
        super().__init__("general.change_password")

    def _action(self) -> bool:
        assert config.user.id is not None

        users = userdb.load_users(lock=True)
        user = users[config.user.id]

        cur_password = html.request.get_str_input_mandatory('cur_password')
        password = html.request.get_str_input_mandatory('password')
        password2 = html.request.get_str_input_mandatory('password2', '')

        # Force change pw mode
        if not cur_password:
            raise MKUserError("cur_password", _("You need to provide your current password."))

        if not password:
            raise MKUserError("password", _("You need to change your password."))

        if cur_password == password:
            raise MKUserError("password", _("The new password must differ from your current one."))

        if userdb.check_credentials(config.user.id, cur_password) is False:
            raise MKUserError("cur_password", _("Your old password is wrong."))

        if password2 and password != password2:
            raise MKUserError("password2", _("The both new passwords do not match."))

        watolib.verify_password_policy(password)
        user['password'] = hash_password(password)
        user['last_pw_change'] = int(time.time())

        # In case the user was enforced to change it's password, remove the flag
        try:
            del user['enforce_pw_change']
        except KeyError:
            pass

        # Increase serial to invalidate old authentication cookies
        if 'serial' not in user:
            user['serial'] = 1
        else:
            user['serial'] += 1

        userdb.save_users(users)

        # Set the new cookie to prevent logout for the current user
        login.update_auth_cookie(config.user.id)

        return True

    def _show_form(self, profile_changed: bool) -> None:
        assert config.user.id is not None

        users = userdb.load_users()

        change_reason = html.request.get_ascii_input('reason')

        if change_reason == 'expired':
            html.p(_('Your password is too old, you need to choose a new password.'))
        elif change_reason == 'enforced':
            html.p(_('You are required to change your password before proceeding.'))

        if profile_changed:
            html.show_message(_("Your password has been changed."))
            if change_reason:
                raise HTTPRedirect(html.request.get_str_input_mandatory('_origtarget', 'index.py'))

        if html.has_user_errors():
            html.show_user_errors()

        user = users.get(config.user.id)
        if user is None:
            html.show_warning(_("Sorry, your user account does not exist."))
            html.footer()
            return

        locked_attributes = userdb.locked_attributes(user.get('connector'))
        if "password" in locked_attributes:
            raise MKUserError(
                "cur_password",
                _("You can not change your password, because it is "
                  "managed by another system."))

        html.begin_form("profile", method="POST")
        html.prevent_password_auto_completion()
        html.open_div(class_="wato")
        forms.header(self._page_title())

>>>>>>> upstream/master
        forms.section(_("Current Password"))
        html.password_input('cur_password', autocomplete="new-password")

        forms.section(_("New Password"))
        html.password_input('password', autocomplete="new-password")

        forms.section(_("New Password Confirmation"))
        html.password_input('password2', autocomplete="new-password")

<<<<<<< HEAD
    if not change_pw and config.user.may('general.edit_profile'):
        select_language(user)

        # Let the user configure how he wants to be notified
        if not rulebased_notifications \
            and config.user.may('general.edit_notifications') \
            and user.get("notifications_enabled"):
=======
        forms.end()
        html.close_div()
        html.hidden_fields()
        html.end_form()
        html.footer()


@page_registry.register_page("user_profile")
class UserProfile(ABCUserProfilePage):
    def _page_title(self) -> str:
        return _("Edit profile")

    def __init__(self) -> None:
        super().__init__("general.edit_profile")

    def _action(self) -> bool:
        assert config.user.id is not None

        users = userdb.load_users(lock=True)
        user = users[config.user.id]

        language = html.request.get_ascii_input_mandatory('language', "")
        # Set the users language if requested to set it explicitly
        if language != "_default_":
            user['language'] = language
            config.user.language = language
            html.set_language_cookie(language)

        else:
            if 'language' in user:
                del user['language']
            config.user.reset_language()

        # load the new language
        cmk.gui.i18n.localize(config.user.language)

        if config.user.may('general.edit_notifications') and user.get("notifications_enabled"):
            value = forms.get_input(watolib.get_vs_flexible_notifications(), "notification_method")
            user["notification_method"] = value

        # Custom attributes
        if config.user.may('general.edit_user_attributes'):
            for name, attr in userdb.get_user_attributes():
                if not attr.user_editable():
                    continue

                if attr.permission() and not config.user.may(attr.permission()):
                    continue

                vs = attr.valuespec()
                value = vs.from_html_vars('ua_' + name)
                vs.validate_value(value, "ua_" + name)
                user[name] = value

        userdb.save_users(users)

        return True

    def _show_form(self, profile_changed: bool) -> None:
        assert config.user.id is not None

        users = userdb.load_users()

        if profile_changed:
            html.reload_sidebar()
            html.show_message(_("Successfully updated user profile."))
            # Ensure theme changes are applied without additional user interaction
            html.immediate_browser_redirect(0.5, makeuri(global_request, []))

        if html.has_user_errors():
            html.show_user_errors()

        user = users.get(config.user.id)
        if user is None:
            html.show_warning(_("Sorry, your user account does not exist."))
            html.footer()
            return

        html.begin_form("profile", method="POST")
        html.prevent_password_auto_completion()
        html.open_div(class_="wato")
        forms.header(_("Personal settings"))

        forms.section(_("Name"), simple=True)
        html.write_text(user.get("alias", config.user.id))

        select_language(user)

        # Let the user configure how he wants to be notified
        rulebased_notifications = rulebased_notifications_enabled()
        if (not rulebased_notifications and config.user.may('general.edit_notifications') and
                user.get("notifications_enabled")):
>>>>>>> upstream/master
            forms.section(_("Notifications"))
            html.help(
                _("Here you can configure how you want to be notified about host and service problems and "
                  "other monitoring events."))
            watolib.get_vs_flexible_notifications().render_input("notification_method",
                                                                 user.get("notification_method"))

        if config.user.may('general.edit_user_attributes'):
<<<<<<< HEAD
            for name, attr in userdb.get_user_attributes():
                if attr.user_editable():
                    vs = attr.valuespec()
                    forms.section(_u(vs.title()))
                    value = user.get(name, vs.default_value())
                    if not attr.permission() or config.user.may(attr.permission()):
                        vs.render_input("ua_" + name, value)
                        html.help(_u(vs.help()))
                    else:
                        html.write(vs.value_to_text(value))

    # Save button
    forms.end()
    html.button("_save", _("Save"))
    html.close_div()
    html.hidden_fields()
    html.end_form()
    html.footer()
=======
            custom_user_attr_topics = get_user_attributes_by_topic()
            _show_custom_user_attr(user, custom_user_attr_topics.get("personal", []))
            forms.header(_("Interface settings"), isopen=False)
            _show_custom_user_attr(user, custom_user_attr_topics.get("interface", []))

        forms.end()
        html.close_div()
        html.hidden_fields()
        html.end_form()
        html.footer()


def _show_custom_user_attr(user, custom_attr):
    for name, attr in custom_attr:
        if attr.user_editable():
            vs = attr.valuespec()
            forms.section(_u(vs.title()))
            value = user.get(name, vs.default_value())
            if not attr.permission() or config.user.may(attr.permission()):
                vs.render_input("ua_" + name, value)
                html.help(_u(vs.help()))
            else:
                html.write(vs.value_to_text(value))
>>>>>>> upstream/master


@page_registry.register_page("wato_ajax_profile_repl")
class ModeAjaxProfileReplication(AjaxPage):
    """AJAX handler for asynchronous replication of user profiles (changed passwords)"""
    def page(self):
        request = self.webapi_request()

<<<<<<< HEAD
        site_id = request.get("site")
        if not site_id:
            raise MKUserError(None, "The site_id is missing")

        if site_id not in config.sitenames():
            raise MKUserError(None, _("The requested site does not exist"))

        status = cmk.gui.sites.states().get(site_id, {}).get("state", "unknown")
=======
        site_id_val = request.get("site")
        if not site_id_val:
            raise MKUserError(None, "The site_id is missing")
        site_id = site_id_val
        if site_id not in config.sitenames():
            raise MKUserError(None, _("The requested site does not exist"))

        status = cmk.gui.sites.states().get(site_id,
                                            cmk.gui.sites.SiteStatus({})).get("state", "unknown")
>>>>>>> upstream/master
        if status == "dead":
            raise MKGeneralException(_('The site is marked as dead. Not trying to replicate.'))

        site = config.site(site_id)
<<<<<<< HEAD
        result = self._synchronize_profile(site_id, site, config.user.id)

        if result != True:
=======
        assert config.user.id is not None
        result = self._synchronize_profile(site_id, site, config.user.id)

        if result is not True:
            assert result is not False
>>>>>>> upstream/master
            _add_profile_replication_change(site_id, result)
            raise MKGeneralException(result)

        return _("Replication completed successfully.")

<<<<<<< HEAD
    def _synchronize_profile(self, site_id, site, user_id):
        users = userdb.load_users(lock=False)
        if not user_id in users:
=======
    def _synchronize_profile(self, site_id: SiteId, site: SiteConfiguration,
                             user_id: UserId) -> Union[bool, str]:
        users = userdb.load_users(lock=False)
        if user_id not in users:
>>>>>>> upstream/master
            raise MKUserError(None, _('The requested user does not exist'))

        start = time.time()
        result = push_user_profiles_to_site_transitional_wrapper(site, {user_id: users[user_id]})

        duration = time.time() - start
        watolib.ActivateChanges().update_activation_time(site_id, ACTIVATION_TIME_PROFILE_SYNC,
                                                         duration)
        return result
<<<<<<< HEAD
=======


def page_menu_dropdown_user_related(page_name: str) -> PageMenuDropdown:
    return PageMenuDropdown(
        name="related",
        title=_("Related"),
        topics=[
            PageMenuTopic(
                title=_("User"),
                entries=list(_page_menu_entries_related(page_name)),
            ),
        ],
    )


def _page_menu_entries_related(page_name: str) -> Iterator[PageMenuEntry]:
    if page_name != "user_change_pw":
        yield PageMenuEntry(
            title=_("Change password"),
            icon_name="topic_change_password",
            item=make_simple_link("user_change_pw.py"),
        )

    if page_name != "user_profile":
        yield PageMenuEntry(
            title=_("Edit profile"),
            icon_name="topic_profile",
            item=make_simple_link("user_profile.py"),
        )

    if page_name != "user_notifications_p" and rulebased_notifications_enabled(
    ) and config.user.may('general.edit_notifications'):
        yield PageMenuEntry(
            title=_("Notification rules"),
            icon_name="topic_events",
            item=make_simple_link("wato.py?mode=user_notifications_p"),
        )
>>>>>>> upstream/master
