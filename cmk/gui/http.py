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
"""Wrapper layer between WSGI and the GUI application code"""

import re

import six
import werkzeug.http
import werkzeug.wrappers

import cmk.gui.log as log
from cmk.gui.i18n import _

# TODO: For some aracane reason, we are a bit restrictive about the allowed
# variable names. Try to figure out why...
_VARNAME_REGEX = re.compile(r'^[:\w.%*+=-]+$')


def _valid_varname(v):
    return _VARNAME_REGEX.match(v)


class Request(object):
    """Provides information about the users HTTP request to the application

    This class essentially wraps the information provided with the WSGI environment
    and provides some low level functions to the application for accessing these
    information. These should be basic HTTP request handling things and no application
    specific mechanisms."""
    def __init__(self, wsgi_environ):
        super(Request, self).__init__()
        self._logger = log.logger.getChild("http.Request")
        self._wsgi_environ = wsgi_environ

        # Last occurrence takes precedence, making appending to current URL simpler
        wrequest = werkzeug.wrappers.Request(wsgi_environ)
        self._vars = {k: vs[-1].encode("utf-8") \
                      for k, vs in wrequest.values.lists()
                      if _valid_varname(k)}

        # NOTE: There could be multiple entries with the same key, we ignore that for now...
        self._uploads = {}
        for k, f in wrequest.files.iteritems():
            # TODO: We read the whole data here and remember it. Should we
            # offer the underlying stream directly?
            self._uploads[k] = (f.filename, f.mimetype, f.read())
            f.close()

        # TODO: To be compatible with Check_MK <1.5 handling / code base we
        # prevent parse_cookie() from decoding the stuff to unicode. One bright
        # day we'll switch all input stuff to be parsed to unicode, then we'll
        # clean this up!
        self.cookies = werkzeug.http.parse_cookie(wsgi_environ, charset=None)

    @property
    def requested_file(self):
        return self._wsgi_environ["SCRIPT_NAME"]

    @property
    def requested_url(self):
        return self._wsgi_environ["REQUEST_URI"]

    @property
    def request_method(self):
        return self._wsgi_environ['REQUEST_METHOD']

    @property
    def remote_ip(self):
        try:
            return self._wsgi_environ["HTTP_X_FORWARDED_FOR"].split(",")[-1].strip()
        except KeyError:
            return self._wsgi_environ["REMOTE_ADDR"]

    @property
    def remote_user(self):
        """Returns either the REMOTE_USER authenticated with the web server or None"""
        return self._wsgi_environ.get("REMOTE_USER")

    @property
    def is_ssl_request(self):
        return self._wsgi_environ.get("HTTP_X_FORWARDED_PROTO") == "https"

    @property
    def is_multithreaded(self):
        return self._wsgi_environ.get("wsgi.multithread", False)

    @property
    def user_agent(self):
        return self._wsgi_environ.get("USER_AGENT", "")

    @property
    def referer(self):
        return self._wsgi_environ.get("REFERER")

    @property
    def request_timeout(self):
        """The system web servers configured request timeout. This is the time
        before the request is terminated from the view of the client."""
        # TODO: Found no way to get this information from WSGI environment. Hard code
        # the timeout for the moment.
        return 110

    def get_request_header(self, key, deflt=None):
        """Returns the value of a HTTP request header

        Applies the CGI variable name mangling to the requested variable name
        which is used by Apache 2.4+ and mod_wsgi to finally produce the
        wsgi_environ.

        a) mod_wsgi/Apache only make the variables available that consist of alpha numeric
           and minus characters. Other variables are skipped.
        b) e.g. X-Remote-User is available as HTTP_X_REMOTE_USER
        """
        env_key = "HTTP_%s" % key.upper().replace("-", "_")
        return self._wsgi_environ.get(env_key, deflt)

    def has_cookie(self, varname):
        """Whether or not the client provides a cookie with the given name"""
        return varname in self.cookies

    def get_cookie_names(self):
        """Return the names of all cookies sent by the client"""
        return self.cookies.keys()

    def cookie(self, varname, deflt=None):
        """Return either the value of the cookie provided by the client, the given deflt value or None"""
        try:
            return self.cookies[varname]
        except KeyError:
            return deflt

    #
    # Variable handling
    #

    def var(self, varname, deflt=None):
        return self._vars.get(varname, deflt)

    def has_var(self, varname):
        return varname in self._vars

    def itervars(self, prefix=""):
        return (item \
                for item in self._vars.iteritems() \
                if item[0].startswith(prefix))

    # TODO: self._vars should be strictly read only in the Request() object
    def set_var(self, varname, value):
        if not isinstance(value, six.string_types):
            raise TypeError(_("Only str and unicode values are allowed, got %s") % type(value))

        # All items in self._vars are encoded at the moment. This should be changed one day,
        # but for the moment we treat vars set with set_var() equal to the vars received from
        # the HTTP request.
        if isinstance(varname, six.text_type):
            varname = varname.encode("utf-8")
        if isinstance(value, six.text_type):
            value = value.encode("utf-8")

        self._vars[varname] = value

    # TODO: self._vars should be strictly read only in the Request() object
    def del_var(self, varname):
        self._vars.pop(varname, None)

    # TODO: self._vars should be strictly read only in the Request() object
    def del_vars(self, prefix=""):
        for varname, _value in list(self.itervars(prefix)):
            self.del_var(varname)

    def uploaded_file(self, varname):
        # returns either a triple of (filename, mime-type, content) or None
        return self._uploads.get(varname)


