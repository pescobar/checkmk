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

import ast
from typing import NamedTuple

import cmk.gui.config as config
import cmk.gui.userdb as userdb
from cmk.gui.i18n import _
from cmk.gui.exceptions import MKGeneralException
from cmk.gui.globals import html
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import ast
import time
from multiprocessing.pool import ThreadPool
from multiprocessing import TimeoutError as mp_TimeoutError

from typing import NamedTuple

import cmk.gui.sites as sites
import cmk.gui.hooks as hooks
import cmk.gui.config as config
import cmk.gui.userdb as userdb
from cmk.gui.i18n import _
from cmk.gui.exceptions import MKGeneralException, RequestTimeout
from cmk.gui.globals import html
from cmk.gui.watolib.changes import add_change
>>>>>>> upstream/master
from cmk.gui.watolib.automation_commands import (
    AutomationCommand,
    automation_command_registry,
)
from cmk.gui.watolib.automations import (
    MKAutomationException,
    do_remote_automation,
    get_url,
)
from cmk.gui.watolib.utils import (
    mk_eval,
    mk_repr,
)

<<<<<<< HEAD
=======
# In case the sync is done on the master of a distributed setup the auth serial
# is increased on the master, but not on the slaves. The user can not access the
# slave sites anymore with the master sites cookie since the serials differ. In
# case the slave sites sync with LDAP on their own this issue will be repaired after
# the next LDAP sync on the slave, but in case the slaves do not sync, this problem
# will be repaired automagically once an admin performs the next WATO sync for
# another reason.
# Now, to solve this issue, we issue a user profile sync in case the password has
# been changed. We do this only when only the password has changed.
# Hopefully we have no large bulks of users changing their passwords at the same
# time. In this case the implementation does not scale well. We would need to
# change this to some kind of profile bulk sync per site.
# TODO: Should we move this to watolib?


class SynchronizationResult:
    def __init__(self, site_id, error_text=None, disabled=False, succeeded=False, failed=False):
        self.site_id = site_id
        self.error_text = error_text
        self.failed = failed
        self.disabled = disabled
        self.succeeded = succeeded


def _synchronize_profiles_to_sites(logger, profiles_to_synchronize):
    if not profiles_to_synchronize:
        return

    remote_sites = [(site_id, config.site(site_id)) for site_id in config.get_login_slave_sites()]

    logger.info('Credentials changed for %s. Trying to sync to %d sites' %
                (", ".join(profiles_to_synchronize.keys()), len(remote_sites)))

    states = sites.states()

    pool = ThreadPool()
    jobs = []
    for site_id, site in remote_sites:
        jobs.append(
            pool.apply_async(_sychronize_profile_worker,
                             (states, site_id, site, profiles_to_synchronize)))

    results = []
    start_time = time.time()
    while time.time() - start_time < 30:
        for job in jobs[:]:
            try:
                results.append(job.get(timeout=0.5))
                jobs.remove(job)
            except mp_TimeoutError:
                pass
        if not jobs:
            break

    contacted_sites = {x[0] for x in remote_sites}
    working_sites = {result.site_id for result in results}
    for site_id in contacted_sites - working_sites:
        results.append(
            SynchronizationResult(site_id,
                                  error_text=_("No response from update thread"),
                                  failed=True))

    for result in results:
        if result.error_text:
            logger.info('  FAILED [%s]: %s' % (result.site_id, result.error_text))
            if config.wato_enabled:
                add_change("edit-users",
                           _('Password changed (sync failed: %s)') % result.error_text,
                           add_user=False,
                           sites=[result.site_id],
                           need_restart=False)

    pool.terminate()
    pool.join()

    num_failed = sum([1 for result in results if result.failed])
    num_disabled = sum([1 for result in results if result.disabled])
    num_succeeded = sum([1 for result in results if result.succeeded])
    logger.info('  Disabled: %d, Succeeded: %d, Failed: %d' %
                (num_disabled, num_succeeded, num_failed))


