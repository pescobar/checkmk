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

import json
import time
import six

from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.plugins.views import (
    layout_registry,
    Layout,
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import json
import time
from typing import TYPE_CHECKING

from six import ensure_str

import cmk.gui.escaping as escaping
from cmk.gui.globals import html
from cmk.gui.htmllib import HTML
from cmk.gui.type_defs import Rows
from cmk.gui.plugins.views import (
    exporter_registry,
    Exporter,
>>>>>>> upstream/master
    join_row,
    output_csv_headers,
)

<<<<<<< HEAD

@layout_registry.register
class LayoutPythonRaw(Layout):
    @property
    def ident(self):
        return "python-raw"

    @property
    def title(self):
        return _("Python raw data output")

    @property
    def can_display_checkboxes(self):
        return False

    @property
    def is_hidden(self):
        return True

    def render(self, rows, view, group_cells, cells, num_columns, show_checkboxes):
        html.write(repr(rows))


@layout_registry.register
class LayoutPython(Layout):
    @property
    def ident(self):
        return "python"

    @property
    def title(self):
        return _("Python data output")

    @property
    def can_display_checkboxes(self):
        return False

    @property
    def is_hidden(self):
        return True

    def render(self, rows, view, group_cells, cells, num_columns, show_checkboxes):
        html.write_text("[\n")
        html.write(repr([cell.export_title() for cell in cells]))
        html.write_text(",\n")
        for row in rows:
            html.write_text("[")
            for cell in cells:
                joined_row = join_row(row, cell)
                _tdclass, content = cell.render_content(joined_row)
                html.write(repr(html.strip_tags(content)))
                html.write_text(",")
            html.write_text("],")
        html.write_text("\n]\n")


class JSONLayout(Layout):
    def render(self, rows, view, group_cells, cells, num_columns, show_checkboxes):
        painted_rows = []

        header_row = []
        for cell in cells:
            header_row.append(html.strip_tags(cell.export_title()))
        painted_rows.append(header_row)

        for row in rows:
            painted_row = []
            for cell in cells:
                joined_row = join_row(row, cell)
                content = cell.render_content(joined_row)[1]
                if isinstance(content, (list, dict)):
                    # Allow painters to return lists and dicts, then json encode them
                    # as such data structures without wrapping them into strings
                    pass

                else:
                    if isinstance(content, six.text_type):
                        content = content.encode("utf-8")
                    else:
                        content = "%s" % content
                    content = html.strip_tags(content.replace("<br>", "\n"))

                painted_row.append(content)

            painted_rows.append(painted_row)

        html.write(json.dumps(painted_rows, indent=True))


@layout_registry.register
class LayoutJSONExport(JSONLayout):
    @property
    def ident(self):
        return "json_export"

    @property
    def title(self):
        return _("JSON data export")

    @property
    def can_display_checkboxes(self):
        return False

    @property
    def is_hidden(self):
        return True

    def render(self, rows, view, group_cells, cells, num_columns, show_checkboxes):
        filename = '%s-%s.json' % (view['name'],
                                   time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
        if isinstance(filename, six.text_type):
            filename = filename.encode("utf-8")
        html.response.headers["Content-Disposition"] = "Attachment; filename=\"%s\"" % filename

        super(LayoutJSONExport, self).render(rows, view, group_cells, cells, num_columns,
                                             show_checkboxes)


@layout_registry.register
class LayoutJSON(JSONLayout):
    @property
    def ident(self):
        return "json"

    @property
    def title(self):
        return _("JSON data output")

    @property
    def can_display_checkboxes(self):
        return False

    @property
    def is_hidden(self):
        return True


@layout_registry.register
class LayoutJSONP(JSONLayout):
    @property
    def ident(self):
        return "jsonp"

    @property
    def title(self):
        return _("JSONP data output")

    @property
    def can_display_checkboxes(self):
        return False

    @property
    def is_hidden(self):
        return True

    def render(self, rows, view, group_cells, cells, num_columns, show_checkboxes):
        html.write("%s(\n" % html.request.var('jsonp', 'myfunction'))
        super(LayoutJSONP, self).render(rows, view, group_cells, cells, num_columns,
                                        show_checkboxes)
        html.write_text(");\n")


class CSVLayout(Layout):
    def render(self, rows, view, group_cells, cells, num_columns, show_checkboxes):
        csv_separator = html.request.var("csv_separator", ";")
        first = True
        for cell in group_cells + cells:
=======
if TYPE_CHECKING:
    from cmk.gui.views import View


def _export_python_raw(view: "View", rows: Rows) -> None:
    html.write(repr(rows))


exporter_registry.register(Exporter(
    name="python-raw",
    handler=_export_python_raw,
))


def _export_python(view: "View", rows: Rows) -> None:
    html.write_text("[\n")
    html.write(repr([cell.export_title() for cell in view.row_cells]))
    html.write_text(",\n")
    for row in rows:
        html.write_text("[")
        for cell in view.row_cells:
            joined_row = join_row(row, cell)
            content = cell.render_for_export(joined_row)

            # The aggr_treestate painters are returning a dictionary data structure (see
            # paint_aggregated_tree_state()) in case the output_format is not HTML. Only
            # remove the HTML tags from the top level strings produced by painters.
            if isinstance(content, (HTML, str)):
                content = escaping.strip_tags(content)

            html.write(repr(content))
            html.write_text(",")
        html.write_text("],")
    html.write_text("\n]\n")


exporter_registry.register(Exporter(
    name="python",
    handler=_export_python,
))


def _show_json(view: "View", rows: Rows) -> None:
    painted_rows = []

    header_row = []
    for cell in view.row_cells:
        header_row.append(escaping.strip_tags(cell.export_title()))
    painted_rows.append(header_row)

    for row in rows:
        painted_row = []
        for cell in view.row_cells:
            joined_row = join_row(row, cell)
            content = cell.render_for_export(joined_row)
            if isinstance(content, (list, dict)):
                # Allow painters to return lists and dicts, then json encode them
                # as such data structures without wrapping them into strings
                pass

            else:
                content = escaping.strip_tags(str(content).replace("<br>", "\n"))

            painted_row.append(content)

        painted_rows.append(painted_row)

    html.write(json.dumps(painted_rows, indent=True))


def _export_json(view: "View", rows: Rows) -> None:
    _show_json(view, rows)


exporter_registry.register(Exporter(
    name="json",
    handler=_export_json,
))


def _export_json_export(view: "View", rows: Rows) -> None:
    filename = '%s-%s.json' % (view.name,
                               time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
    html.response.headers["Content-Disposition"] = "Attachment; filename=\"%s\"" % ensure_str(
        filename)

    _show_json(view, rows)


exporter_registry.register(Exporter(
    name="json_export",
    handler=_export_json_export,
))


def _export_jsonp(view: "View", rows: Rows) -> None:
    html.write("%s(\n" % html.request.var('jsonp', 'myfunction'))
    _show_json(view, rows)
    html.write_text(");\n")


exporter_registry.register(Exporter(
    name="jsonp",
    handler=_export_jsonp,
))


class CSVRenderer:
    def show(self, view: "View", rows: Rows) -> None:
        csv_separator = html.request.get_str_input_mandatory("csv_separator", ";")
        first = True
        for cell in view.group_cells + view.row_cells:
>>>>>>> upstream/master
            if first:
                first = False
            else:
                html.write(csv_separator)
            content = cell.export_title()
            html.write('"%s"' % self._format_for_csv(content))

        for row in rows:
            html.write_text("\n")
            first = True
<<<<<<< HEAD
            for cell in group_cells + cells:
=======
            for cell in view.group_cells + view.row_cells:
>>>>>>> upstream/master
                if first:
                    first = False
                else:
                    html.write(csv_separator)
                joined_row = join_row(row, cell)
<<<<<<< HEAD
                _tdclass, content = cell.render_content(joined_row)
                html.write('"%s"' % self._format_for_csv(content))

    def _format_for_csv(self, raw_data):
        # raw_data can also be int, float
        content = "%s" % raw_data
        stripped = html.strip_tags(content).replace('\n', '').replace('"', '""')
        return stripped.encode("utf-8")


@layout_registry.register
class LayoutCSVExport(CSVLayout):
    @property
    def ident(self):
        return "csv_export"

    @property
    def title(self):
        return _("CSV data export")

    @property
    def can_display_checkboxes(self):
        return False

    @property
    def is_hidden(self):
        return True

    def render(self, rows, view, group_cells, cells, num_columns, show_checkboxes):
        output_csv_headers(view)

        super(LayoutCSVExport, self).render(rows, view, group_cells, cells, num_columns,
                                            show_checkboxes)


@layout_registry.register
class LayoutCSV(CSVLayout):
    @property
    def ident(self):
        return "csv"

    @property
    def title(self):
        return _("CSV data output")

    @property
    def can_display_checkboxes(self):
        return False

    @property
    def is_hidden(self):
        return True
=======
                content = cell.render_for_export(joined_row)
                html.write('"%s"' % self._format_for_csv(content))

    def _format_for_csv(self, raw_data):
        # raw_data can also be int, float, dict (labels)
        if isinstance(raw_data, dict):
            return ', '.join(["%s: %s" % (key, value) for key, value in raw_data.items()])

        return escaping.strip_tags(str(raw_data)).replace('\n', '').replace('"', '""')


def _export_csv_export(view: "View", rows: Rows) -> None:
    output_csv_headers(view.spec)
    CSVRenderer().show(view, rows)


exporter_registry.register(Exporter(
    name="csv_export",
    handler=_export_csv_export,
))


def _export_csv(view: "View", rows: Rows) -> None:
    CSVRenderer().show(view, rows)


exporter_registry.register(Exporter(
    name="csv",
    handler=_export_csv,
))
>>>>>>> upstream/master
