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
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

# TODO:
#
# Notes for future rewrite:
#
# - Find all call sites which do something like "int(html.request.var(...))"
<<<<<<< HEAD
#   and replace it with html.get_integer_input(...)
=======
#   and replace it with html.request.get_integer_input_mandatory(...)
>>>>>>> upstream/master
#
# - Make clear which functions return values and which write out values
#   render_*, add_*, write_* (e.g. icon() -> outputs directly,
#                                  render_icon() -> returns icon
#
# - Order of arguments:
#   e.g. icon(help, icon) -> change and make help otional?
#
# - Fix names of message() show_error() show_warning()
#
<<<<<<< HEAD
# - change naming of html.attrencode() to html.render()
=======
# - change naming of escaping.escape_attribute() to html.render()
>>>>>>> upstream/master
#
# - General rules:
# 1. values of type str that are passed as arguments or
#    return values or are stored in datastructures must not contain
#    non-Ascii characters! UTF-8 encoding must just be used in
#    the last few CPU cycles before outputting. Conversion from
#    input to str or unicode must happen as early as possible,
#    directly when reading from file or URL.
#
# - indentify internal helper methods and prefix them with "_"
#
# - Split HTML handling (page generating) code and generic request
#   handling (vars, cookies, ...) up into separate classes to make
#   the different tasks clearer. For ABCHTMLGenerator() or similar.
<<<<<<< HEAD

import time
import os
import urllib
import ast
import random
import re
import signal
import json
import abc
import pprint
from contextlib import contextmanager
# suppress missing import error from mypy
from html import escape as html_escape  # type: ignore
from pathlib2 import Path

import six
=======
#
# - Unify CSS classes attribute to "class_"
import functools
import os
import ast
import re
import json
import json.encoder  # type: ignore[import]
import abc
import pprint
from contextlib import contextmanager
from typing import (
    Union,
    Optional,
    List,
    Dict,
    Tuple,
    Any,
    Iterator,
    cast,
    Mapping,
    Set,
    Sequence,
    TYPE_CHECKING,
    TypeVar,
)
from pathlib import Path
import urllib.parse

from six import ensure_str

Value = TypeVar('Value')
>>>>>>> upstream/master


# TODO: Cleanup this dirty hack. Import of htmllib must not magically modify the behaviour of
# the json module. Better would be to create a JSON wrapper in cmk.utils.json which uses a
# custom subclass of the JSONEncoder.
#
# Monkey patch in order to make the HTML class below json-serializable without changing the default json calls.
<<<<<<< HEAD
def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)
=======
def _default(self: json.JSONEncoder, obj: object) -> str:
    # ignore attr-defined: See hack below
    return getattr(obj.__class__, "to_json", _default.default)(obj)  # type: ignore[attr-defined]
>>>>>>> upstream/master


# TODO: suppress mypy warnings for this monkey patch right now. See also:
# https://github.com/python/mypy/issues/2087
# Save unmodified default:
<<<<<<< HEAD
_default.default = json.JSONEncoder().default  # type: ignore
# replacement:
json.JSONEncoder.default = _default  # type: ignore

import cmk.utils.paths
from cmk.utils.exceptions import MKGeneralException
from cmk.gui.exceptions import MKUserError, RequestTimeout

import cmk.gui.utils as utils
import cmk.gui.config as config
import cmk.gui.log as log
from cmk.gui.i18n import _

#.
#   .--Escaper-------------------------------------------------------------.
#   |                 _____                                                |
#   |                | ____|___  ___ __ _ _ __   ___ _ __                  |
#   |                |  _| / __|/ __/ _` | '_ \ / _ \ '__|                 |
#   |                | |___\__ \ (_| (_| | |_) |  __/ |                    |
#   |                |_____|___/\___\__,_| .__/ \___|_|                    |
#   |                                    |_|                               |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------


class Escaper(object):
    def __init__(self):
        super(Escaper, self).__init__()
        self._unescaper_text = re.compile(
            r'&lt;(/?)(h1|h2|b|tt|i|u|br(?: /)?|nobr(?: /)?|pre|a|sup|p|li|ul|ol)&gt;')
        self._quote = re.compile(r"(?:&quot;|&#x27;)")
        self._a_href = re.compile(r'&lt;a href=((?:&quot;|&#x27;).*?(?:&quot;|&#x27;))&gt;')

    # Encode HTML attributes. Replace HTML syntax with HTML text.
    # For example: replace '"' with '&quot;', '<' with '&lt;'.
    # This code is slow. Works on str and unicode without changing
    # the type. Also works on things that can be converted with '%s'.
    def escape_attribute(self, value):
        attr_type = type(value)
        if value is None:
            return ''
        elif attr_type == int:
            return str(value)
        elif isinstance(value, HTML):
            return "%s" % value  # This is HTML code which must not be escaped
        elif not isinstance(attr_type, six.string_types):  # also possible: type Exception!
            value = "%s" % value  # Note: this allows Unicode. value might not have type str now
        return html_escape(value, quote=True)

    def unescape_attributes(self, value):
        # In python3 use html.unescape
        return value.replace("&amp;", "&")\
                    .replace("&quot;", "\"")\
                    .replace("&lt;", "<")\
                    .replace("&gt;", ">")

    # render HTML text.
    # We only strip od some tags and allow some simple tags
    # such as <h1>, <b> or <i> to be part of the string.
    # This is useful for messages where we want to keep formatting
    # options. (Formerly known as 'permissive_attrencode') """
    # for the escaping functions
    def escape_text(self, text):
        if isinstance(text, HTML):
            return "%s" % text  # This is HTML code which must not be escaped

        text = self.escape_attribute(text)
        text = self._unescaper_text.sub(r'<\1\2>', text)
        for a_href in self._a_href.finditer(text):
            text = text.replace(a_href.group(0),
                                "<a href=%s>" % self._quote.sub("\"", a_href.group(1)))
        return text.replace("&amp;nbsp;", "&nbsp;")


#.
#   .--Encoding------------------------------------------------------------.
#   |              _____                     _ _                           |
#   |             | ____|_ __   ___ ___   __| (_)_ __   __ _               |
#   |             |  _| | '_ \ / __/ _ \ / _` | | '_ \ / _` |              |
#   |             | |___| | | | (_| (_) | (_| | | | | | (_| |              |
#   |             |_____|_| |_|\___\___/ \__,_|_|_| |_|\__, |              |
#   |                                                  |___/               |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


class Encoder(object):
    def urlencode_vars(self, vars_):
        """Convert a mapping object or a sequence of two-element tuples to a “percent-encoded” string

        This function returns a str object, never unicode!
        Note: This should be changed once we change everything to
        unicode internally.
        """
        assert isinstance(vars_, list)
        pairs = []
        for varname, value in sorted(vars_):
            assert isinstance(varname, str)

            if isinstance(value, int):
                value = str(value)
            elif isinstance(value, six.text_type):
                value = value.encode("utf-8")
            elif value is None:
                # TODO: This is not ideal and should better be cleaned up somehow. Shouldn't
                # variables with None values simply be skipped? We currently can not find the
                # call sites easily. This may be cleaned up once we establish typing. Until then
                # we need to be compatible with the previous behavior.
                value = ""

            #assert type(value) == str, "%s: %s" % (varname, value)

            pairs.append((varname, value))

        return urllib.urlencode(pairs)

    def urlencode(self, value):
        """Replace special characters in string using the %xx escape.

        This function returns a str object, never unicode!
        Note: This should be changed once we change everything to
        unicode internally.
        """
        if isinstance(value, six.text_type):
            value = value.encode("utf-8")
        elif value is None:
            return ""

        assert isinstance(value, str)

        return urllib.quote_plus(value)


#.
#   .--HTML----------------------------------------------------------------.
#   |                      _   _ _____ __  __ _                            |
#   |                     | | | |_   _|  \/  | |                           |
#   |                     | |_| | | | | |\/| | |                           |
#   |                     |  _  | | | | |  | | |___                        |
#   |                     |_| |_| |_| |_|  |_|_____|                       |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | This is a simple class which wraps a unicode string provided by      |
#   | the caller to make html.attrencode() know that this string should    |
#   | not be escaped.                                                      |
#   |                                                                      |
#   | This way we can implement encodings while still allowing HTML code.  |
#   | This is useful when one needs to print out HTML tables in messages   |
#   | or help texts.                                                       |
#   |                                                                      |
#   | The HTML class is implemented as an immutable type.                  |
#   | Every instance of the class is a unicode string.                     |
#   | Only utf-8 compatible encodings are supported.                       |
#   '----------------------------------------------------------------------'


class HTML(object):
    def __init__(self, value=u''):
        super(HTML, self).__init__()
        self.value = self._ensure_unicode(value)

    def _ensure_unicode(self, thing, encoding_index=0):
        try:
            return six.text_type(thing)
        except UnicodeDecodeError:
            return thing.decode("utf-8")

    def __bytebatzen__(self):
        return self.value.encode("utf-8")

    def __str__(self):
        # Against the sense of the __str__() method, we need to return the value
        # as unicode here. Why? There are many cases where something like
        # "%s" % HTML(...) is done in the GUI code. This calls the __str__ function
        # because the origin is a str() object. The call will then return a UTF-8
        # encoded str() object. This brings a lot of compatbility issues to the code
        # which can not be solved easily.
        # To deal with this situation we need the implicit conversion from str to
        # unicode that happens when we return a unicode value here. In all relevant
        # cases this does exactly what we need. It would only fail if the origin
        # string contained characters that can not be decoded with the ascii codec
        # which is not relevant for us here.
        #
        # This is problematic:
        #   html.write("%s" % HTML("ä"))
        #
        # Bottom line: We should relly cleanup internal unicode/str handling.
        return self.value

    def __repr__(self):
        return ("HTML(\"%s\")" % self.value).encode("utf-8")

    def to_json(self):
        return self.value

    def __add__(self, other):
        return HTML(self.value + self._ensure_unicode(other))

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return HTML(self._ensure_unicode(other) + self.value)

    def join(self, iterable):
        return HTML(self.value.join(map(self._ensure_unicode, iterable)))

    def __eq__(self, other):
        return self.value == self._ensure_unicode(other)

    def __ne__(self, other):
        return self.value != self._ensure_unicode(other)

    def __len__(self):
        return len(self.value)

    def __getitem__(self, index):
        return HTML(self.value[index])

    def __contains__(self, item):
        return self._ensure_unicode(item) in self.value

    def count(self, sub, *args):
        return self.value.count(self._ensure_unicode(sub), *args)

    def index(self, sub, *args):
        return self.value.index(self._ensure_unicode(sub), *args)

    def lstrip(self, *args):
        args = tuple(map(self._ensure_unicode, args[:1])) + args[1:]
        return HTML(self.value.lstrip(*args))

    def rstrip(self, *args):
        args = tuple(map(self._ensure_unicode, args[:1])) + args[1:]
        return HTML(self.value.rstrip(*args))

    def strip(self, *args):
        args = tuple(map(self._ensure_unicode, args[:1])) + args[1:]
        return HTML(self.value.strip(*args))

    def lower(self):
        return HTML(self.value.lower())

    def upper(self):
        return HTML(self.value.upper())

    def startswith(self, prefix, *args):
        return self.value.startswith(self._ensure_unicode(prefix), *args)


#.
#   .--OutputFunnel--------------------------------------------------------.
#   |     ___        _               _   _____                       _     |
#   |    / _ \ _   _| |_ _ __  _   _| |_|  ___|   _ _ __  _ __   ___| |    |
#   |   | | | | | | | __| '_ \| | | | __| |_ | | | | '_ \| '_ \ / _ \ |    |
#   |   | |_| | |_| | |_| |_) | |_| | |_|  _|| |_| | | | | | | |  __/ |    |
#   |    \___/ \__,_|\__| .__/ \__,_|\__|_|   \__,_|_| |_|_| |_|\___|_|    |
#   |                   |_|                                                |
#   +----------------------------------------------------------------------+
#   | Provides the write functionality. The method _lowlevel_write needs   |
#   | to be overwritten in the specific subclass!                          |
#   |                                                                      |
#   |  Usage of plugged context:                                           |
#   |          with html.plugged():                                        |
#   |             html.write("something")                                  |
#   |             html_code = html.drain()                                 |
#   |          print html_code                                             |
#   '----------------------------------------------------------------------'


class OutputFunnel(six.with_metaclass(abc.ABCMeta, object)):
    def __init__(self):
        super(OutputFunnel, self).__init__()
        self.plug_text = []

    # Accepts str and unicode objects only!
    # The plugged functionality can be used for debugging.
    def write(self, text):
        if not text:
            return

        if isinstance(text, HTML):
            text = "%s" % text

        if not isinstance(text, six.string_types):  # also possible: type Exception!
            raise MKGeneralException(
                _('Type Error: html.write accepts str and unicode input objects only!'))

        if self._is_plugged():
            self.plug_text[-1].append(text)
        else:
            # encode when really writing out the data. Not when writing plugged,
            # because the plugged code will be handled somehow by our code. We
            # only encode when leaving the pythonic world.
            if isinstance(text, six.text_type):
                text = text.encode("utf-8")
            self._lowlevel_write(text)

    @abc.abstractmethod
    def _lowlevel_write(self, text):
        raise NotImplementedError()

    @contextmanager
    def plugged(self):
        self.plug_text.append([])
        try:
            yield
        finally:
            text = self.drain()
            self.plug_text.pop()
            self.write(text)

    def _is_plugged(self):
        return bool(self.plug_text)

    # Get the sink content in order to do something with it.
    def drain(self):
        if not self._is_plugged():  # TODO: Raise exception or even remove "if"?
            return ''

        text = "".join(self.plug_text.pop())
        self.plug_text.append([])
        return text

=======
_default.default = json.JSONEncoder().default  # type: ignore[attr-defined]
# replacement:
json.JSONEncoder.default = _default  # type: ignore[assignment]

# And here we go for another dirty JSON hack. We often use he JSON we produce for adding it to HTML
# tags and the JSON produced by json.dumps() can not directly be added to <script> tags in a save way.
# TODO: This is something which should be realized by using a custom JSONEncoder. The slash encoding
# is not necessary when the resulting string is not added to HTML content, but there is no problem
# to apply it to all encoded strings.


def _patch_json(json_module):
    # We make this a function which is called on import-time because mypy fell into an endless-loop
    # due to changes outside this scope.
    orig_func = json_module.encoder.encode_basestring_ascii

    @functools.wraps(orig_func)
    def _escaping_wrapper(s):
        return orig_func(s).replace('/', '\\/')

    json_module.encoder.encode_basestring_ascii = _escaping_wrapper


_patch_json(json)

import cmk.utils.version as cmk_version
import cmk.utils.paths
from cmk.utils.exceptions import MKGeneralException

from cmk.gui.exceptions import MKUserError
import cmk.gui.escaping as escaping
import cmk.gui.utils as utils
import cmk.gui.config as config
import cmk.gui.log as log
from cmk.gui.utils.html import HTML
from cmk.gui.utils.output_funnel import OutputFunnel
from cmk.gui.utils.popups import PopupMethod
from cmk.gui.utils.transaction_manager import TransactionManager
from cmk.gui.utils.timeout_manager import TimeoutManager
from cmk.gui.utils.url_encoder import URLEncoder
from cmk.gui.utils.urls import (
    makeactionuri,
    makeactionuri_contextless,
    requested_file_name,
)
from cmk.gui.i18n import _
from cmk.gui.http import Response
from cmk.gui.breadcrumb import Breadcrumb, BreadcrumbRenderer
from cmk.gui.page_state import PageState, PageStateRenderer
from cmk.gui.page_menu import (
    PageMenu,
    PageMenuRenderer,
    PageMenuPopupsRenderer,
    enable_page_menu_entry,
)
from cmk.gui.type_defs import (
    CSSSpec,
    Icon,
    Choices,
    ChoiceGroup,
    GroupedChoices,
)
from cmk.gui.watolib.activate_changes import get_pending_changes_info

if TYPE_CHECKING:
    from cmk.gui.http import Request
    from cmk.gui.type_defs import VisualContext, HTTPVariables
    from cmk.gui.valuespec import ValueSpec
    from cmk.gui.utils.output_funnel import OutputFunnelInput

HTMLTagName = str
HTMLTagValue = Optional[str]
HTMLContent = Union[None, int, HTML, str]
HTMLTagAttributeValue = Union[None, CSSSpec, HTMLTagValue, List[str]]
HTMLTagAttributes = Dict[str, HTMLTagAttributeValue]
HTMLMessageInput = Union[HTML, str]
DefaultChoice = str
>>>>>>> upstream/master

#.
#   .--HTML Generator------------------------------------------------------.
#   |                      _   _ _____ __  __ _                            |
#   |                     | | | |_   _|  \/  | |                           |
#   |                     | |_| | | | | |\/| | |                           |
#   |                     |  _  | | | | |  | | |___                        |
#   |                     |_| |_| |_| |_|  |_|_____|                       |
#   |                                                                      |
#   |             ____                           _                         |
#   |            / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __             |
#   |           | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|            |
#   |           | |_| |  __/ | | |  __/ | | (_| | || (_) | |               |
#   |            \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|               |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Generator which provides top level HTML writing functionality.      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
class ABCHTMLGenerator(six.with_metaclass(abc.ABCMeta, OutputFunnel)):
=======
class ABCHTMLGenerator(metaclass=abc.ABCMeta):
>>>>>>> upstream/master
    """ Usage Notes:

          - Tags can be opened using the open_[tag]() call where [tag] is one of the possible tag names.
            All attributes can be passed as function arguments, such as open_div(class_="example").
            However, python specific key words need to be escaped using a trailing underscore.
            One can also provide a dictionary as attributes: open_div(**{"class": "example"}).

          - All tags can be closed again using the close_[tag]() syntax.

          - For tags which shall only contain plain text (i.e. no tags other than highlighting tags)
            you can a the direct call using the tag name only as function name,
            self.div("Text content", **attrs). Tags featuring this functionality are listed in
            the "featured shortcuts" list.

          - Some tags require mandatory arguments. Those are defined explicitly below.
            For example an a tag needs the href attribute everytime.

          - If you want to provide plain HTML to a tag, please use the tag_content function or
            facillitate the HTML class.

        HOWTO HTML Attributes:

          - Python specific attributes have to be escaped using a trailing underscore

          - All attributes can be python objects. However, some attributes can also be lists of attrs:

                'class' attributes will be concatenated using one whitespace
                'style' attributes will be concatenated using the semicolon and one whitespace
                Behaviorial attributes such as 'onclick', 'onmouseover' will bec concatenated using
                a semicolon and one whitespace.

          - All attributes will be escaped, i.e. the characters '&', '<', '>', '"' will be replaced by
            non HtML relevant signs '&amp;', '&lt;', '&gt;' and '&quot;'. """

<<<<<<< HEAD
    # NOTE: This class is obviously still abstract, but pylint fails to see
    # this, even in the presence of the meta class assignment below, see
    # https://github.com/PyCQA/pylint/issues/179.

    # pylint: disable=abstract-method

    # TODO: Replace u, i, b with underline, italic, bold, usw.

    # these tags can be called by their tag names, e.g. 'self.title(content)'
    _shortcut_tags = {"title", "h1", "h2", "h3", "h4", "th", "tr", "td", "center", "pre", "style", "iframe",\
                          "div", "p", "span", "canvas", "strong", "sub", "tt", "u", "i", "b", "x", "option"}

    # these tags can be called by open_name(), close_name() and render_name(), e.g. 'self.open_html()'
    _tag_names = {
        'html', 'head', 'body', 'header', 'footer', 'a', 'b', 'sup', 'script', 'form', 'button',
        'p', 'select', 'fieldset', 'table', 'tbody', 'thead', 'row', 'ul', 'li', 'br', 'nobr',
        'input', 'span', 'tags', 'tag'
    }

    # Of course all shortcut tags can be used as well.
    _tag_names.update(_shortcut_tags)

    def __init__(self):
        super(ABCHTMLGenerator, self).__init__()
        self.escaper = Escaper()

=======
>>>>>>> upstream/master
    #
    # Rendering
    #

