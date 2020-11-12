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

import abc
import six
from pathlib2 import Path  # pylint: disable=unused-import

import cmk.utils.store


class WatoSimpleConfigFile(six.with_metaclass(abc.ABCMeta, object)):
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import abc
from pathlib import Path

import cmk.utils.store as store


class WatoSimpleConfigFile(metaclass=abc.ABCMeta):
>>>>>>> upstream/master
    """Manage simple .mk config file containing a single dict variable

    The file handling logic is inherited from cmk.utils.store.load_from_mk_file()
    and cmk.utils.store.save_to_mk_file().
    """
<<<<<<< HEAD
    def __init__(self, config_file_path, config_variable):
        # type: (Path, str) -> None
=======
    def __init__(self, config_file_path: Path, config_variable: str) -> None:
>>>>>>> upstream/master
        self._config_file_path = config_file_path
        self._config_variable = config_variable

    def load_for_reading(self):
        return self._load_file(lock=False)

    def load_for_modification(self):
        return self._load_file(lock=True)

    def _load_file(self, lock=False):
<<<<<<< HEAD
        return cmk.utils.store.load_from_mk_file("%s" % self._config_file_path,
                                                 key=self._config_variable,
                                                 default={},
                                                 lock=lock)

    def save(self, cfg):
        self._config_file_path.parent.mkdir(mode=0o770, exist_ok=True, parents=True)
        cmk.utils.store.save_to_mk_file(str(self._config_file_path), self._config_variable, cfg)
=======
        return store.load_from_mk_file(
            "%s" % self._config_file_path,
            key=self._config_variable,
            default={},
            lock=lock,
        )

    def save(self, cfg):
        self._config_file_path.parent.mkdir(mode=0o770, exist_ok=True, parents=True)
        store.save_to_mk_file(str(self._config_file_path), self._config_variable, cfg)
>>>>>>> upstream/master

    def filter_usable_entries(self, entries):
        return entries

    def filter_editable_entries(self, entries):
        return entries