def _sychronize_profile_worker(states, site_id, site, profiles_to_synchronize):
    if not site.get("replication"):
        return SynchronizationResult(site_id, disabled=True)

    if site.get("disabled"):
        return SynchronizationResult(site_id, disabled=True)

    status = states.get(site_id, {}).get("state", "unknown")
    if status == "dead":
        return SynchronizationResult(site_id,
                                     error_text=_("Site %s is dead") % site_id,
                                     failed=True)

    try:
        result = push_user_profiles_to_site_transitional_wrapper(site, profiles_to_synchronize)
        if result is not True:
            return SynchronizationResult(site_id, error_text=result, failed=True)
        return SynchronizationResult(site_id, succeeded=True)
    except RequestTimeout:
        # This function is currently only used by the background job
        # which does not have any request timeout set, just in case...
        raise
    except Exception as e:
        return SynchronizationResult(site_id, error_text="%s" % e, failed=True)


# TODO: Why is the logger handed over here? The sync job could simply gather it's own
def _handle_ldap_sync_finished(logger, profiles_to_synchronize, changes):
    _synchronize_profiles_to_sites(logger, profiles_to_synchronize)

    if changes and config.wato_enabled and not config.is_wato_slave_site():
        add_change("edit-users", "<br>".join(changes), add_user=False)


hooks.register_builtin("ldap-sync-finished", _handle_ldap_sync_finished)

>>>>>>> upstream/master

def push_user_profiles_to_site_transitional_wrapper(site, user_profiles):
    try:
        return push_user_profiles_to_site(site, user_profiles)
    except MKAutomationException as e:
        if "Invalid automation command: push-profiles" in "%s" % e:
            failed_info = []
<<<<<<< HEAD
            for user_id, user in user_profiles.iteritems():
                result = _legacy_push_user_profile_to_site(site, user_id, user)
                if result != True:
=======
            for user_id, user in user_profiles.items():
                result = _legacy_push_user_profile_to_site(site, user_id, user)
                if result is not True:
>>>>>>> upstream/master
                    failed_info.append(result)

            if failed_info:
                return "\n".join(failed_info)
            return True
<<<<<<< HEAD
        else:
            raise
=======
        raise
>>>>>>> upstream/master


def _legacy_push_user_profile_to_site(site, user_id, profile):
    url = site["multisiteurl"] + "automation.py?" + html.urlencode_vars([
        ("command", "push-profile"),
        ("secret", site["secret"]),
        ("siteid", site['id']),
        ("debug", config.debug and "1" or ""),
    ])

    response = get_url(url,
                       site.get('insecure', False),
                       data={
                           'user_id': user_id,
                           'profile': mk_repr(profile),
                       },
                       timeout=60)

    if not response:
        raise MKAutomationException(_("Empty output from remote site."))

    try:
        response = mk_eval(response)
<<<<<<< HEAD
    except:
=======
    except Exception:
>>>>>>> upstream/master
        # The remote site will send non-Python data in case of an error.
        raise MKAutomationException("%s: <pre>%s</pre>" % (_("Got invalid data"), response))
    return response


def push_user_profiles_to_site(site, user_profiles):
    return do_remote_automation(site,
                                "push-profiles", [("profiles", repr(user_profiles))],
                                timeout=60)


PushUserProfilesRequest = NamedTuple("PushUserProfilesRequest", [("user_profiles", dict)])


@automation_command_registry.register
class PushUserProfilesToSite(AutomationCommand):
    def command_name(self):
        return "push-profiles"

    def get_request(self):
<<<<<<< HEAD
        return PushUserProfilesRequest(ast.literal_eval(html.request.var("profiles")))
=======
        return PushUserProfilesRequest(
            ast.literal_eval(html.request.get_ascii_input_mandatory("profiles")))
>>>>>>> upstream/master

    def execute(self, request):
        user_profiles = request.user_profiles

        if not user_profiles:
            raise MKGeneralException(_('Invalid call: No profiles set.'))

        users = userdb.load_users(lock=True)
<<<<<<< HEAD
        for user_id, profile in user_profiles.iteritems():
=======
        for user_id, profile in user_profiles.items():
>>>>>>> upstream/master
            users[user_id] = profile
        userdb.save_users(users)
        return True
