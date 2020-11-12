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

import httplib
import os
import time
import traceback
from hashlib import md5
import six
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import http.client
import os
import traceback
import contextlib
from hashlib import sha256
from typing import List, Union, Optional, Tuple, Iterator
from pathlib import Path
from contextlib import suppress

from six import ensure_binary, ensure_str
from werkzeug.local import LocalProxy

import cmk.utils.version as cmk_version
import cmk.utils.paths
from cmk.utils.type_defs import UserId
>>>>>>> upstream/master

import cmk.gui.config as config
import cmk.gui.userdb as userdb
import cmk.gui.utils as utils
from cmk.gui.log import logger
import cmk.gui.i18n
import cmk.gui.mobile
<<<<<<< HEAD
from cmk.gui.pages import page_registry, Page
from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.htmllib import HTML

import cmk.utils.paths

from cmk.gui.exceptions import HTTPRedirect, MKInternalError, MKAuthException, MKUserError, FinalizeRequest

auth_type = None
auth_logger = logger.getChild("auth")


# Perform the user authentication. This is called by index.py to ensure user
# authentication and initialization of the user related data structures.
#
# Initialize the user session with the mod_python provided request object.
# The user may have configured (basic) authentication by the web server. In
# case a user is provided, we trust that user and assume it as authenticated.
#
# Otherwise we check / ask for the cookie authentication or eventually the
# automation secret authentication.
def authenticate(request):
    # Check whether or not already authenticated
    user_id = check_auth(request)
    if user_id:
        login(user_id)
        return True
    return False


# After the user has been authenticated, tell the different components
# of the GUI which user is authenticated.
def login(user_id):
    if not isinstance(user_id, six.text_type):
        raise MKInternalError("Invalid user id type")
    config.set_user_by_id(user_id)
    html.set_user_id(user_id)


def auth_cookie_name():
    return 'auth%s' % site_cookie_suffix()


def site_cookie_suffix():
=======
from cmk.gui.http import Request
from cmk.gui.pages import page_registry, Page
from cmk.gui.i18n import _
from cmk.gui.globals import html, local, request as global_request
from cmk.gui.htmllib import HTML
from cmk.gui.breadcrumb import Breadcrumb

from cmk.gui.exceptions import HTTPRedirect, MKInternalError, MKAuthException, MKUserError, FinalizeRequest

from cmk.gui.utils.urls import makeuri

auth_logger = logger.getChild("auth")


@contextlib.contextmanager
def authenticate(request: Request) -> Iterator[bool]:
    """Perform the user authentication

    This is called by index.py to ensure user
    authentication and initialization of the user related data structures.

    Initialize the user session with the mod_python provided request object.
    The user may have configured (basic) authentication by the web server. In
    case a user is provided, we trust that user and assume it as authenticated.

    Otherwise we check / ask for the cookie authentication or eventually the
    automation secret authentication."""

    user_id = _check_auth(request)
    if not user_id:
        yield False
        return

    with UserContext(user_id):
        yield True


@contextlib.contextmanager
def UserContext(user_id: UserId) -> Iterator[None]:
    """Managing authenticated user context

    After the user has been authenticated, initialize the global user object.
    Also cleanup when leaving"""
    try:
        config.set_user_by_id(user_id)
        yield
    finally:
        html.transaction_manager.store_new()
        userdb.on_end_of_request(user_id)
        config.clear_user_login()


def auth_cookie_name() -> str:
    return 'auth%s' % site_cookie_suffix()


def site_cookie_suffix() -> str:
>>>>>>> upstream/master
    url_prefix = config.url_prefix()

    # Strip of eventual present "http://<host>". DIRTY!
    if url_prefix.startswith('http:'):
        url_prefix = url_prefix[url_prefix[7:].find('/') + 7:]

    return os.path.dirname(url_prefix).replace('/', '_')


<<<<<<< HEAD
# Reads the auth secret from a file. Creates the files if it does
# not exist. Having access to the secret means that one can issue valid
# cookies for the cookie auth.
def load_secret():
    secret_path = '%s/auth.secret' % os.path.dirname(cmk.utils.paths.htpasswd_file)
    secret = ''
    if os.path.exists(secret_path):
        secret = open(secret_path).read().strip()
