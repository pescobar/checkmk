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
"""MK Livestatus Python API"""

import socket
import time
import re
import os
import ast
import ssl
<<<<<<< HEAD
from typing import Tuple, Union, Dict, Pattern, Optional  # pylint: disable=unused-import

try:
    from cmk.gui.i18n import _
except ImportError:
    _ = lambda x: x
=======
from typing import NewType, AnyStr, Any, Type, List, Tuple, Union, Dict, Pattern, Optional, Set

# TODO: Find a better solution for this issue. Astroid 2.x bug prevents us from using NewType :(
# (https://github.com/PyCQA/pylint/issues/2296)
UserId = str  # NewType("UserId", str)
SiteId = str  # NewType("SiteId", str)
SiteConfiguration = Dict[str, Any]  # NewType("SiteConfiguration", Dict[str, Any])
SiteConfigurations = Dict[
    SiteId, SiteConfiguration]  # NewType("SiteConfigurations", Dict[SiteId, SiteConfiguration])

LivestatusColumn = Any
LivestatusRow = NewType("LivestatusRow", List[LivestatusColumn])
LivestatusResponse = NewType("LivestatusResponse", List[LivestatusRow])
>>>>>>> upstream/master

#   .--Globals-------------------------------------------------------------.
#   |                    ____ _       _           _                        |
#   |                   / ___| | ___ | |__   __ _| |___                    |
#   |                  | |  _| |/ _ \| '_ \ / _` | / __|                   |
#   |                  | |_| | | (_) | |_) | (_| | \__ \                   |
#   |                   \____|_|\___/|_.__/ \__,_|_|___/                   |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Global variables and Exception classes                              |
#   '----------------------------------------------------------------------'

# TODO: This mechanism does not take different connection options into account
# Keep a global array of persistant connections
<<<<<<< HEAD
persistent_connections = {}  # type: Dict[str, socket.socket]

# Regular expression for removing Cache: headers if caching is not allowed
remove_cache_regex = re.compile("\nCache:[^\n]*")  # type: Pattern


def ensure_unicode(text):
    if hasattr(text, "decode"):
        try:
            return text.decode("utf-8")
        except UnicodeEncodeError:
            return text
    return text


def ensure_bytestr(text):
    try:
        return text.encode("utf-8")
    except UnicodeDecodeError:
        return text


class MKLivestatusException(Exception):
    def __init__(self, value):
        self.parameter = value
        super(MKLivestatusException, self).__init__(value)

    def __str__(self):
        return str(self.parameter)
=======
persistent_connections: Dict[str, socket.socket] = {}

# Regular expression for removing Cache: headers if caching is not allowed
remove_cache_regex: Pattern = re.compile("\nCache:[^\n]*")


def _ensure_unicode(value: Union[str, bytes]) -> str:
    if isinstance(value, str):
        return value
    return value.decode("utf-8")


class MKLivestatusException(Exception):
    pass

>>>>>>> upstream/master

    def plain_title(self):
        return _("Livestatus problem")

    def title(self):
        return _("Livestatus problem")


class MKLivestatusSocketError(MKLivestatusException):
    pass


class MKLivestatusSocketClosed(MKLivestatusSocketError):
    pass


class MKLivestatusConfigError(MKLivestatusException):
    pass


class MKLivestatusQueryError(MKLivestatusException):
    pass


class MKLivestatusNotFoundError(MKLivestatusException):
<<<<<<< HEAD
    def __str__(self):
        return "No matching entries found for query %s" % str(self.parameter)

    def plain_title(self):
        return _("Livestatus-data not found")

    def title(self):
        return _("Data not found")
=======
    pass
>>>>>>> upstream/master


class MKLivestatusTableNotFoundError(MKLivestatusException):
    pass


# We need some unique value here
NO_DEFAULT = lambda: None


# Escape/strip unwanted chars from (user provided) strings to
# use them in livestatus queries. Prevent injections of livestatus
# protocol related chars or strings
<<<<<<< HEAD
def lqencode(s):
    # It is not enough to strip off \n\n, because one might submit "\n \n",
    # which is also interpreted as termination of the last query and beginning
    # of the next query.
    return ensure_unicode(s).replace(u"\n", u"")


def quote_dict(s):
=======
def lqencode(s: AnyStr) -> str:
    # It is not enough to strip off \n\n, because one might submit "\n \n",
    # which is also interpreted as termination of the last query and beginning
    # of the next query.
    return _ensure_unicode(s).replace(u"\n", u"")


def quote_dict(s: str) -> str:
>>>>>>> upstream/master
    """Apply the quoting used for dict-valued columns (See #6972)"""
    return "'%s'" % s.replace(u"'", u"''")


<<<<<<< HEAD
def site_local_ca_path():
=======
def site_local_ca_path() -> str:
>>>>>>> upstream/master
    """Path to the site local CA bundle"""
    omd_root = os.getenv("OMD_ROOT")
    if not omd_root:
        raise MKLivestatusConfigError("OMD_ROOT is not set. You are not running in OMD context.")

    return os.path.join(omd_root, "var/ssl/ca-certificates.crt")


<<<<<<< HEAD
def create_client_socket(family, tls, verify, ca_file_path):
=======
def create_client_socket(family: socket.AddressFamily, tls: bool, verify: bool,
                         ca_file_path: Optional[str]) -> socket.socket:
