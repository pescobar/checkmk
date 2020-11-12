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
# | Copyright Mathias Kettner 2018             mk@mathias-kettner.de |
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

import os
import subprocess
import time

import six

import cmk
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from logging import Logger
import os
import subprocess
import time
from typing import Any, Dict, Optional, Set

>>>>>>> upstream/master
import cmk.utils.debug
import cmk.utils.defines
from cmk.utils.log import VERBOSE
import livestatus

<<<<<<< HEAD
=======
from .settings import Settings

>>>>>>> upstream/master
#.
#   .--Actions-------------------------------------------------------------.
#   |                     _        _   _                                   |
#   |                    / \   ___| |_(_) ___  _ __  ___                   |
#   |                   / _ \ / __| __| |/ _ \| '_ \/ __|                  |
#   |                  / ___ \ (__| |_| | (_) | | | \__ \                  |
#   |                 /_/   \_\___|\__|_|\___/|_| |_|___/                  |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Global functions for executing rule actions like sending emails and  |
#   | executing scripts.                                                   |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def event_has_opened(history, settings, config, logger, event_server, event_columns, rule, event):
=======
def event_has_opened(history: Any, settings: Settings, config: Dict[str, Any], logger: Logger,
                     event_server: Any, event_columns: Any, rule: Any, event: Any) -> None:
>>>>>>> upstream/master
    # Prepare for events with a limited livetime. This time starts
    # when the event enters the open state or acked state
    if "livetime" in rule:
        livetime, phases = rule["livetime"]
        event["live_until"] = time.time() + livetime
        event["live_until_phases"] = phases

    if rule.get("actions_in_downtime", True) is False and event["host_in_downtime"]:
        logger.info("Skip actions for event %d: Host is in downtime" % event["id"])
        return

    do_event_actions(history,
                     settings,
                     config,
                     logger,
                     event_server,
                     event_columns,
                     rule.get("actions", []),
                     event,
                     is_cancelling=False)


# Execute a list of actions on an event that has just been
# opened or cancelled.
<<<<<<< HEAD
def do_event_actions(history, settings, config, logger, event_server, event_columns, actions, event,
                     is_cancelling):
=======
def do_event_actions(history: Any, settings: Settings, config: Dict[str, Any], logger: Logger,
                     event_server: Any, event_columns: Any, actions: Any, event: Any,
                     is_cancelling: bool) -> None:
>>>>>>> upstream/master
    for aname in actions:
        if aname == "@NOTIFY":
            do_notify(event_server, logger, event, is_cancelling=is_cancelling)
        else:
            action = config["action"].get(aname)
            if not action:
                logger.info("Cannot execute undefined action '%s'" % aname)
                logger.info("We have to following actions: %s" % ", ".join(config["action"].keys()))
            else:
                logger.info("Going to execute action '%s' on event %d" %
                            (action["title"], event["id"]))
                do_event_action(history, settings, config, logger, event_columns, action, event, "")


# Rule actions are currently done synchronously. Actions should
# not hang for more than a couple of ms.


<<<<<<< HEAD
def do_event_action(history, settings, config, logger, event_columns, action, event, user):
=======
def do_event_action(history: Any, settings: Settings, config: Dict[str, Any], logger: Logger,
                    event_columns: Any, action: Any, event: Any, user: Any) -> None:
>>>>>>> upstream/master
    if action["disabled"]:
        logger.info("Skipping disabled action %s." % action["id"])
        return

    try:
        action_type, action_settings = action["action"]
        if action_type == 'email':
            to = _escape_null_bytes(
                _substitute_event_tags(event_columns, action_settings["to"], event))
            subject = _escape_null_bytes(
                _substitute_event_tags(event_columns, action_settings["subject"], event))
            body = _escape_null_bytes(
                _substitute_event_tags(event_columns, action_settings["body"], event))

            _send_email(config, to, subject, body, logger)
            history.add(event, "EMAIL", user, "%s|%s" % (to, subject))
        elif action_type == 'script':
            _execute_script(
                event_columns,
                _escape_null_bytes(
                    _substitute_event_tags(event_columns, action_settings["script"],
                                           _get_quoted_event(event, logger))), event, logger)
            history.add(event, "SCRIPT", user, action['id'])
        else:
            logger.error("Cannot execute action %s: invalid action type %s" %
                         (action["id"], action_type))
    except Exception:
        if settings.options.debug:
            raise
        logger.exception("Error during execution of action %s" % action["id"])


