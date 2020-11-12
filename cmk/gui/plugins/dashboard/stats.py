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
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import abc
from typing import Tuple, List
>>>>>>> upstream/master

from livestatus import MKLivestatusNotFoundError
import cmk.gui.sites as sites
import cmk.gui.visuals as visuals
from cmk.gui.i18n import _
<<<<<<< HEAD
from cmk.gui.globals import html
from cmk.gui.htmllib import HTML

from cmk.gui.plugins.visuals.utils import FilterCRESite
=======
from cmk.gui.globals import html, request
from cmk.gui.htmllib import HTML

>>>>>>> upstream/master
from cmk.gui.plugins.dashboard import (
    Dashlet,
    dashlet_registry,
)

<<<<<<< HEAD

class DashletStats(six.with_metaclass(abc.ABCMeta, Dashlet)):
=======
from cmk.gui.utils.urls import makeuri_contextless


class DashletStats(Dashlet, metaclass=abc.ABCMeta):
>>>>>>> upstream/master
    @classmethod
    def is_resizable(cls):
        return False

    @classmethod
    def initial_size(cls):
        return (30, 18)

    @classmethod
    def initial_refresh_interval(cls):
        return 60

<<<<<<< HEAD
=======
    @classmethod
    def has_context(cls):
        return True