>>>>>>> upstream/master
    """Create a client socket object for the livestatus connection"""
    sock = socket.socket(family, socket.SOCK_STREAM)

    if not tls:
        return sock

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED if verify else ssl.CERT_NONE
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

    ca_file_path = ca_file_path if ca_file_path is not None else site_local_ca_path()
    try:
        context.load_verify_locations(ca_file_path)
    except Exception as e:
        raise MKLivestatusConfigError("Failed to load CA file '%s': %s" % (ca_file_path, e))

    return context.wrap_socket(sock)


#.
#   .--Helpers-------------------------------------------------------------.
#   |                  _   _      _                                        |
#   |                 | | | | ___| |_ __   ___ _ __ ___                    |
#   |                 | |_| |/ _ \ | '_ \ / _ \ '__/ __|                   |
#   |                 |  _  |  __/ | |_) |  __/ |  \__ \                   |
#   |                 |_| |_|\___|_| .__/ \___|_|  |___/                   |
#   |                              |_|                                     |
#   +----------------------------------------------------------------------+
#   |  Helper class implementing some generic shortcut functions, e.g.     |
#   |  for fetching just one row or one single value.                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
class Helpers(object):
    def query(self, query, add_headers=""):
        raise NotImplementedError()

    def query_value(self, query, deflt=NO_DEFAULT):
=======
class Helpers:
    def query(self,
              query: 'QueryTypes',
              add_headers: Union[str, bytes] = u"") -> 'LivestatusResponse':
        raise NotImplementedError()

    def query_value(self, query: 'QueryTypes', deflt: Any = NO_DEFAULT) -> LivestatusColumn:
>>>>>>> upstream/master
        """Issues a query that returns exactly one line and one columns and returns
           the response as a single value"""
        normalized_query = Query(query) if not isinstance(query, Query) else query

        result = self.query(normalized_query, "ColumnHeaders: off\n")
        try:
            return result[0][0]
        except IndexError:
            if deflt == NO_DEFAULT:
                raise MKLivestatusNotFoundError("No matching entries found for query: %s" %
                                                normalized_query)
            return deflt

    def query_row(self, query: 'QueryTypes') -> LivestatusRow:
        """Issues a query that returns one line of data and returns the elements
           of that line as list"""
        normalized_query = Query(query) if not isinstance(query, Query) else query

        result = self.query(normalized_query, "ColumnHeaders: off\n")
        try:
            return result[0]
        except IndexError:
            raise MKLivestatusNotFoundError("No matching entries found for query: %s" %
                                            normalized_query)

    def query_row_assoc(self, query: 'QueryTypes') -> Dict[str, Any]:
        """Issues a query that returns one line of data and returns the elements
           of that line as a dictionary from column names to values"""
        normalized_query = Query(query) if not isinstance(query, Query) else query

        r = self.query(normalized_query, "ColumnHeaders: on\n")[0:2]
        return dict(zip(r[0], r[1]))

    def query_column(self, query: 'QueryTypes') -> List[LivestatusColumn]:
        """Issues a query that returns exactly one column and returns the values
           of all lines in that column as a single list"""
<<<<<<< HEAD
        return [l[0] for l in self.query(query, "ColumnHeaders: off\n")]
=======
        normalized_query = Query(query) if not isinstance(query, Query) else query
>>>>>>> upstream/master

        return [l[0] for l in self.query(normalized_query, "ColumnHeaders: off\n")]

    def query_column_unique(self, query: 'QueryTypes') -> List[LivestatusColumn]:
        """Issues a query that returns exactly one column and returns the values
           of all lines with duplicates removed. The "natural order" of the rows is
           not preserved."""
        normalized_query = Query(query) if not isinstance(query, Query) else query
        result: Set[LivestatusColumn] = set()
        for line in self.query(normalized_query, "ColumnHeaders: off\n"):
            result.add(line[0])
        return list(result)

    def query_table(self, query: 'QueryTypes') -> LivestatusResponse:
        """Issues a query that may return multiple lines and columns and returns
           a list of lists"""
        normalized_query = Query(query) if not isinstance(query, Query) else query

        return self.query(normalized_query, "ColumnHeaders: off\n")

    def query_table_assoc(self, query: 'QueryTypes') -> List[Dict[str, Any]]:
        """Issues a query that may return multiple lines and columns and returns
           a dictionary from column names to values for each line. This can be
           very ineffective for large response sets."""
        normalized_query = Query(query) if not isinstance(query, Query) else query

        response = self.query(normalized_query, "ColumnHeaders: on\n")
        headers = response[0]
        result = []
        for line in response[1:]:
            result.append(dict(zip(headers, line)))
        return result

<<<<<<< HEAD
    def query_summed_stats(self, query, add_headers=""):
        """Convenience function for adding up numbers from Stats queries
        Adds up results column-wise. This is useful for multisite queries."""
        data = self.query(query, add_headers)
        if not data:
            raise MKLivestatusNotFoundError("Empty result to Stats-Query")
=======
    def query_summed_stats(self,
                           query: 'QueryTypes',
                           add_headers: Union[str, bytes] = u"") -> List[int]:
        """Convenience function for adding up numbers from Stats queries
        Adds up results column-wise. This is useful for multisite queries."""
        normalized_query = Query(query) if not isinstance(query, Query) else query

        data = self.query(normalized_query, add_headers)
        if not data:
            raise MKLivestatusNotFoundError(
                "No matching entries found for query: Empty result to Stats-Query")
>>>>>>> upstream/master
        return [sum(column) for column in zip(*data)]


# TODO: Add more functionality to the Query class:
# - set_prepend_site
# - set_only_sites
# - set_auth_domain
# All these are mostly set for a single query and reset back to another
# value after the query. But nearly all of these usages does not care
# about resetting the option in case of an exception. This could be
# handled better using the query class
<<<<<<< HEAD
class Query(object):
=======
class Query:
>>>>>>> upstream/master
    """This object can be passed to all livestatus methods accepting a livestatus
    query. The object can be used to hand over the handling code some flags, for
    example to influence the error handling during query processing."""

