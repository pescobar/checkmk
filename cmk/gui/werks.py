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

# Functions for parsing Werks and showing the users a browsable change
# log

import itertools
import os
import re
import time
<<<<<<< HEAD
=======
from typing import Any, Dict, Union, Iterator

from six import ensure_str
>>>>>>> upstream/master

import cmk.utils.store as store
import cmk.utils.paths
import cmk.utils.werks

import cmk.gui.pages
import cmk.gui.utils as utils
import cmk.gui.config as config
from cmk.gui.table import table_element
from cmk.gui.exceptions import MKUserError
from cmk.gui.i18n import _
<<<<<<< HEAD
from cmk.gui.globals import html
=======
from cmk.gui.globals import html, request
>>>>>>> upstream/master
from cmk.gui.valuespec import (
    ListChoice,
    Timerange,
    TextAscii,
    DropdownChoice,
    Tuple,
    Integer,
    TextUnicode,
)
<<<<<<< HEAD
=======
from cmk.gui.breadcrumb import (
    make_main_menu_breadcrumb,
    make_current_page_breadcrumb_item,
    BreadcrumbItem,
    Breadcrumb,
)
from cmk.gui.main_menu import mega_menu_registry
from cmk.gui.page_menu import (
    PageMenu,
    PageMenuDropdown,
    PageMenuTopic,
    PageMenuEntry,
    PageMenuSidePopup,
    make_simple_link,
    make_display_options_dropdown,
)
from cmk.gui.utils.urls import makeuri, makeuri_contextless, make_confirm_link
>>>>>>> upstream/master

acknowledgement_path = cmk.utils.paths.var_dir + "/acknowledged_werks.mk"

# Keep global variable for caching werks between requests. The never change.
<<<<<<< HEAD
g_werks = None
=======
g_werks: Dict[int, Dict[str, Any]] = {}
>>>>>>> upstream/master


@cmk.gui.pages.register("version")
def page_version():
<<<<<<< HEAD
    html.header(_("Check_MK %s Release Notes") % cmk.__version__)
    load_werks()
    handle_acknowledgement()
    render_werks_table()
=======
    breadcrumb = _release_notes_breadcrumb()

    load_werks()
    werk_table_options = _werk_table_options_from_request()

    html.header(_("Release notes"), breadcrumb,
                _release_notes_page_menu(breadcrumb, werk_table_options))

    handle_acknowledgement()
    render_werks_table(werk_table_options)

>>>>>>> upstream/master
    html.footer()


def handle_acknowledgement():
<<<<<<< HEAD
    if html.request.var("_werk_ack") and html.check_transaction():
        werk_id = html.get_integer_input("_werk_ack")
=======
    if not html.check_transaction():
        return

    if html.request.var("_werk_ack"):
        werk_id = html.request.get_integer_input_mandatory("_werk_ack")
>>>>>>> upstream/master
        if werk_id not in g_werks:
            raise MKUserError("werk", _("This werk does not exist."))
        werk = g_werks[werk_id]

        if werk["compatible"] == "incomp_unack":
            acknowledge_werk(werk)
