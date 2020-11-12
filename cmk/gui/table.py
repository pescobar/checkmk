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

from contextlib import contextmanager
import re
import json
<<<<<<< HEAD
import six

import cmk.gui.utils as utils
import cmk.gui.config as config
from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.htmllib import HTML


@contextmanager
def table_element(table_id=None, title=None, **kwargs):
    with html.plugged():
        table = Table(table_id, title, **kwargs)
=======
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Literal,
    NamedTuple,
    Optional,
    Tuple,
    Union,
    TYPE_CHECKING,
    cast,
)

from six import ensure_str

from cmk.gui.utils.html import HTML
import cmk.gui.utils as utils
import cmk.gui.config as config
import cmk.gui.escaping as escaping
from cmk.gui.i18n import _
from cmk.gui.globals import html, request
from cmk.gui.utils.urls import makeuri

if TYPE_CHECKING:
    from cmk.gui.htmllib import HTMLContent, HTMLTagAttributes
    from cmk.gui.type_defs import CSSSpec

TableHeader = NamedTuple(
    "TableHeader",
    [
        ("title", Union[int, HTML, str]),  # basically HTMLContent without None
        ("css", 'CSSSpec'),
        ("help_txt", Optional[str]),
        ("sortable", bool),
    ])

CellSpec = NamedTuple("CellSpec", [
    ("content", str),
    ("css", 'CSSSpec'),
    ("colspan", Optional[int]),
])

TableRow = NamedTuple("TableRow", [
    ("cells", List[CellSpec]),
    ("css", Optional[str]),
    ("state", int),
    ("fixed", bool),
    ("row_attributes", 'HTMLTagAttributes'),
])

GroupHeader = NamedTuple("GroupHeader", [
    ("title", str),
    ("fixed", bool),
    ("row_attributes", 'HTMLTagAttributes'),
])

TableRows = List[Union[TableRow, GroupHeader]]


@contextmanager
def table_element(
    table_id: Optional[str] = None,
    title: 'HTMLContent' = None,
    searchable: bool = True,
    sortable: bool = True,
    foldable: bool = False,
    limit: Union[None, int, Literal[False]] = None,
    output_format: str = "html",
    omit_if_empty: bool = False,
    omit_empty_columns: bool = False,
    omit_headers: bool = False,
    omit_update_header: bool = False,
    empty_text: Optional[str] = None,
    help: Optional[str] = None,  # pylint: disable=redefined-builtin
    css: Optional[str] = None,
) -> Iterator['Table']:
    with html.plugged():
        table = Table(table_id=table_id,
                      title=title,
                      searchable=searchable,
                      sortable=sortable,
                      foldable=foldable,
                      limit=limit,
                      output_format=output_format,
                      omit_if_empty=omit_if_empty,
                      omit_empty_columns=omit_empty_columns,
                      omit_headers=omit_headers,
                      omit_update_header=omit_update_header,
                      empty_text=empty_text,
                      help=help,
                      css=css)
>>>>>>> upstream/master
        try:
            yield table
        finally:
            table._finish_previous()
            table._end()


#.
#   .--Table---------------------------------------------------------------.
#   |                       _____     _     _                              |
#   |                      |_   _|_ _| |__ | | ___                         |
#   |                        | |/ _` | '_ \| |/ _ \                        |
#   |                        | | (_| | |_) | |  __/                        |
#   |                        |_|\__,_|_.__/|_|\___|                        |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   | Usage:                                                               |
#   |                                                                      |
#   |        with table_element() as table:                                |
#   |            table.row()                                               |
#   |            table.cell("header", "content")                           |
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
class Table(object):
    def __init__(self, table_id=None, title=None, **kwargs):
        super(Table, self).__init__()
        self.next_func = lambda: None
        self.next_header = None

        # Use our pagename as table id if none is specified
        table_id = table_id if table_id is not None else html.myfile

        # determine row limit
        limit = kwargs.get('limit', config.table_row_limit)
        if html.request.var('limit') == 'none' or kwargs.get("output_format", "html") != "html":