=======
def _load_secret() -> str:
    """Reads the sites auth secret from a file

    Creates the files if it does not exist. Having access to the secret means that one can issue
    valid cookies for the cookie auth.
    """
    htpasswd_path = Path(cmk.utils.paths.htpasswd_file)
    secret_path = htpasswd_path.parent.joinpath('auth.secret')

    secret = u''
    if secret_path.exists():
        with secret_path.open(encoding="utf-8") as f:
            secret = f.read().strip()
>>>>>>> upstream/master

    # Create new secret when this installation has no secret
    #
    # In past versions we used another bad approach to generate a secret. This
    # checks for such secrets and creates a new one. This will invalidate all
    # current auth cookies which means that all logged in users will need to
    # renew their login after update.
    if secret == '' or len(secret) == 32:
<<<<<<< HEAD
        secret = generate_secret()
        open(secret_path, 'w').write(secret)
=======
        secret = _generate_secret()
        with secret_path.open("w", encoding="utf-8") as f:
            f.write(secret)
>>>>>>> upstream/master

    return secret


<<<<<<< HEAD
def generate_secret():
    return utils.get_random_string(256)


# Load the password serial of the user. This serial identifies the current config
# state of the user account. If either the password is changed or the account gets
# locked the serial is increased and all cookies get invalidated.
# Better use the value from the "serials.mk" file, instead of loading the whole
# user database via load_users() for performance reasons.
def load_serial(username):
    return userdb.load_custom_attr(username, 'serial', int, 0)


def generate_auth_hash(username, now):
    return generate_hash(username, username.encode("utf-8") + str(now))


# Generates a hash to be added into the cookie value
def generate_hash(username, value):
    secret = load_secret()
    serial = load_serial(username)
    return md5(value + str(serial) + secret).hexdigest()


def del_auth_cookie():
=======
def _generate_secret() -> str:
    return ensure_str(utils.get_random_string(256))


def _load_serial(username: UserId) -> int:
    """Load the password serial of the user

    This serial identifies the current config state of the user account. If either the password is
    changed or the account gets locked the serial is increased and all cookies get invalidated.
    Better use the value from the "serials.mk" file, instead of loading the whole user database via
    load_users() for performance reasons.
    """
    return userdb.load_custom_attr(username, 'serial', int, 0)


def _generate_auth_hash(username: UserId, session_id: str) -> str:
    return _generate_hash(username, ensure_str(username) + session_id)


def _generate_hash(username: UserId, value: str) -> str:
    """Generates a hash to be added into the cookie value"""
    secret = _load_secret()
    serial = _load_serial(username)
    return sha256(ensure_binary(value + str(serial) + secret)).hexdigest()


def del_auth_cookie() -> None:
>>>>>>> upstream/master
    # Note: in distributed setups a cookie issued by one site is accepted by
    # others with the same auth.secret and user serial numbers. When a users
    # logs out then we need to delete all cookies that are accepted by us -
    # not just the one that we have issued.
    for cookie_name in html.request.get_cookie_names():
        if cookie_name.startswith("auth_"):
<<<<<<< HEAD
            if auth_cookie_is_valid(cookie_name):
                html.response.delete_cookie(cookie_name)


def auth_cookie_value(username):
    now = str(time.time())
    return ":".join([username, now, generate_auth_hash(username, now)])


def invalidate_auth_session():
    if config.single_user_session is not None:
        userdb.invalidate_session(config.user.id)

=======
            if _auth_cookie_is_valid(cookie_name):
                html.response.delete_cookie(cookie_name)


def _auth_cookie_value(username: UserId, session_id: str) -> str:
    return ":".join([ensure_str(username), session_id, _generate_auth_hash(username, session_id)])


def _invalidate_auth_session() -> None:
>>>>>>> upstream/master
    del_auth_cookie()
    html.del_language_cookie()


<<<<<<< HEAD
def renew_auth_session(username):
    if config.single_user_session is not None:
        userdb.refresh_session(username)

    set_auth_cookie(username)