<<<<<<< HEAD
def _escape_null_bytes(s):
    return s.replace("\000", "\\000")


def _get_quoted_event(event, logger):
    new_event = {}
    fields_to_quote = ["application", "match_groups", "text", "comment", "contact"]
    for key, value in event.iteritems():
=======
def _escape_null_bytes(s: Any) -> Any:
    return s.replace("\000", "\\000")


def _get_quoted_event(event: Any, logger: Logger) -> Any:
    new_event: Dict[str, Any] = {}
    fields_to_quote = ["application", "match_groups", "text", "comment", "contact"]
    for key, value in event.items():
>>>>>>> upstream/master
        if key not in fields_to_quote:
            new_event[key] = value
        else:
            try:
<<<<<<< HEAD
                if isinstance(value, list):
                    new_value = map(quote_shell_string, value)
=======
                new_value: Any = None
                if isinstance(value, list):
                    new_value = list(map(quote_shell_string, value))
>>>>>>> upstream/master
                elif isinstance(value, tuple):
                    new_value = value
                else:
                    new_value = quote_shell_string(value)
                new_event[key] = new_value
            except Exception as e:
                # If anything unforeseen happens, we use the intial value
                new_event[key] = value
                logger.exception("Unable to quote event text %r: %r, %r" % (key, value, e))

    return new_event


<<<<<<< HEAD
def _substitute_event_tags(event_columns, text, event):
    for key, value in _get_event_tags(event_columns, event).iteritems():
=======
def _substitute_event_tags(event_columns: Any, text: Any, event: Any) -> Any:
    for key, value in _get_event_tags(event_columns, event).items():
>>>>>>> upstream/master
        text = text.replace('$%s$' % key.upper(), value)
    return text


<<<<<<< HEAD
def quote_shell_string(s):
    return "'" + s.replace("'", "'\"'\"'") + "'"


def _send_email(config, to, subject, body, logger):
=======
def quote_shell_string(s: Any) -> Any:
    return "'" + s.replace("'", "'\"'\"'") + "'"


def _send_email(config: Dict[str, Any], to: Any, subject: Any, body: Any, logger: Logger) -> bool:
>>>>>>> upstream/master
    command_utf8 = [
        "mail", "-S", "sendcharsets=utf-8", "-s",
        subject.encode("utf-8"),
        to.encode("utf-8")
    ]

    if config["debug_rules"]:
        logger.info("  Executing: %s" % " ".join(command_utf8))