=======
class Table:
    def __init__(
        self,
        table_id: Optional[str] = None,
        title: 'HTMLContent' = None,
        searchable: bool = True,
        sortable: bool = True,
        foldable: bool = False,
        limit: Union[None, int, Literal[False]] = None,
        output_format: str = "html",
        omit_if_empty: bool = False,
        omit_empty_columns: bool = False,
        omit_headers: bool = False,
        omit_update_header: bool = False,
        empty_text: Optional[str] = None,
        help: Optional[str] = None,  # pylint: disable=redefined-builtin
        css: Optional[str] = None,
    ):
        super(Table, self).__init__()
        self.next_func = lambda: None
        self.next_header: Optional[str] = None

        # Use our pagename as table id if none is specified
        table_id = table_id if table_id is not None else html.myfile
        assert table_id is not None

        # determine row limit
        if limit is None:
            limit = config.table_row_limit
        if html.request.get_ascii_input('limit') == 'none' or output_format != "html":
>>>>>>> upstream/master
            limit = None

        self.id = table_id
        self.title = title
<<<<<<< HEAD
        self.rows = []
        self.limit = limit
        self.headers = []
        self.options = {
            "collect_headers": False,  # also: True, "finished"
            "omit_if_empty": kwargs.get("omit_if_empty", False),
            "omit_empty_columns": kwargs.get("omit_empty_columns", False),
            "omit_headers": kwargs.get("omit_headers", False),
            "searchable": kwargs.get("searchable", True),
            "sortable": kwargs.get("sortable", True),
            "foldable": kwargs.get("foldable", False),
            "output_format": kwargs.get("output_format", "html"),  # possible: html, csv, fetch
        }

        self.empty_text = kwargs.get("empty_text", _("No entries."))
        self.help = kwargs.get("help", None)
        self.css = kwargs.get("css", None)
=======
        self.rows: TableRows = []
        self.limit = limit
        self.limit_reached = False
        self.limit_hint: Optional[int] = None
        self.headers: List[TableHeader] = []
        self.options = {
            "collect_headers": False,  # also: True, "finished"
            "omit_if_empty": omit_if_empty,
            "omit_empty_columns": omit_empty_columns,
            "omit_headers": omit_headers,
            "omit_update_header": omit_update_header,
            "searchable": searchable,
            "sortable": sortable,
            "foldable": foldable,
            "output_format": output_format,  # possible: html, csv, fetch
        }

        self.empty_text = empty_text if empty_text is not None else _("No entries.")
        self.help = help
        self.css = css
>>>>>>> upstream/master
        self.mode = 'row'

    def row(self, *posargs, **kwargs):
        self._finish_previous()
        self.next_func = lambda: self._add_row(*posargs, **kwargs)

<<<<<<< HEAD
    def text_cell(self, *args, **kwargs):
        self.cell(*args, escape_text=True, **kwargs)

    def cell(self, *posargs, **kwargs):
        self._finish_previous()
        self.next_func = lambda: self._add_cell(*posargs, **kwargs)

    def _finish_previous(self):
        self.next_func()
        self.next_func = lambda: None

    def _add_row(self, css=None, state=0, collect_headers=True, fixed=False, **attrs):
        if self.next_header:
            self.rows.append((self.next_header, None, "header", True, attrs))
            self.next_header = None
        self.rows.append(([], css, state, fixed, attrs))
