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

import base64
import six

from cmk.gui.htmllib import HTML
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import base64
from typing import Union, Callable, Dict, Optional, Tuple, List, Any, TYPE_CHECKING
from six import ensure_binary, ensure_str

import cmk.gui.escaping as escaping
from cmk.gui.utils.html import HTML
>>>>>>> upstream/master
from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.exceptions import MKUserError

<<<<<<< HEAD
=======
if TYPE_CHECKING:
    from typing import Sequence
    from cmk.gui.valuespec import Dictionary, ValueSpec, Transform

>>>>>>> upstream/master
g_header_open = False
g_section_open = False


<<<<<<< HEAD
# An input function with the same call syntax as htmllib.textinput()
def textinput(valuespec, varprefix, defvalue):
    if html.form_submitted(html.form_name):
        value = valuespec.from_html_vars(varprefix)
    else:
        value = defvalue
    valuespec.render_input(varprefix, value)


def get_input(valuespec, varprefix):
=======
def get_input(valuespec: 'ValueSpec', varprefix: str) -> Any:
>>>>>>> upstream/master
    value = valuespec.from_html_vars(varprefix)
    valuespec.validate_value(value, varprefix)
    return value


<<<<<<< HEAD
# TODO: Remove all call sites and clean this up! The mechanic of this
# and the edit_dictionaries() is very uncommon compared to the other
# usages of valuespecs.
def edit_dictionary(entries, value, **args):
    result = edit_dictionaries([("value", entries)], {"value": value}, **args)
    if result:
        return result["value"]
    return result


=======
>>>>>>> upstream/master
# Edit a list of several dictionaries. Those can either be dictionary
# valuespec or just a list of elements. Each entry in dictionaries is
# a pair of key and either a list of elements or a Dictionary.
# TODO: As soon as the reports have been migrated to pagetypes.py
# we can drop edit_dictionaries()? At least the function for editing
# several dictionaries at once.
# TODO: Remove all call sites and clean this up! The mechanic of this
<<<<<<< HEAD
# and the edit_dictionary() is very uncommon compared to the other
# usages of valuespecs.
def edit_dictionaries(dictionaries,
                      value,
                      focus=None,
                      hover_help=True,
                      validate=None,
                      buttontext=None,
                      title=None,
                      buttons=None,
                      method="GET",
                      preview=False,
                      varprefix="",
                      formname="form",
                      consume_transid=True):

    # Convert list of entries/dictionaries
    sections = []
    for keyname, d in dictionaries:
        if isinstance(d, list):
            sections.append((keyname, title or _("Properties"), d))
        else:
            sections.append((keyname, None, d))  # valuespec Dictionary, title used from dict

    if html.request.var("filled_in") == formname and html.transaction_valid():
        if not preview and consume_transid:
            html.check_transaction()

        messages = []
        new_value = {}
        for keyname, _section_title, entries in sections:
            if isinstance(entries, list):
                new_value[keyname] = value.get(keyname, {}).copy()
                for name, vs in entries:
                    if len(sections) == 1:
                        vp = varprefix
                    else:
                        vp = keyname + "_" + varprefix
                    try:
                        v = vs.from_html_vars(vp + name)
                        vs.validate_value(v, vp + name)
                        new_value[keyname][name] = v
                    except MKUserError as e:
                        messages.append("%s: %s" % (vs.title(), e))
                        html.add_user_error(e.varname, e)

            else:
                new_value[keyname] = {}
                try:
                    edited_value = entries.from_html_vars(keyname)
                    entries.validate_value(edited_value, keyname)
                    new_value[keyname].update(edited_value)
                except MKUserError as e:
                    messages.append("%s: %s" % (entries.title() or _("Properties"), e))
                    html.add_user_error(e.varname, e)
                except Exception as e:
                    messages.append("%s: %s" % (entries.title() or _("Properties"), e))
                    html.add_user_error(None, e)
=======
# is very uncommon compared to the other usages of valuespecs.
def edit_dictionaries(dictionaries: 'Sequence[Tuple[str, Union[Transform, Dictionary]]]',
                      value: Dict[str, Any],
                      focus: Optional[str] = None,
                      hover_help: bool = True,
                      validate: Optional[Callable[[Any], None]] = None,
                      title: Optional[str] = None,
                      method: str = "GET",
                      preview: bool = False,
                      varprefix: str = "",
                      formname: str = "form",
                      consume_transid: bool = True):

    if html.request.get_ascii_input("filled_in") == formname and html.transaction_valid():
        if not preview and consume_transid:
            html.check_transaction()

        messages: List[str] = []
        new_value: Dict[str, Dict[str, Any]] = {}
        for keyname, vs_dict in dictionaries:
            dict_varprefix = varprefix + keyname
            new_value[keyname] = {}
            try:
                edited_value = vs_dict.from_html_vars(dict_varprefix)
                vs_dict.validate_value(edited_value, dict_varprefix)
                new_value[keyname].update(edited_value)
            except MKUserError as e:
                messages.append("%s: %s" % (vs_dict.title() or _("Properties"), e))
                html.add_user_error(e.varname, e)
            except Exception as e:
                messages.append("%s: %s" % (vs_dict.title() or _("Properties"), e))
                html.add_user_error(None, e)
