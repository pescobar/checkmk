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

import abc
import json
import inspect
<<<<<<< HEAD
import six
=======
from typing import Any, Callable, Dict, Mapping, Optional, Type
>>>>>>> upstream/master

import cmk.utils.plugin_registry
from cmk.gui.globals import html
import cmk.gui.config as config
<<<<<<< HEAD
from cmk.gui.exceptions import MKException
from cmk.gui.log import logger


class Page(six.with_metaclass(abc.ABCMeta, object)):
    @classmethod
    #TODO: Use when we are using python3 abc.abstractmethod
    def ident(cls):
        raise NotImplementedError()

    def handle_page(self):
        self.page()

    @abc.abstractmethod
    def page(self):
=======
from cmk.utils.exceptions import MKException
from cmk.gui.log import logger

PageHandlerFunc = Callable[[], None]
PageResult = Any
AjaxPageResult = Dict[str, Any]


# At the moment pages are simply callables that somehow render content for the HTTP response
# and send it to the client.
#
# At least for HTML pages we should standardize the pages a bit more since there are things all pages do
# - Create a title, render the header
# - Have a breadcrumb
# - Optional: Handle actions
# - Render the page
#
# TODO: Check out the WatoMode class and find out how to do this. Looks like handle_page() could
# implement parts of the cmk.gui.wato.page_handler.page_handler() logic.
class Page(metaclass=abc.ABCMeta):
    # TODO: In theory a page class could be registered below multiple URLs. For this case it would
    # be better to move the ident out of the class, to the registry. At the moment the URL is stored
    # in self._ident by PageRegistry.register_page().
    # In practice this is no problem at the moment, because each page is accessible only through a
    # single endpoint.
    @classmethod
    def ident(cls) -> str:
        raise NotImplementedError()

    def handle_page(self) -> None:
        self.page()

    @abc.abstractmethod
    def page(self) -> PageResult:
>>>>>>> upstream/master
        """Override this to implement the page functionality"""
        raise NotImplementedError()


# TODO: Clean up implicit _from_vars() procotocol
<<<<<<< HEAD
class AjaxPage(six.with_metaclass(abc.ABCMeta, Page)):
=======
class AjaxPage(Page, metaclass=abc.ABCMeta):
>>>>>>> upstream/master
    """Generic page handler that wraps page() calls into AJAX respones"""
    def __init__(self):
        super(AjaxPage, self).__init__()
        self._from_vars()

<<<<<<< HEAD
    def _from_vars(self):
        """Override this method to set mode specific attributes based on the
        given HTTP variables."""
        pass

    def webapi_request(self):
        return html.get_request()

    def handle_page(self):
=======
    def _from_vars(self) -> None:
        """Override this method to set mode specific attributes based on the
        given HTTP variables."""

    def webapi_request(self) -> Dict[str, str]:
        return html.get_request()

    @abc.abstractmethod
    def page(self) -> AjaxPageResult:
        """Override this to implement the page functionality"""
        raise NotImplementedError()

    def handle_page(self) -> None:
>>>>>>> upstream/master
        """The page handler, called by the page registry"""
        html.set_output_format("json")
        try:
            action_response = self.page()
            response = {"result_code": 0, "result": action_response}
        except MKException as e:
            response = {"result_code": 1, "result": "%s" % e}

        except Exception as e:
            if config.debug:
                raise
            logger.exception("error calling AJAX page handler")
            response = {"result_code": 1, "result": "%s" % e}

        html.write(json.dumps(response))


<<<<<<< HEAD
class PageRegistry(cmk.utils.plugin_registry.ClassRegistry):
    def plugin_base_class(self):
        return Page

    def plugin_name(self, plugin_class):
        return plugin_class.ident()

    def register_page(self, path):
        def wrap(plugin_class):
            if not inspect.isclass(plugin_class):
                raise NotImplementedError()

            plugin_class._ident = path
            plugin_class.ident = classmethod(lambda cls: cls._ident)
=======
class PageRegistry(cmk.utils.plugin_registry.Registry[Type[Page]]):
    def plugin_name(self, instance: Type[Page]) -> str:
        return instance.ident()

    def register_page(self, path: str) -> Callable[[Type[Page]], Type[Page]]:
        def wrap(plugin_class: Type[Page]) -> Type[Page]:
            if not inspect.isclass(plugin_class):
                raise NotImplementedError()

            # mypy is not happy with this. Find a cleaner way
            plugin_class._ident = path  # type: ignore[attr-defined]
            plugin_class.ident = classmethod(lambda cls: cls._ident)  # type: ignore[assignment]
>>>>>>> upstream/master

            self.register(plugin_class)
            return plugin_class

        return wrap


page_registry = PageRegistry()


# TODO: Refactor all call sites to sub classes of Page() and change the
# registration to page_registry.register("path")
<<<<<<< HEAD
def register(path):
=======
def register(path: str) -> Callable[[PageHandlerFunc], PageHandlerFunc]:
>>>>>>> upstream/master
    """Register a function to be called when the given URL is called.

    In case you need to register some callable like staticmethods or
    classmethods, you will have to use register_page_handler() directly
    because this decorator can not deal with them.

    It is essentially a decorator that calls register_page_handler().
    """
<<<<<<< HEAD
    def wrap(wrapped_callable):
=======
    def wrap(wrapped_callable: PageHandlerFunc) -> PageHandlerFunc:
>>>>>>> upstream/master
        cls_name = "PageClass%s" % path.title().replace(":", "")
        LegacyPageClass = type(cls_name, (Page,), {
            "_wrapped_callable": (wrapped_callable,),
            "page": lambda self: self._wrapped_callable[0]()
        })

        page_registry.register_page(path)(LegacyPageClass)
        return lambda: LegacyPageClass().handle_page()

    return wrap


# TODO: replace all call sites by directly calling page_registry.register_page("path")
<<<<<<< HEAD
def register_page_handler(path, page_func):
=======
def register_page_handler(path: str, page_func: PageHandlerFunc) -> PageHandlerFunc:
>>>>>>> upstream/master
    """Register a function to be called when the given URL is called."""
    wrap = register(path)
    return wrap(page_func)


<<<<<<< HEAD
def get_page_handler(name, dflt=None):
=======
def get_page_handler(name: str,
                     dflt: Optional[PageHandlerFunc] = None) -> Optional[PageHandlerFunc]:
>>>>>>> upstream/master
    """Returns either the page handler registered for the given name or None

    In case dflt is given it returns dflt instead of None when there is no
    page handler for the requested name."""
<<<<<<< HEAD
    handle_class = page_registry.get(name)
    if handle_class is None:
        return dflt
    return lambda: handle_class().handle_page()
=======
    # NOTE: Workaround for our non-generic registries... :-/
    pr: Mapping[str, Type[Page]] = page_registry
    handle_class = pr.get(name)
    if handle_class is None:
        return dflt
    # NOTE: We can'use functools.partial because of https://bugs.python.org/issue3445
    return (lambda hc: lambda: hc().handle_page())(handle_class)
>>>>>>> upstream/master
