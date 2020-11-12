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

import httplib
from typing import Optional, Text  # pylint: disable=unused-import

from werkzeug.http import HTTP_STATUS_CODES

from cmk.gui.i18n import _

from cmk.utils.exceptions import MKGeneralException, MKException, MKTimeout
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import http.client
from typing import Optional

from werkzeug.http import HTTP_STATUS_CODES

from cmk.utils.exceptions import (
    MKException,
    MKGeneralException,
    MKTimeout,
)
>>>>>>> upstream/master


class RequestTimeout(MKTimeout):
    """Is raised from the alarm signal handler (handle_request_timeout()) to
    abort page processing before the system apache times out."""
<<<<<<< HEAD
    pass


class FinalizeRequest(Exception):
    """Is used to end the HTTP request processing from deeper code levels"""
    def __init__(self, code):
        # type: (int) -> None
=======


class FinalizeRequest(MKException):
    """Is used to end the HTTP request processing from deeper code levels"""
    def __init__(self, code: int) -> None:
>>>>>>> upstream/master
        super(FinalizeRequest, self).__init__("%d %s" % (code, HTTP_STATUS_CODES[code]))
        self.status = code


class HTTPRedirect(FinalizeRequest):
    """Is used to end the HTTP request processing from deeper code levels
    and making the client request another page after receiving the response."""
<<<<<<< HEAD
    def __init__(self, url):
        # type: (str) -> None
        super(HTTPRedirect, self).__init__(httplib.FOUND)
        self.url = url  #type: str


class MKAuthException(MKException):
    def __init__(self, reason):
        # type: (str) -> None
        self.reason = reason  # type: str
        super(MKAuthException, self).__init__(reason)

    def __str__(self):
        # type: () -> str
        return self.reason

    def title(self):
        # type: () -> unicode
        return _("Permission denied")

    def plain_title(self):
        # type: () -> unicode
        return _("Authentication error")


class MKUnauthenticatedException(MKGeneralException):
    def title(self):
        # type: () -> unicode
        return _("Not authenticated")

    def plain_title(self):
        # type: () -> unicode
        return _("Missing authentication credentials")


class MKConfigError(MKException):
    def title(self):
        # type: () -> unicode
        return _("Configuration error")

    def plain_title(self):
        # type: () -> unicode
        return self.title()


class MKUserError(MKException):
    def __init__(self, varname, message):
        # type: (Optional[str], Text) -> None
        self.varname = varname  # type: Optional[str]
        self.message = message  # type: Text
=======
    def __init__(self, url: str, code: int = http.client.FOUND) -> None:
        super(HTTPRedirect, self).__init__(code)
        self.url: str = url


class MKAuthException(MKException):
    pass


class MKUnauthenticatedException(MKGeneralException):
    pass


class MKConfigError(MKException):
    pass


class MKUserError(MKException):
    def __init__(self, varname: Optional[str], message: str) -> None:
        self.varname: Optional[str] = varname
        self.message: str = message
>>>>>>> upstream/master
        super(MKUserError, self).__init__(varname, message)

    def __str__(self):
        return self.message

<<<<<<< HEAD
    def title(self):
        # type: () -> Text
        return _("Invalid User Input")

    def plain_title(self):
        # type: () -> Text
        return _("User error")

=======
>>>>>>> upstream/master

class MKInternalError(MKException):
    pass