def create_auth_session(username):
    if config.single_user_session is not None:
        session_id = userdb.initialize_session(username)
        set_session_cookie(username, session_id)

    set_auth_cookie(username)


def set_auth_cookie(username):
    html.response.set_http_cookie(auth_cookie_name(), auth_cookie_value(username))


def set_session_cookie(username, session_id):
    html.response.set_http_cookie(session_cookie_name(), session_cookie_value(username, session_id))


def session_cookie_name():
    return 'session%s' % site_cookie_suffix()


def session_cookie_value(username, session_id):
    value = username.encode("utf-8") + ":" + session_id
    return value + ":" + generate_hash(username, value)


def get_session_id_from_cookie(username):
    raw_value = html.request.cookie(session_cookie_name(), "::")
    cookie_username, session_id, cookie_hash = raw_value.split(':', 2)

    if cookie_username.decode("utf-8") != username \
       or cookie_hash != generate_hash(username, username.encode("utf-8") + ":" + session_id):
        auth_logger.error("Invalid session: %s, Cookie: %r" % (username, raw_value))
=======
def _renew_auth_session(username: UserId, session_id: str) -> None:
    _set_auth_cookie(username, session_id)


def _create_auth_session(username: UserId, session_id: str) -> None:
    _set_auth_cookie(username, session_id)


def update_auth_cookie(username: UserId) -> None:
    """Is called during password change to set a new cookie

    We are not able to validate the old cookie value here since the password was already changed
    on the server side. Skip validation in this case, this is fine. The cookie was valdiated
    before accessing this page.
    """
    _set_auth_cookie(username, _get_session_id_from_cookie(username, revalidate_cookie=False))


def _set_auth_cookie(username: UserId, session_id: str) -> None:
    html.response.set_http_cookie(auth_cookie_name(), _auth_cookie_value(username, session_id))


def _get_session_id_from_cookie(username: UserId, revalidate_cookie: bool) -> str:
    cookie_username, session_id, cookie_hash = _parse_auth_cookie(auth_cookie_name())

    # Has been checked before, but validate before using that information, just to be sure
    if revalidate_cookie:
        _check_parsed_auth_cookie(username, session_id, cookie_hash)

    if cookie_username != username:
        auth_logger.error("Invalid session: (User: %s, Session: %s)", username, session_id)
>>>>>>> upstream/master
        return ""

    return session_id


<<<<<<< HEAD
def renew_cookie(cookie_name, username):
=======
def _renew_cookie(cookie_name: str, username: UserId, session_id: str) -> None:
>>>>>>> upstream/master
    # Do not renew if:
    # a) The _ajaxid var is set
    # b) A logout is requested
    if (html.myfile != 'logout' and not html.request.has_var('_ajaxid')) \
       and cookie_name == auth_cookie_name():
        auth_logger.debug("Renewing auth cookie (%s.py, vars: %r)" %
                          (html.myfile, dict(html.request.itervars())))
<<<<<<< HEAD
        renew_auth_session(username)


def check_auth_cookie(cookie_name):
    username, issue_time, cookie_hash = parse_auth_cookie(cookie_name)
    check_parsed_auth_cookie(username, issue_time, cookie_hash)

    # Check whether or not there is an idle timeout configured, delete cookie and
    # require the user to renew the log when the timeout exceeded.
    if userdb.login_timed_out(username, issue_time):
        del_auth_cookie()
        return

    # Check whether or not a single user session is allowed at a time and the user
    # is doing this request with the currently active session.
    if config.single_user_session is not None:
        session_id = get_session_id_from_cookie(username)
        if not userdb.is_valid_user_session(username, session_id):
            del_auth_cookie()
            return

    # Once reached this the cookie is a good one. Renew it!
    renew_cookie(cookie_name, username)
=======
        _renew_auth_session(username, session_id)


def _check_auth_cookie(cookie_name: str) -> Optional[UserId]:
    username, session_id, cookie_hash = _parse_auth_cookie(cookie_name)
    _check_parsed_auth_cookie(username, session_id, cookie_hash)

    try:
        userdb.on_access(username, session_id)
    except MKAuthException:
        del_auth_cookie()
        raise

    # Once reached this the cookie is a good one. Renew it!
    _renew_cookie(cookie_name, username, session_id)
