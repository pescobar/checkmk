<<<<<<< HEAD
# -*- coding: utf-8 -*-
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
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master
r"""
Send notification messages to Slack
===================================

Use a slack webhook to send notification messages
"""
<<<<<<< HEAD
from __future__ import unicode_literals

from typing import Dict  # pylint: disable=unused-import
=======
from typing import Dict

from six import ensure_str
>>>>>>> upstream/master

import cmk.notification_plugins.utils as utils

COLORS = {
    "CRITICAL": "#EE0000",
    "DOWN": "#EE0000",
    "WARNING": "#FFDD00",
    "OK": "#00CC00",
    "UP": "#00CC00",
    "UNKNOWN": "#CCCCCC",
    "UNREACHABLE": "#CCCCCC",
}


<<<<<<< HEAD
def slack_msg(context):
    # type: (Dict) -> Dict
=======
def slack_msg(context: Dict) -> Dict:
>>>>>>> upstream/master
    """Build the message for slack"""

    if context.get('WHAT', None) == "SERVICE":
        color = COLORS.get(context["SERVICESTATE"])
        title = "Service {NOTIFICATIONTYPE} notification".format(**context)
        text = "Host: {host_link} (IP: {HOSTADDRESS})\nService: {service_link}\nState: {SERVICESTATE}".format(
<<<<<<< HEAD
            host_link=utils.format_link('<%s|%s>', utils.host_url_from_context(context),
                                        context['HOSTNAME']),
            service_link=utils.format_link('<%s|%s>', utils.service_url_from_context(context),
=======
            host_link=utils.format_link(ensure_str('<%s|%s>'), utils.host_url_from_context(context),
                                        context['HOSTNAME']),
            service_link=utils.format_link(ensure_str('<%s|%s>'),
                                           utils.service_url_from_context(context),
>>>>>>> upstream/master
                                           context['SERVICEDESC']),
            **context)
        output = context["SERVICEOUTPUT"]
    else:
        color = COLORS.get(context["HOSTSTATE"])
        title = "Host {NOTIFICATIONTYPE} notification".format(**context)
        text = "Host: {host_link} (IP: {HOSTADDRESS})\nState: {HOSTSTATE}".format(
<<<<<<< HEAD
            host_link=utils.format_link('<%s|%s>', utils.host_url_from_context(context),
=======
            host_link=utils.format_link(ensure_str('<%s|%s>'), utils.host_url_from_context(context),
>>>>>>> upstream/master
                                        context['HOSTNAME']),
            **context)
        output = context["HOSTOUTPUT"]

    return {
        "attachments": [
            {
                "color": color,
                "title": title,
                "text": text,
            },
            {
                "color": color,
                "title": "Additional Info",
                "text": output + "\nPlease take a look: " +
                        ", ".join(map("@{}".format, context["CONTACTNAME"].split(','))),
                "footer": "Check_MK notification: {LONGDATETIME}".format(**context),
            },
        ]
    }