=======
    def text_cell(
        self,
        title: 'HTMLContent' = "",
        text: 'HTMLContent' = "",
        css: 'CSSSpec' = None,
        help_txt: Optional[str] = None,
        colspan: Optional[int] = None,
        sortable: bool = True,
    ):
        self.cell(title=title,
                  text=text,
                  css=css,
                  help_txt=help_txt,
                  colspan=colspan,
                  escape_text=True)

    def cell(
        self,
        title: 'HTMLContent' = "",
        text: 'HTMLContent' = "",
        css: 'CSSSpec' = None,
        help_txt: Optional[str] = None,
        colspan: Optional[int] = None,
        sortable: bool = True,
        escape_text: bool = False,
    ):
        self._finish_previous()
        self.next_func = lambda: self._add_cell(title=title,
                                                text=text,
                                                css=css,
                                                help_txt=help_txt,
                                                colspan=colspan,
                                                sortable=sortable,
                                                escape_text=escape_text)

    def _finish_previous(self) -> None:
        self.next_func()
        self.next_func = lambda: None

    def _add_row(self,
                 css: Optional[str] = None,
                 state: int = 0,
                 collect_headers: bool = True,
                 fixed: bool = False,
                 **attrs: Any) -> None:
        if self.next_header:
            self.rows.append(GroupHeader(title=self.next_header, fixed=True, row_attributes=attrs))
            self.next_header = None
        self.rows.append(TableRow([], css, state, fixed, attrs))
>>>>>>> upstream/master
        if collect_headers:
            if self.options["collect_headers"] is False:
                self.options["collect_headers"] = True
            elif self.options["collect_headers"] is True:
                self.options["collect_headers"] = "finished"
        elif not collect_headers and self.options["collect_headers"] is True:
            self.options["collect_headers"] = False

<<<<<<< HEAD
    def _add_cell(self,
                  title="",
                  text="",
                  css=None,
                  help_txt=None,
                  colspan=None,
                  sortable=True,
                  escape_text=False):
        if escape_text:
            text = html.permissive_attrencode(text)
        else:
            if isinstance(text, HTML):
                text = "%s" % text
            if not isinstance(text, six.text_type):
                text = str(text)

        htmlcode = text + html.drain()
=======
        self.limit_reached = False if self.limit is None else len(self.rows) > self.limit

    def _add_cell(
        self,
        title: 'HTMLContent' = "",
        text: 'HTMLContent' = "",
        css: 'CSSSpec' = None,
        help_txt: Optional[str] = None,
        colspan: Optional[int] = None,
        sortable: bool = True,
        escape_text: bool = False,
    ):
        if escape_text:
            cell_text = escaping.escape_text(text)
        else:
            if isinstance(text, HTML):
                cell_text = "%s" % text
            elif not isinstance(text, str):
                cell_text = str(text)
            else:
                cell_text = text

        htmlcode: str = cell_text + html.drain()

        if title is None:
            title = ""
>>>>>>> upstream/master

        if self.options["collect_headers"] is True:
            # small helper to make sorting introducion easier. Cells which contain
            # buttons are never sortable
            if css and 'buttons' in css and sortable:
                sortable = False
<<<<<<< HEAD
            self.headers.append((title, css, help_txt, sortable))

        self.rows[-1][0].append((htmlcode, css, colspan))

    # Intermediate title, shown as soon as there is a following row.
    # We store the group headers in the list of rows, with css None
    # and state set to "header"
    def groupheader(self, title):
        self.next_header = title

    def _end(self):
=======
            self.headers.append(
                TableHeader(title=title, css=css, help_txt=help_txt, sortable=sortable))

        current_row = self.rows[-1]
        assert isinstance(current_row, TableRow)
        current_row.cells.append(CellSpec(htmlcode, css, colspan))

    def groupheader(self, title: str) -> None:
        """Intermediate title, shown as soon as there is a following row.
        We store the group headers in the list of rows, with css None and state set to "header"
        """
        self.next_header = title

    def _end(self) -> None:
>>>>>>> upstream/master
        if not self.rows and self.options["omit_if_empty"]:
            return

        if self.options["output_format"] == "csv":
<<<<<<< HEAD
            self._write_csv(csv_separator=html.request.var("csv_separator", ";"))
=======
            self._write_csv(
                csv_separator=html.request.get_str_input_mandatory("csv_separator", ";"))
>>>>>>> upstream/master
            return

        if self.title:
            if self.options["foldable"]:
                html.begin_foldable_container(treename="table",
                                              id_=self.id,
                                              isopen=True,
                                              indent=False,
                                              title=html.render_h3(self.title,
                                                                   class_=["treeangle", "title"]))
            else:
                html.open_h3()
                html.write(self.title)
                html.close_h3()

        if self.help:
            html.help(self.help)

        if not self.rows:
            html.div(self.empty_text, class_="info")
            return

        # Controls whether or not actions are available for a table
