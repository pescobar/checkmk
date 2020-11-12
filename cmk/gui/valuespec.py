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

# FIXME: Cleanups
# - Consolidate ListChoice and DualListChoice to use the same class
#   and rename to better name
<<<<<<< HEAD
# - Consolidate RadioChoice and DropdownChoice to use same class
#   and rename to better name
# - Consolidate ListOf and ListOfStrings/ListOfIntegers
=======
# - Consolidate ListOf and ListOfStrings
>>>>>>> upstream/master
# - Checkbox
#   -> rename to Boolean
#   -> Add alternative rendering "dropdown"
# - Some reordering, e.g. move specific valuspecs / factories to the bottom of
#   the file
# - Refactor "orientation" argument to use some Enum, similar to Labels.World

<<<<<<< HEAD
from __future__ import division
import abc
import base64
from enum import Enum
import hashlib
import ipaddress  # type: ignore
=======
import abc
import base64
from collections.abc import MutableMapping, Sequence as ABCSequence
from enum import Enum
import datetime
import hashlib
import io
import ipaddress
>>>>>>> upstream/master
import json
import logging
import math
import numbers
<<<<<<< HEAD
import os
import re
import socket
import sre_constants
import time
import types
import urlparse
from UserDict import DictMixin
from StringIO import StringIO
from typing import (  # pylint: disable=unused-import
    Dict, Pattern, Type, Union, Callable, Text, Any, List, Optional as TypingOptional, Tuple as
    TypingTuple,
)
from PIL import Image  # type: ignore

import six
from Cryptodome.PublicKey import RSA
=======
from pathlib import Path
import re
import socket
import time
import uuid
import urllib.parse
from typing import (Any, Callable, Dict, Generic, List, Optional as _Optional, Pattern, Set,
                    SupportsFloat, Tuple as _Tuple, Type, TypeVar, Union, Sequence, NamedTuple,
                    Protocol)

from dateutil.relativedelta import relativedelta
from dateutil.tz import tzlocal

from PIL import Image  # type: ignore[import]
from six import ensure_binary, ensure_str
from Cryptodome.PublicKey import RSA
from OpenSSL import crypto  # type: ignore[import]
>>>>>>> upstream/master

import cmk.utils.log
import cmk.utils.paths
import cmk.utils.defines as defines
<<<<<<< HEAD

import cmk.gui.forms as forms
import cmk.gui.utils as utils
from cmk.gui.i18n import _
from cmk.gui.pages import page_registry, Page, AjaxPage
from cmk.gui.globals import html
from cmk.gui.htmllib import HTML
from cmk.gui.exceptions import MKUserError, MKGeneralException
from cmk.gui.plugins.metrics import metric_info
=======
from cmk.utils.type_defs import Seconds
import cmk.utils.regex

import cmk.gui.forms as forms
import cmk.gui.utils as utils
import cmk.gui.escaping as escaping
import cmk.gui.sites as sites
import cmk.gui.config as config
from cmk.gui.i18n import _
from cmk.gui.pages import page_registry, AjaxPage
from cmk.gui.globals import html, request as global_request
from cmk.gui.utils.html import HTML
from cmk.gui.exceptions import MKUserError, MKGeneralException
from cmk.gui.type_defs import Choices, GroupedChoices, ChoiceGroup
from cmk.gui.view_utils import render_labels
from cmk.gui.utils.popups import MethodAjax, MethodColorpicker

from cmk.gui.utils.urls import makeuri
>>>>>>> upstream/master

import livestatus

seconds_per_day = 86400

# Some arbitrary object for checking whether or not default_value was set
<<<<<<< HEAD
_DEF_VALUE = object()


class ValueSpec(object):
=======
DEF_VALUE = object()

ValueSpecValidateFunc = Callable[[Any, str], None]
ValueSpecHelp = Union[str, HTML, Callable[[], Union[str, HTML]]]

C = TypeVar('C', bound='Comparable')


# Look, mom, we finally have Haskell type classes! :-D Naive version requiring
# only <, hopefully some similar class will make it into typing soon...
class Comparable(Protocol):
    @abc.abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass


# NOTE: Bounds are inclusive!
class Bounds(Generic[C]):
    def __init__(self, lower: _Optional[C], upper: _Optional[C]) -> None:
        super().__init__()
        self.__lower = lower
        self.__upper = upper

    def lower(self, default: C) -> C:
        return default if self.__lower is None else self.__lower

    def validate_value(self, value: C, varprefix: str) -> None:
        if self.__lower is not None and value < self.__lower:
            raise MKUserError(
                varprefix,
                _("%s is too low. The minimum allowed value is %s.") % (value, self.__lower))
        if self.__upper is not None and self.__upper < value:
            raise MKUserError(
                varprefix,
                _("%s is too high. The maximum allowed value is %s.") % (value, self.__upper))


class ValueSpec:
>>>>>>> upstream/master
    """Abstract base class of all value declaration classes"""

    # TODO: Remove **kwargs once all valuespecs have been changed
    # TODO: Cleanup help argument redefined-builtin
    def __init__(  # pylint: disable=redefined-builtin
            self,
<<<<<<< HEAD
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
            **kwargs):
        super(ValueSpec, self).__init__()
        self._title = title
        self._help = help
        if default_value is not _DEF_VALUE:
            self._default_value = default_value
        self._validate = validate

    def title(self):
        return self._title

    def help(self):
        if isinstance(self._help, (types.FunctionType, types.MethodType)):
            return self._help()
        return self._help

    def render_input(self, varprefix, value):
=======
            title: _Optional[str] = None,
            help: _Optional[ValueSpecHelp] = None,
            default_value: Any = DEF_VALUE,
            validate: _Optional[ValueSpecValidateFunc] = None,
            **kwargs):
        super().__init__()
        self._title = title
        self._help = help
        if default_value is not DEF_VALUE:
            self._default_value = default_value
        self._validate = validate

    def title(self) -> _Optional[str]:
        return self._title

    def help(self) -> Union[str, HTML, None]:
        if callable(self._help):
            return self._help()

        if isinstance(self._help, HTML):
            return self._help

        if self._help is None:
            return None

        assert isinstance(self._help, str)
        return ensure_str(self._help)

    def render_input(self, varprefix: str, value: Any) -> None:
>>>>>>> upstream/master
        """Create HTML-form elements that represent a given
        value and let the user edit that value

        The varprefix is prepended to the HTML variable names and is needed in
        order to make the variable unique in case that another Value of the same
        type is being used as well.  The function may assume that the type of the
        value is valid."""
<<<<<<< HEAD
        pass

    def set_focus(self, varprefix):
=======

    def set_focus(self, varprefix: str) -> None:
>>>>>>> upstream/master
        """Sets the input focus (cursor) into the most promiment field of the
        HTML code previously rendered with render_input()"""
        html.set_focus(varprefix)

<<<<<<< HEAD
    def canonical_value(self):
=======
    def canonical_value(self) -> Any:
>>>>>>> upstream/master
        """Create a canonical, minimal, default value that matches the datatype
        of the value specification and fulfills also data validation."""
        return None

<<<<<<< HEAD
    def default_value(self):
=======
    def default_value(self) -> Any:
>>>>>>> upstream/master
        """Return a default value for this variable

        This is optional and only used in the value editor for same cases where
        the default value is known."""
        try:
<<<<<<< HEAD
            if isinstance(self._default_value, (types.FunctionType, types.MethodType)):
=======
            if callable(self._default_value):
>>>>>>> upstream/master
                return self._default_value()
            return self._default_value
        except Exception:
            return self.canonical_value()

    # TODO: Rename to value_to_html?
<<<<<<< HEAD
    def value_to_text(self, value):
=======
    def value_to_text(self, value: Any) -> str:
>>>>>>> upstream/master
        """Creates a text-representation of the value that can be
        used in tables and other contextes

        It is to be read by the user and need not to be parsable.  The function
        may assume that the type of the value is valid.

        In the current implementation this function is only used to render the
        object for html code. So it is allowed to add html code for better
        layout in the GUI."""
        return repr(value)

<<<<<<< HEAD
    def from_html_vars(self, varprefix):
=======
    def value_to_json(self, value):
        raise NotImplementedError()

    def value_from_json(self, json_value):
        raise NotImplementedError()

    def from_html_vars(self, varprefix: str) -> Any:
>>>>>>> upstream/master
        """Create a value from the current settings of the HTML variables

        This function must also check the validity and may raise a MKUserError
        in case of invalid set variables."""
        return None

<<<<<<< HEAD
    def validate_value(self, value, varprefix):
=======
    def validate_value(self, value: Any, varprefix: str) -> None:
>>>>>>> upstream/master
        """Check if a given value is a valid structure for the current valuespec

        The validation is done in 3 phases:

        1. validate_datatype : Ensure the python data type is as expected
        2. _validate_value   : Valuespec type specific validations
<<<<<<< HEAD
        3. _custom_validate  : instance specific validations
=======
        3. self._validate    : instance specific validations
>>>>>>> upstream/master
        """
        # TODO: Would be really good to enable this to prevent unexpected data
        # types being written to the configuration. For the moment we can not
        # enable this because of the Web API: When using JSON as request_format
        # the JSON modules decodes all strings to unicode strings which are not
        # accepted by some attribute valuespecs which base on e.g. TextAscii.
        # This should be solved during Python3 transformation where we will
        # finally make a huge switch to unicode strings in many places.
        # TODO: Cleanup all external direct calls to validate_datatype() once this is
        #       being enabled.
        #self.validate_datatype(value, varprefix)
        self._validate_value(value, varprefix)
<<<<<<< HEAD
        self._custom_validate(value, varprefix)

    def validate_datatype(self, value, varprefix):
        """Check if a given value matches the datatype of described by this class."""
        pass

    def _validate_value(self, value, varprefix):
=======
        if self._validate:
            self._validate(value, varprefix)

    def validate_datatype(self, value: Any, varprefix: str) -> None:
        """Check if a given value matches the datatype of described by this class."""

    def _validate_value(self, value: Any, varprefix: str) -> None:
>>>>>>> upstream/master
        """Override this method to implement custom validation functions for sub-valuespec types

        This function should assume that the data type is valid (either because
        it has been returned by from_html_vars() or because it has been checked
        with validate_datatype())."""
<<<<<<< HEAD
        pass

    def _custom_validate(self, value, varprefix):
        """Call instance specific validations

        These are the ones that are configured by the valuespec instance argument
        validate = ...."""
        if self._validate:
            self._validate(value, varprefix)
=======

    def transform_value(self, value: Any) -> Any:
        """Transform the given value with the valuespecs transform logic and give it back"""
        return value
>>>>>>> upstream/master


class FixedValue(ValueSpec):
    """A fixed non-editable value, e.g. to be used in 'Alternative'"""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            value,  # type: Any
            totext=None,  # type: Text
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(FixedValue, self).__init__(title=title,
                                         help=help,
                                         default_value=default_value,
                                         validate=validate)
        self._value = value
        self._totext = totext

    def canonical_value(self):
        return self._value

    def render_input(self, varprefix, value):
        html.write(self.value_to_text(value))

    def value_to_text(self, value):
        if self._totext is not None:
            return self._totext
        elif isinstance(value, six.text_type):
            return value
        return str(value)

    def from_html_vars(self, varprefix):
        return self._value

    def validate_datatype(self, value, varprefix):
=======
        self,
        value: Any,
        totext: _Optional[str] = None,
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        self._value = value
        self._totext = totext

    def canonical_value(self) -> Any:
        return self._value

    def render_input(self, varprefix: str, value: Any) -> None:
        html.write(self.value_to_text(value))

    def value_to_text(self, value: Any) -> str:
        if self._totext is not None:
            return self._totext
        if isinstance(value, str):
            return value
        return ensure_str(value)

    def value_to_json(self, value):
        return value

    def value_from_json(self, json_value):
        return json_value

    def from_html_vars(self, varprefix: str) -> Any:
        return self._value

    def validate_datatype(self, value: Any, varprefix: str) -> None:
>>>>>>> upstream/master
        if not self._value == value:
            raise MKUserError(varprefix,
                              _("Invalid value, must be '%r' but is '%r'") % (self._value, value))


class Age(ValueSpec):
    """Time in seconds"""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            label=None,  # type: TypingOptional[Text]
            minvalue=None,  # type: TypingOptional[int]
            maxvalue=None,  # type: TypingOptional[Union[int, float]]
            display=None,  # type: TypingOptional[List[str]]
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Age, self).__init__(title=title,
                                  help=help,
                                  default_value=default_value,
                                  validate=validate)
        self._label = label
        self._minvalue = minvalue
        self._maxvalue = maxvalue
        self._display = display if display is not None else \
            ["days", "hours", "minutes", "seconds"]

    def canonical_value(self):
        if self._minvalue:
            return self._minvalue
        return 0

    def render_input(self, varprefix, value):
=======
        self,
        label: _Optional[str] = None,
        minvalue: _Optional[Seconds] = None,
        maxvalue: _Optional[Seconds] = None,
        display: _Optional[List[str]] = None,
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
        cssclass: _Optional[str] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        self._label = label
        self._bounds = Bounds[Seconds](minvalue, maxvalue)
        self._display = display if display is not None else \
            ["days", "hours", "minutes", "seconds"]
        self._cssclass = cssclass

    def canonical_value(self) -> Seconds:
        return self._bounds.lower(0)

    def render_input(self, varprefix: str, value: Seconds) -> None:
>>>>>>> upstream/master
        days, rest = divmod(value, 60 * 60 * 24)
        hours, rest = divmod(rest, 60 * 60)
        minutes, seconds = divmod(rest, 60)

<<<<<<< HEAD
        html.open_div()
=======
        html.open_div(class_=["vs_age", self._cssclass])
>>>>>>> upstream/master
        if self._label:
            html.write(self._label + " ")

        takeover = 0
<<<<<<< HEAD
        first = True
=======
>>>>>>> upstream/master
        for uid, title, val, tkovr_fac in [("days", _("days"), days, 24),
                                           ("hours", _("hours"), hours, 60),
                                           ("minutes", _("mins"), minutes, 60),
                                           ("seconds", _("secs"), seconds, 60)]:
            if uid in self._display:
                val += takeover
                takeover = 0
<<<<<<< HEAD
                html.number_input(varprefix + "_" + uid, val, 3 if first else 2)
                html.write(" %s " % title)
                first = False
=======
                html.text_input(varprefix + "_" + uid,
                                default_value=str(val),
                                size=4,
                                cssclass="number")
                html.write(" %s " % title)
>>>>>>> upstream/master
            else:
                takeover = (takeover + val) * tkovr_fac
        html.close_div()

<<<<<<< HEAD
    def from_html_vars(self, varprefix):
        # TODO: Validate for correct numbers!
        return (utils.saveint(html.request.var(varprefix + '_days', 0)) * 3600 * 24 +
                utils.saveint(html.request.var(varprefix + '_hours', 0)) * 3600 +
                utils.saveint(html.request.var(varprefix + '_minutes', 0)) * 60 +
                utils.saveint(html.request.var(varprefix + '_seconds', 0)))

    def value_to_text(self, value):
=======
    def from_html_vars(self, varprefix: str) -> Seconds:
        # TODO: Validate for correct numbers!
        return (html.request.get_integer_input_mandatory(varprefix + '_days', 0) * 3600 * 24 +
                html.request.get_integer_input_mandatory(varprefix + '_hours', 0) * 3600 +
                html.request.get_integer_input_mandatory(varprefix + '_minutes', 0) * 60 +
                html.request.get_integer_input_mandatory(varprefix + '_seconds', 0))

    def value_to_text(self, value: Seconds) -> str:
>>>>>>> upstream/master
        days, rest = divmod(value, 60 * 60 * 24)
        hours, rest = divmod(rest, 60 * 60)
        minutes, seconds = divmod(rest, 60)
        parts = []
        for title, count in [
            (_("days"), days),
            (_("hours"), hours),
            (_("minutes"), minutes),
            (_("seconds"), seconds),
        ]:
            if count:
                parts.append("%d %s" % (count, title))

        if parts:
            return " ".join(parts)
        return _("no time")

<<<<<<< HEAD
    def validate_datatype(self, value, varprefix):
=======
    def value_to_json(self, value):
        return value

    def value_from_json(self, json_value):
        return json_value

    def validate_datatype(self, value: Seconds, varprefix: str) -> None:
>>>>>>> upstream/master
        if not isinstance(value, int):
            raise MKUserError(
                varprefix,
                _("The value %r has type %s, but must be of type int") % (value, _type_name(value)))

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
        if self._minvalue is not None and value < self._minvalue:
            raise MKUserError(
                varprefix,
                _("%s is too low. The minimum allowed value is %s.") % (value, self._minvalue))
        if self._maxvalue is not None and value > self._maxvalue:
            raise MKUserError(
                varprefix,
                _("%s is too high. The maximum allowed value is %s.") % (value, self._maxvalue))


class Integer(ValueSpec):
    """Editor for a single integer"""
    def __init__(  # pylint: disable=redefined-builtin
            self,
            size=None,  # type: TypingOptional[int]
            minvalue=None,  # type: TypingOptional[Union[float, int]]
            maxvalue=None,  # type: TypingOptional[Union[float, int]]
            label=None,  # type: TypingOptional[Text]
            unit="",  # type: Text
            thousand_sep=None,  # type: TypingOptional[Text]
            display_format="%d",  # type: Text
            align="left",  # type: str
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Integer, self).__init__(title=title,
                                      help=help,
                                      default_value=default_value,
                                      validate=validate)
        # TODO: inconsistency with default_value. All should be named with underscore
        self._minvalue = minvalue
        self._maxvalue = maxvalue
        self._label = label
        self._unit = unit
        self._thousand_sep = thousand_sep
        self._display_format = display_format
        self._align = align

        if size is None and maxvalue is not None:
            self._size = 1 + int(math.log10(maxvalue)) + \
               (3 if isinstance(maxvalue, float) else 0)
        else:
            self._size = size if size is not None else 5

    def canonical_value(self):
        if self._minvalue:
            return self._minvalue
        return 0

    def render_input(self, varprefix, value):
        if self._label:
            html.write(self._label)
            html.nbsp()
        if self._align == "right":
            style = "text-align: right;"
        else:
            style = ""
        if value == "":  # This is needed for ListOfIntegers
            html.text_input(varprefix, "", "number", size=self._size, style=style)
        else:
            html.number_input(varprefix, self._render_value(value), size=self._size, style=style)
=======
    def _validate_value(self, value: Seconds, varprefix: str) -> None:
        self._bounds.validate_value(value, varprefix)


class NumericRenderer:
    def __init__(
        self,
        size: _Optional[int],
        maxvalue: _Optional[SupportsFloat],
        label: _Optional[str],
        unit: str,
        thousand_sep: _Optional[str],
        align: str,
    ):
        super().__init__()
        if size is not None:
            self._size = size
        elif maxvalue is not None:
            self._size = (4 if isinstance(maxvalue, float) else 1) + int(math.log10(maxvalue))
        else:
            self._size = 5
        self._label = label
        self._unit = unit
        self._thousand_sep = thousand_sep
        self._align = align

    def text_input(self, varprefix: str, text: str) -> None:
        html.text_input(varprefix,
                        default_value=text,
                        cssclass="number",
                        size=self._size,
                        style="text-align: right;" if self._align == "right" else "")

    def render_input(self, varprefix: str, text: str) -> None:
        if self._label:
            html.write(self._label)
            html.nbsp()
        self.text_input(varprefix, text)
>>>>>>> upstream/master
        if self._unit:
            html.nbsp()
            html.write(self._unit)

<<<<<<< HEAD
    def _render_value(self, value):
        return self._display_format % utils.saveint(value)

    def from_html_vars(self, varprefix):
        try:
            return int(html.request.var(varprefix))
        except:
            raise MKUserError(
                varprefix,
                _("The text <b><tt>%s</tt></b> is not a valid integer number.") %
                html.request.var(varprefix))

    def value_to_text(self, value):
        text = self._display_format % value
        if self._thousand_sep:
            sepped = ""
            rest = text
            while len(rest) > 3:
                sepped = self._thousand_sep + rest[-3:] + sepped
                rest = rest[:-3]
            sepped = rest + sepped
            text = sepped

=======
    def format_text(self, text: str) -> str:
        if self._thousand_sep:
            sepped = text[:((len(text) + 3 - 1) % 3) + 1]
            for pos in range(len(sepped), len(text), 3):
                sepped += self._thousand_sep + text[pos:pos + 3]
            text = sepped
>>>>>>> upstream/master
        if self._unit:
            text += "&nbsp;" + self._unit
        return text

<<<<<<< HEAD
    def validate_datatype(self, value, varprefix):
        if not isinstance(value, numbers.Integral):
            raise MKUserError(
                varprefix,
                _("The value %r has the wrong type %s, but must be of type int") %
                (value, _type_name(value)))

    def _validate_value(self, value, varprefix):
        if self._minvalue is not None and value < self._minvalue:
            raise MKUserError(
                varprefix,
                _("%s is too low. The minimum allowed value is %s.") % (value, self._minvalue))
        if self._maxvalue is not None and value > self._maxvalue:
            raise MKUserError(
                varprefix,
                _("%s is too high. The maximum allowed value is %s.") % (value, self._maxvalue))
=======

class Integer(ValueSpec):
    """Editor for a single integer"""
    def __init__(  # pylint: disable=redefined-builtin
        self,
        size: _Optional[int] = None,
        minvalue: _Optional[int] = None,
        maxvalue: _Optional[int] = None,
        label: _Optional[str] = None,
        unit: str = "",
        thousand_sep: _Optional[str] = None,
        display_format: str = "%d",
        align: str = "left",
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        self._bounds = Bounds[int](minvalue, maxvalue)
        self._renderer = NumericRenderer(size=size,
                                         maxvalue=maxvalue,
                                         label=label,
                                         unit=unit,
                                         thousand_sep=thousand_sep,
                                         align=align)
        self._display_format = display_format

    def canonical_value(self) -> int:
        return self._bounds.lower(0)

    def render_input(self, varprefix: str, value: _Optional[int]) -> None:
        # This is needed for displaying the "empty field" when using Integer valuespecs in
        # ListOfStrings()
        if value is None:
            text: str = ""
        else:
            text = self._render_value(value)

        self._renderer.render_input(varprefix, text)

    def _render_value(self, value: int) -> str:
        return self._display_format % utils.saveint(value)

    def from_html_vars(self, varprefix: str) -> int:
        return html.request.get_integer_input_mandatory(varprefix)

    def value_to_text(self, value: int) -> str:
        return self._renderer.format_text(self._render_value(value))

    def validate_datatype(self, value: int, varprefix: str) -> None:
        if isinstance(value, numbers.Integral):
            return
        raise MKUserError(
            varprefix,
            _("The value %r has the wrong type %s, but must be of type int") %
            (value, _type_name(value)))

    def _validate_value(self, value: int, varprefix: str) -> None:
        self._bounds.validate_value(value, varprefix)
>>>>>>> upstream/master


class Filesize(Integer):
    """Filesize in Byte, KByte, MByte, Gigabyte, Terabyte"""
<<<<<<< HEAD
    _names = ['Byte', 'KByte', 'MByte', 'GByte', 'TByte']

    def get_exponent(self, value):
        for exp, count in ((exp, 1024**exp) for exp in reversed(xrange(len(self._names)))):
=======
    _names = [u'Byte', u'KByte', u'MByte', u'GByte', u'TByte']

    def get_exponent(self, value: int) -> _Tuple[int, int]:
        for exp, count in ((exp, 1024**exp) for exp in reversed(range(len(self._names)))):
>>>>>>> upstream/master
            if value == 0:
                return 0, 0
            if value % count == 0:
                return exp, int(value / count)  # fixed: true-division
<<<<<<< HEAD

    def render_input(self, varprefix, value):
        exp, count = self.get_exponent(value)
        html.number_input(varprefix + '_size', count, size=self._size)
        html.nbsp()
        choices = [(str(nr), name) for (nr, name) in enumerate(self._names)]
        html.dropdown(varprefix + '_unit', choices, deflt=str(exp))

    def from_html_vars(self, varprefix):
        try:
            return int(html.request.var(varprefix + '_size')) * (1024**int(
                html.request.var(varprefix + '_unit')))
        except:
            raise MKUserError(varprefix + '_size', _("Please enter a valid integer number"))

    def value_to_text(self, value):
=======
        raise ValueError("Invalid value: %r" % value)

    def render_input(self, varprefix: str, value: _Optional[int]) -> None:
        # The value type is only Optional to be compatible with the base class
        assert value is not None
        exp, count = self.get_exponent(value)
        self._renderer.text_input(varprefix + '_size', str(count))
        html.nbsp()
        choices: Choices = [(str(nr), name) for (nr, name) in enumerate(self._names)]
        html.dropdown(varprefix + '_unit', choices, deflt=str(exp))

    def from_html_vars(self, varprefix: str) -> int:
        try:
            return html.request.get_integer_input_mandatory(varprefix + '_size') * (
                1024**html.request.get_integer_input_mandatory(varprefix + '_unit'))
        except Exception:
            raise MKUserError(varprefix + '_size', _("Please enter a valid integer number"))

    # TODO: Cleanup this hierarchy problem
    def value_to_text(self, value: int) -> str:  # type: ignore[override]
>>>>>>> upstream/master
        exp, count = self.get_exponent(value)
        return "%s %s" % (count, self._names[exp])


class TextAscii(ValueSpec):
    """Editor for a line of text"""

    # TODO: Cleanup attrencode attribute
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            label=None,  # type: TypingOptional[Text]
            size=25,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex=None,  # type: TypingOptional[Union[str, Pattern[str]]]
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            autocomplete=True,  # type: bool
            hidden=False,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(TextAscii, self).__init__(title=title,
                                        help=help,
                                        default_value=default_value,
                                        validate=validate)
=======
        self,
        label: _Optional[str] = None,
        size: Union[int, str] = 25,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex: Union[None, str, Pattern[str]] = None,
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        autocomplete: bool = True,
        hidden: bool = False,
        placeholder: _Optional[str] = None,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._label = label
        self._size = size  # also possible: "max"
        self._try_max_width = try_max_width  # If set, uses calc(100%-10px)
        self._cssclass = cssclass
        self._strip = strip
        self._attrencode = attrencode
        self._allow_empty = allow_empty
        self._empty_text = empty_text
        self._read_only = read_only
<<<<<<< HEAD
        self._none_is_empty = none_is_empty
        self._forbidden_chars = forbidden_chars
        self._regex = regex
        if isinstance(self._regex, str):
            self._regex = re.compile(self._regex)
=======
        self._forbidden_chars = forbidden_chars
        if isinstance(regex, str):
            self._regex: _Optional[Pattern[str]] = re.compile(regex)
        else:
            self._regex = regex
>>>>>>> upstream/master
        self._regex_error = regex_error if regex_error is not None else \
            _("Your input does not match the required format.")
        self._minlen = minlen
        self._onkeyup = onkeyup
        self._autocomplete = autocomplete
        self._hidden = hidden
<<<<<<< HEAD

    def canonical_value(self):
        return ""

    def render_input(self, varprefix, value):
        value_text = "%s" % value if value is not None else ""

=======
        self._placeholder = placeholder

    def canonical_value(self) -> str:
        return ""

    # NOTE: Class hierarchy is broken, we can get Unicode here!
    def render_input(self, varprefix: str, value: _Optional[str]) -> None:
>>>>>>> upstream/master
        if self._label:
            html.write(self._label)
            html.nbsp()

<<<<<<< HEAD
        type_ = "password" if self._hidden else "text"

        attrs = {}
        if self._onkeyup:
            attrs["onkeyup"] = self._onkeyup

        html.text_input(
            varprefix,
            value_text,
=======
        html.text_input(
            varprefix,
            default_value="%s" % value if value is not None else "",
>>>>>>> upstream/master
            size=self._size,
            try_max_width=self._try_max_width,
            read_only=self._read_only,
            cssclass=self._cssclass,
<<<<<<< HEAD
            type_=type_,
            attrs=attrs,
            autocomplete="off" if not self._autocomplete else None,
        )

    def value_to_text(self, value):
=======
            type_="password" if self._hidden else "text",
            autocomplete="off" if not self._autocomplete else None,
            onkeyup=self._onkeyup if self._onkeyup else None,
            placeholder=self._placeholder,
        )

    # NOTE: Class hierarchy is broken, we can get Unicode here!
    def value_to_text(self, value: str) -> str:
>>>>>>> upstream/master
        if not value:
            return self._empty_text

        if self._attrencode:
<<<<<<< HEAD
            return html.attrencode(value)
        return value

    def from_html_vars(self, varprefix):
        value = html.request.var(varprefix, "")
        if self._strip:
            value = value.strip()
        if self._none_is_empty and not value:
            return None
        return value

    def validate_datatype(self, value, varprefix):
        if self._none_is_empty and value is None:
            return

=======
            return escaping.escape_attribute(value)
        return ensure_str(value)

    def from_html_vars(self, varprefix: str) -> str:
        value = html.request.get_str_input_mandatory(varprefix, "")

        if self._strip and value:
            value = value.strip()

        return value

    def validate_datatype(self, value: str, varprefix: str) -> None:
>>>>>>> upstream/master
        if not isinstance(value, str):
            raise MKUserError(
                varprefix,
                _("The value must be of type str, but it has type %s") % _type_name(value))

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
        try:
            six.text_type(value)
        except UnicodeDecodeError:
            raise MKUserError(varprefix, _("Non-ASCII characters are not allowed here."))
=======
    # NOTE: Class hierarchy is broken, we can get Unicode here!
    def _validate_value(self, value: str, varprefix: str) -> None:
        try:
            if isinstance(value, bytes):
                value.decode("ascii")
        except UnicodeDecodeError:
            raise MKUserError(varprefix, _("Non-ASCII characters are not allowed here."))

>>>>>>> upstream/master
        if self._forbidden_chars:
            for c in self._forbidden_chars:
                if c in value:
                    raise MKUserError(varprefix,
                                      _("The character <tt>%s</tt> is not allowed here.") % c)
<<<<<<< HEAD
        if self._none_is_empty and value == "":
            raise MKUserError(varprefix, _("An empty value must be represented with None here."))
        if not self._allow_empty and value.strip() == "":
            raise MKUserError(varprefix, _("An empty value is not allowed here."))
        if value and self._regex:
            if not self._regex.match(value):
=======

        if not self._allow_empty and value.strip() == "":
            raise MKUserError(varprefix, _("An empty value is not allowed here."))
        if value and self._regex:
            if not self._regex.match(ensure_str(value)):
>>>>>>> upstream/master
                raise MKUserError(varprefix, self._regex_error)

        if self._minlen is not None and len(value) < self._minlen:
            raise MKUserError(varprefix,
                              _("You need to provide at least %d characters.") % self._minlen)


<<<<<<< HEAD
class TextUnicode(TextAscii):
    def from_html_vars(self, varprefix):
        return html.get_unicode_input(varprefix, "").strip()

    def validate_datatype(self, value, varprefix):
        if not isinstance(value, six.string_types):
=======
class UUID(TextAscii):
    """Documentation for UUID

    """
    def from_html_vars(self, varprefix: str) -> str:
        value = html.request.get_str_input_mandatory(varprefix, "")
        if not value:
            value = str(uuid.uuid4())
        return value

    def render_input(self, varprefix: str, value: _Optional[str]) -> None:
        html.hidden_field(varprefix, value, add_var=True)


class TextUnicode(TextAscii):
    # TODO: Once we switched to Python 3 we can merge the unicode and non unicode class
    def from_html_vars(self, varprefix: str) -> str:  # type: ignore[override]
        return html.request.get_unicode_input_mandatory(varprefix, "").strip()

    def validate_datatype(self, value: str, varprefix: str) -> None:
        if not isinstance(value, str):
>>>>>>> upstream/master
            raise MKUserError(
                varprefix,
                _("The value must be of type str or unicode, but it has type %s") %
                _type_name(value))

<<<<<<< HEAD
=======
    def value_to_json(self, value):
        return value

    def value_from_json(self, json_value):
        return json_value

>>>>>>> upstream/master

# TODO: Cleanup kwargs
def ID(**kwargs):
    """Internal ID as used in many places (for contact names, group name, an so on)"""
    return TextAscii(regex=re.compile('^[a-zA-Z_][-a-zA-Z0-9_]*$'),
                     regex_error=_("An identifier must only consist of letters, digits, dash and "
                                   "underscore and it must start with a letter or underscore."),
                     **kwargs)


# TODO: Cleanup kwargs
def UnicodeID(**kwargs):
    """Same as the ID class, but allowing unicode objects"""
    return TextUnicode(regex=re.compile(r'^[\w][-\w0-9_]*$', re.UNICODE),
                       regex_error=_("An identifier must only consist of letters, digits, dash and "
                                     "underscore and it must start with a letter or underscore."),
                       **kwargs)


# TODO: Cleanup kwargs
def UserID(**kwargs):
    return TextUnicode(regex=re.compile(r'^[\w][-\w0-9_\.@]*$', re.UNICODE),
                       regex_error=_(
                           "An identifier must only consist of letters, digits, dash, dot, "
                           "at and underscore. But it must start with a letter or underscore."),
                       **kwargs)


class RegExp(TextAscii):
    infix = "infix"
    prefix = "prefix"
    complete = "complete"

    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            mode,  # type: str
            case_sensitive=True,  # type: bool
            mingroups=0,  # type: int
            maxgroups=None,  # type: TypingOptional[int]
            # TextAscii
            label=None,  # type: TypingOptional[Text]
            size=25,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex=None,  # type: TypingOptional[Union[str, Pattern[str]]]
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            autocomplete=True,  # type: bool
            hidden=False,  # type: bool
            # From ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(RegExp, self).__init__(
=======
        self,
        mode: str,
        case_sensitive: bool = True,
        mingroups: int = 0,
        maxgroups: _Optional[int] = None,
        # TextAscii
        label: _Optional[str] = None,
        size: Union[int, str] = 25,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex: Union[None, str, Pattern[str]] = None,
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        autocomplete: bool = True,
        hidden: bool = False,
        # From ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
>>>>>>> upstream/master
            label=label,
            size=size,
            try_max_width=try_max_width,
            cssclass=self._css_classes(case_sensitive, mode),
            strip=strip,
            attrencode=attrencode,
            allow_empty=allow_empty,
            empty_text=empty_text,
            read_only=read_only,
<<<<<<< HEAD
            none_is_empty=none_is_empty,
=======
>>>>>>> upstream/master
            forbidden_chars=forbidden_chars,
            regex=regex,
            regex_error=regex_error,
            minlen=minlen,
            onkeyup=onkeyup,
            autocomplete=autocomplete,
            hidden=hidden,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )

        self._mode = mode
        self._case_sensitive = case_sensitive
        self._mingroups = mingroups
        self._maxgroups = maxgroups

<<<<<<< HEAD
    def help(self):
        help_text = []

        default_help_text = super(RegExp, self).help()
=======
    def help(self) -> Union[str, HTML, None]:
        help_text: List[Union[str, HTML]] = []

        default_help_text = super().help()