<<<<<<< HEAD
            html.message(
=======
            html.show_message(
>>>>>>> upstream/master
                _("Werk %s - %s has been acknowledged.") %
                (render_werk_id(werk, with_link=True), render_werk_title(werk)))
            html.reload_sidebar()
            load_werks()  # reload ack states after modification

    elif html.request.var("_ack_all"):
<<<<<<< HEAD
        if html.confirm(_("Do you really want to acknowledge <b>all</b> incompatible werks?"),
                        method="GET"):
            num = len(unacknowledged_incompatible_werks())
            acknowledge_all_werks()
            html.message(_("%d incompatible Werks have been acknowledged.") % num)
            html.reload_sidebar()
            load_werks()  # reload ack states after modification
=======
        num = len(unacknowledged_incompatible_werks())
        acknowledge_all_werks()
        html.show_message(_("%d incompatible Werks have been acknowledged.") % num)
        html.reload_sidebar()
        load_werks()  # reload ack states after modification
>>>>>>> upstream/master

    render_unacknowleged_werks()


<<<<<<< HEAD
@cmk.gui.pages.register("werk")
def page_werk():
    load_werks()
    werk_id = html.get_integer_input("werk")
=======
def _release_notes_breadcrumb() -> Breadcrumb:
    breadcrumb = make_main_menu_breadcrumb(mega_menu_registry.menu_setup())

    breadcrumb.append(BreadcrumbItem(
        title=_("Maintenance"),
        url=None,
    ))

    breadcrumb.append(BreadcrumbItem(
        title=_("Release notes"),
        url="version.py",
    ))

    return breadcrumb


def _release_notes_page_menu(breadcrumb: Breadcrumb, werk_table_options: Dict[str,
                                                                              Any]) -> PageMenu:
    menu = PageMenu(
        dropdowns=[
            PageMenuDropdown(
                name="werks",
                title=_("Werks"),
                topics=[
                    PageMenuTopic(
                        title=_("Incompatible werks"),
                        entries=list(_page_menu_entries_ack_all_werks()),
                    ),
                ],
            ),
        ],
        breadcrumb=breadcrumb,
    )
    _extend_display_dropdown(menu, werk_table_options)
    return menu


def _page_menu_entries_ack_all_werks() -> Iterator[PageMenuEntry]:
    if not may_acknowledge():
        return

    yield PageMenuEntry(
        title=_("Acknowledge all"),
        icon_name="werk_ack",
        is_shortcut=True,
        is_suggested=True,
        item=make_simple_link(
            make_confirm_link(
                url=html.makeactionuri([("_ack_all", "1")]),
                message=_("Do you really want to acknowledge <b>all</b> incompatible werks?"),
            )),
        is_enabled=bool(unacknowledged_incompatible_werks()),
    )


def _extend_display_dropdown(menu, werk_table_options: Dict[str, Any]) -> None:
    display_dropdown = menu.get_dropdown_by_name("display", make_display_options_dropdown())
    display_dropdown.topics.insert(
        0,
        PageMenuTopic(
            title=_("Filter"),
            entries=[
                PageMenuEntry(
                    title=_("Filter view"),
                    icon_name="filters",
                    item=PageMenuSidePopup(_render_werk_options_form(werk_table_options)),
                    name="filters",
                    is_shortcut=True,
                ),
            ],
        ))


def _render_werk_options_form(werk_table_options: Dict[str, Any]) -> str:
    with html.plugged():
        html.begin_form("werks")
        html.hidden_field("wo_set", "set")

        _show_werk_options_controls()

        html.open_div(class_="side_popup_content")
        for name, height, vs, _default_value in _werk_table_option_entries():
            html.render_floating_option(name, height, "wo_", vs, werk_table_options[name])
        html.close_div()

        html.hidden_fields()
        html.end_form()

        return html.drain()


def _show_werk_options_controls() -> None:
    html.open_div(class_="side_popup_controls")

    html.open_div(class_="update_buttons")
    html.button("apply", _("Apply"), "submit")
    html.buttonlink(makeuri(request, [], remove_prefix=""), _("Reset"))
    html.close_div()

    html.close_div()


@cmk.gui.pages.register("werk")
def page_werk():
    load_werks()
    werk_id = html.request.get_integer_input_mandatory("werk")
>>>>>>> upstream/master
    if werk_id not in g_werks:
        raise MKUserError("werk", _("This werk does not exist."))
    werk = g_werks[werk_id]

<<<<<<< HEAD
    html.header(("%s %s - %s") % (_("Werk"), render_werk_id(werk, with_link=False), werk["title"]))
    html.begin_context_buttons()
    back_url = html.makeuri([], filename="version.py", delvars=["werk"])  # keeps filter settings
    html.context_button(_("Back"), back_url, "back")
    if werk["compatible"] == "incomp_unack" and may_acknowledge():
        ack_url = html.makeactionuri([("_werk_ack", werk["id"])], filename="version.py")
        html.context_button(_("Acknowledge"), ack_url, "werk_ack")
    html.end_context_buttons()
=======
    title = ("%s %s - %s") % (_("Werk"), render_werk_id(werk, with_link=False), werk["title"])

    breadcrumb = _release_notes_breadcrumb()
    breadcrumb.append(make_current_page_breadcrumb_item(title))
    html.header(title, breadcrumb, _page_menu_werk(breadcrumb, werk))
>>>>>>> upstream/master

    html.open_table(class_=["data", "headerleft", "werks"])

    def werk_table_row(caption, content, css=None):
        html.open_tr()
        html.th(caption)
        html.open_td(class_=css)
        html.write(content)
        html.close_td()
        html.close_tr()

    translator = cmk.utils.werks.WerkTranslator()
    werk_table_row(_("ID"), render_werk_id(werk, with_link=False))
    werk_table_row(_("Title"), html.render_b(render_werk_title(werk)))
    werk_table_row(_("Component"), translator.component_of(werk))
    werk_table_row(_("Date"), render_werk_date(werk))
<<<<<<< HEAD
    werk_table_row(_("Check_MK Version"), werk["version"])
=======
    werk_table_row(_("Checkmk Version"), werk["version"])
>>>>>>> upstream/master
    werk_table_row(_("Level"),
                   translator.level_of(werk),
                   css="werklevel werklevel%d" % werk["level"])
    werk_table_row(_("Class"),
                   translator.class_of(werk),
                   css="werkclass werkclass%s" % werk["class"])
    werk_table_row(_("Compatibility"),
                   translator.compatibility_of(werk),
                   css="werkcomp werkcomp%s" % werk["compatible"])
    werk_table_row(_("Description"), render_werk_description(werk), css="nowiki")

    html.close_table()

    html.footer()


<<<<<<< HEAD
def load_werks():
    global g_werks
    if g_werks is None:
=======
def _page_menu_werk(breadcrumb: Breadcrumb, werk: Dict[str, Any]):
    return PageMenu(
        dropdowns=[
            PageMenuDropdown(
                name="Werk",
                title="Werk",
                topics=[
                    PageMenuTopic(
                        title=_("Incompatible werk"),
                        entries=list(_page_menu_entries_ack_werk(werk)),
                    ),
                ],
            ),
        ],
        breadcrumb=breadcrumb,
    )


def _page_menu_entries_ack_werk(werk: Dict[str, Any]) -> Iterator[PageMenuEntry]:
    if not may_acknowledge():
        return

    ack_url = html.makeactionuri([("_werk_ack", werk["id"])], filename="version.py")
    yield PageMenuEntry(
        title=_("Acknowledge"),
        icon_name="werk_ack",
        item=make_simple_link(ack_url),
        is_enabled=werk["compatible"] == "incomp_unack",
    )


def load_werks():
    global g_werks
    if not g_werks:
>>>>>>> upstream/master
        g_werks = cmk.utils.werks.load()

    ack_ids = load_acknowledgements()
    for werk in g_werks.values():
        if werk["compatible"] in ["incomp", "incomp_unack"]:
            if werk["id"] in ack_ids or werk_is_pre_127(werk):
                werk["compatible"] = "incomp_ack"
            else:
                werk["compatible"] = "incomp_unack"


def may_acknowledge():
    return config.user.may("general.acknowledge_werks")


def acknowledge_werk(werk):
    acknowledge_werks([werk])


def acknowledge_werks(werks, check_permission=True):
    if check_permission:
        config.user.need_permission("general.acknowledge_werks")

    ack_ids = load_acknowledgements()
    for werk in werks:
        ack_ids.append(werk["id"])
        werk["compatible"] = "incomp_ack"
    save_acknowledgements(ack_ids)


def save_acknowledgements(acknowledged_werks):
<<<<<<< HEAD
    store.save_data_to_file(acknowledgement_path, acknowledged_werks)
=======
    store.save_object_to_file(acknowledgement_path, acknowledged_werks)
>>>>>>> upstream/master


def acknowledge_all_werks(check_permission=True):
    load_werks()
    acknowledge_werks(unacknowledged_incompatible_werks(), check_permission)


def werk_is_pre_127(werk):
    return werk["version"].startswith("1.2.5") \
        or werk["version"].startswith("1.2.6")


def load_acknowledgements():
<<<<<<< HEAD
    return store.load_data_from_file(acknowledgement_path, [])
=======
    return store.load_object_from_file(acknowledgement_path, default=[])
>>>>>>> upstream/master


def unacknowledged_incompatible_werks():
    return cmk.utils.werks.sort_by_date(werk  #
                                        for werk in g_werks.values()
                                        if werk["compatible"] == "incomp_unack")


def num_unacknowledged_incompatible_werks():
    load_werks()
    return len(unacknowledged_incompatible_werks())


def _werk_table_option_entries():
    translator = cmk.utils.werks.WerkTranslator()
    return [
        ("classes", "double", ListChoice(
            title=_("Classes"),
            choices=sorted(translator.classes()),
        ), ["feature", "fix", "security"]),
        ("levels", "double", ListChoice(
            title=_("Levels"),
            choices=sorted(translator.levels()),
        ), [1, 2, 3]),
        ("date", "double", Timerange(title=_("Date")), ('date', (1383149313, int(time.time())))),
<<<<<<< HEAD
        ("id", "single",
         TextAscii(
             title=_("Werk ID"),
             label="#",
             regex="[0-9]{4}",
             allow_empty=True,
             size=4,
         ), ""),
=======
        ("id", "single", TextAscii(
            title=_("Werk ID"),
            label="#",
            regex="^[0-9]{1,5}$",
            size=7,
        ), ""),
>>>>>>> upstream/master
        ("compatibility", "single",
         DropdownChoice(title=_("Compatibility"),
                        choices=[
                            (["compat", "incomp_ack",
                              "incomp_unack"], _("Compatible and incompatible Werks")),
                            (["compat"], _("Compatible Werks")),
                            (["incomp_ack", "incomp_unack"], _("Incompatible Werks")),
                            (["incomp_unack"], _("Unacknowledged incompatible Werks")),
                            (["incomp_ack"], _("Acknowledged incompatible Werks")),
                        ]), ["compat", "incomp_ack", "incomp_unack"]),
        ("component", "single",
         DropdownChoice(
             title=_("Component"),
             choices=[
                 (None, _("All components")),
             ] + sorted(translator.components()),
         ), None),
        ("edition", "single",
         DropdownChoice(
             title=_("Edition"),
             choices=[
                 (None, _("All editions")),
                 ("cme", _("Werks only concerning the Managed Services Edition")),
                 ("cee", _("Werks only concerning the Enterprise Edition")),
                 ("cre", _("Werks also concerning the Raw Edition")),
             ],
         ), None),
        ("werk_content", "single", TextUnicode(
            title=_("Werk title or content"),
            size=41,
        ), ""),
        ("version", "single",
<<<<<<< HEAD
         Tuple(title=_("Check_MK Version"),
=======
         Tuple(title=_("Checkmk Version"),
>>>>>>> upstream/master
               orientation="float",
               elements=[
                   TextAscii(label=_("from:"), size=12),
                   TextAscii(label=_("to:"), size=12),
               ]), ("", "")),
        ("grouping", "single",
         DropdownChoice(
             title=_("Group Werks by"),
             choices=[
<<<<<<< HEAD
                 ("version", _("Check_MK Version")),
=======
                 ("version", _("Checkmk Version")),
>>>>>>> upstream/master
                 ("day", _("Day of creation")),
                 ("week", _("Week of creation")),
                 (None, _("Do not group")),
             ],
         ), "version"),
        ("group_limit", "single",
         Integer(
             title=_("Show number of groups"),
             unit=_("groups"),
             minvalue=1,
         ), 20),
    ]


def render_unacknowleged_werks():
    werks = unacknowledged_incompatible_werks()
<<<<<<< HEAD
    if werks and may_acknowledge():
        html.begin_context_buttons()
        html.context_button(_("Acknowledge all"), html.makeactionuri([("_ack_all", "1")]),
                            "werk_ack")
        html.end_context_buttons()

=======
>>>>>>> upstream/master
    if werks and not html.request.has_var("show_unack"):
        html.open_div(class_=["warning"])
        html.write_text(
            _("<b>Warning:</b> There are %d unacknowledged incompatible werks:") % len(werks))
        html.br()
        html.br()
        html.a(_("Show unacknowledged incompatible werks"),
<<<<<<< HEAD
               href=html.makeuri_contextless([("show_unack", "1"), ("wo_compatibility", "3")]))
=======
               href=makeuri_contextless(request, [("show_unack", "1"), ("wo_compatibility", "3")]))
>>>>>>> upstream/master
        html.close_div()


# NOTE: The sorter and the grouping function should better agree, otherwise chaos will ensue...
_SORT_AND_GROUP = {
    "version": (
        cmk.utils.werks.sort_by_version_and_component,
        lambda werk: werk["version"]  #
    ),
    "day": (
        cmk.utils.werks.sort_by_date,
        lambda werk: time.strftime("%Y-%m-%d", time.localtime(werk["date"]))  #
    ),
    "week": (
        cmk.utils.werks.sort_by_date,
<<<<<<< HEAD
        lambda werk: time.strftime("%s %%U - %%Y" % _("Week"), time.localtime(werk["date"]))  #
=======
        lambda werk: time.strftime("%s %%U - %%Y" % ensure_str(_("Week")),
                                   time.localtime(werk["date"]))  #
>>>>>>> upstream/master
    ),
    None: (
        cmk.utils.werks.sort_by_date,
        lambda _werk: None  #
    ),
}


<<<<<<< HEAD
def render_werks_table():
    if html.request.var("show_unack") and not html.request.has_var("wo_set"):
        werk_table_options = _default_werk_table_options()
    else:
        werk_table_options = _render_werk_table_options()
=======
def render_werks_table(werk_table_options: Dict[str, Any]):
>>>>>>> upstream/master
    translator = cmk.utils.werks.WerkTranslator()
    number_of_werks = 0
    sorter, grouper = _SORT_AND_GROUP[werk_table_options["grouping"]]
    werklist = sorter(werk  #
                      for werk in g_werks.values()
                      if werk_matches_options(werk, werk_table_options))
    groups = itertools.groupby(werklist, key=grouper)
    for group_title, werks in itertools.islice(groups, werk_table_options["group_limit"]):
        with table_element(title=group_title,
                           limit=None,
                           searchable=False,
                           sortable=False,
                           css="werks") as table:
            for werk in werks:
                number_of_werks += 1
                render_werks_table_row(table, translator, werk)
    if not number_of_werks:
        html.h3(_("No matching Werks found."))


def render_werks_table_row(table, translator, werk):
    table.row()
    table.cell(_("ID"), render_werk_id(werk, with_link=True), css="number narrow")
    table.cell(_("Version"), werk["version"], css="number narrow")
    table.cell(_("Date"), render_werk_date(werk), css="number narrow")
    table.cell(_("Class"), translator.class_of(werk), css="werkclass werkclass%s" % werk["class"])
    table.cell(_("Level"), translator.level_of(werk), css="werklevel werklevel%d" % werk["level"])
    table.cell(_("Compatibility"),
               translator.compatibility_of(werk),
               css="werkcomp werkcomp%s" % werk["compatible"])
    table.cell(_("Component"), translator.component_of(werk), css="nowrap")
    table.cell(_("Title"), render_werk_title(werk))


def werk_matches_options(werk, werk_table_options):
<<<<<<< HEAD
    if not ((not werk_table_options["id"] or werk["id"] == int(werk_table_options["id"])) and \
           werk["level"] in werk_table_options["levels"] and \
           werk["class"] in werk_table_options["classes"] and \
           werk["compatible"] in werk_table_options["compatibility"] and \
           werk_table_options["component"] in ( None, werk["component" ]) and \
           werk["date"] >= werk_table_options["date_range"][0] and \
           werk["date"] <= werk_table_options["date_range"][1]):
=======
    # TODO: Fix this silly typing chaos below!
    # check if werk id is int because valuespec is TextAscii
    # else, set empty id to return all results beside input warning
    try:
        werk_to_match: Union[int, str] = int(werk_table_options["id"])
    except ValueError:
        werk_to_match = ""

    if not ((not werk_to_match or werk["id"] == werk_to_match) and werk["level"]
            in werk_table_options["levels"] and werk["class"] in werk_table_options["classes"] and
            werk["compatible"] in werk_table_options["compatibility"] and
            werk_table_options["component"] in (None, werk["component"]) and
            werk["date"] >= werk_table_options["date_range"][0] and
            werk["date"] <= werk_table_options["date_range"][1]):
>>>>>>> upstream/master
        return False

    if werk_table_options["edition"] and werk["edition"] != werk_table_options["edition"]:
        return False

    from_version, to_version = werk_table_options["version"]
    if from_version and utils.cmp_version(werk["version"], from_version) < 0:
        return False

    if to_version and utils.cmp_version(werk["version"], to_version) > 0:
        return False

    if werk_table_options["werk_content"]:
        have_match = False
        search_text = werk_table_options["werk_content"].lower()
        for line in [werk["title"]] + werk["body"]:
            if search_text in line.lower():
                have_match = True
                break
        if not have_match:
            return False

    return True


def _default_werk_table_options():
    werk_table_options = {
<<<<<<< HEAD
        name: default_value for name, _height, _vs, default_value in _werk_table_option_entries()
=======
        name: default_value  #
        for name, _height, _vs, default_value in _werk_table_option_entries()
>>>>>>> upstream/master
    }
    werk_table_options["date_range"] = (1, time.time())
    werk_table_options["compatibility"] = ["incomp_unack"]
    return werk_table_options


<<<<<<< HEAD
def _render_werk_table_options():
    werk_table_options = {}

    for name, height, vs, default_value in _werk_table_option_entries():
=======
def _werk_table_options_from_request() -> Dict[str, Any]:
    if html.request.var("show_unack") and not html.request.has_var("wo_set"):
        return _default_werk_table_options()

    werk_table_options: Dict[str, Any] = {}
    for name, _height, vs, default_value in _werk_table_option_entries():
>>>>>>> upstream/master
        value = default_value
        try:
            if html.request.has_var("wo_set"):
                value = vs.from_html_vars("wo_" + name)
                vs.validate_value(value, "wo_" + name)
        except MKUserError as e:
            html.user_error(e)

        werk_table_options.setdefault(name, value)

<<<<<<< HEAD
    html.begin_foldable_container("werks",
                                  "options",
                                  isopen=True,
                                  title=_("Searching and Filtering"),
                                  indent=False)
    html.begin_form("werks")
    html.hidden_field("wo_set", "set")
    html.begin_floating_options("werks", is_open=True)
    for name, height, vs, default_value in _werk_table_option_entries():
        html.render_floating_option(name, height, "wo_", vs, werk_table_options[name])
    html.end_floating_options(reset_url=html.makeuri([], remove_prefix=""))
    html.hidden_fields()
    html.end_form()
    html.end_foldable_container()

=======
>>>>>>> upstream/master
    from_date, until_date = Timerange().compute_range(werk_table_options["date"])[0]
    werk_table_options["date_range"] = from_date, until_date

    return werk_table_options


def render_werk_id(werk, with_link):
    if with_link:
<<<<<<< HEAD
        url = html.makeuri([("werk", werk["id"])], filename="werk.py")
=======
        url = makeuri(request, [("werk", werk["id"])], filename="werk.py")
>>>>>>> upstream/master
        return html.render_a(render_werk_id(werk, with_link=False), url)
    return "#%04d" % werk["id"]


def render_werk_date(werk):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(werk["date"]))


