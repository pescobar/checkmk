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
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

from cmk.gui.i18n import _
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    RulespecGroupCheckParametersStorage,
    rulespec_registry,
)
from cmk.gui.valuespec import Dictionary, Integer, TextAscii, Tuple


<<<<<<< HEAD
def _mongodb_collections_size_tuple(title, course):
    return Tuple(title=_(title),
                 elements=[
                     Integer(title=_("Warning if %s") % course, unit=_("MiB"), minvalue=0),
                     Integer(title=_("Critical if %s") % course, unit=_("MiB"), minvalue=0),
=======
def _mongodb_collections_size_tuple(title, course, unit):
    return Tuple(title=_(title),
                 elements=[
                     Integer(title=_("Warning if %s") % course, unit=_(unit), minvalue=0),
                     Integer(title=_("Critical if %s") % course, unit=_(unit), minvalue=0),
>>>>>>> upstream/master
                 ])


def _parameter_valuespec_mongodb_collections():
    return Dictionary(elements=[
<<<<<<< HEAD
        ("levels_size", _mongodb_collections_size_tuple("Uncompressed size in memory", "above")),
        ("levels_storagesize",
         _mongodb_collections_size_tuple("Allocated for document storage", "above")),
=======
        ("levels_size",
         _mongodb_collections_size_tuple("Uncompressed size in memory", "above", "MiB")),
        ("levels_storageSize",
         _mongodb_collections_size_tuple("Allocated for document storage", "above", "MiB")),
        ("levels_totalIndexSize",
         _mongodb_collections_size_tuple("Total size of all indexes for the collection", "above",
                                         "KByte")),
>>>>>>> upstream/master
    ])


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="mongodb_collections",
        group=RulespecGroupCheckParametersStorage,
<<<<<<< HEAD
        item_spec=lambda: TextAscii(title=_(
            "Database/Collection name ('<DB name> <collection name>')"),),
=======
        item_spec=lambda: TextAscii(title=_("MongoDB Collection Size"),),
>>>>>>> upstream/master
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_mongodb_collections,
        title=lambda: _("MongoDB Collection Size"),
    ))