<<<<<<< HEAD
    default_suppressed_exceptions = [MKLivestatusTableNotFoundError]

    def __init__(self, query, suppress_exceptions=None):
        super(Query, self).__init__()

        self._query = ensure_unicode(query)
=======
    default_suppressed_exceptions: List[Type[Exception]] = [MKLivestatusTableNotFoundError]

    def __init__(self,
                 query: Union[str, bytes],
                 suppress_exceptions: Optional[List[Type[Exception]]] = None) -> None:
        super(Query, self).__init__()

        self._query = _ensure_unicode(query)
>>>>>>> upstream/master

        if suppress_exceptions is None:
            self.suppress_exceptions = self.default_suppressed_exceptions
        else:
            self.suppress_exceptions = suppress_exceptions

<<<<<<< HEAD
    def __unicode__(self):
        return self._query

    def __str__(self):
        return self._query.encode("utf-8")

=======
    def __str__(self) -> str:
        return self._query


QueryTypes = Union[str, bytes, Query]
OnlySites = Optional[List[SiteId]]
DeadSite = Dict[str, Union[str, int, Exception, SiteConfiguration]]
>>>>>>> upstream/master

#.
#   .--SingleSiteConn------------------------------------------------------.
#   |  ____  _             _      ____  _ _        ____                    |
#   | / ___|(_)_ __   __ _| | ___/ ___|(_) |_ ___ / ___|___  _ __  _ __    |
#   | \___ \| | '_ \ / _` | |/ _ \___ \| | __/ _ \ |   / _ \| '_ \| '_ \   |
#   |  ___) | | | | | (_| | |  __/___) | | ||  __/ |__| (_) | | | | | | |  |
#   | |____/|_|_| |_|\__, |_|\___|____/|_|\__\___|\____\___/|_| |_|_| |_|  |
#   |                |___/                                                 |
#   +----------------------------------------------------------------------+
#   |  Connections to one local Unix or remote TCP socket.                 |
#   '----------------------------------------------------------------------'


class SingleSiteConnection(Helpers):
    def __init__(self,
<<<<<<< HEAD
                 socketurl,
                 persist=False,
                 allow_cache=False,
                 tls=False,
                 verify=True,
                 ca_file_path=None):
        # type: (str, bool, bool, bool, bool, Optional[str]) -> None
        """Create a new connection to a MK Livestatus socket"""
        super(SingleSiteConnection, self).__init__()
        self.prepend_site = False
        self.auth_users = {}  # type: Dict[str, str]
        # never filled, just to have the same API as MultiSiteConnection (TODO: Cleanup)
        self.deadsites = {}  # type: Dict[str, Dict[str, str]]
        self.limit = None
        self.add_headers = ""
        self.auth_header = ""
=======
                 socketurl: str,
                 persist: bool = False,
                 allow_cache: bool = False,
                 tls: bool = False,
                 verify: bool = True,
                 ca_file_path: Optional[str] = None) -> None:
        """Create a new connection to a MK Livestatus socket"""
        super(SingleSiteConnection, self).__init__()
        self.prepend_site = False
        self.auth_users: Dict[str, UserId] = {}
        # never filled, just to have the same API as MultiSiteConnection (TODO: Cleanup)
        self.deadsites: Dict[SiteId, DeadSite] = {}
        self.limit: Optional[int] = None
        self.add_headers = u""
        self.auth_header = u""
>>>>>>> upstream/master
        self.persist = persist
        self.allow_cache = allow_cache
        self.socketurl = socketurl
        self.socket: Optional[socket.socket] = None
        self.timeout: Optional[int] = None
        self.successful_persistence = False

        # Whether to establish an encrypted connection
        self.tls = tls
        # Whether to accept any certificate or to verify it
        self.tls_verify = verify
        self._tls_ca_file_path = ca_file_path

    @property
<<<<<<< HEAD
    def tls_ca_file_path(self):
        # type: () -> str
=======
    def tls_ca_file_path(self) -> str:
>>>>>>> upstream/master
        """CA file bundle to use for certificate verification"""
        if self._tls_ca_file_path is None:
            return site_local_ca_path()
        return self._tls_ca_file_path

<<<<<<< HEAD
    def successfully_persisted(self):
        # type: () -> bool
=======
    def successfully_persisted(self) -> bool:
>>>>>>> upstream/master
        return self.successful_persistence

    def add_header(self, header: str) -> None:
        self.add_headers += header + "\n"

    def set_timeout(self, timeout: int) -> None:
        self.timeout = timeout
        if self.socket:
            self.socket.settimeout(float(timeout))

    def connect(self) -> None:
        if self.persist and self.socketurl in persistent_connections:
            self.socket = persistent_connections[self.socketurl]
            self.successful_persistence = True
            return

        self.successful_persistence = False
        family, address = self._parse_socket_url(self.socketurl)
        self.socket = self._create_socket(family)

        # If a timeout is set, then we retry after a failure with mild
        # a binary backoff.
        if self.timeout:
            before = time.time()
            sleep_interval = 0.1

        while True:
            try:
                if self.timeout:
                    self.socket.settimeout(float(sleep_interval))
                self.socket.connect(address)
                break
            except ssl.SSLError as e:
                # Do not retry in case of SSL protocol / handshake errors. They don't seem to be
                # recoverable by retrying

                if "The handshake operation timed out" in str(e):
                    raise MKLivestatusSocketError("Cannot connect to '%s': %s. The encryption "
                                                  "settings are probably wrong." %
                                                  (self.socketurl, e))

                raise

            except Exception as e:
                if self.timeout:
                    time_left = self.timeout - (time.time() - before)
                    # only try again, if there is substantial time left
                    if time_left > sleep_interval:
                        time.sleep(sleep_interval)
                        sleep_interval *= 1.5
                        continue

                self.socket = None
                raise MKLivestatusSocketError("Cannot connect to '%s': %s" % (self.socketurl, e))

        if self.persist:
            persistent_connections[self.socketurl] = self.socket

