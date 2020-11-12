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

# This is our home-grown version of flask.globals and flask.ctx. It
# can be removed when fully do things the flasky way.

from functools import partial
import logging
<<<<<<< HEAD
from typing import Any, Union  # pylint: disable=unused-import

from werkzeug.local import LocalProxy
from werkzeug.local import LocalStack

import cmk.gui.htmllib  # pylint: disable=unused-import

#####################################################################
# a namespace for storing data during an application context
=======

from typing import Any, TYPE_CHECKING, Optional, List

from werkzeug.local import LocalProxy, LocalStack

#####################################################################
# a namespace for storing data during an application context
# Cyclical import

if TYPE_CHECKING:
    from cmk.gui import htmllib, http, config, userdb
>>>>>>> upstream/master

_sentinel = object()


<<<<<<< HEAD
class _AppCtxGlobals(object):
=======
class _AppCtxGlobals:
>>>>>>> upstream/master
    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    def pop(self, name, default=_sentinel):
        if default is _sentinel:
            return self.__dict__.pop(name)
        return self.__dict__.pop(name, default)

    def setdefault(self, name, default=None):
        return self.__dict__.setdefault(name, default)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)


#####################################################################
# application context

_app_ctx_stack = LocalStack()


def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError("Working outside of application context.")
    return getattr(top, name)


<<<<<<< HEAD
class AppContext(object):
=======
class AppContext:
>>>>>>> upstream/master
    def __init__(self, app):
        self.app = app
        self.g = _AppCtxGlobals()

    def __enter__(self):
        _app_ctx_stack.push(self)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        _app_ctx_stack.pop()


current_app = LocalProxy(partial(_lookup_app_object, "app"))
<<<<<<< HEAD
g = LocalProxy(partial(_lookup_app_object, "g"))  # type: Any
=======
g: Any = LocalProxy(partial(_lookup_app_object, "g"))
>>>>>>> upstream/master

######################################################################
# TODO: This should live somewhere else...


class _PrependURLFilter(logging.Filter):
    def filter(self, record):
        if record.levelno >= logging.ERROR:
<<<<<<< HEAD
            record.msg = "%s %s" % (html.request.requested_url, record.msg)
=======
            record.msg = "%s %s" % (request.requested_url, record.msg)
>>>>>>> upstream/master
        return True


######################################################################
# request context

_request_ctx_stack = LocalStack()


def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError("Working outside of request context.")
<<<<<<< HEAD
    return getattr(top, name)


class RequestContext(object):
    def __init__(self, html_obj):
        self.html = html_obj
=======

    if name is None:
        return top

    return getattr(top, name)


class RequestContext:
    def __init__(self, html_obj=None, req=None, resp=None):
        self.html = html_obj
        self.auth_type = None
        self.session: Optional["userdb.SessionInfo"] = None
        self.flashes: Optional[List[str]] = None

        if req is None and html_obj:
            req = html_obj.request
        if resp is None and html_obj:
            resp = html_obj.response

        self.request = req
        self.response = resp
        # TODO: cyclical import with config -> globals -> config -> ...
        from cmk.gui.config import LoggedInNobody
        self.user = LoggedInNobody()
>>>>>>> upstream/master

    def __enter__(self):
        _request_ctx_stack.push(self)
        # TODO: Move this plus the corresponding cleanup code to hooks.
        self._web_log_handler = logging.getLogger().handlers[0]
        self._prepend_url_filter = _PrependURLFilter()
        self._web_log_handler.addFilter(self._prepend_url_filter)

        return self

    def __exit__(self, exc_type, exc_value, tb):
        self._web_log_handler.removeFilter(self._prepend_url_filter)
<<<<<<< HEAD
        _request_ctx_stack.pop()
        self.html.finalize()
=======
        # html.finalize needs to be called before popping the stack, because it does
        # something with the user object. We make this optional, so we can use the RequestContext
        # without the html object (for APIs for example).
        if self.html is not None:
            self.html.finalize()
        _request_ctx_stack.pop()
>>>>>>> upstream/master


# NOTE: Flask offers the proxies below, and we should go into that direction,
# too. But currently our html class is a swiss army knife with tons of
<<<<<<< HEAD
# resposibilites which we should really, really split up...
#
# request = LocalProxy(partial(_lookup_req_object, "request"))
# session = LocalProxy(partial(_lookup_req_object, "session"))

html = LocalProxy(partial(_lookup_req_object,
                          "html"))  # type: Union[cmk.gui.htmllib.html, LocalProxy]
=======
# responsibilities which we should really, really split up...
def request_local_attr(name=None):
    """Delegate access to the corresponding attribute on RequestContext

    When the returned object is accessed, the Proxy will fetch the current
    RequestContext from the LocalStack and return the attribute given by `name`.

    Args:
        name (str): The name of the attribute on RequestContext

    Returns:
        A proxy which wraps the value stored on RequestContext.

    """
    return LocalProxy(partial(_lookup_req_object, name))


local = request_local_attr()  # None as name will get the whole object.

# NOTE: All types FOO below are actually a Union[Foo, LocalProxy], but
# LocalProxy is meant as a transparent proxy, so we leave it out to de-confuse
# mypy. LocalProxy uses a lot of reflection magic, which can't be understood by
# tools in general.
user: 'config.LoggedInUser' = request_local_attr('user')
request: 'http.Request' = request_local_attr('request')
session: 'userdb.Session' = request_local_attr('session')

html: 'htmllib.html' = request_local_attr('html')
>>>>>>> upstream/master