<<<<<<< HEAD
        rows, actions_enabled, actions_visible, search_term, user_opts = self._evaluate_user_opts()
=======
        rows, actions_visible, search_term = self._evaluate_user_opts()
>>>>>>> upstream/master

        # Apply limit after search / sorting etc.
        num_rows_unlimited = len(rows)
        limit = self.limit
<<<<<<< HEAD
        if limit is not None:
            # only use rows up to the limit plus the fixed rows
            rows = [rows[i] for i in range(num_rows_unlimited) if i < limit or rows[i][3]]
            # Display corrected number of rows
            num_rows_unlimited -= len([r for r in rows if r[3]])

        # Render header
        show_action_row = self.options["searchable"] or (self.options["sortable"] and
                                                         self._get_sort_column(user_opts[self.id]))
        self._write_table(rows, show_action_row, actions_visible, search_term)

        if self.title and self.options["foldable"]:
            html.end_foldable_container()

        if limit is not None and num_rows_unlimited > limit:
            html.message(
                _('This table is limited to show only %d of %d rows. '
                  'Click <a href="%s">here</a> to disable the limitation.') %
                (limit, num_rows_unlimited, html.makeuri([('limit', 'none')])))

        if actions_enabled:
            config.user.save_file("tableoptions", user_opts)
        return

    def _evaluate_user_opts(self):
        table_id = self.id
=======
        if limit:
            # only use rows up to the limit plus the fixed rows
            limited_rows = []
            for index in range(num_rows_unlimited):
                row = rows[index]
                if index < limit or isinstance(row, GroupHeader) or row.fixed:
                    limited_rows.append(row)
            # Display corrected number of rows
            num_rows_unlimited -= len(
                [r for r in limited_rows if isinstance(row, GroupHeader) or r.fixed])
            rows = limited_rows

        # Render header
        if self.limit_hint is not None:
            num_rows_unlimited = self.limit_hint

        if limit and num_rows_unlimited > limit:

            html.show_message(
                _('This table is limited to show only %d of %d rows. '
                  'Click <a href="%s">here</a> to disable the limitation.') %
                (limit, num_rows_unlimited, makeuri(request, [('limit', 'none')])))

        self._write_table(rows, num_rows_unlimited, self._show_action_row(), actions_visible,
                          search_term)

        if self.title and self.options["foldable"]:
            html.end_foldable_container()

        return

    def _show_action_row(self) -> bool:
        if self.options["searchable"]:
            return True

        if self.options["sortable"] and self._get_sort_column(config.user.tableoptions[self.id]):
            return True

        return False

    def _evaluate_user_opts(self) -> Tuple[TableRows, bool, Optional[str]]:
        assert self.id is not None
        table_id = ensure_str(self.id)
>>>>>>> upstream/master
        rows = self.rows

        search_term = None
        actions_enabled = (self.options["searchable"] or self.options["sortable"])

        if not actions_enabled:
<<<<<<< HEAD
            return rows, False, False, None, None

        user_opts = config.user.load_file("tableoptions", {})
        user_opts.setdefault(table_id, {})
        table_opts = user_opts[table_id]

        # Handle the initial visibility of the actions
        actions_visible = user_opts[table_id].get('actions_visible', False)
        if html.request.var('_%s_actions' % table_id):
            actions_visible = html.request.var('_%s_actions' % table_id) == '1'
            user_opts[table_id]['actions_visible'] = actions_visible

        if html.request.var('_%s_reset' % table_id):
=======
            return rows, False, None

        table_opts = config.user.tableoptions.setdefault(table_id, {})

        # Handle the initial visibility of the actions
        actions_visible = table_opts.get('actions_visible', False)
        if html.request.get_ascii_input('_%s_actions' % table_id):
            actions_visible = html.request.get_ascii_input('_%s_actions' % table_id) == '1'
            table_opts['actions_visible'] = actions_visible

        if html.request.get_ascii_input('_%s_reset' % table_id):