<<<<<<< HEAD
    def _parse_socket_url(self, url):
        # type: (str) -> Tuple[socket.AddressFamily, Union[str, tuple]]
=======
    def _parse_socket_url(self, url: str) -> Tuple[socket.AddressFamily, Union[str, tuple]]:
>>>>>>> upstream/master
        """Parses a Livestatus socket URL to address family and address"""
        family_txt, url = url.split(":", 1)
        if family_txt == "unix":
            return socket.AF_UNIX, url

        if family_txt in ["tcp", "tcp6"]:
            try:
                host, port_txt = url.rsplit(":", 1)
                port = int(port_txt)
            except ValueError:
                raise MKLivestatusConfigError(
                    "Invalid livestatus tcp URL '%s'. "
                    "Correct example is 'tcp:somehost:6557' or 'tcp6:somehost:6557'" % url)
            address_family = socket.AF_INET if family_txt == "tcp" else socket.AF_INET6
            return address_family, (host, port)

        raise MKLivestatusConfigError("Invalid livestatus URL '%s'. "
                                      "Must begin with 'tcp:', 'tcp6:' or 'unix:'" % url)

<<<<<<< HEAD
    def _create_socket(self, family):
=======
    def _create_socket(self, family: socket.AddressFamily) -> socket.socket:
>>>>>>> upstream/master
        """Creates the Livestatus client socket

        It ensures that either a TLS secured socket or a plain text socket
        is being created."""
        return create_client_socket(family, self.tls, self.tls_verify, self._tls_ca_file_path)

<<<<<<< HEAD
    def disconnect(self):
=======
    def disconnect(self) -> None:
>>>>>>> upstream/master
        self.socket = None
        if self.persist:
            try:
                del persistent_connections[self.socketurl]
            except KeyError:
                pass
<<<<<<< HEAD

    def receive_data(self, size):
=======

    def receive_data(self, size: int) -> bytes:
        if self.socket is None:
            raise MKLivestatusSocketError("Socket to '%s' is not connected" % self.socketurl)

>>>>>>> upstream/master
        result = b""
        # Timeout is only honored when connecting
        self.socket.settimeout(None)
        while size > 0:
            packet = self.socket.recv(size)
            if not packet:
                raise MKLivestatusSocketClosed(
                    "Read zero data from socket, nagios server closed connection")
            size -= len(packet)
            result += packet
        return result

<<<<<<< HEAD
    def do_query(self, query, add_headers=""):
        self.send_query(query, add_headers)
        return self.recv_response(query, add_headers)

    def send_query(self, query_obj, add_headers="", do_reconnect=True):
        orig_query = query_obj

        query = "%s" % query_obj
=======
    # TODO: change all call sites to hand over Query + str
    def do_query(self, query: Query, add_headers: str = u"") -> LivestatusResponse:
        self.send_query(query, add_headers)
        return self.recv_response(query, add_headers)

    def send_query(self,
                   query_obj: Query,
                   add_headers: str = u"",
                   do_reconnect: bool = True) -> None:
        orig_query = query_obj

        query = u"%s" % query_obj
>>>>>>> upstream/master
        if not self.allow_cache:
            query = remove_cache_regex.sub("", query)

        if self.socket is None:
            self.connect()

        if not query.endswith("\n"):
            query += "\n"
        query += self.auth_header + self.add_headers
<<<<<<< HEAD
        query += "Localtime: %d\nOutputFormat: python\nKeepAlive: on\nResponseHeader: fixed16\n" % int(
            time.time())
=======
        query += "Localtime: %d\n" % int(time.time())
        query += "OutputFormat: python3\n"
        query += "KeepAlive: on\n"
        query += "ResponseHeader: fixed16\n"
>>>>>>> upstream/master
        query += add_headers

        if not query.endswith("\n"):
            query += "\n"
        query += "\n"

        if self.socket is None:
            raise MKLivestatusSocketError("Socket to '%s' is not connected" % self.socketurl)

        try:
<<<<<<< HEAD
            # socket.send() only works with byte strings
            query = ensure_bytestr(query)
            self.socket.send(query)
=======
            # TODO: Use socket.sendall()
            # socket.send() only works with byte strings
            self.socket.send(query.encode("utf-8"))
>>>>>>> upstream/master
        except IOError as e:
            if self.persist:
                del persistent_connections[self.socketurl]
                self.successful_persistence = False
            self.socket = None

            if do_reconnect:
                # Automatically try to reconnect in case of an error, but
                # only once.
                self.connect()
                self.send_query(orig_query, add_headers, False)
                return

            raise MKLivestatusSocketError("RC1:" + str(e))

    # Reads a response from the livestatus socket. If the socket is closed
    # by the livestatus server, we automatically make a reconnect and send
    # the query again (once). This is due to timeouts during keepalive.
<<<<<<< HEAD
    def recv_response(self, query=None, add_headers="", timeout_at=None):