>>>>>>> upstream/master
        if default_help_text is not None:
            help_text.append(default_help_text + "<br><br>")

        help_text.append(_("The text entered here is handled as a regular expression pattern."))

        if self._mode == RegExp.infix:
            help_text.append(
                _("The pattern is applied as infix search. Add a leading <tt>^</tt> "
                  "to make it match from the beginning and/or a tailing <tt>$</tt> "
                  "to match till the end of the text."))
        elif self._mode == RegExp.prefix:
            help_text.append(
                _("The pattern is matched from the beginning. Add a tailing "
                  "<tt>$</tt> to change it to a whole text match."))
        elif self._mode == RegExp.complete:
            help_text.append(
                _("The pattern is matching the whole text. You can add <tt>.*</tt> "
                  "in front or at the end of your pattern to make it either a prefix "
                  "or infix search."))

        if self._case_sensitive is True:
            help_text.append(_("The match is performed case sensitive."))
        elif self._case_sensitive is False:
            help_text.append(_("The match is performed case insensitive."))

        help_text.append(
<<<<<<< HEAD
            _("Read more about <a href=\"https://checkmk.com/cms_regexes.html\" target=\"_blank\">regular "
              "expression matching in Checkmk</a> in our user manual."))

        return " ".join(help_text)
=======
            _("Read more about [cms_regexes|regular expression matching in Checkmk] in our user manual."
             ))

        return u" ".join(u"%s" % h for h in help_text)
>>>>>>> upstream/master

    def _css_classes(self, case_sensitive, mode):
        classes = ["text", "regexp"]

        if case_sensitive is True:
            classes.append("case_sensitive")
        elif case_sensitive is False:
            classes.append("case_insensitive")

        if mode is not None:
            classes.append(mode)

        return " ".join(classes)

    def _validate_value(self, value, varprefix):
<<<<<<< HEAD
        super(RegExp, self)._validate_value(value, varprefix)
=======
        super()._validate_value(value, varprefix)
>>>>>>> upstream/master

        # Check if the string is a valid regex
        try:
            compiled = re.compile(value)
<<<<<<< HEAD
        except sre_constants.error as e:
=======
        except re.error as e:
>>>>>>> upstream/master
            raise MKUserError(varprefix, _('Invalid regular expression: %s') % e)

        if compiled.groups < self._mingroups:
            raise MKUserError(
                varprefix,
                _("Your regular expression containes <b>%d</b> groups. "
                  "You need at least <b>%d</b> groups.") % (compiled.groups, self._mingroups))
        if self._maxgroups is not None and compiled.groups > self._maxgroups:
            raise MKUserError(
                varprefix,
                _("Your regular expression containes <b>%d</b> groups. "
                  "It must have at most <b>%d</b> groups.") % (compiled.groups, self._maxgroups))


# TODO: Cleanup this multiple inheritance
class RegExpUnicode(TextUnicode, RegExp):
    pass