>>>>>>> upstream/master
            html.request.del_var('_%s_search' % table_id)
            if 'search' in table_opts:
                del table_opts['search']  # persist

        if self.options["searchable"]:
            # Search is always lower case -> case insensitive
<<<<<<< HEAD
            search_term = html.get_unicode_input('_%s_search' % table_id,
                                                 table_opts.get('search', '')).lower()
=======
            search_term = html.request.get_unicode_input_mandatory('_%s_search' % table_id,
                                                                   table_opts.get('search', ''))
            search_term = search_term.lower()
>>>>>>> upstream/master
            if search_term:
                html.request.set_var('_%s_search' % table_id, search_term)
                table_opts['search'] = search_term  # persist
                rows = _filter_rows(rows, search_term)

<<<<<<< HEAD
        if html.request.var('_%s_reset_sorting' % table_id):
=======
        if html.request.get_ascii_input('_%s_reset_sorting' % table_id):
>>>>>>> upstream/master
            html.request.del_var('_%s_sort' % table_id)
            if 'sort' in table_opts:
                del table_opts['sort']  # persist

        if self.options["sortable"]:
            # Now apply eventual sorting settings
            sort = self._get_sort_column(table_opts)
            if sort is not None:
                html.request.set_var('_%s_sort' % table_id, sort)
                table_opts['sort'] = sort  # persist
                sort_col, sort_reverse = map(int, sort.split(',', 1))
                rows = _sort_rows(rows, sort_col, sort_reverse)

<<<<<<< HEAD
        return rows, actions_enabled, actions_visible, search_term, user_opts

    def _get_sort_column(self, table_opts):
        return html.request.var('_%s_sort' % self.id, table_opts.get('sort'))

    def _write_table(self, rows, actions_enabled, actions_visible, search_term):
        headinfo = _("1 row") if len(rows) == 1 else _("%d rows") % len(rows)
        html.javascript("cmk.utils.update_header_info(%s);" % json.dumps(headinfo))
=======
        if actions_enabled:
            config.user.save_tableoptions()

        return rows, actions_visible, search_term

    def _get_sort_column(self, table_opts: Dict[str, Any]) -> Optional[str]:
        return html.request.get_ascii_input('_%s_sort' % self.id, table_opts.get('sort'))

    def _write_table(self, rows: TableRows, num_rows_unlimited: int, actions_enabled: bool,
                     actions_visible: bool, search_term: Optional[str]) -> None:
        if not self.options["omit_update_header"]:
            headinfo = _("1 row") if len(rows) == 1 else _("%d rows") % num_rows_unlimited

            html.javascript("cmk.utils.update_header_info(%s);" % json.dumps(headinfo))
>>>>>>> upstream/master

        table_id = self.id

        num_cols = self._get_num_cols(rows)

        empty_columns = self._get_empty_columns(rows, num_cols)
        if self.options["omit_empty_columns"]:
            num_cols -= len([v for v in empty_columns if v])

        html.open_table(class_=["data", "oddeven", self.css])

        # If we have no group headers then paint the headers now
<<<<<<< HEAD
        if self.rows and self.rows[0][2] != "header":
=======
        if self.rows and not isinstance(self.rows[0], GroupHeader):
>>>>>>> upstream/master
            self._render_headers(
                actions_enabled,
                actions_visible,
                empty_columns,
            )

        if actions_enabled and actions_visible:
            html.open_tr(class_=["data", "even0", "actions"])
            html.open_td(colspan=num_cols)
            if not html.in_form():
                html.begin_form("%s_actions" % table_id)

            if self.options["searchable"]:
                html.open_div(class_="search")
                html.text_input("_%s_search" % table_id)
                html.button("_%s_submit" % table_id, _("Search"))
                html.button("_%s_reset" % table_id, _("Reset search"))
                html.set_focus("_%s_search" % table_id)
                html.close_div()

            if html.request.has_var('_%s_sort' % table_id):
                html.open_div(class_=["sort"])
                html.button("_%s_reset_sorting" % table_id, _("Reset sorting"))
                html.close_div()

            if not html.in_form():
                html.begin_form("%s_actions" % table_id)

            html.hidden_fields()
            html.end_form()
            html.close_tr()