>>>>>>> upstream/master

    if html.myfile != 'user_change_pw':
        result = userdb.need_to_change_pw(username)
        if result:
            raise HTTPRedirect('user_change_pw.py?_origtarget=%s&reason=%s' %
<<<<<<< HEAD
                               (html.urlencode(html.makeuri([])), result))
=======
                               (html.urlencode(makeuri(global_request, [])), result))
>>>>>>> upstream/master

    # Return the authenticated username
    return username


<<<<<<< HEAD
def parse_auth_cookie(cookie_name):
    raw_value = html.request.cookie(cookie_name, "::")
    username, issue_time, cookie_hash = raw_value.split(':', 2)
    return username.decode("utf-8"), float(issue_time) if issue_time else 0.0, cookie_hash


def check_parsed_auth_cookie(username, issue_time, cookie_hash):
    if not userdb.user_exists(username):
        raise MKAuthException(_('Username is unknown'))

    if cookie_hash != generate_auth_hash(username, issue_time):
        raise MKAuthException(_('Invalid credentials'))


def auth_cookie_is_valid(cookie_name):
    try:
        check_parsed_auth_cookie(*parse_auth_cookie(cookie_name))
=======
def _parse_auth_cookie(cookie_name: str) -> Tuple[UserId, str, str]:
    raw_cookie = html.request.cookie(cookie_name, "::")
    assert raw_cookie is not None

    raw_value = ensure_str(raw_cookie)
    username, session_id, cookie_hash = raw_value.split(':', 2)

    # Refuse pre 2.0 cookies: These held the "issue time" in the 2nd field.
    with suppress(ValueError):
        float(session_id)
        raise MKAuthException("Refusing pre 2.0 auth cookie")

    return UserId(username), session_id, cookie_hash


def _check_parsed_auth_cookie(username: UserId, session_id: str, cookie_hash: str) -> None:
    if not userdb.user_exists(username):
        raise MKAuthException(_('Username is unknown'))

    if cookie_hash != _generate_auth_hash(username, session_id):
        raise MKAuthException(_('Invalid credentials'))


def _auth_cookie_is_valid(cookie_name: str) -> bool:
    try:
        _check_parsed_auth_cookie(*_parse_auth_cookie(cookie_name))
>>>>>>> upstream/master
        return True
    except MKAuthException:
        return False
    except Exception:
        return False


# TODO: Needs to be cleaned up. When using HTTP header auth or web server auth it is not
# ensured that a user exists after letting the user in. This is a problem for the following
# code! We need to define a point where the following code can rely on an existing user
<<<<<<< HEAD
# object. userdb.hook_login() is doing some similar stuff
=======
# object. userdb.check_credentials() is doing some similar stuff
>>>>>>> upstream/master
# - It also checks the type() of the user_id (Not in the same way :-/)
# - It also calls userdb.is_customer_user_allowed_to_login()
# - It calls userdb.create_non_existing_user() but we don't
# - It calls connection.is_locked() but we don't
<<<<<<< HEAD
def check_auth(request):
    user_id = check_auth_web_server(request)

    if html.request.var("_secret"):
        user_id = check_auth_automation()

    elif config.auth_by_http_header:
        user_id = check_auth_http_header()

    if user_id is None:
        user_id = check_auth_by_cookie()

    if (user_id is not None and not isinstance(user_id, six.text_type)) or user_id == u'':
=======
def _check_auth(request: Request) -> Optional[UserId]:
    user_id = _check_auth_web_server(request)

    if html.request.var("_secret"):
        user_id = _check_auth_automation()

    elif config.auth_by_http_header:
        if not config.user_login:
            return None
        user_id = _check_auth_http_header()

    if user_id is None:
        if not config.user_login:
            return None
        user_id = _check_auth_by_cookie()

    if (user_id is not None and not isinstance(user_id, str)) or user_id == u'':