>>>>>>> upstream/master

            if validate and not html.has_user_errors():
                try:
                    validate(new_value[keyname])
                except MKUserError as e:
<<<<<<< HEAD
                    messages.append(e)
=======
                    messages.append("%s" % e)
>>>>>>> upstream/master
                    html.add_user_error(e.varname, e)

        if messages:
            messages_joined = "".join(["%s<br>\n" % m for m in messages])
            if not preview:
                html.show_error(messages_joined)
            else:
                raise MKUserError(None, messages_joined)
        else:
            return new_value

    html.begin_form(formname, method=method)
<<<<<<< HEAD
    for keyname, title1, entries in sections:
        subvalue = value.get(keyname, {})
        if isinstance(entries, list):
            header(title1)
            first = True
            for name, vs in entries:
                section(vs.title())
                html.help(vs.help())
                if name in subvalue:
                    v = subvalue[name]
                else:
                    v = vs.default_value()
                if len(sections) == 1:
                    vp = varprefix
                else:
                    vp = keyname + "_" + varprefix
                vs.render_input(vp + name, v)
                if (not focus and first) or (name == focus):
                    vs.set_focus(vp + name)
                    first = False
        else:
            entries.render_input_as_form(keyname, subvalue)

    end()
    if buttons:
        for name, button_title, _icon in buttons:
            html.button(name, button_title)
    else:
        if buttontext is None:
            buttontext = _("Save")
        html.button("save", buttontext)
=======
    for keyname, vs_dict in dictionaries:
        dict_varprefix = varprefix + keyname
        subvalue = value.get(keyname, {})
        vs_dict.render_input_as_form(dict_varprefix, subvalue)

    end()
>>>>>>> upstream/master
    # Should be ignored be hidden_fields, but I do not dare to change it there
    html.request.del_var("filled_in")
    html.hidden_fields()
    html.end_form()


<<<<<<< HEAD
# Similar but for editing an arbitrary valuespec
def edit_valuespec(vs,
                   value,
                   buttontext=None,
                   method="GET",
                   varprefix="",
                   validate=None,
                   formname="form",
                   consume_transid=True,
                   focus=None):

    if html.request.var("filled_in") == formname and html.transaction_valid():
        if consume_transid:
            html.check_transaction()

        messages = []
        try:
            new_value = vs.from_html_vars(varprefix)
            vs.validate_value(new_value, varprefix)

        except MKUserError as e:
            messages.append("%s: %s" % (vs.title(), e.message))
            html.add_user_error(e.varname, e.message)

        if validate and not html.has_user_errors():
            try:
                validate(new_value)
            except MKUserError as e:
                messages.append(e.message)
                html.add_user_error(e.varname, e.message)

        if messages:
            html.show_error("".join(["%s<br>\n" % m for m in messages]))
        else:
            return new_value

    html.begin_form(formname, method=method)
    html.help(vs.help())
    vs.render_input(varprefix, value)
    if buttontext is None:
        buttontext = _("Save")
    html.button("save", buttontext)
    # Should be ignored be hidden_fields, but I do not dare to change it there
    html.request.del_var("filled_in")
    html.hidden_fields()
    if focus:
        html.set_focus(focus)
    else:
        vs.set_focus(varprefix)
    html.end_form()


# New functions for painting forms


def header(title, isopen=True, table_id="", narrow=False, css=None):
=======
# New functions for painting forms


def header(title: str,
           isopen: bool = True,
           table_id: str = "",
           narrow: bool = False,
           css: Optional[str] = None,
           show_more_toggle: bool = False,
           show_more_mode: bool = False) -> None:
>>>>>>> upstream/master
    global g_header_open, g_section_open
    if g_header_open:
        end()

<<<<<<< HEAD
    html.open_table(id_=table_id if table_id else None,
                    class_=["nform", "narrow" if narrow else None, css if css else None])

    html.begin_foldable_container(
        treename=html.form_name if html.form_name else "nform",
        id_=base64.b64encode(title.encode("utf-8") if isinstance(title, six.text_type) else title),
        isopen=isopen,
        title=title,
        indent="nform")