<<<<<<< HEAD
        for nr, (row_spec, css, state, _fixed, attrs) in enumerate(rows):
            if not css and "class_" in attrs:
                css = attrs.pop("class_")
            if not css and "class" in attrs:
                css = attrs.pop("class")

            # Intermediate header
            if state == "header":
                # Show the header only, if at least one (non-header) row follows
                if nr < len(rows) - 1 and rows[nr + 1][2] != "header":
                    html.open_tr(class_="groupheader")
                    html.open_td(colspan=num_cols)
                    html.open_h3()
                    html.write(row_spec)
=======
        for nr, row in enumerate(rows):
            # Intermediate header
            if isinstance(row, GroupHeader):
                # Show the header only, if at least one (non-header) row follows
                if nr < len(rows) - 1 and not isinstance(rows[nr + 1], GroupHeader):
                    html.open_tr(class_="groupheader")
                    html.open_td(colspan=num_cols)
                    html.open_h3()
                    html.write(row.title)
>>>>>>> upstream/master
                    html.close_h3()
                    html.close_td()
                    html.close_tr()

                    self._render_headers(actions_enabled, actions_visible, empty_columns)
                continue

            oddeven_name = "even" if (nr - 1) % 2 == 0 else "odd"
<<<<<<< HEAD

            html.open_tr(class_=["data",
                                 "%s%d" % (oddeven_name, state), css if css else None],
                         **attrs)
            for col_index, (cell_content, css_classes, colspan) in enumerate(row_spec):
                if self.options["omit_empty_columns"] and empty_columns[col_index]:
                    continue

                html.open_td(class_=css_classes if css_classes else None,
                             colspan=colspan if colspan else None)
                html.write(cell_content)
=======
            class_ = ["data", "%s%d" % (oddeven_name, row.state)]
            if row.css:
                class_.append(row.css)
            else:
                for k in ["class_", "class"]:
                    if k in row.row_attributes:
                        cls_spec = cast('CSSSpec', row.row_attributes.pop(k))
                        if isinstance(cls_spec, list):
                            class_.extend([c for c in cls_spec if c is not None])
                        elif cls_spec is not None:
                            class_.append(cls_spec)

            html.open_tr(class_=class_, **row.row_attributes)
            for col_index, cell in enumerate(row.cells):
                if self.options["omit_empty_columns"] and empty_columns[col_index]:
                    continue

                html.open_td(class_=cell.css, colspan=cell.colspan)
                html.write(cell.content)
>>>>>>> upstream/master
                html.close_td()
            html.close_tr()

        if not rows and search_term:
            html.open_tr(class_=["data", "odd0", "no_match"])
            html.td(_('Found no matching rows. Please try another search term.'), colspan=num_cols)
            html.close_tr()

        html.close_table()

<<<<<<< HEAD
    def _get_num_cols(self, rows):
        if self.headers:
            return len(self.headers)
        elif self.rows:
            return len(self.rows[0])
        return 0

    def _get_empty_columns(self, rows, num_cols):
=======
    def _get_num_cols(self, rows: TableRows) -> int:
        if self.headers:
            return len(self.headers)
        if self.rows:
            return len(self.rows[0])
        return 0

    def _get_empty_columns(self, rows: TableRows, num_cols: int) -> List[bool]:
>>>>>>> upstream/master
        if not num_cols:
            return []

        empty_columns = [True] * num_cols
<<<<<<< HEAD
        for row_spec, _css, state, _fixed, _attrs in rows:
            if state == "header":
                continue  # Don't care about group headers

            for col_index, (cell_content, _css_classes, _colspan) in enumerate(row_spec):
                empty_columns[col_index] &= not cell_content
        return empty_columns

    def _write_csv(self, csv_separator):
        rows = self.rows
        headers = self.headers