<<<<<<< HEAD
    def _render_attributes(self, **attrs):
        # make class attribute foolproof
        css = []
        for k in ["class_", "css", "cssclass", "class"]:
            if k in attrs:
                if isinstance(attrs[k], list):
                    css.extend(attrs.pop(k))
                elif attrs[k] is not None:
                    css.append(attrs.pop(k))
=======
    def _render_attributes(self, **attrs: HTMLTagAttributeValue) -> Iterator[str]:
        css = self._get_normalized_css_classes(attrs)
>>>>>>> upstream/master
        if css:
            attrs["class"] = css

        # options such as 'selected' and 'checked' dont have a value in html tags
        options = []

<<<<<<< HEAD
        # render all attributes
        for k, v in attrs.iteritems():

            if v is None:
                continue

            k = self.escaper.escape_attribute(k.rstrip('_'))

            if v == '':
                options.append(k)
                continue

            if not isinstance(v, list):
                v = self.escaper.escape_attribute(v)
            else:
                if k == "class":
                    sep = ' '
                elif k == "style" or k.startswith('on'):
=======
        # Links require href to be first attribute
        href = attrs.pop('href', None)
        if href:
            attributes = list(attrs.items())
            attributes.insert(0, ("href", href))
        else:
            attributes = list(attrs.items())

        # render all attributes
        for key_unescaped, v in attributes:
            if v is None:
                continue

            key = escaping.escape_attribute(key_unescaped.rstrip('_'))

            if v == '':
                options.append(key)
                continue

            if not isinstance(v, list):
                v = escaping.escape_attribute(v)
            else:
                if key == "class":
                    sep = ' '
                elif key == "style" or key.startswith('on'):
>>>>>>> upstream/master
                    sep = '; '
                else:
                    sep = '_'

<<<<<<< HEAD
                v = sep.join([a for a in (self.escaper.escape_attribute(vi) for vi in v) if a])

                if sep.startswith(';'):
                    v = re.sub(';+', ';', v)

            yield ' %s=\"%s\"' % (k, v)
=======
                joined_value = sep.join(
                    [a for a in (escaping.escape_attribute(vi) for vi in v) if a])

                if sep.startswith(';'):
                    joined_value = re.sub(';+', ';', joined_value)

                v = joined_value

            yield ' %s=\"%s\"' % (key, v)
>>>>>>> upstream/master

        for k in options:
            yield " %s=\'\'" % k

<<<<<<< HEAD
    # applies attribute encoding to prevent code injections.
    def _render_opening_tag(self, tag_name, close_tag=False, **attrs):
=======
    def _get_normalized_css_classes(self, attrs: HTMLTagAttributes) -> List[str]:
        # make class attribute foolproof
        css: List[str] = []
        for k in ["class_", "css", "cssclass", "class"]:
            if k in attrs:
                cls_spec = cast(CSSSpec, attrs.pop(k))
                css += self.normalize_css_spec(cls_spec)
        return css

    def normalize_css_spec(self, css_classes: CSSSpec) -> List[str]:
        if isinstance(css_classes, list):
            return [c for c in css_classes if c is not None]

        if css_classes is not None:
            return [css_classes]

        return []

    # applies attribute encoding to prevent code injections.
    def _render_start_tag(self,
                          tag_name: HTMLTagName,
                          close_tag: bool = False,
                          **attrs: HTMLTagAttributeValue) -> HTML:
>>>>>>> upstream/master
        """ You have to replace attributes which are also python elements such as
            'class', 'id', 'for' or 'type' using a trailing underscore (e.g. 'class_' or 'id_'). """
        return HTML("<%s%s%s>" %
                    (tag_name, '' if not attrs else ''.join(self._render_attributes(**attrs)),
                     '' if not close_tag else ' /'))

<<<<<<< HEAD
    def _render_closing_tag(self, tag_name):
        return HTML("</%s>" % (tag_name))

    def _render_content_tag(self, tag_name, tag_content, **attrs):
        open_tag = self._render_opening_tag(tag_name, **attrs)
=======
    def _render_end_tag(self, tag_name: HTMLTagName) -> HTML:
        return HTML("</%s>" % (tag_name))

    def _render_element(self, tag_name: HTMLTagName, tag_content: HTMLContent,
                        **attrs: HTMLTagAttributeValue) -> HTML:
        open_tag = self._render_start_tag(tag_name, close_tag=False, **attrs)
>>>>>>> upstream/master

        if not tag_content:
            tag_content = ""
        elif not isinstance(tag_content, HTML):
<<<<<<< HEAD
            tag_content = self.escaper.escape_text(tag_content)

        return HTML("%s%s</%s>" % (open_tag, tag_content, tag_name))

    # This is used to create all the render_tag() and close_tag() functions
    def __getattr__(self, name):
        """ All closing tags can be called like this:
            self.close_html(), self.close_tr(), etc. """

        parts = name.split('_')

        # generating the shortcut tag calls
        if len(parts) == 1 and name in self._shortcut_tags:
            return lambda content, **attrs: self.write_html(
                self._render_content_tag(name, content, **attrs))

        # generating the open, close and render calls
        elif len(parts) == 2:
            what, tag_name = parts[0], parts[1]

            if what == "open" and tag_name in self._tag_names:
                return lambda **attrs: self.write_html(self._render_opening_tag(tag_name, **attrs))

            elif what == "close" and tag_name in self._tag_names:
                return lambda: self.write_html(self._render_closing_tag(tag_name))

            elif what == "render" and tag_name in self._tag_names:
                return lambda content, **attrs: HTML(
                    self._render_content_tag(tag_name, content, **attrs))

        else:
            # FIXME: This returns None, which is not a very informative error message
            return object.__getattribute__(self, name)
=======
            tag_content = escaping.escape_text(tag_content)

        return HTML("%s%s</%s>" % (open_tag, tag_content, tag_name))

    #
    # Showing / rendering
    #

    def render_text(self, text: HTMLContent) -> HTML:
        return HTML(escaping.escape_text(text))

    def write_text(self, text: HTMLContent) -> None:
        """ Write text. Highlighting tags such as h2|b|tt|i|br|pre|a|sup|p|li|ul|ol are not escaped. """
        self.write(self.render_text(text))

    def write_html(self, content: HTML) -> None:
        """ Write HTML code directly, without escaping. """
        self.write(content)

    @abc.abstractmethod
    def write(self, text: 'OutputFunnelInput') -> None:
        raise NotImplementedError()
>>>>>>> upstream/master

    #
    # HTML element methods
    # If an argument is mandatory, it is used as default and it will overwrite an
    # implicit argument (e.g. id_ will overwrite attrs["id"]).
    #

    #
    # basic elements
    #

<<<<<<< HEAD
    def render_text(self, text):
        return HTML(self.escaper.escape_text(text))

    def write_text(self, text):
        """ Write text. Highlighting tags such as h2|b|tt|i|br|pre|a|sup|p|li|ul|ol are not escaped. """
        self.write(self.render_text(text))

    def write_html(self, content):
        """ Write HTML code directly, without escaping. """
        self.write(content)

    def comment(self, comment_text):
        self.write("<!--%s-->" % self.encode_attribute(comment_text))

    def meta(self, httpequiv=None, **attrs):
        if httpequiv:
            attrs['http-equiv'] = httpequiv
        self.write_html(self._render_opening_tag('meta', close_tag=True, **attrs))

    def base(self, target):
        self.write_html(self._render_opening_tag('base', close_tag=True, target=target))

    def open_a(self, href, **attrs):
        attrs['href'] = href
        self.write_html(self._render_opening_tag('a', **attrs))

    def render_a(self, content, href, **attrs):
        attrs['href'] = href
        return self._render_content_tag('a', content, **attrs)

    def a(self, content, href, **attrs):
        self.write_html(self.render_a(content, href, **attrs))

    def stylesheet(self, href):
        self.write_html(
            self._render_opening_tag('link',
                                     rel="stylesheet",
                                     type_="text/css",
                                     href=href,
                                     close_tag=True))

    #
    # Scriptingi
    #

    def render_javascript(self, code):
        return HTML("<script type=\"text/javascript\">\n%s\n</script>\n" % code)

    def javascript(self, code):
        self.write_html(self.render_javascript(code))

    def javascript_file(self, src):
        """ <script type="text/javascript" src="%(name)"/>\n """
        self.write_html(self._render_content_tag('script', '', type_="text/javascript", src=src))

    def render_img(self, src, **attrs):
        attrs['src'] = src
        return self._render_opening_tag('img', close_tag=True, **attrs)

    def img(self, src, **attrs):
        self.write_html(self.render_img(src, **attrs))

    def open_button(self, type_, **attrs):
        attrs['type'] = type_
        self.write_html(self._render_opening_tag('button', close_tag=True, **attrs))

    def play_sound(self, url):
        self.write_html(self._render_opening_tag('audio autoplay', src_=url))
=======
    def meta(self, httpequiv: Optional[str] = None, **attrs: HTMLTagAttributeValue) -> None:
        if httpequiv:
            attrs['http-equiv'] = httpequiv
        self.write_html(self._render_start_tag('meta', close_tag=True, **attrs))

    def base(self, target: str) -> None:
        self.write_html(self._render_start_tag('base', close_tag=True, target=target))

    def open_a(self, href: Optional[str], **attrs: HTMLTagAttributeValue) -> None:
        if href is not None:
            attrs['href'] = href
        self.write_html(self._render_start_tag('a', close_tag=False, **attrs))

    def render_a(self, content: HTMLContent, href: Union[None, str, str],
                 **attrs: HTMLTagAttributeValue) -> HTML:
        if href is not None:
            attrs['href'] = href
        return self._render_element('a', content, **attrs)

    def a(self, content: HTMLContent, href: str, **attrs: HTMLTagAttributeValue) -> None:
        self.write_html(self.render_a(content, href, **attrs))

    def stylesheet(self, href: str) -> None:
        self.write_html(
            self._render_start_tag('link',
                                   rel="stylesheet",
                                   type_="text/css",
                                   href=href,
                                   close_tag=True))

    #
    # Scripting
    #

    def render_javascript(self, code: str) -> HTML:
        return HTML("<script type=\"text/javascript\">\n%s\n</script>\n" % code)

    def javascript(self, code: str) -> None:
        self.write_html(self.render_javascript(code))

    def javascript_file(self, src: str) -> None:
        """ <script type="text/javascript" src="%(name)"/>\n """
        self.write_html(self._render_element('script', '', type_="text/javascript", src=src))

    def render_img(self, src: str, **attrs: HTMLTagAttributeValue) -> HTML:
        attrs['src'] = src
        return self._render_start_tag('img', close_tag=True, **attrs)

    def img(self, src: str, **attrs: HTMLTagAttributeValue) -> None:
        self.write_html(self.render_img(src, **attrs))

    def open_button(self, type_: str, **attrs: HTMLTagAttributeValue) -> None:
        attrs['type'] = type_
        self.write_html(self._render_start_tag('button', close_tag=True, **attrs))

    def play_sound(self, url: str) -> None:
        self.write_html(self._render_start_tag('audio autoplay', src_=url))
>>>>>>> upstream/master

    #
    # form elements
    #

<<<<<<< HEAD
    def render_label(self, content, for_, **attrs):
        attrs['for'] = for_
        return self._render_content_tag('label', content, **attrs)

    def label(self, content, for_, **attrs):
        self.write_html(self.render_label(content, for_, **attrs))

    def render_input(self, name, type_, **attrs):
        attrs['type_'] = type_
        attrs['name'] = name
        return self._render_opening_tag('input', close_tag=True, **attrs)

    def input(self, name, type_, **attrs):
=======
    def render_label(self, content: HTMLContent, for_: str, **attrs: HTMLTagAttributeValue) -> HTML:
        attrs['for'] = for_
        return self._render_element('label', content, **attrs)

    def label(self, content: HTMLContent, for_: str, **attrs: HTMLTagAttributeValue) -> None:
        self.write_html(self.render_label(content, for_, **attrs))

    def render_input(self, name: Optional[str], type_: str, **attrs: HTMLTagAttributeValue) -> HTML:
        attrs['type_'] = type_
        attrs['name'] = name
        return self._render_start_tag('input', close_tag=True, **attrs)

    def input(self, name: Optional[str], type_: str, **attrs: HTMLTagAttributeValue) -> None:
>>>>>>> upstream/master
        self.write_html(self.render_input(name, type_, **attrs))

    #
    # table and list elements
    #

<<<<<<< HEAD
    def td(self, content, **attrs):
        """ Only for text content. You can't put HTML structure here. """
        self.write_html(self._render_content_tag('td', content, **attrs))

    def li(self, content, **attrs):
        """ Only for text content. You can't put HTML structure here. """
        self.write_html(self._render_content_tag('li', content, **attrs))
=======
    def li(self, content: HTMLContent, **attrs: HTMLTagAttributeValue) -> None:
        """ Only for text content. You can't put HTML structure here. """
        self.write_html(self._render_element('li', content, **attrs))
>>>>>>> upstream/master

    #
    # structural text elements
    #

<<<<<<< HEAD
    def render_heading(self, content):
        """ <h2>%(content)</h2> """
        return self._render_content_tag('h2', content)

    def heading(self, content):
        self.write_html(self.render_heading(content))

    def render_br(self):
        return HTML("<br/>")

    def br(self):
        self.write_html(self.render_br())

    def render_hr(self, **attrs):
        return self._render_opening_tag('hr', close_tag=True, **attrs)

    def hr(self, **attrs):
        self.write_html(self.render_hr(**attrs))

    def rule(self):
        return self.hr()

    def render_nbsp(self):
        return HTML("&nbsp;")

    def nbsp(self):
        self.write_html(self.render_nbsp())


#.
#   .--TimeoutMgr.---------------------------------------------------------.
#   |      _____ _                            _   __  __                   |
#   |     |_   _(_)_ __ ___   ___  ___  _   _| |_|  \/  | __ _ _ __        |
#   |       | | | | '_ ` _ \ / _ \/ _ \| | | | __| |\/| |/ _` | '__|       |
#   |       | | | | | | | | |  __/ (_) | |_| | |_| |  | | (_| | | _        |
#   |       |_| |_|_| |_| |_|\___|\___/ \__,_|\__|_|  |_|\__, |_|(_)       |
#   |                                                    |___/             |
#   '----------------------------------------------------------------------'


class TimeoutManager(object):
    """Request timeout handling

    The system apache process will end the communication with the client after
    the timeout configured for the proxy connection from system apache to site
    apache. This is done in /omd/sites/[site]/etc/apache/proxy-port.conf file
    in the "timeout=x" parameter of the ProxyPass statement.

    The regular request timeout configured here should always be lower to make
    it possible to abort the page processing and send a helpful answer to the
    client.

    It is possible to disable the applications request timeout (temoporarily)
    or totally for specific calls, but the timeout to the client will always
    be applied by the system webserver. So the client will always get a error
    page while the site apache continues processing the request (until the
    first try to write anything to the client) which will result in an
    exception.
    """
    def enable_timeout(self, duration):
        def handle_request_timeout(signum, frame):
            raise RequestTimeout(
                _("Your request timed out after %d seconds. This issue may be "
                  "related to a local configuration problem or a request which works "
                  "with a too large number of objects. But if you think this "
                  "issue is a bug, please send a crash report.") % duration)

        signal.signal(signal.SIGALRM, handle_request_timeout)
        signal.alarm(duration)

    def disable_timeout(self):
        signal.alarm(0)


#.
#   .--Transactions--------------------------------------------------------.
#   |      _____                               _   _                       |
#   |     |_   _| __ __ _ _ __  ___  __ _  ___| |_(_) ___  _ __  ___       |
#   |       | || '__/ _` | '_ \/ __|/ _` |/ __| __| |/ _ \| '_ \/ __|      |
#   |       | || | | (_| | | | \__ \ (_| | (__| |_| | (_) | | | \__ \      |
#   |       |_||_|  \__,_|_| |_|___/\__,_|\___|\__|_|\___/|_| |_|___/      |
#   |                                                                      |
#   '----------------------------------------------------------------------'


class TransactionManager(object):
    """Manages the handling of transaction IDs used by the GUI to prevent against
    performing the same action multiple times."""
    def __init__(self, request):
        super(TransactionManager, self).__init__()
        self._request = request

        self._new_transids = []
        self._ignore_transids = False
        self._current_transid = None

    def ignore(self):
        """Makes the GUI skip all transaction validation steps"""
        self._ignore_transids = True

    def get(self):
        """Returns a transaction ID that can be used during a subsequent action"""
        if not self._current_transid:
            self._current_transid = self.fresh_transid()
        return self._current_transid

    def fresh_transid(self):
        """Compute a (hopefully) unique transaction id.

        This is generated during rendering of a form or an action link, stored
        in a user specific file for later validation, sent to the users browser
        via HTML code, then submitted by the user together with the action
        (link / form) and then validated if it is a known transid. When it is a
        known transid, it will be used and invalidated. If the id is not known,
        the action will not be processed."""
        transid = "%d/%d" % (int(time.time()), random.getrandbits(32))
        self._new_transids.append(transid)
        return transid

    def store_new(self):
        """All generated transids are saved per user.

        They are stored in the transids.mk.  Per user only up to 20 transids of
        the already existing ones are kept. The transids generated on the
        current page are all kept. IDs older than one day are deleted."""
        if not self._new_transids:
            return

        valid_ids = self._load_transids(lock=True)
        cleared_ids = []
        now = time.time()
        for valid_id in valid_ids:
            timestamp = valid_id.split("/")[0]
            if now - int(timestamp) < 86400:  # one day
                cleared_ids.append(valid_id)
        self._save_transids((cleared_ids[-20:] + self._new_transids))

    def transaction_valid(self):
        """Checks if the current transaction is valid

        i.e. in case of browser reload a browser reload, the form submit should
        not be handled  a second time.. The HTML variable _transid must be
        present.

        In case of automation users (authed by _secret in URL): If it is empty
        or -1, then it's always valid (this is used for webservice calls).
        This was also possible for normal users, but has been removed to preven
        security related issues."""
        if not self._request.has_var("_transid"):
            return False

        transid = self._request.var("_transid")
        if self._ignore_transids and (not transid or transid == '-1'):
            return True  # automation

        if '/' not in transid:
            return False

        # Normal user/password auth user handling
        timestamp = transid.split("/", 1)[0]

        # If age is too old (one week), it is always
        # invalid:
        now = time.time()
        if now - int(timestamp) >= 604800:  # 7 * 24 hours
            return False

        # Now check, if this transid is a valid one
        return transid in self._load_transids()

    def is_transaction(self):
        """Checks, if the current page is a transation, i.e. something that is secured by
        a transid (such as a submitted form)"""
        return self._request.has_var("_transid")

    def check_transaction(self):
        """called by page functions in order to check, if this was a reload or the original form submission.

        Increases the transid of the user, if the latter was the case.

        There are three return codes:

        True:  -> positive confirmation by the user
        False: -> not yet confirmed, question is being shown
        None:  -> a browser reload or a negative confirmation
        """
        if self.transaction_valid():
            transid = self._request.var("_transid")
            if transid and transid != "-1":
                self._invalidate(transid)
            return True
        else:
            return False

    def _invalidate(self, used_id):
        """Remove the used transid from the list of valid ones"""
        valid_ids = self._load_transids(lock=True)
        try:
            valid_ids.remove(used_id)
        except ValueError:
            return
        self._save_transids(valid_ids)

    def _load_transids(self, lock=False):
        return config.user.load_file("transids", [], lock)

    def _save_transids(self, used_ids):
        if config.user.id:
            config.user.save_file("transids", used_ids)
