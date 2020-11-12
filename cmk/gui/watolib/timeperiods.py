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

import cmk.utils.store as store
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import Dict

import cmk.utils.store as store
from cmk.utils.type_defs import TimeperiodName, TimeperiodSpec
>>>>>>> upstream/master

import cmk.gui.config as config
from cmk.gui.i18n import _
from cmk.gui.valuespec import DropdownChoice
from cmk.gui.watolib.utils import wato_root_dir
<<<<<<< HEAD


def builtin_timeperiods():
=======
from cmk.gui.globals import g

TimeperiodSpecs = Dict[TimeperiodName, TimeperiodSpec]


def builtin_timeperiods() -> TimeperiodSpecs:
>>>>>>> upstream/master
    return {
        "24X7": {
            "alias": _("Always"),
            "monday": [("00:00", "24:00")],
            "tuesday": [("00:00", "24:00")],
            "wednesday": [("00:00", "24:00")],
            "thursday": [("00:00", "24:00")],
            "friday": [("00:00", "24:00")],
            "saturday": [("00:00", "24:00")],
            "sunday": [("00:00", "24:00")],
        }
    }


<<<<<<< HEAD
def load_timeperiods():
    timeperiods = store.load_from_mk_file(wato_root_dir() + "timeperiods.mk", "timeperiods", {})
    timeperiods.update(builtin_timeperiods())
    return timeperiods


def save_timeperiods(timeperiods):
=======
def load_timeperiods() -> TimeperiodSpecs:
    if "timeperiod_information" in g:
        return g.timeperiod_information
    timeperiods = store.load_from_mk_file(wato_root_dir() + "timeperiods.mk", "timeperiods", {})
    timeperiods.update(builtin_timeperiods())

    g.timeperiod_information = timeperiods
    return timeperiods


def load_timeperiod(name: str):
    timeperiods = load_timeperiods()
    try:
        return timeperiods[name]
    except KeyError:
        return


def save_timeperiods(timeperiods: TimeperiodSpecs) -> None:
>>>>>>> upstream/master
    store.mkdir(wato_root_dir())
    store.save_to_mk_file(wato_root_dir() + "timeperiods.mk",
                          "timeperiods",
                          _filter_builtin_timeperiods(timeperiods),
                          pprint_value=config.wato_pprint_config)
<<<<<<< HEAD


def _filter_builtin_timeperiods(timeperiods):
    builtin_keys = builtin_timeperiods().keys()
=======
    g.timeperiod_information = timeperiods


def save_timeperiod(name, timeperiod) -> None:
    existing_timeperiods = load_timeperiods()
    existing_timeperiods[name] = timeperiod
    save_timeperiods(existing_timeperiods)


def verify_timeperiod_name_exists(name):
    existing_timperiods = load_timeperiods()
    return name in existing_timperiods


def _filter_builtin_timeperiods(timeperiods: TimeperiodSpecs) -> TimeperiodSpecs:
    builtin_keys = set(builtin_timeperiods().keys())
>>>>>>> upstream/master
    return {k: v for k, v in timeperiods.items() if k not in builtin_keys}


class TimeperiodSelection(DropdownChoice):
    def __init__(self, **kwargs):
        kwargs.setdefault("no_preselect", True)
        kwargs.setdefault("no_preselect_title", _("Select a timeperiod"))
        DropdownChoice.__init__(self, choices=self._get_choices, **kwargs)

    def _get_choices(self):
        timeperiods = load_timeperiods()
        elements = [(name, "%s - %s" % (name, tp["alias"])) for (name, tp) in timeperiods.items()]

        always = ("24X7", _("Always"))
        if always[0] not in dict(elements):
            elements.insert(0, always)

        return sorted(elements, key=lambda x: x[1].lower())