=======
    id_ = ensure_str(base64.b64encode(ensure_binary(title)))
    treename = html.form_name or "nform"
    isopen = html.foldable_container_is_open(treename, id_, isopen)

    html.open_table(id_=table_id if table_id else None,
                    class_=[
                        "nform",
                        "narrow" if narrow else None,
                        css if css else None,
                        "open" if isopen else "closed",
                        "more" if show_more_mode else None,
                    ])

    _begin_foldable_nform_container(
        treename=treename,
        id_=id_,
        isopen=isopen,
        title=title,
        show_more_toggle=show_more_toggle,
    )
>>>>>>> upstream/master
    html.tr(html.render_td('', colspan=2))
    g_header_open = True
    g_section_open = False


<<<<<<< HEAD
# container without legend and content
def container():
    global g_section_open
    if g_section_open:
        html.close_td()
        html.close_tr()
    html.open_tr()
    html.open_td(colspan=2, class_=container)
    g_section_open = True


def space():
    html.tr(html.render_td('', colspan=2, style="height:15px;"))


def section(title=None,
            checkbox=None,
            section_id=None,
            simple=False,
            hide=False,
            legend=True,
            css=None):
    global g_section_open
    if g_section_open:
        html.close_td()
        html.close_tr()
    html.open_tr(id_=section_id, class_=[css], style="display:none;" if hide else None)
=======
def _begin_foldable_nform_container(
    treename: str,
    id_: str,
    isopen: bool,
    title: str,
    show_more_toggle: bool,
) -> bool:
    isopen = html.foldable_container_is_open(treename, id_, isopen)
    onclick = html.foldable_container_onclick(treename, id_, fetch_url=None)
    img_id = html.foldable_container_img_id(treename, id_)
    container_id = html.foldable_container_id(treename, id_)

    html.open_thead()
    html.open_tr(class_="heading")
    html.open_td(id_="nform.%s.%s" % (treename, id_), onclick=onclick, colspan=2)
    html.img(id_=img_id,
             class_=["treeangle", "nform", "open" if isopen else "closed"],
             src="themes/%s/images/tree_closed.png" % (html.get_theme()),
             align="absbottom")
    html.write_text(title)
    if show_more_toggle:
        html.more_button("foldable_" + id_, dom_levels_up=4)
    html.close_td()
    html.close_tr()
    html.close_thead()
    html.open_tbody(id_=container_id, class_=["open" if isopen else "closed"])

    return isopen


# container without legend and content
def container() -> None:
    global g_section_open
    section_close()
    html.open_tr()
    html.open_td(colspan=2)
    g_section_open = True


def space() -> None:
    html.tr(html.render_td('', colspan=2, style="height:15px;"))


def section(title: Union[None, HTML, str] = None,
            checkbox: Union[None, HTML, str, Tuple[str, bool, str]] = None,
            section_id: Optional[str] = None,
            simple: bool = False,
            hide: bool = False,
            legend: bool = True,
            css: Optional[str] = None,
            is_show_more: bool = False) -> None:
    global g_section_open
    section_close()
    html.open_tr(
        id_=section_id,
        class_=[css, "show_more_mode" if is_show_more else "basic"],
        style="display:none;" if hide else None,
    )
>>>>>>> upstream/master

    if legend:
        html.open_td(class_=["legend", "simple" if simple else None])
        if title:
            html.open_div(class_=["title", "withcheckbox" if checkbox else None],
<<<<<<< HEAD
                          title=html.strip_tags(title))
            html.write(html.permissive_attrencode(title))
            html.span('.' * 100, class_="dots")
            html.close_div()
        if checkbox:
            html.open_div(class_="checkbox")
            if isinstance(checkbox, six.string_types + (HTML,)):
=======
                          title=escaping.strip_tags(title))
            html.write(escaping.escape_text(title))
            html.span('.' * 200, class_="dots")
            html.close_div()
        if checkbox:
            html.open_div(class_="checkbox")
            if isinstance(checkbox, (str, HTML)):
>>>>>>> upstream/master
                html.write(checkbox)
            else:
                name, active, attrname = checkbox
                html.checkbox(name,
                              active,
                              onclick='cmk.wato.toggle_attribute(this, \'%s\')' % attrname)
            html.close_div()
        html.close_td()
    html.open_td(class_=["content", "simple" if simple else None])
    g_section_open = True


<<<<<<< HEAD
def end():
    global g_header_open
    g_header_open = False
    if g_section_open:
        html.close_td()
        html.close_tr()
    html.end_foldable_container()
=======
def section_close() -> None:
    if g_section_open:
        html.close_td()
        html.close_tr()


def end() -> None:
    global g_header_open
    g_header_open = False
    section_close()
>>>>>>> upstream/master
    html.tr(html.render_td('', colspan=2), class_=["bottom"])
    html.close_tbody()
    html.close_table()