>>>>>>> upstream/master
        raise MKInternalError(_("Invalid user authentication"))

    if user_id and not userdb.is_customer_user_allowed_to_login(user_id):
        # A CME not assigned with the current sites customer
        # is not allowed to login
        auth_logger.debug("User '%s' is not allowed to authenticate: Invalid customer" % user_id)
        return None

    return user_id


<<<<<<< HEAD
def check_auth_automation():
    secret = html.request.var("_secret", "").strip()
    user_id = html.get_unicode_input("_username", "").strip()
    html.request.del_var('_username')
    html.request.del_var('_secret')
    if secret and user_id and "/" not in user_id:
        path = cmk.utils.paths.var_dir + "/web/" + user_id.encode("utf-8") + "/automation.secret"
        if os.path.isfile(path) and open(path).read().strip() == secret:
            # Auth with automation secret succeeded - mark transid as unneeded in this case
            html.transaction_manager.ignore()
            set_auth_type("automation")
            return user_id
    raise MKAuthException(_("Invalid automation secret for user %s") % user_id)


# When http header auth is enabled, try to read the user_id from the var
# and when there is some available, set the auth cookie (for other addons) and proceed.
def check_auth_http_header():
=======
def verify_automation_secret(user_id: UserId, secret: str) -> bool:
    if secret and user_id and "/" not in user_id:
        path = Path(cmk.utils.paths.var_dir) / "web" / ensure_str(user_id) / "automation.secret"
        if not path.is_file():
            return False

        with path.open(encoding="utf-8") as f:
            return ensure_str(f.read()).strip() == secret

    return False


def _check_auth_automation() -> UserId:
    secret = html.request.get_str_input_mandatory("_secret", "").strip()
    user_id = html.request.get_unicode_input_mandatory("_username", "")

    user_id = UserId(user_id.strip())
    html.del_var_from_env('_username')
    html.del_var_from_env('_secret')

    if verify_automation_secret(user_id, secret):
        # Auth with automation secret succeeded - mark transid as unneeded in this case
        html.transaction_manager.ignore()
        set_auth_type("automation")
        return user_id
    raise MKAuthException(_("Invalid automation secret for user %s") % user_id)


def _check_auth_http_header() -> Optional[UserId]:
    """When http header auth is enabled, try to read the user_id from the var
    and when there is some available, set the auth cookie (for other addons) and proceed."""
    assert isinstance(config.auth_by_http_header, str)
>>>>>>> upstream/master
    user_id = html.request.get_request_header(config.auth_by_http_header)
    if not user_id:
        return None

<<<<<<< HEAD
    user_id = user_id.decode("utf-8")
    set_auth_type("http_header")
    renew_cookie(auth_cookie_name(), user_id)
    return user_id


# Try to get the authenticated user from the mod_python provided request object.
# The user may have configured (basic) authentication by the web server. In
# case a user is provided, we trust that user.
def check_auth_web_server(request):
    user = request.remote_user
    if user is not None:
        set_auth_type("web_server")
        return user.decode("utf-8")


def check_auth_by_cookie():
=======
    user_id = UserId(ensure_str(user_id))
    set_auth_type("http_header")

    if auth_cookie_name() not in html.request.cookies:
        userdb.on_succeeded_login(user_id)

    return user_id


def _check_auth_web_server(request: Request) -> Optional[UserId]:
    """Try to get the authenticated user from the HTTP request

    The user may have configured (basic) authentication by the web server. In
    case a user is provided, we trust that user.
    """
    user = request.remote_user
    if user is not None:
        set_auth_type("web_server")
        return UserId(ensure_str(user))
    return None


def _check_auth_by_cookie() -> Optional[UserId]:
>>>>>>> upstream/master
    for cookie_name in html.request.get_cookie_names():
        if cookie_name.startswith('auth_'):
            try:
                set_auth_type("cookie")
<<<<<<< HEAD
                return check_auth_cookie(cookie_name)
=======
                return _check_auth_cookie(cookie_name)
>>>>>>> upstream/master
            except MKAuthException:
                # Suppress cookie validation errors from other sites cookies
                auth_logger.debug('Exception while checking cookie %s: %s' %
                                  (cookie_name, traceback.format_exc()))
            except Exception:
