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
# | Copyright Mathias Kettner 2016             mk@mathias-kettner.de |
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
"""This module wraps some regex handling functions used by Check_MK"""

import re
from typing import Dict, Pattern, Tuple  # pylint:disable=unused-import
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""This module wraps some regex handling functions used by Check_MK"""

import re
from typing import Any, AnyStr, Dict, Pattern, Tuple
>>>>>>> upstream/master

from cmk.utils.exceptions import MKGeneralException
from cmk.utils.i18n import _

<<<<<<< HEAD
g_compiled_regexes = {}  # type: Dict[Tuple[str, int], Pattern]


def regex(pattern, flags=0):
    # type: (str, int) -> Pattern
=======
g_compiled_regexes: Dict[Tuple[Any, int], Pattern] = {}

REGEX_HOST_NAME_CHARS = r'-0-9a-zA-Z_.'
REGEX_HOST_NAME = r'^[%s]+$' % REGEX_HOST_NAME_CHARS


def regex(pattern: AnyStr, flags: int = 0) -> Pattern[AnyStr]:
>>>>>>> upstream/master
    """Compile regex or look it up in already compiled regexes.
    (compiling is a CPU consuming process. We cache compiled regexes)."""
    try:
        return g_compiled_regexes[(pattern, flags)]
    except KeyError:
        pass

    try:
        reg = re.compile(pattern, flags=flags)
    except Exception as e:
        raise MKGeneralException(_("Invalid regular expression '%s': %s") % (pattern, e))

    g_compiled_regexes[(pattern, flags)] = reg
    return reg


<<<<<<< HEAD
def is_regex(pattern):
    # type: (str) -> bool
=======
def is_regex(pattern: str) -> bool:
>>>>>>> upstream/master
    """Checks if a string contains characters that make it neccessary
    to use regular expression logic to handle it correctly"""
    for c in pattern:
        if c in '.?*+^$|[](){}\\':
            return True
    return False


<<<<<<< HEAD
def escape_regex_chars(match):
    # type: (str) -> str
=======
def escape_regex_chars(match: str) -> str:
>>>>>>> upstream/master
    r = ""
    for c in match:
        if c in r"[]\().?{}|*^$+":
            r += "\\"
        r += c
    return r
<<<<<<< HEAD
=======


def unescape(pattern: str) -> str:
    r"""Reverse of re.escape()

    >>> from cmk.utils.regex import unescape
    >>> unescape(re.escape(r"a b c"))
    'a b c'
    >>> unescape(re.escape(r"http://abc.de/"))
    'http://abc.de/'
    >>> unescape(re.escape(r"\\u\n\c"))
    '\\\\u\\n\\c'
    >>> unescape(re.escape(r"ä b .*(C)"))
    'ä b .*(C)'
    """
    return re.sub(r'\\(.)', r'\1', pattern)
>>>>>>> upstream/master
