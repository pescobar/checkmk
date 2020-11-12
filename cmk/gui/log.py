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

import logging
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import logging
from typing import Dict
>>>>>>> upstream/master

import cmk.utils.log
import cmk.utils.paths

logger = logging.getLogger("cmk.web")


<<<<<<< HEAD
def init_logging():
=======
def init_logging() -> None:
>>>>>>> upstream/master
    handler = logging.FileHandler("%s/web.log" % cmk.utils.paths.log_dir, encoding="UTF-8")
    handler.setFormatter(cmk.utils.log.get_formatter())
    root = logging.getLogger()
    del root.handlers[:]  # Remove all previously existing handlers
    root.addHandler(handler)


<<<<<<< HEAD
def set_log_levels(log_levels):
    for name, level in _augmented_log_levels(log_levels).iteritems():
=======
def set_log_levels(log_levels: Dict[str, int]) -> None:
    for name, level in _augmented_log_levels(log_levels).items():
>>>>>>> upstream/master
        logging.getLogger(name).setLevel(level)


# To see log entries from libraries and non-GUI code, reuse cmk.web's level.
<<<<<<< HEAD
def _augmented_log_levels(log_levels):
=======
def _augmented_log_levels(log_levels: Dict[str, int]) -> Dict[str, int]:
>>>>>>> upstream/master
    root_level = log_levels.get("cmk.web")
    all_levels = {} if root_level is None else {"": root_level, "cmk": root_level}
    all_levels.update(log_levels)
    return all_levels