<<<<<<< HEAD
                auth_logger.error('Exception while checking cookie %s: %s' %
                                  (cookie_name, traceback.format_exc()))


def set_auth_type(ty):
    global auth_type
    auth_type = ty


def do_login():
    # handle the sent login form
    if html.request.var('_login'):
        try:
            username = html.get_unicode_input('_username', '').rstrip()
            if username == '':
                raise MKUserError('_username', _('No username given.'))

            password = html.request.var('_password', '')
            if password == '':
=======
                auth_logger.debug('Exception while checking cookie %s: %s' %
                                  (cookie_name, traceback.format_exc()))
    return None


def set_auth_type(_auth_type: str) -> None:
    local.auth_type = _auth_type


auth_type: Union[str, LocalProxy] = LocalProxy(lambda: local.auth_type)


@page_registry.register_page("login")
class LoginPage(Page):
    def __init__(self) -> None:
        super(LoginPage, self).__init__()
        self._no_html_output = False

    def set_no_html_output(self, no_html_output: bool) -> None:
        self._no_html_output = no_html_output

    def page(self) -> None:
        # Initialize the cmk.gui.i18n for the login dialog. This might be
        # overridden later after user login
        cmk.gui.i18n.localize(html.request.var("lang", config.get_language()))

        self._do_login()

        if self._no_html_output:
            raise MKAuthException(_("Invalid login credentials."))

        if html.mobile:
            cmk.gui.mobile.page_login()
            return

        self._show_login_page()

    def _do_login(self) -> None:
        """handle the sent login form"""
        if not html.request.var('_login'):
            return

        try:
            if not config.user_login:
                raise MKUserError(None, _('Login is not allowed on this site.'))

            username_var = html.request.get_unicode_input('_username', '')
            assert username_var is not None
            username = UserId(username_var.rstrip())
            if not username:
                raise MKUserError('_username', _('No username given.'))

            password = html.request.var('_password', '')
            if not password:
>>>>>>> upstream/master
                raise MKUserError('_password', _('No password given.'))

            default_origtarget = config.url_prefix() + "check_mk/"
            origtarget = html.get_url_input("_origtarget", default_origtarget)

            # Disallow redirections to:
            #  - logout.py: Happens after login
            #  - side.py: Happens when invalid login is detected during sidebar refresh
            if "logout.py" in origtarget or 'side.py' in origtarget:
                origtarget = default_origtarget

<<<<<<< HEAD
            # None        -> User unknown, means continue with other connectors
            # '<user_id>' -> success
            # False       -> failed
            result = userdb.hook_login(username, password)
=======
            result = userdb.check_credentials(username, password)
>>>>>>> upstream/master
            if result:
                # use the username provided by the successful login function, this function
                # might have transformed the username provided by the user. e.g. switched
                # from mixed case to lower case.
                username = result

<<<<<<< HEAD
                # When single user session mode is enabled, check that there is not another
                # active session
                userdb.ensure_user_can_init_session(username)

                # reset failed login counts
                userdb.on_succeeded_login(username)
=======
                session_id = userdb.on_succeeded_login(username)
>>>>>>> upstream/master

                # The login succeeded! Now:
                # a) Set the auth cookie
                # b) Unset the login vars in further processing
                # c) Redirect to really requested page
<<<<<<< HEAD
                create_auth_session(username)
=======
                _create_auth_session(username, session_id)
>>>>>>> upstream/master

                # Never use inplace redirect handling anymore as used in the past. This results
                # in some unexpected situations. We simpy use 302 redirects now. So we have a
                # clear situation.
                # userdb.need_to_change_pw returns either False or the reason description why the
                # password needs to be changed
<<<<<<< HEAD
                result = userdb.need_to_change_pw(username)
                if result:
                    raise HTTPRedirect('user_change_pw.py?_origtarget=%s&reason=%s' %
                                       (html.urlencode(origtarget), result))
                else:
                    raise HTTPRedirect(origtarget)
            else:
                userdb.on_failed_login(username)
                raise MKUserError(None, _('Invalid credentials.'))
        except MKUserError as e:
            html.add_user_error(e.varname, e)
            return "%s" % e