=======
    def recv_response(self,
                      query: Optional[Query] = None,
                      add_headers: str = "",
                      timeout_at: Optional[float] = None) -> LivestatusResponse:
>>>>>>> upstream/master
        try:
            # Headers are always ASCII encoded
            resp = self.receive_data(16)
            code = resp[0:3].decode("ascii")
            try:
                length = int(resp[4:15].lstrip())
<<<<<<< HEAD
            except:
=======
            except Exception:
>>>>>>> upstream/master
                self.disconnect()
                raise MKLivestatusSocketError(
                    "Malformed output. Livestatus TCP socket might be unreachable or wrong"
                    "encryption settings are used.")

            data = self.receive_data(length).decode("utf-8")

            if code == "200":
                try:
                    return ast.literal_eval(data)
<<<<<<< HEAD
                except:
=======
                except Exception:
>>>>>>> upstream/master
                    self.disconnect()
                    raise MKLivestatusSocketError("Malformed output")

            elif code == "404":
                raise MKLivestatusTableNotFoundError("Not Found (%s): %s" % (code, data.strip()))

            else:
                raise MKLivestatusQueryError("%s: %s" % (code, data.strip()))

        except (MKLivestatusSocketClosed, IOError) as e:
            # In case of an IO error or the other side having
            # closed the socket do a reconnect and try again
            self.disconnect()

            # In case of unix socket connections, do not start any reconnection attempts
            # The other side (liveproxyd) might have had a good reason to disconnect
            # Note: In most scenarios the liveproxyd still tries to send back a reasonable
            # error response back to the client
            if self.socket and self.socket.family == socket.AF_UNIX:
                raise MKLivestatusSocketError("Unix socket was closed by peer")

            now = time.time()
            if query and (not timeout_at or timeout_at > now):
                if timeout_at is None:
                    # Try until timeout reached in case there was a timeout configured.
                    # Otherwise only retry once.
                    timeout_at = now
                    if self.timeout:
                        timeout_at += self.timeout

                time.sleep(0.1)
                self.connect()
                self.send_query(query, add_headers)
                return self.recv_response(
                    query, add_headers,
                    timeout_at)  # do not send query again -> danger of infinite loop
<<<<<<< HEAD
            else:
                raise MKLivestatusSocketError(str(e))
=======
            raise MKLivestatusSocketError(str(e))
>>>>>>> upstream/master

        except MKLivestatusTableNotFoundError:
            raise

        except Exception as e:
            # Catches
            # MKLivestatusQueryError
            # MKLivestatusSocketError
            # FIXME: ? self.disconnect()
            raise MKLivestatusSocketError("Unhandled exception: %s" % e)

    def set_prepend_site(self, p: bool) -> None:
        self.prepend_site = p

<<<<<<< HEAD
    def set_only_sites(self, sites=None):
        pass

    def set_limit(self, limit=None):
        self.limit = limit

    def query(self, query, add_headers=""):
        if self.limit is not None:
            query += "Limit: %d\n" % self.limit
        data = self.do_query(query, add_headers)
        if self.prepend_site:
            return [[''] + line for line in data]
        return data

    def command(self, command, site=None):
        self.do_command(command)

    def do_command(self, command):
        if self.socket is None:
            self.connect()
        if not command.endswith("\n"):
            command += "\n"
        try:
            self.socket.send("COMMAND " + command + "\n")
=======
    def set_only_sites(self, sites: Optional[List[SiteId]] = None) -> None:
        pass

    def set_limit(self, limit: Optional[int] = None) -> None:
        self.limit = limit

    def query(self,
              query: 'QueryTypes',
              add_headers: Union[str, bytes] = u"") -> LivestatusResponse:

        # Normalize argument types
        normalized_add_headers = _ensure_unicode(add_headers)
        normalized_query = Query(query) if not isinstance(query, Query) else query

        if self.limit is not None:
            normalized_query = Query(u"%sLimit: %d\n" % (normalized_query, self.limit),
                                     normalized_query.suppress_exceptions)

        response = self.do_query(normalized_query, normalized_add_headers)
        if self.prepend_site:
            for row in response:
                row.insert(0, b"")
        return response

    # TODO: Cleanup all call sites to hand over str types
    def command(self, command: AnyStr, site: Optional[SiteId] = None) -> None:
        self.do_command(command)

    def do_command(self, command: AnyStr) -> None:
        cmd = _ensure_unicode(command)

        if self.socket is None:
            self.connect()
        assert self.socket is not None  # TODO: refactor to avoid assert

        if not cmd.endswith(u"\n"):
            cmd += u"\n"

        try:
            self.socket.send(("COMMAND %s\n" % cmd).encode("utf-8"))
>>>>>>> upstream/master
        except IOError as e:
            self.socket = None
            if self.persist:
                del persistent_connections[self.socketurl]
            raise MKLivestatusSocketError(str(e))

    # Set user to be used in certain authorization domain
    def set_auth_user(self, domain: str, user: UserId) -> None:
        if user:
            self.auth_users[domain] = user
        elif domain in self.auth_users:
            del self.auth_users[domain]

    # Switch future request to new authorization domain
    def set_auth_domain(self, domain: str) -> None:
        auth_user = self.auth_users.get(domain)
        if auth_user:
            self.auth_header = "AuthUser: %s\n" % auth_user
        else:
            self.auth_header = u""


