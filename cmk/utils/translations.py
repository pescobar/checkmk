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

from cmk.utils.regex import regex


def translate_hostname(translation, hostname):
    return _translate(translation, hostname)


def translate_service_description(translation, service_description):
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import Dict
import ipaddress

from cmk.utils.regex import regex
from cmk.utils.type_defs import ServiceName

TranslationOptions = Dict  # TODO: Improve this type


def translate_hostname(translation: TranslationOptions, hostname: str) -> str:
    return _translate(translation, hostname)


def translate_service_description(translation: TranslationOptions,
                                  service_description: ServiceName) -> ServiceName:
>>>>>>> upstream/master
    if service_description.strip() in \
        ["Check_MK", "Check_MK Agent",
         "Check_MK Discovery", "Check_MK inventory",
         "Check_MK HW/SW Inventory"]:
        return service_description.strip()
    return _translate(translation, service_description)


<<<<<<< HEAD
def _translate(translation, name):
=======
def _translate(translation: TranslationOptions, name: str) -> str:
>>>>>>> upstream/master
    # 1. Case conversion
    caseconf = translation.get("case")
    if caseconf == "upper":
        name = name.upper()
    elif caseconf == "lower":
        name = name.lower()

    # 2. Drop domain part (not applied to IP addresses!)
<<<<<<< HEAD
    if translation.get("drop_domain") and not name[0].isdigit():
        name = name.split(".", 1)[0]

    # 3. Multiple regular expression conversion
    if isinstance(translation.get("regex"), tuple):
        translations = [translation.get("regex")]
=======
    if translation.get("drop_domain"):
        try:
            ipaddress.ip_address(name)
        except ValueError:
            # Drop domain if "name " is not a valid IP address
            name = name.split(".", 1)[0]

    # 3. Multiple regular expression conversion
    if isinstance(translation.get("regex"), tuple):
        translations = [translation["regex"]]
>>>>>>> upstream/master
    else:
        translations = translation.get("regex", [])

    for expr, subst in translations:
        if not expr.endswith('$'):
            expr += '$'
        rcomp = regex(expr)
        # re.RegexObject.sub() by hand to handle non-existing references
        mo = rcomp.match(name)
        if mo:
            name = subst
            for nr, text in enumerate(mo.groups("")):
                name = name.replace("\\%d" % (nr + 1), text)
            break

    # 4. Explicity mapping
    for from_name, to_name in translation.get("mapping", []):
        if from_name == name:
            name = to_name
            break

    return name.strip()