@page_registry.register_page("login")
class LoginPage(Page):
    def __init__(self):
        super(LoginPage, self).__init__()
        self._no_html_output = False

    def set_no_html_output(self, no_html_output):
        self._no_html_output = no_html_output

    def page(self):
        # Initialize the cmk.gui.i18n for the login dialog. This might be
        # overridden later after user login
        cmk.gui.i18n.localize(html.request.var("lang", config.get_language()))

        result = do_login()
        if isinstance(result, tuple):
            return  # Successful login

        if self._no_html_output:
            raise MKAuthException(_("Invalid login credentials."))

        if html.mobile:
            return cmk.gui.mobile.page_login()

        return normal_login_page()


def normal_login_page(called_directly=True):
    html.set_render_headfoot(False)
    html.add_body_css_class("login")
    html.header(config.get_page_heading(), javascripts=[])

    default_origtarget = "index.py" if html.myfile in ["login", "logout"] else html.makeuri([])
    origtarget = html.get_url_input("_origtarget", default_origtarget)

    # Never allow the login page to be opened in a frameset. Redirect top page to login page.
    # This will result in a full screen login page.
    html.javascript('''if(top != self) {
    window.top.location.href = location;
}''')

    # When someone calls the login page directly and is already authed redirect to main page
    if html.myfile == 'login' and check_auth(html.request):
        raise HTTPRedirect(origtarget)

    html.open_div(id_="login")

    html.open_div(id_="login_window")

    html.div("" if "hide_version" in config.login_screen else cmk.__version__, id_="version")

    html.begin_form("login", method='POST', add_transid=False, action='login.py')
    html.hidden_field('_login', '1')
    html.hidden_field('_origtarget', origtarget)
    html.label("%s:" % _('Username'), id_="label_user", class_=["legend"], for_="_username")
    html.br()
    html.text_input("_username", id_="input_user")
    html.label("%s:" % _('Password'), id_="label_pass", class_=["legend"], for_="_password")
    html.br()
    html.password_input("_password", id_="input_pass", size=None)

    if html.has_user_errors():
        html.open_div(id_="login_error")
        html.show_user_errors()
        html.close_div()

    html.open_div(id_="button_text")
    html.button("_login", _('Login'))
    html.close_div()
    html.close_div()

    html.open_div(id_="foot")

    if config.login_screen.get("login_message"):
        html.open_div(id_="login_message")
        html.show_info(config.login_screen["login_message"])
        html.close_div()

    footer = []
    for title, url, target in config.login_screen.get("footer_links", []):
        footer.append(html.render_a(title, href=url, target=target))

    if "hide_version" not in config.login_screen:
        footer.append("Version: %s" % cmk.__version__)

    footer.append("&copy; %s" %
                  html.render_a("tribe29 GmbH", href="https://checkmk.com", target="_blank"))

    html.write(HTML(" - ").join(footer))

    if cmk.is_raw_edition():
        html.br()
        html.br()
        html.write(
            _('You can use, modify and distribute Check_MK under the terms of the <a href="%s" target="_blank">'
              'GNU GPL Version 2</a>.') % "https://checkmk.com/gpl.html")

    html.close_div()

    html.set_focus('_username')
    html.hidden_fields()
    html.end_form()
    html.close_div()

    html.footer()