#.
#   .--MultiSiteConn-------------------------------------------------------.
#   |     __  __       _ _   _ ____  _ _        ____                       |
#   |    |  \/  |_   _| | |_(_) ___|(_) |_ ___ / ___|___  _ __  _ __       |
#   |    | |\/| | | | | | __| \___ \| | __/ _ \ |   / _ \| '_ \| '_ \      |
#   |    | |  | | |_| | | |_| |___) | | ||  __/ |__| (_) | | | | | | |     |
#   |    |_|  |_|\__,_|_|\__|_|____/|_|\__\___|\____\___/|_| |_|_| |_|     |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Connections to a list of local and remote sites.                    |
#   '----------------------------------------------------------------------'

#.
#   .--MultiSiteConn-------------------------------------------------------.
#   |     __  __       _ _   _ ____  _ _        ____                       |
#   |    |  \/  |_   _| | |_(_) ___|(_) |_ ___ / ___|___  _ __  _ __       |
#   |    | |\/| | | | | | __| \___ \| | __/ _ \ |   / _ \| '_ \| '_ \      |
#   |    | |  | | |_| | | |_| |___) | | ||  __/ |__| (_) | | | | | | |     |
#   |    |_|  |_|\__,_|_|\__|_|____/|_|\__\___|\____\___/|_| |_|_| |_|     |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Connections to a list of local and remote sites.                    |
#   '----------------------------------------------------------------------'

# sites is a dictionary from site name to a dict.
# Keys in the dictionary:
# socket:   socketurl (obligatory)
# timeout:  timeout for tcp/unix in seconds

# TODO: Move the connect/disconnect stuff to separate methods. Then make
# it possible to connect/disconnect duing existance of a single object.


class MultiSiteConnection(Helpers):
<<<<<<< HEAD
    def __init__(self, sites, disabled_sites=None):
=======
    def __init__(self,
                 sites: SiteConfigurations,
                 disabled_sites: Optional[SiteConfigurations] = None) -> None:
>>>>>>> upstream/master
        if disabled_sites is None:
            disabled_sites = {}

        self.sites = sites
        self.connections: List[Tuple[SiteId, SiteConfiguration, SingleSiteConnection]] = []
        self.deadsites: Dict[SiteId, DeadSite] = {}
        self.prepend_site = False
        self.only_sites: OnlySites = None
        self.limit: Optional[int] = None
        self.parallelize = True

        # Status host: A status host helps to prevent trying to connect
        # to a remote site which is unreachable. This is done by looking
        # at the current state of a certain host on a local site that is
        # representing the connection to the remote site. The status host
        # is specified as an optional pair of (site, host) in the entry
        # "status_host". We first connect to all sites without a status_host
        # entry, then retrieve the host states of the status hosts and then
        # connect to the remote site which are reachable

        # Tackle very special problem: If the user disables a site which
        # provides status_host information for other sites, the dead-detection
        # would not work. For that cases we make a temporary connection just
        # to fetch the status information
        extra_status_sites = {}
        if len(disabled_sites) > 0:
            status_sitenames = set()
            for sitename, site in sites.items():
                try:
                    s, h = site.get("status_host", [])
                except ValueError:
                    continue
<<<<<<< HEAD

                status_sitenames.add(s)

            for sitename in status_sitenames:
                site = disabled_sites.get(sitename)
                if site:
                    extra_status_sites[sitename] = site

        # First connect to sites without status host. Collect status
        # hosts at the same time.

        status_hosts = {}  # dict from site to list of status_hosts
=======

                status_sitenames.add(s)

            for sitename in status_sitenames:
                status_site = disabled_sites.get(sitename)
                if status_site:
                    extra_status_sites[sitename] = status_site

        # First connect to sites without status host. Collect status
        # hosts at the same time.

        # dict from site to list of status_hosts
        status_hosts: Dict[SiteId, List[bytes]] = {}
>>>>>>> upstream/master
        sites_dict = sites.copy()
        sites_dict.update(extra_status_sites)
        for sitename, site in sites_dict.items():
            status_host = site.get("status_host")
            if status_host:
                if not isinstance(status_host, tuple) or len(status_host) != 2:
                    raise MKLivestatusConfigError(
                        "Status host of site %s is %r, but must be pair of site and host" %
                        (sitename, status_host))
                s, h = status_host
                status_hosts[s] = status_hosts.get(s, []) + [h]
            else:
                try:
                    connection = self.connect_to_site(sitename, site)
                    self.connections.append((sitename, site, connection))
                except Exception as e:
                    self.deadsites[sitename] = {
                        "exception": e,
                        "site": site,
                    }

        # Now learn current states of status hosts and store it in a dictionary
        # from (local_site, host) => state
        status_host_states = {}
        for sitename, hosts in status_hosts.items():
            # Fetch all the states of status hosts of this local site in one query
            query = u"GET hosts\nColumns: name state has_been_checked last_time_up\n"
            for host in hosts:
<<<<<<< HEAD
                query += "Filter: name = %s\n" % host
            query += "Or: %d\n" % len(hosts)
=======
                query += u"Filter: name = %s\n" % str(host)
            query += u"Or: %d\n" % len(hosts)