<<<<<<< HEAD
class EmailAddress(TextAscii):
    def __init__(  # pylint: disable=redefined-builtin
            self,
            make_clickable=False,  # type: bool
            # TextAscii
            label=None,  # type: TypingOptional[Text]
            size=40,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            autocomplete=True,  # type: bool
            hidden=False,  # type: bool
            # From ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(EmailAddress, self).__init__(
=======
class EmailAddress(TextUnicode):
    def __init__(  # pylint: disable=redefined-builtin
        self,
        make_clickable: bool = False,
        # TextAscii
        label: _Optional[str] = None,
        size: Union[int, str] = 40,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        autocomplete: bool = True,
        hidden: bool = False,
        # From ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
>>>>>>> upstream/master
            label=label,
            size=size,
            try_max_width=try_max_width,
            cssclass=cssclass,
            strip=strip,
            attrencode=attrencode,
            allow_empty=allow_empty,
            empty_text=empty_text,
            read_only=read_only,
<<<<<<< HEAD
            none_is_empty=none_is_empty,
            forbidden_chars=forbidden_chars,
            # The "new" top level domains are very unlimited in length. Theoretically they can be
            # up to 63 chars long. But currently the longest is 24 characters. Check this out with:
            # wget -qO - http://data.iana.org/TLD/tlds-alpha-by-domain.txt | tail -n+2 | wc -L
            regex=re.compile(r'^[A-Z0-9._%&+-]+@(localhost|[A-Z0-9.-]+\.[A-Z]{2,24})$', re.I),
=======
            forbidden_chars=forbidden_chars,
            # According to RFC5322 an email address is defined as:
            #     address = name-addr / addr-spec / group
            # We only allow the dot-atom of addr-spec here:
            #     addr-spec = (dot-atom / quoted-string / obs-local-part) "@" domain
            #     dot-atom = [CFWS] 1*atext *("." 1*atext) [CFWS]
            #     atext = ALPHA / DIGIT / "!" / "#" /  ; Printable US-ASCII
            #             "$" / "%" / "&" / "'"        ;  characters not including
            #             "&" / "'" / "*" / "+"        ;  specials. Used for atoms.
            #             "-" / "/" / "=" / "?"
            #             "^" / "_" / "`" / "{"
            #             "|" / "}" / "~"
            # with the additional extension of atext to the addr-spec as specified
            # by RFC6531:
            #     atext   =/  UTF8-non-ascii
            # Furthermore we do not allow comments inside CFWS and any leading or
            # trailing whitespace in the address is removed.
            #
            # The domain part of addr-spec is defined as:
            #     domain = dot-atom / domain-literal / obs-domain
            # We only allow dot-atom with a restricted character of [A-Z0-9.-] and a
            # length of 2-24 for the top level domain here. Although top level domains
            # may be longer the longest top level domain currently in use is 24
            # characters wide. Check this out with:
            #     wget -qO - http://data.iana.org/TLD/tlds-alpha-by-domain.txt | tail -n+2 | wc -L
            #
            # Note that the current regex allows multiple subsequent "." which are
            # not allowed by RFC5322.
            regex=re.compile(r"^[\w.!#$%&'*+-=?^`{|}~]+@(localhost|[\w.-]+\.[\w]{2,24})$",
                             re.I | re.UNICODE),
>>>>>>> upstream/master
            regex_error=regex_error,
            minlen=minlen,
            onkeyup=onkeyup,
            autocomplete=autocomplete,
            hidden=hidden,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
        self._make_clickable = make_clickable

<<<<<<< HEAD
    def value_to_text(self, value):
        if not value:
            return super(EmailAddress, self).value_to_text(value)
        elif self._make_clickable:
=======
    def value_to_text(self, value: str) -> str:
        if not value:
            return super().value_to_text(value)
        if self._make_clickable:
>>>>>>> upstream/master
            # TODO: This is a workaround for a bug. This function needs to return str objects right now.
            return "%s" % html.render_a(HTML(value), href="mailto:%s" % value)
        return value


<<<<<<< HEAD
# TODO: Cleanup kwargs
class EmailAddressUnicode(TextUnicode, EmailAddress):
    def __init__(self, **kwargs):
        super(EmailAddressUnicode, self).__init__(**kwargs)
        self._regex = re.compile(r'^[\w.%&+-]+@(localhost|[\w.-]+\.[\w]{2,24})$', re.I | re.UNICODE)


# TODO: Do not use kwargs here. Find out the arguments that are used
def IPNetwork(ip_class=None, **kwargs):
    """Same as IPv4Network, but allowing both IPv4 and IPv6"""
    if ip_class is None:
        ip_class = ipaddress.ip_interface

    def _validate_value(self, value, varprefix):
        super(IPNetwork, self)._validate_value(value, varprefix)

        try:
            ip_class()(value.decode("utf-8"))
        except ValueError as e:
            raise MKUserError(varprefix, _("Invalid address: %s") % e)

    kwargs.setdefault("size", 34)
    return TextAscii(validate=_validate_value, **kwargs)


# TODO: Do not use kwargs here. Find out the arguments that are used
def IPv4Network(**kwargs):
    """Network as used in routing configuration, such as '10.0.0.0/8' or '192.168.56.1'"""
    kwargs.setdefault("size", 18)
    return IPNetwork(ip_class=ipaddress.IPv4Interface, **kwargs)


# TODO: Do not use kwargs here. Find out the arguments that are used
def IPv4Address(**kwargs):
    kwargs.setdefault("size", 16)
    return IPNetwork(ip_class=ipaddress.IPv4Address, **kwargs)


class TextAsciiAutocomplete(TextAscii):
    def __init__(  # pylint: disable=redefined-builtin
            self,
            completion_ident,  # type: Text
            completion_params,  # type: Dict[Text, Any]
            # TextAscii
            label=None,  # type: TypingOptional[Text]
            size=40,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex=None,  # type: TypingOptional[Union[str, Pattern[str]]]
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            hidden=False,  # type: bool
            # From ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
=======
def IPNetwork(  # pylint: disable=redefined-builtin
    ip_class: Union[None, Type[ipaddress.IPv4Network], Type[ipaddress.IPv6Network]] = None,
    # TextAscii
    allow_empty: bool = True,
    size: Union[int, str] = 34,
    # From ValueSpec
    title: _Optional[str] = None,
    help: _Optional[ValueSpecHelp] = None,
    default_value: Any = DEF_VALUE,
) -> TextAscii:
    """Same as IPv4Network, but allowing both IPv4 and IPv6"""
    def _validate_value_for_one_class(value: str, varprefix: str) -> None:
        assert ip_class is not None
        try:
            ip_class(ensure_str(value))
        except ValueError as exc:
            ip_class_text = {
                ipaddress.IPv4Network: "IPv4",
                ipaddress.IPv6Network: "IPv6",
            }[ip_class]

            raise MKUserError(varprefix, _("Invalid %s address: %s") % (ip_class_text, exc))

    def _validate_value_for_both_classes(value: str, varprefix: str):
        errors = {}
        for ipc in (ipaddress.IPv4Network, ipaddress.IPv6Network):
            try:
                ipc(ensure_str(value))
                return
            except ValueError as exc:
                errors[ipc] = exc

        raise MKUserError(
            varprefix,
            _("Invalid host or network address. IPv4: %s, IPv6: %s") %
            (errors[ipaddress.IPv4Network], errors[ipaddress.IPv6Network]))

    def _validate_value(value: str, varprefix: str) -> None:
        if ip_class is not None:
            _validate_value_for_one_class(value, varprefix)
            return

        _validate_value_for_both_classes(value, varprefix)

    return TextAscii(
        validate=_validate_value,
        allow_empty=allow_empty,
        size=size,
        title=title,
        help=help,
        default_value=default_value,
    )


def IPv4Network(  # pylint: disable=redefined-builtin
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None) -> TextAscii:
    """Network as used in routing configuration, such as '10.0.0.0/8' or '192.168.56.1'"""
    return IPNetwork(ip_class=ipaddress.IPv4Network, size=18, title=title, help=help)


def IPv4Address(  # pylint: disable=redefined-builtin
    # TextAscii
    allow_empty: bool = True,
    # From ValueSpec
    title: _Optional[str] = None,
    help: _Optional[ValueSpecHelp] = None,
    default_value: Any = DEF_VALUE,
) -> TextAscii:
    def _validate_value(value: str, varprefix: str):
        try:
            ipaddress.IPv4Address(ensure_str(value))
        except ValueError as exc:
            raise MKUserError(varprefix, _("Invalid IPv4 address: %s") % exc)

    return TextAscii(
        validate=_validate_value,
        size=16,
        title=title,
        help=help,
        default_value=default_value,
        allow_empty=allow_empty,
    )


class TextAsciiAutocomplete(TextAscii):
    ident = ""

    def __init__(  # pylint: disable=redefined-builtin
        self,
        completion_ident: str,
        completion_params: Dict[str, Any],
        # TextAscii
        label: _Optional[str] = None,
        size: Union[int, str] = 40,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex: Union[None, str, Pattern[str]] = None,
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        hidden: bool = False,
        placeholder: _Optional[str] = None,
        # From ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
>>>>>>> upstream/master
    ):
        onkeyup = "cmk.valuespecs.autocomplete(this, %s, %s, %s);%s" % \
                            (json.dumps(completion_ident),
                             json.dumps(completion_params),
                             json.dumps(onkeyup), onkeyup)
<<<<<<< HEAD
        super(TextAsciiAutocomplete, self).__init__(
=======
        super().__init__(
>>>>>>> upstream/master
            label=label,
            size=size,
            try_max_width=try_max_width,
            cssclass=cssclass,
            strip=strip,
            attrencode=attrencode,
            allow_empty=allow_empty,
            empty_text=empty_text,
            read_only=read_only,
<<<<<<< HEAD
            none_is_empty=none_is_empty,
=======
>>>>>>> upstream/master
            forbidden_chars=forbidden_chars,
            regex=regex,
            regex_error=regex_error,
            minlen=minlen,
            onkeyup=onkeyup,
            autocomplete=False,
            hidden=hidden,
<<<<<<< HEAD
=======
            placeholder=placeholder,
>>>>>>> upstream/master
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )

    @classmethod
<<<<<<< HEAD
    def idents(cls):
        idents = {}
        for type_class in cls.__subclasses__():  # pylint: disable=no-member
=======
    def idents(cls) -> 'Dict[str, Type[TextAsciiAutocomplete]]':
        idents = {}
        for type_class in cls.__subclasses__():
>>>>>>> upstream/master
            idents[type_class.ident] = type_class
        return idents

    @classmethod
<<<<<<< HEAD
    def ajax_handler(cls):
        ident = html.request.var("ident")
=======
    def ajax_handler(cls, request) -> Choices:
        ident = request["ident"]
>>>>>>> upstream/master
        if not ident:
            raise MKUserError("ident", _("You need to set the \"%s\" parameter.") % "ident")

        if ident not in cls.idents():
            raise MKUserError("ident", _("Invalid ident: %s") % ident)

<<<<<<< HEAD
        raw_params = html.request.var("params")
        if not raw_params:
            raise MKUserError("params", _("You need to set the \"%s\" parameter.") % "params")

        try:
            params = json.loads(raw_params)
        except ValueError as e:  # Python 3: json.JSONDecodeError
            raise MKUserError("params", _("Invalid parameters: %s") % e)

        value = html.request.var("value")
=======
        params = request.get("params")
        if params is None:
            raise MKUserError("params", _("You need to set the \"%s\" parameter.") % "params")

        value = request.get("value")
>>>>>>> upstream/master
        if value is None:
            raise MKUserError("params", _("You need to set the \"%s\" parameter.") % "value")

        result_data = cls.idents()[ident].autocomplete_choices(value, params)

        # Check for correct result_data format
        assert isinstance(result_data, list)
        if result_data:
            assert isinstance(result_data[0], (list, tuple))
            assert len(result_data[0]) == 2

<<<<<<< HEAD
        html.write(json.dumps(result_data))

    #@abc.abstractclassmethod
    @classmethod
    def autocomplete_choices(cls, value, params):
=======
        return result_data

    #@abc.abstractclassmethod
    @classmethod
    def autocomplete_choices(cls, value: str, params: Dict) -> Choices:
>>>>>>> upstream/master
        raise NotImplementedError()


# TODO: Cleanup kwargs
class MonitoredHostname(TextAsciiAutocomplete):
    """Hostname input with dropdown completion

    Renders an input field for entering a host name while providing an auto completion dropdown field.
    Fetching the choices from the current live config via livestatus"""
    ident = "monitored_hostname"

    def __init__(self, **kwargs):
<<<<<<< HEAD
        super(MonitoredHostname, self).__init__(completion_ident=self.ident,
                                                completion_params={},
                                                **kwargs)

    @classmethod
    def autocomplete_choices(cls, value, params):
        """Return the matching list of dropdown choices
        Called by the webservice with the current input field value and the completions_params to get the list of choices"""
        import cmk.gui.sites as sites

        query = ("GET hosts\n"
                 "Columns: host_name\n"
                 "Filter: host_name ~~ %s" % livestatus.lqencode(value))
=======
        super().__init__(completion_ident=self.ident, completion_params={}, **kwargs)

    @classmethod
    def autocomplete_choices(cls, value: str, params: Dict) -> Choices:
        """Return the matching list of dropdown choices
        Called by the webservice with the current input field value and the completions_params to get the list of choices"""
        query = ("GET hosts\n"
                 "Columns: host_name\n"
                 "Filter: host_name ~~ %s" % livestatus.lqencode(value))

>>>>>>> upstream/master
        hosts = sorted(sites.live().query_column_unique(query))

        return [(h, h) for h in hosts]


@page_registry.register_page("ajax_vs_autocomplete")
<<<<<<< HEAD
class PageVsAutocomplete(Page):
    def page(self):
        # TODO: Move ajax_handler to this class? Should we also move the autocomplete_choices()?
        TextAsciiAutocomplete.ajax_handler()


# TODO: Cleanup kwargs
def Hostname(allow_empty=False, **kwargs):
    """A host name with or without domain part. Also allow IP addresses"""
    return TextAscii(regex=re.compile('^[-0-9a-zA-Z_.]+$'),
                     regex_error=_("Please enter a valid hostname or IPv4 address. "
                                   "Only letters, digits, dash, underscore and dot are allowed."),
                     **kwargs)
=======
class PageVsAutocomplete(AjaxPage):
    def page(self):
        # TODO: Move ajax_handler to this class? Should we also move the autocomplete_choices()?
        return {"choices": TextAsciiAutocomplete.ajax_handler(self.webapi_request())}


def Hostname(  # pylint: disable=redefined-builtin
    # TextAscii
    allow_empty=False,
    # ValueSpec
    title: _Optional[str] = None,
    help: _Optional[ValueSpecHelp] = None,
    default_value: Any = DEF_VALUE,
):
    """A host name with or without domain part. Also allow IP addresses"""
    return TextAscii(
        regex=cmk.utils.regex.regex(cmk.utils.regex.REGEX_HOST_NAME),
        regex_error=_("Please enter a valid hostname or IPv4 address. "
                      "Only letters, digits, dash, underscore and dot are allowed."),
        allow_empty=allow_empty,
        title=title,
        help=help,
        default_value=default_value,
    )
>>>>>>> upstream/master


class HostAddress(TextAscii):
    """Use this for all host / ip address input fields!"""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            allow_host_name=True,  # type: bool
            allow_ipv4_address=True,  # type: bool
            allow_ipv6_address=True,  # type: bool
            # TextAscii
            label=None,  # type: TypingOptional[Text]
            size=64,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex=None,  # type: TypingOptional[Union[str, Pattern[str]]]
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            autocomplete=True,  # type: bool
            hidden=False,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(HostAddress, self).__init__(
=======
        self,
        allow_host_name: bool = True,
        allow_ipv4_address: bool = True,
        allow_ipv6_address: bool = True,
        # TextAscii
        label: _Optional[str] = None,
        size: Union[int, str] = 64,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex: Union[None, str, Pattern[str]] = None,
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        autocomplete: bool = True,
        hidden: bool = False,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
>>>>>>> upstream/master
            label=label,
            size=size,
            try_max_width=try_max_width,
            cssclass=cssclass,
            strip=strip,
            attrencode=attrencode,
            allow_empty=allow_empty,
            empty_text=empty_text,
            read_only=read_only,
<<<<<<< HEAD
            none_is_empty=none_is_empty,
=======
>>>>>>> upstream/master
            forbidden_chars=forbidden_chars,
            regex=regex,
            regex_error=regex_error,
            minlen=minlen,
            onkeyup=onkeyup,
            autocomplete=autocomplete,
            hidden=hidden,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
        self._allow_host_name = allow_host_name
        self._allow_ipv4_address = allow_ipv4_address
        self._allow_ipv6_address = allow_ipv6_address

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
=======
    def _validate_value(self, value: str, varprefix: str) -> None:
>>>>>>> upstream/master
        if value and self._allow_host_name and self._is_valid_host_name(value):
            pass
        elif value and self._allow_ipv4_address and self._is_valid_ipv4_address(value):
            pass
        elif value and self._allow_ipv6_address and self._is_valid_ipv6_address(value):
            pass
        elif not self._allow_empty:
            raise MKUserError(
                varprefix,
                _("Invalid host address. You need to specify the address "
                  "either as %s.") % ", ".join(self._allowed_type_names()))

<<<<<<< HEAD
    def _is_valid_host_name(self, hostname):
=======
    def _is_valid_host_name(self, hostname: str) -> bool:
>>>>>>> upstream/master
        # http://stackoverflow.com/questions/2532053/validate-a-hostname-string/2532344#2532344
        if len(hostname) > 255:
            return False

        if hostname[-1] == ".":
            hostname = hostname[:-1]  # strip exactly one dot from the right, if present

        # must be not all-numeric, so that it can't be confused with an IPv4 address.
        # Host names may start with numbers (RFC 1123 section 2.1) but never the final part,
        # since TLDs are alphabetic.
        if re.match(r"[\d.]+$", hostname):
            return False

        allowed = re.compile(r"(?!-)[A-Z_\d-]{1,63}(?<!-)$", re.IGNORECASE)
        return all(allowed.match(x) for x in hostname.split("."))

<<<<<<< HEAD
    def _is_valid_ipv4_address(self, address):
=======
    def _is_valid_ipv4_address(self, address: str) -> bool:
>>>>>>> upstream/master
        # http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python/4017219#4017219
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False

            return address.count('.') == 3

        except socket.error:  # not a valid address
            return False

        return True

<<<<<<< HEAD
    def _is_valid_ipv6_address(self, address):
=======
    def _is_valid_ipv6_address(self, address: str) -> bool:
>>>>>>> upstream/master
        # http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python/4017219#4017219
        try:
            address = address.split('%')[0]
            socket.inet_pton(socket.AF_INET6, address)
        except socket.error:  # not a valid address
            return False
        return True

<<<<<<< HEAD
    def _allowed_type_names(self):
        allowed = []
=======
    def _allowed_type_names(self) -> List[str]:
        allowed: List[str] = []
>>>>>>> upstream/master
        if self._allow_host_name:
            allowed.append(_("Host- or DNS name"))

        if self._allow_ipv4_address:
            allowed.append(_("IPv4 address"))

        if self._allow_ipv6_address:
            allowed.append(_("IPv6 address"))

        return allowed


<<<<<<< HEAD
# TODO: Cleanup kwargs
def AbsoluteDirname(**kwargs):
    return TextAscii(
        regex=re.compile('^(/|(/[^/]+)+)$'),
        regex_error=_("Please enter a valid absolut pathname with / as a path separator."),
        **kwargs)
=======
def AbsoluteDirname(  # pylint: disable=redefined-builtin
    # TextAscii
    allow_empty: bool = True,
    size: Union[int, str] = 25,
    # ValueSpec
    title: _Optional[str] = None,
    help: _Optional[ValueSpecHelp] = None,
    default_value: Any = DEF_VALUE,
    validate: _Optional[ValueSpecValidateFunc] = None,
) -> TextAscii:
    return TextAscii(
        regex=re.compile('^(/|(/[^/]+)+)$'),
        regex_error=_("Please enter a valid absolut pathname with / as a path separator."),
        allow_empty=allow_empty,
        size=size,
        title=title,
        help=help,
        default_value=default_value,
        validate=validate,
    )
>>>>>>> upstream/master


class Url(TextAscii):
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            default_scheme,  # type: Text
            allowed_schemes,  # type: List[Text]
            show_as_link=False,  # type: bool
            target=None,  # type: TypingOptional[Text]
            # TextAscii
            label=None,  # type: TypingOptional[Text]
            size=64,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex=None,  # type: TypingOptional[Union[str, Pattern[str]]]
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            autocomplete=True,  # type: bool
            hidden=False,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Url, self).__init__(
=======
        self,
        default_scheme: str,
        allowed_schemes: List[str],
        show_as_link: bool = False,
        target: _Optional[str] = None,
        # TextAscii
        label: _Optional[str] = None,
        size: Union[int, str] = 64,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex: Union[None, str, Pattern[str]] = None,
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        autocomplete: bool = True,
        hidden: bool = False,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
>>>>>>> upstream/master
            label=label,
            size=size,
            try_max_width=try_max_width,
            cssclass=cssclass,
            strip=strip,
            attrencode=attrencode,
            allow_empty=allow_empty,
            empty_text=empty_text,
            read_only=read_only,
<<<<<<< HEAD
            none_is_empty=none_is_empty,
=======
>>>>>>> upstream/master
            forbidden_chars=forbidden_chars,
            regex=regex,
            regex_error=regex_error,
            minlen=minlen,
            onkeyup=onkeyup,
            autocomplete=autocomplete,
            hidden=hidden,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
        self._default_scheme = default_scheme
        self._allowed_schemes = allowed_schemes
        self._show_as_link = show_as_link
        self._link_target = target

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
        super(Url, self)._validate_value(value, varprefix)

        if self._allow_empty and value == "":
            self._custom_validate(value, varprefix)
            return

        parts = urlparse.urlparse(value)
=======
    def _validate_value(self, value: str, varprefix: str) -> None:
        assert value is not None
        super()._validate_value(value, varprefix)

        if self._allow_empty and value == "":
            return

        parts = urllib.parse.urlparse(value)
>>>>>>> upstream/master
        if not parts.scheme or not parts.netloc:
            raise MKUserError(varprefix, _("Invalid URL given"))

        if parts.scheme not in self._allowed_schemes:
            raise MKUserError(
                varprefix,
                _("Invalid URL scheme. Must be one of: %s") % ", ".join(self._allowed_schemes))

<<<<<<< HEAD
    def from_html_vars(self, varprefix):
        value = super(Url, self).from_html_vars(varprefix)
=======
    def from_html_vars(self, varprefix: str) -> str:
        value = super().from_html_vars(varprefix)
>>>>>>> upstream/master
        if value and "://" not in value:
            value = self._default_scheme + "://" + value
        return value

<<<<<<< HEAD
    def value_to_text(self, value):
=======
    def value_to_text(self, value: str) -> str:
>>>>>>> upstream/master
        if not any(value.startswith(scheme + "://") for scheme in self._allowed_schemes):
            value = self._default_scheme + "://" + value

        try:
<<<<<<< HEAD
            parts = urlparse.urlparse(value)
=======
            parts = urllib.parse.urlparse(value)
>>>>>>> upstream/master
            if parts.path in ['', '/']:
                text = parts.netloc
            else:
                text = parts.netloc + parts.path
        except Exception:
            text = value[7:]

        # Remove trailing / if the url does not contain any path component
        if self._show_as_link:
<<<<<<< HEAD
            return html.render_a(text,
                                 href=value,
                                 target=self._link_target if self._link_target else None)
=======
            return u"%s" % html.render_a(
                text, href=value, target=self._link_target if self._link_target else None)
>>>>>>> upstream/master

        return value


<<<<<<< HEAD
# TODO: cleanup kwargs
def HTTPUrl(show_as_link=True, **kwargs):
    """Valuespec for a HTTP or HTTPS Url, that automatically adds http:// to the value if no scheme has been specified"""
    return Url(allowed_schemes=["http", "https"],
               default_scheme="http",
               show_as_link=show_as_link,
               **kwargs)


# TODO: cleanup kwargs
def CheckMKVersion(**kwargs):
    return TextAscii(regex=r"[0-9]+\.[0-9]+\.[0-9]+([bpi][0-9]+|i[0-9]+p[0-9]+)?$",
                     regex_error=_("This is not a valid Checkmk version number"),
                     **kwargs)
=======
def HTTPUrl(  # pylint: disable=redefined-builtin
    show_as_link: bool = True,
    # Url
    regex: Union[None, str, Pattern[str]] = None,
    regex_error: _Optional[str] = None,
    # TextAscii
    allow_empty: bool = True,
    size: Union[int, str] = 80,
    # ValueSpec
    title: _Optional[str] = None,
    help: _Optional[ValueSpecHelp] = None,
    default_value: Any = DEF_VALUE,
):
    """Valuespec for a HTTP or HTTPS Url, that automatically adds http:// to the value if no scheme has been specified"""
    return Url(
        allowed_schemes=["http", "https"],
        default_scheme="http",
        regex=regex,
        regex_error=regex_error,
        show_as_link=show_as_link,
        allow_empty=allow_empty,
        size=size,
        title=title,
        help=help,
        default_value=default_value,
    )


def CheckMKVersion(
    # ValueSpec
    title: _Optional[str] = None,
    default_value: Any = DEF_VALUE,
):
    return TextAscii(
        regex=r"[0-9]+\.[0-9]+\.[0-9]+([bpi][0-9]+|i[0-9]+p[0-9]+)?$",
        regex_error=_("This is not a valid Checkmk version number"),
        title=title,
        default_value=default_value,
    )
>>>>>>> upstream/master


class TextAreaUnicode(TextUnicode):
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            cols=60,  # type: int
            rows=20,  # type: Union[int, Text]
            minrows=0,  # type: int
            monospaced=False,  # type: bool
            # TextAscii
            label=None,  # type: TypingOptional[Text]
            size=64,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex=None,  # type: TypingOptional[Union[str, Pattern[str]]]
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            autocomplete=True,  # type: bool
            hidden=False,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(TextAreaUnicode, self).__init__(
=======
        self,
        cols: int = 60,
        rows: Union[int, str] = 20,
        minrows: int = 0,
        monospaced: bool = False,
        # TextAscii
        label: _Optional[str] = None,
        size: Union[int, str] = 64,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex: Union[None, str, Pattern[str]] = None,
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        autocomplete: bool = True,
        hidden: bool = False,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
>>>>>>> upstream/master
            label=label,
            size=size,
            try_max_width=try_max_width,
            cssclass=cssclass,
            strip=strip,
            attrencode=attrencode,
            allow_empty=allow_empty,
            empty_text=empty_text,
            read_only=read_only,
<<<<<<< HEAD
            none_is_empty=none_is_empty,
=======
>>>>>>> upstream/master
            forbidden_chars=forbidden_chars,
            regex=regex,
            regex_error=regex_error,
            minlen=minlen,
            onkeyup=onkeyup,
            autocomplete=autocomplete,
            hidden=hidden,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
        self._cols = cols
        self._try_max_width = try_max_width
        self._rows = rows  # Allowed: "auto" -> Auto resizing
        self._minrows = minrows  # Minimum number of initial rows when "auto"
        self._monospaced = monospaced  # select TT font

<<<<<<< HEAD
    def value_to_text(self, value):
        if self._monospaced:
            # TODO: This is a workaround for a bug. This function needs to return str objects right now.
            return "%s" % html.render_pre(HTML(value), class_="ve_textarea")
        return html.attrencode(value).replace("\n", "<br>")

    def render_input(self, varprefix, value):
=======
    def value_to_text(self, value: str) -> str:
        if self._monospaced:
            # TODO: This is a workaround for a bug. This function needs to return str objects right now.
            return "%s" % html.render_pre(HTML(value), class_="ve_textarea")
        return escaping.escape_attribute(value).replace("\n", "<br>")

    # TODO: Once we switched to Python 3 we can merge the unicode and non unicode class
    def render_input(self, varprefix: str, value: str) -> None:  # type: ignore[override]
>>>>>>> upstream/master
        if value is None:
            value = ""  # should never happen, but avoids exception for invalid input
        if self._rows == "auto":
            func = 'cmk.valuespecs.textarea_resize(this);'
            attrs = {"onkeyup": func, "onmousedown": func, "onmouseup": func, "onmouseout": func}
            if html.request.has_var(varprefix):
<<<<<<< HEAD
                rows = len(html.request.var(varprefix).splitlines())
=======
                rows = len(self.from_html_vars(varprefix).splitlines())
>>>>>>> upstream/master
            else:
                rows = len(value.splitlines())
            rows = max(rows, self._minrows)
        else:
            attrs = {}
<<<<<<< HEAD
=======
            assert isinstance(self._rows, int)
>>>>>>> upstream/master
            rows = self._rows

        if self._monospaced:
            attrs["class"] = "tt"

        html.text_area(varprefix,
                       value,
                       rows=rows,
                       cols=self._cols,
<<<<<<< HEAD
                       attrs=attrs,
                       try_max_width=self._try_max_width)

    # Overridded because we do not want to strip() here and remove '\r'
    def from_html_vars(self, varprefix):
        text = html.get_unicode_input(varprefix, "").replace('\r', '')
=======
                       try_max_width=self._try_max_width,
                       **attrs)

    # Overridden because we do not want to strip() here and remove '\r'
    # TODO: Once we switched to Python 3 we can merge the unicode and non unicode class
    def from_html_vars(self, varprefix: str) -> str:  # type: ignore[override]
        text = html.request.get_unicode_input_mandatory(varprefix, "").replace('\r', '')
>>>>>>> upstream/master
        if text and not text.endswith("\n"):
            text += "\n"  # force newline at end
        return text


# TODO: Rename the valuespec here to ExistingFilename or somehting similar
# TODO: Change to factory?
class Filename(TextAscii):
    """A variant of TextAscii() that validates a path to a filename that lies in an existing directory."""

    # TODO: Cleanup default / default_value?
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            default="/tmp/foo",  # type: Text
            trans_func=None,  # type: TypingOptional[Callable[[Text], Text]]
            # TextAscii
            label=None,  # type: TypingOptional[Text]
            size=60,  # type: Union[int, str]
            try_max_width=False,  # type: bool
            cssclass="text",  # type: str
            strip=True,  # type: bool
            attrencode=True,  # type: bool
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            read_only=False,  # type: bool
            none_is_empty=False,  # type: bool
            forbidden_chars="",  # type: Text
            regex=None,  # type: TypingOptional[Union[str, Pattern[str]]]
            regex_error=None,  # type: TypingOptional[Text]
            minlen=None,  # type: TypingOptional[int]
            onkeyup=None,  # type: TypingOptional[Text]
            autocomplete=True,  # type: bool
            hidden=False,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Filename, self).__init__(
=======
        self,
        default: str = "/tmp/foo",
        trans_func: _Optional[Callable[[str], str]] = None,
        # TextAscii
        label: _Optional[str] = None,
        size: Union[int, str] = 60,
        try_max_width: bool = False,
        cssclass: str = "text",
        strip: bool = True,
        attrencode: bool = True,
        allow_empty: bool = True,
        empty_text: str = "",
        read_only: bool = False,
        forbidden_chars: str = "",
        regex: Union[None, str, Pattern[str]] = None,
        regex_error: _Optional[str] = None,
        minlen: _Optional[int] = None,
        onkeyup: _Optional[str] = None,
        autocomplete: bool = True,
        hidden: bool = False,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
>>>>>>> upstream/master
            label=label,
            size=size,
            try_max_width=try_max_width,
            cssclass=cssclass,
            strip=strip,
            attrencode=attrencode,
            allow_empty=allow_empty,
            empty_text=empty_text,
            read_only=read_only,
<<<<<<< HEAD
            none_is_empty=none_is_empty,
=======
>>>>>>> upstream/master
            forbidden_chars=forbidden_chars,
            regex=regex,
            regex_error=regex_error,
            minlen=minlen,
            onkeyup=onkeyup,
            autocomplete=autocomplete,
            hidden=hidden,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
        self._default_path = default
        self._trans_func = trans_func

<<<<<<< HEAD
    def canonical_value(self):
        return self._default_path

    def _validate_value(self, value, varprefix):
=======
    def canonical_value(self) -> str:
        return self._default_path

    def _validate_value(self, value: str, varprefix: str) -> None:
>>>>>>> upstream/master
        # The transformation function only changes the value for validation. This is
        # usually a function which is later also used within the code which uses
        # this variable to e.g. replace macros
        if self._trans_func:
            value = self._trans_func(value)

        if len(value) == 0:
            raise MKUserError(varprefix, _("Please enter a filename."))

        if value[0] != "/":
            raise MKUserError(
                varprefix,
                _("Sorry, only absolute filenames are allowed. "
                  "Your filename must begin with a slash."))
        if value[-1] == "/":
            raise MKUserError(varprefix, _("Your filename must not end with a slash."))

<<<<<<< HEAD
        directory = value.rsplit("/", 1)[0]
        if not os.path.isdir(directory):
=======
        directory = Path(value).parent
        if not directory.is_dir():
>>>>>>> upstream/master
            raise MKUserError(
                varprefix,
                _("The directory %s does not exist or is not a directory.") % directory)

        # Write permissions to the file cannot be checked here since we run with Apache
        # permissions and the file might be created with Nagios permissions (on OMD this
        # is the same, but for others not)


class ListOfStrings(ValueSpec):
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            # ListOfStrings
            valuespec=None,  # type: TypingOptional[ValueSpec]
            size=25,  # type: Union[str, int]
            orientation="vertical",  # type: Text
            allow_empty=True,  # type: bool
            empty_text="",  # type: Text
            max_entries=None,  # type: TypingOptional[int]
            separator="",  # type: Text
            split_on_paste=True,  # type: bool
            split_separators=";",  # type: Text
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(ListOfStrings, self).__init__(title=title,
                                            help=help,
                                            default_value=default_value,
                                            validate=validate)
=======
        self,
        # ListOfStrings
        valuespec: _Optional[ValueSpec] = None,
        size: Union[str, int] = 25,
        orientation: str = "vertical",
        allow_empty: bool = True,
        empty_text: str = "",
        max_entries: _Optional[int] = None,
        separator: str = "",
        split_on_paste: bool = True,
        split_separators: str = ";",
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master

        self._valuespec = valuespec if valuespec is not None else TextAscii(size=size)
        self._vertical = orientation == "vertical"
        self._allow_empty = allow_empty
        self._empty_text = empty_text
        self._max_entries = max_entries
        self._separator = separator  # in case of float

        self._split_on_paste = split_on_paste
        self._split_separators = split_separators

<<<<<<< HEAD
    def help(self):
        help_texts = [
            super(ListOfStrings, self).help(),
=======
    def help(self) -> Union[str, HTML, None]:
        help_texts = [
            super().help(),
>>>>>>> upstream/master
            self._valuespec.help(),
        ]

        if self._split_on_paste:
            help_texts.append(
                _("You may paste a text from your clipboard which contains several "
                  "parts separated by \"%s\" characters into the last input field. The text will "
                  "then be split by these separators and the single parts are added into dedicated "
                  "input fields.") % self._split_separators)

<<<<<<< HEAD
        return " ".join([t for t in help_texts if t])

    def render_input(self, varprefix, value):
=======
        return u" ".join(u"%s" % t for t in help_texts if t)

    def render_input(self, varprefix: str, value: List[str]) -> None:
>>>>>>> upstream/master
        # Form already submitted?
        if html.request.has_var(varprefix + "_0"):
            value = self.from_html_vars(varprefix)
            # Remove variables from URL, so that they do not appear
            # in hidden_fields()
            nr = 0
            while html.request.has_var(varprefix + "_%d" % nr):
                html.request.del_var(varprefix + "_%d" % nr)
                nr += 1

        class_ = ["listofstrings"]
        if self._vertical:
            class_.append("vertical")
        else:
            class_.append("horizontal")
        html.open_div(id_=varprefix, class_=class_)

<<<<<<< HEAD
        for nr, s in enumerate(value + [""]):
            html.open_div()
            self._valuespec.render_input(varprefix + "_%d" % nr, s)
            if self._vertical != "vertical" and self._separator:
=======
        elements: List[_Optional[str]] = []
        elements += value
        elements.append(None)
        for nr, s in enumerate(elements):
            html.open_div()
            self._valuespec.render_input(varprefix + "_%d" % nr, s)
            if not self._vertical and self._separator:
>>>>>>> upstream/master
                html.nbsp()
                html.write(self._separator)
                html.nbsp()
            html.close_div()
        html.close_div()
        html.div('', style="clear:left;")
        html.javascript("cmk.valuespecs.list_of_strings_init(%s, %s, %s);" %
                        (json.dumps(varprefix), json.dumps(
                            self._split_on_paste), json.dumps(self._split_separators)))

<<<<<<< HEAD
    def canonical_value(self):
        return []

    def value_to_text(self, value):
=======
    def canonical_value(self) -> List[str]:
        return []

    def value_to_text(self, value: List[str]) -> str:
>>>>>>> upstream/master
        if not value:
            return self._empty_text

        if self._vertical:
            # TODO: This is a workaround for a bug. This function needs to return str objects right now.
            s = [
                html.render_tr(html.render_td(HTML(self._valuespec.value_to_text(v))))
                for v in value
            ]
            return "%s" % html.render_table(HTML().join(s))
<<<<<<< HEAD
        return ", ".join([self._valuespec.value_to_text(v) for v in value])

    def from_html_vars(self, varprefix):
        value = []
=======
        return u", ".join([self._valuespec.value_to_text(v) for v in value])

    def from_html_vars(self, varprefix: str) -> List[str]:
        value: List[str] = []
>>>>>>> upstream/master
        nr = 0
        while True:
            varname = varprefix + "_%d" % nr
            if not html.request.has_var(varname):
                break
<<<<<<< HEAD
            if html.request.var(varname, "").strip():
=======
            if html.request.get_str_input_mandatory(varname, "").strip():
>>>>>>> upstream/master
                value.append(self._valuespec.from_html_vars(varname))
            nr += 1
        return value

<<<<<<< HEAD
    def validate_datatype(self, value, varprefix):
=======
    def validate_datatype(self, value: List[str], varprefix: str) -> None:
>>>>>>> upstream/master
        if not isinstance(value, list):
            raise MKUserError(
                varprefix,
                _("Expected data type is list, but your type is %s.") % _type_name(value))
        for nr, s in enumerate(value):
            self._valuespec.validate_datatype(s, varprefix + "_%d" % nr)

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
=======
    def _validate_value(self, value: List[str], varprefix: str) -> None:
>>>>>>> upstream/master
        if len(value) == 0 and not self._allow_empty:
            if self._empty_text:
                msg = self._empty_text
            else:
                msg = _("Please specify at least one value")
            raise MKUserError(varprefix + "_0", msg)

        if self._max_entries is not None and len(value) > self._max_entries:
            raise MKUserError(varprefix + "_%d" % self._max_entries,
                              _("You can specify at most %d entries") % self._max_entries)

        if self._valuespec:
            for nr, s in enumerate(value):
                self._valuespec.validate_value(s, varprefix + "_%d" % nr)


# TODO: Spread use of this valuespec
<<<<<<< HEAD
def NetworkPort(title, default_value=_DEF_VALUE):
    # type: (TypingOptional[Text], Union[object, int]) -> Integer
=======
def NetworkPort(title: _Optional[str], default_value: Union[object, int] = DEF_VALUE) -> Integer:
>>>>>>> upstream/master
    return Integer(
        title=title,
        minvalue=1,
        maxvalue=65535,
        default_value=default_value,
    )


<<<<<<< HEAD
def ListOfNetworkPorts(title, default_value):
    # type: (TypingOptional[Text], List[int]) -> ListOfStrings
=======
def ListOfNetworkPorts(title: _Optional[str], default_value: List[int]) -> ListOfStrings:
>>>>>>> upstream/master
    return ListOfStrings(
        valuespec=NetworkPort(title=_("Port")),
        title=title,
        orientation="horizontal",
        default_value=default_value,
    )


class ListOf(ValueSpec):
    """Generic list-of-valuespec ValueSpec with Javascript-based add/delete/move"""
    class Style(Enum):
        REGULAR = "regular"
        FLOATING = "floating"

    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            valuespec,  # type: ValueSpec
            magic="@!@",  # type: Text
            add_label=None,  # type: TypingOptional[Text]
            del_label=None,  # type: TypingOptional[Text]
            movable=True,  # type: bool
            style=None,  # type: TypingOptional[ListOf.Style]
            totext=None,  # type: TypingOptional[Text]
            text_if_empty=None,  # type: TypingOptional[Text]
            allow_empty=True,  # type: bool
            empty_text=None,  # type: TypingOptional[Text]
            sort_by=None,  # type: TypingOptional[int]
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(ListOf, self).__init__(title=title,
                                     help=help,
                                     default_value=default_value,
                                     validate=validate)
=======
        self,
        valuespec: ValueSpec,
        magic: str = "@!@",
        add_label: _Optional[str] = None,
        del_label: _Optional[str] = None,
        movable: bool = True,
        style: '_Optional[ListOf.Style]' = None,
        totext: _Optional[str] = None,
        text_if_empty: _Optional[str] = None,
        allow_empty: bool = True,
        empty_text: _Optional[str] = None,
        sort_by: _Optional[int] = None,
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._valuespec = valuespec
        self._magic = magic
        self._add_label = add_label if add_label else _("Add new element")
        self._del_label = del_label if del_label else _("Delete this entry")
        self._movable = movable
        self._style = style or ListOf.Style.REGULAR
        self._totext = totext  # pattern with option %d
        self._text_if_empty = text_if_empty if text_if_empty is not None else _("No entries")
        self._allow_empty = allow_empty
        self._empty_text = empty_text if empty_text is not None else \
            _("Please specify at least one entry")

        # Makes a sort button visible that can be used to sort the list in the GUI
        # (without submitting the form). But this currently only works for list of
        # tuples that contain input field elements directly. The value of sort_by
        # refers to the index of the sort values in the tuple
        self._sort_by = sort_by

    # Implementation idea: we render our element-valuespec
    # once in a hidden div that is not evaluated. All occurances
    # of a magic string are replaced with the actual number
    # of entry, while beginning with 1 (this makes visual
    # numbering in labels, etc. possible). The current number
    # of entries is stored in the hidden variable 'varprefix'
<<<<<<< HEAD
    def render_input(self, varprefix, value):
=======
    def render_input(self, varprefix: str, value: List[Any]) -> None:
>>>>>>> upstream/master
        html.open_div(class_=["valuespec_listof", self._style.value])

        # Beware: the 'value' is only the default value in case the form
        # has not yet been filled in. In the complain phase we must
        # ignore 'value' but reuse the input from the HTML variables -
        # even if they are not syntactically correct. Calling from_html_vars
        # here is *not* an option since this might not work in case of
        # a wrong user input.

        # Render reference element for cloning
        self._show_reference_entry(varprefix, self._magic, self._valuespec.default_value())

        # In the 'complain' phase, where the user already saved the
        # form but the validation failed, we must not display the
        # original 'value' but take the value from the HTML variables.
        if html.request.has_var("%s_count" % varprefix):
            count = len(self.get_indexes(varprefix))
            value = [None] * count  # dummy for the loop
        else:
            count = len(value)

        html.hidden_field('%s_count' % varprefix,
                          str(count),
                          id_='%s_count' % varprefix,
                          add_var=True)

        self._show_entries(varprefix, value)

        html.close_div()

        if count:
            html.javascript("cmk.valuespecs.listof_update_indices(%s)" % json.dumps(varprefix))

<<<<<<< HEAD
    def _show_entries(self, varprefix, value):
=======
    def _show_entries(self, varprefix: str, value: List[Any]) -> None:
>>>>>>> upstream/master
        if self._style == ListOf.Style.REGULAR:
            self._show_current_entries(varprefix, value)
            html.br()
            self._list_buttons(varprefix)

        elif self._style == ListOf.Style.FLOATING:
            html.open_table()
            html.open_tbody()
            html.open_tr()
            html.open_td()
            self._list_buttons(varprefix)
            html.close_td()
            html.open_td()
            self._show_current_entries(varprefix, value)
            html.close_td()
            html.close_tr()
            html.close_tbody()
            html.close_table()

        else:
            raise NotImplementedError()

<<<<<<< HEAD
    def _list_buttons(self, varprefix):
=======
    def _list_buttons(self, varprefix: str) -> None:
>>>>>>> upstream/master
        html.jsbutton(
            varprefix + "_add", self._add_label, "cmk.valuespecs.listof_add(%s, %s, %s)" %
            (json.dumps(varprefix), json.dumps(self._magic), json.dumps(self._style.value)))

        if self._sort_by is not None:
            html.jsbutton(
                varprefix + "_sort", _("Sort"), "cmk.valuespecs.listof_sort(%s, %s, %s)" %
                (json.dumps(varprefix), json.dumps(self._magic), json.dumps(self._sort_by)))

<<<<<<< HEAD
    def _show_reference_entry(self, varprefix, index, value):
=======
    def _show_reference_entry(self, varprefix: str, index: str, value: Any) -> None:
>>>>>>> upstream/master
        if self._style == ListOf.Style.REGULAR:
            html.open_table(style="display:none;")
            html.open_tbody(id_="%s_prototype" % varprefix, class_="vlof_prototype")

            self._show_entry(varprefix, index, value)

            html.close_tbody()
            html.close_table()

        elif self._style == ListOf.Style.FLOATING:
            html.open_div(id_="%s_prototype" % varprefix,
                          class_="vlof_prototype",
                          style="display:none;")

            self._show_entry(varprefix, index, value)

            html.close_div()

        else:
            raise NotImplementedError()

<<<<<<< HEAD
    def _show_current_entries(self, varprefix, value):
=======
    def _show_current_entries(self, varprefix: str, value: Any) -> None:
>>>>>>> upstream/master
        if self._style == ListOf.Style.REGULAR:
            html.open_table(class_=["valuespec_listof"])
            html.open_tbody(id_="%s_container" % varprefix)

            for nr, v in enumerate(value):
                self._show_entry(varprefix, "%d" % (nr + 1), v)

            html.close_tbody()
            html.close_table()

        elif self._style == ListOf.Style.FLOATING:
            html.open_div(id_="%s_container" % varprefix,
                          class_=["valuespec_listof_floating_container"])

            for nr, v in enumerate(value):
                self._show_entry(varprefix, "%d" % (nr + 1), v)

            html.close_div()

        else:
            raise NotImplementedError()

<<<<<<< HEAD
    def _show_entry(self, varprefix, index, value):
=======
    def _show_entry(self, varprefix: str, index: str, value: Any) -> None:
>>>>>>> upstream/master
        entry_id = "%s_entry_%s" % (varprefix, index)

        if self._style == ListOf.Style.REGULAR:
            html.open_tr(id_=entry_id)
            self._show_entry_cell(varprefix, index, value)
            html.close_tr()

        elif self._style == ListOf.Style.FLOATING:
            html.open_table(id_=entry_id)
            html.open_tbody()
            html.open_tr()
            self._show_entry_cell(varprefix, index, value)
            html.close_tr()
            html.close_tbody()
            html.close_table()

        else:
            raise NotImplementedError()

<<<<<<< HEAD
    def _show_entry_cell(self, varprefix, index, value):
=======
    def _show_entry_cell(self, varprefix: str, index: str, value: Any) -> None:
>>>>>>> upstream/master
        html.open_td(class_="vlof_buttons")

        html.hidden_field(varprefix + "_indexof_" + index, "", add_var=True,
                          class_="index")  # reconstruct order after moving stuff
        html.hidden_field(varprefix + "_orig_indexof_" + index,
                          "",
                          add_var=True,
                          class_="orig_index")
        if self._movable:
            html.element_dragger_js("tr",
                                    drop_handler="cmk.valuespecs.listof_drop_handler",
                                    handler_args={
                                        "cur_index": index,
                                        "varprefix": varprefix
                                    })
        self._del_button(varprefix, index)
        html.close_td()
        html.open_td(class_="vlof_content")
        self._valuespec.render_input(varprefix + "_" + index, value)
        html.close_td()

<<<<<<< HEAD
    def _del_button(self, vp, nr):
        js = "cmk.valuespecs.listof_delete(%s, %s)" % (json.dumps(vp), json.dumps(nr))
        html.icon_button("#", self._del_label, "delete", onclick=js)

    def canonical_value(self):
        return []

    def value_to_text(self, value):
=======
    def _del_button(self, vp: str, nr: str) -> None:
        js = "cmk.valuespecs.listof_delete(%s, %s)" % (json.dumps(vp), json.dumps(nr))
        html.icon_button("#", self._del_label, "close", onclick=js, class_="delete_button")

    def canonical_value(self) -> List[Any]:
        return []

    def value_to_text(self, value: List[Any]) -> str:
>>>>>>> upstream/master
        if self._totext:
            if "%d" in self._totext:
                return self._totext % len(value)
            return self._totext
<<<<<<< HEAD
        elif not value:
=======
        if not value:
>>>>>>> upstream/master
            return self._text_if_empty

        # TODO: This is a workaround for a bug. This function needs to return str objects right now.
        s = [html.render_tr(html.render_td(HTML(self._valuespec.value_to_text(v)))) for v in value]
        return "%s" % html.render_table(HTML().join(s))

<<<<<<< HEAD
    def get_indexes(self, varprefix):
        count = html.get_integer_input(varprefix + "_count", 0)
=======
    def get_indexes(self, varprefix: str) -> Dict[int, int]:
        count = html.request.get_integer_input_mandatory(varprefix + "_count", 0)
>>>>>>> upstream/master
        n = 1
        indexes = {}
        while n <= count:
            indexof = html.request.var(varprefix + "_indexof_%d" % n)
            # for deleted entries, we have removed the whole row, therefore indexof is None
            if indexof is not None:
                indexes[int(indexof)] = n
            n += 1
        return indexes

<<<<<<< HEAD
    def from_html_vars(self, varprefix):
=======
    def from_html_vars(self, varprefix: str) -> List[Any]:
>>>>>>> upstream/master
        indexes = self.get_indexes(varprefix)
        value = []
        k = sorted(indexes.keys())
        for i in k:
            val = self._valuespec.from_html_vars(varprefix + "_%d" % indexes[i])
            value.append(val)
        return value

<<<<<<< HEAD
    def validate_datatype(self, value, varprefix):
=======
    def validate_datatype(self, value: List[Any], varprefix: str) -> None:
>>>>>>> upstream/master
        if not isinstance(value, list):
            raise MKUserError(varprefix, _("The type must be list, but is %s") % _type_name(value))
        for n, v in enumerate(value):
            self._valuespec.validate_datatype(v, varprefix + "_%d" % (n + 1))

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
=======
    def _validate_value(self, value: List[Any], varprefix: str) -> None:
>>>>>>> upstream/master
        if not self._allow_empty and len(value) == 0:
            raise MKUserError(varprefix, self._empty_text)
        for n, v in enumerate(value):
            self._valuespec.validate_value(v, varprefix + "_%d" % (n + 1))


<<<<<<< HEAD
=======
ListOfMultipleChoices = List[_Tuple[str, ValueSpec]]

ListOfMultipleChoiceGroup = NamedTuple("ListOfMultipleChoiceGroup", [
    ("title", str),
    ("choices", ListOfMultipleChoices),
])

GroupedListOfMultipleChoices = List[ListOfMultipleChoiceGroup]


>>>>>>> upstream/master
class ListOfMultiple(ValueSpec):
    """A generic valuespec where the user can choose from a list of sub-valuespecs.
    Each sub-valuespec can be added only once
    """
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            choices,  # type: List[TypingTuple[str, Text]]
            choice_page_name,  # type: str
            page_request_vars=None,  # type: Dict[Text, Text]
            size=None,  # type: TypingOptional[int]
            add_label=None,  # type: TypingOptional[Text]
            del_label=None,  # type: TypingOptional[Text]
            delete_style="default",  # type: str
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(ListOfMultiple, self).__init__(title=title,
                                             help=help,
                                             default_value=default_value,
                                             validate=validate)
        self._choices = choices
        self._choice_dict = dict(choices)
=======
        self,
        choices: Union[GroupedListOfMultipleChoices, ListOfMultipleChoices],
        choice_page_name: str,
        page_request_vars: _Optional[Dict[str, Any]] = None,
        size: _Optional[int] = None,
        add_label: _Optional[str] = None,
        del_label: _Optional[str] = None,
        delete_style: str = "default",
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
        allow_empty: bool = True,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        # Normalize all to grouped choice structure
        grouped: GroupedListOfMultipleChoices = []
        ungrouped_group = ListOfMultipleChoiceGroup(title="", choices=[])
        grouped.append(ungrouped_group)
        for e in choices:
            if not isinstance(e, ListOfMultipleChoiceGroup):
                ungrouped_group.choices.append(e)
            else:
                grouped.append(e)

        self._grouped_choices = grouped
        self._choice_dict = {choice[0]: choice[1] for group in grouped for choice in group.choices}
>>>>>>> upstream/master
        self._choice_page_name = choice_page_name
        self._page_request_vars = page_request_vars or {}
        self._size = size
        self._add_label = add_label if add_label is not None else _("Add element")
        self._del_label = del_label if del_label is not None else _("Delete this entry")
        self._delete_style = delete_style  # or "filter"
<<<<<<< HEAD

    def del_button(self, varprefix, ident):
        js = "cmk.valuespecs.listofmultiple_del(%s, %s)" % (json.dumps(varprefix),
                                                            json.dumps(ident))
        html.icon_button("#", self._del_label, "delete", onclick=js)

    def render_input(self, varprefix, value):
=======
        self._allow_empty = allow_empty

    def del_button(self, varprefix: str, ident: str) -> None:
        js = "cmk.valuespecs.listofmultiple_del(%s, %s)" % (json.dumps(varprefix),
                                                            json.dumps(ident))
        html.icon_button("#", self._del_label, "close", onclick=js, class_="delete_button")

    def render_input(self, varprefix: str, value: Dict[str, Any]) -> None:
>>>>>>> upstream/master
        # Beware: the 'value' is only the default value in case the form
        # has not yet been filled in. In the complain phase we must
        # ignore 'value' but reuse the input from the HTML variables -
        # even if they are not syntactically correct. Calling from_html_vars
        # here is *not* an option since this might not work in case of
        # a wrong user input.

        # Special styling for filters
        extra_css = "filter" if self._delete_style == "filter" else None

        # In the 'complain' phase, where the user already saved the
        # form but the validation failed, we must not display the
        # original 'value' but take the value from the HTML variables.
        if html.request.var("%s_active" % varprefix):
            value = self.from_html_vars(varprefix)

<<<<<<< HEAD
        # Save all selected items
        html.hidden_field('%s_active' % varprefix,
                          ';'.join([k for k in value.keys() if k in self._choice_dict]),
=======
        sorted_idents: List[str] = []
        for group in self._grouped_choices:
            for ident, _vs in group.choices:
                if ident in value and ident in self._choice_dict:
                    sorted_idents.append(ident)

        # Save all selected items
        html.hidden_field('%s_active' % varprefix,
                          ';'.join(sorted_idents),
>>>>>>> upstream/master
                          id_='%s_active' % varprefix,
                          add_var=True)

        # Actual table of currently existing entries
        html.open_table(id_="%s_table" % varprefix, class_=["valuespec_listof", extra_css])
        html.open_tbody()

<<<<<<< HEAD
        for ident, vs in self._choices:
            if ident in value:
                self.show_choice_row(varprefix, ident, value)
=======
        for ident in sorted_idents:
            self.show_choice_row(varprefix, ident, value)
>>>>>>> upstream/master

        html.close_tbody()
        html.close_table()

<<<<<<< HEAD
        choices = [('', '')] + [(ident, vs.title()) for ident, vs in self._choices]
=======
        self._show_add_elements(varprefix)

    def _show_add_elements(self, varprefix: str) -> None:
        choices: GroupedChoices = [ChoiceGroup(title="", choices=[("", "")])]
        for group in self._grouped_choices:
            choices.append(
                ChoiceGroup(title=group.title,
                            choices=[(ident, vs.title() or "") for ident, vs in group.choices]))

>>>>>>> upstream/master
        html.dropdown(varprefix + '_choice',
                      choices,
                      style="width: %dex" % self._size if self._size is not None else None,
                      class_="vlof_filter" if self._delete_style == "filter" else None)
        html.javascript('cmk.valuespecs.listofmultiple_init(%s);' % json.dumps(varprefix))
        html.jsbutton(
<<<<<<< HEAD
            varprefix + '_add', self._add_label, "cmk.valuespecs.listofmultiple_add(%s, %s, %s)" %
            (json.dumps(varprefix), json.dumps(
                self._choice_page_name), json.dumps(self._page_request_vars)))

    def show_choice_row(self, varprefix, ident, value):
        prefix = varprefix + '_' + ident
        html.open_tr(id_="%s_row" % prefix)
        if self._delete_style == "filter":
            self._show_del_button(varprefix, ident)
            self._show_content(varprefix, ident, value)
        else:
            self._show_del_button(varprefix, ident)
            self._show_content(varprefix, ident, value)
        html.close_tr()

    def _show_content(self, varprefix, ident, value):
=======
            varprefix + '_add',
            self._add_label,
            "cmk.valuespecs.listofmultiple_add(%s, %s, %s)" % (
                json.dumps(varprefix),  #
                json.dumps(self._choice_page_name),
                json.dumps(self._page_request_vars)))

    def show_choice_row(self, varprefix: str, ident: str, value: Dict[str, Any]) -> None:
        prefix = varprefix + '_' + ident
        html.open_tr(id_="%s_row" % prefix)
        self._show_del_button(varprefix, ident)
        self._show_content(varprefix, ident, value)
        html.close_tr()

    def _show_content(self, varprefix: str, ident: str, value: Dict[str, Any]) -> None:
>>>>>>> upstream/master
        prefix = varprefix + '_' + ident
        html.open_td(class_=["vlof_content"])
        self._choice_dict[ident].render_input(prefix, value.get(ident))
        html.close_td()

<<<<<<< HEAD
    def _show_del_button(self, varprefix, ident):
=======
    def _show_del_button(self, varprefix: str, ident: str) -> None:
>>>>>>> upstream/master
        html.open_td(class_=["vlof_buttons"])
        self.del_button(varprefix, ident)
        html.close_td()

<<<<<<< HEAD
    def canonical_value(self):
        return {}

    def value_to_text(self, value):
        table_content = HTML()
        for ident, val in value:
            vs = self._choice_dict[ident]
            # TODO: This is a workaround for a bug. This function needs to return str objects right now.
            table_content += html.render_tr(html.render_td(vs.title())\
                                          + html.render_td(    HTML(vs.value_to_text(val))    ))
        return "%s" % html.render_table(table_content)

    def from_html_vars(self, varprefix):
        value = {}
        active = html.request.var('%s_active' % varprefix).strip()
=======
    def canonical_value(self) -> Dict[str, Any]:
        return {}

    def value_to_text(self, value: Dict[str, Any]) -> str:
        table_content = HTML()
        for ident, val in value.items():
            vs = self._choice_dict[ident]
            # TODO: This is a workaround for a bug. This function needs to return str objects right now.
            table_content += html.render_tr(
                html.render_td(vs.title()) + html.render_td(HTML(vs.value_to_text(val))))
        return "%s" % html.render_table(table_content)

    def from_html_vars(self, varprefix: str) -> Dict[str, Any]:
        value: Dict[str, Any] = {}
        active = html.request.get_str_input_mandatory('%s_active' % varprefix).strip()
>>>>>>> upstream/master
        if not active:
            return value

        for ident in active.split(';'):
            vs = self._choice_dict[ident]
            value[ident] = vs.from_html_vars(varprefix + '_' + ident)
        return value

<<<<<<< HEAD
    def validate_datatype(self, value, varprefix):
=======
    def validate_datatype(self, value: Dict[str, Any], varprefix: str) -> None:
>>>>>>> upstream/master
        if not isinstance(value, dict):
            raise MKUserError(varprefix, _("The type must be dict, but is %s") % _type_name(value))
        for ident, val in value.items():
            self._choice_dict[ident].validate_datatype(val, varprefix + '_' + ident)

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
=======
    def _validate_value(self, value: Dict[str, Any], varprefix: str) -> None:
        if not self._allow_empty and not value:
            raise MKUserError(varprefix, _('You must specify at least one element.'))
>>>>>>> upstream/master
        for ident, val in value.items():
            self._choice_dict[ident].validate_value(val, varprefix + '_' + ident)


<<<<<<< HEAD
class ABCPageListOfMultipleGetChoice(six.with_metaclass(abc.ABCMeta, AjaxPage)):
    @abc.abstractmethod
    def _get_choices(self, request):
        raise NotImplementedError()

    def page(self):
        request = html.get_request()
        vs = ListOfMultiple(self._get_choices(request), "unused_dummy_page")
        with html.plugged():
            vs.show_choice_row(request["varprefix"], request["ident"], {})
            return {"html_code": html.drain()}


class Float(Integer):
    """Same as Integer, but for floating point values"""
    def __init__(  # pylint: disable=redefined-builtin
            self,
            decimal_separator=".",  # type: Text
            allow_int=False,  # type: bool
            # Integer
            size=None,  # type: TypingOptional[int]
            minvalue=None,  # type: TypingOptional[Union[int, float]]
            maxvalue=None,  # type: TypingOptional[Union[int, float]]
            label=None,  # type: TypingOptional[Text]
            unit="",  # type: Text
            thousand_sep=None,  # type: TypingOptional[Text]
            display_format="%.2f",  # type: Text
            align="left",  # type: str
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Float, self).__init__(size=size,
                                    minvalue=minvalue,
                                    maxvalue=maxvalue,
                                    label=label,
                                    unit=unit,
                                    thousand_sep=thousand_sep,
                                    display_format=display_format,
                                    align=align,
                                    title=title,
                                    help=help,
                                    default_value=default_value,
                                    validate=validate)
        self._decimal_separator = decimal_separator
        self._allow_int = allow_int

    def _render_value(self, value):
        return self._display_format % utils.savefloat(value)

    def canonical_value(self):
        return float(Integer.canonical_value(self))

    def value_to_text(self, value):
        return super(Float, self).value_to_text(value).replace(".", self._decimal_separator)

    def from_html_vars(self, varprefix):
        try:
            return float(html.request.var(varprefix))
        except:
            raise MKUserError(
                varprefix,
                _("The text <b><tt>%s</tt></b> is not a valid floating point number.") %
                html.request.var(varprefix))

    def validate_datatype(self, value, varprefix):
        if isinstance(value, float):
            return

        if isinstance(value, numbers.Integral) and self._allow_int:
            return

=======
class ABCPageListOfMultipleGetChoice(AjaxPage, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _get_choices(self, request: Dict[str, str]) -> List[_Tuple[str, ValueSpec]]:
        raise NotImplementedError()

    def page(self) -> Dict:
        request = html.get_request()
        vs = ListOfMultiple(self._get_choices(request), "unused_dummy_page")
        with html.plugged():
            vs.show_choice_row(ensure_str(request["varprefix"]), ensure_str(request["ident"]), {})
            return {"html_code": html.drain()}


class Float(ValueSpec):
    """Same as Integer, but for floating point values"""
    def __init__(  # pylint: disable=redefined-builtin
        self,
        decimal_separator: str = ".",
        allow_int: bool = False,
        # Integer
        size: _Optional[int] = None,
        minvalue: _Optional[float] = None,
        maxvalue: _Optional[float] = None,
        label: _Optional[str] = None,
        unit: str = "",
        thousand_sep: _Optional[str] = None,
        display_format: str = "%.2f",
        align: str = "left",
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        self._bounds = Bounds[float](minvalue, maxvalue)
        self._renderer = NumericRenderer(size=size,
                                         maxvalue=maxvalue,
                                         label=label,
                                         unit=unit,
                                         thousand_sep=thousand_sep,
                                         align=align)
        self._display_format = display_format
        self._decimal_separator = decimal_separator
        self._allow_int = allow_int

    def canonical_value(self) -> float:
        return self._bounds.lower(0.0)

    def render_input(self, varprefix: str, value: float) -> None:
        self._renderer.render_input(varprefix, self._render_value(value))

    def _render_value(self, value: float) -> str:
        return self._display_format % utils.savefloat(value)

    def from_html_vars(self, varprefix: str) -> float:
        return html.request.get_float_input_mandatory(varprefix)

    def value_to_text(self, value: float) -> str:
        txt = self._renderer.format_text(self._render_value(value))
        return txt.replace(".", self._decimal_separator)

    def validate_datatype(self, value: float, varprefix: str) -> None:
        if isinstance(value, float):
            return
        if isinstance(value, numbers.Integral) and self._allow_int:
            return
>>>>>>> upstream/master
        raise MKUserError(
            varprefix,
            _("The value %r has type %s, but must be of type float%s") %
            (value, _type_name(value), _(" or int") if self._allow_int else ''))

<<<<<<< HEAD

class Percentage(Float):
    def __init__(  # pylint: disable=redefined-builtin
            self,
            # Float
            decimal_separator=".",  # type: Text
            allow_int=False,  # type: bool
            # Integer
            size=None,  # type: TypingOptional[int]
            minvalue=0.0,  # type: TypingOptional[Union[int, float]]
            maxvalue=101.0,  # type: TypingOptional[Union[int, float]]
            label=None,  # type: TypingOptional[Text]
            unit="%",  # type: Text
            thousand_sep=None,  # type: TypingOptional[Text]
            display_format="%.1f",  # type: Text
            align="left",  # type: str
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Percentage, self).__init__(decimal_separator=decimal_separator,
                                         allow_int=allow_int,
                                         size=size,
                                         minvalue=minvalue,
                                         maxvalue=maxvalue,
                                         label=label,
                                         unit=unit,
                                         thousand_sep=thousand_sep,
                                         display_format=display_format,
                                         align=align,
                                         title=title,
                                         help=help,
                                         default_value=default_value,
                                         validate=validate)

    def value_to_text(self, value):
        return (self._display_format + "%%") % value

    def validate_datatype(self, value, varprefix):
=======
    def validate_value(self, value: float, varprefix: str) -> None:
        self._bounds.validate_value(value, varprefix)


class Percentage(Float):
    def __init__(  # pylint: disable=redefined-builtin
        self,
        # Float
        decimal_separator: str = ".",
        allow_int: bool = False,
        # Integer
        size: _Optional[int] = None,
        minvalue: Union[None, int, float] = 0.0,
        maxvalue: Union[None, int, float] = 101.0,
        label: _Optional[str] = None,
        unit: str = "%",
        thousand_sep: _Optional[str] = None,
        display_format: str = "%.1f",
        align: str = "left",
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
            decimal_separator=decimal_separator,
            allow_int=allow_int,
            size=size,
            minvalue=minvalue,
            maxvalue=maxvalue,
            label=label,
            unit=unit,
            thousand_sep=thousand_sep,
            display_format=display_format,
            align=align,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )

    def value_to_text(self, value: float) -> str:
        return (self._display_format + "%%") % value

    def validate_datatype(self, value: float, varprefix: str) -> None:
>>>>>>> upstream/master
        if self._allow_int:
            if not isinstance(value, (int, float)):
                raise MKUserError(
                    varprefix,
                    _("The value %r has type %s, but must be either float or int") %
                    (value, _type_name(value)))
        else:
<<<<<<< HEAD
            super(Percentage, self).validate_datatype(value, varprefix)
=======
            super().validate_datatype(value, varprefix)
>>>>>>> upstream/master


class Checkbox(ValueSpec):
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            label=None,  # type: TypingOptional[Text]
            true_label=None,  # type: TypingOptional[Text]
            false_label=None,  # type: TypingOptional[Text]
            onclick=None,  # type: TypingOptional[Text]
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Checkbox, self).__init__(title=title,
                                       help=help,
                                       default_value=default_value,
                                       validate=validate)
=======
        self,
        label: _Optional[str] = None,
        true_label: _Optional[str] = None,
        false_label: _Optional[str] = None,
        onclick: _Optional[str] = None,
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._label = label
        self._true_label = true_label if true_label is not None else _("on")
        self._false_label = false_label if false_label is not None else _("off")
        self._onclick = onclick

<<<<<<< HEAD
    def canonical_value(self):
        return False

    def render_input(self, varprefix, value):
        html.checkbox(varprefix, value, label=self._label, onclick=self._onclick)

    def value_to_text(self, value):
        return self._true_label if value else self._false_label

    def from_html_vars(self, varprefix):
        return bool(html.request.var(varprefix))

    def validate_datatype(self, value, varprefix):
=======
    def canonical_value(self) -> bool:
        return False

    def render_input(self, varprefix: str, value: bool) -> None:
        html.checkbox(varprefix, value, label=self._label, onclick=self._onclick)

    def value_to_text(self, value: bool) -> str:
        return self._true_label if value else self._false_label

    def value_to_json(self, value):
        return value

    def value_from_json(self, json_value):
        return json_value

    def from_html_vars(self, varprefix: str) -> bool:
        return bool(html.request.var(varprefix))

    def validate_datatype(self, value: bool, varprefix: str) -> None:
>>>>>>> upstream/master
        if not isinstance(value, bool):
            raise MKUserError(
                varprefix,
                _("The value %r has type %s, but must be of type bool") %
                (value, _type_name(value)))


<<<<<<< HEAD
class DropdownChoice(ValueSpec):
    """A type-save dropdown choice
=======
DropdownChoiceValue = Any  # TODO: Can we be more specific?
DropdownChoiceEntry = _Tuple[DropdownChoiceValue, str]
DropdownChoices = Union[List[DropdownChoiceEntry], Callable[[], List[DropdownChoiceEntry]]]


class DropdownChoice(ValueSpec):
    """A type-safe dropdown choice
>>>>>>> upstream/master

    Parameters:
    help_separator: if you set this to a character, e.g. "-", then
    value_to_text will omit texts from the character up to the end of
    a choices name.
<<<<<<< HEAD
    Note: The list of choices may contain 2-tuples or 3-tuples.
    The format is (value, text {, icon} )
=======
>>>>>>> upstream/master
    choices may also be a function that returns - when called
    without arguments - such a tuple list. That way the choices
    can by dynamically computed"""

    # TODO: Cleanup redefined builtin sorted
    def __init__(  # pylint: disable=redefined-builtin
            self,
            # DropdownChoice
<<<<<<< HEAD
            choices,  # type: Union[List[TypingTuple[Any, Text]], Callable[[], List[TypingTuple[Any, Text]]]]
            sorted=False,  # type: bool
            label=None,  # type: TypingOptional[Text]
            help_separator=None,  # type: Text
            prefix_values=False,  # type: bool
            empty_text=None,  # type: TypingOptional[Text]
            invalid_choice="complain",  # type: TypingOptional[str]
            invalid_choice_title=None,  # type: TypingOptional[Text]
            invalid_choice_error=None,  # type: TypingOptional[Text]
            no_preselect=False,  # type: bool
            no_preselect_value=None,  # type: Any
            no_preselect_title="",  # type: Text
            no_preselect_error=None,  # type: Text
            on_change=None,  # type: Text
            read_only=False,  # type: bool
            encode_value=True,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(DropdownChoice, self).__init__(title=title,
                                             help=help,
                                             default_value=default_value,
                                             validate=validate)
=======
            choices: DropdownChoices,
            sorted: bool = False,
            label: _Optional[str] = None,
            help_separator: _Optional[str] = None,
            prefix_values: bool = False,
            empty_text: _Optional[str] = None,
            invalid_choice: _Optional[str] = "complain",
            invalid_choice_title: _Optional[str] = None,
            invalid_choice_error: _Optional[str] = None,
            no_preselect: bool = False,
            no_preselect_value: Any = None,
            no_preselect_title: str = "",
            no_preselect_error: _Optional[str] = None,
            on_change: _Optional[str] = None,
            read_only: bool = False,
            encode_value: bool = True,
            # ValueSpec
            title: _Optional[str] = None,
            help: _Optional[ValueSpecHelp] = None,
            default_value: Any = DEF_VALUE,
            validate: _Optional[ValueSpecValidateFunc] = None,
            deprecated_choices: Sequence[DropdownChoiceValue] = (),
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._choices = choices
        self._help_separator = help_separator
        self._label = label
        self._prefix_values = prefix_values
        self._sorted = sorted
<<<<<<< HEAD
        self._empty_text = empty_text if empty_text is not None else \
            _("There are no elements defined for this selection yet.")
        self._invalid_choice = invalid_choice
        self._invalid_choice_title = invalid_choice_title if invalid_choice_title is not None else \
            _("Element '%r' does not exist anymore")
        self._invalid_choice_error = invalid_choice_error if invalid_choice_error is not None else \
            _("The selected element is not longer available. Please select something else.")
        self._no_preselect = no_preselect
        self._no_preselect_value = no_preselect_value
        self._no_preselect_title = no_preselect_title
        self._no_preselect_error = no_preselect_error if no_preselect_error is not None else \
            _("Please make a selection")
        self._on_change = on_change
        self._read_only = read_only
        self._encode_value = encode_value

    def choices(self):
        # type: () -> List[TypingTuple[Any, Text]]
        result = []  # type: List[TypingTuple[Any, Text]]
        if isinstance(self._choices, list):
            result = self._choices
        elif isinstance(self._choices, dict):
            result = ListChoice.dict_choices(self._choices)
        else:
            result = self._choices()

=======
        self._empty_text = (empty_text if empty_text is not None else
                            _("There are no elements defined for this selection yet."))
        self._invalid_choice = invalid_choice
        self._invalid_choice_title = (invalid_choice_title if invalid_choice_title is not None else
                                      _("Element '%r' does not exist anymore"))
        self._invalid_choice_error = (
            invalid_choice_error if invalid_choice_error is not None else
            _("The selected element '%r' is not longer available. Please select something else."))
        self._no_preselect = no_preselect
        self._no_preselect_value = no_preselect_value
        self._no_preselect_title = no_preselect_title
        self._no_preselect_error = (no_preselect_error if no_preselect_error is not None else
                                    _("Please make a selection"))
        self._on_change = on_change
        self._read_only = read_only
        self._encode_value = encode_value
        self._deprecated_choices = deprecated_choices

    def choices(self) -> List[DropdownChoiceEntry]:
        if callable(self._choices):
            result = self._choices()
        else:
            result = self._choices
>>>>>>> upstream/master
        if self._no_preselect:
            return [(self._no_preselect_value, self._no_preselect_title)] + result
        return result

<<<<<<< HEAD
    def canonical_value(self):
=======
    def canonical_value(self) -> DropdownChoiceValue:
>>>>>>> upstream/master
        choices = self.choices()
        if len(choices) > 0:
            return choices[0][0]
        return None

<<<<<<< HEAD
    def render_input(self, varprefix, value):
=======
    def render_input(self, varprefix: str, value: DropdownChoiceValue) -> None:
>>>>>>> upstream/master
        if self._label:
            html.write("%s " % self._label)

        choices = self.choices()
<<<<<<< HEAD

        defval = choices[0][0] if choices else None
        options = []
        for entry in self.choices():
=======
        defval = choices[0][0] if choices else None
        options = []
        for entry in choices:
>>>>>>> upstream/master
            if self._prefix_values:
                entry = (entry[0], "%s - %s" % entry)

            options.append(entry)
            if entry[0] == value:
                defval = entry[0]

        # In complain mode: Use the value received from the HTML variable
        if self._invalid_choice == "complain" and value is not None and self._value_is_invalid(
                value):
            defval = value
<<<<<<< HEAD
            options.append((defval, self._get_invalid_choice_title(value)))
=======
            options.append((defval, self._get_invalid_choice_text(self._invalid_choice_title,
                                                                  value)))
>>>>>>> upstream/master

        if value is None and not options:
            html.write(self._empty_text)
            return

        if len(options) == 0:
            html.write(self._empty_text)
<<<<<<< HEAD
        elif len(options[0]) == 3:
            html.icon_dropdown(varprefix,
                               self._options_for_html(options),
                               deflt=self._option_for_html(defval))
        else:
            html.dropdown(varprefix,
                          self._options_for_html(options),
                          deflt=self._option_for_html(defval),
                          onchange=self._on_change,
                          ordered=self._sorted,
                          read_only=self._read_only)

    def _get_invalid_choice_title(self, value):
        if "%s" in self._invalid_choice_title or "%r" in self._invalid_choice_title:
            return self._invalid_choice_title % (value,)
        return self._invalid_choice_title

    def value_to_text(self, value):
        for entry in self.choices():
            val, title = entry[:2]
            if value == val:
                if self._help_separator:
                    return html.attrencode(title.split(self._help_separator, 1)[0].strip())
                return html.attrencode(title)
        return html.attrencode(self._get_invalid_choice_title(value))

    def from_html_vars(self, varprefix):
        choices = self.choices()

        for entry in choices:
            val, _title = entry[:2]
=======
            return

        html.dropdown(varprefix,
                      self._options_for_html(options),
                      deflt=self._option_for_html(defval),
                      onchange=self._on_change,
                      ordered=self._sorted,
                      read_only=self._read_only)

    def validate_datatype(self, value: Any, varprefix: str) -> None:
        if any(isinstance(value, type(choice[0]))
               for choice in self.choices()) or value in self._deprecated_choices:
            return
        raise MKUserError(
            varprefix,
            _("The value %r has type %s, but does not match any of the available choice types.") %
            (value, _type_name(value)))

    def _get_invalid_choice_text(self, tmpl: str, value: DropdownChoiceValue) -> str:
        if "%s" in tmpl or "%r" in tmpl:
            return tmpl % (value,)
        return tmpl

    def value_to_text(self, value: DropdownChoiceValue) -> str:
        for val, title in self.choices():
            if value == val:
                if self._help_separator:
                    return escaping.escape_attribute(
                        title.split(self._help_separator, 1)[0].strip())
                return escaping.escape_attribute(title)
        return escaping.escape_attribute(
            self._get_invalid_choice_text(self._invalid_choice_title, value))

    def value_to_json(self, value):
        return value

    def value_from_json(self, json_value):
        return json_value

    def from_html_vars(self, varprefix: str) -> DropdownChoiceValue:
        choices = self.choices()

        for val, _title in choices:
>>>>>>> upstream/master
            if self._is_selected_option_from_html(varprefix, val):
                return val

        if self._invalid_choice == "replace":
            return self.default_value()  # garbled URL or len(choices) == 0
<<<<<<< HEAD
        elif not choices:
            raise MKUserError(varprefix, self._empty_text)
        else:
            raise MKUserError(varprefix, self._invalid_choice_error)

    def _is_selected_option_from_html(self, varprefix, val):
        selected_value = html.request.var(varprefix)
        return selected_value == self._option_for_html(val)

    def _option_for_html(self, value):
=======
        if not choices:
            raise MKUserError(varprefix, self._empty_text)
        raise MKUserError(
            varprefix,
            self._get_invalid_choice_text(self._invalid_choice_error, html.request.var(varprefix)))

    def _is_selected_option_from_html(self, varprefix: str, val: DropdownChoiceValue) -> bool:
        selected_value = html.request.var(varprefix)
        return selected_value == self._option_for_html(val)

    def _option_for_html(self, value: DropdownChoiceValue) -> DropdownChoiceValue:
>>>>>>> upstream/master
        if self._encode_value:
            return self.option_id(value)
        return value

<<<<<<< HEAD
    def _options_for_html(self, orig_options):
        options = []
        for val, title in orig_options:
            options.append((self._option_for_html(val), title))
        return options

    @staticmethod
    def option_id(val):
        return "%s" % hashlib.sha256(repr(val)).hexdigest()

    def _validate_value(self, value, varprefix):
=======
    def _options_for_html(
            self,
            orig_options: List[DropdownChoiceEntry]) -> List[_Tuple[DropdownChoiceValue, str]]:
        return [(self._option_for_html(val), title) for val, title in orig_options]

    @staticmethod
    def option_id(val) -> str:
        return "%s" % hashlib.sha256(ensure_binary(repr(val))).hexdigest()

    def _validate_value(self, value: DropdownChoiceValue, varprefix: str) -> None:
>>>>>>> upstream/master
        if self._no_preselect and value == self._no_preselect_value:
            raise MKUserError(varprefix, self._no_preselect_error)

        if self._invalid_choice == "complain" and self._value_is_invalid(value):
            if value is not None:
                raise MKUserError(varprefix, self._invalid_choice_error)
<<<<<<< HEAD
            else:
                raise MKUserError(varprefix, self._empty_text)

    def _value_is_invalid(self, value):
        for entry in self.choices():
            if entry[0] == value:
                return False
        return True
=======
            raise MKUserError(varprefix, self._empty_text)

    def _value_is_invalid(self, value: DropdownChoiceValue) -> bool:
        return all(value != val for val, _title in self.choices())
>>>>>>> upstream/master


# TODO: Rename to ServiceState() or something like this
def MonitoringState(**kwargs):
    """Special convenience variant for monitoring states"""
    kwargs.setdefault("default_value", 0)
    return DropdownChoice(choices=[
        (0, _("OK")),
        (1, _("WARN")),
        (2, _("CRIT")),
        (3, _("UNKNOWN")),
    ],
                          **kwargs)


def HostState(**kwargs):
    kwargs.setdefault("default_value", 0)
    return DropdownChoice(choices=[
        (0, _("UP")),
        (1, _("DOWN")),
        (2, _("UNREACHABLE")),
    ], **kwargs)


<<<<<<< HEAD
=======
CascadingDropdownChoiceIdent = Union[None, str, bool, int]
CascadingDropdownChoiceValue = Union[CascadingDropdownChoiceIdent,
                                     _Tuple[CascadingDropdownChoiceIdent, Any]]
CascadingDropdownCleanChoice = _Tuple[CascadingDropdownChoiceIdent, str, _Optional[ValueSpec]]
CascadingDropdownShortChoice = _Tuple[CascadingDropdownChoiceIdent, str]
CascadingDropdownChoice = Union[CascadingDropdownShortChoice, CascadingDropdownCleanChoice]
CascadingDropdownChoices = Union[List[CascadingDropdownChoice],
                                 Callable[[], List[CascadingDropdownChoice]]]


def _normalize_choices(
        choices: List[CascadingDropdownChoice]) -> List[CascadingDropdownCleanChoice]:
    return [(c[0], c[1], _sub_valuespec(c)) for c in choices]


def _sub_valuespec(choice: CascadingDropdownChoice) -> _Optional[ValueSpec]:
    if len(choice) == 2:
        return None
    if len(choice) == 3:
        # NOTE: mypy is too dumb to figure out tuple lengths, so we use the funny "+ 0" below. Fragile...
        vs = choice[2 + 0]
        if vs is None or isinstance(vs, ValueSpec):
            return vs
    raise Exception("invalid CascadingDropdownChoice %r" % (choice,))


>>>>>>> upstream/master
class CascadingDropdown(ValueSpec):
    """A Dropdown choice where the elements are ValueSpecs.

    The currently selected ValueSpec will be displayed.  The text
    representations of the ValueSpecs will be used as texts.  A ValueSpec of
    None is also allowed and will return the value None. It is also allowed to
    leave out the value spec for some of the choices (which is the same as
    using None).

    The resulting value is either a single value (if no value spec is defined
    for the selected entry) or a pair of (x, y) where x is the value of the
    selected entry and y is the value of the valuespec assigned to that entry.
    choices is a list of triples: [ ( value, title, vs ), ... ]
    """
    class Render(Enum):
        normal = "normal"
        foldable = "foldable"

    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            # TODO: Make this more specific
            choices,  # type: Union[List[TypingTuple[Text, Text, ValueSpec]], Callable]
            label=None,  # type: TypingOptional[Text]
            separator=", ",  # type: TypingOptional[Text]
            sorted=True,  # type: bool
            orientation="vertical",  # type: Text
            render=None,  # type: TypingOptional[CascadingDropdown.Render]
            encoding="tuple",  # type: Text
            no_elements_text=None,  # type: TypingOptional[Text]
            no_preselect=False,  # type: bool
            no_preselect_value=None,  # type: TypingOptional[Any]
            no_preselect_title="",  # type: Text
            no_preselect_error=None,  # type: TypingOptional[Text]
            render_sub_vs_page_name=None,  # type: TypingOptional[Text]
            render_sub_vs_request_vars=None,  # type: TypingOptional[Dict]
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(CascadingDropdown, self).__init__(title=title,
                                                help=help,
                                                default_value=default_value,
                                                validate=validate)

        if isinstance(choices, list):
            self._choices = self.normalize_choices(choices)
        else:
            self._choices = choices  # function, store for later
=======
        self,
        choices: CascadingDropdownChoices,
        label: _Optional[str] = None,
        separator: str = ", ",
        sorted: bool = True,
        orientation: str = "vertical",
        render: '_Optional[CascadingDropdown.Render]' = None,
        no_elements_text: _Optional[str] = None,
        no_preselect: bool = False,
        no_preselect_value: _Optional[Any] = None,
        no_preselect_title: str = "",
        no_preselect_error: _Optional[str] = None,
        render_sub_vs_page_name: _Optional[str] = None,
        render_sub_vs_request_vars: _Optional[Dict] = None,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)

        if isinstance(choices, list):
            self._choices: Union[List[CascadingDropdownCleanChoice], Callable[
                [], List[CascadingDropdownChoice]]] = _normalize_choices(choices)
        else:
            # function, store for later
            self._choices = choices
>>>>>>> upstream/master

        self._label = label
        self._separator = separator
        self._sorted = sorted
        self._orientation = orientation  # or horizontal
        self._render = render if render is not None else CascadingDropdown.Render.normal
<<<<<<< HEAD
        self._encoding_type = list if encoding == "list" else tuple

        self._no_elements_text = no_elements_text if not no_elements_text is not None else \
            _("There are no elements defined for this selection")
=======

        self._no_elements_text = no_elements_text if no_elements_text is not None else _(
            "There are no elements defined for this selection")
>>>>>>> upstream/master

        self._no_preselect = no_preselect
        self._no_preselect_value = no_preselect_value
        self._no_preselect_title = no_preselect_title  # if not preselected
<<<<<<< HEAD
        self._no_preselect_error = no_preselect_error if no_preselect_error is not None else \
            _("Please make a selection")
=======
        self._no_preselect_error = no_preselect_error if no_preselect_error is not None else _(
            "Please make a selection")
>>>>>>> upstream/master

        # When given, this ajax page is called to render the input fields of a cascaded valuespec
        # once the user selected this choice in case it was initially hidden.
        self._render_sub_vs_page_name = render_sub_vs_page_name
        self._render_sub_vs_request_vars = render_sub_vs_request_vars or {}

<<<<<<< HEAD
    def normalize_choices(self, choices):
        new_choices = []
        for entry in choices:
            if len(entry) == 2:  # plain entry with no sub-valuespec
                entry = entry + (None,)  # normlize to three entries
            new_choices.append(entry)
        return new_choices

    def choices(self):
        if isinstance(self._choices, list):
            result = self._choices
        else:
            result = self.normalize_choices(self._choices())

        if self._no_preselect:
            result = [(self._no_preselect_value, self._no_preselect_title, None)] \
                     + result

        return result

    def canonical_value(self):
        choices = self.choices()
        if not choices:
            return None

        if choices[0][2]:
            return self._encoding_type((choices[0][0], choices[0][2].canonical_value()))
        return choices[0][0]

    def default_value(self):
=======
    def choices(self) -> List[CascadingDropdownCleanChoice]:
        if isinstance(self._choices, list):
            result: List[CascadingDropdownCleanChoice] = self._choices
        else:
            result = _normalize_choices(self._choices())

        if self._no_preselect:
            choice: CascadingDropdownCleanChoice = (self._no_preselect_value,
                                                    self._no_preselect_title, None)
            result = [choice] + result

        return result

    def canonical_value(self) -> CascadingDropdownChoiceValue:
        choices = self.choices()
        if not choices:
            return None
        first_choice: CascadingDropdownCleanChoice = choices[0]
        value: CascadingDropdownChoiceValue = first_choice[0]
        vs: _Optional[ValueSpec] = first_choice[2]
        if vs is None:
            return value
        # TODO: What should we do when we have a complex value *and* a ValueSpec?
        # We can't nest things arbitrarily deep, so we just return the first part.
        if isinstance(value, tuple):
            return value[0]
        return value, vs.canonical_value()

    def default_value(self) -> CascadingDropdownChoiceValue:
>>>>>>> upstream/master
        try:
            return self._default_value
        except Exception:
            choices = self.choices()
            if not choices:
                return None
<<<<<<< HEAD

            if choices[0][2]:
                return self._encoding_type((choices[0][0], choices[0][2].default_value()))
            return choices[0][0]

    def render_input(self, varprefix, value):
        def_val = '0'
        options = []
=======
            first_choice: CascadingDropdownCleanChoice = choices[0]
            value: CascadingDropdownChoiceValue = first_choice[0]
            vs: _Optional[ValueSpec] = first_choice[2]
            if vs is None:
                return value
            # TODO: What should we do when we have a complex value *and* a ValueSpec?
            # We can't nest things arbitrarily deep, so we just return the first part.
            if isinstance(value, tuple):
                return value[0]
            return value, vs.default_value()

    def render_input(self, varprefix: str, value: CascadingDropdownChoiceValue) -> None:
        def_val = '0'
        options: Choices = []
>>>>>>> upstream/master
        choices = self.choices()
        if not choices:
            html.write(self._no_elements_text)
            return

        for nr, (val, title, vs) in enumerate(choices):
            options.append((str(nr), title))
            # Determine the default value for the select, so the
            # the dropdown pre-selects the line corresponding with value.
            # Note: the html.dropdown() with automatically show the modified
            # selection, if the HTML variable varprefix_sel aleady
            # exists.
<<<<<<< HEAD
            if value == val or (isinstance(value, self._encoding_type) and value[0] == val):
=======
            if value == val or (isinstance(value, tuple) and value[0] == val):
>>>>>>> upstream/master
                def_val = str(nr)

        vp = varprefix + "_sel"
        onchange = "cmk.valuespecs.cascading_change(this, '%s', %d);" % (varprefix, len(choices))
        html.dropdown(vp,
                      options,
                      deflt=def_val,
                      onchange=onchange,
                      ordered=self._sorted,
                      label=self._label)

        # make sure, that the visibility is done correctly, in both
        # cases:
        # 1. Form painted for the first time (no submission yet, vp missing in URL)
        # 2. Form already submitted -> honor URL variable vp for visibility
        cur_val = html.request.var(vp)

        if self._orientation == "vertical":
            html.br()
        else:
            html.nbsp()

        for nr, (val, title, vs) in enumerate(choices):
            if not vs:
                continue

            vp = "%s_%d" % (varprefix, nr)
            if cur_val is not None:
                # Form already submitted once (and probably in complain state)
                show = nr == int(cur_val)

                def_val_2 = vs.default_value()
                # Only try to get the current value for the currently selected choice
                if show:
                    try:
                        def_val_2 = vs.from_html_vars(vp)
                    except MKUserError:
                        pass  # Fallback to default value here

            else:
                # Form painted the first time
                if nr == int(def_val):
                    # This choice is the one choosen by the given value
<<<<<<< HEAD
                    if isinstance(value, self._encoding_type) and len(value) == 2:
=======
                    if isinstance(value, tuple) and len(value) == 2:
>>>>>>> upstream/master
                        def_val_2 = value[1]
                    else:
                        def_val_2 = vs.default_value()

                    show = True
                else:
                    def_val_2 = vs.default_value()
                    show = False

            if not self._render_sub_vs_page_name or show:
                html.open_span(id_="%s_sub" % vp, style="display:%s;" % ("" if show else "none"))
                self.show_sub_valuespec(vp, vs, def_val_2)
                html.close_span()
            else:
<<<<<<< HEAD
                self._show_sub_valuespec_container(vp, val, def_val_2)

    def show_sub_valuespec(self, varprefix, vs, value):
        html.help(vs.help())
        vs.render_input(varprefix, value)

    def _show_sub_valuespec_container(self, varprefix, choice_id, value):
=======
                # TODO: What should we do when we have a complex value? We can't
                # nest things arbitrarily deep, so we just use the first part.
                if isinstance(val, tuple):
                    val = val[0]
                self._show_sub_valuespec_container(vp, val, def_val_2)

    def show_sub_valuespec(self, varprefix: str, vs: ValueSpec, value: Any) -> None:
        html.help(vs.help())
        vs.render_input(varprefix, value)

    def _show_sub_valuespec_container(self, varprefix: str, choice_id: CascadingDropdownChoiceIdent,
                                      value: Any) -> None:
>>>>>>> upstream/master
        html.span("", id_="%s_sub" % varprefix)

        request_vars = {
            "varprefix": varprefix,
            "choice_id": repr(choice_id),
            "encoded_value": repr(value),
        }
        request_vars.update(self._render_sub_vs_request_vars)

        html.javascript("cmk.valuespecs.add_cascading_sub_valuespec_parameters(%s, %s);" %
                        (json.dumps(varprefix),
                         json.dumps({
                             "page_name": self._render_sub_vs_page_name,
                             "request_vars": request_vars,
                         })))

<<<<<<< HEAD
    def value_to_text(self, value):
        choices = self.choices()
        for val, title, vs in choices:
            if (vs and value and value[0] == val) or \
               (value == val):
                if not vs:
                    return title

                rendered_value = vs.value_to_text(value[1])
                if not rendered_value:
                    return title

                if self._render == CascadingDropdown.Render.foldable:
                    with html.plugged():
                        html.begin_foldable_container("foldable_cascading_dropdown",
                                                      id_=hashlib.sha256(repr(value)).hexdigest(),
                                                      isopen=False,
                                                      title=title,
                                                      indent=False)
                        html.write(vs.value_to_text(value[1]))
                        html.end_foldable_container()
                    return html.drain()

                return title + self._separator + \
                       vs.value_to_text(value[1])

        return ""  # Nothing selected? Should never happen

    def from_html_vars(self, varprefix):
=======
    def value_to_text(self, value: CascadingDropdownChoiceValue) -> str:
        value_ident: CascadingDropdownChoiceIdent = value[0] if isinstance(value, tuple) else value

        try:
            ident, title, vs = next(elem for elem in self.choices() if elem[0] == value_ident)
        except StopIteration:
            return "Could not render: %r" % (value,)

        if vs is None and ident == value:
            return title

        assert isinstance(value, tuple), "value is %r (not a tuple) and vs not None" % (value,)

        rendered_value = vs and vs.value_to_text(value[1])
        if not rendered_value:
            return title

        if self._render == CascadingDropdown.Render.foldable:
            with html.plugged():
                html.begin_foldable_container(
                    "foldable_cascading_dropdown",
                    id_=hashlib.sha256(ensure_binary(repr(value))).hexdigest(),
                    isopen=False,
                    title=title,
                    indent=False,
                )
                html.write(rendered_value)
                html.end_foldable_container()
            return html.drain()

        return title + self._separator + rendered_value

    def value_to_json(self, value: CascadingDropdownChoiceValue):
        value_ident: CascadingDropdownChoiceIdent = value[0] if isinstance(value, tuple) else value
        try:
            ident, _title, vs = next(elem for elem in self.choices() if elem[0] == value_ident)
        except StopIteration:
            # just by passes should be considered a bug, value_to_json is not guarantied to return a value
            return

        if vs is None and ident == value:
            return value

        assert isinstance(value, tuple) and vs is not None

        try:
            vs.validate_datatype(value[1], "")
            return [ident, vs.value_to_json(value[1])]
        except Exception:  # TODO: fix exc
            return

    def value_from_json(self, json_value) -> CascadingDropdownChoiceValue:
        value_ident = json_value[0] if isinstance(json_value, list) else json_value
        try:
            ident, _title, vs = next(elem for elem in self.choices() if elem[0] == value_ident)
        except StopIteration:
            # just by passes should be considered a bug, value_from_json is not guarantied to return a value
            return None

        if vs is None and ident == json_value:
            return json_value

        assert isinstance(json_value, list) and vs is not None

        try:
            value = vs.value_from_json(json_value[1])
            vs.validate_datatype(value, "")
            return (ident, value)
        except Exception:  # TODO: fix exc
            return None

    def from_html_vars(self, varprefix: str) -> CascadingDropdownChoiceValue:
>>>>>>> upstream/master
        choices = self.choices()

        # No choices and "no elements text" is shown: The html var is
        # not present and no choice can be made. So fallback to default
        # value and let the validation methods lead to an error message.
        if not choices:
            return self.default_value()

<<<<<<< HEAD
        try:
            sel = int(html.request.var(varprefix + "_sel", ""))
        except ValueError:
            sel = 0
        val, _title, vs = choices[sel]
        if vs:
            val = self._encoding_type((val, vs.from_html_vars(varprefix + "_%d" % sel)))
        return val

    def validate_datatype(self, value, varprefix):
        choices = self.choices()
        for nr, (val, _title, vs) in enumerate(choices):
            if value == val or (isinstance(value, self._encoding_type) and value[0] == val):
                if vs:
                    if not isinstance(value, self._encoding_type) or len(value) != 2:
                        raise MKUserError(
                            varprefix + "_sel",
                            _("Value must be a %s with two elements.") %
                            self._encoding_type.__name__)
=======
        sel = html.request.get_integer_input_mandatory(varprefix + "_sel", 0)
        choice: CascadingDropdownCleanChoice = choices[sel]
        value: CascadingDropdownChoiceValue = choice[0]
        vs: _Optional[ValueSpec] = choice[2]
        if vs is None:
            return value
        # TODO: What should we do when we have a complex value *and* a ValueSpec?
        # We can't nest things arbitrarily deep, so we just return the first part.
        if isinstance(value, tuple):
            return value[0]
        return value, vs.from_html_vars(varprefix + "_%d" % sel)

    def validate_datatype(self, value: CascadingDropdownChoiceValue, varprefix: str) -> None:
        choices = self.choices()
        for nr, (val, _title, vs) in enumerate(choices):
            if value == val or (isinstance(value, tuple) and value[0] == val):
                if vs:
                    if not isinstance(value, tuple) or len(value) != 2:
                        raise MKUserError(varprefix + "_sel",
                                          _("Value must be a tuple with two elements."))
>>>>>>> upstream/master
                    vs.validate_datatype(value[1], varprefix + "_%d" % nr)
                return
        raise MKUserError(varprefix + "_sel", _("Value %r is not allowed here.") % value)

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
=======
    def _validate_value(self, value: CascadingDropdownChoiceValue, varprefix: str) -> None:
>>>>>>> upstream/master
        if self._no_preselect and value == self._no_preselect_value:
            raise MKUserError(varprefix + "_sel", self._no_preselect_error)

        choices = self.choices()
        for nr, (val, _title, vs) in enumerate(choices):
<<<<<<< HEAD
            if value == val or (isinstance(value, self._encoding_type) and value[0] == val):
                if vs:
                    vs.validate_value(value[1], varprefix + "_%d" % nr)
                self._custom_validate(value, varprefix)
                return
        raise MKUserError(varprefix + "_sel", _("Value %r is not allowed here.") % (value,))


class RadioChoice(DropdownChoice):
    """The same logic as the dropdown choice, but rendered as a group of radio buttons.
    columns is None or unset -> separate with '&nbsp;'"""
    def __init__(  # pylint: disable=redefined-builtin
            self,
            choices,  # type: List[TypingTuple[Any, Text]]
            columns=None,  # type: TypingOptional[int]
            orientation=None,  # typing: TypingOptional[Text]
            # DropdownChoice
            sorted=False,  # type: bool
            label=None,  # type: TypingOptional[Text]
            help_separator=None,  # type: Text
            prefix_values=False,  # type: bool
            empty_text=None,  # type: TypingOptional[Text]
            invalid_choice="complain",  # type: TypingOptional[str]
            invalid_choice_title=None,  # type: TypingOptional[Text]
            invalid_choice_error=None,  # type: TypingOptional[Text]
            no_preselect=False,  # type: bool
            no_preselect_value=None,  # type: Any
            no_preselect_title="",  # type: Text
            no_preselect_error=None,  # type: Text
            on_change=None,  # type: Text
            read_only=False,  # type: bool
            encode_value=True,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(RadioChoice, self).__init__(choices=choices,
                                          sorted=sorted,
                                          label=label,
                                          help_separator=help_separator,
                                          prefix_values=prefix_values,
                                          empty_text=empty_text,
                                          invalid_choice=invalid_choice,
                                          invalid_choice_title=invalid_choice_title,
                                          invalid_choice_error=invalid_choice_error,
                                          no_preselect=no_preselect,
                                          no_preselect_value=no_preselect_value,
                                          no_preselect_title=no_preselect_title,
                                          no_preselect_error=no_preselect_error,
                                          on_change=on_change,
                                          read_only=read_only,
                                          encode_value=encode_value,
                                          title=title,
                                          help=help,
                                          default_value=default_value,
                                          validate=validate)
        self._columns = columns
        # Allow orientation as corner cases of columns
        orientation = orientation
        if orientation == "vertical":
            self._columns = 1
        elif orientation == "horizontal":
            self._columns = 9999999

    def render_input(self, varprefix, value):
        html.begin_radio_group()
        if self._columns is not None:
            html.open_table(class_=["radiochoice"])
            html.open_tr()

        if self._sorted:
            choices = self._choices[:]
            choices.sort(key=lambda x: x[1])
        else:
            choices = self._choices

        for index, entry in enumerate(choices):
            if self._columns is not None:
                html.open_td()

            if len(entry) > 2 and entry[2] is not None:  # icon!
                label = html.render_icon(entry[2], entry[1])
            else:
                label = entry[1]

            html.radiobutton(varprefix, self.option_id(entry[0]), value == entry[0], label)

            if len(entry) > 3 and entry[3]:
                html.open_p()
                html.write(entry[3])
                html.close_p()

            if self._columns is not None:
                html.close_td()
                if (index + 1) % self._columns == 0 and (index + 1) < len(self._choices):
                    html.tr('')
            else:
                html.nbsp()

        if self._columns is not None:
            mod = len(self._choices) % self._columns
            if mod:
                for _td_counter in range(self._columns - mod - 1):
                    html.td('')
            html.close_tr()
            html.close_table()

        html.end_radio_group()
=======
            if value == val or (isinstance(value, tuple) and value[0] == val):
                if vs:
                    assert isinstance(value, tuple)
                    vs.validate_value(value[1], varprefix + "_%d" % nr)
                return
        raise MKUserError(varprefix + "_sel", _("Value %r is not allowed here.") % (value,))

    def transform_value(self, value: CascadingDropdownChoiceValue) -> CascadingDropdownChoiceValue:
        value_ident: CascadingDropdownChoiceIdent = value[0] if isinstance(value, tuple) else value
        try:
            ident, _title, vs = next(elem for elem in self.choices() if elem[0] == value_ident)
        except StopIteration:
            raise ValueError(_("%s is not an allowed value") % value)

        if vs is None and ident == value:
            return value

        assert isinstance(value, tuple) and vs is not None

        return (value[0], vs.transform_value(value[1]))


ListChoiceChoiceValue = Union[str, int]
ListChoiceChoicePairs = Sequence[_Tuple[ListChoiceChoiceValue, str]]
ListChoiceChoices = Union[None, ListChoiceChoicePairs, Callable[[], ListChoiceChoicePairs],
                          Dict[ListChoiceChoiceValue, str]]
>>>>>>> upstream/master


class ListChoice(ValueSpec):
    """A list of checkboxes representing a list of values"""
    @staticmethod
    def dict_choices(choices):
        return [("%s" % type_id, "%d - %s" % (type_id, type_name))
                for (type_id, type_name) in sorted(choices.items())]

    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            # ListChoice
            choices=None,  # type: TypingOptional[Union[List[TypingTuple[Text, Text]], Dict[Text, Text], Callable[[], List]]]
            columns=1,  # type: int
            allow_empty=True,  # type: bool
            empty_text=None,  # type: TypingOptional[Text]
            render_function=None,  # type: TypingOptional[Callable[[Text, Text], Text]]
            toggle_all=False,  # type: bool
            # TODO: Rename to "orientation" to be in line with other valuespecs
            render_orientation="horizontal",  # type: Text
            no_elements_text=None,  # type: TypingOptional[Text]
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(ListChoice, self).__init__(title=title,
                                         help=help,
                                         default_value=default_value,
                                         validate=validate)
=======
        self,
        # ListChoice
        choices: ListChoiceChoices = None,
        columns: int = 1,
        allow_empty: bool = True,
        empty_text: _Optional[str] = None,
        render_function: _Optional[Callable[[str, str], str]] = None,
        toggle_all: bool = False,
        # TODO: Rename to "orientation" to be in line with other valuespecs
        render_orientation: str = "horizontal",
        no_elements_text: _Optional[str] = None,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._choices = choices
        self._columns = columns
        self._allow_empty = allow_empty
        self._empty_text = empty_text if empty_text is not None else _("(nothing selected)")
<<<<<<< HEAD
        self._loaded_at = None
=======
        self._loaded_at: _Optional[int] = None
>>>>>>> upstream/master
        self._render_function = render_function if render_function is not None else (
            lambda id, val: val)
        self._toggle_all = toggle_all
        self._render_orientation = render_orientation  # other: vertical
        self._no_elements_text = no_elements_text if no_elements_text is not None else \
            _("There are no elements defined for this selection")

    # In case of overloaded functions with dynamic elements
    def load_elements(self):
<<<<<<< HEAD
        if self._choices is not None:
            if isinstance(self._choices, list):
                self._elements = self._choices
            elif isinstance(self._choices, dict):
                self._elements = ListChoice.dict_choices(self._choices)
            else:
                self._elements = self._choices()
            return

        if self._loaded_at != id(html):
            self._elements = self.get_elements()
            self._loaded_at = id(html)  # unique for each query!
=======
        if self._choices is None:
            if self._loaded_at != id(html):
                self._elements = self.get_elements()
                self._loaded_at = id(html)  # unique for each query!
        elif isinstance(self._choices, ABCSequence):
            self._elements = self._choices
        elif isinstance(self._choices, dict):
            self._elements = self.dict_choices(self._choices)
        elif callable(self._choices):
            self._elements = self._choices()
        else:
            raise ValueError("illegal type for choices")
>>>>>>> upstream/master

    def get_elements(self):
        raise NotImplementedError()

    def canonical_value(self):
        return []

    def _draw_listchoice(self, varprefix, value, elements, columns, toggle_all):

        if self._toggle_all:
            html.a(_("Check / Uncheck all"),
                   href="javascript:cmk.valuespecs.list_choice_toggle_all('%s')" % varprefix)

        html.open_table(id_="%s_tbl" % varprefix, class_=["listchoice"])
        for nr, (key, title) in enumerate(elements):
            if nr % self._columns == 0:
                if nr > 0:
                    html.close_tr()
                html.open_tr()
            html.open_td()
            html.checkbox("%s_%d" % (varprefix, nr), key in value, label=title)
            html.close_td()
        html.close_tr()
        html.close_table()

    def render_input(self, varprefix, value):
        self.load_elements()
        if not self._elements:
            html.write(self._no_elements_text)
            return

        self._draw_listchoice(varprefix, value, self._elements, self._columns, self._toggle_all)

        # Make sure that at least one variable with the prefix is present
        html.hidden_field(varprefix, "1", add_var=True)

    def value_to_text(self, value):
        if not value:
            return self._empty_text

        self.load_elements()
        d = dict(self._elements)
        texts = [self._render_function(v, d.get(v, v)) for v in value]
        if self._render_orientation == "horizontal":
            return ", ".join(texts)

        # TODO: This is a workaround for a bug. This function needs to return str objects right now.
        return "%s" % html.render_table(
            html.render_tr(html.render_td(html.render_br().join(HTML(x) for x in texts))))
        #OLD: return "<table><tr><td>" + "<br>".join(texts) + "</td></tr></table>"

    def from_html_vars(self, varprefix):
        self.load_elements()
<<<<<<< HEAD
        value = []

        for nr, (key, _title) in enumerate(self._elements):
            if html.get_checkbox("%s_%d" % (varprefix, nr)):
                value.append(key)
        return value

    def validate_datatype(self, value, varprefix):
        self.load_elements()

=======
        return [
            key  #
            for nr, (key, _title) in enumerate(self._elements)
            if html.get_checkbox("%s_%d" % (varprefix, nr))
        ]

    def value_to_json(self, value):
        return value

    def value_from_json(self, json_value):
        return json_value

    def validate_datatype(self, value, varprefix):
>>>>>>> upstream/master
        if not isinstance(value, list):
            raise MKUserError(varprefix,
                              _("The datatype must be list, but is %s") % _type_name(value))

<<<<<<< HEAD
        for v in value:
            if self._value_is_invalid(v):
                raise MKUserError(varprefix, _("%s is not an allowed value") % v)

    def _validate_value(self, value, varprefix):
        if not self._allow_empty and not value:
            raise MKUserError(varprefix, _('You have to select at least one element.'))

    def _value_is_invalid(self, value):
        d = dict(self._elements)
        return value not in d
=======
    def _validate_value(self, value, varprefix):
        if not self._allow_empty and not value:
            raise MKUserError(varprefix, _('You have to select at least one element.'))
        self.load_elements()
        for v in value:
            if self._value_is_invalid(v):
                raise MKUserError(varprefix, _("%s is not an allowed value") % v)

    def _value_is_invalid(self, value: ListChoiceChoiceValue) -> bool:
        return all(value != val for val, _title in self._elements)
>>>>>>> upstream/master


class DualListChoice(ListChoice):
    """Implements a choice of items which is realized with two ListChoices
    select fields.

    One contains every unselected item and the other one contains the selected
    items.  Optionally you can have the user influence the order of the entries
    by simply clicking them in a certain order.  If that feature is not being
    used, then the original order of the elements is kept.

    Beware: the keys in this choice are not type safe.  They can only be
    strings. They must not contain | or other dangerous characters. We should
    fix this and make it this compatible to DropdownChoice()
    """
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            # DualListChoice
            autoheight=False,  # type: bool
            custom_order=False,  # type: bool
            instant_add=False,  # type: bool
            enlarge_active=False,  # type: bool
            rows=None,  # type: TypingOptional[int]
            size=None,  # type: TypingOptional[int]
            # ListChoice
            choices=None,  # type: TypingOptional[Union[List[TypingTuple[Text, Text]], Dict[Text, Text], Callable[[], List]]]
            columns=1,  # type: int
            allow_empty=True,  # type: bool
            empty_text=None,  # type: TypingOptional[Text]
            render_function=None,  # type: TypingOptional[Callable[[Text, Text], Text]]
            toggle_all=False,  # type: bool
            # TODO: Rename to "orientation" to be in line with other valuespecs
            render_orientation="horizontal",  # type: Text
            no_elements_text=None,  # type: TypingOptional[Text]
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(DualListChoice, self).__init__(choices=choices,
                                             columns=columns,
                                             allow_empty=allow_empty,
                                             empty_text=empty_text,
                                             render_function=render_function,
                                             toggle_all=toggle_all,
                                             render_orientation=render_orientation,
                                             no_elements_text=no_elements_text,
                                             title=title,
                                             help=help,
                                             default_value=default_value,
                                             validate=validate)
=======
        self,
        # DualListChoice
        autoheight: bool = False,
        custom_order: bool = False,
        instant_add: bool = False,
        enlarge_active: bool = False,
        rows: _Optional[int] = None,
        size: _Optional[int] = None,
        # ListChoice
        choices: ListChoiceChoices = None,
        columns: int = 1,
        allow_empty: bool = True,
        empty_text: _Optional[str] = None,
        render_function: _Optional[Callable[[str, str], str]] = None,
        toggle_all: bool = False,
        # TODO: Rename to "orientation" to be in line with other valuespecs
        render_orientation: str = "horizontal",
        no_elements_text: _Optional[str] = None,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
            choices=choices,
            columns=columns,
            allow_empty=allow_empty,
            empty_text=empty_text,
            render_function=render_function,
            toggle_all=toggle_all,
            render_orientation=render_orientation,
            no_elements_text=no_elements_text,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
>>>>>>> upstream/master
        self._autoheight = autoheight
        self._custom_order = custom_order
        self._instant_add = instant_add
        self._enlarge_active = enlarge_active
        if rows is not None:
            self._rows = rows
            self._autoheight = False
        else:
            self._rows = 5
        self._size = size  # Total width in ex

    def render_input(self, varprefix, value):
        self.load_elements()
        if not self._elements:
            html.write_text(_("There are no elements for selection."))
            return

        # Use values from HTTP request in complain mode
        if value is None:
            value = self.from_html_vars(varprefix)

        selected = []
        unselected = []
        if self._custom_order:
            edict = dict(self._elements)
            allowed_keys = edict.keys()
            for v in value:
                if v in allowed_keys:
                    selected.append((v, edict[v]))

            for v, _name in self._elements:
                if v not in value:
                    unselected.append((v, edict[v]))
        else:
            for e in self._elements:
                if e[0] in value:
                    selected.append(e)
                else:
                    unselected.append(e)

        select_func = 'cmk.valuespecs.duallist_switch(\'unselected\', \'%s\', %d);' % (
            varprefix, 1 if self._custom_order else 0)
        unselect_func = 'cmk.valuespecs.duallist_switch(\'selected\', \'%s\', %d);' % (
            varprefix, 1 if self._custom_order else 0)

        html.open_table(class_=["vs_duallist"],
                        style="width: %dpx;" % (self._size * 6.4) if self._size else None)

        html.open_tr()
        html.open_td(class_="head")
        html.write_text(_('Available'))
        if not self._instant_add:
            html.a(">", href="javascript:%s;" % select_func, class_=["control", "add"])
        html.close_td()

        html.open_td(class_="head")
        html.write_text(_('Selected'))
        if not self._instant_add:
            html.a("<", href="javascript:%s;" % unselect_func, class_=["control", "del"])
        html.close_td()
        html.close_tr()

        html.open_tr()
        for suffix, choices, select_func in [
            ("unselected", unselected, select_func),
            ("selected", selected, unselect_func),
        ]:

            onchange_func = select_func if self._instant_add else ''
            if self._enlarge_active:
                onchange_func = 'cmk.valuespecs.duallist_enlarge(%s, %s);' % (json.dumps(suffix),
                                                                              json.dumps(varprefix))

<<<<<<< HEAD
            attrs = {
                'multiple': 'multiple',
                'style': 'height:auto' if self._autoheight else "height: %dpx" % (self._rows * 16),
                'ondblclick': select_func if not self._instant_add else '',
            }

            html.open_td()
            attrs["onchange"] = onchange_func
            html.multi_select("%s_%s" % (varprefix, suffix),
                              choices,
                              deflt='',
                              ordered=self._custom_order,
                              **attrs)
=======
            html.open_td()
            html.dropdown(
                "%s_%s" % (varprefix, suffix),
                choices,
                deflt='',
                ordered=self._custom_order,
                multiple="multiple",
                style='height:auto' if self._autoheight else "height: %dpx" % (self._rows * 16),
                ondblclick=select_func if not self._instant_add else '',
                onchange=onchange_func,
            )

>>>>>>> upstream/master
            html.close_td()
        html.close_tr()

        html.close_table()
        html.hidden_field(varprefix,
                          '|'.join([k for k, v in selected]),
                          id_=varprefix,
                          add_var=True)

    def _validate_value(self, value, varprefix):
        try:
<<<<<<< HEAD
            super(DualListChoice, self)._validate_value(value, varprefix)
        except MKUserError as e:
            raise MKUserError(e.varname + "_selected", e.message)

    def from_html_vars(self, varprefix):
        self.load_elements()
        selected = html.request.var(varprefix, '').split('|')
        value = []
=======
            super()._validate_value(value, varprefix)
        except MKUserError as e:
            v = "" if e.varname is None else e.varname
            raise MKUserError(v + "_selected", e.message)

    def from_html_vars(self, varprefix):
        self.load_elements()
        value: List = []
        selection_str = html.request.var(varprefix, '')
        if selection_str is None:
            return value
        selected = selection_str.split('|')
>>>>>>> upstream/master
        if self._custom_order:
            edict = dict(self._elements)
            allowed_keys = edict.keys()
            for v in selected:
                if v in allowed_keys:
                    value.append(v)
        else:
            for key, _title in self._elements:
                if key in selected:
                    value.append(key)
        return value


class OptionalDropdownChoice(DropdownChoice):
<<<<<<< HEAD
    """A type-save dropdown choice with one extra field that
    opens a further value spec for entering an alternative
    Value."""
    def __init__(  # pylint: disable=redefined-builtin
            self,
            explicit,  # type: ValueSpec
            choices,  # type: List[TypingTuple[Any, Text]]
            otherlabel=None,  # type: TypingOptional[Text]
            # DropdownChoice
            sorted=False,  # type: bool
            label=None,  # type: TypingOptional[Text]
            help_separator=None,  # type: Text
            prefix_values=False,  # type: bool
            empty_text=None,  # type: TypingOptional[Text]
            invalid_choice="complain",  # type: TypingOptional[str]
            invalid_choice_title=None,  # type: TypingOptional[Text]
            invalid_choice_error=None,  # type: TypingOptional[Text]
            no_preselect=False,  # type: bool
            no_preselect_value=None,  # type: Any
            no_preselect_title="",  # type: Text
            no_preselect_error=None,  # type: Text
            on_change=None,  # type: Text
            read_only=False,  # type: bool
            encode_value=True,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(OptionalDropdownChoice, self).__init__(choices=choices,
                                                     sorted=sorted,
                                                     label=label,
                                                     help_separator=help_separator,
                                                     prefix_values=prefix_values,
                                                     empty_text=empty_text,
                                                     invalid_choice=invalid_choice,
                                                     invalid_choice_title=invalid_choice_title,
                                                     invalid_choice_error=invalid_choice_error,
                                                     no_preselect=no_preselect,
                                                     no_preselect_value=no_preselect_value,
                                                     no_preselect_title=no_preselect_title,
                                                     no_preselect_error=no_preselect_error,
                                                     on_change=on_change,
                                                     read_only=read_only,
                                                     encode_value=encode_value,
                                                     title=title,
                                                     help=help,
                                                     default_value=default_value,
                                                     validate=validate)
=======
    """A type-safe dropdown choice with one extra field that
    opens a further value spec for entering an alternative
    Value."""
    def __init__(  # pylint: disable=redefined-builtin
        self,
        explicit: ValueSpec,
        choices: DropdownChoices,
        otherlabel: _Optional[str] = None,
        # DropdownChoice
        sorted: bool = False,
        label: _Optional[str] = None,
        help_separator: _Optional[str] = None,
        prefix_values: bool = False,
        empty_text: _Optional[str] = None,
        invalid_choice: _Optional[str] = "complain",
        invalid_choice_title: _Optional[str] = None,
        invalid_choice_error: _Optional[str] = None,
        no_preselect: bool = False,
        no_preselect_value: Any = None,
        no_preselect_title: str = "",
        no_preselect_error: _Optional[str] = None,
        on_change: _Optional[str] = None,
        read_only: bool = False,
        encode_value: bool = True,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
            choices=choices,
            sorted=sorted,
            label=label,
            help_separator=help_separator,
            prefix_values=prefix_values,
            empty_text=empty_text,
            invalid_choice=invalid_choice,
            invalid_choice_title=invalid_choice_title,
            invalid_choice_error=invalid_choice_error,
            no_preselect=no_preselect,
            no_preselect_value=no_preselect_value,
            no_preselect_title=no_preselect_title,
            no_preselect_error=no_preselect_error,
            on_change=on_change,
            read_only=read_only,
            encode_value=encode_value,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
>>>>>>> upstream/master

        self._explicit = explicit
        self._otherlabel = otherlabel if otherlabel is not None else _("Other")

    def canonical_value(self):
        return self._explicit.canonical_value()

    def value_is_explicit(self, value):
        return value not in [c[0] for c in self.choices()]

    def render_input(self, varprefix, value):
        defval = "other"
<<<<<<< HEAD
        options = []
=======
        options: List[_Tuple[_Optional[str], str]] = []
>>>>>>> upstream/master
        for n, (val, title) in enumerate(self.choices()):
            options.append((str(n), title))
            if val == value:
                defval = str(n)
        if self._sorted:
            options.sort(key=lambda x: x[1])
        options.append(("other", self._otherlabel))
        html.dropdown(
            varprefix,
            options,
            deflt=defval,  # style="float:left;",
            onchange="cmk.valuespecs.toggle_dropdown(this, '%s_ex');" % varprefix)
        if html.request.has_var(varprefix):
            div_is_open = html.request.var(varprefix) == "other"
        else:
            div_is_open = self.value_is_explicit(value)

        html.open_span(id_="%s_ex" % varprefix,
                       style=["white-space: nowrap;", None if div_is_open else "display:none;"])
        html.nbsp()

        if defval == "other":
            input_value = value
        else:
            input_value = self._explicit.default_value()
        html.help(self._explicit.help())
        self._explicit.render_input(varprefix + "_ex", input_value)
        html.close_span()

    def value_to_text(self, value):
        for val, title in self.choices():
            if val == value:
                return title
        return self._explicit.value_to_text(value)

    def from_html_vars(self, varprefix):
        choices = self.choices()
        sel = html.request.var(varprefix)
        if sel == "other":
            return self._explicit.from_html_vars(varprefix + "_ex")

        for n, (val, _title) in enumerate(choices):
            if sel == str(n):
                return val
        return choices[0][0]  # can only happen if user garbled URL

    def _validate_value(self, value, varprefix):
        if self.value_is_explicit(value):
            self._explicit.validate_value(value, varprefix)

    def validate_datatype(self, value, varprefix):
        for val, _title in self.choices():
            if val == value:
                return
        self._explicit.validate_datatype(value, varprefix + "_ex")


def round_date(t):
    return int(int(t) / seconds_per_day) * seconds_per_day


def today():
    return round_date(time.time())


# TODO: Cleanup kwargs
def Weekday(**kwargs):
    return DropdownChoice(choices=sorted(defines.weekdays().items()), **kwargs)


class RelativeDate(OptionalDropdownChoice):
    """Input of date with optimization for nearby dates in the future

    Useful for example for alarms. The date is represented by a UNIX timestamp
    where the seconds are silently ignored."""
    def __init__(self, **kwargs):
        choices = [
            (0, _("today")),
            (1, _("tomorrow")),
        ]
        weekday = time.localtime(today()).tm_wday
        for w in range(2, 7):
            wd = (weekday + w) % 7
            choices.append((w, defines.weekday_name(wd)))
        for w in range(0, 7):
            wd = (weekday + w) % 7
            if w < 2:
                title = _(" next week")
            else:
                title = _(" in %d days") % (w + 7)
            choices.append((w + 7, defines.weekday_name(wd) + title))

        kwargs['choices'] = choices
        kwargs['explicit'] = Integer()
        kwargs['otherlabel'] = _("in ... days")

<<<<<<< HEAD
        super(RelativeDate, self).__init__(**kwargs)
=======
        super().__init__(**kwargs)
>>>>>>> upstream/master

        if "default_days" in kwargs:
            self._default_value = kwargs["default_days"] * seconds_per_day + today()
        else:
            self._default_value = today()

    def canonical_value(self):
        return self._default_value

    def render_input(self, varprefix, value):
        reldays = int((round_date(value) - today()) / seconds_per_day)  # fixed: true-division
<<<<<<< HEAD
        super(RelativeDate, self).render_input(varprefix, reldays)
=======
        super().render_input(varprefix, reldays)
>>>>>>> upstream/master

    def value_to_text(self, value):
        reldays = int((round_date(value) - today()) / seconds_per_day)  # fixed: true-division
        if reldays == -1:
            return _("yesterday")
<<<<<<< HEAD
        elif reldays == -2:
            return _("two days ago")
        elif reldays < 0:
            return _("%d days ago") % -reldays
        elif reldays < len(self._choices):
            return self._choices[reldays][1]
        return _("in %d days") % reldays

    def from_html_vars(self, varprefix):
        reldays = super(RelativeDate, self).from_html_vars(varprefix)
=======
        if reldays == -2:
            return _("two days ago")
        if reldays < 0:
            return _("%d days ago") % -reldays
        choices = self.choices()  # TODO: Is this correct with no_preselect?
        if reldays < len(choices):
            return choices[reldays][1]
        return _("in %d days") % reldays

    def from_html_vars(self, varprefix):
        reldays = super().from_html_vars(varprefix)
>>>>>>> upstream/master
        return today() + reldays * seconds_per_day

    def validate_datatype(self, value, varprefix):
        if not isinstance(value, (int, float)):
            raise MKUserError(varprefix, _("Date must be a number value"))


class AbsoluteDate(ValueSpec):
    """A ValueSpec for editing a date

    The date is represented as a UNIX timestamp x where x % seconds_per_day is
    zero (or will be ignored if non-zero), as long as include_time is not set
    to True"""
    def __init__(self, **kwargs):
<<<<<<< HEAD
        super(AbsoluteDate, self).__init__(**kwargs)
=======
        super().__init__(**kwargs)
>>>>>>> upstream/master
        self._show_titles = kwargs.get("show_titles", True)
        self._label = kwargs.get("label")
        self._include_time = kwargs.get("include_time", False)
        self._format = kwargs.get("format", "%F %T" if self._include_time else "%F")
        self._default_value = kwargs.get("default_value", None)
        self._allow_empty = kwargs.get('allow_empty', False)
        # The default is that "None" means show current date/time in the
        # input fields. This option changes the input fields to be empty by default
        # and makes the value able to be None when no time is set.
        # FIXME: Shouldn't this be the default?
        self._none_means_empty = kwargs.get("none_means_empty", False)
<<<<<<< HEAD
=======
        self._submit_form_name = kwargs.get("submit_form_name")
>>>>>>> upstream/master

    def default_value(self):
        if self._default_value is not None:
            return self._default_value

        if self._allow_empty:
            return None

        if self._include_time:
            return time.time()
        return today()

    def canonical_value(self):
        return self.default_value()

<<<<<<< HEAD
    def split_date(self, value):
        if self._none_means_empty and value is None:
            return (None,) * 6
        lt = time.localtime(value)
        return lt.tm_year, lt.tm_mon, lt.tm_mday, \
               lt.tm_hour, lt.tm_min, lt.tm_sec

    def render_input(self, varprefix, value):
=======
    def split_date(
        self, value: _Optional[float]
    ) -> _Tuple[_Optional[int], _Optional[int], _Optional[int], _Optional[int], _Optional[int],
                _Optional[int]]:
        if self._none_means_empty and value is None:
            return None, None, None, None, None, None
        lt = time.localtime(value)
        return lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec

    def render_input(self, varprefix: Any, value: Any) -> None:
>>>>>>> upstream/master
        if self._label:
            html.write("%s" % self._label)
            html.nbsp()

        year, month, day, hour, mmin, sec = self.split_date(value)
<<<<<<< HEAD
        values = [
            ("_year", year, 4),
            ("_month", month, 2),
            ("_day", day, 2),
=======
        values: List[_Optional[_Tuple[str, _Optional[int], int]]] = [
            ("_year", year, 6),
            ("_month", month, 3),
            ("_day", day, 3),
>>>>>>> upstream/master
        ]
        if self._include_time:
            values += [
                None,
                ("_hour", hour, 2),
                ("_min", mmin, 2),
                ("_sec", sec, 2),
            ]

<<<<<<< HEAD
        if not self._show_titles:
=======
        if self._show_titles:
>>>>>>> upstream/master
            titles = [_("Year"), _("Month"), _("Day")]
            if self._include_time:
                titles += ['', _("Hour"), _("Minute"), _("Sec.")]

            html.open_table(class_=["vs_date"])

            html.open_tr()
<<<<<<< HEAD
            map(html.th, titles)
=======
            for t in titles:
                html.th(t)
>>>>>>> upstream/master
            html.close_tr()

            html.open_tr()
            for val in values:
                html.open_td()
                if val is None:
                    html.nbsp()
                else:
<<<<<<< HEAD
                    html.number_input(varprefix + val[0], val[1], size=val[2])
=======
                    html.text_input(
                        varprefix + val[0],
                        default_value=str(val[1]) if val[1] is not None else "",
                        size=val[2],
                        cssclass="number",
                        submit=self._submit_form_name,
                    )
>>>>>>> upstream/master
                html.close_td()
            html.close_tr()

            html.close_table()

        else:
            for count, val in enumerate(values):
                if count > 0:
                    html.write_text(" ")
                if val is None:
                    html.nbsp()
                else:
<<<<<<< HEAD
                    html.number_input(varprefix + val[0], val[1], size=val[2])
=======
                    html.text_input(
                        varprefix + val[0],
                        default_value=str(val[1]),
                        size=val[2],
                        cssclass="number",
                        submit=self._submit_form_name,
                    )
>>>>>>> upstream/master

    def set_focus(self, varprefix):
        html.set_focus(varprefix + "_year")

    def value_to_text(self, value):
        return time.strftime(self._format, time.localtime(value))

<<<<<<< HEAD
    def from_html_vars(self, varprefix):
=======
    def value_to_json(self, value):
        return value

    def value_from_json(self, json_value):
        return json_value

    # TODO: allow_empty is a *very* bad idea typing-wise! We are poisoned by Optional... :-P
    def from_html_vars(self, varprefix: str) -> _Optional[float]:
>>>>>>> upstream/master
        parts = []
        entries = [
            ("year", _("year"), 1970, 2038),
            ("month", _("month"), 1, 12),
            ("day", _("day"), 1, 31),
        ]

        if self._include_time:
            entries += [
                ("hour", _("hour"), 0, 23),
                ("min", _("min"), 0, 59),
                ("sec", _("sec"), 0, 59),
            ]

        for what, title, mmin, mmax in entries:
            try:
                varname = varprefix + "_" + what
<<<<<<< HEAD
                part = int(html.request.var(varname, ""))
            except ValueError:
                if self._allow_empty:
                    return None
                else:
                    raise MKUserError(varname, _("Please enter a valid number"))
=======
                part_str = html.request.var(varname, "")
                if part_str is None:
                    raise ValueError()
                part = int(part_str)
            except ValueError:
                if self._allow_empty:
                    return None
                raise MKUserError(varname, _("Please enter a valid number"))
>>>>>>> upstream/master
            if part < mmin or part > mmax:
                raise MKUserError(
                    varname,
                    _("The value for %s must be between %d and %d") % (title, mmin, mmax))
            parts.append(part)

        # Construct broken time from input fields. Assume no-dst
        parts += [0] * (3 if self._include_time else 6)
        # Convert to epoch
<<<<<<< HEAD
        epoch = time.mktime(tuple(parts))
=======
        epoch = time.mktime((
            parts[0],  # tm_year
            parts[1],  # tm_mon
            parts[2],  # tm_mday
            parts[3],  # tm_hour
            parts[4],  # tm_min
            parts[5],  # tm_sec
            parts[6],  # tm_wday
            parts[7],  # tm_yday
            parts[8],  # tm_isdst
        ))
>>>>>>> upstream/master
        # Convert back to localtime in order to know DST setting
        localtime = time.localtime(epoch)
        # Enter DST setting of that time
        parts[-1] = localtime.tm_isdst
        # Convert to epoch again
<<<<<<< HEAD
        return time.mktime(tuple(parts))
=======
        return time.mktime((
            parts[0],  # tm_year
            parts[1],  # tm_mon
            parts[2],  # tm_mday
            parts[3],  # tm_hour
            parts[4],  # tm_min
            parts[5],  # tm_sec
            parts[6],  # tm_wday
            parts[7],  # tm_yday
            parts[8],  # tm_isdst
        ))
>>>>>>> upstream/master

    def validate_datatype(self, value, varprefix):
        if value is None and self._allow_empty:
            return
        if not isinstance(value, (int, float)):
            raise MKUserError(
                varprefix,
                _("The type of the timestamp must be int or float, but is %s") % _type_name(value))

    def _validate_value(self, value, varprefix):
        if (not self._allow_empty and value is None) or value < 0 or int(value) > (2**31 - 1):
            return MKUserError(varprefix, _("%s is not a valid UNIX timestamp") % value)


<<<<<<< HEAD
=======
TimeofdayValue = _Tuple[int, int]


>>>>>>> upstream/master
class Timeofday(ValueSpec):
    """Valuespec for entering times like 00:35 or 16:17

    Currently no seconds are supported. But this could easily be added.  The
    value itself is stored as a pair of integers, a.g.  (0, 35) or (16, 17). If
    the user does not enter a time the vs will return None.
    """
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            allow_24_00=False,  # type: bool
            allow_empty=True,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Timeofday, self).__init__(title=title,
                                        help=help,
                                        default_value=default_value,
                                        validate=validate)
        self._allow_24_00 = allow_24_00
        self._allow_empty = allow_empty

    def canonical_value(self):
=======
        self,
        allow_24_00: bool = False,
        allow_empty: bool = True,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        self._allow_24_00 = allow_24_00
        self._allow_empty = allow_empty

    def canonical_value(self) -> _Optional[TimeofdayValue]:
>>>>>>> upstream/master
        if self._allow_empty:
            return None
        return (0, 0)

<<<<<<< HEAD
    def render_input(self, varprefix, value):
        text = ("%02d:%02d" % value) if value else ''
        html.text_input(varprefix, text, size=5)

    def value_to_text(self, value):
        if value is None:
            return ""
        return "%02d:%02d" % value

    def from_html_vars(self, varprefix):
        # Fully specified
        text = html.request.var(varprefix, "").strip()
=======
    def render_input(self, varprefix: str, value: _Optional[TimeofdayValue]) -> None:
        text = ("%02d:%02d" % value) if value else ''
        html.text_input(varprefix, text, size=5)

    def value_to_text(self, value: _Optional[TimeofdayValue]) -> str:
        if value is None:
            return u""
        return u"%02d:%02d" % value

    def from_html_vars(self, varprefix: str) -> _Optional[TimeofdayValue]:
        # Fully specified
        text = html.request.get_str_input_mandatory(varprefix, "").strip()
>>>>>>> upstream/master
        if not text:
            return None

        if re.match("^(24|[0-1][0-9]|2[0-3]):[0-5][0-9]$", text):
<<<<<<< HEAD
            return tuple(map(int, text.split(":")))
=======
            hours, minutes = text.split(":")
            return int(hours), int(minutes)
>>>>>>> upstream/master

        # only hours
        try:
            b = int(text)
            return (b, 0)
<<<<<<< HEAD
        except:
=======
        except Exception:
>>>>>>> upstream/master
            raise MKUserError(
                varprefix,
                _("Invalid time format '<tt>%s</tt>', please use <tt>24:00</tt> format.") % text)

<<<<<<< HEAD
    def validate_datatype(self, value, varprefix):
=======
    def validate_datatype(self, value: _Optional[TimeofdayValue], varprefix: str) -> None:
>>>>>>> upstream/master
        if self._allow_empty and value is None:
            return

        if not isinstance(value, tuple):
            raise MKUserError(varprefix,
                              _("The datatype must be tuple, but ist %s") % _type_name(value))

        if len(value) != 2:
            raise MKUserError(
                varprefix,
                _("The tuple must contain two elements, but you have %d") % len(value))

        for x in value:
            if not isinstance(x, int):
                raise MKUserError(
                    varprefix,
                    _("All elements of the tuple must be of type int, you have %s") % _type_name(x))

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
        if not self._allow_empty and value is None:
            raise MKUserError(varprefix, _("Please enter a time."))
=======
    def _validate_value(self, value: _Optional[TimeofdayValue], varprefix: str) -> None:
        if not self._allow_empty and value is None:
            raise MKUserError(varprefix, _("Please enter a time."))

        if value is None:
            return

>>>>>>> upstream/master
        if self._allow_24_00:
            max_value = (24, 0)
        else:
            max_value = (23, 59)
<<<<<<< HEAD
        if value > max_value:
            raise MKUserError(varprefix,
                              _("The time must not be greater than %02d:%02d.") % max_value)
        elif value[0] < 0 or value[1] < 0 or value[0] > 24 or value[1] > 59:
            raise MKUserError(varprefix, _("Hours/Minutes out of range"))


class TimeofdayRange(ValueSpec):
    """Range like 00:15 - 18:30"""
    def __init__(  # pylint: disable=redefined-builtin
            self,
            allow_empty=True,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(TimeofdayRange, self).__init__(title=title,
                                             help=help,
                                             default_value=default_value,
                                             validate=validate)
=======

        if value > max_value:
            raise MKUserError(varprefix,
                              _("The time must not be greater than %02d:%02d.") % max_value)
        if value[0] < 0 or value[1] < 0 or value[0] > 24 or value[1] > 59:
            raise MKUserError(varprefix, _("Hours/Minutes out of range"))


TimeofdayRangeValue = _Tuple[_Tuple[int, int], _Tuple[int, int]]


class TimeofdayRange(ValueSpec):
    """Range like 00:15 - 18:30"""
    def __init__(  # pylint: disable=redefined-builtin
        self,
        allow_empty: bool = True,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._allow_empty = allow_empty
        self._bounds = (
            Timeofday(allow_empty=self._allow_empty, allow_24_00=True),
            Timeofday(allow_empty=self._allow_empty, allow_24_00=True),
        )

<<<<<<< HEAD
    def canonical_value(self):
=======
    def canonical_value(self) -> _Optional[TimeofdayRangeValue]:
>>>>>>> upstream/master
        if self._allow_empty:
            return None
        return (0, 0), (24, 0)

<<<<<<< HEAD
    def render_input(self, varprefix, value):
        if value is None:
            value = (None, None)
        self._bounds[0].render_input(varprefix + "_from", value[0])
        html.nbsp()
        html.write_text("-")
        html.nbsp()
        self._bounds[1].render_input(varprefix + "_until", value[1])

    def value_to_text(self, value):
        if value is None:
            return ""

        return self._bounds[0].value_to_text(value[0]) + "-" + \
               self._bounds[1].value_to_text(value[1])

    def from_html_vars(self, varprefix):
=======
    def render_input(self, varprefix: str, value: _Optional[TimeofdayRangeValue]) -> None:
        self._bounds[0].render_input(varprefix + "_from", value[0] if value is not None else None)
        html.nbsp()
        html.write_text("-")
        html.nbsp()
        self._bounds[1].render_input(varprefix + "_until", value[1] if value is not None else None)

    def value_to_text(self, value: _Optional[TimeofdayRangeValue]) -> str:
        if value is None:
            return u""

        return ensure_str(self._bounds[0].value_to_text(value[0]) + "-" +
                          self._bounds[1].value_to_text(value[1]))

    def from_html_vars(self, varprefix: str) -> _Optional[TimeofdayRangeValue]:
>>>>>>> upstream/master
        from_value = self._bounds[0].from_html_vars(varprefix + "_from")
        until_value = self._bounds[1].from_html_vars(varprefix + "_until")
        if (from_value is None) != (until_value is None):
            raise MKUserError(
                varprefix + "_from",
                _("Please leave either both from and until empty or enter two times."))
        if from_value is None:
            return None
<<<<<<< HEAD
        return (from_value, until_value)

    def validate_datatype(self, value, varprefix):
=======
        if until_value is None:
            return None
        return (from_value, until_value)

    def validate_datatype(self, value: _Optional[TimeofdayRangeValue], varprefix: str) -> None:
>>>>>>> upstream/master
        if self._allow_empty and value is None:
            return

        if not isinstance(value, tuple):
            raise MKUserError(varprefix,
                              _("The datatype must be tuple, but ist %s") % _type_name(value))

        if len(value) != 2:
            raise MKUserError(
                varprefix,
                _("The tuple must contain two elements, but you have %d") % len(value))

        self._bounds[0].validate_datatype(value[0], varprefix + "_from")
        self._bounds[1].validate_datatype(value[1], varprefix + "_until")

<<<<<<< HEAD
    def _validate_value(self, value, varprefix):
        if value is None:
            if self._allow_empty:
                return
            else:
                raise MKUserError(varprefix + "_from", _("Please enter a valid time of day range"))
            return
=======
    def _validate_value(self, value: _Optional[TimeofdayRangeValue], varprefix: str) -> None:
        if value is None:
            if self._allow_empty:
                return
            raise MKUserError(varprefix + "_from", _("Please enter a valid time of day range"))
>>>>>>> upstream/master

        self._bounds[0].validate_value(value[0], varprefix + "_from")
        self._bounds[1].validate_value(value[1], varprefix + "_until")
        if value[0] > value[1]:
            raise MKUserError(
                varprefix + "_until",
                _("The <i>from</i> time must not be later then the <i>until</i> time."))


<<<<<<< HEAD
class TimeHelper(object):
    @staticmethod
    def round(timestamp, unit):
        time_s = list(time.localtime(timestamp))
        time_s[3] = time_s[4] = time_s[5] = 0
        time_s[8] = -1
        if unit == 'd':
            return time.mktime(time_s)
        elif unit == 'w':
            days = time_s[6]  # 0 based
        elif unit == 'm':
            days = time_s[2] - 1  # 1 based
        elif unit == 'y':
            days = time_s[7] - 1  # 1 based
        else:
            raise MKGeneralException("invalid time unit %s" % unit)

        return TimeHelper.round(time.mktime(time_s) - days * 86400 + 3600, 'd')

    @staticmethod
    def add(timestamp, count, unit):
        if unit == 'h':
            return timestamp + 3600 * count
        elif unit == 'd':
            return timestamp + 86400 * count
        elif unit == 'w':
            return timestamp + (7 * 86400) * count
        elif unit == 'm':
            time_s = list(time.localtime(timestamp))
            years, months = divmod(abs(count), 12)

            if count < 0:
                years *= -1
                months *= -1

            time_s[0] += years
            time_s[1] += months
            if time_s[1] <= 0:
                time_s[0] -= 1
                time_s[1] = 12 + time_s[1]
            time_s[8] = -1
            return time.mktime(time_s)
        elif unit == 'y':
            time_s = list(time.localtime(timestamp))
            time_s[0] += count
            return time.mktime(time_s)
        else:
            MKGeneralException("invalid time unit %s" % unit)


class Timerange(CascadingDropdown):
    def __init__(  # pylint: disable=redefined-builtin
            self,
            allow_empty=False,  # type: bool
            include_time=False,  # type: bool
            choices=None,  # type: TypingOptional[Union[List[TypingTuple[Text, Text, ValueSpec]], Callable]]
            # CascadingDropdown
            # TODO: Make this more specific
            label=None,  # type: TypingOptional[Text]
            separator=", ",  # type: TypingOptional[Text]
            sorted=True,  # type: bool
            orientation="vertical",  # type: Text
            render=None,  # type: TypingOptional[CascadingDropdown.Render]
            encoding="tuple",  # type: Text
            no_elements_text=None,  # type: TypingOptional[Text]
            no_preselect=False,  # type: bool
            no_preselect_value=None,  # type: TypingOptional[Any]
            no_preselect_title="",  # type: Text
            no_preselect_error=None,  # type: TypingOptional[Text]
            render_sub_vs_page_name=None,  # type: TypingOptional[Text]
            render_sub_vs_request_vars=None,  # type: TypingOptional[Dict]
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Timerange, self).__init__(
=======
class TimeHelper:
    @staticmethod
    def round(timestamp, unit):
        lt = datetime.datetime.fromtimestamp(timestamp, tzlocal()).replace(hour=0,
                                                                           minute=0,
                                                                           second=0)

        if unit == 'w':
            lt -= datetime.timedelta(days=lt.weekday())
        elif unit == 'm':
            lt = lt.replace(day=1)
        elif unit == 'y':
            lt = lt.replace(month=1, day=1)
        elif unit != 'd':
            raise MKGeneralException("invalid time unit %s" % unit)

        return time.mktime(lt.timetuple())
        # py3 return lt.timestamp()

    @staticmethod
    def add(timestamp, count, unit):
        lt = datetime.datetime.fromtimestamp(timestamp, tzlocal())
        if unit == 'h':
            lt += relativedelta(hours=count)
        elif unit == 'd':
            lt += relativedelta(days=count)
        elif unit == 'w':
            lt += relativedelta(days=7 * count)
        elif unit == 'm':
            lt += relativedelta(months=count)
        elif unit == 'y':
            lt += relativedelta(years=count)
        else:
            MKGeneralException("invalid time unit %s" % unit)

        return time.mktime(lt.timetuple())
        # py3 return lt.timestamp()


class Timerange(CascadingDropdown):
    def __init__(  # pylint: disable=redefined-builtin
        self,
        allow_empty: bool = False,
        include_time: bool = False,
        choices: Union[None, List[CascadingDropdownChoice],
                       Callable[[], List[CascadingDropdownChoice]]] = None,
        # CascadingDropdown
        # TODO: Make this more specific
        label: _Optional[str] = None,
        separator: str = ", ",
        sorted: bool = False,
        orientation: str = "vertical",
        render: _Optional[CascadingDropdown.Render] = None,
        no_elements_text: _Optional[str] = None,
        no_preselect: bool = False,
        no_preselect_value: _Optional[Any] = None,
        no_preselect_title: str = "",
        no_preselect_error: _Optional[str] = None,
        render_sub_vs_page_name: _Optional[str] = None,
        render_sub_vs_request_vars: _Optional[Dict] = None,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(
>>>>>>> upstream/master
            choices=self._prepare_choices,
            label=label,
            separator=separator,
            sorted=sorted,
            orientation=orientation,
            render=render,
<<<<<<< HEAD
            encoding=encoding,
=======
>>>>>>> upstream/master
            no_elements_text=no_elements_text,
            no_preselect=no_preselect,
            no_preselect_value=no_preselect_value,
            no_preselect_title=no_preselect_title,
            no_preselect_error=no_preselect_error,
            render_sub_vs_page_name=render_sub_vs_page_name,
            render_sub_vs_request_vars=render_sub_vs_request_vars,
            title=title,
            help=help,
            default_value=default_value,
            validate=validate,
        )
        self._title = title if title is not None else _('Time range')
        self._allow_empty = allow_empty
        self._include_time = include_time
<<<<<<< HEAD
        self._fixed_choices = choices or []

    def _prepare_choices(self):
        choices = list(self._fixed_choices)

        if self._allow_empty:
            choices += [(None, '')]

        choices += self._get_graph_timeranges() + [
            ("d0", _("Today")),
            ("d1", _("Yesterday")),
            ("w0", _("This week")),
            ("w1", _("Last week")),
=======
        self._fixed_choices = choices

    def _prepare_choices(self) -> List[CascadingDropdownChoice]:
        # TODO: We have dispatching code like this all over place...
        if self._fixed_choices is None:
            choices: List[CascadingDropdownChoice] = []
        elif isinstance(self._fixed_choices, list):
            choices = list(self._fixed_choices)
        elif callable(self._fixed_choices):
            choices = self._fixed_choices()
        else:
            raise ValueError("invalid type for choices")

        if self._allow_empty:
            choices += [(None, '', None)]

        choices.extend(self._get_graph_timeranges())
        choices.extend([
            ("d0", _("Today")),
            ("d1", _("Yesterday")),
            ("d7", _("7 days back (this day last week)")),
            ("d8", _("8 days back")),
            ("w0", _("This week")),
            ("w1", _("Last week")),
            ("w2", _("2 weeks back")),
>>>>>>> upstream/master
            ("m0", _("This month")),
            ("m1", _("Last month")),
            ("y0", _("This year")),
            ("y1", _("Last year")),
            ("age", _("The last..."), Age()),
            ("date", _("Date range"),
             Tuple(orientation="horizontal",
                   title_br=False,
                   elements=[
                       AbsoluteDate(title=_("From:")),
                       AbsoluteDate(title=_("To:")),
                   ])),
<<<<<<< HEAD
        ]
=======
        ])
>>>>>>> upstream/master

        if self._include_time:
            choices += [("time", _("Date & time range"),
                         Tuple(orientation="vertical",
                               title_br=False,
                               elements=[
                                   AbsoluteDate(
                                       title=_("From:"),
                                       include_time=True,
                                   ),
                                   AbsoluteDate(
                                       title=_("To:"),
                                       include_time=True,
                                   ),
                               ]))]
        return choices

<<<<<<< HEAD
    def _get_graph_timeranges(self):
        try:
            import cmk.gui.config as config  # FIXME
            return [(('age', timerange_attrs["duration"]), timerange_attrs['title'])
                    for timerange_attrs in config.graph_timeranges]

        except AttributeError:  # only available in cee
            return [
=======
    def _get_graph_timeranges(self) -> List[CascadingDropdownCleanChoice]:
        try:
            return _normalize_choices([(timerange_attrs["duration"], timerange_attrs['title'])
                                       for timerange_attrs in config.graph_timeranges])

        except AttributeError:  # only available in cee
            return _normalize_choices([
>>>>>>> upstream/master
                ("4h", _("The last 4 hours")),
                ("25h", _("The last 25 hours")),
                ("8d", _("The last 8 days")),
                ("35d", _("The last 35 days")),
                ("400d", _("The last 400 days")),
<<<<<<< HEAD
            ]

    def compute_range(self, rangespec):
        if rangespec is None:
            rangespec = "4h"
=======
            ])

    def value_to_text(self, value: CascadingDropdownChoiceValue):
        for ident, title, _vs in self._get_graph_timeranges():
            if value == ident:
                return title
            # Cleanup on Werk 4477, treat old(pre 2.0) casted defaults earlier
            if isinstance(value, tuple) and value == ("age", ident):
                return title

        return super().value_to_text(value)

    def value_to_json(self, value: CascadingDropdownChoiceValue):
        if isinstance(value, int):  # Handle default graph_timeranges
            value = ("age", value)
        return super().value_to_json(value)

    def value_from_json(self, json_value):
        value = super().value_from_json(json_value)
        # Handle default graph_timeranges
        for ident, _title, _vs in self._get_graph_timeranges():
            if value == ("age", ident):
                return ident
        return value

    def compute_range(self, rangespec):
        def _date_span(from_time, until_time):
            start = AbsoluteDate().value_to_text(from_time)
            end = AbsoluteDate().value_to_text(until_time - 1)
            if start == end:
                return start
            return start + u" \u2014 " + end

        def _month_edge_days(now: float, day_id: str) -> _Tuple[_Tuple[float, float], str]:
            # base time is current time rounded down to month
            from_time = TimeHelper.round(now, 'm')
            if day_id == 'f1':
                from_time = TimeHelper.add(from_time, -1, 'm')
            if day_id == 'l1':
                from_time = TimeHelper.add(from_time, -1, 'd')
            end_time = TimeHelper.add(from_time, 1, 'd')
            return (from_time, end_time), time.strftime("%d/%m/%Y", time.localtime(from_time))

        def _fixed_dates(rangespec):
            from_time, until_time = rangespec[1]
            if from_time > until_time:
                raise MKUserError("avo_rangespec_9_0_year",
                                  _("The end date must be after the start date"))
            if rangespec[0] == 'date':
                # This includes the end day
                until_time = TimeHelper.add(until_time, 1, 'd')
            return (from_time, until_time), _date_span(from_time, until_time)

        if rangespec is None:
            rangespec = "4h"
        elif isinstance(rangespec, int):
            rangespec = ("age", rangespec)
>>>>>>> upstream/master

        # Compatibility with previous versions
        elif rangespec[0] == "pnp_view":
            rangespec = {
                1: "4h",
                2: "25h",
                3: "8d",
                4: "35d",
                5: "400d",
            }.get(rangespec[1], "4h")

        now = time.time()

        if rangespec[0] == 'age':
<<<<<<< HEAD
            from_time = now - rangespec[1]
            until_time = now
            title = _("The last ") + Age().value_to_text(rangespec[1])
            return (from_time, until_time), title
        elif rangespec[0] == 'next':
            from_time = now
            until_time = now + rangespec[1]
            title = _("The next ") + Age().value_to_text(rangespec[1])
            return (from_time, until_time), title
        elif rangespec[0] == 'until':
            return (now, rangespec[1]), AbsoluteDate().value_to_text(rangespec[1])

        elif rangespec[0] in ['date', 'time']:
            from_time, until_time = rangespec[1]
            if from_time > until_time:
                raise MKUserError("avo_rangespec_9_0_year",
                                  _("The end date must be after the start date"))
            if rangespec[0] == 'date':
                # add 25 hours, then round to 00:00 of that day. This accounts for
                # daylight-saving time
                until_time = TimeHelper.round(TimeHelper.add(until_time, 25, 'h'), 'd')
            title = AbsoluteDate().value_to_text(from_time) + " ... " + \
                    AbsoluteDate().value_to_text(until_time)
            return (from_time, until_time), title

        else:
            until_time = now
            if rangespec[0].isdigit():  # 4h, 400d
                count = int(rangespec[:-1])
                from_time = TimeHelper.add(now, count * -1, rangespec[-1])
                unit_name = {'d': "days", 'h': "hours"}[rangespec[-1]]
                title = _("Last %d %s") % (count, unit_name)
                return (from_time, now), title

            year, month = time.localtime(now)[:2]
            # base time is current time rounded down to the nearest unit (day, week, ...)
            from_time = TimeHelper.round(now, rangespec[0])
            # derive titles from unit ()
            titles = {
                'd': (_("Today"), _("Yesterday")),
                'w': (_("This week"), _("Last week")),
                'y': (str(year), None),
                'm': ("%s %d" % (defines.month_name(month - 1), year), None),
            }[rangespec[0]]

            if rangespec[1] == '0':
                return (from_time, now), titles[0]

            # last (previous)
            prev_time = TimeHelper.add(from_time, -1 * int(rangespec[1:]), rangespec[0])
            # add one hour to the calculated time so that if dst started in that period,
            # we don't round down a whole day
            prev_time = TimeHelper.round(prev_time + 3600, 'd')

            # This only works for Months, but those are the only defaults in Forecast Graphs
            # Language localization to system language not CMK GUI language
            if prev_time > from_time:
                from_time, prev_time = prev_time, from_time
            prev_time_str = time.strftime("%B %Y", time.localtime(prev_time))
            end_time_str = time.strftime("%B %Y", time.localtime(from_time - 1))
            if prev_time_str != end_time_str:
                prev_time_str += " - " + end_time_str
            if rangespec[0] == "y":
                prev_time_str = time.strftime("%Y", time.localtime(prev_time))

            return (prev_time, from_time), titles[1] or prev_time_str
=======
            title = _("The last ") + Age().value_to_text(rangespec[1])
            return (now - rangespec[1], now), title
        if rangespec[0] == 'next':
            title = _("The next ") + Age().value_to_text(rangespec[1])
            return (now, now + rangespec[1]), title
        if rangespec[0] == 'until':
            return (now, rangespec[1]), AbsoluteDate().value_to_text(rangespec[1])
        if rangespec[0] in ['date', 'time']:
            return _fixed_dates(rangespec)

        if rangespec[0].isdigit():  # 4h, 400d
            count = int(rangespec[:-1])
            from_time = TimeHelper.add(now, count * -1, rangespec[-1])
            unit_name = {'d': "days", 'h': "hours"}[rangespec[-1]]
            title = _("Last %d %s") % (count, unit_name)
            return (from_time, now), title

        if rangespec in ['f0', 'f1', 'l1']:
            return _month_edge_days(now, rangespec)

        # base time is current time rounded down to the nearest unit (day, week, ...)
        from_time = TimeHelper.round(now, rangespec[0])
        year, month = time.localtime(now)[:2]
        # derive titles from unit ()
        titles = {
            'd': (_("Today"), _("Yesterday")),
            'w': (_("This week"), _("Last week")),
            'y': (str(year), None),
            'm': ("%s %d" % (defines.month_name(month - 1), year), None),
        }[rangespec[0]]

        if rangespec[1] == '0':
            return (from_time, now), titles[0]

        # last (previous)
        span = int(rangespec[1:])
        prev_time = TimeHelper.add(from_time, -1 * span, rangespec[0])
        # day and week spans for historic data
        if rangespec[0] in ['d', 'w']:
            end_time = TimeHelper.add(prev_time, 1, rangespec[0])
            title = _date_span(prev_time, end_time) if span > 1 else titles[1]
            return (prev_time, end_time), title

        # This only works for Months, but those are the only defaults in Forecast Graphs
        # Language localization to system language not CMK GUI language
        if prev_time > from_time:
            from_time, prev_time = prev_time, from_time
        prev_time_str: str = time.strftime("%B %Y", time.localtime(prev_time))
        end_time_str = time.strftime("%B %Y", time.localtime(from_time - 1))
        if prev_time_str != end_time_str:
            prev_time_str += u" \u2014 " + end_time_str
        if rangespec[0] == "y":
            prev_time_str = time.strftime("%Y", time.localtime(prev_time))

        return (prev_time, from_time), titles[1] or prev_time_str
>>>>>>> upstream/master


# TODO: Cleanup kwargs
def DateFormat(**kwargs):
    """A selection of various date formats"""
    kwargs.setdefault("title", _("Date format"))
    kwargs.setdefault("default_value", "%Y-%m-%d")
<<<<<<< HEAD
=======
    kwargs.setdefault("encode_value", False)
>>>>>>> upstream/master
    return DropdownChoice(choices=[
        ("%Y-%m-%d", "1970-12-18"),
        ("%d.%m.%Y", "18.12.1970"),
        ("%m/%d/%Y", "12/18/1970"),
        ("%d.%m.", "18.12."),
        ("%m/%d", "12/18"),
    ],
                          **kwargs)


# TODO: Cleanup kwargs
def TimeFormat(**kwargs):
    kwargs.setdefault("title", _("Time format"))
    kwargs.setdefault("default_value", "%H:%M:%S")
    return DropdownChoice(choices=[
        ("%H:%M:%S", "18:27:36"),
        ("%l:%M:%S %p", "12:27:36 PM"),
        ("%H:%M", "18:27"),
        ("%l:%M %p", "6:27 PM"),
        ("%H", "18"),
        ("%l %p", "6 PM"),
    ],
                          **kwargs)


class Optional(ValueSpec):
    """Make a configuration value optional, i.e. it may be None.

    The user has a checkbox for activating the option. Example:
    debug_log: it is either None or set to a filename."""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            valuespec,  # type: ValueSpec
            label=None,  # type: TypingOptional[Text]
            negate=False,  # type: bool
            none_label=None,  # type: TypingOptional[Text]
            none_value=None,  # type: Any
            sameline=False,  # type: bool
            indent=True,  # type: bool
            allow_empty=True,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Optional, self).__init__(title=title,
                                       help=help,
                                       default_value=default_value,
                                       validate=validate)
=======
        self,
        valuespec: ValueSpec,
        label: _Optional[str] = None,
        negate: bool = False,
        none_label: _Optional[str] = None,
        none_value: Any = None,
        sameline: bool = False,
        indent: bool = True,
        allow_empty: bool = True,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._valuespec = valuespec
        self._label = label
        self._negate = negate
        self._none_label = none_label if none_label is not None else _("(unset)")
        self._none_value = none_value
        self._sameline = sameline
        self._indent = indent

    def canonical_value(self):
        return self._none_value

    def render_input(self, varprefix, value):
        div_id = "option_" + varprefix
        checked = html.get_checkbox(varprefix + "_use")
        if checked is None:
            if self._negate:
                checked = value == self._none_value
            else:
                checked = value != self._none_value

        html.open_span()
<<<<<<< HEAD

        if self._label is not None:
            label = self._label
        elif self.title():
            label = self.title()
        elif self._negate:
            label = _(" Ignore this option")
        else:
            label = _(" Activate this option")

        html.checkbox("%s_use" % varprefix,
                      checked,
                      label=label,
                      onclick="cmk.valuespecs.toggle_option(this, %r, %r)" %
                      (div_id, 1 if self._negate else 0))

=======
        html.checkbox("%s_use" % varprefix,
                      checked,
                      label=self._get_label(),
                      onclick="cmk.valuespecs.toggle_option(this, %s, %r)" %
                      (json.dumps(div_id), 1 if self._negate else 0))
>>>>>>> upstream/master
        if self._sameline:
            html.nbsp()
        else:
            html.br()
        html.close_span()

        if self._indent:
            indent = 40
        else:
            indent = 0

        html.open_span(id_=div_id,
                       style=[
                           "margin-left: %dpx;" % indent,
                           "display:none;" if checked == self._negate else None
                       ])
        if value == self._none_value:
            value = self._valuespec.default_value()
        if self._valuespec.title():
<<<<<<< HEAD
            html.write(self._valuespec.title() + " ")
        self._valuespec.render_input(varprefix + "_value", value)
        html.close_span()

=======
            the_title = self._valuespec.title()
            html.write(("???" if the_title is None else the_title) + " ")
        self._valuespec.render_input(varprefix + "_value", value)
        html.close_span()

    def _get_label(self) -> str:
        if self._label is not None:
            return self._label
        t = self.title()
        if t:
            return t
        if self._negate:
            return _(" Ignore this option")
        return _(" Activate this option")

>>>>>>> upstream/master
    def value_to_text(self, value):
        if value == self._none_value:
            return self._none_label
        return self._valuespec.value_to_text(value)

    def from_html_vars(self, varprefix):
        checkbox_checked = html.get_checkbox(varprefix + "_use") is True  # not None or False
        if checkbox_checked != self._negate:
            return self._valuespec.from_html_vars(varprefix + "_value")
        return self._none_value

    def validate_datatype(self, value, varprefix):
        if value != self._none_value:
            self._valuespec.validate_datatype(value, varprefix + "_value")

    def _validate_value(self, value, varprefix):
        if value != self._none_value:
            self._valuespec.validate_value(value, varprefix + "_value")

<<<<<<< HEAD
=======
    def transform_value(self, value):
        return self._valuespec.transform_value(value)

>>>>>>> upstream/master

class Alternative(ValueSpec):
    """Handle case when there are several possible allowed formats
    for the value (e.g. strings, 4-tuple or 6-tuple like in SNMP-Communities)
    The different alternatives must have different data types that can
    be distinguished with validate_datatype."""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            elements,  # type: List[ValueSpec]
            match=None,  # type: TypingOptional[Callable[[Any], int]]
            style="radio",  # type: Text
            show_alternative_title=False,  # type: bool
            on_change=None,  # type: TypingOptional[Text]
            orientation="vertical",  # type: Text
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Alternative, self).__init__(title=title,
                                          help=help,
                                          default_value=default_value,
                                          validate=validate)
        self._elements = elements
        self._match = match  # custom match function, returns index in elements
        self._style = style  # alternative: "dropdown"
        self._show_alternative_title = show_alternative_title
        self._on_change = on_change  # currently only working for style="dropdown"
        self._orientation = orientation  # or horizontal: for style="dropdown"
=======
        self,
        elements: List[ValueSpec],
        match: _Optional[Callable[[Any], int]] = None,
        style: str = "",  # Unused argument left here to remain compatible with user extensions.
        show_alternative_title: bool = False,
        on_change: _Optional[str] = None,
        orientation: str = "vertical",
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        self._elements = elements
        self._match = match  # custom match function, returns index in elements
        self._show_alternative_title = show_alternative_title
        self._on_change = on_change
        self._orientation = orientation  # or horizontal
>>>>>>> upstream/master

    # Return the alternative (i.e. valuespec)
    # that matches the datatype of a given value. We assume
    # that always one matches. No error handling here.
    # This may also tranform the input value in case it gets
    # "decorated" in the from_html_vars function
    def matching_alternative(self, value):
        if self._match:
            return self._elements[self._match(value)], value

        for vs in self._elements:
            try:
                vs.validate_datatype(value, "")
                return vs, value
            except Exception:
                pass

        return None, value

    def render_input(self, varprefix, value):
<<<<<<< HEAD
        if self._style == "radio":
            self.render_input_radio(varprefix, value)
        else:
            self.render_input_dropdown(varprefix, value)

    def render_input_dropdown(self, varprefix, value):
        mvs, value = self.matching_alternative(value)
        options = []
=======
        mvs, value = self.matching_alternative(value)
        options: List[_Tuple[_Optional[str], str]] = []
>>>>>>> upstream/master
        sel_option = html.request.var(varprefix + "_use")
        for nr, vs in enumerate(self._elements):
            if not sel_option and vs == mvs:
                sel_option = str(nr)
<<<<<<< HEAD
            options.append((str(nr), vs.title()))
        onchange = "cmk.valuespecs.cascading_change(this, '%s', %d);" % (varprefix, len(options))
=======
            the_title = vs.title()
            options.append((str(nr), "???" if the_title is None else the_title))
        onchange = u"cmk.valuespecs.cascading_change(this, '%s', %d);" % (varprefix, len(options))
>>>>>>> upstream/master
        if self._on_change:
            onchange += self._on_change
        if self._orientation == "horizontal":
            html.open_table()
            html.open_tr()
            html.open_td()
<<<<<<< HEAD
        html.dropdown(varprefix + "_use", options, deflt=sel_option, onchange=onchange)
=======
        html.dropdown(varprefix + "_use",
                      options,
                      deflt=("???" if sel_option is None else sel_option),
                      onchange=onchange)
>>>>>>> upstream/master
        if self._orientation == "vertical":
            html.br()
            html.br()

        for nr, vs in enumerate(self._elements):
            if str(nr) == sel_option:
                disp = ""
                cur_val = value
            else:
                disp = "none"
                cur_val = vs.default_value()

            if self._orientation == "horizontal":
                html.close_td()
                html.open_td()
            html.open_span(id_="%s_%s_sub" % (varprefix, nr), style="display:%s" % disp)
            html.help(vs.help())
            vs.render_input(varprefix + "_%d" % nr, cur_val)
            html.close_span()

        if self._orientation == "horizontal":
            html.close_td()
            html.close_tr()
            html.close_table()

<<<<<<< HEAD
    def render_input_radio(self, varprefix, value):
        mvs, value = self.matching_alternative(value)
        for nr, vs in enumerate(self._elements):
            if html.request.has_var(varprefix + "_use"):
                checked = html.request.var(varprefix + "_use") == str(nr)
            else:
                checked = vs == mvs

            html.help(vs.help())
            title = vs.title()
            if not title and nr:
                html.nbsp()
                html.nbsp()

            html.radiobutton(varprefix + "_use", str(nr), checked, title)
            if title:
                html.open_ul()
            if vs == mvs:
                val = value
            else:
                val = vs.default_value()
            vs.render_input(varprefix + "_%d" % nr, val)
            if title:
                html.close_ul()

=======
>>>>>>> upstream/master
    def set_focus(self, varprefix):
        # TODO: Set focus to currently active option
        pass

    def canonical_value(self):
        return self._elements[0].canonical_value()

    def default_value(self):
        try:
            if isinstance(self._default_value, type(lambda: True)):
                return self._default_value()
            return self._default_value
        except Exception:
            return self._elements[0].default_value()

    def value_to_text(self, value):
        vs, value = self.matching_alternative(value)
        if vs:
            output = ""
            if self._show_alternative_title and vs.title():
                output = "%s<br>" % vs.title()
            return output + vs.value_to_text(value)
<<<<<<< HEAD
        else:
            return _("invalid:") + " " + html.attrencode(str(value))

    def from_html_vars(self, varprefix):
        nr = int(html.request.var(varprefix + "_use"))
=======
        return _("invalid:") + " " + escaping.escape_attribute(str(value))

    def from_html_vars(self, varprefix):
        nr = html.request.get_integer_input_mandatory(varprefix + "_use")
>>>>>>> upstream/master
        vs = self._elements[nr]
        return vs.from_html_vars(varprefix + "_%d" % nr)

    def validate_datatype(self, value, varprefix):
        for vs in self._elements:
            try:
                vs.validate_datatype(value, "")
                return
            except Exception:
                pass
        raise MKUserError(
            varprefix,
            _("The data type of the value does not match any of the "
              "allowed alternatives."))

    def _validate_value(self, value, varprefix):
        vs, value = self.matching_alternative(value)
        for nr, v in enumerate(self._elements):
            if vs == v:
                vs.validate_value(value, varprefix + "_%d" % nr)


class Tuple(ValueSpec):
    """Edit a n-tuple (with fixed size) of values"""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            elements,  # type: List[ValueSpec]
            show_titles=True,  # type: bool
            orientation="vertical",  # type: str
            separator=" ",  # type: Text
            title_br=True,  # type: bool
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Tuple, self).__init__(title=title,
                                    help=help,
                                    default_value=default_value,
                                    validate=validate)
=======
        self,
        elements: List[ValueSpec],
        show_titles: bool = True,
        orientation: str = "vertical",
        separator: str = " ",
        title_br: bool = True,
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._elements = elements
        self._show_titles = show_titles
        self._orientation = orientation  # also: horizontal, float
        self._separator = separator  # in case of float
        self._title_br = title_br

    def canonical_value(self):
        return tuple([x.canonical_value() for x in self._elements])

    def default_value(self):
        return tuple([x.default_value() for x in self._elements])

    def render_input(self, varprefix, value):
        if self._orientation != "float":
            html.open_table(class_=["valuespec_tuple", self._orientation])
            if self._orientation == "horizontal":
                html.open_tr()

        for no, element in enumerate(self._elements):
            try:
                val = value[no]
            except (TypeError, IndexError):
                val = element.default_value()
            vp = varprefix + "_" + str(no)
            if self._orientation == "vertical":
                html.open_tr()
            elif self._orientation == "float":
                html.write(self._separator)

            if self._show_titles:
                elem_title = element.title()
                if elem_title:
<<<<<<< HEAD
                    title = element.title()[0].upper() + element.title()[1:]
=======
                    title = elem_title[0].upper() + elem_title[1:]
>>>>>>> upstream/master
                else:
                    title = ""
                if self._orientation == "vertical":
                    html.open_td(class_="tuple_left")
                    html.write(title)

                    html.close_td()
                elif self._orientation == "horizontal":
                    html.open_td(class_="tuple_td")
                    html.open_span(class_=["title"])
                    html.write(title)

                    html.close_span()
                    if self._title_br:
                        html.br()
                    else:
                        html.write_text(" ")
                else:
                    html.write_text(" ")

            else:
                if self._orientation == "horizontal":
                    html.open_td(class_="tuple_td")

            if self._orientation == "vertical":
                html.open_td(class_="tuple_right")

            html.help(element.help())
            element.render_input(vp, val)
            if self._orientation != "float":
                html.close_td()
                if self._orientation == "vertical":
                    html.close_tr()
        if self._orientation == "horizontal":
            html.close_tr()
        if self._orientation != "float":
            html.close_table()

    def set_focus(self, varprefix):
        self._elements[0].set_focus(varprefix + "_0")

    def value_to_text(self, value):
        return "" + ", ".join(
            [element.value_to_text(val) for (element, val) in zip(self._elements, value)]) + ""

<<<<<<< HEAD
=======
    def value_to_json(self, value):
        json_value = []
        for idx, element in enumerate(self._elements):
            json_value.append(element.value_to_json(value[idx]))
        return json_value

    def value_from_json(self, json_value):
        real_value = []
        for idx, element in enumerate(self._elements):
            real_value.append(element.value_from_json(json_value[idx]))
        return tuple(real_value)

>>>>>>> upstream/master
    def from_html_vars(self, varprefix):
        value = []
        for no, element in enumerate(self._elements):
            vp = varprefix + "_" + str(no)
            value.append(element.from_html_vars(vp))
        return tuple(value)

    def _validate_value(self, value, varprefix):
        for no, (element, val) in enumerate(zip(self._elements, value)):
            vp = varprefix + "_" + str(no)
            element.validate_value(val, vp)

    def validate_datatype(self, value, varprefix):
        if not isinstance(value, tuple):
            raise MKUserError(varprefix,
                              _("The datatype must be a tuple, but is %s") % _type_name(value))
        if len(value) != len(self._elements):
            raise MKUserError(
                varprefix,
                _("The number of elements in the tuple must be exactly %d.") % len(self._elements))

        for no, (element, val) in enumerate(zip(self._elements, value)):
            vp = varprefix + "_" + str(no)
            element.validate_datatype(val, vp)

<<<<<<< HEAD
=======
    def transform_value(self, value: _Tuple[Any, ...]) -> _Tuple[Any, ...]:
        assert isinstance(value, tuple), "Tuple.transform_value() got a non-tuple: %r" % (value,)
        return tuple(vs.transform_value(value[index]) for index, vs in enumerate(self._elements))


DictionaryEntry = _Tuple[str, ValueSpec]
DictionaryElements = Union[List[DictionaryEntry], Callable[[], List[DictionaryEntry]]]

>>>>>>> upstream/master

class Dictionary(ValueSpec):
    # TODO: Cleanup ancient "migrate"
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            elements,  # type: List[TypingTuple[str, ValueSpec]]
            empty_text=None,  # type: TypingOptional[Text]
            default_text=None,  # type: TypingOptional[Text]
            optional_keys=True,  # type: Union[bool, List[str]]
            required_keys=None,  # type: TypingOptional[List[str]]
            ignored_keys=None,  # type: TypingOptional[List[str]]
            default_keys=None,  # type: TypingOptional[List[str]]
            hidden_keys=None,  # type: TypingOptional[List[str]]
            columns=1,  # type: int
            render="normal",  # type: str
            form_narrow=False,  # type: bool
            form_isopen=True,  # type: bool
            headers=None,  # type: TypingOptional[Union[str, List[Union[TypingTuple[str, List[str]], TypingTuple[str, str, List[str]]]]]]
            migrate=None,  # type: Callable[[TypingTuple], Dict]
            indent=True,  # type: bool
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Dictionary, self).__init__(title=title,
                                         help=help,
                                         default_value=default_value,
                                         validate=validate)
=======
        self,
        elements: DictionaryElements,
        empty_text: _Optional[str] = None,
        default_text: _Optional[str] = None,
        optional_keys: Union[bool, List[str]] = True,
        required_keys: _Optional[List[str]] = None,
        show_more_keys: _Optional[List[str]] = None,
        ignored_keys: _Optional[List[str]] = None,
        default_keys: _Optional[List[str]] = None,
        hidden_keys: _Optional[List[str]] = None,
        columns: int = 1,
        render: str = "normal",
        form_narrow: bool = False,
        form_isopen: bool = True,
        headers: Union[None, str, List[Union[_Tuple[str, List[str]], _Tuple[str, str,
                                                                            List[str]]]]] = None,
        migrate: _Optional[Callable[[_Tuple], Dict]] = None,
        indent: bool = True,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._elements = elements
        self._empty_text = empty_text if empty_text is not None else _("(no parameters)")

        # Optionally a text can be specified to be shown by value_to_text()
        # when the value equal the default value of the value spec. Normally
        # the default values are shown.
        self._default_text = default_text
        self._required_keys = required_keys or []
<<<<<<< HEAD
=======
        self._show_more_keys = show_more_keys or []
>>>>>>> upstream/master
        self._ignored_keys = ignored_keys or []
        self._default_keys = default_keys or []  # keys present in default value
        self._hidden_keys = hidden_keys or []

        if isinstance(optional_keys, list) and optional_keys:
            self._required_keys = [e[0] for e in self._get_elements() if e[0] not in optional_keys]
            self._optional_keys = True
        elif optional_keys:
            self._optional_keys = True
        else:
            self._optional_keys = False

        self._columns = columns  # possible: 1 or 2
        self._render = render  # also: "form" -> use forms.section()
        self._form_narrow = form_narrow  # used if render == "form"
        self._form_isopen = form_isopen  # used if render == "form"
        self._headers = headers  # "sup" -> small headers in oneline mode
        self._migrate = migrate  # value migration from old tuple version
        self._indent = indent

    def migrate(self, value):
        if self._migrate:
            return self._migrate(value)
        return value

    def _get_elements(self):
<<<<<<< HEAD
        if hasattr(self._elements, '__call__') or isinstance(self._elements, types.MethodType):
            return self._elements()
        elif isinstance(self._elements, list):
=======
        if callable(self._elements):
            return self._elements()
        if isinstance(self._elements, list):
>>>>>>> upstream/master
            return self._elements
        return []

    def render_input_as_form(self, varprefix, value):
<<<<<<< HEAD
        value = self.migrate(value)
        if not isinstance(value, (dict, DictMixin)):
            value = {}  # makes code simpler in complain phase

        self._render_input_form(varprefix, value)

    def render_input(self, varprefix, value):
        value = self.migrate(value)
        if not isinstance(value, (dict, DictMixin)):
            value = {}  # makes code simpler in complain phase

        if self._render == "form":
            self._render_input_form(varprefix, value)
        elif self._render == "form_part":
            self._render_input_form(varprefix, value, as_part=True)
        else:
            self._render_input_normal(varprefix, value, self._render == "oneline")

    def _render_input_normal(self, varprefix, value, oneline=False):
        headers_sup = oneline and self._headers == "sup"
        if headers_sup or not oneline:
            html.open_table(class_=["dictionary"])
        if headers_sup:
=======
        self._render_input(varprefix, value, "form")

    def render_input(self, varprefix, value):
        self._render_input(varprefix, value, self._render)

    def _render_input(self, varprefix, value, render):
        value = self.migrate(value)
        if not isinstance(value, MutableMapping):
            value = {}  # makes code simpler in complain phase

        if render == "form":
            self._render_input_form(varprefix, value)
        elif render == "form_part":
            self._render_input_form(varprefix, value, as_part=True)
        else:
            self._render_input_normal(varprefix,
                                      value,
                                      oneline=render == "oneline",
                                      small_headers=self._headers == "sup",
                                      two_columns=self._columns == 2)

    def _render_input_normal(self, varprefix, value, oneline, small_headers, two_columns):
        if not oneline or small_headers:
            html.open_table(class_=["dictionary"])
        if oneline and small_headers:
>>>>>>> upstream/master
            html.open_tr()
        for param, vs in self._get_elements():
            if param in self._hidden_keys:
                continue
            if not oneline:
                html.open_tr()
                html.open_td(class_="dictleft")

            div_id = varprefix + "_d_" + param
            vp = varprefix + "_p_" + param
            colon_printed = False
            if self._optional_keys and param not in self._required_keys:
<<<<<<< HEAD
                visible = html.get_checkbox(vp + "_USE")
                if visible is None:
                    visible = param in value
                label = vs.title()
                if self._columns == 2:
                    label += ":"
                    colon_printed = True
                html.checkbox("%s_USE" % vp,
                              visible,
                              label=label,
                              onclick="cmk.valuespecs.toggle_option(this, %r)" % div_id)
            else:
                visible = True
                if vs.title():
                    if headers_sup:
                        html.open_td()
                        html.open_b(class_=["header"])
                    html.write(" %s" % vs.title())
                    if oneline:
                        if self._headers == "sup":
                            html.close_b()
                            html.br()
                        else:
                            html.write_text(": ")

            if self._columns == 2:
=======
                checkbox_varname = vp + "_USE"
                visible = html.get_checkbox(checkbox_varname)
                if visible is None:
                    visible = param in value
                label = vs.title()
                if two_columns:
                    label += ":"
                    colon_printed = True
                html.checkbox(checkbox_varname,
                              visible,
                              label=label,
                              onclick="cmk.valuespecs.toggle_option(this, %s)" % json.dumps(div_id))
            else:
                visible = True
                if vs.title():
                    if oneline and small_headers:
                        html.open_td()
                        html.open_b(class_=["header"])
                    html.write(" %s" % vs.title())
                    if oneline and small_headers:
                        html.close_b()
                        html.br()
                    if oneline and not small_headers:
                        html.write_text(": ")

            if two_columns:
>>>>>>> upstream/master
                if vs.title() and not colon_printed:
                    html.write_text(':')
                html.help(vs.help())
                if not oneline:
                    html.close_td()
                    html.open_td(class_="dictright")

            else:
                if not oneline:
                    html.br()

            html.open_div(
                id_=div_id,
<<<<<<< HEAD
                class_=["dictelement", "indent" if (self._indent and self._columns == 1) else None],
                style="display:none;" if not visible else
                ("display:inline-block;" if oneline else None))

            if self._columns == 1:
=======
                class_=["dictelement", "indent" if (self._indent and not two_columns) else None],
                style="display:none;" if not visible else
                ("display:inline-block;" if oneline else None))

            if not two_columns:
>>>>>>> upstream/master
                html.help(vs.help())
            # Remember: in complain mode we do not render 'value' (the default value),
            # but re-display the values from the HTML variables. We must not use 'value'
            # in that case.
<<<<<<< HEAD
            if isinstance(value, dict):
                vs.render_input(vp, value.get(param, vs.default_value()))
            else:
                vs.render_input(vp, None)
            html.close_div()
            if not oneline:
                html.close_td()
                html.close_tr()
            elif headers_sup:
                html.close_td()

        if not oneline:
            html.close_table()
        elif oneline and self._headers == "sup":
            html.close_tr()
            html.close_table()

    def _render_input_form(self, varprefix, value, as_part=False):
        if self._headers:
            for entry in self._headers:
                if len(entry) == 2:
                    header, section_elements = entry
                    css = None
                else:
                    header, css, section_elements = entry
                self.render_input_form_header(varprefix,
                                              value,
                                              header,
                                              section_elements,
                                              as_part,
                                              css=css)
        else:
            self.render_input_form_header(varprefix,
                                          value,
                                          self.title() or _("Properties"),
                                          None,
                                          as_part,
                                          css=None)

        if not as_part:
            forms.end()

    def render_input_form_header(self, varprefix, value, title, section_elements, as_part, css):
        if not as_part:
            forms.header(title, isopen=self._form_isopen, narrow=self._form_narrow)
=======
            the_value = value.get(param, vs.default_value()) if isinstance(value, dict) else None
            vs.render_input(vp, the_value)
            html.close_div()
            if not oneline or small_headers:
                html.close_td()
            if not oneline:
                html.close_tr()

        if oneline and small_headers:
            html.close_tr()
        if not oneline or small_headers:
            html.close_table()

    def _render_input_form(self, varprefix, value, as_part=False):
        headers = self._headers if self._headers else [(ensure_str(self.title() or _("Properties")),
                                                        [])]
        for header, css, section_elements in map(self._normalize_header, headers):
            self.render_input_form_header(varprefix,
                                          value,
                                          header,
                                          section_elements,
                                          as_part,
                                          css=css)
        if not as_part:
            forms.end()

    @staticmethod
    def _normalize_header(header):
        if isinstance(header, tuple):
            if len(header) == 2:
                return header[0], None, header[1]
            if len(header) == 3:
                return header[0], header[1], header[2]
            raise ValueError("invalid header tuple length")
        raise ValueError("invalid header type")

    def render_input_form_header(self, varprefix, value, title, section_elements, as_part, css):
        if not as_part:
            forms.header(title,
                         isopen=self._form_isopen,
                         narrow=self._form_narrow,
                         show_more_toggle=bool(self._show_more_keys))
>>>>>>> upstream/master

        for param, vs in self._get_elements():
            if param in self._hidden_keys:
                continue

            if section_elements and param not in section_elements:
                continue

            div_id = varprefix + "_d_" + param
            vp = varprefix + "_p_" + param
            if self._optional_keys and param not in self._required_keys:
                visible = html.get_checkbox(vp + "_USE")
                if visible is None:
                    visible = param in value
                checkbox_code = html.render_checkbox(
                    vp + "_USE",
                    deflt=visible,
<<<<<<< HEAD
                    onclick="cmk.valuespecs.toggle_option(this, %r)" % div_id)
                forms.section(vs.title(), checkbox=checkbox_code, css=css)
            else:
                visible = True
                forms.section(vs.title(), css=css)
=======
                    onclick="cmk.valuespecs.toggle_option(this, %s)" % json.dumps(div_id))
                forms.section(vs.title(),
                              checkbox=checkbox_code,
                              css=css,
                              is_show_more=param in self._show_more_keys)
            else:
                visible = True
                forms.section(vs.title(), css=css, is_show_more=param in self._show_more_keys)
>>>>>>> upstream/master

            html.open_div(id_=div_id, style="display:none;" if not visible else None)
            html.help(vs.help())
            vs.render_input(vp, value.get(param, vs.default_value()))
            html.close_div()

    def set_focus(self, varprefix):
        elements = self._get_elements()
        if elements:
            elements[0][1].set_focus(varprefix + "_p_" + elements[0][0])

    def canonical_value(self):
<<<<<<< HEAD
        return dict([(name, vs.canonical_value())
                     for (name, vs) in self._get_elements()
                     if name in self._required_keys or not self._optional_keys])

    def default_value(self):
        def_val = {}
        for name, vs in self._get_elements():
            if name in self._required_keys or not self._optional_keys or name in self._default_keys:
                def_val[name] = vs.default_value()

        return def_val
=======
        return {
            name: vs.canonical_value()
            for (name, vs) in self._get_elements()
            if name in self._required_keys or not self._optional_keys
        }

    def default_value(self):
        return {
            name: vs.default_value()
            for name, vs in self._get_elements()
            if name in self._required_keys or not self._optional_keys or name in self._default_keys
        }
>>>>>>> upstream/master

    def value_to_text(self, value):
        value = self.migrate(value)
        oneline = self._render == "oneline"
        if not value:
            return self._empty_text

        if self._default_text and value == self.default_value():
            return self._default_text

        elem = self._get_elements()
<<<<<<< HEAD
        s = '' if oneline else HTML()
        for param, vs in elem:
            if param in value:
                # TODO: This is a workaround for a bug. This function needs to return str objects right now.
                text = HTML(vs.value_to_text(value[param]))
                if oneline:
                    if param != elem[0][0]:
                        s += ", "
                    s += "%s: %s" % (vs.title(), text)
                else:
                    s += html.render_tr(
                        html.render_td("%s:&nbsp;" % vs.title(), class_="title") +
                        html.render_td(text))
        if not oneline:
            s = html.render_table(s)
        return "%s" % s
=======
        return self._value_to_text_oneline(
            elem, value) if oneline else self._value_to_text_multiline(elem, value)

    def _value_to_text_oneline(self, elem, value):
        s = ''
        for param, vs in elem:
            if param in value:
                if param != elem[0][0]:
                    s += ", "
                s += "%s: %s" % (vs.title(), self._funny_workaround(vs, value[param]))
        return s

    def _value_to_text_multiline(self, elem, value):
        s = HTML()
        for param, vs in elem:
            if param in value:
                s += html.render_tr(
                    html.render_td("%s:&nbsp;" % vs.title(), class_="title") +
                    html.render_td(self._funny_workaround(vs, value[param])))
        return str(html.render_table(s))

    def _funny_workaround(self, vs, value):
        # TODO: This is a workaround for a bug. This function needs to return str objects right now.
        return HTML(vs.value_to_text(value))

    def value_to_json(self, value):
        json_value = {}
        for param, vs in self._get_elements():
            if param not in value:
                continue
            json_value[param] = vs.value_to_json(value[param])
        return json_value

    def value_from_json(self, json_value):
        real_value = {}
        for param, vs in self._get_elements():
            if param not in json_value:
                continue
            real_value[param] = vs.value_from_json(json_value[param])
        return real_value
>>>>>>> upstream/master

    def from_html_vars(self, varprefix):
        value = {}
        for param, vs in self._get_elements():
            vp = varprefix + "_p_" + param
            if not self._optional_keys \
                or param in self._required_keys \
                or html.get_checkbox(vp + "_USE"):
                value[param] = vs.from_html_vars(vp)
        return value

    def validate_datatype(self, value, varprefix):
        value = self.migrate(value)

        if not isinstance(value, dict):
            raise MKUserError(
                varprefix,
                _("The type must be a dictionary, but it is a %s") % _type_name(value))

        for param, vs in self._get_elements():
            if param in value:
                vp = varprefix + "_p_" + param
                try:
                    vs.validate_datatype(value[param], vp)
                except MKUserError as e:
                    raise MKUserError(e.varname, _("%s: %s") % (vs.title(), e))
            elif not self._optional_keys or param in self._required_keys:
                raise MKUserError(varprefix, _("The entry %s is missing") % vs.title())

        # Check for exceeding keys
        allowed_keys = [p for p, _v in self._get_elements()]
        if self._ignored_keys:
            allowed_keys += self._ignored_keys
        for param in value.keys():
            if param not in allowed_keys:
                raise MKUserError(
                    varprefix,
                    _("Undefined key '%s' in the dictionary. Allowed are %s.") %
                    (param, ", ".join(allowed_keys)))

    def _validate_value(self, value, varprefix):
        value = self.migrate(value)

        for param, vs in self._get_elements():
            if param in value:
                vp = varprefix + "_p_" + param
                vs.validate_value(value[param], vp)
            elif not self._optional_keys or param in self._required_keys:
                raise MKUserError(varprefix, _("The entry %s is missing") % vs.title())

<<<<<<< HEAD
=======
    def transform_value(self, value: Dict[str, Any]) -> Dict[str, Any]:
        assert isinstance(value, dict), "Dictionary.transform_value() got a non-dict: %r" % (value,)
        return {
            **{
                param: vs.transform_value(value[param])  #
                for param, vs in self._get_elements()  #
                if param in value
            },
            **{
                param: value[param]  #
                for param in self._ignored_keys  #
                if param in value
            }
        }

>>>>>>> upstream/master

# TODO: Cleanup this and all call sites. Replace it with some kind of DropdownChoice
# based valuespec
class ElementSelection(ValueSpec):
    """Base class for selection of a Nagios element out of a given list that must be loaded from a file.

    Example: GroupSelection. Child class must define
    a function get_elements() that returns a dictionary
    from element keys to element titles."""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            label=None,  # type: TypingOptional[Text]
            empty_text=None,  # type: TypingOptional[Text]
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(ElementSelection, self).__init__(title=title,
                                               help=help,
                                               default_value=default_value,
                                               validate=validate)
        self._loaded_at = None
=======
        self,
        label: _Optional[str] = None,
        empty_text: _Optional[str] = None,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
        self._loaded_at: _Optional[int] = None
>>>>>>> upstream/master
        self._label = label
        self._empty_text = empty_text if empty_text is not None else \
            _("There are no elements defined for this selection yet.")

    def load_elements(self):
        if self._loaded_at != id(html):
            self._elements = self.get_elements()
            self._loaded_at = id(html)  # unique for each query!

    def get_elements(self):
        raise NotImplementedError()

    def canonical_value(self):
        self.load_elements()
        if len(self._elements) > 0:
<<<<<<< HEAD
            return self._elements.keys()[0]
=======
            return list(self._elements.keys())[0]
>>>>>>> upstream/master

    def render_input(self, varprefix, value):
        self.load_elements()
        if len(self._elements) == 0:
            html.write(self._empty_text)
        else:
            if self._label:
                html.write("%s" % self._label)
                html.nbsp()
            html.dropdown(varprefix, self._elements.items(), deflt=value, ordered=True)

    def value_to_text(self, value):
        self.load_elements()
<<<<<<< HEAD
        return html.attrencode(self._elements.get(value, value))
=======
        return escaping.escape_attribute(self._elements.get(value, value))
>>>>>>> upstream/master

    def from_html_vars(self, varprefix):
        return html.request.var(varprefix)

    def _validate_value(self, value, varprefix):
        self.load_elements()
        if len(self._elements) == 0:
            raise MKUserError(varprefix, _("You cannot save this rule.") + ' ' + self._empty_text)
        if value not in self._elements:
            raise MKUserError(varprefix,
                              _("%s is not an existing element in this selection.") % (value,))

    def validate_datatype(self, value, varprefix):
        self.load_elements()
        # When no elements exists the default value is None and e.g. in wato.mode_edit_rule()
        # handed over to validate_datatype() before rendering the input form. Disable the
        # validation in this case to prevent validation errors. A helpful message is shown
        # during render_input()
        if len(self._elements) == 0 and value is None:
            return

        if not isinstance(value, str):
            raise MKUserError(varprefix,
                              _("The datatype must be str (string), but is %s") % _type_name(value))


class AutoTimestamp(FixedValue):
<<<<<<< HEAD
    def canonical_value(self):
        return time.time()

    def from_html_vars(self, varprefix):
        return time.time()

    def value_to_text(self, value):
        return time.strftime("%F %T", time.localtime(value))

    def validate_datatype(self, value, varprefix):
=======
    def canonical_value(self) -> float:
        return time.time()

    def from_html_vars(self, varprefix: str) -> float:
        return time.time()

    def value_to_text(self, value: float) -> str:
        return time.strftime("%F %T", time.localtime(value))

    def validate_datatype(self, value: float, varprefix: str) -> None:
>>>>>>> upstream/master
        if not isinstance(value, (int, float)):
            return MKUserError(varprefix, _("Invalid datatype of timestamp: must be int or float."))


class Foldable(ValueSpec):
    """Fully transparant VS encapsulating a vs in a foldable container"""
<<<<<<< HEAD
    def __init__(self, valuespec, **kwargs):
        super(Foldable, self).__init__(**kwargs)
        self._valuespec = valuespec
        self._open = kwargs.get("open", False)
        self._title_function = kwargs.get("title_function", None)

    def render_input(self, varprefix, value):
        try:
=======
    def __init__(self,
                 valuespec: ValueSpec,
                 title_function: _Optional[Callable[[Any], str]] = None,
                 **kwargs: Any) -> None:  # pylint: disable=redefined-builtin
        super().__init__(**kwargs)
        self._valuespec = valuespec
        self._title_function = title_function

    def render_input(self, varprefix: str, value: Any) -> None:
        html.begin_foldable_container(
            treename="valuespec_foldable",
            id_=varprefix,
            isopen=False,
            title=self._get_title(varprefix, value),
            indent=False,
        )
        html.help(self._valuespec.help())
        self._valuespec.render_input(varprefix, value)
        html.end_foldable_container()

    def _get_title(self, varprefix: str, value: Any) -> str:
        if self._title_function:
>>>>>>> upstream/master
            title_value = value
            if html.form_submitted():
                try:
                    title_value = self._valuespec.from_html_vars(varprefix)
                except Exception:
                    pass
<<<<<<< HEAD
            title = self._title_function(title_value)
        except Exception:
            title = self._valuespec.title()
            if not title:
                title = _("(no title)")
        html.begin_foldable_container("valuespec_foldable", varprefix, self._open, title, False)
        html.help(self._valuespec.help())
        self._valuespec.render_input(varprefix, value)
        html.end_foldable_container()

    def set_focus(self, varprefix):
        self._valuespec.set_focus(varprefix)

    def canonical_value(self):
        return self._valuespec.canonical_value()

    def default_value(self):
        return self._valuespec.default_value()

    def value_to_text(self, value):
        return self._valuespec.value_to_text(value)

    def from_html_vars(self, varprefix):
        return self._valuespec.from_html_vars(varprefix)

    def validate_datatype(self, value, varprefix):
        self._valuespec.validate_datatype(value, varprefix)

    def _validate_value(self, value, varprefix):
        self._valuespec.validate_value(value, varprefix)

=======
            return self._title_function(title_value)

        title = self._valuespec.title()
        if not title:
            title = _("(no title)")
        return title

    def set_focus(self, varprefix: str) -> None:
        self._valuespec.set_focus(varprefix)

    def canonical_value(self) -> Any:
        return self._valuespec.canonical_value()

    def default_value(self) -> Any:
        return self._valuespec.default_value()

    def value_to_text(self, value: Any) -> str:
        return self._valuespec.value_to_text(value)

    def from_html_vars(self, varprefix: str) -> Any:
        return self._valuespec.from_html_vars(varprefix)

    def validate_datatype(self, value: Any, varprefix: str) -> None:
        self._valuespec.validate_datatype(value, varprefix)

    def _validate_value(self, value: Any, varprefix: str) -> None:
        self._valuespec.validate_value(value, varprefix)

    def transform_value(self, value):
        return self._valuespec.transform_value(value)

>>>>>>> upstream/master

class Transform(ValueSpec):
    """Transforms the value from one representation to another while being
    completely transparent to the user

    forth: function that converts a value into the representation
           needed by the encapsulated vs
    back:  function that converts a value created by the encapsulated
           vs back to the outer representation"""
    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            valuespec,  # type: ValueSpec
            back=None,  # type: TypingOptional[Callable[[Any], Any]]
            forth=None,  # type: TypingOptional[Callable[[Any], Any]]
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Union[Text, Callable[[], Text]]]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        super(Transform, self).__init__(title=title,
                                        help=help,
                                        default_value=default_value,
                                        validate=validate)
=======
        self,
        valuespec: ValueSpec,
        back: _Optional[Callable[[Any], Any]] = None,
        forth: _Optional[Callable[[Any], Any]] = None,
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._valuespec = valuespec
        self._back = back
        self._forth = forth

<<<<<<< HEAD
    def forth(self, value):
=======
    def forth(self, value: Any) -> Any:
>>>>>>> upstream/master
        if self._forth:
            return self._forth(value)
        return value

<<<<<<< HEAD
    def back(self, value):
=======
    def back(self, value: Any) -> Any:
>>>>>>> upstream/master
        if self._back:
            return self._back(value)
        return value

<<<<<<< HEAD
    def title(self):
=======
    def title(self) -> _Optional[str]:
>>>>>>> upstream/master
        if self._title:
            return self._title
        return self._valuespec.title()

<<<<<<< HEAD
    def help(self):
        if self._help:
            return self._help
        return self._valuespec.help()

    def render_input(self, varprefix, value):
        self._valuespec.render_input(varprefix, self.forth(value))

    def render_input_as_form(self, varprefix, value):
=======
    def help(self) -> Union[str, HTML, None]:
        transform_help = super().help()
        if transform_help:
            return transform_help
        return self._valuespec.help()

    def render_input(self, varprefix: str, value: Any) -> None:
        self._valuespec.render_input(varprefix, self.forth(value))

    def render_input_as_form(self, varprefix: str, value: Dict[str, Any]) -> None:
>>>>>>> upstream/master
        if not isinstance(self._valuespec, Dictionary):
            raise NotImplementedError()
        self._valuespec.render_input_as_form(varprefix, self.forth(value))

<<<<<<< HEAD
    def set_focus(self, varprefix):
        self._valuespec.set_focus(varprefix)

    def canonical_value(self):
        return self.back(self._valuespec.canonical_value())

    def default_value(self):
        return self.back(self._valuespec.default_value())

    def value_to_text(self, value):
        return self._valuespec.value_to_text(self.forth(value))

    def from_html_vars(self, varprefix):
        return self.back(self._valuespec.from_html_vars(varprefix))

    def validate_datatype(self, value, varprefix):
        self._valuespec.validate_datatype(self.forth(value), varprefix)

    def _validate_value(self, value, varprefix):
        self._valuespec.validate_value(self.forth(value), varprefix)


# TODO: Change to factory, cleanup kwargs
class LDAPDistinguishedName(TextUnicode):
    def __init__(self, **kwargs):
        super(LDAPDistinguishedName, self).__init__(**kwargs)
        self.enforce_suffix = kwargs.get('enforce_suffix')

    def _validate_value(self, value, varprefix):
        super(LDAPDistinguishedName, self)._validate_value(value, varprefix)
=======
    def set_focus(self, varprefix: str) -> None:
        self._valuespec.set_focus(varprefix)

    def canonical_value(self) -> Any:
        return self.back(self._valuespec.canonical_value())

    def default_value(self) -> Any:
        return self.back(self._valuespec.default_value())

    def value_to_text(self, value: Any) -> str:
        return self._valuespec.value_to_text(self.forth(value))

    def from_html_vars(self, varprefix: str) -> Any:
        return self.back(self._valuespec.from_html_vars(varprefix))

    def validate_datatype(self, value: Any, varprefix: str) -> None:
        self._valuespec.validate_datatype(self.forth(value), varprefix)

    def _validate_value(self, value: Any, varprefix: str) -> None:
        self._valuespec.validate_value(self.forth(value), varprefix)

    def transform_value(self, value: Any) -> Any:
        return self.back(self._valuespec.transform_value(self.forth(value)))


# TODO: Change to factory, cleanup kwargs
class LDAPDistinguishedName(TextUnicode):
    def __init__(self, enforce_suffix: _Optional[str] = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.enforce_suffix = enforce_suffix

    def _validate_value(self, value: str, varprefix: str) -> None:
        super()._validate_value(value, varprefix)
>>>>>>> upstream/master

        # Check whether or not the given DN is below a base DN
        if self.enforce_suffix and value and not value.lower().endswith(
                self.enforce_suffix.lower()):
            raise MKUserError(varprefix, _('Does not ends with "%s".') % self.enforce_suffix)


class Password(TextAscii):
<<<<<<< HEAD
    def __init__(self, is_stored_plain=True, **kwargs):
=======
    # TODO: Cleanup kwargs
    def __init__(self, is_stored_plain: bool = True, **kwargs: Any) -> None:
>>>>>>> upstream/master
        self._is_stored_plain = is_stored_plain
        kwargs.setdefault("autocomplete", False)

        if self._is_stored_plain:
            plain_help = _("The password entered here is stored in plain text within the "
                           "monitoring site. This usually needed because the monitoring "
                           "process needs to have access to the unencrypted password "
                           "because it needs to submit it to authenticate with remote systems. ")

            if "help" in kwargs:
                kwargs["help"] += "<br><br>" + plain_help
            else:
                kwargs["help"] = plain_help

<<<<<<< HEAD
        super(Password, self).__init__(attrencode=True, **kwargs)

    def render_input(self, varprefix, value):
=======
        super().__init__(attrencode=True, **kwargs)

    def render_input(self, varprefix: str, value: _Optional[str]) -> None:
>>>>>>> upstream/master
        if value is None:
            value = ""

        if self._label:
            html.write(self._label)
            html.nbsp()

<<<<<<< HEAD
        kwargs = {
            "size": self._size,
        }

        if self._autocomplete is False:
            kwargs["autocomplete"] = "new-password"

        html.password_input(varprefix, str(value), **kwargs)

    def password_plaintext_warning(self):
=======
        html.password_input(
            varprefix,
            str(value),
            size=self._size,
            autocomplete="new-password" if self._autocomplete is False else None,
        )

    def password_plaintext_warning(self) -> None:
>>>>>>> upstream/master
        if self._is_stored_plain:
            html.span(
                _("<br>Please note that Check_MK needs this password in clear"
                  "<br>text during normal operation and thus stores it unencrypted"
                  "<br>on the Check_MK server."))

<<<<<<< HEAD
    def value_to_text(self, value):
        if value is None:
            return _("none")
        return '******'


class PasswordSpec(Password):
    def __init__(self, hidden=True, **kwargs):
        super(PasswordSpec, self).__init__(hidden=hidden, **kwargs)

    def render_input(self, varprefix, value):
        super(PasswordSpec, self).render_input(varprefix, value)
        if not value:
            html.icon_button("#",
                             _(u"Randomize password"),
=======
    def value_to_text(self, value: _Optional[str]) -> str:
        if value is None:
            return _("none")
        return u'******'


class PasswordSpec(Password):
    # TODO: Cleanup kwargs
    def __init__(self, hidden: bool = True, **kwargs: Any) -> None:
        super().__init__(hidden=hidden, **kwargs)

    def render_input(self, varprefix: str, value: _Optional[str]) -> None:
        super().render_input(varprefix, value)
        if not value:
            html.icon_button("#",
                             _("Randomize password"),
>>>>>>> upstream/master
                             "random",
                             onclick="cmk.valuespecs.passwordspec_randomize(this);")
        if self._hidden:
            html.icon_button("#",
<<<<<<< HEAD
                             _(u"Show/Hide password"),
=======
                             _("Show/Hide password"),
>>>>>>> upstream/master
                             "showhide",
                             onclick="cmk.valuespecs.toggle_hidden(this);")

        self.password_plaintext_warning()


class FileUpload(ValueSpec):
    def __init__(self, **kwargs):
<<<<<<< HEAD
        super(FileUpload, self).__init__(**kwargs)
=======
        super().__init__(**kwargs)
>>>>>>> upstream/master
        self._allow_empty = kwargs.get('allow_empty', True)
        self._allowed_extensions = kwargs.get('allowed_extensions')
        self._allow_empty_content = kwargs.get('allow_empty_content', True)

    def canonical_value(self):
        if self._allow_empty:
            return None
        return ''

    def _validate_value(self, value, varprefix):
        if not value:
            raise MKUserError(varprefix, _('Please select a file.'))

        file_name, _mime_type, content = value

        if not self._allow_empty and (content == '' or file_name == ''):
            raise MKUserError(varprefix, _('Please select a file.'))

        if not self._allow_empty_content and len(content) == 0:
            raise MKUserError(varprefix,
                              _('The selected file is empty. Please select a non-empty file.'))
        if self._allowed_extensions is not None:
            matched = False
            for extension in self._allowed_extensions:
                if file_name.endswith(extension):
                    matched = True
                    break
            if not matched:
                raise MKUserError(
                    varprefix,
                    _("Invalid file name extension. Allowed are: %s") %
                    ", ".join(self._allowed_extensions))

    def render_input(self, varprefix, value):
        html.upload_file(varprefix)

    def from_html_vars(self, varprefix):
        return html.request.uploaded_file(varprefix)


class ImageUpload(FileUpload):
    def __init__(self, max_size=None, show_current_image=False, **kwargs):
        self._max_size = max_size
        self._show_current_image = show_current_image
<<<<<<< HEAD
        super(ImageUpload, self).__init__(**kwargs)
=======
        super().__init__(**kwargs)
>>>>>>> upstream/master

    def render_input(self, varprefix, value):
        if self._show_current_image and value:
            html.open_table()
            html.open_tr()
            html.td(_("Current image:"))
<<<<<<< HEAD
            html.td(html.render_img("data:image/png;base64,%s" % base64.b64encode(value)))
=======
            html.td(
                html.render_img("data:image/png;base64,%s" %
                                ensure_str(base64.b64encode(ensure_binary(value)))))
>>>>>>> upstream/master
            html.close_tr()
            html.open_tr()
            html.td(_("Upload new:"))
            html.open_td()
<<<<<<< HEAD
            super(ImageUpload, self).render_input(varprefix, value)
=======
            super().render_input(varprefix, value)
>>>>>>> upstream/master
            html.close_td()
            html.close_tr()
            html.close_table()
        else:
<<<<<<< HEAD
            super(ImageUpload, self).render_input(varprefix, value)
=======
            super().render_input(varprefix, value)
>>>>>>> upstream/master

    def _validate_value(self, value, varprefix):
        if not value:
            raise MKUserError(varprefix, _('Please choose a PNG image.'))

        file_name, mime_type, content = value

        if not file_name.endswith('.png') \
           or mime_type != 'image/png' \
<<<<<<< HEAD
           or not content.startswith('\x89PNG'):
            raise MKUserError(varprefix, _('Please choose a PNG image.'))

        try:
            im = Image.open(StringIO(content))
=======
           or not content.startswith(b'\x89PNG'):
            raise MKUserError(varprefix, _('Please choose a PNG image.'))

        try:
            im = Image.open(io.BytesIO(content))
>>>>>>> upstream/master
        except IOError:
            raise MKUserError(varprefix, _('Please choose a valid PNG image.'))

        if self._max_size:
            w, h = im.size
            max_w, max_h = self._max_size
            if w > max_w or h > max_h:
                raise MKUserError(varprefix, _('Maximum image size: %dx%dpx') % (max_w, max_h))


class UploadOrPasteTextFile(Alternative):
    def __init__(self, **kwargs):
        file_title = kwargs.pop("file_title", _("File"))
        allow_empty = kwargs.pop("allow_empty", True)
        kwargs["elements"] = [
            FileUpload(title=_("Upload %s") % file_title, allow_empty=allow_empty),
            TextAreaUnicode(title=_("Content of %s") % file_title,
                            allow_empty=allow_empty,
                            cols=80,
                            rows="auto"),
        ]

        if kwargs.pop("default_mode", "text") == "upload":
            kwargs["match"] = lambda *args: 0
        else:
            kwargs["match"] = lambda *args: 1

<<<<<<< HEAD
        kwargs.setdefault("style", "dropdown")
        super(UploadOrPasteTextFile, self).__init__(**kwargs)

    def from_html_vars(self, varprefix):
        value = super(UploadOrPasteTextFile, self).from_html_vars(varprefix)
=======
        super().__init__(**kwargs)

    def from_html_vars(self, varprefix):
        value = super().from_html_vars(varprefix)
>>>>>>> upstream/master
        # Convert textarea value to format of upload field
        if not isinstance(value, tuple):
            value = (None, None, value)
        return value


<<<<<<< HEAD
class ABCTextOrRegExp(six.with_metaclass(abc.ABCMeta, Alternative)):
    #@classmethod
    @abc.abstractmethod
    def _text_valuespec_class(self):
        # type: () -> Type[ValueSpec]
=======
class ABCTextOrRegExp(Alternative, metaclass=abc.ABCMeta):
    #@classmethod
    @abc.abstractmethod
    def _text_valuespec_class(self) -> Type[ValueSpec]:
>>>>>>> upstream/master
        raise NotImplementedError()

    #@classmethod
    @abc.abstractmethod
<<<<<<< HEAD
    def _regex_valuespec_class(self):
        # type: () -> Type[ValueSpec]
=======
    def _regex_valuespec_class(self) -> Type[ValueSpec]:
>>>>>>> upstream/master
        raise NotImplementedError()

    def __init__(self, **kwargs):
        allow_empty = kwargs.pop("allow_empty", True)

        if "text_valuespec" in kwargs:
            vs_text = kwargs.pop("text_valuespec")
        else:
            vs_text = self._text_valuespec_class()(
                title=_("Explicit match"),
                allow_empty=allow_empty,
            )

        vs_regex = self._regex_valuespec_class()(
            mode=RegExp.prefix,
            title=_("Regular expression match"),
            allow_empty=allow_empty,
        )

        kwargs.update({
            "elements": [
                vs_text,
                Transform(
                    vs_regex,
                    forth=lambda v: v[1:],  # strip of "~"
                    back=lambda v: "~" + v,  # add "~"
                ),
            ],
            # Use RegExp field when value is prefixed with "~"
            "match": lambda v: 1 if v and v[0] == "~" else 0,
<<<<<<< HEAD
            "style": "dropdown",
            "orientation": "horizontal",
        })

        super(ABCTextOrRegExp, self).__init__(**kwargs)
=======
            "orientation": "horizontal",
        })

        super().__init__(**kwargs)
>>>>>>> upstream/master


class TextOrRegExp(ABCTextOrRegExp):
    @classmethod
    def _text_valuespec_class(cls):
        return TextAscii

    @classmethod
    def _regex_valuespec_class(cls):
        return RegExp


class TextOrRegExpUnicode(ABCTextOrRegExp):
    @classmethod
    def _text_valuespec_class(cls):
        return TextUnicode

    @classmethod
    def _regex_valuespec_class(cls):
        return RegExpUnicode


class Labels(ValueSpec):
    """Valuespec to render and input a collection of object labels"""
    class World(Enum):
        CONFIG = "config"
        CORE = "core"

    class Source(Enum):
        EXPLICIT = "explicit"
        RULESET = "ruleset"
        DISCOVERED = "discovered"

    def __init__(  # pylint: disable=redefined-builtin
<<<<<<< HEAD
            self,
            world,  # type: Labels.World
            label_source=None,  # type: Labels.Source
            max_labels=None,  # type: TypingOptional[int]
            # ValueSpec
            title=None,  # type: TypingOptional[Text]
            help=None,  # type: TypingOptional[Text]
            default_value=_DEF_VALUE,  # type: Any
            validate=None,  # type: TypingOptional[Callable[[str, Any], None]]
    ):
        help_ = help if help is not None else ""
        help_ += _("Labels need to be in the format <tt>[KEY]:[VALUE]</tt>. "
                   "For example <tt>os:windows</tt>.")
        super(Labels, self).__init__(title=title,
                                     help=help_,
                                     default_value=default_value,
                                     validate=validate)

=======
        self,
        world: 'Labels.World',
        label_source: _Optional['Labels.Source'] = None,
        max_labels: _Optional[int] = None,
        # ValueSpec
        title: _Optional[str] = None,
        help: _Optional[ValueSpecHelp] = None,
        default_value: Any = DEF_VALUE,
        validate: _Optional[ValueSpecValidateFunc] = None,
    ):
        super().__init__(title=title, help=help, default_value=default_value, validate=validate)
>>>>>>> upstream/master
        self._world = world
        # Set this source to mark the labels that have no explicit label source set
        self._label_source = label_source
        # Set to positive integer to limit the number of labels to add to this field
        self._max_labels = max_labels

<<<<<<< HEAD
=======
    def help(self) -> Union[str, HTML, None]:
        h = super().help()
        return (u"" if h is None else h) + _(
            "Labels need to be in the format <tt>[KEY]:[VALUE]</tt>. For example <tt>os:windows</tt>."
        )

>>>>>>> upstream/master
    def canonical_value(self):
        return {}

    def from_html_vars(self, varprefix):
<<<<<<< HEAD
        labels = {}

        for entry in json.loads(html.get_unicode_input(varprefix) or "[]"):
=======
        labels: Dict[str, Any] = {}

        try:
            decoded_labels = json.loads(html.request.get_unicode_input(varprefix) or "[]")
        except ValueError as e:
            raise MKUserError(varprefix, _("Failed to parse labels: %s") % e)

        for entry in decoded_labels:
>>>>>>> upstream/master
            label_id, label_value = [p.strip() for p in entry["value"].split(":", 1)]
            if label_id in labels:
                raise MKUserError(
                    varprefix,
                    _("A label key can be used only once per object. "
                      "The Label key \"%s\" is used twice.") % label_id)
            labels[label_id] = label_value

        return labels

    def _validate_value(self, value, varprefix):
<<<<<<< HEAD
        for k, v in value.iteritems():
            if not isinstance(k, six.text_type):
                raise MKUserError(
                    varprefix,
                    _("The label ID %r is of type %s, but should be %s") %
                    (k, type(k), six.text_type))
            if not isinstance(v, six.text_type):
                raise MKUserError(
                    varprefix,
                    _("The label value %r is of type %s, but should be %s") %
                    (k, type(v), six.text_type))

    def value_to_text(self, value):
        from cmk.gui.view_utils import render_labels
=======
        for k, v in value.items():
            if not isinstance(k, str):
                raise MKUserError(
                    varprefix,
                    _("The label ID %r is of type %s, but should be %s") % (k, type(k), str))
            if not isinstance(v, str):
                raise MKUserError(
                    varprefix,
                    _("The label value %r is of type %s, but should be %s") % (k, type(v), str))

    def value_to_text(self, value):
>>>>>>> upstream/master
        label_sources = {k: self._label_source.value for k in value.keys()
                        } if self._label_source else {}
        return render_labels(value, "host", with_links=False, label_sources=label_sources)

    def render_input(self, varprefix, value):
        html.help(self.help())
        # tagify outputs a warning for value of "[]" right now
        # see: https://github.com/yairEO/tagify/pull/275
        labels = _encode_labels_for_tagify(value.items())
        html.text_input(varprefix,
<<<<<<< HEAD
                        default_value=json.dumps(labels).decode("utf-8") if labels else "",
                        cssclass="labels",
                        attrs={
                            "placeholder": _("Add some label"),
                            "data-world": self._world.value,
                            "data-max-labels": self._max_labels,
                        })
=======
                        default_value=ensure_str(json.dumps(labels)) if labels else "",
                        cssclass="labels",
                        placeholder=_("Add some label"),
                        data_world=self._world.value,
                        data_max_labels=self._max_labels)
>>>>>>> upstream/master


def SingleLabel(world, label_source=None, **kwargs):
    """Input element for a single label"""
    return Labels(world, label_source=label_source, max_labels=1, **kwargs)


@page_registry.register_page("ajax_autocomplete_labels")
class PageAutocompleteLabels(AjaxPage):
    """Return all known labels to support tagify label input dropdown completion"""
    def page(self):
        request = html.get_request()
        return _encode_labels_for_tagify(
            self._get_labels(Labels.World(request["world"]), request["search_label"]))

    def _get_labels(self, world, search_label):
        if world == Labels.World.CONFIG:
            return self._get_labels_from_config(search_label)

        if world == Labels.World.CORE:
            return self._get_labels_from_core(search_label)

        raise NotImplementedError()

    def _get_labels_from_config(self, search_label):
        return []  # TODO: Implement me

    # TODO: Provide information about the label source
    # Would be better to optimize this kind of query somehow. The best we can
    # do without extending livestatus is to use the Cache header for liveproxyd
    def _get_labels_from_core(self, search_label):
<<<<<<< HEAD
        import cmk.gui.sites as sites
        query = ("GET services\n" \
                "Cache: reload\n" \
                "Columns: host_labels labels\n")

        labels = set()
=======
        query = (
            "GET services\n"  #
            "Cache: reload\n"  #
            "Columns: host_labels labels\n")

        labels: Set = set()
>>>>>>> upstream/master
        for row in sites.live().query(query):
            labels.update(row[0].items())
            labels.update(row[1].items())

        return list(labels)


def _encode_labels_for_tagify(labels):
    return [{"value": "%s:%s" % e} for e in labels]


class IconSelector(ValueSpec):
<<<<<<< HEAD
    def __init__(self, **kwargs):
        super(IconSelector, self).__init__(**kwargs)
        self._allow_empty = kwargs.get('allow_empty', True)
        self._empty_img = kwargs.get('emtpy_img', 'empty')
=======
    def __init__(self,
                 allow_empty=True,
                 empty_img="empty",
                 show_builtin_icons=True,
                 with_emblem=True,
                 **kwargs):
        super().__init__(**kwargs)
        self._allow_empty = allow_empty
        self._empty_img = empty_img
        self._show_builtin_icons = show_builtin_icons
        self._with_emblem = with_emblem
>>>>>>> upstream/master

        self._exclude = [
            'trans',
            'empty',
        ]

    @classmethod
    def categories(cls):
<<<<<<< HEAD
        import cmk.gui.config as config  # FIXME: Clean this up. But how?
=======
>>>>>>> upstream/master
        return config.wato_icon_categories

    @classmethod
    def category_alias(cls, category_name):
        return dict(cls.categories()).get(category_name, category_name)

    # All icons within the images/icons directory have the ident of a category
    # witten in the PNG meta data. For the default images we have done this scripted.
    # During upload of user specific icons, the meta data is added to the images.
<<<<<<< HEAD
    def available_icons(self, only_local=False):
        dirs = [
            os.path.join(cmk.utils.paths.omd_root, "local/share/check_mk/web/htdocs/images/icons"),
        ]
        if not only_local:
            dirs.append(
                os.path.join(cmk.utils.paths.omd_root, "share/check_mk/web/htdocs/images/icons"))

        valid_categories = dict(self.categories()).keys()

        #
        # Read all icons from the icon directories
        #
        icons = {}
        for directory in dirs:
            try:
                files = os.listdir(directory)
            except OSError:
                continue

            for file_name in files:
                file_path = directory + "/" + file_name
                if file_name[-4:] == '.png' and os.path.isfile(file_path):

                    # extract the category from the meta data
                    try:
                        im = Image.open(file_path)
                    except IOError as e:
                        if "%s" % e == "cannot identify image file":
                            continue  # Silently skip invalid files
                        else:
                            raise

                    category = im.info.get('Comment')
                    if category not in valid_categories:
                        category = 'misc'

                    icon_name = file_name[:-4]
                    icons[icon_name] = category

        for exclude in self._exclude:
            try:
                del icons[exclude]
            except KeyError:
                pass

        return icons

    def available_icons_by_category(self, icons):
        by_cat = {}
=======
    def available_icons(self, only_local: bool = False) -> Dict[str, str]:
        icons = {}
        icons.update(self._available_builtin_icons("icon_", only_local))
        icons.update(self._available_user_icons(only_local))
        return icons

    def available_emblems(self, only_local: bool = False) -> Dict[str, str]:
        return self._available_builtin_icons("emblem_", only_local)

    def _available_builtin_icons(self, prefix: str, only_local: bool = False) -> Dict[str, str]:
        if not self._show_builtin_icons:
            return {}

        icons = {}
        for theme in html.icon_themes():
            dirs = [Path(cmk.utils.paths.local_web_dir) / "htdocs/themes" / theme / "images"]
            if not only_local:
                dirs.append(Path(cmk.utils.paths.web_dir) / "htdocs/themes" / theme / "images")

            for file_stem, category in self._get_icons_from_directories(
                    dirs, default_category="builtin").items():
                if file_stem.startswith(prefix):
                    icons[file_stem[len(prefix):]] = category
        return icons

    def _available_user_icons(self, only_local=False) -> Dict[str, str]:
        dirs = [Path(cmk.utils.paths.local_web_dir) / "htdocs/images/icons"]
        if not only_local:
            dirs.append(Path(cmk.utils.paths.web_dir) / "htdocs/images/icons")

        return self._get_icons_from_directories(dirs, default_category="misc")

    def _get_icons_from_directories(self, dirs: List[Path],
                                    default_category: str) -> Dict[str, str]:
        icons: Dict[str, str] = {}
        for directory in dirs:
            try:
                files = [f for f in directory.iterdir() if f.is_file()]
            except OSError:
                continue

            for file_ in files:
                if file_.suffix == '.png':
                    try:
                        category = self._extract_category_from_png(file_, default_category)
                    except IOError as e:
                        if "%s" % e == "cannot identify image file":
                            continue  # silently skip invalid files
                        raise
                elif file_.suffix == '.svg':
                    # users are not able to add SVGs and our builtin SVGs don't have a category
                    category = default_category
                else:
                    continue

                icons[file_.stem] = category

        for exclude in self._exclude:
            icons.pop(exclude, None)

        return icons

    def _extract_category_from_png(self, file_path: Path, default: str) -> str:
        # extract the category from the meta data
        category = Image.open(file_path).info.get('Comment')
        valid_categories = {k for k, _v in self.categories()}
        if category not in valid_categories:
            return default
        return category

    def _available_icons_by_category(self, icons):
        by_cat: Dict[str, List[str]] = {}
>>>>>>> upstream/master
        for icon_name, category_name in icons.items():
            by_cat.setdefault(category_name, [])
            by_cat[category_name].append(icon_name)

<<<<<<< HEAD
=======
        categories = self.categories()
        if self._show_builtin_icons:
            categories.append(("builtin", _("Builtin")))

>>>>>>> upstream/master
        icon_categories = []
        for category_name, category_alias in self.categories():
            if category_name in by_cat:
                icon_categories.append((category_name, category_alias, by_cat[category_name]))
        return icon_categories

<<<<<<< HEAD
    def render_icon(self, icon_name, onclick='', title='', id_=''):
        if not icon_name:
            icon_name = self._empty_img

        icon = html.render_icon(icon_name, title=title, middle=True, id_=id_)
        if onclick:
            icon = html.render_a(icon, href="javascript:void(0)", onclick=onclick)

        return icon

    def render_input(self, varprefix, value):
=======
    def _render_icon(self, icon, onclick='', title='', id_=''):
        if not icon:
            icon = self._empty_img
        if id_.endswith('_emblem_img'):
            icon = {'icon': 'empty', 'emblem': icon}

        icon_tag = html.render_icon(icon, title=title, middle=True, id_=id_)
        if onclick:
            icon_tag = html.render_a(icon_tag, href="javascript:void(0)", onclick=onclick)

        return icon_tag

    def _transform_icon_str(self, value):
        if isinstance(value, dict):
            return value
        return {'icon': value, 'emblem': None}

    def render_input(self, varprefix, value):
        value = self._transform_icon_str(value)

        self._render_input(varprefix, value['icon'])
        if self._with_emblem:
            self._render_input(varprefix + "_emblem", value['emblem'])

    def _render_input(self, varprefix, value):
>>>>>>> upstream/master
        # Handle complain phase with validation errors correctly and get the value
        # from the HTML vars
        if value is None:
            value = html.request.var(varprefix + "_value")

        if not value:
            value = self._empty_img

        html.hidden_field(varprefix + "_value", value or '', varprefix + "_value", add_var=True)

        if value:
<<<<<<< HEAD
            content = self.render_icon(value, '', _('Choose another Icon'), id_=varprefix + '_img')
=======
            content = self._render_icon(value, '', _('Choose another Icon'), id_=varprefix + '_img')
>>>>>>> upstream/master
        else:
            content = _('Select an Icon')

        html.popup_trigger(
            content,
            varprefix + '_icon_selector',
<<<<<<< HEAD
            'icon_selector',
            url_vars=[
                ('value', value),
                ('varprefix', varprefix),
                ('allow_empty', '1' if self._allow_empty else '0'),
                ('back', html.makeuri([])),
            ],
=======
            MethodAjax(endpoint='icon_selector',
                       url_vars=[
                           ('value', value),
                           ('varprefix', varprefix),
                           ('allow_empty', '1' if self._allow_empty else '0'),
                           ('show_builtin_icons', '1' if self._show_builtin_icons else '0'),
                           ('back', makeuri(global_request, [])),
                       ]),
>>>>>>> upstream/master
            resizable=True,
        )

    def render_popup_input(self, varprefix, value):
        html.open_div(class_="icons", id_="%s_icons" % varprefix)

<<<<<<< HEAD
        icons = self.available_icons()
        available_icons = self.available_icons_by_category(icons)
=======
        is_emblem = varprefix.endswith("_emblem")
        icons = self.available_emblems() if is_emblem else self.available_icons()
        available_icons = self._available_icons_by_category(icons)
>>>>>>> upstream/master
        active_category = icons.get(value, available_icons[0][0])

        # Render tab navigation
        html.open_ul()
<<<<<<< HEAD
        for category_name, category_alias, icons in available_icons:
            html.open_li(class_="active" if active_category == category_name else None)
            html.a(category_alias,
                   href="javascript:cmk.valuespecs.iconselector_toggle(\'%s\', \'%s\')" %
                   (varprefix, category_name),
=======
        for category_name, category_alias, _icons in available_icons:
            html.open_li(class_="active" if active_category == category_name else None)
            html.a(category_alias,
                   href="javascript:cmk.valuespecs.iconselector_toggle(%s, %s)" %
                   (json.dumps(varprefix), json.dumps(category_name)),
>>>>>>> upstream/master
                   id_="%s_%s_nav" % (varprefix, category_name),
                   class_="%s_nav" % varprefix)
            html.close_li()
        html.close_ul()

        # Now render the icons grouped by category
<<<<<<< HEAD
        empty = ['empty'] if self._allow_empty else []
=======
        empty = ['empty'] if self._allow_empty or is_emblem else []
>>>>>>> upstream/master
        for category_name, category_alias, icons in available_icons:
            html.open_div(id_="%s_%s_container" % (varprefix, category_name),
                          class_=["icon_container", "%s_container" % varprefix],
                          style="display:none;" if active_category != category_name else None)

            for icon in empty + sorted(icons):
                html.open_a(
                    href=None,
                    class_="icon",
<<<<<<< HEAD
                    onclick='cmk.valuespecs.iconselector_select(event, \'%s\', \'%s\')' %
                    (varprefix, icon),
                    title=icon,
                )

                html.write_html(self.render_icon(icon, id_=varprefix + '_i_' + icon, title=icon))
=======
                    onclick='cmk.valuespecs.iconselector_select(event, %s, %s)' %
                    (json.dumps(varprefix), json.dumps(icon)),
                    title=icon,
                )

                icon_path = (html.detect_icon_path(icon, prefix="emblem")
                             if is_emblem and icon != 'empty' else icon)
                html.write_html(
                    self._render_icon(icon_path, id_=varprefix + '_i_' + icon, title=icon))
>>>>>>> upstream/master

                html.span(icon)

                html.close_a()

            html.close_div()

        html.open_div(class_="buttons")

        html.jsbutton("_toggle_names",
                      _("Toggle names"),
                      onclick="cmk.valuespecs.iconselector_toggle_names(event, %s)" %
                      json.dumps(varprefix))

<<<<<<< HEAD
        import cmk.gui.config as config  # FIXME: Clean this up. But how?
=======
>>>>>>> upstream/master
        if config.user.may('wato.icons'):
            back_param = '&back=' + html.urlencode(
                html.get_url_input('back')) if html.request.has_var('back') else ''
            html.buttonlink('wato.py?mode=icons' + back_param, _('Manage'))

        html.close_div()

        html.close_div()

    def from_html_vars(self, varprefix):
<<<<<<< HEAD
=======
        icon = self._from_html_vars(varprefix)
        if not self._with_emblem:
            return icon

        emblem = self._from_html_vars(varprefix + "_emblem")
        if not emblem:
            return icon

        return {'icon': icon, 'emblem': emblem}

    def _from_html_vars(self, varprefix):
>>>>>>> upstream/master
        icon = html.request.var(varprefix + '_value')
        if icon == 'empty':
            return None
        return icon

    def value_to_text(self, value):
        # TODO: This is a workaround for a bug. This function needs to return str objects right now.
<<<<<<< HEAD
        return "%s" % self.render_icon(value)

    def validate_datatype(self, value, varprefix):
        if value is not None and not isinstance(value, str):
            raise MKUserError(varprefix, _("The type is %s, but should be str") % type(value))

    def _validate_value(self, value, varprefix):
        if not self._allow_empty and not value:
            raise MKUserError(varprefix, _("You need to select an icon."))

        if value and value not in self.available_icons():
            raise MKUserError(varprefix, _("The selected icon image does not exist."))
=======
        return "%s" % self._render_icon(value["icon"] if isinstance(value, dict) else value)

    def validate_datatype(self, value, varprefix):
        if self._with_emblem and not isinstance(value, (str, dict)):
            raise MKUserError(varprefix, "The type is %s, but should be str or dict" % type(value))
        if not self._with_emblem and not isinstance(value, str):
            raise MKUserError(varprefix, "The type is %s, but should be str or dict" % type(value))

        value = self._transform_icon_str(value)
        if not (value["icon"] is None or isinstance(value["icon"], str)):
            raise MKUserError(varprefix,
                              _("The icon type is %s, but should be str") % type(value["icon"]))
        if not (value["emblem"] is None or isinstance(value["emblem"], str)):
            raise MKUserError(varprefix,
                              _("The emblem type is %s, but should be str") % type(value["emblem"]))

    def _validate_value(self, value, varprefix):
        value = self._transform_icon_str(value)

        if not self._allow_empty and not value["icon"]:
            raise MKUserError(varprefix, _("You need to select an icon."))

        if value["icon"] and value["icon"] not in self.available_icons():
            raise MKUserError(varprefix, _("The selected icon does not exist."))

        if value["emblem"] and value["emblem"] not in self.available_emblems():
            raise MKUserError(varprefix, _("The selected emblem does not exist."))
>>>>>>> upstream/master


# TODO: Cleanup kwargs
def ListOfTimeRanges(**kwargs):
    return ListOf(TimeofdayRange(allow_empty=True,),
                  movable=False,
                  add_label=_("Add time range"),
                  del_label=_("Delete time range"),
                  style=ListOf.Style.FLOATING,
                  magic="#!#",
                  **kwargs)


# Kept for compatibility reasons (removed in 1.6)
TimeofdayRanges = ListOfTimeRanges


# TODO: Cleanup kwargs
def Fontsize(**kwargs):
    kwargs.setdefault("title", _("Font size"))
    kwargs.setdefault("default_value", 10)
    return Float(size=5, unit=_("pt"), **kwargs)


class Color(ValueSpec):
    def __init__(self, **kwargs):
        kwargs["regex"] = "#[0-9]{3,6}"
        kwargs["regex_error"] = _("The color needs to be given in hex format.")
<<<<<<< HEAD
        super(Color, self).__init__(**kwargs)
=======
        super().__init__(**kwargs)
>>>>>>> upstream/master
        self._on_change = kwargs.get("on_change")
        self._allow_empty = kwargs.get("allow_empty", True)

    def render_input(self, varprefix, value):
        if not value:
            value = "#FFFFFF"

        # Holds the actual value for form submission
        html.hidden_field(varprefix + "_value", value or '', varprefix + "_value", add_var=True)

        indicator = html.render_div('',
                                    id_="%s_preview" % varprefix,
                                    class_="cp-preview",
                                    style="background-color:%s" % value)

<<<<<<< HEAD
        # TODO(rh): Please take a look at this hard coded HTML
        # FIXME: Rendering with HTML class causes bug in html popup_trigger function.
        #        Reason is HTML class and the escaping.
        menu_content = "<div id=\"%s_picker\" class=\"cp-small\"></div>" % varprefix
        menu_content += "<div class=\"cp-input\">" \
            "%s" \
            "<input id=\"%s_input\" type=\"text\"></input></div>" % \
                (_("Hex color:"), varprefix)

        menu_content += "<script language=\"javascript\">" \
            "cmk.valuespecs.add_color_picker(%s, %s)" \
            "</script>" % (json.dumps(varprefix), json.dumps(value))

        html.popup_trigger(indicator,
                           varprefix + '_popup',
                           menu_content=menu_content,
=======
        html.popup_trigger(indicator,
                           varprefix + '_popup',
                           MethodColorpicker(varprefix, value),
>>>>>>> upstream/master
                           cssclass="colorpicker",
                           onclose=self._on_change)

    def from_html_vars(self, varprefix):
        color = html.request.var(varprefix + '_value')
        if color == '':
            return None
        return color

    def value_to_text(self, value):
        return value

    def validate_datatype(self, value, varprefix):
        if value is not None and not isinstance(value, str):
            raise MKUserError(varprefix, _("The type is %s, but should be str") % type(value))

    def _validate_value(self, value, varprefix):
        if not self._allow_empty and not value:
            raise MKUserError(varprefix, _("You need to select a color."))


def GraphColor(title, default_value):
    return Alternative(
        title=title,
<<<<<<< HEAD
        style="dropdown",
=======
>>>>>>> upstream/master
        elements=[
            FixedValue(
                "default",
                title=_("Use default color"),
                totext=_("Use default color of the theme or medium"),
            ),
            Color(title=_("Use the following color")),
        ],
        default_value=default_value,
    )


class SSHKeyPair(ValueSpec):
    def render_input(self, varprefix, value):
        if value:
            html.write(_("Fingerprint: %s") % self.value_to_text(value))
            html.hidden_field(varprefix, self._encode_key_for_url(value), add_var=True)
        else:
            html.write(_("Key pair will be generated when you save."))

    def value_to_text(self, value):
        return self._get_key_fingerprint(value)

    def from_html_vars(self, varprefix):
        if html.request.has_var(varprefix):
            return self._decode_key_from_url(html.request.var(varprefix))
        return self._generate_ssh_key(varprefix)

    @staticmethod
    def _encode_key_for_url(value):
        return "|".join(value)

    @staticmethod
    def _decode_key_from_url(text):
        return text.split("|")

    @classmethod
    def _generate_ssh_key(cls, varprefix):
        key = RSA.generate(4096)
        private_key = key.exportKey('PEM')
        pubkey = key.publickey()
        public_key = pubkey.exportKey('OpenSSH')
        return (private_key, public_key)

    @classmethod
    def _get_key_fingerprint(cls, value):
        _private_key, public_key = value
        key = base64.b64decode(public_key.strip().split()[1].encode('ascii'))
        fp_plain = hashlib.md5(key).hexdigest()
        return ':'.join(a + b for a, b in zip(fp_plain[::2], fp_plain[1::2]))


# TODO: Cleanup kwargs
def SchedulePeriod(from_end=True, **kwargs):
    if from_end:
<<<<<<< HEAD
        from_end_choice = [
=======
        from_end_choice: List[CascadingDropdownChoice] = [
>>>>>>> upstream/master
            ("month_end", _("At the end of every month at day"),
             Integer(minvalue=1, maxvalue=28, unit=_("from the end"))),
        ]
    else:
        from_end_choice = []

<<<<<<< HEAD
    return CascadingDropdown(
        title=_("Period"),
        orientation="horizontal",
        choices=[
            ("day", _("Every day")),
            ("week", _("Every week on..."), Weekday(title=_("Day of the week"))),
            ("month_begin", _("At the beginning of every month at day"),
             Integer(minvalue=1, maxvalue=28)),
        ] + from_end_choice,
        **kwargs)
=======
    dwm: List[CascadingDropdownChoice] = [
        ("day", _("Every day"), None),
        ("week", _("Every week on..."), Weekday(title=_("Day of the week"))),
        ("month_begin", _("At the beginning of every month at day"), Integer(minvalue=1,
                                                                             maxvalue=28)),
    ]
    return CascadingDropdown(title=_("Period"),
                             orientation="horizontal",
                             choices=dwm + from_end_choice,
                             **kwargs)
>>>>>>> upstream/master


class CAorCAChain(UploadOrPasteTextFile):
    def __init__(self, **args):
        args.setdefault("title", _("Certificate Chain (Root / Intermediate Certificate)"))
        args.setdefault("file_title", _("CRT/PEM File"))
<<<<<<< HEAD
        super(CAorCAChain, self).__init__(**args)
=======
        super().__init__(**args)
>>>>>>> upstream/master

    def from_html_vars(self, varprefix):
        value = Alternative.from_html_vars(self, varprefix)
        if isinstance(value, tuple):
            value = value[2]  # FileUpload sends (filename, mime-type, content)
        return value

    def _validate_value(self, value, varprefix):
        try:
            self.analyse_cert(value)
        except Exception as e:
            raise MKUserError(varprefix, _("Invalid certificate file: %s") % e)

    def analyse_cert(self, value):
<<<<<<< HEAD
        from OpenSSL import crypto
=======
>>>>>>> upstream/master
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, value)
        titles = {
            "C": _("Country"),
            "ST": _("State or Province Name"),
            "L": _("Locality Name"),
            "O": _("Organization Name"),
            "CN": _("Common Name"),
        }
<<<<<<< HEAD
        cert_info = {}
=======
        cert_info: Dict[str, Dict] = {}
>>>>>>> upstream/master
        for what, x509 in [
            ("issuer", cert.get_issuer()),
            ("subject", cert.get_subject()),
        ]:
            cert_info[what] = {}
            for key, val in x509.get_components():
                if key in titles:
                    cert_info[what][titles[key]] = val.decode("utf8")
        return cert_info

    def value_to_text(self, value):
        cert_info = self.analyse_cert(value)
<<<<<<< HEAD
        text = "<table>"
=======
        text = u"<table>"
>>>>>>> upstream/master
        for what, title in [
            ("issuer", _("Issuer")),
            ("subject", _("Subject")),
        ]:
<<<<<<< HEAD
            text += "<tr><td>%s:</td><td>" % title
            for title1, val in sorted(cert_info[what].items()):
                text += "%s: %s<br>" % (title1, val)
            text += "</tr>"
        text += "</table>"
=======
            text += u"<tr><td>%s:</td><td>" % title
            for title1, val in sorted(cert_info[what].items()):
                text += u"%s: %s<br>" % (title1, val)
            text += u"</tr>"
        text += u"</table>"
>>>>>>> upstream/master
        return text


# TODO: Cleanup kwargs
def ListOfCAs(**args):
    args.setdefault("title", _("CAs to accept"))
    args.setdefault(
        "help",
        _("Only accepting HTTPS connections with a server which certificate "
          "is signed with one of the CAs that are listed here. That way it is guaranteed "
          "that it is communicating only with the authentic update server. "
          "If you use self signed certificates for you server then enter that certificate "
          "here."))
    args.setdefault("add_label", _("Add new CA certificate or chain"))
    args.setdefault(
        "empty_text",
        _("You need to enter at least one CA. Otherwise no SSL connection can be made."))
    args.setdefault("allow_empty", False)
    return ListOf(CAorCAChain(), movable=False, **args)


# TODO: Change to factory, Cleanup kwargs
class SiteChoice(DropdownChoice):
    def __init__(self, **kwargs):
        kwargs.setdefault("title", _("Site"))
        kwargs.setdefault("default_value", self._site_default_value)
        kwargs.setdefault("invalid_choice_error",
                          _("The configured site is not known to this site."))

        kwargs.update({
            "choices": self._site_choices,
            "invalid_choice": "complain",
            "invalid_choice_title": _("Unknown site (%s)"),
        })

<<<<<<< HEAD
        super(SiteChoice, self).__init__(**kwargs)

    def _site_default_value(self):
        import cmk.gui.config as config
=======
        super().__init__(**kwargs)

    def _site_default_value(self):
>>>>>>> upstream/master
        if config.is_wato_slave_site():
            return False

        default_value = config.site_attribute_default_value()
        if default_value:
            return default_value
        return self.canonical_value()

    def _site_choices(self):
<<<<<<< HEAD
        import cmk.gui.config as config  # FIXME
=======
>>>>>>> upstream/master
        return config.site_attribute_choices()


# TODO: Cleanup kwargs
def LogLevelChoice(**kwargs):
    kwargs.setdefault("default_value", logging.INFO)
    return DropdownChoice(choices=[
        (logging.CRITICAL, _("Critical")),
        (logging.ERROR, _("Error")),
        (logging.WARNING, _("Warning")),
        (logging.INFO, _("Informational")),
        (cmk.utils.log.VERBOSE, _("Verbose")),
        (logging.DEBUG, _("Debug")),
    ],
                          **kwargs)


<<<<<<< HEAD
def MetricName():
    """Factory of a Dropdown menu from all known metric names"""
    return DropdownChoice(
        title=_("Metric Name"),
        sorted=True,
        choices=[
            (metric_id, metric_detail['title']) for metric_id, metric_detail in metric_info.items()
        ],
=======
def rule_option_elements(disabling: bool = True) -> List[DictionaryEntry]:
    elements: List[DictionaryEntry] = [
        ("description",
         TextUnicode(
             title=_("Description"),
             help=_("A description or title of this rule"),
             size=80,
         )),
        ("comment", RuleComment()),
        ("docu_url", DocumentationURL()),
    ]
    if disabling:
        elements += [
            ("disabled",
             Checkbox(
                 title=_("Rule activation"),
                 help=_("Disabled rules are kept in the configuration but are not applied."),
                 label=_("do not apply this rule"),
             )),
        ]
    return elements


class RuleComment(TextAreaUnicode):
    def __init__(self) -> None:
        super().__init__(
            title=_("Comment"),
            help=_("An optional comment that may be used to explain the purpose of this object. "
                   "The comment is only visible in this dialog and may help other users "
                   "understanding the intentions of the configured attributes."),
            rows=4,
            cols=80,
        )

    # TODO: Once we switched to Python 3 we can merge the unicode and non unicode class
    def render_input(self, varprefix: str, value: str) -> None:  # type: ignore[override]
        html.open_div(style="white-space: nowrap;")

        super().render_input(varprefix, value)

        date_and_user = "%s %s: " % (time.strftime("%F", time.localtime()), config.user.id)

        html.nbsp()
        html.icon_button(None,
                         title=_("Prefix date and your name to the comment"),
                         icon="insertdate",
                         onclick="cmk.valuespecs.rule_comment_prefix_date_and_user(this, '%s');" %
                         date_and_user)
        html.close_div()


def DocumentationURL() -> TextAscii:
    return TextAscii(
        title=_("Documentation URL"),
        help=HTML(
            _("An optional URL pointing to documentation or any other page. This will be displayed "
              "as an icon %s and open a new page when clicked. "
              "You can use either global URLs (beginning with <tt>http://</tt>), absolute local urls "
              "(beginning with <tt>/</tt>) or relative URLs (that are relative to <tt>check_mk/</tt>)."
             ) % html.render_icon("url")),
        size=80,
>>>>>>> upstream/master
    )


def _type_name(v):
    try:
        return type(v).__name__
    except Exception:
<<<<<<< HEAD
        return html.attrencode(type(v))
=======
        return escaping.escape_attribute(str(type(v)))
>>>>>>> upstream/master