=======
                change_pw_result = userdb.need_to_change_pw(username)
                if change_pw_result:
                    raise HTTPRedirect('user_change_pw.py?_origtarget=%s&reason=%s' %
                                       (html.urlencode(origtarget), change_pw_result))
                raise HTTPRedirect(origtarget)

            userdb.on_failed_login(username)
            raise MKUserError(None, _('Invalid credentials.'))
        except MKUserError as e:
            html.add_user_error(e.varname, e)

    def _show_login_page(self) -> None:
        html.set_render_headfoot(False)
        html.add_body_css_class("login")
        html.header(config.get_page_heading(), Breadcrumb(), javascripts=[])

        default_origtarget = ("index.py" if html.myfile in ["login", "logout"] else makeuri(
            global_request, []))
        origtarget = html.get_url_input("_origtarget", default_origtarget)

        # Never allow the login page to be opened in the iframe. Redirect top page to login page.
        # This will result in a full screen login page.
        html.javascript('''if(top != self) {
    window.top.location.href = location;
}''')

        # When someone calls the login page directly and is already authed redirect to main page
        if html.myfile == 'login' and _check_auth(html.request):
            raise HTTPRedirect(origtarget)

        html.open_div(id_="login")

        html.open_div(id_="login_window")

        html.div("" if "hide_version" in config.login_screen else cmk_version.__version__,
                 id_="version")

        html.begin_form("login", method='POST', add_transid=False, action='login.py')
        html.hidden_field('_login', '1')
        html.hidden_field('_origtarget', origtarget)
        html.label("%s:" % _('Username'), id_="label_user", class_=["legend"], for_="_username")
        html.br()
        html.text_input("_username", id_="input_user")
        html.label("%s:" % _('Password'), id_="label_pass", class_=["legend"], for_="_password")
        html.br()
        html.password_input("_password", id_="input_pass", size=None)

        if html.has_user_errors():
            html.open_div(id_="login_error")
            html.show_user_errors()
            html.close_div()

        html.open_div(id_="button_text")
        html.button("_login", _('Login'), cssclass="hot")
        html.close_div()
        html.close_div()

        html.open_div(id_="foot")

        if config.login_screen.get("login_message"):
            html.open_div(id_="login_message")
            html.show_message(config.login_screen["login_message"])
            html.close_div()

        footer: List[Union[HTML, str]] = []
        for title, url, target in config.login_screen.get("footer_links", []):
            footer.append(html.render_a(title, href=url, target=target))

        if "hide_version" not in config.login_screen:
            footer.append("Version: %s" % cmk_version.__version__)

        footer.append("&copy; %s" %
                      html.render_a("tribe29 GmbH", href="https://checkmk.com", target="_blank"))

        html.write(HTML(" - ").join(footer))

        if cmk_version.is_raw_edition():
            html.br()
            html.br()
            html.write(
                _('You can use, modify and distribute Check_MK under the terms of the <a href="%s" target="_blank">'
                  'GNU GPL Version 2</a>.') % "https://checkmk.com/gpl.html")

        html.close_div()

        html.set_focus('_username')
        html.hidden_fields()
        html.end_form()
        html.close_div()

        html.footer()
>>>>>>> upstream/master


@page_registry.register_page("logout")
class LogoutPage(Page):
<<<<<<< HEAD
    def page(self):
        invalidate_auth_session()

        if auth_type == 'cookie':
            raise HTTPRedirect(config.url_prefix() + 'check_mk/login.py')
        else:
            # Implement HTTP logout with cookie hack
            if not html.request.has_cookie('logout'):
                html.response.headers[
                    'WWW-Authenticate'] = 'Basic realm="OMD Monitoring Site %s"' % config.omd_site(
                    )
                html.response.set_http_cookie('logout', '1')
                raise FinalizeRequest(httplib.UNAUTHORIZED)
            else:
                html.response.delete_cookie('logout')
                raise HTTPRedirect(config.url_prefix() + 'check_mk/')
=======
    def page(self) -> None:
        assert config.user.id is not None

        _invalidate_auth_session()

        session_id = _get_session_id_from_cookie(config.user.id, revalidate_cookie=True)
        userdb.on_logout(config.user.id, session_id)

        if auth_type == 'cookie':
            raise HTTPRedirect(config.url_prefix() + 'check_mk/login.py')

        # Implement HTTP logout with cookie hack
        if not html.request.has_cookie('logout'):
            html.response.headers['WWW-Authenticate'] = ('Basic realm="OMD Monitoring Site %s"' %
                                                         config.omd_site())
            html.response.set_http_cookie('logout', '1')
            raise FinalizeRequest(http.client.UNAUTHORIZED)

        html.response.delete_cookie('logout')
        raise HTTPRedirect(config.url_prefix() + 'check_mk/')
>>>>>>> upstream/master