<<<<<<< HEAD
    p = subprocess.Popen(command_utf8,
                         close_fds=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    # FIXME: This may lock on too large buffer. We should move all "mail sending" code
    # to a general place and fix this for all our components (notification plugins,
    # notify.py, this one, ...)
    stdout_txt, stderr_txt = p.communicate(body.encode("utf-8"))
=======
    p = subprocess.Popen(
        command_utf8,
        close_fds=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        encoding="utf-8",
    )
    # FIXME: This may lock on too large buffer. We should move all "mail sending" code
    # to a general place and fix this for all our components (notification plugins,
    # notify.py, this one, ...)
    stdout, stderr = p.communicate(input=body)
>>>>>>> upstream/master
    exitcode = p.returncode

    logger.info('  Exitcode: %d' % exitcode)
    if exitcode != 0:
        logger.info("  Error: Failed to send the mail.")
<<<<<<< HEAD
        for line in (stdout_txt + stderr_txt).splitlines():
=======
        for line in (stdout + stderr).splitlines():
>>>>>>> upstream/master
            logger.info("  Output: %s" % line.rstrip())
        return False

    return True


<<<<<<< HEAD
def _execute_script(event_columns, body, event, logger):
    script_env = os.environ.copy()

    for key, value in _get_event_tags(event_columns, event).iteritems():
        if isinstance(key, six.text_type):
            key = key.encode("utf-8")
        if isinstance(value, six.text_type):
=======
def _execute_script(event_columns: Any, body: Any, event: Any, logger: Any) -> None:
    script_env = os.environ.copy()

    for key, value in _get_event_tags(event_columns, event).items():
        if isinstance(key, str):
            key = key.encode("utf-8")
        if isinstance(value, str):
>>>>>>> upstream/master
            value = value.encode("utf-8")
        script_env["CMK_" + key.upper()] = value

    # Traps can contain 0-Bytes. We need to remove this from the script
    # body. Otherwise suprocess.Popen will crash.
    p = subprocess.Popen(
        ['/bin/bash'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        close_fds=True,
        env=script_env,
<<<<<<< HEAD
    )
    output = p.communicate(body.encode('utf-8'))[0]
    logger.info('  Exit code: %d' % p.returncode)
    if output:
        logger.info('  Output: \'%s\'' % output)


def _get_event_tags(event_columns, event):
=======
        encoding="utf-8",
    )
    stdout, _stderr = p.communicate(input=body)
    logger.info('  Exit code: %d' % p.returncode)
    if stdout:
        logger.info('  Output: \'%s\'' % stdout)


def _get_event_tags(event_columns: Any, event: Any) -> Dict[Any, Any]:
>>>>>>> upstream/master
    substs = [
        ("match_group_%d" % (nr + 1), g) for (nr, g) in enumerate(event.get("match_groups", ()))
    ]

    for key, defaultvalue in event_columns:
        varname = key[6:]
        substs.append((varname, event.get(varname, defaultvalue)))

<<<<<<< HEAD
    def to_string(v):
        if isinstance(v, six.string_types):
=======
    def to_string(v: Any) -> str:
        if isinstance(v, str):
>>>>>>> upstream/master
            return v
        return "%s" % v

    tags = {}
    for key, value in substs:
        if isinstance(value, tuple):
            value = " ".join(map(to_string, value))
        else:
            value = to_string(value)

        tags[key] = value

    return tags


#.
#   .--Notification--------------------------------------------------------.
#   |         _   _       _   _  __ _           _   _                      |
#   |        | \ | | ___ | |_(_)/ _(_) ___ __ _| |_(_) ___  _ __           |
#   |        |  \| |/ _ \| __| | |_| |/ __/ _` | __| |/ _ \| '_ \          |
#   |        | |\  | (_) | |_| |  _| | (_| (_| | |_| | (_) | | | |         |
#   |        |_| \_|\___/ \__|_|_| |_|\___\__,_|\__|_|\___/|_| |_|         |
#   |                                                                      |
#   +----------------------------------------------------------------------+
<<<<<<< HEAD
#   |  EC create Check_MK native notifications via cmk --notify.           |
=======
#   |  EC create Checkmk native notifications via cmk --notify.           |
>>>>>>> upstream/master
#   '----------------------------------------------------------------------'

# Es fehlt:
# - Wenn CONTACTS fehlen, dann müssen in notify.py die Fallbackadressen
#   genommen werden.
# - Was ist mit Nagios als Core. Sendet der CONTACTS? Nein!!
#
# - Das muss sich in den Hilfetexten wiederspiegeln


<<<<<<< HEAD
# This function creates a Check_MK Notification for a locally running Check_MK.
# We simulate a *service* notification.
def do_notify(event_server, logger, event, username=None, is_cancelling=False):
=======
# This function creates a Checkmk Notification for a locally running Checkmk.
# We simulate a *service* notification.
def do_notify(event_server: Any,
              logger: Logger,
              event: Any,
              username: Optional[bool] = None,
              is_cancelling: bool = False) -> None:
>>>>>>> upstream/master
    if _core_has_notifications_disabled(event, logger):
        return

    context = _create_notification_context(event_server, event, username, is_cancelling, logger)

    if logger.isEnabledFor(VERBOSE):
        logger.log(VERBOSE, "Sending notification via Check_MK with the following context:")
<<<<<<< HEAD
        for varname, value in sorted(context.iteritems()):
=======
        for varname, value in sorted(context.items()):
>>>>>>> upstream/master
            logger.log(VERBOSE, "  %-25s: %s", varname, value)

    if context["HOSTDOWNTIME"] != "0":
        logger.info("Host %s is currently in scheduled downtime. "
                    "Skipping notification of event %s." % (context["HOSTNAME"], event["id"]))
        return

    # Send notification context via stdin.
<<<<<<< HEAD
    context_string = to_utf8("".join([
        "%s=%s\n" % (varname, value.replace("\n", "\\n"))
        for (varname, value) in context.iteritems()
    ]))

    p = subprocess.Popen(["cmk", "--notify", "stdin"],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         close_fds=True)
    response = p.communicate(input=context_string)[0]
    status = p.returncode
    if status:
        logger.error("Error notifying via Check_MK: %s" % response.strip())
=======
    context_string = "".join(
        ["%s=%s\n" % (varname, value.replace("\n", "\\n")) for (varname, value) in context.items()])

    p = subprocess.Popen(
        ["cmk", "--notify", "stdin"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        close_fds=True,
        encoding="utf-8",
    )
    stdout, _stderr = p.communicate(input=context_string)
    status = p.returncode
    if status:
        logger.error("Error notifying via Check_MK: %s" % stdout.strip())
>>>>>>> upstream/master
    else:
        logger.info("Successfully forwarded notification for event %d to Check_MK" % event["id"])


<<<<<<< HEAD
def _create_notification_context(event_server, event, username, is_cancelling, logger):
=======
def _create_notification_context(event_server: Any, event: Any, username: Any, is_cancelling: bool,
                                 logger: Logger) -> Any:
>>>>>>> upstream/master
    context = _base_notification_context(event, username, is_cancelling)
    _add_infos_from_monitoring_host(event_server, context, event)  # involves Livestatus query
    _add_contacts_from_rule(context, event, logger)
    return context


<<<<<<< HEAD
def _base_notification_context(event, username, is_cancelling):
=======
def _base_notification_context(event: Any, username: Any, is_cancelling: bool) -> Dict[str, Any]:
>>>>>>> upstream/master
    return {
        "WHAT": "SERVICE",
        "CONTACTNAME": "check-mk-notify",
        "DATE": str(int(event["last"])),  # -> Event: Time
        "MICROTIME": str(int(event["last"] * 1000000)),
        "LASTSERVICESTATE": is_cancelling and "CRITICAL"
                            or "OK",  # better assume OK, we have no transition information
        "LASTSERVICESTATEID": is_cancelling and "2" or "0",  # -> immer OK
        "LASTSERVICEOK": "0",  # 1.1.1970
        "LASTSERVICESTATECHANGE": str(int(event["last"])),
        "LONGSERVICEOUTPUT": "",
        "NOTIFICATIONAUTHOR": username or "",
        "NOTIFICATIONAUTHORALIAS": username or "",
        "NOTIFICATIONAUTHORNAME": username or "",
        "NOTIFICATIONCOMMENT": "",
        "NOTIFICATIONTYPE": is_cancelling and "RECOVERY" or "PROBLEM",
        "SERVICEACKAUTHOR": "",
        "SERVICEACKCOMMENT": "",
        "SERVICEATTEMPT": "1",
        "SERVICECHECKCOMMAND": event["rule_id"] is None and "ec-internal"
                               or "ec-rule-" + event["rule_id"],
        "SERVICEDESC": event["application"] or "Event Console",
        "SERVICENOTIFICATIONNUMBER": "1",
        "SERVICEOUTPUT": event["text"],
        "SERVICEPERFDATA": "",
        "SERVICEPROBLEMID": "ec-id-" + str(event["id"]),
        "SERVICESTATE": cmk.utils.defines.service_state_name(event["state"]),
        "SERVICESTATEID": str(event["state"]),
        "SERVICE_EC_CONTACT": event.get("owner", ""),
        "SERVICE_SL": str(event["sl"]),
        "SVC_SL": str(event["sl"]),

        # Some fields only found in EC notifications
        "EC_ID": str(event["id"]),
        "EC_RULE_ID": event["rule_id"] or "",
        "EC_PRIORITY": str(event["priority"]),
        "EC_FACILITY": str(event["facility"]),
        "EC_PHASE": event["phase"],
        "EC_COMMENT": event.get("comment", ""),
        "EC_OWNER": event.get("owner", ""),
        "EC_CONTACT": event.get("contact", ""),
        "EC_PID": str(event.get("pid", 0)),
        "EC_MATCH_GROUPS": "\t".join(event["match_groups"]),
        "EC_CONTACT_GROUPS": " ".join(event.get("contact_groups") or []),
        "EC_ORIG_HOST": event.get("orig_host", event["host"]),
    }


# "CONTACTS" is allowed to be missing in the context, cmk --notify will
# add the fallback contacts then.
<<<<<<< HEAD
def _add_infos_from_monitoring_host(event_server, context, event):
    def _add_artificial_context_info():
=======
def _add_infos_from_monitoring_host(event_server: Any, context: Any, event: Any) -> None:
    def _add_artificial_context_info() -> None:
>>>>>>> upstream/master
        context.update({
            "HOSTNAME": event["host"],
            "HOSTALIAS": event["host"],
            "HOSTADDRESS": event["ipaddress"],
            "HOSTTAGS": "",
            "HOSTDOWNTIME": "0",  # Non existing host cannot be in scheduled downtime ;-)
            "CONTACTS": "?",  # Will trigger using fallback contacts
            "SERVICECONTACTGROUPNAMES": "",
        })

    if not event["core_host"]:
        # Host not known in active monitoring. Create artificial host context
        # as good as possible.
        _add_artificial_context_info()
        return

<<<<<<< HEAD
    host_config = event_server.host_config.get(event["core_host"])
=======
    host_config = event_server.host_config.get_config_for_host(event["core_host"], None)
>>>>>>> upstream/master
    if not host_config:
        _add_artificial_context_info()  # No config found - Host has vanished?
        return

    context.update({
        "HOSTNAME": host_config["name"],
        "HOSTALIAS": host_config["alias"],
        "HOSTADDRESS": host_config["address"],
        "HOSTTAGS": host_config["custom_variables"].get("TAGS", ""),
        "CONTACTS": ",".join(host_config["contacts"]),
        "SERVICECONTACTGROUPNAMES": ",".join(host_config["contact_groups"]),
    })

    # Add custom variables to the notification context
<<<<<<< HEAD
    for key, val in host_config["custom_variables"].iteritems():
=======
    for key, val in host_config["custom_variables"].items():
>>>>>>> upstream/master
        context["HOST_%s" % key] = val

    context["HOSTDOWNTIME"] = "1" if event["host_in_downtime"] else "0"


<<<<<<< HEAD
def _add_contacts_from_rule(context, event, logger):
=======
def _add_contacts_from_rule(context: Any, event: Any, logger: Logger) -> None:
>>>>>>> upstream/master
    # Add contact information from the rule, but only if the
    # host is unknown or if contact groups in rule have precedence

    if event.get("contact_groups") is not None and \
       event.get("contact_groups_notify") and (
           "CONTACTS" not in context or
           event.get("contact_groups_precedence", "host") != "host" or
           not event['core_host']):
        _add_contact_information_to_context(context, event["contact_groups"], logger)


<<<<<<< HEAD
def _add_contact_information_to_context(context, contact_groups, logger):
=======
def _add_contact_information_to_context(context: Any, contact_groups: Any, logger: Any) -> None:
>>>>>>> upstream/master
    contact_names = _rbn_groups_contacts(contact_groups)
    context["CONTACTS"] = ",".join(contact_names)
    context["SERVICECONTACTGROUPNAMES"] = ",".join(contact_groups)
    logger.log(VERBOSE, "Setting %d contacts %s resulting from rule contact groups %s",
               len(contact_names), ",".join(contact_names), ",".join(contact_groups))


# NOTE: This function is an exact copy from modules/notify.py. We need
<<<<<<< HEAD
# to move all this Check_MK-specific livestatus query stuff to a helper
# module in lib some day.
def _rbn_groups_contacts(groups):
=======
# to move all this Checkmk-specific livestatus query stuff to a helper
# module in lib some day.
# NOTE: Typing chaos ahead!
def _rbn_groups_contacts(groups: Any) -> Any:
>>>>>>> upstream/master
    if not groups:
        return {}
    query = "GET contactgroups\nColumns: members\n"
    for group in groups:
        query += "Filter: name = %s\n" % group
    query += "Or: %d\n" % len(groups)

    try:
<<<<<<< HEAD
        contacts = set([])
=======
        contacts: Set[str] = set()
>>>>>>> upstream/master
        for contact_list in livestatus.LocalConnection().query_column(query):
            contacts.update(contact_list)
        return contacts

    except livestatus.MKLivestatusNotFoundError:
        return []

    except Exception:
        if cmk.utils.debug.enabled():
            raise
        return []


<<<<<<< HEAD
def _core_has_notifications_disabled(event, logger):
=======
def _core_has_notifications_disabled(event: Any, logger: Logger) -> bool:
>>>>>>> upstream/master
    try:
        notifications_enabled = livestatus.LocalConnection().query_value(
            "GET status\nColumns: enable_notifications")
        if not notifications_enabled:
            logger.info("Notifications are currently disabled. Skipped notification for event %d" %
                        event["id"])
            return True
    except Exception as e:
        logger.info("Cannot determine whether notifcations are enabled in core: %s. Assuming YES." %
                    e)
<<<<<<< HEAD

    return False


def to_utf8(x):
    if isinstance(x, six.text_type):
        return x.encode("utf-8")
    return x
=======
    return False
>>>>>>> upstream/master