>>>>>>> upstream/master
    @abc.abstractmethod
    def _livestatus_table(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def _table(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def _filter(self):
        raise NotImplementedError()

<<<<<<< HEAD
    # TODO: Refactor this method
    def show(self):
        # pie_id, what, table, filter, dashlet):
=======
    @abc.abstractmethod
    def _view_name(self):
        raise NotImplementedError()

    # TODO: Refactor this method
    def show(self):
>>>>>>> upstream/master
        pie_id = "dashlet_%d" % self._dashlet_id
        pie_diameter = 130
        pie_left_aspect = 0.5
        pie_right_aspect = 0.8
<<<<<<< HEAD
        what = self._livestatus_table()
        table = self._table()
        filter_ = self._filter()

        if what == 'hosts':
            info = 'host'
            infos = [info]
        else:
            info = 'service'
            infos = ['host', 'service']
        use_filters = visuals.filters_of_visual(self._dashlet_spec, infos)
        for filt in use_filters:
            if filt.available() and not isinstance(filt, FilterCRESite):
                filter_ += filt.filter(info)

        query = "GET %s\n" % what
        for entry in table:
            query += entry[3]
        query += filter_

        site = self._dashlet_spec['context'].get('siteopt', {}).get('site')
        if site:
            sites.live().set_only_sites([site])
            result = sites.live().query_row(query)
            sites.live().set_only_sites()
=======
        table = self._table()

        filter_headers, only_sites = visuals.get_filter_headers(table=self._livestatus_table(),
                                                                infos=self.infos(),
                                                                context=self.context)

        query = "GET %s\n" % self._livestatus_table()
        for entry in table:
            query += entry[3]
        query += self._filter() + filter_headers

        if only_sites:
            try:
                sites.live().set_only_sites(only_sites)
                result: List[int] = sites.live().query_row(query)
            finally:
                sites.live().set_only_sites()
>>>>>>> upstream/master
        else:
            try:
                result = sites.live().query_summed_stats(query)
            except MKLivestatusNotFoundError:
                result = []

<<<<<<< HEAD
        pies = zip(table, result)
=======
        pies = list(zip(table, result))
>>>>>>> upstream/master
        total = sum([x[1] for x in pies])

        html.open_div(class_="stats")
        html.canvas('',
                    class_="pie",
                    id_="%s_stats" % pie_id,
<<<<<<< HEAD
                    width=pie_diameter,
                    height=pie_diameter,
=======
                    width="%d" % pie_diameter,
                    height="%d" % pie_diameter,
>>>>>>> upstream/master
                    style="float: left")
        html.img(html.theme_url("images/globe.png"), class_="globe")

        html.open_table(class_=["hoststats"] + (["narrow"] if len(pies) > 0 else []),
                        style="float:left")

<<<<<<< HEAD
        table_entries = pies
        while len(table_entries) < 6:
            table_entries = table_entries + [(("", None, "", ""), HTML("&nbsp;"))]
        table_entries.append(((_("Total"), "", "all%s" % what, ""), total))

        for (name, color, viewurl, query), count in table_entries:
            url = "view.py?view_name=" + viewurl + "&filled_in=filter&search=1"
            for filter_name, url_params in self._dashlet_spec['context'].items():
                if filter_name == "wato_folder" and html.request.has_var("wato_folder"):
                    url += "&wato_folder=" + html.request.var("wato_folder")

                elif filter_name == "svcstate":
                    # The svcstate filter URL vars are controlled by dashlet
                    continue

                else:
                    url += '&' + html.urlencode_vars(url_params.items())
=======
        table_entries: List[Tuple] = []
        table_entries += pies
        while len(table_entries) < 6:
            table_entries = table_entries + [(("", None, [], ""), HTML("&nbsp;"))]
        table_entries.append(((_("Total"), "", [], ""), total))

        for (name, color, table_url_vars, query), count in table_entries:
            url_vars = [
                ("view_name", self._view_name()),
                ("filled_in", "filter"),
                ("search", "1"),
            ] + table_url_vars + self._dashlet_context_vars()
            url = makeuri_contextless(request, url_vars, filename="view.py")
>>>>>>> upstream/master

            html.open_tr()
            html.th(html.render_a(name, href=url))
            html.td('', class_="color", style="background-color: %s" % color if color else '')
            html.td(html.render_a(count, href=url))
            html.close_tr()

        html.close_table()

        pie_parts = []
        if total > 0:
            # Count number of non-empty classes
            num_nonzero = 0
<<<<<<< HEAD
            for info, value in pies:
=======
            for _info, value in pies:
>>>>>>> upstream/master
                if value > 0:
                    num_nonzero += 1

            # Each non-zero class gets at least a view pixels of visible thickness.
            # We reserve that space right now. All computations are done in percent
            # of the radius.
            separator = 0.02  # 3% of radius
            remaining_separatorspace = num_nonzero * separator  # space for separators
            remaining_radius = 1 - remaining_separatorspace  # remaining space
            remaining_part = 1.0  # keep track of remaining part, 1.0 = 100%

            # Loop over classes, begin with most outer sphere. Inner spheres show
            # worse states and appear larger to the user (which is the reason we
            # are doing all this stuff in the first place)
<<<<<<< HEAD
            for (name, color, viewurl, _q), value in pies[::1]:
=======
            for (name, color, _unused, _q), value in pies[::1]:
>>>>>>> upstream/master
                if value > 0 and remaining_part > 0:  # skip empty classes

                    # compute radius of this sphere *including all inner spheres!* The first
                    # sphere always gets a radius of 1.0, of course.
                    radius = remaining_separatorspace + remaining_radius * (remaining_part**
                                                                            (1 / 3.0))
                    pie_parts.append('chart_pie("%s", %f, %f, %r, true);' %
                                     (pie_id, pie_right_aspect, radius, color))
                    pie_parts.append('chart_pie("%s", %f, %f, %r, false);' %
                                     (pie_id, pie_left_aspect, radius, color))

                    # compute relative part of this class
                    part = float(value) / total  # ranges from 0 to 1
                    remaining_part -= part
                    remaining_separatorspace -= separator

        html.close_div()

        html.javascript(
            """
function chart_pie(pie_id, x_scale, radius, color, right_side) {
    var context = document.getElementById(pie_id + "_stats").getContext('2d');
    if (!context)
        return;
    var pie_x = %(x)f;
    var pie_y = %(y)f;
    var pie_d = %(d)f;
    context.fillStyle = color;
    context.save();
    context.translate(pie_x, pie_y);
    context.scale(x_scale, 1);
    context.beginPath();
    if(right_side)
        context.arc(0, 0, (pie_d / 2) * radius, 1.5 * Math.PI, 0.5 * Math.PI, false);
    else
        context.arc(0, 0, (pie_d / 2) * radius, 0.5 * Math.PI, 1.5 * Math.PI, false);
    context.closePath();
    context.fill();
    context.restore();
    context = null;
}


if (cmk.dashboard.has_canvas_support()) {
    %(p)s
}
""" % {
                "x": int(pie_diameter / 2.0),
                "y": int(pie_diameter / 2.0),
                "d": pie_diameter,
                'p': '\n'.join(pie_parts)
            })


@dashlet_registry.register
class HostStatsDashlet(DashletStats):
    """Dashlet that displays statistics about host states as globe and a table"""
    @classmethod
    def type_name(cls):
        return "hoststats"

    @classmethod
    def title(cls):
        return _("Host Statistics")

    @classmethod
    def description(cls):
        return _("Displays statistics about host states as globe and a table.")

    @classmethod
    def sort_index(cls):
        return 45

<<<<<<< HEAD
    def _livestatus_table(self):
        return "hosts"

    # TODO: Refactor this data structure
    def _table(self):
        return [
           ( _("Up"), "#0b3",
            "searchhost&is_host_scheduled_downtime_depth=0&hst0=on",
            "Stats: state = 0\n" \
            "Stats: scheduled_downtime_depth = 0\n" \
            "StatsAnd: 2\n"),

           ( _("Down"), "#f00",
            "searchhost&is_host_scheduled_downtime_depth=0&hst1=on",
            "Stats: state = 1\n" \
            "Stats: scheduled_downtime_depth = 0\n" \
            "StatsAnd: 2\n"),

           ( _("Unreachable"), "#f80",
            "searchhost&is_host_scheduled_downtime_depth=0&hst2=on",
            "Stats: state = 2\n" \
            "Stats: scheduled_downtime_depth = 0\n" \
            "StatsAnd: 2\n"),

           ( _("In Downtime"), "#0af",
            "searchhost&search=1&is_host_scheduled_downtime_depth=1",
            "Stats: scheduled_downtime_depth > 0\n" \
           )
=======
    @classmethod
    def infos(cls) -> List[str]:
        return ["host"]

    def _livestatus_table(self):
        return "hosts"

    def _view_name(self):
        return "searchhost"

    # TODO: Refactor this data structure
    def _table(self):
        return [
            (
                _("Up"),
                "#0b3",
                [("is_host_scheduled_downtime_depth", "0"), ("hst0", "on")],
                "Stats: state = 0\n"  #
                "Stats: scheduled_downtime_depth = 0\n"  #
                "StatsAnd: 2\n"),
            (
                _("Down"),
                "#f00",
                [("is_host_scheduled_downtime_depth", "0"), ("hst1", "on")],
                "Stats: state = 1\n"  #
                "Stats: scheduled_downtime_depth = 0\n"  #
                "StatsAnd: 2\n"),
            (
                _("Unreachable"),
                "#f80",
                [("is_host_scheduled_downtime_depth", "0"), ("hst2", "on")],
                "Stats: state = 2\n"  #
                "Stats: scheduled_downtime_depth = 0\n"  #
                "StatsAnd: 2\n"),
            (_("In Downtime"), "#0af", [
                ("searchhost&search", "1"),
                ("is_host_scheduled_downtime_depth", "1"),
            ], "Stats: scheduled_downtime_depth > 0\n")
>>>>>>> upstream/master
        ]

    def _filter(self):
        return "Filter: custom_variable_names < _REALNAME\n"


@dashlet_registry.register
class ServiceStatsDashlet(DashletStats):
    """Dashlet that displays statistics about service states as globe and a table"""
    @classmethod
    def type_name(cls):
        return "servicestats"

    @classmethod
    def title(cls):
        return _("Service Statistics")

    @classmethod
    def description(cls):
        return _("Displays statistics about service states as globe and a table.")

    @classmethod
    def sort_index(cls):
        return 50

<<<<<<< HEAD
    def _livestatus_table(self):
        return "services"

    def _table(self):
        return [
           ( _("OK"), "#0b3",
            "searchsvc&hst0=on&st0=on&is_in_downtime=0",
            "Stats: state = 0\n" \
            "Stats: scheduled_downtime_depth = 0\n" \
            "Stats: host_scheduled_downtime_depth = 0\n" \
            "Stats: host_state = 0\n" \
            "Stats: host_has_been_checked = 1\n" \
            "StatsAnd: 5\n"),

           ( _("In Downtime"), "#0af",
            "searchsvc&is_in_downtime=1",
            "Stats: scheduled_downtime_depth > 0\n" \
            "Stats: host_scheduled_downtime_depth > 0\n" \
            "StatsOr: 2\n"),

           ( _("On Down host"), "#048",
            "searchsvc&hst1=on&hst2=on&hstp=on&is_in_downtime=0",
            "Stats: scheduled_downtime_depth = 0\n" \
            "Stats: host_scheduled_downtime_depth = 0\n" \
            "Stats: host_state != 0\n" \
            "StatsAnd: 3\n"),

           ( _("Warning"), "#ff0",
            "searchsvc&hst0=on&st1=on&is_in_downtime=0",
            "Stats: state = 1\n" \
            "Stats: scheduled_downtime_depth = 0\n" \
            "Stats: host_scheduled_downtime_depth = 0\n" \
            "Stats: host_state = 0\n" \
            "Stats: host_has_been_checked = 1\n" \
            "StatsAnd: 5\n"),

           ( _("Unknown"), "#f80",
            "searchsvc&hst0=on&st3=on&is_in_downtime=0",
            "Stats: state = 3\n" \
            "Stats: scheduled_downtime_depth = 0\n" \
            "Stats: host_scheduled_downtime_depth = 0\n" \
            "Stats: host_state = 0\n" \
            "Stats: host_has_been_checked = 1\n" \
            "StatsAnd: 5\n"),

           ( _("Critical"), "#f00",
            "searchsvc&hst0=on&st2=on&is_in_downtime=0",
            "Stats: state = 2\n" \
            "Stats: scheduled_downtime_depth = 0\n" \
            "Stats: host_scheduled_downtime_depth = 0\n" \
            "Stats: host_state = 0\n" \
            "Stats: host_has_been_checked = 1\n" \
            "StatsAnd: 5\n"),
=======
    @classmethod
    def infos(cls) -> List[str]:
        return ['host', 'service']

    def _livestatus_table(self):
        return "services"

    def _view_name(self):
        return "searchsvc"

    def _table(self):
        return [
            (_("OK"), "#0b3", [("hst0", "on"), ("st0", "on"),
                               ("is_in_downtime", "0")], "Stats: state = 0\n"
             "Stats: scheduled_downtime_depth = 0\n"
             "Stats: host_scheduled_downtime_depth = 0\n"
             "Stats: host_state = 0\n"
             "Stats: host_has_been_checked = 1\n"
             "StatsAnd: 5\n"),
            (_("In Downtime"), "#0af", [("is_in_downtime", "1")],
             "Stats: scheduled_downtime_depth > 0\n"
             "Stats: host_scheduled_downtime_depth > 0\n"
             "StatsOr: 2\n"),
            (_("On Down host"), "#048", [("hst1", "on"), ("hst2", "on"), ("hstp", "on"),
                                         ("is_in_downtime", "0")],
             "Stats: scheduled_downtime_depth = 0\n"
             "Stats: host_scheduled_downtime_depth = 0\n"
             "Stats: host_state != 0\n"
             "StatsAnd: 3\n"),
            (_("Warning"), "#ff0", [("hst0", "on"), ("st1", "on"),
                                    ("is_in_downtime", "0")], "Stats: state = 1\n"
             "Stats: scheduled_downtime_depth = 0\n"
             "Stats: host_scheduled_downtime_depth = 0\n"
             "Stats: host_state = 0\n"
             "Stats: host_has_been_checked = 1\n"
             "StatsAnd: 5\n"),
            (_("Unknown"), "#f80", [("hst0", "on"), ("st3", "on"),
                                    ("is_in_downtime", "0")], "Stats: state = 3\n"
             "Stats: scheduled_downtime_depth = 0\n"
             "Stats: host_scheduled_downtime_depth = 0\n"
             "Stats: host_state = 0\n"
             "Stats: host_has_been_checked = 1\n"
             "StatsAnd: 5\n"),
            (_("Critical"), "#f00", [("hst0", "on"), ("st2", "on"),
                                     ("is_in_downtime", "0")], "Stats: state = 2\n"
             "Stats: scheduled_downtime_depth = 0\n"
             "Stats: host_scheduled_downtime_depth = 0\n"
             "Stats: host_state = 0\n"
             "Stats: host_has_been_checked = 1\n"
             "StatsAnd: 5\n"),
>>>>>>> upstream/master
        ]

    def _filter(self):
        return "Filter: host_custom_variable_names < _REALNAME\n"
