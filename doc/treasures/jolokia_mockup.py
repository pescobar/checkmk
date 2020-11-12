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
# | Copyright Mathias Kettner 2015             mk@mathias-kettner.de |
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

# small mock server simulating a jolokia server. Not very sophisticated
# but enough to get several checks to display something

<<<<<<< HEAD
from __future__ import print_function
import SocketServer
import SimpleHTTPServer
import urlparse
=======
import socketserver
import http.server
from urllib.parse import urlparse
>>>>>>> upstream/master

PORT = 8080


<<<<<<< HEAD
class FakeHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsedParams = urlparse.urlparse(self.path)
=======
class FakeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsedParams = urlparse(self.path)
>>>>>>> upstream/master
        params = [par for par in parsedParams.path.split('/') if par]

        print(params)

        self.send_response(200)
        self.send_header('Content-Type', 'application/xml')
        self.end_headers()

        if len(params) > 1:
            self.wfile.write(b'{"value": 1}')
        else:
            self.wfile.write(
                b'{"value": {"info": {"version": "1.0", "product": "Fake_Product"}, "agent": "Fake_Agent"}}'
            )

        self.wfile.close()
<<<<<<< HEAD

=======
>>>>>>> upstream/master


class FakeTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


httpd = FakeTCPServer(("", 8080), FakeHandler)
httpd.serve_forever()