>>>>>>> upstream/master
            self.set_only_sites([sitename])  # only connect one site
            try:
                result = self.query_table(query)
                # raise MKLivestatusConfigError("TRESulT: %s" % (result,))
                for host, state, has_been_checked, lastup in result:
                    if has_been_checked == 0:
                        state = 3
                    status_host_states[(sitename, host)] = (state, lastup)
            except Exception as e:
                raise MKLivestatusConfigError(e)
        self.set_only_sites()  # clear site filter

        # Disconnect from disabled sites that we connected to only to
        # get status information from
        for sitename, site in extra_status_sites.items():
            self._disconnect_site(sitename)

        # Now loop over all sites having a status_host and take that state
        # of that into consideration
        for sitename, site in sites.items():
            status_host = site.get("status_host")
            if status_host:
                now = time.time()
                shs, lastup = status_host_states.get(status_host,
                                                     (4, now))  # None => Status host not existing
                if shs == 0 or shs is None:
                    try:
                        connection = self.connect_to_site(sitename, site)
                        self.connections.append((sitename, site, connection))
                    except Exception as e:
                        self.deadsites[sitename] = {
                            "exception": e,
                            "site": site,
                        }
                else:
                    if shs == 1:
                        ex = "The remote monitoring host is down"
                    elif shs == 2:
                        ex = "The remote monitoring host is unreachable"
                    elif shs == 3:
                        ex = "The remote monitoring host's state it not yet determined"
                    elif shs == 4:
                        ex = "Invalid status host: site %s has no host %s" % (status_host[0],
                                                                              status_host[1])
                    else:
                        ex = "Error determining state of remote monitoring host: %s" % shs
                    self.deadsites[sitename] = {
                        "site": site,
                        "status_host_state": shs,
                        "exception": ex,
                    }

<<<<<<< HEAD
    def connect_to_site(self, sitename, site, temporary=False):
=======
    def connect_to_site(self,
                        sitename: SiteId,
                        site: SiteConfiguration,
                        temporary: bool = False) -> SingleSiteConnection:
>>>>>>> upstream/master
        """Helper function for connecting to a site"""
        url = site["socket"]
        persist = not temporary and site.get("persist", False)
        tls_type, tls_params = site.get("tls", ("plain_text", {}))

        connection = SingleSiteConnection(
            socketurl=url,
            persist=persist,
            allow_cache=site.get("cache", False),
            tls=tls_type != "plain_text",
            verify=tls_params.get("verify", True),
            ca_file_path=tls_params.get("ca_file_path", None),
        )

        if "timeout" in site:
            connection.set_timeout(int(site["timeout"]))
        connection.connect()
        return connection

    # Needed for temporary connection for status_hosts in disabled sites
<<<<<<< HEAD
    def _disconnect_site(self, sitename):
=======
    def _disconnect_site(self, sitename: SiteId) -> None:
>>>>>>> upstream/master
        i = 0
        for name, _site, _connection in self.connections:
            if name == sitename:
                del self.connections[i]
                return
            i += 1

<<<<<<< HEAD
    def add_header(self, header):
=======
    def add_header(self, header: str) -> None:
>>>>>>> upstream/master
        for _sitename, _site, connection in self.connections:
            connection.add_header(header)

    def set_prepend_site(self, p: bool) -> None:
        self.prepend_site = p

<<<<<<< HEAD
    def set_only_sites(self, sites=None):
=======
    def set_only_sites(self, sites: OnlySites = None) -> None:
>>>>>>> upstream/master
        """Make future queries only contact the given sites.

        Provide a list of site IDs to not contact all configured sites, but only the listed
        site IDs. In case None is given, the limitation is removed.
        """
        self.only_sites = sites

    # Impose Limit on number of returned datasets (distributed amoung sites)
<<<<<<< HEAD
    def set_limit(self, limit=None):
=======
    def set_limit(self, limit: Optional[int] = None) -> None:
>>>>>>> upstream/master
        self.limit = limit

    def dead_sites(self) -> Dict[SiteId, DeadSite]:
        return self.deadsites

<<<<<<< HEAD
    def alive_sites(self):
        return [s[0] for s in self.connections]

    def successfully_persisted(self):
=======
    def alive_sites(self) -> List[SiteId]:
        return [s[0] for s in self.connections]

    def successfully_persisted(self) -> bool:
>>>>>>> upstream/master
        for _sitename, _site, connection in self.connections:
            if connection.successfully_persisted():
                return True
        return False

<<<<<<< HEAD
    def set_auth_user(self, domain, user):
        for _sitename, _site, connection in self.connections:
            connection.set_auth_user(domain, user)

    def set_auth_domain(self, domain):
        for _sitename, _site, connection in self.connections:
            connection.set_auth_domain(domain)

    def query(self, query, add_headers=""):
        if self.parallelize:
            return self.query_parallel(query, add_headers)
        return self.query_non_parallel(query, add_headers)

    def query_non_parallel(self, query, add_headers=""):
        result = []
=======
    def set_auth_user(self, domain: str, user: UserId) -> None:
        for _sitename, _site, connection in self.connections:
            connection.set_auth_user(domain, user)

    def set_auth_domain(self, domain: str) -> None:
        for _sitename, _site, connection in self.connections:
            connection.set_auth_domain(domain)

    def query(self,
              query: 'QueryTypes',
              add_headers: Union[str, bytes] = u"") -> LivestatusResponse:

        # Normalize argument types
        normalized_add_headers = _ensure_unicode(add_headers)
        normalized_query = Query(query) if not isinstance(query, Query) else query

        if self.parallelize:
            return self.query_parallel(normalized_query, normalized_add_headers)
        return self.query_non_parallel(normalized_query, normalized_add_headers)

    def query_non_parallel(self, query: Query, add_headers: str = u"") -> LivestatusResponse:
        result = LivestatusResponse([])
>>>>>>> upstream/master
        stillalive = []
        limit = self.limit
        for sitename, site, connection in self.connections:
            if self.only_sites is not None and sitename not in self.only_sites:
                stillalive.append((sitename, site, connection))  # state unknown, assume still alive
                continue
            try:
                if limit is not None:
                    limit_header = "Limit: %d\n" % limit
                else:
                    limit_header = ""
                r = connection.query(query, add_headers + limit_header)
                if self.prepend_site:
<<<<<<< HEAD
                    r = [[sitename] + l for l in r]
=======
                    for row in r:
                        row.insert(0, sitename)
>>>>>>> upstream/master
                if limit is not None:
                    limit -= len(r)  # Account for portion of limit used by this site
                result += r
                stillalive.append((sitename, site, connection))
            except Exception as e:
                connection.disconnect()
                self.deadsites[sitename] = {
                    "exception": e,
                    "site": site,
                }
        self.connections = stillalive
        return result

    # New parallelized version of query(). The semantics differs in the handling
    # of Limit: since all sites are queried in parallel, the Limit: is simply
    # applied to all sites - resulting in possibly more results then Limit requests.
<<<<<<< HEAD
    def query_parallel(self, query, add_headers=""):
=======
    def query_parallel(self, query: Query, add_headers: str = u"") -> LivestatusResponse:
>>>>>>> upstream/master
        stillalive = []
        if self.only_sites is not None:
            connect_to_sites = [c for c in self.connections if c[0] in self.only_sites]
            # Unused sites are assumed to be alive
            stillalive.extend([c for c in self.connections if c[0] not in self.only_sites])
        else:
            connect_to_sites = self.connections

        limit = self.limit
        if limit is not None:
<<<<<<< HEAD
            limit_header = "Limit: %d\n" % limit
=======
            limit_header = u"Limit: %d\n" % limit
>>>>>>> upstream/master
        else:
            limit_header = u""

        # First send all queries
        for sitename, site, connection in connect_to_sites:
            try:
                connection.send_query(query, add_headers + limit_header)
            except Exception as e:
                self.deadsites[sitename] = {
                    "exception": e,
                    "site": site,
                }

<<<<<<< HEAD
        if isinstance(query, Query):
            suppress_exceptions = tuple(query.suppress_exceptions)
        else:
            suppress_exceptions = tuple(Query.default_suppressed_exceptions)

        # Then retrieve all answers. We will be as slow as the slowest of all
        # connections.
        result = []
=======
        suppress_exceptions = tuple(query.suppress_exceptions)

        # Then retrieve all answers. We will be as slow as the slowest of all
        # connections.
        result = LivestatusResponse([])
>>>>>>> upstream/master
        for sitename, site, connection in connect_to_sites:
            try:
                r = connection.recv_response(query, add_headers + limit_header)
                stillalive.append((sitename, site, connection))
                if self.prepend_site:
<<<<<<< HEAD
                    r = [[sitename] + l for l in r]
=======
                    for row in r:
                        row.insert(0, sitename)
>>>>>>> upstream/master
                result += r
            except suppress_exceptions:  # pylint: disable=catching-non-exception
                stillalive.append((sitename, site, connection))
                continue

            except Exception as e:
                connection.disconnect()
                self.deadsites[sitename] = {
                    "exception": e,
                    "site": site,
                }

        self.connections = stillalive
        return result

<<<<<<< HEAD
    def command(self, command, sitename="local"):
=======
    # TODO: Is this SiteId(...) the way to go? Without this mypy complains about incompatible bytes
    # vs. Optional[SiteId]
    def command(self, command: AnyStr, sitename: Optional[SiteId] = SiteId("local")) -> None:
>>>>>>> upstream/master
        if sitename in self.deadsites:
            raise MKLivestatusSocketError("Connection to site %s is dead: %s" %
                                          (sitename, self.deadsites[sitename]["exception"]))
        conn = [t[2] for t in self.connections if t[0] == sitename]
        if len(conn) == 0:
            raise MKLivestatusConfigError("Cannot send command to unconfigured site '%s'" %
                                          sitename)
        conn[0].do_command(command)

    # Return connection to localhost (UNIX), if available
<<<<<<< HEAD
    def local_connection(self):
=======
    def local_connection(self) -> SingleSiteConnection:
>>>>>>> upstream/master
        for _sitename, site, connection in self.connections:
            if site["socket"].startswith("unix:") and "liveproxy" not in site["socket"]:
                return connection
        raise MKLivestatusConfigError("No livestatus connection to local host")

<<<<<<< HEAD
    def get_connection(self, site_id):
        # type: (str) -> SingleSiteConnection
=======
    def get_connection(self, site_id: SiteId) -> SingleSiteConnection:
>>>>>>> upstream/master
        for this_site_id, _site, connection in self.connections:
            if this_site_id == site_id:
                return connection
        raise KeyError("Connection does not exist")


#.
#   .--LocalConn-----------------------------------------------------------.
#   |            _                    _  ____                              |
#   |           | |    ___   ___ __ _| |/ ___|___  _ __  _ __              |
#   |           | |   / _ \ / __/ _` | | |   / _ \| '_ \| '_ \             |
#   |           | |__| (_) | (_| (_| | | |__| (_) | | | | | | |            |
#   |           |_____\___/ \___\__,_|_|\____\___/|_| |_|_| |_|            |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  LocalConnection is a convenciance class for connecting to the       |
#   |  local Livestatus socket within an OMD site. It only works within    |
#   |  OMD context.                                                        |
#   '----------------------------------------------------------------------'


class LocalConnection(SingleSiteConnection):
<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
=======
    def __init__(self, *args: Any, **kwargs: Any) -> None:
>>>>>>> upstream/master
        omd_root = os.getenv("OMD_ROOT")
        if not omd_root:
            raise MKLivestatusConfigError(
                "OMD_ROOT is not set. You are not running in OMD context.")
        SingleSiteConnection.__init__(self, "unix:" + omd_root + "/tmp/run/live", *args, **kwargs)