=======
        for row in rows:
            if isinstance(row, GroupHeader):
                continue  # Don't care about group headers

            for col_index, cell in enumerate(row.cells):
                empty_columns[col_index] &= not cell.content
        return empty_columns

    def _write_csv(self, csv_separator: str) -> None:
        rows = self.rows
>>>>>>> upstream/master
        limit = self.limit
        omit_headers = self.options["omit_headers"]

        # Apply limit after search / sorting etc.
        if limit is not None:
            rows = rows[:limit]

        # If we have no group headers then paint the headers now
<<<<<<< HEAD
        if not omit_headers and self.rows and self.rows[0][2] != "header":
            html.write(
                csv_separator.join(
                    [html.strip_tags(header) or ""
                     for (header, _css, _help, _sortable) in headers]) + "\n")

        for row_spec, _css, _state, _fixed, _attrs in rows:
            html.write(
                csv_separator.join([
                    html.strip_tags(cell_content)
                    for cell_content, _css_classes, _colspan in row_spec
                ]))
            html.write("\n")

    def _render_headers(self, actions_enabled, actions_visible, empty_columns):
=======
        if not omit_headers and self.rows and not isinstance(self.rows[0], GroupHeader):
            html.write(
                csv_separator.join(
                    [escaping.strip_tags(header.title) or "" for header in self.headers]) + "\n")

        for row in rows:
            if isinstance(row, GroupHeader):
                continue

            html.write(csv_separator.join([escaping.strip_tags(cell.content) for cell in row.cells
                                          ]))
            html.write("\n")

    def _render_headers(self, actions_enabled: bool, actions_visible: bool,
                        empty_columns: List[bool]) -> None:
>>>>>>> upstream/master
        if self.options["omit_headers"]:
            return

        table_id = self.id

        html.open_tr()
        first_col = True
<<<<<<< HEAD
        for nr, (header, css, help_txt, sortable) in enumerate(self.headers):
            if self.options["omit_empty_columns"] and empty_columns[nr]:
                continue

            text = header

            if help_txt:
                header = '<span title="%s">%s</span>' % (html.attrencode(help_txt), header)

            css_class = "header_%s" % css if css else None

            if not self.options["sortable"] or not sortable:
                html.open_th(class_=css_class)
            else:
                reverse = 0
                sort = html.request.var('_%s_sort' % table_id)
=======
        for nr, header in enumerate(self.headers):
            if self.options["omit_empty_columns"] and empty_columns[nr]:
                continue

            if header.help_txt:
                header_title: Union[int, HTML, str] = html.render_span(header.title,
                                                                       title=header.help_txt)
            else:
                header_title = header.title

            if not isinstance(header.css, list):
                css_class: 'CSSSpec' = [header.css]
            else:
                css_class = header.css

            assert isinstance(css_class, list)
            css_class = [("header_%s" % c) for c in css_class if c is not None]

            if not self.options["sortable"] or not header.sortable:
                html.open_th(class_=css_class)
            else:
                css_class.insert(0, "sort")
                reverse = 0
                sort = html.request.get_ascii_input('_%s_sort' % table_id)
>>>>>>> upstream/master
                if sort:
                    sort_col, sort_reverse = map(int, sort.split(',', 1))
                    if sort_col == nr:
                        reverse = 1 if sort_reverse == 0 else 0

                action_uri = html.makeactionuri([('_%s_sort' % table_id, '%d,%d' % (nr, reverse))])