=======
    def render_heading(self, content: HTMLContent) -> HTML:
        return self._render_element('h2', content)

    def heading(self, content: HTMLContent) -> None:
        self.write_html(self.render_heading(content))

    def render_br(self) -> HTML:
        return HTML("<br/>")

    def br(self) -> None:
        self.write_html(self.render_br())

    def render_hr(self, **attrs: HTMLTagAttributeValue) -> HTML:
        return self._render_start_tag('hr', close_tag=True, **attrs)

    def hr(self, **attrs: HTMLTagAttributeValue) -> None:
        self.write_html(self.render_hr(**attrs))

    def rule(self) -> None:
        self.hr()

    def render_nbsp(self) -> HTML:
        return HTML("&nbsp;")

    def nbsp(self) -> None:
        self.write_html(self.render_nbsp())

    #
    # Simple HTML object rendering without specific functionality
    #

    def pre(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("pre", content, **kwargs))

    def h2(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("h2", content, **kwargs))

    def h3(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("h3", content, **kwargs))

    def h1(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("h1", content, **kwargs))

    def h4(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("h4", content, **kwargs))

    def style(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("style", content, **kwargs))

    def span(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("span", content, **kwargs))

    def sub(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("sub", content, **kwargs))

    def title(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("title", content, **kwargs))

    def tt(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("tt", content, **kwargs))

    def tr(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("tr", content, **kwargs))

    def th(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("th", content, **kwargs))

    def td(self,
           content: HTMLContent,
           colspan: Optional[int] = None,
           **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(
            self._render_element("td",
                                 content,
                                 colspan=str(colspan) if colspan is not None else None,
                                 **kwargs))

    def option(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("option", content, **kwargs))

    def canvas(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("canvas", content, **kwargs))

    def strong(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("strong", content, **kwargs))

    def b(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("b", content, **kwargs))

    def center(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("center", content, **kwargs))

    def i(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("i", content, **kwargs))

    def p(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("p", content, **kwargs))

    def u(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("u", content, **kwargs))

    def iframe(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("iframe", content, **kwargs))

    def x(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("x", content, **kwargs))

    def div(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_element("div", content, **kwargs))

    def open_pre(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("pre", close_tag=False, **kwargs))

    def close_pre(self) -> None:
        self.write_html(self._render_end_tag("pre"))

    def render_pre(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("pre", content, **kwargs)

    def open_h2(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("h2", close_tag=False, **kwargs))

    def close_h2(self) -> None:
        self.write_html(self._render_end_tag("h2"))

    def render_h2(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("h2", content, **kwargs)

    def open_h3(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("h3", close_tag=False, **kwargs))

    def close_h3(self) -> None:
        self.write_html(self._render_end_tag("h3"))

    def render_h3(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("h3", content, **kwargs)

    def open_h1(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("h1", close_tag=False, **kwargs))

    def close_h1(self) -> None:
        self.write_html(self._render_end_tag("h1"))

    def render_h1(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("h1", content, **kwargs)

    def open_h4(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("h4", close_tag=False, **kwargs))

    def close_h4(self) -> None:
        self.write_html(self._render_end_tag("h4"))

    def render_h4(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("h4", content, **kwargs)

    def open_header(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("header", close_tag=False, **kwargs))

    def close_header(self) -> None:
        self.write_html(self._render_end_tag("header"))

    def render_header(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("header", content, **kwargs)

    def open_tag(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("tag", close_tag=False, **kwargs))

    def close_tag(self) -> None:
        self.write_html(self._render_end_tag("tag"))

    def render_tag(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("tag", content, **kwargs)

    def open_table(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("table", close_tag=False, **kwargs))

    def close_table(self) -> None:
        self.write_html(self._render_end_tag("table"))

    def render_table(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("table", content, **kwargs)

    def open_select(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("select", close_tag=False, **kwargs))

    def close_select(self) -> None:
        self.write_html(self._render_end_tag("select"))

    def render_select(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("select", content, **kwargs)

    def open_row(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("row", close_tag=False, **kwargs))

    def close_row(self) -> None:
        self.write_html(self._render_end_tag("row"))

    def render_row(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("row", content, **kwargs)

    def open_style(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("style", close_tag=False, **kwargs))

    def close_style(self) -> None:
        self.write_html(self._render_end_tag("style"))

    def render_style(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("style", content, **kwargs)

    def open_span(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("span", close_tag=False, **kwargs))

    def close_span(self) -> None:
        self.write_html(self._render_end_tag("span"))

    def render_span(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("span", content, **kwargs)

    def open_sub(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("sub", close_tag=False, **kwargs))

    def close_sub(self) -> None:
        self.write_html(self._render_end_tag("sub"))

    def render_sub(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("sub", content, **kwargs)

    def open_script(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("script", close_tag=False, **kwargs))

    def close_script(self) -> None:
        self.write_html(self._render_end_tag("script"))

    def render_script(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("script", content, **kwargs)

    def open_tt(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("tt", close_tag=False, **kwargs))

    def close_tt(self) -> None:
        self.write_html(self._render_end_tag("tt"))

    def render_tt(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("tt", content, **kwargs)

    def open_tr(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("tr", close_tag=False, **kwargs))

    def close_tr(self) -> None:
        self.write_html(self._render_end_tag("tr"))

    def render_tr(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("tr", content, **kwargs)

    def open_tbody(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("tbody", close_tag=False, **kwargs))

    def close_tbody(self) -> None:
        self.write_html(self._render_end_tag("tbody"))

    def render_tbody(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("tbody", content, **kwargs)

    def open_li(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("li", close_tag=False, **kwargs))

    def close_li(self) -> None:
        self.write_html(self._render_end_tag("li"))

    def render_li(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("li", content, **kwargs)

    def open_html(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("html", close_tag=False, **kwargs))

    def close_html(self) -> None:
        self.write_html(self._render_end_tag("html"))

    def render_html(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("html", content, **kwargs)

    def open_th(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("th", close_tag=False, **kwargs))

    def close_th(self) -> None:
        self.write_html(self._render_end_tag("th"))

    def render_th(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("th", content, **kwargs)

    def open_sup(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("sup", close_tag=False, **kwargs))

    def close_sup(self) -> None:
        self.write_html(self._render_end_tag("sup"))

    def render_sup(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("sup", content, **kwargs)

    def open_input(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("input", close_tag=False, **kwargs))

    def close_input(self) -> None:
        self.write_html(self._render_end_tag("input"))

    def open_td(self, colspan: Optional[int] = None, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(
            self._render_start_tag("td",
                                   close_tag=False,
                                   colspan=str(colspan) if colspan is not None else None,
                                   **kwargs))

    def close_td(self) -> None:
        self.write_html(self._render_end_tag("td"))

    def render_td(self,
                  content: HTMLContent,
                  colspan: Optional[int] = None,
                  **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("td",
                                    content,
                                    colspan=str(colspan) if colspan is not None else None,
                                    **kwargs)

    def open_thead(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("thead", close_tag=False, **kwargs))

    def close_thead(self) -> None:
        self.write_html(self._render_end_tag("thead"))

    def render_thead(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("thead", content, **kwargs)

    def open_body(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("body", close_tag=False, **kwargs))

    def close_body(self) -> None:
        self.write_html(self._render_end_tag("body"))

    def render_body(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("body", content, **kwargs)

    def open_head(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("head", close_tag=False, **kwargs))

    def close_head(self) -> None:
        self.write_html(self._render_end_tag("head"))

    def render_head(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("head", content, **kwargs)

    def open_fieldset(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("fieldset", close_tag=False, **kwargs))

    def close_fieldset(self) -> None:
        self.write_html(self._render_end_tag("fieldset"))

    def render_fieldset(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("fieldset", content, **kwargs)

    def open_optgroup(self, **kwargs):
        # type: (**HTMLTagAttributeValue) -> None
        self.write_html(self._render_start_tag("optgroup", close_tag=False, **kwargs))

    def close_optgroup(self):
        # type: () -> None
        self.write_html(self._render_end_tag("optgroup"))

    def open_option(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("option", close_tag=False, **kwargs))

    def close_option(self) -> None:
        self.write_html(self._render_end_tag("option"))

    def render_option(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("option", content, **kwargs)

    def open_form(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("form", close_tag=False, **kwargs))

    def close_form(self) -> None:
        self.write_html(self._render_end_tag("form"))

    def render_form(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("form", content, **kwargs)

    def open_tags(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("tags", close_tag=False, **kwargs))

    def close_tags(self) -> None:
        self.write_html(self._render_end_tag("tags"))

    def render_tags(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("tags", content, **kwargs)

    def open_canvas(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("canvas", close_tag=False, **kwargs))

    def close_canvas(self) -> None:
        self.write_html(self._render_end_tag("canvas"))

    def render_canvas(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("canvas", content, **kwargs)

    def open_nobr(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("nobr", close_tag=False, **kwargs))

    def close_nobr(self) -> None:
        self.write_html(self._render_end_tag("nobr"))

    def render_nobr(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("nobr", content, **kwargs)

    def open_br(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("br", close_tag=False, **kwargs))

    def close_br(self) -> None:
        self.write_html(self._render_end_tag("br"))

    def open_strong(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("strong", close_tag=False, **kwargs))

    def close_strong(self) -> None:
        self.write_html(self._render_end_tag("strong"))

    def render_strong(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("strong", content, **kwargs)

    def close_a(self) -> None:
        self.write_html(self._render_end_tag("a"))

    def open_b(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("b", close_tag=False, **kwargs))

    def close_b(self) -> None:
        self.write_html(self._render_end_tag("b"))

    def render_b(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("b", content, **kwargs)

    def open_center(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("center", close_tag=False, **kwargs))

    def close_center(self) -> None:
        self.write_html(self._render_end_tag("center"))

    def render_center(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("center", content, **kwargs)

    def open_footer(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("footer", close_tag=False, **kwargs))

    def close_footer(self) -> None:
        self.write_html(self._render_end_tag("footer"))

    def render_footer(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("footer", content, **kwargs)

    def open_i(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("i", close_tag=False, **kwargs))

    def close_i(self) -> None:
        self.write_html(self._render_end_tag("i"))

    def render_i(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("i", content, **kwargs)

    def close_button(self) -> None:
        self.write_html(self._render_end_tag("button"))

    def open_title(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("title", close_tag=False, **kwargs))

    def close_title(self) -> None:
        self.write_html(self._render_end_tag("title"))

    def render_title(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("title", content, **kwargs)

    def open_p(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("p", close_tag=False, **kwargs))

    def close_p(self) -> None:
        self.write_html(self._render_end_tag("p"))

    def render_p(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("p", content, **kwargs)

    def open_u(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("u", close_tag=False, **kwargs))

    def close_u(self) -> None:
        self.write_html(self._render_end_tag("u"))

    def render_u(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("u", content, **kwargs)

    def open_iframe(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("iframe", close_tag=False, **kwargs))

    def close_iframe(self) -> None:
        self.write_html(self._render_end_tag("iframe"))

    def render_iframe(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("iframe", content, **kwargs)

    def open_x(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("x", close_tag=False, **kwargs))

    def close_x(self) -> None:
        self.write_html(self._render_end_tag("x"))

    def render_x(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("x", content, **kwargs)

    def open_div(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("div", close_tag=False, **kwargs))

    def close_div(self) -> None:
        self.write_html(self._render_end_tag("div"))

    def render_div(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("div", content, **kwargs)

    def open_ul(self, **kwargs: HTMLTagAttributeValue) -> None:
        self.write_html(self._render_start_tag("ul", close_tag=False, **kwargs))

    def close_ul(self) -> None:
        self.write_html(self._render_end_tag("ul"))

    def render_ul(self, content: HTMLContent, **kwargs: HTMLTagAttributeValue) -> HTML:
        return self._render_element("ul", content, **kwargs)
>>>>>>> upstream/master


#.
#   .--html----------------------------------------------------------------.
#   |                        _     _             _                         |
#   |                       | |__ | |_ _ __ ___ | |                        |
#   |                       | '_ \| __| '_ ` _ \| |                        |
#   |                       | | | | |_| | | | | | |                        |
#   |                       |_| |_|\__|_| |_| |_|_|                        |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Caution! The class needs to be derived from Outputfunnel first!      |
#   '----------------------------------------------------------------------'

<<<<<<< HEAD

class html(ABCHTMLGenerator):
    def __init__(self, request, response):
=======
OUTPUT_FORMAT_MIME_TYPES = {
    "json": "application/json",
    "json_export": "application/json",
    "jsonp": "application/javascript",
    "csv": "text/csv",
    "csv_export": "text/csv",
    "python": "text/plain",
    "text": "text/plain",
    "html": "text/html",
    "xml": "text/xml",
    "pdf": "application/pdf",
    "x-tgz": "application/x-tgz",
}


class html(ABCHTMLGenerator):
    def __init__(self, request: 'Request') -> None:
>>>>>>> upstream/master
        super(html, self).__init__()

        self._logger = log.logger.getChild("html")

        # rendering state
        self._header_sent = False
<<<<<<< HEAD
        self._context_buttons_open = False
=======
>>>>>>> upstream/master

        # style options
        self._body_classes = ['main']
        self._default_javascripts = ["main"]

        # behaviour options
        self.render_headfoot = True
        self.enable_debug = False
        self.screenshotmode = False
        self.have_help = False
<<<<<<< HEAD
        self.help_visible = False

        # browser options
        self.output_format = "html"
        self.browser_reload = 0
        self.browser_redirect = ''
        self.link_target = None
        self.myfile = None

        # Browser options
        self._user_id = None
        self.user_errors = {}
        self.focus_object = None
        self.events = set([])  # currently used only for sounds
        self.status_icons = {}
        self.final_javascript_code = ""
        self.treestates = None
        self.page_context = {}
=======

        # browser options
        self.output_format = "html"
        self.browser_reload = 0.0
        self.browser_redirect = ''
        self.link_target: Optional[str] = None

        # Browser options
        self.user_errors: Dict[Optional[str], str] = {}
        self.focus_object: Union[None, Tuple[Optional[str], str], str] = None
        self.final_javascript_code = ""
        self.page_context: 'VisualContext' = {}
>>>>>>> upstream/master

        # Settings
        self.mobile = False
        self._theme = "facelift"

        # Forms
<<<<<<< HEAD
        self.form_name = None
        self.form_vars = []

        # Time measurement
        self.times = {}
        self.start_time = time.time()
        self.last_measurement = self.start_time

        # Register helpers
        self.encoder = Encoder()
        self.timeout_manager = TimeoutManager()
        self.transaction_manager = TransactionManager(request)
        self.request = request
        self.response = response

=======
        self.form_name: Optional[str] = None
        self.form_vars: List[str] = []

        # Register helpers
        self.encoder = URLEncoder()
        self.timeout_manager = TimeoutManager()
        self.transaction_manager = TransactionManager(request)
        self.response = Response()
        self.output_funnel = OutputFunnel(self.response)
        self.request = request

        # TODO: Cleanup this side effect (then remove disable_request_timeout() e.g. from update_config.py)
>>>>>>> upstream/master
        self.enable_request_timeout()

        self.response.headers["Content-type"] = "text/html; charset=UTF-8"

        self.init_mobile()

<<<<<<< HEAD
        self.myfile = self._requested_file_name()
=======
        self.myfile = requested_file_name(self.request)
>>>>>>> upstream/master

        # Disable caching for all our pages as they are mostly dynamically generated,
        # user related and are required to be up-to-date on every refresh
        self.response.headers["Cache-Control"] = "no-cache"

        try:
<<<<<<< HEAD
            self.set_output_format(self.get_ascii_input("output_format", "html").lower())
        except (MKUserError, MKGeneralException):
            pass  # Silently ignore unsupported formats

    def _lowlevel_write(self, text):
        self.response.stream.write(text)

    def init_modes(self):
=======
            output_format = self.request.get_ascii_input_mandatory("output_format", "html")
            self.set_output_format(output_format.lower())
        except (MKUserError, MKGeneralException):
            pass  # Silently ignore unsupported formats

    def init_modes(self) -> None:
>>>>>>> upstream/master
        """Initializes the operation mode of the html() object. This is called
        after the Check_MK GUI configuration has been loaded, so it is safe
        to rely on the config."""
        self._verify_not_using_threaded_mpm()

        self._init_screenshot_mode()
        self._init_debug_mode()
        self._init_webapi_cors_header()
        self.init_theme()

<<<<<<< HEAD
    def _init_webapi_cors_header(self):
=======
    def _init_webapi_cors_header(self) -> None:
>>>>>>> upstream/master
        # Would be better to put this to page individual code, but we currently have
        # no mechanism for a page to set do this before the authentication is made.
        if self.myfile == "webapi":
            self.response.headers["Access-Control-Allow-Origin"] = "*"

<<<<<<< HEAD
    def init_theme(self):
        self.set_theme(config.ui_theme)

    def set_theme(self, theme_id):
        # type: (str) -> None
=======
    def init_theme(self) -> None:
        self.set_theme(config.ui_theme)

    def set_theme(self, theme_id: str) -> None:
>>>>>>> upstream/master
        if not theme_id:
            theme_id = config.ui_theme

        if theme_id not in dict(config.theme_choices()):
            theme_id = "facelift"

        self._theme = theme_id

<<<<<<< HEAD
    def get_theme(self):
        # type: () -> str
        return self._theme

    def theme_url(self, rel_url):
        # type: (str) -> str
        return "themes/%s/%s" % (self._theme, rel_url)

    def _verify_not_using_threaded_mpm(self):
        if self.request.is_multithreaded:
            raise MKGeneralException(
                _("You are trying to Check_MK together with a threaded Apache multiprocessing module (MPM). "
                  "Check_MK is only working with the prefork module. Please change the MPM module to make "
                  "Check_MK work."))

    def _init_debug_mode(self):
=======
    def get_theme(self) -> str:
        return self._theme

    def icon_themes(self) -> List[str]:
        """Returns the themes where icons of a theme can be found in increasing order of importance.
        By default the facelift theme provides all icons. If a theme wants to use different icons it
        only needs to add those icons under the same name. See detect_icon_path for a detailed list
        of paths.
        """
        return ["facelift"] if self._theme == "facelift" else ["facelift", self._theme]

    def theme_url(self, rel_url: str) -> str:
        return "themes/%s/%s" % (self._theme, rel_url)

    def _verify_not_using_threaded_mpm(self) -> None:
        if self.request.is_multithread:
            raise MKGeneralException(
                _("You are trying to Checkmk together with a threaded Apache multiprocessing module (MPM). "
                  "Check_MK is only working with the prefork module. Please change the MPM module to make "
                  "Check_MK work."))

    def _init_debug_mode(self) -> None:
>>>>>>> upstream/master
        # Debug flag may be set via URL to override the configuration
        if self.request.var("debug"):
            config.debug = True
        self.enable_debug = config.debug

    # Enabling the screenshot mode omits the fancy background and
    # makes it white instead.
<<<<<<< HEAD
    def _init_screenshot_mode(self):
        if self.request.var("screenshotmode", config.screenshotmode):
            self.screenshotmode = True

    def _requested_file_name(self):
        parts = self.request.requested_file.rstrip("/").split("/")

        if len(parts) == 3 and parts[-1] == "check_mk":
            # Load index page when accessing /[site]/check_mk
            myfile = "index"

        elif parts[-1].endswith(".py"):
            # Regular pages end with .py - Stript it away to get the page name
            myfile = parts[-1][:-3]
            if myfile == "":
                myfile = "index"

        else:
            myfile = "index"

        # Redirect to mobile GUI if we are a mobile device and the index is requested
        if myfile == "index" and self.mobile:
            myfile = "mobile"

        return myfile

    def init_mobile(self):
=======
    def _init_screenshot_mode(self) -> None:
        if self.request.var("screenshotmode", "1" if config.screenshotmode else ""):
            self.screenshotmode = True

    def init_mobile(self) -> None:
>>>>>>> upstream/master
        if self.request.has_var("mobile"):
            # TODO: Make private
            self.mobile = bool(self.request.var("mobile"))
            # Persist the explicitly set state in a cookie to have it maintained through further requests
            self.response.set_http_cookie("mobile", str(int(self.mobile)))

        elif self.request.has_cookie("mobile"):
            self.mobile = self.request.cookie("mobile", "0") == "1"

        else:
<<<<<<< HEAD
            self.mobile = self._is_mobile_client(self.request.user_agent)

    def _is_mobile_client(self, user_agent):
        # These regexes are taken from the public domain code of Matt Sullivan
        # http://sullerton.com/2011/03/django-mobile-browser-detection-middleware/
        reg_b = re.compile(
            r"android.+mobile|avantgo|bada\\/|blackberry|bb10|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|symbian|treo|up\\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino",
            re.I | re.M)
        reg_v = re.compile(
            r"1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\\-(n|u)|c55\\/|capi|ccwa|cdm\\-|cell|chtm|cldc|cmd\\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\\-s|devi|dica|dmob|do(c|p)o|ds(12|\\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\\-|_)|g1 u|g560|gene|gf\\-5|g\\-mo|go(\\.w|od)|gr(ad|un)|haie|hcit|hd\\-(m|p|t)|hei\\-|hi(pt|ta)|hp( i|ip)|hs\\-c|ht(c(\\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\\-(20|go|ma)|i230|iac( |\\-|\\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\\/)|klon|kpt |kwc\\-|kyo(c|k)|le(no|xi)|lg( g|\\/(k|l|u)|50|54|e\\-|e\\/|\\-[a-w])|libw|lynx|m1\\-w|m3ga|m50\\/|ma(te|ui|xo)|mc(01|21|ca)|m\\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\\-2|po(ck|rt|se)|prox|psio|pt\\-g|qa\\-a|qc(07|12|21|32|60|\\-[2-7]|i\\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\\-|oo|p\\-)|sdk\\/|se(c(\\-|0|1)|47|mc|nd|ri)|sgh\\-|shar|sie(\\-|m)|sk\\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\\-|v\\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\\-|tdg\\-|tel(i|m)|tim\\-|t\\-mo|to(pl|sh)|ts(70|m\\-|m3|m5)|tx\\-9|up(\\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|xda(\\-|2|g)|yas\\-|your|zeto|zte\\-",
            re.I | re.M)

        return reg_b.search(user_agent) or reg_v.search(user_agent[0:4])
=======
            self.mobile = self._is_mobile_client(self.request.user_agent.string)

    def _is_mobile_client(self, user_agent: str) -> bool:
        # These regexes are taken from the public domain code of Matt Sullivan
        # http://sullerton.com/2011/03/django-mobile-browser-detection-middleware/
        reg_b = re.compile(
            r"android.+mobile|avantgo|bada\\/|blackberry|bb10|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|symbian|treo|up\\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino",  # noqa: E501
            re.I | re.M)
        reg_v = re.compile(
            r"1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\\-(n|u)|c55\\/|capi|ccwa|cdm\\-|cell|chtm|cldc|cmd\\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\\-s|devi|dica|dmob|do(c|p)o|ds(12|\\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\\-|_)|g1 u|g560|gene|gf\\-5|g\\-mo|go(\\.w|od)|gr(ad|un)|haie|hcit|hd\\-(m|p|t)|hei\\-|hi(pt|ta)|hp( i|ip)|hs\\-c|ht(c(\\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\\-(20|go|ma)|i230|iac( |\\-|\\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\\/)|klon|kpt |kwc\\-|kyo(c|k)|le(no|xi)|lg( g|\\/(k|l|u)|50|54|e\\-|e\\/|\\-[a-w])|libw|lynx|m1\\-w|m3ga|m50\\/|ma(te|ui|xo)|mc(01|21|ca)|m\\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\\-2|po(ck|rt|se)|prox|psio|pt\\-g|qa\\-a|qc(07|12|21|32|60|\\-[2-7]|i\\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\\-|oo|p\\-)|sdk\\/|se(c(\\-|0|1)|47|mc|nd|ri)|sgh\\-|shar|sie(\\-|m)|sk\\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\\-|v\\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\\-|tdg\\-|tel(i|m)|tim\\-|t\\-mo|to(pl|sh)|ts(70|m\\-|m3|m5)|tx\\-9|up(\\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|xda(\\-|2|g)|yas\\-|your|zeto|zte\\-",  # noqa: E501
            re.I | re.M)

        return reg_b.search(user_agent) is not None or reg_v.search(user_agent[0:4]) is not None
>>>>>>> upstream/master

    #
    # HTTP variable processing
    #

    @contextmanager
<<<<<<< HEAD
    def stashed_vars(self):
=======
    def stashed_vars(self) -> Iterator[None]:
>>>>>>> upstream/master
        saved_vars = dict(self.request.itervars())
        try:
            yield
        finally:
            self.request.del_vars()
<<<<<<< HEAD
            for varname, value in saved_vars.iteritems():
                self.request.set_var(varname, value)

    def get_ascii_input(self, varname, deflt=None):
        """Helper to retrieve a byte string and ensure it only contains ASCII characters
        In case a non ASCII character is found an MKUserError() is raised."""
        try:
            value = self.request.var(varname, deflt)
            if value is not None:
                value.decode("ascii")
            return value
        except UnicodeDecodeError:
            raise MKUserError(varname, _("The given text must only contain ASCII characters."))

    def get_unicode_input(self, varname, deflt=None):
        try:
            val = self.request.var(varname, deflt)
            return val.decode("utf-8") if isinstance(val, str) else val
        except UnicodeDecodeError:
            raise MKUserError(
                varname,
                _("The given text is wrong encoded. "
                  "You need to provide a UTF-8 encoded text."))

    def get_item_input(self, varname, collection):
        """Helper to get an item from the given collection
        Raises a MKUserError() in case the requested item is not available."""
        item = self.get_ascii_input(varname)
        if item not in collection:
            raise MKUserError(varname, _("The requested item %s does not exist") % item)
        return collection[item], item

    def get_integer_input(self, varname, deflt=None):
        if deflt is not None and not self.request.has_var(varname):
            return deflt

        try:
            return int(self.request.var(varname))
        except TypeError:
            raise MKUserError(varname, _("The parameter \"%s\" is missing.") % varname)
        except ValueError:
            raise MKUserError(varname, _("The parameter \"%s\" is not an integer.") % varname)

    # TODO: Invalid default URL is not validated. Should we do it?
    # TODO: This is only protecting against some not allowed URLs but does not
    #       really verify that this is some kind of URL.
    def get_url_input(self, varname, deflt=None):
=======
            for varname, value in saved_vars.items():
                self.request.set_var(varname, value)

    def del_var_from_env(self, varname: str) -> None:
        # HACKY WORKAROUND, REMOVE WHEN NO LONGER NEEDED
        # We need to get rid of query-string entries which can contain secret information.
        # As this is the only location where these are stored on the WSGI environment this
        # should be enough.
        # See also cmk.gui.globals:RequestContext
        # Filter the variables even if there are multiple copies of them (this is allowed).
        decoded_qs = [
            (key, value) for key, value in self.request.args.items(multi=True) if key != varname
        ]
        self.request.environ['QUERY_STRING'] = urllib.parse.urlencode(decoded_qs)
        # We remove the form entry. As this entity is never copied it will be modified within
        # it's cache.
        dict.pop(self.request.form, varname, None)
        # We remove the __dict__ entries to allow @cached_property to reload them from
        # the environment. The rest of the request object stays the same.
        self.request.__dict__.pop('args', None)
        self.request.__dict__.pop('values', None)

    def get_item_input(self, varname: str, collection: Mapping[str, Value]) -> Tuple[Value, str]:
        """Helper to get an item from the given collection
        Raises a MKUserError() in case the requested item is not available."""
        item = self.request.get_ascii_input(varname)
        if item not in collection:
            raise MKUserError(varname, _("The requested item %s does not exist") % item)
        assert item is not None
        return collection[item], item

    # TODO: Invalid default URL is not validated. Should we do it?
    # TODO: This is only protecting against some not allowed URLs but does not
    #       really verify that this is some kind of URL.
    def get_url_input(self, varname: str, deflt: Optional[str] = None) -> str:
>>>>>>> upstream/master
        """Helper function to retrieve a URL from HTTP parameters

        This is mostly used to the "back url" which can then be used to create
        a link to the previous page. For this kind of functionality it is
        necessary to restrict the URLs to prevent different attacks on users.

        In case the parameter is not given or is not valid the deflt URL will
        be used. In case no deflt URL is given a MKUserError() is raised.
        """
        if not self.request.has_var(varname):
            if deflt is not None:
                return deflt
            raise MKUserError(varname, _("The parameter \"%s\" is missing.") % varname)

        url = self.request.var(varname)
<<<<<<< HEAD
=======
        assert url is not None

>>>>>>> upstream/master
        if not utils.is_allowed_url(url):
            if deflt:
                return deflt
            raise MKUserError(varname, _("The parameter \"%s\" is not a valid URL.") % varname)

        return url

<<<<<<< HEAD
    # Returns a dictionary containing all parameters the user handed over to this request.
    # The concept is that the user can either provide the data in a single "request" variable,
    # which contains the request data encoded as JSON, or provide multiple GET/POST vars which
    # are then used as top level entries in the request object.
    def get_request(self, exclude_vars=None):
=======
    def get_request(self, exclude_vars: Optional[List[str]] = None) -> Dict[str, Any]:
        """Returns a dictionary containing all parameters the user handed over to this request.

        The concept is that the user can either provide the data in a single "request" variable,
        which contains the request data encoded as JSON, or provide multiple GET/POST vars which
        are then used as top level entries in the request object.
        """

>>>>>>> upstream/master
        if exclude_vars is None:
            exclude_vars = []

        if self.request.var("request_format") == "python":
            try:
                python_request = self.request.var("request", "{}")
<<<<<<< HEAD
=======
                assert python_request is not None
>>>>>>> upstream/master
                request = ast.literal_eval(python_request)
            except (SyntaxError, ValueError) as e:
                raise MKUserError(
                    "request",
                    _("Failed to parse Python request: '%s': %s") % (python_request, e))
        else:
            try:
                json_request = self.request.var("request", "{}")
<<<<<<< HEAD
=======
                assert json_request is not None
>>>>>>> upstream/master
                request = json.loads(json_request)
                request["request_format"] = "json"
            except ValueError as e:  # Python3: json.JSONDecodeError
                raise MKUserError("request",
                                  _("Failed to parse JSON request: '%s': %s") % (json_request, e))

        for key, val in self.request.itervars():
            if key not in ["request", "output_format"] + exclude_vars:
<<<<<<< HEAD
                request[key] = val.decode("utf-8")
=======
                request[key] = ensure_str(val) if isinstance(val, bytes) else val
>>>>>>> upstream/master

        return request

    #
    # Transaction IDs
    #

    # TODO: Cleanup all call sites to self.transaction_manager.*
<<<<<<< HEAD
    def transaction_valid(self):
        return self.transaction_manager.transaction_valid()

    # TODO: Cleanup all call sites to self.transaction_manager.*
    def is_transaction(self):
        return self.transaction_manager.is_transaction()

    # TODO: Cleanup all call sites to self.transaction_manager.*
    def check_transaction(self):
=======
    def transaction_valid(self) -> bool:
        return self.transaction_manager.transaction_valid()

    # TODO: Cleanup all call sites to self.transaction_manager.*
    def is_transaction(self) -> bool:
        return self.transaction_manager.is_transaction()

    # TODO: Cleanup all call sites to self.transaction_manager.*
    def check_transaction(self) -> bool:
>>>>>>> upstream/master
        return self.transaction_manager.check_transaction()

    #
    # Encoding
    #

    # TODO: Cleanup all call sites to self.encoder.*
<<<<<<< HEAD
    def urlencode_vars(self, vars_):
        return self.encoder.urlencode_vars(vars_)

    # TODO: Cleanup all call sites to self.encoder.*
    def urlencode(self, value):
        return self.encoder.urlencode(value)

    #
    # escaping - deprecated functions
    #
    # Encode HTML attributes: e.g. replace '"' with '&quot;', '<' and '>' with '&lt;' and '&gt;'
    # TODO: Cleanup all call sites to self.escaper.*
    def attrencode(self, value):
        return self.escaper.escape_attribute(value)

    # Only strip off some tags. We allow some simple tags like <b> or <tt>.
    # TODO: Cleanup all call sites to self.escaper.*
    def permissive_attrencode(self, obj):
        return self.escaper.escape_text(obj)

    #
    # Stripping
    #

    # remove all HTML-tags
    def strip_tags(self, ht):

        if isinstance(ht, HTML):
            ht = "%s" % ht

        if not isinstance(ht, six.string_types):
            return ht

        while True:
            x = ht.find('<')
            if x == -1:
                break
            y = ht.find('>', x)
            if y == -1:
                break
            ht = ht[0:x] + ht[y + 1:]
        return ht.replace("&nbsp;", " ")

    def strip_scripts(self, ht):
        while True:
            x = ht.find('<script')
            if x == -1:
                break
            y = ht.find('</script>')
            if y == -1:
                break
            ht = ht[0:x] + ht[y + 9:]
        return ht
=======
    def urlencode_vars(self, vars_: List[Tuple[str, Union[None, int, str]]]) -> str:
        return self.encoder.urlencode_vars(vars_)

    # TODO: Cleanup all call sites to self.encoder.*
    def urlencode(self, value: Optional[str]) -> str:
        return self.encoder.urlencode(value)

    #
    # output funnel
    #

    def write(self, text: 'OutputFunnelInput') -> None:
        self.output_funnel.write(text)

    def write_binary(self, data: bytes) -> None:
        self.output_funnel.write_binary(data)

    @contextmanager
    def plugged(self) -> Iterator[None]:
        with self.output_funnel.plugged():
            yield

    def drain(self) -> str:
        return self.output_funnel.drain()
>>>>>>> upstream/master

    #
    # Timeout handling
    #

<<<<<<< HEAD
    def enable_request_timeout(self):
        self.timeout_manager.enable_timeout(self.request.request_timeout)

    def disable_request_timeout(self):
=======
    def enable_request_timeout(self) -> None:
        self.timeout_manager.enable_timeout(self.request.request_timeout)

    def disable_request_timeout(self) -> None:
>>>>>>> upstream/master
        self.timeout_manager.disable_timeout()

    #
    # Content Type
    #

<<<<<<< HEAD
    def set_output_format(self, f):
        if f == "json":
            content_type = "application/json; charset=UTF-8"

        elif f == "jsonp":
            content_type = "application/javascript; charset=UTF-8"

        elif f in ("csv", "csv_export"):  # Cleanup: drop one of these
            content_type = "text/csv; charset=UTF-8"

        elif f == "python":
            content_type = "text/plain; charset=UTF-8"

        elif f == "text":
            content_type = "text/plain; charset=UTF-8"

        elif f == "html":
            content_type = "text/html; charset=UTF-8"

        elif f == "xml":
            content_type = "text/xml; charset=UTF-8"

        elif f == "pdf":
            content_type = "application/pdf"

        else:
            raise MKGeneralException(_("Unsupported context type '%s'") % f)

        self.output_format = f
        self.response.headers["Content-type"] = content_type

    def is_api_call(self):
=======
    def set_output_format(self, f: str) -> None:
        if f not in OUTPUT_FORMAT_MIME_TYPES:
            raise MKGeneralException(_("Unsupported context type '%s'") % f)

        self.output_format = f
        self.response.set_content_type(OUTPUT_FORMAT_MIME_TYPES[f])

    def is_api_call(self) -> bool:
>>>>>>> upstream/master
        return self.output_format != "html"

    #
    # Other things
    #

<<<<<<< HEAD
    def measure_time(self, name):
        self.times.setdefault(name, 0.0)
        now = time.time()
        elapsed = now - self.last_measurement
        self.times[name] += elapsed
        self.last_measurement = now

    def set_user_id(self, user_id):
        self._user_id = user_id
        # TODO: Shouldn't this be moved to some other place?
        self.help_visible = config.user.load_file("help", False)  # cache for later usage

    def is_mobile(self):
        return self.mobile

    def set_page_context(self, c):
        self.page_context = c

    def set_link_target(self, framename):
        self.link_target = framename

    def set_focus(self, varname):
        self.focus_object = (self.form_name, varname)

    def set_focus_by_id(self, dom_id):
        self.focus_object = dom_id

    def set_render_headfoot(self, render):
        self.render_headfoot = render

    def set_browser_reload(self, secs):
        self.browser_reload = secs

    def set_browser_redirect(self, secs, url):
        self.browser_reload = secs
        self.browser_redirect = url

    def clear_default_javascript(self):
        del self._default_javascripts[:]

    def add_default_javascript(self, name):
        if name not in self._default_javascripts:
            self._default_javascripts.append(name)

    def immediate_browser_redirect(self, secs, url):
        self.javascript("cmk.utils.set_reload(%s, '%s');" % (secs, url))

    def add_body_css_class(self, cls):
        self._body_classes.append(cls)

    def add_status_icon(self, img, tooltip, url=None):
        if url:
            self.status_icons[img] = tooltip, url
        else:
            self.status_icons[img] = tooltip

    def final_javascript(self, code):
        self.final_javascript_code += code + "\n"

    def reload_sidebar(self):
        if not self.request.has_var("_ajaxid"):
            self.write_html(self.render_reload_sidebar())

    def render_reload_sidebar(self):
        return self.render_javascript("cmk.utils.reload_sidebar()")

    #
    # Tree states
    #

    def get_tree_states(self, tree):
        self.load_tree_states()
        return self.treestates.get(tree, {})

    def set_tree_state(self, tree, key, val):
        self.load_tree_states()

        if tree not in self.treestates:
            self.treestates[tree] = {}

        self.treestates[tree][key] = val

    def set_tree_states(self, tree, val):
        self.load_tree_states()
        self.treestates[tree] = val

    def save_tree_states(self):
        config.user.save_file("treestates", self.treestates)

    def load_tree_states(self):
        if self.treestates is None:
            self.treestates = config.user.load_file("treestates", {})

    def finalize(self):
        """Finish the HTTP request processing before handing over to the application server"""
        self.transaction_manager.store_new()
=======
    def is_mobile(self) -> bool:
        return self.mobile

    def set_page_context(self, c: 'VisualContext') -> None:
        self.page_context = c

    def set_link_target(self, framename: str) -> None:
        self.link_target = framename

    def set_focus(self, varname: str) -> None:
        self.focus_object = (self.form_name, varname)

    def set_focus_by_id(self, dom_id: str) -> None:
        self.focus_object = dom_id

    def set_render_headfoot(self, render: bool) -> None:
        self.render_headfoot = render

    def set_browser_reload(self, secs: float) -> None:
        self.browser_reload = secs

    def set_browser_redirect(self, secs: float, url: str) -> None:
        self.browser_reload = secs
        self.browser_redirect = url

    def clear_default_javascript(self) -> None:
        del self._default_javascripts[:]

    def add_default_javascript(self, name: str) -> None:
        if name not in self._default_javascripts:
            self._default_javascripts.append(name)

    def immediate_browser_redirect(self, secs: float, url: str) -> None:
        self.javascript("cmk.utils.set_reload(%s, '%s');" % (secs, url))

    def add_body_css_class(self, cls: str) -> None:
        self._body_classes.append(cls)

    def final_javascript(self, code: str) -> None:
        self.final_javascript_code += code + "\n"

    def reload_sidebar(self) -> None:
        if not self.request.has_var("_ajaxid"):
            self.write_html(self.render_reload_sidebar())

    def render_reload_sidebar(self) -> HTML:
        return self.render_javascript("cmk.utils.reload_sidebar()")

    def finalize(self) -> None:
        """Finish the HTTP request processing before handing over to the application server"""
>>>>>>> upstream/master
        self.disable_request_timeout()

    #
    # Messages
    #

<<<<<<< HEAD
    def show_info(self, msg):
        self.message(msg, 'message')

    def show_error(self, msg):
        self.message(msg, 'error')

    def show_warning(self, msg):
        self.message(msg, 'warning')

    def render_info(self, msg):
        return self.render_message(msg, 'message')

    def render_error(self, msg):
        return self.render_message(msg, 'error')

    def render_warning(self, msg):
        return self.render_message(msg, 'warning')

    def message(self, msg, what='message'):
        self.write(self.render_message(msg, what))

    # obj might be either a string (str or unicode) or an exception object
    def render_message(self, msg, what='message'):
=======
    def show_message(self, msg: HTMLMessageInput) -> None:
        self.write(self._render_message(msg, 'message'))

    def show_error(self, msg: HTMLMessageInput) -> None:
        self.write(self._render_message(msg, 'error'))

    def show_warning(self, msg: HTMLMessageInput) -> None:
        self.write(self._render_message(msg, 'warning'))

    def render_message(self, msg: HTMLMessageInput) -> HTML:
        return self._render_message(msg, 'message')

    def render_error(self, msg: HTMLMessageInput) -> HTML:
        return self._render_message(msg, 'error')

    def render_warning(self, msg: HTMLMessageInput) -> HTML:
        return self._render_message(msg, 'warning')

    # obj might be either a string (str or unicode) or an exception object
    def _render_message(self, msg: HTMLMessageInput, what: str = 'message') -> HTML:
>>>>>>> upstream/master
        if what == 'message':
            cls = 'success'
            prefix = _('MESSAGE')
        elif what == 'warning':
            cls = 'warning'
            prefix = _('WARNING')
        else:
            cls = 'error'
            prefix = _('ERROR')

<<<<<<< HEAD
        code = ""
=======
        code = HTML()
>>>>>>> upstream/master

        if self.output_format == "html":
            code += self.render_div(self.render_text(msg), class_=cls)
            if self.mobile:
                code += self.render_center(code)
        else:
<<<<<<< HEAD
            code += self.render_text('%s: %s\n' % (prefix, self.strip_tags(msg)))

        return code

    def show_localization_hint(self):
        url = "wato.py?mode=edit_configvar&varname=user_localizations"
        self.message(
=======
            code += self.render_text('%s: %s\n' % (prefix, escaping.strip_tags(msg)))

        return code

    def show_localization_hint(self) -> None:
        url = "wato.py?mode=edit_configvar&varname=user_localizations"
        self.show_message(
>>>>>>> upstream/master
            self.render_sup("*") + _("These texts may be localized depending on the users' "
                                     "language. You can configure the localizations %s.") %
            self.render_a("in the global settings", href=url))

<<<<<<< HEAD
    def del_language_cookie(self):
        self.response.delete_cookie("language")

    def set_language_cookie(self, lang):
        # type: (str) -> None
        cookie_lang = self.request.cookie("language")
        if cookie_lang != lang:
            if lang is not None:
                self.response.set_http_cookie("language", lang)
            else:
                self.del_language_cookie()

    def help(self, text):
        self.write_html(self.render_help(text))

    def render_help(self, text):
        """Embed help box, whose visibility is controlled by a global button in the page."""
        if text and text.strip():
            self.enable_help_toggle()
            style = "display: %s;" % ("block" if self.help_visible else "none")
            c = self.render_div(text.strip(), class_="help", style=style)
            return c
        return ""

    def enable_help_toggle(self):
=======
    def del_language_cookie(self) -> None:
        self.response.delete_cookie("language")

    def set_language_cookie(self, lang: Optional[str]) -> None:
        cookie_lang = self.request.cookie("language")
        if cookie_lang == lang:
            return
        if lang is None:
            self.del_language_cookie()
        else:
            self.response.set_http_cookie("language", lang)

    def help(self, text: Union[None, HTML, str]) -> None:
        """Embed help box, whose visibility is controlled by a global button in the page.

        You may add macros like this to the help texts to create links to the user
        manual: [cms_piggyback|Piggyback chapter].
        """
        self.write_html(self.render_help(text))

    def render_help(self, text: Union[None, HTML, str]) -> HTML:
        if isinstance(text, HTML):
            text = "%s" % text

        if not text:
            return HTML("")

        stripped = text.strip()
        if not stripped:
            return HTML("")

        help_text = self._resolve_help_text_macros(stripped)

        self.enable_help_toggle()
        style = "display:%s;" % ("block" if config.user.show_help else "none")
        return self.render_div(HTML(help_text), class_="help", style=style)

    def _resolve_help_text_macros(self, text: str) -> str:
        if config.user.language == "de":
            cmk_base_url = "https://checkmk.de"
        else:
            cmk_base_url = "https://checkmk.com"
        return re.sub(r"\[([a-z0-9_-]+)(#[a-z0-9_-]+|)\|([^\]]+)\]",
                      "<a href=\"%s/\\1.html\\2\" target=\"_blank\">\\3</a>" % cmk_base_url, text)

    def enable_help_toggle(self) -> None:
>>>>>>> upstream/master
        self.have_help = True

    #
    # Debugging, diagnose and logging
    #

<<<<<<< HEAD
    def debug(self, *x):
=======
    def debug(self, *x: Any) -> None:
>>>>>>> upstream/master
        for element in x:
            try:
                formatted = pprint.pformat(element)
            except UnicodeDecodeError:
                formatted = repr(element)
            self.write(self.render_pre(formatted))

    #
    # URL building
    #

<<<<<<< HEAD
    # [('varname1', value1), ('varname2', value2) ]
    def makeuri(self, addvars, remove_prefix=None, filename=None, delvars=None):
        new_vars = [nv[0] for nv in addvars]
        vars_ = [(v, val)
                 for v, val in self.request.itervars()
                 if v[0] != "_" and v not in new_vars and (not delvars or v not in delvars)]
        if remove_prefix is not None:
            vars_ = [i for i in vars_ if not i[0].startswith(remove_prefix)]
        vars_ = vars_ + addvars
        if filename is None:
            filename = self.urlencode(self.myfile) + ".py"
        if vars_:
            return filename + "?" + self.urlencode_vars(vars_)
        return filename

    def makeuri_contextless(self, vars_, filename=None):
        if not filename:
            filename = self.myfile + ".py"
        if vars_:
            return filename + "?" + self.urlencode_vars(vars_)
        return filename

    def makeactionuri(self, addvars, filename=None, delvars=None):
        return self.makeuri(addvars + [("_transid", self.transaction_manager.get())],
                            filename=filename,
                            delvars=delvars)

    def makeactionuri_contextless(self, addvars, filename=None):
        return self.makeuri_contextless(addvars + [("_transid", self.transaction_manager.get())],
                                        filename=filename)
=======
    def makeactionuri(self,
                      addvars: 'HTTPVariables',
                      filename: Optional[str] = None,
                      delvars: Optional[Sequence[str]] = None) -> str:
        return makeactionuri(
            self.request,
            self.transaction_manager,
            addvars,
            filename=filename,
            delvars=delvars,
        )

    def makeactionuri_contextless(self,
                                  addvars: 'HTTPVariables',
                                  filename: Optional[str] = None) -> str:
        return makeactionuri_contextless(
            self.request,
            self.transaction_manager,
            addvars,
            filename=filename,
        )
>>>>>>> upstream/master

    #
    # HTML heading and footer rendering
    #

<<<<<<< HEAD
    def default_html_headers(self):
        self.meta(httpequiv="Content-Type", content="text/html; charset=utf-8")
        self.meta(httpequiv="X-UA-Compatible", content="IE=edge")
        self.write_html(
            self._render_opening_tag('link',
                                     rel="shortcut icon",
                                     href="themes/%s/images/favicon.ico" % self._theme,
                                     type_="image/ico",
                                     close_tag=True))

    def _head(self, title, javascripts=None):
=======
    def default_html_headers(self) -> None:
        self.meta(httpequiv="Content-Type", content="text/html; charset=utf-8")
        self.write_html(
            self._render_start_tag('link',
                                   rel="shortcut icon",
                                   href="themes/%s/images/favicon.ico" % self._theme,
                                   type_="image/ico",
                                   close_tag=True))

    def _head(self, title: str, javascripts: Optional[List[str]] = None) -> None:
>>>>>>> upstream/master
        javascripts = javascripts if javascripts else []

        self.open_head()

        self.default_html_headers()
        self.title(title)

        # If the variable _link_target is set, then all links in this page
        # should be targetted to the HTML frame named by _link_target. This
        # is e.g. useful in the dash-board
        if self.link_target:
            self.base(target=self.link_target)

        fname = self._css_filename_for_browser("themes/%s/theme" % self._theme)
        if fname is not None:
            self.stylesheet(fname)

        self._add_custom_style_sheet()

        # Load all scripts
        for js in self._default_javascripts + javascripts:
            filename_for_browser = self.javascript_filename_for_browser(js)
            if filename_for_browser:
                self.javascript_file(filename_for_browser)

<<<<<<< HEAD
        if self.browser_reload != 0:
=======
        if self.browser_reload != 0.0:
>>>>>>> upstream/master
            if self.browser_redirect != '':
                self.javascript('cmk.utils.set_reload(%s, \'%s\')' %
                                (self.browser_reload, self.browser_redirect))
            else:
                self.javascript('cmk.utils.set_reload(%s)' % (self.browser_reload))

        self.close_head()

<<<<<<< HEAD
    def _add_custom_style_sheet(self):
=======
    def _add_custom_style_sheet(self) -> None:
>>>>>>> upstream/master
        for css in self._plugin_stylesheets():
            self.write('<link rel="stylesheet" type="text/css" href="css/%s">\n' % css)

        if config.custom_style_sheet:
            self.write('<link rel="stylesheet" type="text/css" href="%s">\n' %
                       config.custom_style_sheet)

<<<<<<< HEAD
        if self._theme == "classic" and cmk.is_managed_edition():
            import cmk.gui.cme.gui_colors as gui_colors
            gui_colors.GUIColors().render_html()

    def _plugin_stylesheets(self):
        plugin_stylesheets = set([])
        for directory in [
                Path(cmk.utils.paths.web_dir, "htdocs", "css"),
                cmk.utils.paths.local_web_dir.joinpath("htdocs", "css"),
=======
    def _plugin_stylesheets(self) -> Set[str]:
        plugin_stylesheets = set([])
        for directory in [
                Path(cmk.utils.paths.web_dir, "htdocs", "css"),
                cmk.utils.paths.local_web_dir / "htdocs" / "css",
>>>>>>> upstream/master
        ]:
            if directory.exists():
                for entry in directory.iterdir():
                    if entry.suffix == ".css":
                        plugin_stylesheets.add(entry.name)
        return plugin_stylesheets

    # Make the browser load specified javascript files. We have some special handling here:
    # a) files which can not be found shal not be loaded
<<<<<<< HEAD
    # b) in OMD environments, add the Check_MK version to the version (prevents update problems)
    # c) load the minified javascript when not in debug mode
    def javascript_filename_for_browser(self, jsname):
=======
    # b) in OMD environments, add the Checkmk version to the version (prevents update problems)
    # c) load the minified javascript when not in debug mode
    def javascript_filename_for_browser(self, jsname: str) -> Optional[str]:
>>>>>>> upstream/master
        filename_for_browser = None
        rel_path = "/share/check_mk/web/htdocs/js"
        if self.enable_debug:
            min_parts = ["", "_min"]
        else:
            min_parts = ["_min", ""]

        for min_part in min_parts:
            path_pattern = cmk.utils.paths.omd_root + "%s" + rel_path + "/" + jsname + min_part + ".js"
            if os.path.exists(path_pattern % "") or os.path.exists(path_pattern % "/local"):
<<<<<<< HEAD
                filename_for_browser = 'js/%s%s-%s.js' % (jsname, min_part, cmk.__version__)
=======
                filename_for_browser = 'js/%s%s-%s.js' % (jsname, min_part, cmk_version.__version__)
>>>>>>> upstream/master
                break

        return filename_for_browser

<<<<<<< HEAD
    def _css_filename_for_browser(self, css):
        rel_path = "/share/check_mk/web/htdocs/" + css + ".css"
        if os.path.exists(cmk.utils.paths.omd_root + rel_path) or \
            os.path.exists(cmk.utils.paths.omd_root + "/local" + rel_path):
            return '%s-%s.css' % (css, cmk.__version__)

    def html_head(self, title, javascripts=None, force=False):

=======
    def _css_filename_for_browser(self, css: str) -> Optional[str]:
        rel_path = "/share/check_mk/web/htdocs/" + css + ".css"
        if os.path.exists(cmk.utils.paths.omd_root + rel_path) or \
            os.path.exists(cmk.utils.paths.omd_root + "/local" + rel_path):
            return '%s-%s.css' % (css, cmk_version.__version__)
        return None

    def html_head(self,
                  title: str,
                  javascripts: Optional[List[str]] = None,
                  force: bool = False) -> None:
>>>>>>> upstream/master
        force_new_document = force  # for backward stability and better readability

        if force_new_document:
            self._header_sent = False

        if not self._header_sent:
<<<<<<< HEAD
            self.write_html('<!DOCTYPE HTML>\n')
=======
            self.write_html(HTML('<!DOCTYPE HTML>\n'))
>>>>>>> upstream/master
            self.open_html()
            self._head(title, javascripts)
            self._header_sent = True

    def header(self,
<<<<<<< HEAD
               title='',
               javascripts=None,
               force=False,
               show_body_start=True,
               show_top_heading=True):
=======
               title: str,
               breadcrumb: Breadcrumb,
               page_menu: Optional[PageMenu] = None,
               page_state: Optional[PageState] = None,
               javascripts: Optional[List[str]] = None,
               force: bool = False,
               show_body_start: bool = True,
               show_top_heading: bool = True) -> None:
>>>>>>> upstream/master
        if self.output_format == "html":
            if not self._header_sent:
                if show_body_start:
                    self.body_start(title, javascripts=javascripts, force=force)

                self._header_sent = True

<<<<<<< HEAD
                if self.render_headfoot and show_top_heading:
                    self.top_heading(title)

    def body_start(self, title='', javascripts=None, force=False):
        self.html_head(title, javascripts, force)
        self.open_body(class_=self._get_body_css_classes())

    def _get_body_css_classes(self):
        if self.screenshotmode:
            return self._body_classes + ["screenshotmode"]
        return self._body_classes

    def html_foot(self):
        self.close_html()

    def top_heading(self, title):
        if not isinstance(config.user, config.LoggedInNobody):
            login_text = "<b>%s</b> (%s" % (config.user.id, "+".join(config.user.role_ids))
            if self.enable_debug:
                if config.user.language():
                    login_text += "/%s" % config.user.language()
            login_text += ')'
        else:
            login_text = _("not logged in")
        self.top_heading_left(title)

        self.write('<td style="min-width:240px" class=right><span id=headinfo></span>%s &nbsp; ' %
                   login_text)
        if config.pagetitle_date_format:
            self.write(' &nbsp; <b id=headerdate format="%s"></b>' % config.pagetitle_date_format)
        self.write(' <b id=headertime></b>')
        self.top_heading_right()

    def top_heading_left(self, title):
        self.open_table(class_="header")
        self.open_tr()
        self.open_td(width="*", class_="heading")
        # HTML() is needed here to prevent a double escape when we do  self._escape_attribute
        # here and self.a() escapes the content (with permissive escaping) again. We don't want
        # to handle "title" permissive.
        title = HTML(self.escaper.escape_attribute(title))
        self.a(title,
               href="#",
               onfocus="if (this.blur) this.blur();",
               onclick="this.innerHTML=\'%s\'; document.location.reload();" % _("Reloading..."))
        self.close_td()

    def top_heading_right(self):
        cssclass = "active" if self.help_visible else "passive"

        self.icon_button(None,
                         _("Toggle context help texts"),
                         "help",
                         id_="helpbutton",
                         onclick="cmk.help.toggle()",
                         style="display:none",
                         cssclass=cssclass)
        self.open_a(href="https://checkmk.com", class_="head_logo", target="_blank")
        self.img(src="themes/%s/images/logo_cmk_small.png" % self._theme)
        self.close_a()
        self.close_td()
        self.close_tr()
        self.close_table()
        self.hr(class_="header")
=======
                breadcrumb = breadcrumb or Breadcrumb()

                if self.render_headfoot and show_top_heading:
                    self.top_heading(
                        title,
                        breadcrumb=breadcrumb,
                        page_menu=page_menu or PageMenu(breadcrumb=breadcrumb),
                        page_state=page_state,
                    )
            self.begin_page_content()

    def body_start(self,
                   title: str = u'',
                   javascripts: Optional[List[str]] = None,
                   force: bool = False) -> None:
        self.html_head(title, javascripts, force)
        self.open_body(class_=self._get_body_css_classes())

    def _get_body_css_classes(self) -> List[str]:
        classes = self._body_classes[:]
        if self.screenshotmode:
            classes += ["screenshotmode"]
        return classes

    def html_foot(self) -> None:
        self.close_html()

    def top_heading(self,
                    title: str,
                    breadcrumb: Breadcrumb,
                    page_menu: Optional[PageMenu] = None,
                    page_state: Optional[PageState] = None) -> None:
        self.open_div(id_="top_heading")
        self.open_div(class_="titlebar")

        # HTML() is needed here to prevent a double escape when we do  self._escape_attribute
        # here and self.a() escapes the content (with permissive escaping) again. We don't want
        # to handle "title" permissive.
        html_title = HTML(escaping.escape_attribute(title))
        self.a(html_title,
               class_="title",
               href="#",
               onfocus="if (this.blur) this.blur();",
               onclick="this.innerHTML=\'%s\'; document.location.reload();" % _("Reloading..."))

        if breadcrumb:
            BreadcrumbRenderer().show(breadcrumb)

        if page_state is None:
            page_state = self._make_default_page_state()

        if page_state:
            PageStateRenderer().show(page_state)

        self.close_div()  # titlebar

        if page_menu:
            PageMenuRenderer().show(
                page_menu,
                hide_suggestions=not self.foldable_container_is_open("suggestions", "all", True),
                has_changes=bool(get_pending_changes_info() and
                                 (not page_state or self.browser_reload)),
            )

        self.close_div()  # top_heading

        if page_menu:
            PageMenuPopupsRenderer().show(page_menu)
>>>>>>> upstream/master

        if self.enable_debug:
            self._dump_get_vars()

<<<<<<< HEAD
    def footer(self, show_footer=True, show_body_end=True):
        if self.output_format == "html":
=======
    def _make_default_page_state(self) -> Optional[PageState]:
        """Create a general page state for all pages without specific one"""
        if not self.browser_reload:
            return None

        return PageState(
            top_line=_("%d sec. update") % self.browser_reload,
            bottom_line=self.render_a(_("Reload now"),
                                      href="javascript:void(0)",
                                      onclick="this.innerHTML=\'%s\'; document.location.reload();" %
                                      _("Reloading...")),
            icon_name="trans",
            css_classes=["default"],
        )

    def begin_page_content(self):
        content_id = "main_page_content"
        self.open_div(id_=content_id)
        self.final_javascript("cmk.utils.content_scrollbar(%s)" % json.dumps(content_id))

    def end_page_content(self):
        self.close_div()

    def footer(self, show_footer: bool = True, show_body_end: bool = True) -> None:
        if self.output_format == "html":
            self.end_page_content()
>>>>>>> upstream/master
            if show_footer:
                self.bottom_footer()

            if show_body_end:
                self.body_end()

<<<<<<< HEAD
    def bottom_footer(self):
        if self._header_sent:
            self.bottom_focuscode()
            if self.render_headfoot:
                self.open_table(class_="footer")
                self.open_tr()

                self.open_td(class_="left")
                self._write_status_icons()
                self.close_td()

                self.td('', class_="middle")

                self.open_td(class_="right")
                content = _("refresh: %s secs") % self.render_div(self.browser_reload,
                                                                  id_="foot_refresh_time")
                style = "display:inline-block;" if self.browser_reload else "display:none;"
                self.div(HTML(content), id_="foot_refresh", style=style)
                self.close_td()

                self.close_tr()
                self.close_table()

    def bottom_focuscode(self):
        if self.focus_object:
            if isinstance(self.focus_object, tuple):
                formname, varname = self.focus_object
=======
    def bottom_footer(self) -> None:
        self.bottom_focuscode()

    def bottom_focuscode(self) -> None:
        if self.focus_object:
            if isinstance(self.focus_object, tuple):
                formname, varname = self.focus_object
                assert formname is not None
>>>>>>> upstream/master
                obj_ident = formname + "." + varname
            else:
                obj_ident = "getElementById(\"%s\")" % self.focus_object

            js_code = "<!--\n" \
                      "var focus_obj = document.%s;\n" \
                      "if (focus_obj) {\n" \
                      "    focus_obj.focus();\n" \
                      "    if (focus_obj.select)\n" \
                      "        focus_obj.select();\n" \
                      "}\n" \
                      "// -->\n" % obj_ident
            self.javascript(js_code)

<<<<<<< HEAD
    def focus_here(self):
        self.a("", href="#focus_me", id_="focus_me")
        self.set_focus_by_id("focus_me")

    def body_end(self):
        if self.have_help:
            self.javascript("cmk.help.enable();")
=======
    def focus_here(self) -> None:
        self.a("", href="#focus_me", id_="focus_me")
        self.set_focus_by_id("focus_me")

    def body_end(self) -> None:
        if self.have_help:
            enable_page_menu_entry("inline_help")
>>>>>>> upstream/master
        if self.final_javascript_code:
            self.javascript(self.final_javascript_code)
        self.javascript("cmk.visibility_detection.initialize();")
        self.close_body()
        self.close_html()

    #
    # HTML form rendering
    #

<<<<<<< HEAD
    def begin_form(self, name, action=None, method="GET", onsubmit=None, add_transid=True):
        self.form_vars = []
        if action is None:
=======
    def begin_form(self,
                   name: str,
                   action: Optional[str] = None,
                   method: str = "GET",
                   onsubmit: Optional[str] = None,
                   add_transid: bool = True) -> None:
        self.form_vars = []
        if action is None:
            assert self.myfile is not None
>>>>>>> upstream/master
            action = self.myfile + ".py"
        self.current_form = name
        self.open_form(id_="form_%s" % name,
                       name=name,
                       class_=name,
                       action=action,
                       method=method,
                       onsubmit=onsubmit,
                       enctype="multipart/form-data" if method.lower() == "post" else None)
        self.hidden_field("filled_in", name, add_var=True)
        if add_transid:
<<<<<<< HEAD
            self.hidden_field("_transid", str(self.transaction_manager.get()))
        self.form_name = name

    def end_form(self):
        self.close_form()
        self.form_name = None

    def in_form(self):
        return self.form_name is not None

    def prevent_password_auto_completion(self):
=======
            self.hidden_field(
                "_transid",
                str(self.transaction_manager.get()),
                add_var=True,
            )
        self.form_name = name

    def end_form(self) -> None:
        self.close_form()
        self.form_name = None

    def add_confirm_on_submit(self, form_name: str, msg: str) -> None:
        """Adds a confirm dialog to a form that is shown before executing a form submission"""
        self.javascript("cmk.forms.add_confirm_on_submit(%s, %s)" %
                        (json.dumps("form_%s" % form_name), json.dumps(escaping.escape_text(msg))))

    def in_form(self) -> bool:
        return self.form_name is not None

    def prevent_password_auto_completion(self) -> None:
>>>>>>> upstream/master
        # These fields are not really used by the form. They are used to prevent the browsers
        # from filling the default password and previous input fields in the form
        # with password which are eventually saved in the browsers password store.
        self.input(name=None, type_="text", style="display:none;")
        self.input(name=None, type_="password", style="display:none;")

    # Needed if input elements are put into forms without the helper
    # functions of us. TODO: Should really be removed and cleaned up!
<<<<<<< HEAD
    def add_form_var(self, varname):
=======
    def add_form_var(self, varname: str) -> None:
>>>>>>> upstream/master
        self.form_vars.append(varname)

    # Beware: call this method just before end_form(). It will
    # add all current non-underscored HTML variables as hiddedn
    # field to the form - *if* they are not used in any input
    # field. (this is the reason why you must not add any further
    # input fields after this method has been called).
<<<<<<< HEAD
    def hidden_fields(self, varlist=None, **args):
        add_action_vars = args.get("add_action_vars", False)
=======
    def hidden_fields(self,
                      varlist: Optional[List[str]] = None,
                      add_action_vars: bool = False) -> None:
>>>>>>> upstream/master
        if varlist is not None:
            for var in varlist:
                self.hidden_field(var, self.request.var(var, ""))
        else:  # add *all* get variables, that are not set by any input!
            for var, _val in self.request.itervars():
                if var not in self.form_vars and \
<<<<<<< HEAD
                    (var[0] != "_" or add_action_vars): # and var != "filled_in":
                    self.hidden_field(var, self.get_unicode_input(var))

    def hidden_field(self, var, value, id_=None, add_var=False, class_=None):
        self.write_html(
            self.render_hidden_field(var=var, value=value, id_=id_, add_var=add_var, class_=class_))

    def render_hidden_field(self, var, value, id_=None, add_var=False, class_=None):
        if value is None:
            return ""
=======
                    (var[0] != "_" or add_action_vars):  # and var != "filled_in":
                    self.hidden_field(var, self.request.get_unicode_input(var))

    def hidden_field(self,
                     var: str,
                     value: HTMLTagValue,
                     id_: Optional[str] = None,
                     add_var: bool = False,
                     class_: CSSSpec = None) -> None:
        self.write_html(
            self.render_hidden_field(var=var, value=value, id_=id_, add_var=add_var, class_=class_))

    def render_hidden_field(self,
                            var: str,
                            value: HTMLTagValue,
                            id_: Optional[str] = None,
                            add_var: bool = False,
                            class_: CSSSpec = None) -> HTML:
        if value is None:
            return HTML("")
>>>>>>> upstream/master
        if add_var:
            self.add_form_var(var)
        return self.render_input(
            name=var,
            type_="hidden",
            id_=id_,
            value=value,
            class_=class_,
            autocomplete="off",
        )

    #
    # Form submission and variable handling
    #

<<<<<<< HEAD
    def do_actions(self):
=======
    def do_actions(self) -> bool:
>>>>>>> upstream/master
        return self.request.var("_do_actions") not in ["", None, _("No")]

    # Check if the given form is currently filled in (i.e. we display
    # the form a second time while showing value typed in at the first
    # time and complaining about invalid user input)
<<<<<<< HEAD
    def form_submitted(self, form_name=None):
=======
    def form_submitted(self, form_name: Optional[str] = None) -> bool:
>>>>>>> upstream/master
        if form_name is None:
            return self.request.has_var("filled_in")
        return self.request.var("filled_in") == form_name

    # Get value of checkbox. Return True, False or None. None means
    # that no form has been submitted. The problem here is the distintion
    # between False and None. The browser does not set the variables for
    # Checkboxes that are not checked :-(
<<<<<<< HEAD
    def get_checkbox(self, varname):
=======
    def get_checkbox(self, varname: str) -> Optional[bool]:
>>>>>>> upstream/master
        if self.request.has_var(varname):
            return bool(self.request.var(varname))
        if self.form_submitted(self.form_name):
            return False  # Form filled in but variable missing -> Checkbox not checked
        return None

    #
    # Button elements
    #

<<<<<<< HEAD
    def button(self, varname, title, cssclass=None, style=None, help_=None):
        self.write_html(self.render_button(varname, title, cssclass, style, help_=help_))

    def render_button(self, varname, title, cssclass=None, style=None, help_=None):
=======
    def button(self,
               varname: str,
               title: str,
               cssclass: Optional[str] = None,
               style: Optional[str] = None,
               help_: Optional[str] = None,
               form: Optional[str] = None) -> None:
        self.write_html(self.render_button(varname, title, cssclass, style, help_=help_, form=form))

    def render_button(self,
                      varname: str,
                      title: str,
                      cssclass: Optional[str] = None,
                      style: Optional[str] = None,
                      help_: Optional[str] = None,
                      form: Optional[str] = None) -> HTML:
>>>>>>> upstream/master
        self.add_form_var(varname)
        return self.render_input(name=varname,
                                 type_="submit",
                                 id_=varname,
                                 class_=["button", cssclass if cssclass else None],
                                 value=title,
                                 title=help_,
<<<<<<< HEAD
                                 style=style)

    def buttonlink(self,
                   href,
                   text,
                   add_transid=False,
                   obj_id=None,
                   style=None,
                   title=None,
                   disabled=None,
                   class_=None):
=======
                                 style=style,
                                 form=form)

    def buttonlink(self,
                   href: str,
                   text: str,
                   add_transid: bool = False,
                   obj_id: Optional[str] = None,
                   style: Optional[str] = None,
                   title: Optional[str] = None,
                   disabled: Optional[str] = None,
                   class_: CSSSpec = None) -> None:
>>>>>>> upstream/master
        if add_transid:
            href += "&_transid=%s" % self.transaction_manager.get()

        if not obj_id:
            obj_id = utils.gen_id()

        # Same API as other elements: class_ can be a list or string/None
<<<<<<< HEAD
        css_classes = ["button", "buttonlink"]
=======
        css_classes: List[Optional[str]] = ["button", "buttonlink"]
>>>>>>> upstream/master
        if class_:
            if not isinstance(class_, list):
                css_classes.append(class_)
            else:
                css_classes.extend(class_)

        self.input(name=obj_id,
                   type_="button",
                   id_=obj_id,
                   class_=css_classes,
                   value=text,
                   style=style,
                   title=title,
                   disabled=disabled,
                   onclick="location.href=\'%s\'" % href)

<<<<<<< HEAD
    # TODO: Refactor the arguments. It is only used in views/wato
    def toggle_button(self,
                      id_,
                      isopen,
                      icon,
                      title,
                      hidden=False,
                      disabled=False,
                      onclick=None,
                      is_context_button=True):
        if is_context_button:
            self.begin_context_buttons()  # TODO: Check all calls. If done before, remove this!

        if not onclick and not disabled:
            onclick = "cmk.views.toggle_form(this.parentNode, '%s');" % id_

        if disabled:
            state = "off" if disabled else "on"
            cssclass = ""
            title = ""
        else:
            state = "on"
            if isopen:
                cssclass = "down"
            else:
                cssclass = "up"

        self.open_div(
            id_="%s_%s" % (id_, state),
            class_=["togglebutton", state, icon, cssclass],
            title=title,
            style='display:none' if hidden else None,
        )
        self.open_a("javascript:void(0)", onclick=onclick)
        self.icon(title=None, icon=icon)
        self.close_a()
        self.close_div()

    def get_button_counts(self):
        return config.user.get_button_counts()

    def empty_icon_button(self):
        self.write(self.render_icon("trans", cssclass="iconbutton trans"))

    def disabled_icon_button(self, icon):
=======
    def empty_icon_button(self) -> None:
        self.write(self.render_icon("trans", cssclass="iconbutton trans"))

    def disabled_icon_button(self, icon: str) -> None:
>>>>>>> upstream/master
        self.write(self.render_icon(icon, cssclass="iconbutton"))

    # TODO: Cleanup to use standard attributes etc.
    def jsbutton(self,
<<<<<<< HEAD
                 varname,
                 text,
                 onclick,
                 style='',
                 cssclass="",
                 title="",
                 disabled=False,
                 class_=None):
        # Same API as other elements: class_ can be a list or string/None
        classes = []
        if class_:
            classes = class_ if isinstance(class_, list) else [class_]

        if disabled:
            classes.append("disabled")
            disabled = ""
        else:
            disabled = None
=======
                 varname: str,
                 text: str,
                 onclick: str,
                 style: str = '',
                 cssclass: Optional[str] = None,
                 title: str = "",
                 disabled: bool = False,
                 class_: CSSSpec = None) -> None:
        if not isinstance(class_, list):
            class_ = [class_]
        # TODO: Investigate why mypy complains about the latest argument
        classes = ["button", cssclass] + cast(List[Optional[str]], class_)

        if disabled:
            class_.append("disabled")
            disabled_arg: Optional[str] = ""
        else:
            disabled_arg = None
>>>>>>> upstream/master

        # autocomplete="off": Is needed for firefox not to set "disabled="disabled" during page reload
        # when it has been set on a page via javascript before. Needed for WATO activate changes page.
        self.input(name=varname,
                   type_="button",
                   id_=varname,
<<<<<<< HEAD
                   class_=["button", cssclass] + classes,
                   autocomplete="off",
                   onclick=onclick,
                   style=style,
                   disabled=disabled,
=======
                   class_=classes,
                   autocomplete="off",
                   onclick=onclick,
                   style=style,
                   disabled=disabled_arg,
>>>>>>> upstream/master
                   value=text,
                   title=title)

    #
    # Other input elements
    #

<<<<<<< HEAD
    def user_error(self, e):
=======
    def user_error(self, e: MKUserError) -> None:
>>>>>>> upstream/master
        assert isinstance(e, MKUserError), "ERROR: This exception is not a user error!"
        self.open_div(class_="error")
        self.write("%s" % e.message)
        self.close_div()
        self.add_user_error(e.varname, e)

    # user errors are used by input elements to show invalid input
<<<<<<< HEAD
    def add_user_error(self, varname, msg_or_exc):
        if isinstance(msg_or_exc, Exception):
            message = "%s" % msg_or_exc
        else:
            message = msg_or_exc

=======
    def add_user_error(self, varname: Optional[str], msg_or_exc: Union[str, Exception]) -> None:
        if isinstance(msg_or_exc, Exception):
            message: str = u"%s" % msg_or_exc
        else:
            message = ensure_str(msg_or_exc)

        # TODO: Find the multiple varname call sites and clean this up
>>>>>>> upstream/master
        if isinstance(varname, list):
            for v in varname:
                self.add_user_error(v, message)
        else:
            self.user_errors[varname] = message

<<<<<<< HEAD
    def has_user_errors(self):
        return len(self.user_errors) > 0

    def show_user_errors(self):
=======
    def has_user_errors(self) -> bool:
        return len(self.user_errors) > 0

    def show_user_errors(self) -> None:
>>>>>>> upstream/master
        if self.has_user_errors():
            self.open_div(class_="error")
            self.write('<br>'.join(self.user_errors.values()))
            self.close_div()

    def text_input(self,
<<<<<<< HEAD
                   varname,
                   default_value="",
                   cssclass="text",
                   label=None,
                   id_=None,
                   submit=None,
                   attrs=None,
                   **args):
        if attrs is None:
            attrs = {}

        # Model
        error = self.user_errors.get(varname)
        value = self.get_unicode_input(varname, default_value)
=======
                   varname: str,
                   default_value: str = u"",
                   cssclass: str = "text",
                   size: Union[None, str, int] = None,
                   label: Optional[str] = None,
                   id_: Optional[str] = None,
                   submit: Optional[str] = None,
                   try_max_width: bool = False,
                   read_only: bool = False,
                   autocomplete: Optional[str] = None,
                   style: Optional[str] = None,
                   omit_css_width: bool = False,
                   type_: Optional[str] = None,
                   onkeyup: Optional[str] = None,
                   onblur: Optional[str] = None,
                   placeholder: Optional[str] = None,
                   data_world: Optional[str] = None,
                   data_max_labels: Optional[int] = None) -> None:

        # Model
        error = self.user_errors.get(varname)
        value = self.request.get_unicode_input(varname, default_value)
>>>>>>> upstream/master
        if not value:
            value = ""
        if error:
            self.set_focus(varname)
        self.form_vars.append(varname)

        # View
<<<<<<< HEAD
        style, size = None, None
        if args.get("try_max_width"):
            style = "width: calc(100% - 10px); "
            if "size" in args:
                cols = int(args["size"])
            else:
                cols = 16
            style += "min-width: %d.8ex; " % cols

        elif "size" in args and args["size"]:
            if args["size"] == "max":
                style = "width: 100%;"
            else:
                size = "%d" % (args["size"] + 1)
                if not args.get('omit_css_width', False) and "width:" not in args.get(
                        "style", "") and not self.mobile:
                    style = "width: %d.8ex;" % args["size"]

        if args.get("style"):
            style = [style, args["style"]]

        if (submit or label) and not id_:
            id_ = "ti_%s" % varname

        onkeydown = None if not submit else HTML(
            'cmk.forms.textinput_enter_submit(event, \'%s\');' % (submit))

        attributes = {
            "class": cssclass,
            "id": id_,
            "style": style,
            "size": size,
            "autocomplete": args.get("autocomplete"),
            "readonly": "true" if args.get("read_only") else None,
            "value": value,
            "onkeydown": onkeydown,
        }

        for key, val in attrs.iteritems():
            if key not in attributes and key not in ["name", "type", "type_"]:
                attributes[key] = val
            elif key in attributes and attributes[key] is None:
                attributes[key] = val

=======
        # TODO: Move styling away from py code
        style_size: Optional[str] = None
        field_size: Optional[str] = None
        if try_max_width:
            style_size = "width: calc(100% - 10px); "
            if size is not None:
                assert isinstance(size, int)
                cols = size
            else:
                cols = 16
            style_size += "min-width: %d.8ex; " % cols

        elif size is not None:
            if size == "max":
                style_size = "width: 100%;"
            else:
                assert isinstance(size, int)
                field_size = "%d" % (size + 1)
                if not omit_css_width and (style is None or
                                           "width:" not in style) and not self.mobile:
                    style_size = "width: %d.8ex;" % size

        attributes: HTMLTagAttributes = {
            "class": cssclass,
            "id": ("ti_%s" % varname) if (submit or label) and not id_ else id_,
            "style": [style_size] + ([] if style is None else [style]),
            "size": field_size,
            "autocomplete": autocomplete,
            "readonly": "true" if read_only else None,
            "value": value,
            "onblur": onblur,
            "onkeyup": onkeyup,
            "onkeydown": ('cmk.forms.textinput_enter_submit(event, %s);' %
                          json.dumps(submit)) if submit else None,
            "placeholder": placeholder,
            "data-world": data_world,
            "data-max-labels": None if data_max_labels is None else str(data_max_labels),
        }

>>>>>>> upstream/master
        if error:
            self.open_x(class_="inputerror")

        if label:
<<<<<<< HEAD
            self.label(label, for_=id_)
        self.write_html(self.render_input(varname, type_=args.get("type_", "text"), **attributes))
=======
            assert id_ is not None
            self.label(label, for_=id_)

        input_type = "text" if type_ is None else type_
        assert isinstance(input_type, str)
        self.write_html(self.render_input(varname, type_=input_type, **attributes))
>>>>>>> upstream/master

        if error:
            self.close_x()

<<<<<<< HEAD
    # Shows a colored badge with text (used on WATO activation page for the site status)
    def status_label(self, content, status, title, **attrs):
        self.status_label_button(content, status, title, onclick=None, **attrs)

    # Shows a colored button with text (used in site and customer status snapins)
    def status_label_button(self, content, status, title, onclick, **attrs):
=======
    def status_label(self, content: HTMLContent, status: str, title: str,
                     **attrs: HTMLTagAttributeValue) -> None:
        """Shows a colored badge with text (used on WATO activation page for the site status)"""
        self.status_label_button(content, status, title, onclick=None, **attrs)

    def status_label_button(self, content: HTMLContent, status: str, title: str,
                            onclick: Optional[str], **attrs: HTMLTagAttributeValue) -> None:
        """Shows a colored button with text (used in site and customer status snapins)"""
>>>>>>> upstream/master
        button_cls = "button" if onclick else None
        self.div(content,
                 title=title,
                 class_=["status_label", button_cls, status],
                 onclick=onclick,
                 **attrs)

<<<<<<< HEAD
    def toggle_switch(self, enabled, help_txt, **attrs):
        # Same API as other elements: class_ can be a list or string/None
        if "class_" in attrs:
            if not isinstance(attrs["class_"], list):
                attrs["class_"] = [attrs["class_"]]
        else:
            attrs["class_"] = []

        attrs["class_"] += [
            "toggle_switch",
            "on" if enabled else "off",
        ]

        link_attrs = {
            "href": attrs.pop("href", "javascript:void(0)"),
            "onclick": attrs.pop("onclick", None),
        }

        self.open_div(**attrs)
        self.a(_("on") if enabled else _("off"), title=help_txt, **link_attrs)
        self.close_div()

    def number_input(self, varname, deflt="", size=8, style="", submit=None):
        if deflt is not None:
            deflt = str(deflt)
        self.text_input(varname, deflt, "number", size=size, style=style, submit=submit)

    def password_input(self, varname, default_value="", size=12, **args):
        self.text_input(varname, default_value, type_="password", size=size, **args)

    def text_area(self, varname, deflt="", rows=4, cols=30, attrs=None, try_max_width=False):
        if attrs is None:
            attrs = {}

        # Model
        value = self.get_unicode_input(varname, deflt)
=======
    def toggle_switch(self,
                      enabled: bool,
                      help_txt: str,
                      class_: CSSSpec = None,
                      href: str = "javascript:void(0)",
                      **attrs: HTMLTagAttributeValue) -> None:
        # Same API as other elements: class_ can be a list or string/None
        if not isinstance(class_, list):
            class_ = [class_]

        class_ += [
            "toggle_switch",
            "on" if enabled else "off",
        ]
        onclick = attrs.pop("onclick", None)

        self.open_div(class_=class_, **attrs)
        self.a(
            content=_("on") if enabled else _("off"),
            href=href,
            title=help_txt,
            onclick=onclick,
        )
        self.close_div()

    def password_input(self,
                       varname: str,
                       default_value: str = "",
                       cssclass: str = "text",
                       size: Union[None, str, int] = None,
                       label: Optional[str] = None,
                       id_: Optional[str] = None,
                       submit: Optional[str] = None,
                       try_max_width: bool = False,
                       read_only: bool = False,
                       autocomplete: Optional[str] = None) -> None:
        self.text_input(varname,
                        default_value,
                        cssclass=cssclass,
                        size=size,
                        label=label,
                        id_=id_,
                        submit=submit,
                        type_="password",
                        try_max_width=try_max_width,
                        read_only=read_only,
                        autocomplete=autocomplete)

    def text_area(self,
                  varname: str,
                  deflt: str = "",
                  rows: int = 4,
                  cols: int = 30,
                  try_max_width: bool = False,
                  **attrs: HTMLTagAttributeValue) -> None:

        value = self.request.get_unicode_input(varname, deflt)
>>>>>>> upstream/master
        error = self.user_errors.get(varname)

        self.form_vars.append(varname)
        if error:
            self.set_focus(varname)

<<<<<<< HEAD
        # View
=======
>>>>>>> upstream/master
        style = "width: %d.8ex;" % cols
        if try_max_width:
            style += "width: calc(100%% - 10px); min-width: %d.8ex;" % cols
        attrs["style"] = style
<<<<<<< HEAD
        attrs["rows"] = rows
        attrs["cols"] = cols
=======
        attrs["rows"] = str(rows)
        attrs["cols"] = str(cols)
>>>>>>> upstream/master
        attrs["name"] = varname

        # Fix handling of leading newlines (https://www.w3.org/TR/html5/syntax.html#element-restrictions)
        #
        # """
        # A single newline may be placed immediately after the start tag of pre
        # and textarea elements. This does not affect the processing of the
        # element. The otherwise optional newline must be included if the
        # element’s contents themselves start with a newline (because otherwise
        # the leading newline in the contents would be treated like the
        # optional newline, and ignored).
        # """
        if value and value.startswith("\n"):
            value = "\n" + value

        if error:
            self.open_x(class_="inputerror")
<<<<<<< HEAD
        self.write_html(self._render_content_tag("textarea", value, **attrs))
        if error:
            self.close_x()

    # TODO: DEPRECATED!!
    def sorted_select(self, varname, choices, deflt='', onchange=None, attrs=None):
        if attrs is None:
            attrs = {}
        self.dropdown(varname, choices, deflt=deflt, onchange=onchange, ordered=True, **attrs)

    # TODO: DEPRECATED!!
    def select(self, varname, choices, deflt='', onchange=None, attrs=None):
        if attrs is None:
            attrs = {}
        self.dropdown(varname, choices, deflt=deflt, onchange=onchange, **attrs)

    # TODO: DEPRECATED!!
    def icon_select(self, varname, choices, deflt=''):
        self.icon_dropdown(varname, choices, deflt=deflt)

    # Choices is a list pairs of (key, title). They keys of the choices
    # and the default value must be of type None, str or unicode.
    def dropdown(self, varname, choices, deflt='', ordered=False, **attrs):

        current = self.get_unicode_input(varname, deflt)
        error = self.user_errors.get(varname)
        if varname:
            self.form_vars.append(varname)
        attrs.setdefault('size', 1)

        chs = choices[:]
        if ordered:
            # Sort according to display texts, not keys
            chs.sort(key=lambda a: a[1].lower())
=======
        self.write_html(self._render_element("textarea", value, **attrs))
        if error:
            self.close_x()

    # Choices is a list pairs of (key, title). They keys of the choices
    # and the default value must be of type None, str or unicode.
    def dropdown(self,
                 varname: str,
                 choices: Union[Choices, GroupedChoices],
                 deflt: DefaultChoice = '',
                 ordered: bool = False,
                 label: Optional[str] = None,
                 class_: CSSSpec = None,
                 size: int = 1,
                 read_only: bool = False,
                 **attrs: HTMLTagAttributeValue) -> None:
        current = self.request.get_unicode_input(varname, deflt)
        error = self.user_errors.get(varname)
        if varname:
            self.form_vars.append(varname)

        # Normalize all choices to grouped choice structure
        grouped: GroupedChoices = []
        ungrouped_group = ChoiceGroup(title="", choices=[])
        grouped.append(ungrouped_group)
        for e in choices:
            if not isinstance(e, ChoiceGroup):
                ungrouped_group.choices.append(e)
            else:
                grouped.append(e)
>>>>>>> upstream/master

        if error:
            self.open_x(class_="inputerror")

<<<<<<< HEAD
        if "read_only" in attrs and attrs.pop("read_only"):
            attrs["disabled"] = "disabled"
            self.hidden_field(varname, current, add_var=False)

        if attrs.get("label"):
            self.label(attrs["label"], for_=varname)
=======
        if read_only:
            attrs["disabled"] = "disabled"
            self.hidden_field(varname, current, add_var=False)

        if label:
            self.label(label, for_=varname)
>>>>>>> upstream/master

        # Do not enable select2 for select fields that allow multiple
        # selections like the dual list choice valuespec
        if "multiple" not in attrs:
<<<<<<< HEAD
            if "class_" in attrs:
                if isinstance(attrs["class_"], list):
                    attrs["class_"].insert(0, "select2-enable")
                else:
                    attrs["class_"] = ["select2-enable", attrs["class_"]]
            else:
                attrs["class_"] = ["select2-enable"]

        self.open_select(name=varname, id_=varname, **attrs)
        for value, text in chs:
            # if both the default in choices and current was '' then selected depended on the order in choices
            selected = (value == current) or (not value and not current)
            self.option(text, value=value if value else "", selected="" if selected else None)
=======
            css_classes: List[Optional[str]] = ["select2-enable"]
        else:
            css_classes = []

        if isinstance(class_, list):
            css_classes.extend(class_)
        else:
            css_classes.append(class_)

        self.open_select(name=varname,
                         id_=varname,
                         label=label,
                         class_=css_classes,
                         size=str(size),
                         **attrs)

        for group in grouped:
            if group.title:
                self.open_optgroup(label=group.title)

            for value, text in (group.choices if not ordered else sorted(
                    group.choices, key=lambda a: a[1].lower())):
                # if both the default in choices and current was '' then selected depended on the order in choices
                selected = (value == current) or (not value and not current)
                self.option(text, value=value if value else "", selected="" if selected else None)

            if group.title:
                self.close_optgroup()

>>>>>>> upstream/master
        self.close_select()
        if error:
            self.close_x()

<<<<<<< HEAD
    def icon_dropdown(self, varname, choices, deflt=""):
=======
    def icon_dropdown(self,
                      varname: str,
                      choices: List[Tuple[str, str, str]],
                      deflt: str = "") -> None:
>>>>>>> upstream/master
        current = self.request.var(varname, deflt)
        if varname:
            self.form_vars.append(varname)

        self.open_select(class_="icon", name=varname, id_=varname, size="1")
        for value, text, icon in choices:
            # if both the default in choices and current was '' then selected depended on the order in choices
            selected = (value == current) or (not value and not current)
            self.option(text,
                        value=value if value else "",
                        selected='' if selected else None,
                        style="background-image:url(themes/%s/images/icon_%s.png);" %
                        (self._theme, icon))
        self.close_select()

<<<<<<< HEAD
    # Wrapper for DualListChoice
    def multi_select(self, varname, choices, deflt='', ordered='', **attrs):
        attrs["multiple"] = "multiple"
        self.dropdown(varname, choices, deflt=deflt, ordered=ordered, **attrs)

    def upload_file(self, varname):
=======
    def upload_file(self, varname: str) -> None:
>>>>>>> upstream/master
        error = self.user_errors.get(varname)
        if error:
            self.open_x(class_="inputerror")
        self.input(name=varname, type_="file")
        if error:
            self.close_x()
        self.form_vars.append(varname)

<<<<<<< HEAD
    # The confirm dialog is normally not a dialog which need to be protected
    # by a transid itselfs. It is only a intermediate step to the real action
    # But there are use cases where the confirm dialog is used during rendering
    # a normal page, for example when deleting a dashlet from a dashboard. In
    # such cases, the transid must be added by the confirm dialog.
    # add_header: A title can be given to make the confirm method render the HTML
    #             header when showing the confirm message.
    def confirm(self, msg, method="POST", action=None, add_transid=False, add_header=False):
        if self.request.var("_do_actions") == _("No"):
            # User has pressed "No", now invalidate the unused transid
            self.check_transaction()
            return  # None --> "No"

        if not self.request.has_var("_do_confirm"):
            if add_header != False:
                self.header(add_header)

            if self.mobile:
                self.open_center()
            self.open_div(class_="really")
            self.write_text(msg)
            # FIXME: When this confirms another form, use the form name from self.request.itervars()
            self.begin_form("confirm", method=method, action=action, add_transid=add_transid)
            self.hidden_fields(add_action_vars=True)
            self.button("_do_confirm", _("Yes!"), "really")
            self.button("_do_actions", _("No"), "")
            self.end_form()
            self.close_div()
            if self.mobile:
                self.close_center()

            return False  # False --> "Dialog shown, no answer yet"
        else:
            # Now check the transaction
            return True if self.check_transaction(
            ) else None  # True: "Yes", None --> Browser reload of "yes" page

=======
>>>>>>> upstream/master
    #
    # Radio groups
    #

<<<<<<< HEAD
    def begin_radio_group(self, horizontal=False):
        if self.mobile:
            attrs = {'data-type': "horizontal" if horizontal else None, 'data-role': "controlgroup"}
            self.write(self._render_opening_tag("fieldset", **attrs))

    def end_radio_group(self):
        if self.mobile:
            self.write(self._render_closing_tag("fieldset"))

    def radiobutton(self, varname, value, checked, label):
        # Model
        self.form_vars.append(varname)

        # Controller
        if self.request.has_var(varname):
            checked = self.request.var(varname) == value

        # View
=======
    def begin_radio_group(self, horizontal: bool = False) -> None:
        if self.mobile:
            attrs = {'data-type': "horizontal" if horizontal else None, 'data-role': "controlgroup"}
            self.write(self._render_start_tag("fieldset", close_tag=False, **attrs))

    def end_radio_group(self) -> None:
        if self.mobile:
            self.write(self._render_end_tag("fieldset"))

    def radiobutton(self, varname: str, value: str, checked: bool, label: Optional[str]) -> None:
        self.form_vars.append(varname)

        if self.request.has_var(varname):
            checked = self.request.var(varname) == value

>>>>>>> upstream/master
        id_ = "rb_%s_%s" % (varname, value) if label else None
        self.open_span(class_="radiobutton_group")
        self.input(name=varname,
                   type_="radio",
                   value=value,
                   checked='' if checked else None,
                   id_=id_)
<<<<<<< HEAD
        if label:
=======
        if label and id_:
>>>>>>> upstream/master
            self.label(label, for_=id_)
        self.close_span()

    #
    # Checkbox groups
    #

<<<<<<< HEAD
    def begin_checkbox_group(self, horizonal=False):
        self.begin_radio_group(horizonal)

    def end_checkbox_group(self):
        self.end_radio_group()

    def checkbox(self, *args, **kwargs):
        self.write(self.render_checkbox(*args, **kwargs))

    def render_checkbox(self, varname, deflt=False, label='', id_=None, **add_attr):

=======
    def begin_checkbox_group(self, horizonal: bool = False) -> None:
        self.begin_radio_group(horizonal)

    def end_checkbox_group(self) -> None:
        self.end_radio_group()

    def checkbox(self,
                 varname: str,
                 deflt: bool = False,
                 label: HTMLContent = '',
                 id_: Optional[str] = None,
                 **add_attr: HTMLTagAttributeValue) -> None:
        self.write(self.render_checkbox(varname, deflt, label, id_, **add_attr))

    def render_checkbox(self,
                        varname: str,
                        deflt: bool = False,
                        label: HTMLContent = '',
                        id_: Optional[str] = None,
                        **add_attr: HTMLTagAttributeValue) -> HTML:
>>>>>>> upstream/master
        # Problem with checkboxes: The browser will add the variable
        # only to the URL if the box is checked. So in order to detect
        # whether we should add the default value, we need to detect
        # if the form is printed for the first time. This is the
        # case if "filled_in" is not set.
        value = self.get_checkbox(varname)
        if value is None:  # form not yet filled in
            value = deflt

        error = self.user_errors.get(varname)
        if id_ is None:
            id_ = "cb_%s" % varname

        add_attr["id"] = id_
        add_attr["CHECKED"] = '' if value else None

        code = self.render_input(name=varname, type_="checkbox", **add_attr) + self.render_label(
            label, for_=id_)
        code = self.render_span(code, class_="checkbox")

        if error:
            code = self.render_x(code, class_="inputerror")

        self.form_vars.append(varname)
        return code

    #
    # Foldable context
    #

    def begin_foldable_container(self,
<<<<<<< HEAD
                                 treename,
                                 id_,
                                 isopen,
                                 title,
                                 indent=True,
                                 first=False,
                                 icon=None,
                                 fetch_url=None,
                                 title_url=None,
                                 title_target=None,
                                 tree_img="tree"):
        self.folding_indent = indent

        if self._user_id:
            isopen = self.foldable_container_is_open(treename, id_, isopen)

        onclick = "cmk.foldable_container.toggle(%s, %s, %s)"\
                    % (json.dumps(treename), json.dumps(id_), json.dumps(fetch_url if fetch_url else ''))

        img_id = "treeimg.%s.%s" % (treename, id_)
        container_id = "tree.%s.%s" % (treename, id_)

        if indent == "nform":
            self.open_thead()
            self.open_tr(class_="heading")
            self.open_td(id_="nform.%s.%s" % (treename, id_), onclick=onclick, colspan="2")
            if icon:
                self.img(id_=img_id,
                         class_=["treeangle", "title"],
                         src="themes/%s/images/icon_%s.png" % (self._theme, icon))
            else:
                self.img(id_=img_id,
                         class_=["treeangle", "nform", "open" if isopen else "closed"],
                         src="themes/%s/images/%s_closed.png" % (self._theme, tree_img),
                         align="absbottom")
            self.write_text(title)
            self.close_td()
            self.close_tr()
            self.close_thead()
            self.open_tbody(id_=container_id, class_=["open" if isopen else "closed"])
        else:
            self.open_div(class_="foldable")

            if not icon:
                self.img(id_=img_id,
                         class_=["treeangle", "open" if isopen else "closed"],
                         src="themes/%s/images/%s_closed.png" % (self._theme, tree_img),
                         align="absbottom",
                         onclick=onclick)
            if isinstance(title, HTML):  # custom HTML code
                if icon:
                    self.img(class_=["treeangle", "title"],
                             src="themes/%s/images/icon_%s.png" % (self._theme, icon),
                             onclick=onclick)
                self.write_text(title)
                if indent != "form":
                    self.br()
            else:
                self.open_b(class_=["treeangle", "title"], onclick=None if title_url else onclick)
                if icon:
                    self.img(class_=["treeangle", "title"],
                             src="themes/%s/images/icon_%s.png" % (self._theme, icon))
                if title_url:
                    self.a(title, href=title_url, target=title_target)
                else:
                    self.write_text(title)
                self.close_b()
                self.br()

            indent_style = "padding-left: %dpx; " % (indent is True and 15 or 0)
            if indent == "form":
                self.close_td()
                self.close_tr()
                self.close_table()
                indent_style += "margin: 0; "
            self.open_ul(id_=container_id,
                         class_=["treeangle", "open" if isopen else "closed"],
                         style=indent_style)

        # give caller information about current toggling state (needed for nform)
        return isopen

    def end_foldable_container(self):
        if self.folding_indent != "nform":
            self.close_ul()
            self.close_div()

    def foldable_container_is_open(self, treename, id_, isopen):
        # try to get persisted state of tree
        tree_state = self.get_tree_states(treename)
=======
                                 treename: str,
                                 id_: str,
                                 isopen: bool,
                                 title: HTMLContent,
                                 indent: Union[str, None, bool] = True,
                                 first: bool = False,
                                 icon: Optional[str] = None,
                                 fetch_url: Optional[str] = None,
                                 title_url: Optional[str] = None,
                                 title_target: Optional[str] = None) -> bool:
        isopen = self.foldable_container_is_open(treename, id_, isopen)
        onclick = self.foldable_container_onclick(treename, id_, fetch_url)
        img_id = self.foldable_container_img_id(treename, id_)
        container_id = self.foldable_container_id(treename, id_)

        self.open_div(class_=["foldable", "open" if isopen else "closed"])

        if not icon:
            self.img(id_=img_id,
                     class_=["treeangle", "open" if isopen else "closed"],
                     src="themes/%s/images/tree_closed.png" % (self._theme),
                     align="absbottom",
                     onclick=onclick)
        if isinstance(title, HTML):  # custom HTML code
            if icon:
                self.img(class_=["treeangle", "title"],
                         src="themes/%s/images/icon_%s.png" % (self._theme, icon),
                         onclick=onclick)
            self.write_text(title)
            if indent != "form":
                self.br()
        else:
            self.open_b(class_=["treeangle", "title"], onclick=None if title_url else onclick)
            if icon:
                self.img(class_=["treeangle", "title"],
                         src="themes/%s/images/icon_%s.png" % (self._theme, icon))
            if title_url:
                self.a(title, href=title_url, target=title_target)
            else:
                self.write_text(title)
            self.close_b()
            self.br()

        indent_style = "padding-left: %dpx; " % (indent is True and 15 or 0)
        if indent == "form":
            self.close_td()
            self.close_tr()
            self.close_table()
            indent_style += "margin: 0; "
        self.open_ul(id_=container_id,
                     class_=["treeangle", "open" if isopen else "closed"],
                     style=indent_style)

        return isopen

    def end_foldable_container(self) -> None:
        self.close_ul()
        self.close_div()

    def foldable_container_is_open(self, treename: str, id_: str, isopen: bool) -> bool:
        # try to get persisted state of tree
        tree_state = config.user.get_tree_states(treename)
>>>>>>> upstream/master

        if id_ in tree_state:
            isopen = tree_state[id_] == "on"
        return isopen

<<<<<<< HEAD
    #
    # Context Buttons
    #

    def begin_context_buttons(self):
        if not self._context_buttons_open:
            self.context_button_hidden = False
            self.open_div(class_="contextlinks")
            self._context_buttons_open = True

    def end_context_buttons(self):
        if self._context_buttons_open:
            if self.context_button_hidden:
                self.open_div(title=_("Show all buttons"),
                              id="toggle",
                              class_=["contextlink", "short"])
                self.a("...", onclick='cmk.utils.unhide_context_buttons(this);', href='#')
                self.close_div()
            self.div("", class_="end")
            self.close_div()
        self._context_buttons_open = False

    def context_button(self,
                       title,
                       url,
                       icon=None,
                       hot=False,
                       id_=None,
                       bestof=None,
                       hover_title=None,
                       class_=None):
        self._context_button(title,
                             url,
                             icon=icon,
                             hot=hot,
                             id_=id_,
                             bestof=bestof,
                             hover_title=hover_title,
                             class_=class_)

    def _context_button(self,
                        title,
                        url,
                        icon=None,
                        hot=False,
                        id_=None,
                        bestof=None,
                        hover_title=None,
                        class_=None):
        title = self.attrencode(title)
        display = "block"
        if bestof:
            counts = self.get_button_counts()
            weights = counts.items()
            weights.sort(key=lambda x: x[1])
            best = dict(weights[-bestof:])  # pylint: disable=invalid-unary-operand-type
            if id_ not in best:
                display = "none"
                self.context_button_hidden = True

        if not self._context_buttons_open:
            self.begin_context_buttons()

        css_classes = ["contextlink"]
        if hot:
            css_classes.append("hot")
        if class_:
            if isinstance(class_, list):
                css_classes += class_
            else:
                css_classes += class_.split(" ")

        self.open_div(class_=css_classes, id_=id_, style="display:%s;" % display)

        self.open_a(href=url,
                    title=hover_title,
                    onclick="cmk.utils.count_context_button(this);" if bestof else None)

        if icon:
            self.icon('', icon, cssclass="inline", middle=False)

        self.span(title)

        self.close_a()

        self.close_div()
=======
    def foldable_container_onclick(self, treename: str, id_: str, fetch_url: Optional[str]) -> str:
        return "cmk.foldable_container.toggle(%s, %s, %s)" % (
            json.dumps(treename), json.dumps(id_), json.dumps(fetch_url if fetch_url else ''))

    def foldable_container_img_id(self, treename: str, id_: str) -> str:
        return "treeimg.%s.%s" % (treename, id_)

    def foldable_container_id(self, treename: str, id_: str) -> str:
        return "tree.%s.%s" % (treename, id_)
>>>>>>> upstream/master

    #
    # Floating Options
    #

<<<<<<< HEAD
    def begin_floating_options(self, div_id, is_open):
        self.open_div(id_=div_id,
                      class_=["view_form"],
                      style="display: none" if not is_open else None)
        self.open_table(class_=["filterform"], cellpadding="0", cellspacing="0", border="0")
        self.open_tr()
        self.open_td()

    def end_floating_options(self, reset_url=None):
        self.close_td()
        self.close_tr()
        self.open_tr()
        self.open_td()
        self.button("apply", _("Apply"), "submit")
        if reset_url:
            self.buttonlink(reset_url, _("Reset to defaults"))

        self.close_td()
        self.close_tr()
        self.close_table()
        self.close_div()

    def render_floating_option(self, name, height, varprefix, valuespec, value):
=======
    def render_floating_option(self, name: str, height: str, varprefix: str, valuespec: 'ValueSpec',
                               value: Any) -> None:
>>>>>>> upstream/master
        self.open_div(class_=["floatfilter", height, name])
        self.div(valuespec.title(), class_=["legend"])
        self.open_div(class_=["content"])
        valuespec.render_input(varprefix + name, value)
        self.close_div()
        self.close_div()

    #
    # HTML icon rendering
    #

<<<<<<< HEAD
    # FIXME: Change order of input arguments in one: icon and render_icon!!
    def icon(self, title, icon, **kwargs):

        icon_name = icon

        self.write_html(self.render_icon(icon_name=icon_name, title=title, **kwargs))

    def empty_icon(self):
        self.write_html(self.render_icon("trans"))

    def render_icon(self, icon_name, title=None, middle=True, id_=None, cssclass=None, class_=None):

        attributes = {
            'title': title,
            'id': id_,
            'class': ["icon", cssclass],
            'align': 'absmiddle' if middle else None,
            'src': icon_name if "/" in icon_name else self._detect_icon_path(icon_name)
        }

        if class_:
            attributes['class'].extend(class_)

        return self._render_opening_tag('img', close_tag=True, **attributes)

    def _detect_icon_path(self, icon_name):
        """Detect from which place an icon shall be used and return it's path relative to
 htdocs/

        Priority:
        1. In case a theme is active: themes/images/icon_[name].png in site local hierarchy
        2. In case a theme is active: themes/images/icon_[name].png in standard hierarchy
        3. images/icons/[name].png in site local hierarchy
        4. images/icons/[name].png in standard hierarchy
        """

        rel_path = "share/check_mk/web/htdocs/themes/%s/images/icon_%s.png" % (self._theme,
                                                                               icon_name)
        if os.path.exists(cmk.utils.paths.omd_root + "/" +
                          rel_path) or os.path.exists(cmk.utils.paths.omd_root + "/local/" +
                                                      rel_path):
            return "themes/%s/images/icon_%s.png" % (self._theme, icon_name)
=======
    def icon(self,
             icon: Icon,
             title: Optional[str] = None,
             middle: bool = True,
             id_: Optional[str] = None,
             cssclass: Optional[str] = None,
             class_: CSSSpec = None) -> None:
        self.write_html(
            self.render_icon(icon=icon,
                             title=title,
                             middle=middle,
                             id_=id_,
                             cssclass=cssclass,
                             class_=class_))

    def empty_icon(self) -> None:
        self.write_html(self.render_icon("trans"))

    def render_icon(self,
                    icon: Icon,
                    title: Optional[str] = None,
                    middle: bool = True,
                    id_: Optional[str] = None,
                    cssclass: Optional[str] = None,
                    class_: CSSSpec = None) -> HTML:
        classes = ["icon", cssclass]
        if isinstance(class_, list):
            classes.extend(class_)
        else:
            classes.append(class_)

        icon_name = icon["icon"] if isinstance(icon, dict) else icon
        icon_element = self._render_start_tag(
            'img',
            close_tag=True,
            title=title,
            id_=id_,
            class_=classes,
            align='absmiddle' if middle else None,
            src=icon_name if "/" in icon_name else self.detect_icon_path(icon_name, prefix="icon"),
        )

        if isinstance(icon, dict) and icon["emblem"] is not None:
            emblem_path = self.detect_icon_path(icon["emblem"], prefix="emblem")
            return self.render_span(icon_element + self.render_img(emblem_path, class_="emblem"),
                                    class_="emblem")
        return icon_element

    def detect_icon_path(self, icon_name: str, prefix: str) -> str:
        """Detect from which place an icon shall be used and return it's path relative to htdocs/

        Priority:
        1. In case the modern-dark theme is active: <theme> = modern-dark -> priorities 3-6
        2. In case the modern-dark theme is active: <theme> = facelift -> priorities 3-6
        3. In case a theme is active: themes/<theme>/images/icon_[name].svg in site local hierarchy
        4. In case a theme is active: themes/<theme>/images/icon_[name].svg in standard hierarchy
        5. In case a theme is active: themes/<theme>/images/icon_[name].png in site local hierarchy
        6. In case a theme is active: themes/<theme>/images/icon_[name].png in standard hierarchy
        7. images/icons/[name].png in site local hierarchy
        8. images/icons/[name].png in standard hierarchy
        """
        for theme in self.icon_themes():
            path = "share/check_mk/web/htdocs/themes/%s/images/%s_%s" % (theme, prefix, icon_name)
            for file_type in ["svg", "png"]:
                for base_dir in [cmk.utils.paths.omd_root, cmk.utils.paths.omd_root + "/local"]:
                    if os.path.exists(base_dir + "/" + path + "." + file_type):
                        return "themes/%s/images/%s_%s.%s" % (self._theme, prefix, icon_name,
                                                              file_type)
>>>>>>> upstream/master

        # TODO: This fallback is odd. Find use cases and clean this up
        return "images/icons/%s.png" % icon_name

    def render_icon_button(self,
<<<<<<< HEAD
                           url,
                           title,
                           icon,
                           id_=None,
                           onclick=None,
                           style=None,
                           target=None,
                           cssclass=None,
                           class_=None):
        # Same API as other elements: class_ can be a list or string/None
        classes = []
        if cssclass:
            classes.append(cssclass)
        if class_:
            classes = class_ if isinstance(class_, list) else [class_]

        icon = HTML(self.render_icon(icon, cssclass="iconbutton"))

        return self.render_a(
            icon, **{
                'title': title,
                'id': id_,
                'class': classes,
                'style': style,
                'target': target if target else '',
                'href': url if not onclick else "javascript:void(0)",
                'onfocus': "if (this.blur) this.blur();",
                'onclick': onclick
            })

    def icon_button(self, *args, **kwargs):
        self.write_html(self.render_icon_button(*args, **kwargs))

    def popup_trigger(self, *args, **kwargs):
        self.write_html(self.render_popup_trigger(*args, **kwargs))

    def render_popup_trigger(self,
                             content,
                             ident,
                             what=None,
                             data=None,
                             url_vars=None,
                             style=None,
                             menu_content=None,
                             cssclass=None,
                             onclose=None,
                             resizable=False):

        onclick = 'cmk.popup_menu.toggle_popup(event, this, %s, %s, %s, %s, %s, %s, %s);' % \
                    (json.dumps(ident),
                     json.dumps(what if what else None),
                     json.dumps(data if data else None),
                     json.dumps(self.urlencode_vars(url_vars) if url_vars else None),
                     json.dumps(menu_content if menu_content else None),
                     json.dumps(onclose.replace("'", "\\'") if onclose else None),
                     json.dumps(resizable))

        #TODO: Check if HTML'ing content is correct and necessary!
        atag = self.render_a(HTML(content),
                             class_="popup_trigger",
                             href="javascript:void(0);",
                             onclick=onclick)

        return self.render_div(atag,
                               class_=["popup_trigger", cssclass],
                               id_="popup_trigger_%s" % ident,
                               style=style)

    def element_dragger_url(self, dragging_tag, base_url):
=======
                           url: Union[None, str, str],
                           title: str,
                           icon: Icon,
                           id_: Optional[str] = None,
                           onclick: Optional[HTMLTagAttributeValue] = None,
                           style: Optional[str] = None,
                           target: Optional[str] = None,
                           cssclass: Optional[str] = None,
                           class_: CSSSpec = None) -> HTML:
        # Same API as other elements: class_ can be a list or string/None
        classes = [cssclass]
        if isinstance(class_, list):
            classes.extend(class_)
        else:
            classes.append(class_)

        href = url if not onclick else "javascript:void(0)"
        assert href is not None

        return self.render_a(
            content=HTML(self.render_icon(icon, cssclass="iconbutton")),
            href=href,
            title=title,
            id_=id_,
            class_=classes,
            style=style,
            target=target if target else '',
            onfocus="if (this.blur) this.blur();",
            onclick=onclick,
        )

    def icon_button(self,
                    url: Optional[str],
                    title: str,
                    icon: Icon,
                    id_: Optional[str] = None,
                    onclick: Optional[HTMLTagAttributeValue] = None,
                    style: Optional[str] = None,
                    target: Optional[str] = None,
                    cssclass: Optional[str] = None,
                    class_: CSSSpec = None) -> None:
        self.write_html(
            self.render_icon_button(url, title, icon, id_, onclick, style, target, cssclass,
                                    class_))

    def more_button(self,
                    id_: str,
                    dom_levels_up: int,
                    additional_js: str = "",
                    with_text: bool = False) -> None:
        if config.user.get_attribute("show_mode") == "enforce_show_more":
            return

        self.open_a(href="javascript:void(0)",
                    id_="more_%s" % id_,
                    class_=["more", "has_text" if with_text else ""],
                    onfocus="if (this.blur) this.blur();",
                    onclick="cmk.utils.toggle_more(this, %s, %d);%s" %
                    (json.dumps(id_), dom_levels_up, additional_js))
        self.open_div(title="Show more items" if not with_text else "", class_="show_more")
        if with_text:
            self.span(_("show more"))
        self.close_div()
        self.open_div(title="Show less items" if not with_text else "", class_="show_less")
        if with_text:
            self.span(_("show less"))
        self.close_div()
        self.close_a()

    def popup_trigger(self,
                      content: HTML,
                      ident: str,
                      method: PopupMethod,
                      data: Any = None,
                      style: Optional[str] = None,
                      cssclass: CSSSpec = None,
                      onclose: Optional[str] = None,
                      onopen: Optional[str] = None,
                      resizable: bool = False,
                      popup_group: Optional[str] = None,
                      hover_switch_delay: Optional[int] = None) -> None:
        self.write_html(
            self.render_popup_trigger(content, ident, method, data, style, cssclass, onclose,
                                      onopen, resizable, popup_group, hover_switch_delay))

    def render_popup_trigger(self,
                             content: HTML,
                             ident: str,
                             method: PopupMethod,
                             data: Any = None,
                             style: Optional[str] = None,
                             cssclass: CSSSpec = None,
                             onclose: Optional[str] = None,
                             onopen: Optional[str] = None,
                             resizable: bool = False,
                             popup_group: Optional[str] = None,
                             hover_switch_delay: Optional[int] = None) -> HTML:

        onclick = 'cmk.popup_menu.toggle_popup(event, this, %s, %s, %s, %s, %s,  %s);' % \
                    (json.dumps(ident),
                     json.dumps(method.asdict()),
                     json.dumps(data if data else None),
                     json.dumps(onclose.replace("'", "\\'") if onclose else None),
                     json.dumps(onopen.replace("'", "\\'") if onopen else None),
                     json.dumps(resizable))

        if popup_group:
            onmouseenter: Optional[str] = (
                "cmk.popup_menu.switch_popup_menu_group(this, %s, %s)" %
                (json.dumps(popup_group), json.dumps(hover_switch_delay)))
            onmouseleave: Optional[str] = "cmk.popup_menu.stop_popup_menu_group_switch(this)"
        else:
            onmouseenter = None
            onmouseleave = None

        atag = self.render_a(
            content,
            class_="popup_trigger",
            href="javascript:void(0);",
            # Needed to prevent wrong linking when views are parts of dashlets
            target="_self",
            onclick=onclick,
            onmouseenter=onmouseenter,
            onmouseleave=onmouseleave,
        )

        classes: List[Optional[str]] = ["popup_trigger"]
        if isinstance(cssclass, list):
            classes.extend(cssclass)
        elif cssclass:
            classes.append(cssclass)

        return self.render_div(atag + method.content,
                               class_=classes,
                               id_="popup_trigger_%s" % ident,
                               style=style)

    def element_dragger_url(self, dragging_tag: str, base_url: str) -> None:
>>>>>>> upstream/master
        self.write_html(
            self.render_element_dragger(
                dragging_tag,
                drop_handler=
                "function(index){return cmk.element_dragging.url_drop_handler(%s, index);})" %
                json.dumps(base_url)))

<<<<<<< HEAD
    def element_dragger_js(self, dragging_tag, drop_handler, handler_args):
=======
    def element_dragger_js(self, dragging_tag: str, drop_handler: str,
                           handler_args: Dict[str, Any]) -> None:
>>>>>>> upstream/master
        self.write_html(
            self.render_element_dragger(
                dragging_tag,
                drop_handler="function(new_index){return %s(%s, new_index);})" %
                (drop_handler, json.dumps(handler_args))))

    # Currently only tested with tables. But with some small changes it may work with other
    # structures too.
<<<<<<< HEAD
    def render_element_dragger(self, dragging_tag, drop_handler):
=======
    def render_element_dragger(self, dragging_tag: str, drop_handler: str) -> HTML:
>>>>>>> upstream/master
        return self.render_a(self.render_icon("drag", _("Move this entry")),
                             href="javascript:void(0)",
                             class_=["element_dragger"],
                             onmousedown="cmk.element_dragging.start(event, this, %s, %s" %
                             (json.dumps(dragging_tag.upper()), drop_handler))

    #
    # HTML - All the common and more complex HTML rendering methods
    #

<<<<<<< HEAD
    def _dump_get_vars(self):
=======
    def _dump_get_vars(self) -> None:
>>>>>>> upstream/master
        self.begin_foldable_container("html", "debug_vars", True,
                                      _("GET/POST variables of this page"))
        self.debug_vars(hide_with_mouse=False)
        self.end_foldable_container()

<<<<<<< HEAD
    def debug_vars(self, prefix=None, hide_with_mouse=True, vars_=None):
        it = self.request.itervars() if vars_ is None else vars_.iteritems()
=======
    def debug_vars(self,
                   prefix: Optional[str] = None,
                   hide_with_mouse: bool = True,
                   vars_: Optional[Dict[str, str]] = None) -> None:
        it = self.request.itervars() if vars_ is None else vars_.items()
>>>>>>> upstream/master
        hover = "this.style.display=\'none\';"
        self.open_table(class_=["debug_vars"], onmouseover=hover if hide_with_mouse else None)
        self.tr(self.render_th(_("POST / GET Variables"), colspan="2"))
        for name, value in sorted(it):
            if name in ["_password", "password"]:
                value = "***"
            if not prefix or name.startswith(prefix):
                self.tr(self.render_td(name, class_="left") + self.render_td(value, class_="right"))
        self.close_table()
<<<<<<< HEAD

    # TODO: Rename the status_icons because they are not only showing states. There are also actions.
    # Something like footer icons or similar seems to be better
    def _write_status_icons(self):
        self.icon_button(self.makeuri([]),
                         _("URL to this frame"),
                         "frameurl",
                         target="_top",
                         cssclass="inline")
        self.icon_button("index.py?" + self.urlencode_vars([("start_url", self.makeuri([]))]),
                         _("URL to this page including sidebar"),
                         "pageurl",
                         target="_top",
                         cssclass="inline")

        # TODO: Move this away from here. Make a context button. The view should handle this
        if self.myfile == "view" and self.request.var('mode') != 'availability' and config.user.may(
                "general.csv_export"):
            self.icon_button(self.makeuri([("output_format", "csv_export")]),
                             _("Export as CSV"),
                             "download_csv",
                             target="_top",
                             cssclass="inline")

        # TODO: This needs to be realized as plugin mechanism
        if self.myfile == "view":
            mode_name = "availability" if self.request.var("mode") == "availability" else "view"

            encoded_vars = {}
            for k, v in self.page_context.items():
                if v is None:
                    v = ''
                elif isinstance(v, six.text_type):
                    v = v.encode('utf-8')
                encoded_vars[k] = v

            self.popup_trigger(
                self.render_icon("menu", _("Add this view to..."), cssclass="iconbutton inline"),
                'add_visual',
                'add_visual',
                data=[mode_name, encoded_vars, {
                    'name': self.request.var('view_name')
                }],
                url_vars=[("add_type", mode_name)])

        # TODO: This should be handled by pagetypes.py
        elif self.myfile == "graph_collection":

            self.popup_trigger(self.render_icon("menu",
                                                _("Add this graph collection to..."),
                                                cssclass="iconbutton inline"),
                               'add_visual',
                               'add_visual',
                               data=["graph_collection", {}, {
                                   'name': self.request.var('name')
                               }],
                               url_vars=[("add_type", "graph_collection")])

        for img, tooltip in self.status_icons.items():
            if isinstance(tooltip, tuple):
                tooltip, url = tooltip
                self.icon_button(url, tooltip, img, cssclass="inline")
            else:
                self.icon(tooltip, img, cssclass="inline")

        if self.times:
            self.measure_time('body')
            self.open_div(class_=["execution_times"])
            entries = sorted(self.times.items())
            for name, duration in entries:
                self.div("%s: %.1fms" % (name, duration * 1000))
            self.close_div()

    #
    # FIXME: Legacy functions
    #

    # TODO: Remove this specific legacy function. Change code using this to valuespecs
    def datetime_input(self, varname, default_value, submit=None):
        try:
            t = self.get_datetime_input(varname)
        except Exception:
            t = default_value

        if varname in self.user_errors:
            self.add_user_error(varname + "_date", self.user_errors[varname])
            self.add_user_error(varname + "_time", self.user_errors[varname])
            self.set_focus(varname + "_date")

        br = time.localtime(t)
        self.date_input(varname + "_date", br.tm_year, br.tm_mon, br.tm_mday, submit=submit)
        self.write_text(" ")
        self.time_input(varname + "_time", br.tm_hour, br.tm_min, submit=submit)
        self.form_vars.append(varname + "_date")
        self.form_vars.append(varname + "_time")

    # TODO: Remove this specific legacy function. Change code using this to valuespecs
    def time_input(self, varname, hours, mins, submit=None):
        self.text_input(varname,
                        "%02d:%02d" % (hours, mins),
                        cssclass="time",
                        size=5,
                        submit=submit,
                        omit_css_width=True)

    # TODO: Remove this specific legacy function. Change code using this to valuespecs
    def date_input(self, varname, year, month, day, submit=None):
        self.text_input(varname,
                        "%04d-%02d-%02d" % (year, month, day),
                        cssclass="date",
                        size=10,
                        submit=submit,
                        omit_css_width=True)

    # TODO: Remove this specific legacy function. Change code using this to valuespecs
    def get_datetime_input(self, varname):
        t = self.request.var(varname + "_time")
        d = self.request.var(varname + "_date")
        if not t or not d:
            raise MKUserError([varname + "_date", varname + "_time"],
                              _("Please specify a date and time."))

        try:
            br = time.strptime(d + " " + t, "%Y-%m-%d %H:%M")
        except:
            raise MKUserError([varname + "_date", varname + "_time"],
                              _("Please enter the date/time in the format YYYY-MM-DD HH:MM."))
        return int(time.mktime(br))

    # TODO: Remove this specific legacy function. Change code using this to valuespecs
    def get_time_input(self, varname, what):
        t = self.request.var(varname)
        if not t:
            raise MKUserError(varname, _("Please specify %s.") % what)

        try:
            h, m = t.split(":")
            m = int(m)
            h = int(h)
            if m < 0 or m > 59 or h < 0:
                raise Exception()
        except:
            raise MKUserError(varname, _("Please enter the time in the format HH:MM."))
        return m * 60 + h * 3600
=======
>>>>>>> upstream/master