class Response(werkzeug.wrappers.Response):
    # NOTE: Currently we rely on a *relavtive* Location header in redirects!
    autocorrect_location_header = False

    def __init__(self, is_secure, *args, **kwargs):
        super(Response, self).__init__(*args, **kwargs)
        self._is_secure = is_secure

    def set_http_cookie(self, key, value, secure=None):
        if secure is None:
            secure = self._is_secure
        super(Response, self).set_cookie(key, value, secure=secure, httponly=True)
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Wrapper layer between WSGI and GUI application code"""

from typing import List, Optional, Any, Iterator, Union, Dict, Tuple, TypeVar

from six import ensure_binary, ensure_str
import werkzeug.wrappers
import werkzeug.wrappers.json as json
from werkzeug.utils import get_content_type

from cmk.gui.globals import request
from cmk.gui.i18n import _
from cmk.gui.exceptions import MKUserError

UploadedFile = Tuple[str, str, bytes]
T = TypeVar('T')


class LegacyVarsMixin:
    """Holds a dict of vars.

    These vars are being set throughout the codebase. Using this Mixin the vars will
    not modify the default request variables but rather shadow them. In the case of vars
    being removed, the variables from the request will show up again (given they were
    shadowed in the first place).
    """
    DELETED = object()

    def __init__(self, *args: Any, **kw: Any) -> None:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # [mypy:] Too many arguments for "__init__" of "object"  [call-arg]
        super(LegacyVarsMixin, self).__init__(*args, **kw)  # type: ignore[call-arg]
        self.legacy_vars = self._vars = {}  # type: Dict[str, Union[str, object]]

    def set_var(self, varname: str, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(_("Only str and unicode values are allowed, got %s") % type(value))

        # Py2: All items in self._vars are encoded at the moment. This should be changed one day,
        # but for the moment we treat vars set with set_var() equal to the vars received from the
        # HTTP request.
        varname = ensure_str(varname)
        value = ensure_str(value)

        self.legacy_vars[varname] = value

    def del_var(self, varname: str) -> None:
        varname = ensure_str(varname)
        self.legacy_vars[varname] = self.DELETED

    def del_vars(self, prefix: str = "") -> None:
        for varname, _value in list(self.legacy_vars.items()):
            if varname.startswith(prefix):
                self.del_var(varname)

    def itervars(self, prefix: str = "") -> Iterator[Tuple[str, str]]:
        skip = []
        for name, value in self.legacy_vars.items():
            if name.startswith(prefix):
                skip.append(name)
                if value is self.DELETED:
                    continue
                assert isinstance(value, str)
                yield name, value

        # We only fall through to the real HTTP request if our var isn't set and isn't deleted.
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        for name, val in super(LegacyVarsMixin, self).itervars(prefix=prefix):  # type: ignore[misc]
            if name in skip:
                continue
            yield name, val

    def has_var(self, varname: str) -> bool:
        varname = ensure_str(varname)
        if varname in self.legacy_vars:
            return self.legacy_vars[varname] is not self.DELETED

        # We only fall through to the real HTTP request if our var isn't set and isn't deleted.
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        return super(LegacyVarsMixin, self).has_var(varname)  # type: ignore[misc]

    def var(self, varname: str, default: Optional[str] = None) -> Optional[str]:
        varname = ensure_str(varname)
        legacy_var = self.legacy_vars.get(varname, None)
        if legacy_var is not None:
            if legacy_var is not self.DELETED:
                assert isinstance(legacy_var, str)
                return legacy_var
            return default
        # We only fall through to the real HTTP request if our var isn't set and isn't deleted.
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        return super(LegacyVarsMixin, self).var(varname, default)  # type: ignore[misc]


class LegacyUploadMixin:
    def __init__(self, *args: Any, **kw: Any) -> None:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # [mypy:] Too many arguments for "__init__" of "object"  [call-arg]
        super(LegacyUploadMixin, self).__init__(*args, **kw)  # type: ignore[call-arg]
        self.upload_cache: Dict[str, UploadedFile] = {}

    def uploaded_file(self, name: str) -> UploadedFile:
        # NOTE: There could be multiple entries with the same key, we ignore that for now...
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        f = self.files.get(name)  # type: ignore[attr-defined]
        if name not in self.upload_cache and f:
            self.upload_cache[name] = (f.filename, f.mimetype, f.read())
            f.close()

        try:
            upload = self.upload_cache[name]
        except KeyError:
            raise MKUserError(name, _("Please choose a file to upload."))

        return upload


class LegacyDeprecatedMixin:
    """Some wrappers which are still used while their use is considered deprecated.

    They are to be removed as they provide no additional value over the already available
    methods and properties in Request itself.
    """
    def itervars(self, prefix: str = "") -> Iterator[Tuple[str, Optional[str]]]:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        for name, values in self.values.lists():  # type: ignore[attr-defined]
            if name.startswith(prefix):
                # Preserve previous behaviour
                yield name, ensure_str(values[-1]) if values else None

    def var(self, name: str, default: Optional[str] = None) -> Optional[str]:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        values = self.values.getlist(name)  # type: ignore[attr-defined]
        if not values:
            return default

        # Preserve previous behaviour
        return ensure_str(values[-1])

    def has_var(self, varname: str) -> bool:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return varname in self.values  # type: ignore[attr-defined]

    def has_cookie(self, varname: str) -> bool:
        """Whether or not the client provides a cookie with the given name"""
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return varname in self.cookies  # type: ignore[attr-defined]

    def cookie(self, varname: str, default: Optional[str] = None) -> Optional[str]:
        """Return the value of the cookie provided by the client.

        If the cookie has not been set, None will be returned as a default.
        This default can be changed by passing is as the second parameter."""
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        value = self.cookies.get(varname, default)  # type: ignore[attr-defined]
        if value is not None:
            # Why would we want to do that? test_http.py requires it though.
            return ensure_str(value)
        return None

    def get_request_header(self, key: str, default: Optional[str] = None) -> Optional[str]:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return self.headers.get(key, default)  # type: ignore[attr-defined]

    def get_cookie_names(self) -> List[str]:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return list(self.cookies.keys())  # type: ignore[attr-defined]

    @property
    def referer(self) -> Optional[str]:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return self.referrer  # type: ignore[attr-defined]

    @property
    def request_method(self) -> str:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return self.method  # type: ignore[attr-defined]

    @property
    def requested_url(self) -> str:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return self.url  # type: ignore[attr-defined]

    @property
    def requested_file(self) -> str:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return self.base_url  # type: ignore[attr-defined]

    @property
    def is_ssl_request(self) -> bool:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return self.is_secure  # type: ignore[attr-defined]

    @property
    def remote_ip(self) -> str:
        # TODO: mypy does not know about the related mixin classes. This whole class can be cleaned
        # up with 1.7, once we have moved to python 3.
        # TODO: Deprecated
        return self.remote_addr  # type: ignore[attr-defined]


def mandatory_parameter(varname: str, value: Optional[T]) -> T:
    if value is None:
        raise MKUserError(varname, _("The parameter \"%s\" is missing.") % varname)
    return value


class Request(LegacyVarsMixin, LegacyUploadMixin, LegacyDeprecatedMixin, json.JSONMixin,
              werkzeug.wrappers.Request):
    """Provides information about the users HTTP-request to the application

    This class essentially wraps the information provided with the WSGI environment
    and provides some low level functions to the application for accessing this information.
    These should be basic HTTP request handling things and no application specific mechanisms.
    """
    # pylint: disable=too-many-ancestors
    @property
    def request_timeout(self) -> int:
        """The system web servers configured request timeout.

        This is the time before the request terminates from the view of the client."""
        # TODO: Found no way to get this information from WSGI environment. Hard code
        #       the timeout for the moment.
        return 110

    def get_str_input(self, varname: str, deflt: Optional[str] = None) -> Optional[str]:
        try:
            val = self.var(varname, ensure_str(deflt) if deflt is not None else None)
            if val is None:
                return None
            return ensure_str(val)
        except UnicodeDecodeError:
            raise MKUserError(
                varname,
                _("The given text is wrong encoded. "
                  "You need to provide a UTF-8 encoded text."))

    def get_str_input_mandatory(self, varname: str, deflt: Optional[str] = None) -> str:
        return mandatory_parameter(varname, self.get_str_input(varname, deflt))

    def get_ascii_input(self, varname: str, deflt: Optional[str] = None) -> Optional[str]:
        """Helper to retrieve a byte string and ensure it only contains ASCII characters
        In case a non ASCII character is found an MKUserError() is raised."""
        value = self.get_str_input(varname, deflt)
        if value is None:
            return value
        if not value.isascii():
            raise MKUserError(varname, _("The given text must only contain ASCII characters."))
        return value

    def get_ascii_input_mandatory(self, varname: str, deflt: Optional[str] = None) -> str:
        return mandatory_parameter(varname, self.get_ascii_input(varname, deflt))

    def get_unicode_input(self, varname: str, deflt: Optional[str] = None) -> Optional[str]:
        return self.get_str_input(varname, deflt)

    def get_unicode_input_mandatory(self, varname, deflt=None) -> str:
        return mandatory_parameter(varname, self.get_str_input_mandatory(varname, deflt))

    def get_binary_input(self, varname: str, deflt: Optional[bytes] = None) -> Optional[bytes]:
        val = self.var(varname, ensure_str(deflt) if deflt is not None else None)
        if val is None:
            return None
        return ensure_binary(val)

    def get_binary_input_mandatory(self, varname: str, deflt: Optional[bytes] = None) -> bytes:
        return mandatory_parameter(varname, self.get_binary_input(varname, deflt))

    def get_integer_input(self, varname: str, deflt: Optional[int] = None) -> Optional[int]:

        value = self.var(varname, "%d" % deflt if deflt is not None else None)
        if value is None:
            return None

        try:
            return int(value)
        except ValueError:
            raise MKUserError(varname, _("The parameter \"%s\" is not an integer.") % varname)

    def get_integer_input_mandatory(self, varname: str, deflt: Optional[int] = None) -> int:
        return mandatory_parameter(varname, self.get_integer_input(varname, deflt))

    def get_float_input(self, varname: str, deflt: Optional[float] = None) -> Optional[float]:

        value = self.var(varname, "%s" % deflt if deflt is not None else None)
        if value is None:
            return None

        try:
            return float(value)
        except ValueError:
            raise MKUserError(varname, _("The parameter \"%s\" is not a float.") % varname)

    def get_float_input_mandatory(self, varname: str, deflt: Optional[float] = None) -> float:
        return mandatory_parameter(varname, self.get_float_input(varname, deflt))


class Response(werkzeug.wrappers.Response):
    # NOTE: Currently we rely on a *relative* Location header in redirects!
    autocorrect_location_header = False

    def set_http_cookie(self, key: str, value: str, secure: Optional[bool] = None) -> None:
        if secure is None:
            secure = request.is_secure
        super(Response, self).set_cookie(key, value, secure=secure, httponly=True, samesite="Lax")

    def set_content_type(self, mime_type: str) -> None:
        self.headers["Content-type"] = get_content_type(mime_type, self.charset)
>>>>>>> upstream/master