def render_werk_title(werk):
    title = werk["title"]
    # if the title begins with the name or names of check plugins, then
    # we link to the man pages of those checks
    if ":" in title:
        parts = title.split(":", 1)
        title = insert_manpage_links(parts[0]) + ":" + parts[1]
    return title


def render_werk_description(werk):
    html_code = "<p>"
    in_list = False
    in_code = False
    for line in werk["body"]:
        if line.startswith("LI:"):
            if not in_list:
                html_code += "<ul>"
                in_list = True
            html_code += "<li>%s</li>\n" % line[3:]
        else:
            if in_list:
                html_code += "</ul>"
                in_list = False

            if line.startswith("H2:"):
                html_code += "<h3>%s</h3>\n" % line[3:]
            elif line.startswith("C+:"):
                html_code += "<pre class=code>"
                in_code = True
            elif line.startswith("F+:"):
                file_name = line[3:]
                if file_name:
                    html_code += "<div class=filename>%s</div>" % file_name
                html_code += "<pre class=file>"
                in_code = True
            elif line.startswith("C-:") or line.startswith("F-:"):
                html_code += "</pre>"
                in_code = False
            elif line.startswith("OM:"):
                html_code += "OMD[mysite]:~$ <b>" + line[3:] + "</b>\n"
            elif line.startswith("RP:"):
                html_code += "root@myhost:~# <b>" + line[3:] + "</b>\n"
            elif not line.strip() and not in_code:
                html_code += "</p><p>"
            else:
                html_code += line + "\n"

    if in_list:
        html_code += "</ul>"

    html_code = html_code.replace("<script>",
                                  "&lt;script&gt;").replace("</script>", "&lt;/script&gt;")

    html_code += "</p>"
    return html_code


def insert_manpage_links(text):
    parts = text.replace(",", " ").split()
    new_parts = []
    check_regex = re.compile(r"[-_\.a-z0-9]")
    for part in parts:
        if check_regex.match(part) and os.path.exists(cmk.utils.paths.check_manpages_dir + "/" +
                                                      part):
            part = '<a href="wato.py?mode=check_manpage&check_type=%s">%s</a>' % (part, part)
        new_parts.append(part)
    return " ".join(new_parts)
