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

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Tuple,
    Integer,
    TextAscii,
    Age,
    Filesize,
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import List, Tuple as _Tuple
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Age,
    Checkbox,
    Dictionary,
    Filesize,
    Integer,
    ListOf,
    RegExpUnicode,
    TextAscii,
    Tuple,
    ValueSpec,
>>>>>>> upstream/master
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersStorage,
)

<<<<<<< HEAD
=======
file_size_age_elements: List[_Tuple[str, ValueSpec]] = [
    ("minage_oldest",
     Tuple(
         title=_("Minimal age of oldest file"),
         elements=[
             Age(title=_("Warning if younger than")),
             Age(title=_("Critical if younger than")),
         ],
     )),
    ("maxage_oldest",
     Tuple(
         title=_("Maximal age of oldest file"),
         elements=[
             Age(title=_("Warning if older than")),
             Age(title=_("Critical if older than")),
         ],
     )),
    ("minage_newest",
     Tuple(
         title=_("Minimal age of newest file"),
         elements=[
             Age(title=_("Warning if younger than")),
             Age(title=_("Critical if younger than")),
         ],
     )),
    ("maxage_newest",
     Tuple(
         title=_("Maximal age of newest file"),
         elements=[
             Age(title=_("Warning if older than")),
             Age(title=_("Critical if older than")),
         ],
     )),
    ("minsize_smallest",
     Tuple(
         title=_("Minimal size of smallest file"),
         elements=[
             Filesize(title=_("Warning if below")),
             Filesize(title=_("Critical if below")),
         ],
     )),
    ("maxsize_smallest",
     Tuple(
         title=_("Maximal size of smallest file"),
         elements=[
             Filesize(title=_("Warning if above")),
             Filesize(title=_("Critical if above")),
         ],
     )),
    ("minsize_largest",
     Tuple(
         title=_("Minimal size of largest file"),
         elements=[
             Filesize(title=_("Warning if below")),
             Filesize(title=_("Critical if below")),
         ],
     )),
    ("maxsize_largest",
     Tuple(
         title=_("Maximal size of largest file"),
         elements=[
             Filesize(title=_("Warning if above")),
             Filesize(title=_("Critical if above")),
         ],
     )),
]

>>>>>>> upstream/master

def _item_spec_filestats():
    return TextAscii(title=_("File Group Name"),
                     help=_("This name must match the name of the section defined "
                            "in the mk_filestats configuration."),
                     allow_empty=True)


def _parameter_valuespec_filestats():
    return Dictionary(
<<<<<<< HEAD
        elements=[
            ("minage_oldest",
             Tuple(
                 title=_("Minimal age of oldest file"),
                 elements=[
                     Age(title=_("Warning if younger than")),
                     Age(title=_("Critical if younger than")),
                 ],
             )),
            ("maxage_oldest",
             Tuple(
                 title=_("Maximal age of oldest file"),
                 elements=[
                     Age(title=_("Warning if older than")),
                     Age(title=_("Critical if older than")),
                 ],
             )),
            ("minage_newest",
             Tuple(
                 title=_("Minimal age of newest file"),
                 elements=[
                     Age(title=_("Warning if younger than")),
                     Age(title=_("Critical if younger than")),
                 ],
             )),
            ("maxage_newest",
             Tuple(
                 title=_("Maximal age of newest file"),
                 elements=[
                     Age(title=_("Warning if older than")),
                     Age(title=_("Critical if older than")),
                 ],
             )),
            ("minsize_smallest",
             Tuple(
                 title=_("Minimal size of smallest file"),
                 elements=[
                     Filesize(title=_("Warning if below")),
                     Filesize(title=_("Critical if below")),
                 ],
             )),
            ("maxsize_smallest",
             Tuple(
                 title=_("Maximal size of smallest file"),
                 elements=[
                     Filesize(title=_("Warning if above")),
                     Filesize(title=_("Critical if above")),
                 ],
             )),
            ("minsize_largest",
             Tuple(
                 title=_("Minimal size of largest file"),
                 elements=[
                     Filesize(title=_("Warning if below")),
                     Filesize(title=_("Critical if below")),
                 ],
             )),
            ("maxsize_largest",
             Tuple(
                 title=_("Maximal size of largest file"),
                 elements=[
                     Filesize(title=_("Warning if above")),
                     Filesize(title=_("Critical if above")),
                 ],
             )),
=======
        elements=file_size_age_elements + [
>>>>>>> upstream/master
            ("mincount",
             Tuple(
                 title=_("Minimal file count"),
                 elements=[
                     Integer(title=_("Warning if below")),
                     Integer(title=_("Critical if below")),
                 ],
             )),
            ("maxcount",
             Tuple(
                 title=_("Maximal file count"),
                 elements=[
                     Integer(title=_("Warning if above")),
                     Integer(title=_("Critical if above")),
                 ],
             )),
<<<<<<< HEAD
        ],
        help=_("Here you can impose various levels the results reported by the"
               " mk_filstats plugin. Note that some levels only apply to a matching"
               " putput format (e.g. max/min count levels are not applied if only the"
               " smallest, largest, oldes and newest file is reported). In order to"
=======
            ("show_all_files",
             Checkbox(title=_("Show all files in long output"), label=("Show files"))),
            ("additional_rules",
             ListOf(Tuple(elements=[
                 RegExpUnicode(title=_("Filename/- expression"), mode="case_sensitive"),
                 Dictionary(elements=file_size_age_elements),
             ],),
                    title=_("Additional rules for files"),
                    help=_("You can specify a filename or a regular expresion, and additional "
                           "rules that are applied to the matching files. This means that the "
                           "rules set for the whole file group are overwritten for those files. "
                           "Note that the order in which you specify the rules matters: "
                           "in case of multiple matching rules, the first matching rule is "
                           "applied."))),
        ],
        help=_("Here you can impose various levels on the results reported by the"
               " mk_filstats plugin. Note that some levels only apply to a matching"
               " output format (e.g. max/min count levels are not applied if only the"
               " smallest, largest, oldest and newest file is reported). In order to"
>>>>>>> upstream/master
               " receive the required data, you must configure the plugin mk_filestats."),
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="filestats",
        group=RulespecGroupCheckParametersStorage,
        item_spec=_item_spec_filestats,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_filestats,
        title=lambda: _("Size, age and count of file groups (mk_filestats)"),
    ))