<<<<<<< HEAD
                html.open_th(class_=["sort", css_class],
                             title=_("Sort by %s") % text,
=======
                html.open_th(class_=css_class,
                             title=_("Sort by %s") % header.title,
>>>>>>> upstream/master
                             onclick="location.href='%s'" % action_uri)

            # Add the table action link
            if first_col:
                first_col = False
                if actions_enabled:
<<<<<<< HEAD
                    if not header:
                        header = "&nbsp;"  # Fixes layout problem with white triangle
=======
                    if not header_title:
                        header_title = "&nbsp;"  # Fixes layout problem with white triangle

>>>>>>> upstream/master
                    if actions_visible:
                        state = '0'
                        help_txt = _('Hide table actions')
                        img = 'table_actions_on'
                    else:
                        state = '1'
                        help_txt = _('Display table actions')
                        img = 'table_actions_off'
<<<<<<< HEAD
                    html.open_div(class_=["toggle_actions"])
                    html.icon_button(html.makeuri([('_%s_actions' % table_id, state)]),
=======

                    html.open_div(class_=["toggle_actions"])
                    html.icon_button(makeuri(request, [('_%s_actions' % table_id, state)]),
>>>>>>> upstream/master
                                     help_txt,
                                     img,
                                     cssclass='toggle_actions')
                    html.open_span()
<<<<<<< HEAD
                    html.write(header)
                    html.close_span()
                    html.close_div()
                else:
                    html.write(header)
            else:
                html.write(header)
=======
                    html.write(header_title)
                    html.close_span()
                    html.close_div()
                else:
                    html.write(header_title)
            else:
                html.write(header_title)
>>>>>>> upstream/master

            html.close_th()
        html.close_tr()


<<<<<<< HEAD
def _filter_rows(rows, search_term):
    filtered_rows = []
    match_regex = re.compile(search_term, re.IGNORECASE)

    for row_spec, css, state, fixed, attrs in rows:
        if state == "header" or fixed:
            filtered_rows.append((row_spec, css, state, fixed, attrs))
            continue  # skip filtering of headers or fixed rows

        for cell_content, _css_classes, _colspan in row_spec:
            if match_regex.search(cell_content):
                filtered_rows.append((row_spec, css, state, fixed, attrs))
=======
def _filter_rows(rows: TableRows, search_term: str) -> TableRows:
    filtered_rows: TableRows = []
    match_regex = re.compile(search_term, re.IGNORECASE)

    for row in rows:
        if isinstance(row, GroupHeader) or row.fixed:
            filtered_rows.append(row)
            continue  # skip filtering of headers or fixed rows

        for cell in row.cells:
            if match_regex.search(cell.content):
                filtered_rows.append(row)
>>>>>>> upstream/master
                break  # skip other cells when matched
    return filtered_rows


<<<<<<< HEAD
def _sort_rows(rows, sort_col, sort_reverse):
    # remove and remind fixed rows, add to separate list
    fixed_rows = []
    for index, row_spec in enumerate(rows[:]):
        if row_spec[3] is True:
            rows.remove(row_spec)
            fixed_rows.append((index, row_spec))
=======
def _sort_rows(rows: TableRows, sort_col: int, sort_reverse: int) -> TableRows:
    # remove and remind fixed rows, add to separate list
    fixed_rows = []
    for index, row in enumerate(rows[:]):
        if row.fixed:
            rows.remove(row)
            fixed_rows.append((index, row))
>>>>>>> upstream/master

    # Then use natural sorting to sort the list. Note: due to a
    # change in the number of columns of a table in different software
    # versions the cmp-function might fail. This is because the sorting
    # column is persisted in a user file. So we ignore exceptions during
    # sorting. This gives the user the chance to change the sorting and
    # see the table in the first place.
    try:
<<<<<<< HEAD
        rows.sort(key=lambda x: utils.key_num_split(html.strip_tags(x[0][sort_col][0])),
=======
        rows.sort(key=lambda x: utils.key_num_split(escaping.strip_tags(x[0][sort_col][0])),
>>>>>>> upstream/master
                  reverse=sort_reverse == 1)
    except IndexError:
        pass

    # Now re-add the removed "fixed" rows to the list again
    if fixed_rows:
<<<<<<< HEAD
        for index, row_spec in fixed_rows:
            rows.insert(index, row_spec)
=======
        for index, cells in fixed_rows:
            rows.insert(index, cells)
>>>>>>> upstream/master

    return rows
