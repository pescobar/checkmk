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

from typing import List, Tuple as _Tuple
>>>>>>> upstream/master
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Age,
    CascadingDropdown,
    Dictionary,
    Filesize,
    Integer,
    ListOf,
    ListOfTimeRanges,
    MonitoringState,
<<<<<<< HEAD
    TextAscii,
    Transform,
    Tuple,
=======
    RegExpUnicode,
    TextAscii,
    Transform,
    Tuple,
    ValueSpec,
>>>>>>> upstream/master
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersStorage,
    HostRulespec,
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

def _valuespec_fileinfo_groups():
    return ListOf(
        Tuple(
            help=_("This defines one file grouping pattern."),
            show_titles=True,
            orientation="horizontal",
            elements=[
                TextAscii(
                    title=_("Name of group"),
                    size=10,
                ),
                Transform(Tuple(
                    show_titles=True,
                    orientation="vertical",
                    elements=[
                        TextAscii(title=_("Include Pattern"), size=40),
                        TextAscii(title=_("Exclude Pattern"), size=40),
                    ],
                ),
                          forth=lambda params: isinstance(params, str) and (params, '') or params),
            ],
        ),
        title=_('File Grouping Patterns'),
        help=_('The check <tt>fileinfo</tt> monitors the age and size of '
               'a single file. Each file information that is sent '
               'by the agent will create one service. By defining grouping '
               'patterns you can switch to the check <tt>fileinfo.groups</tt>. '
               'That check monitors a list of files at once. You can set levels '
               'not only for the total size and the age of the oldest/youngest '
               'file but also on the count. You can define one or several '
               'patterns for a group containing <tt>*</tt> and <tt>?</tt>, for example '
               '<tt>/var/log/apache/*.log</tt>. Please see Python\'s fnmatch for more '
               'information regarding globbing patterns and special characters. '
               'If the pattern begins with a tilde then this pattern is interpreted as '
               'a regular expression instead of as a filename globbing pattern and '
               '<tt>*</tt> and <tt>?</tt> are treated differently. '
               'For files contained in a group '
               'the discovery will automatically create a group service instead '
               'of single services for each file. This rule also applies when '
               'you use manually configured checks instead of inventorized ones. '
               'Furthermore, the current time/date in a configurable format '
               'may be included in the include pattern. The syntax is as follows: '
               '$DATE:format-spec$ or $YESTERDAY:format-spec$, where format-spec '
               'is a list of time format directives of the unix date command. '
               'Example: $DATE:%Y%m%d$ is todays date, e.g. 20140127. A pattern '
               'of /var/tmp/backups/$DATE:%Y%m%d$.txt would search for .txt files '
               'with todays date  as name in the directory /var/tmp/backups. '
               'The YESTERDAY syntax simply subtracts one day from the reference time.'),
        add_label=_("Add pattern group"),
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupCheckParametersStorage,
        match_type="all",
        name="fileinfo_groups",
        valuespec=_valuespec_fileinfo_groups,
    ))


def _item_spec_fileinfo_groups():
    return TextAscii(
        title=_("File Group Name"),
        help=_(
            "This name must match the name of the group defined "
            "in the <a href=\"wato.py?mode=edit_ruleset&varname=fileinfo_groups\">%s</a> ruleset.")
        % (_('File Grouping Patterns')),
        allow_empty=True)


def _parameter_valuespec_fileinfo_groups():
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
            ("minsize",
             Tuple(
                 title=_("Minimal size"),
                 elements=[
                     Filesize(title=_("Warning if below")),
                     Filesize(title=_("Critical if below")),
                 ],
             )),
            ("maxsize",
             Tuple(
                 title=_("Maximal size"),
                 elements=[
                     Filesize(title=_("Warning if above")),
                     Filesize(title=_("Critical if above")),
                 ],
             )),
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
            ("timeofday",
             ListOfTimeRanges(
                 title=_("Only check during the following times of the day"),
                 help=_("Outside these ranges the check will always be OK"),
             )),
            ("conjunctions",
             ListOf(
                 Tuple(elements=[
                     MonitoringState(title=_("Monitoring state"), default_value=2),
                     ListOf(
                         CascadingDropdown(
                             orientation="horizontal",
                             choices=[
                                 ("count", _("File count at"), Integer()),
                                 ("count_lower", _("File count below"), Integer()),
                                 ("size", _("File size at"), Filesize()),
                                 ("size_lower", _("File size below"), Filesize()),
                                 ("largest_size", _("Largest file size at"), Filesize()),
                                 ("largest_size_lower", _("Largest file size below"), Filesize()),
                                 ("smallest_size", _("Smallest file size at"), Filesize()),
                                 ("smallest_size_lower", _("Smallest file size below"), Filesize()),
                                 ("oldest_age", _("Oldest file age at"), Age()),
                                 ("oldest_age_lower", _("Oldest file age below"), Age()),
                                 ("newest_age", _("Newest file age at"), Age()),
                                 ("newest_age_lower", _("Newest file age below"), Age()),
                             ],
                         ),
                         magic="@#@#",
                     )
                 ],),
                 title=_("Level conjunctions"),
                 help=
                 _("In order to check dependent file group statistics you can configure "
                   "conjunctions of single levels now. A conjunction consists of a monitoring state "
                   "and any number of upper or lower levels. If all of the configured levels within "
                   "a conjunction are reached then the related state is reported."),
             )),
<<<<<<< HEAD
        ],
        ignored_keys=["precompiled_patterns"],
=======
            ("additional_rules",
             ListOf(
                 Tuple(elements=[
                     RegExpUnicode(title=_("Filename/- expression"), mode="case_sensitive"),
                     Dictionary(elements=file_size_age_elements),
                 ],),
                 title=_("Additional rules for files"),
                 help=_("You can specify a filename or a regular expresion, and additional "
                        "rules that are applied to the matching files. This means that the "
                        "rules set for the whole file group are overwritten for those files. "
                        "Note that the order in which you specify the rules matters: "
                        "in case of multiple matching rules, the first matching rule is "
                        "applied."),
             )),
        ],
        ignored_keys=["precompiled_patterns", "group_patterns"],
>>>>>>> upstream/master
    )


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="fileinfo-groups",
        group=RulespecGroupCheckParametersStorage,
        item_spec=_item_spec_fileinfo_groups,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_fileinfo_groups,
        title=lambda: _("Size, age and count of file groups"),
    ))
