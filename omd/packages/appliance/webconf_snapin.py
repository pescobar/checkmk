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
# | Copyright Mathias Kettner 2013             mk@mathias-kettner.de |
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
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.plugins.sidebar import (
    SidebarSnapin,
    snapin_registry,
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import ast
import subprocess

import cmk.utils.version as cmk_version

# Does not detect the module hierarchy correctly. Imports are fine.
from cmk.gui.i18n import _  # pylint: disable=cmk-module-layer-violation
from cmk.gui.globals import html  # pylint: disable=cmk-module-layer-violation
from cmk.gui.plugins.sidebar import (  # pylint: disable=cmk-module-layer-violation
    SidebarSnapin, snapin_registry,
>>>>>>> upstream/master
)


@snapin_registry.register
class SidebarSnapinCMAWebconf(SidebarSnapin):
    @staticmethod
    def type_name():
        return "webconf"

    @classmethod
    def title(cls):
<<<<<<< HEAD
        return _("Check_MK Appliance")

    @classmethod
    def description(cls):
        return _("Access to the Check_MK Appliance Web Configuration")
=======
        return _("Checkmk Appliance")

    @classmethod
    def description(cls):
        return _("Access to the Checkmk Appliance Web Configuration")
>>>>>>> upstream/master

    @classmethod
    def allowed_roles(cls):
        return ["admin"]

    def show(self):
<<<<<<< HEAD

        import imp
        try:
            cma_nav = imp.load_source("cma_nav", "/usr/lib/python2.7/cma_nav.py")
        except IOError:
            html.show_error(_("Unable to import cma_nav module"))
            return

=======
        if not cmk_version.is_cma():
            return

        # The cma_nav-Module is a Python 2.7 module that is already installed by the CMA OS.  For
        # the future we should change this to some structured file format, but for the moment we
        # have to deal with existing firmwares. Use some py27 wrapper to produce the needed output.
        p = subprocess.Popen(["/usr/bin/python2.7"],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             encoding="utf-8",
                             shell=False,
                             close_fds=True)
        stdout, stderr = p.communicate("\n".join([
            'import imp',
            'cma_nav = imp.load_source("cma_nav", "/usr/lib/python2.7/cma_nav.py")',
            'print(cma_nav.modules())',
        ]))

        if stderr:
            html.show_error(_("Failed to render navigation: %s") % stderr)
            return

        nav_modules = ast.literal_eval(stdout)

>>>>>>> upstream/master
        base_url = "/webconf/"

        self._iconlink(_("Main Menu"), base_url, "home")

<<<<<<< HEAD
        for url, icon, title, _descr in cma_nav.modules():
=======
        for url, icon, title, _descr in nav_modules:
>>>>>>> upstream/master
            url = base_url + url
            self._iconlink(title, url, icon)

    # Our version of iconlink -> the images are located elsewhere
    def _iconlink(self, text, url, icon):
        html.open_a(class_=["iconlink", "link"], target="main", href=url)
<<<<<<< HEAD
        html.icon(icon="/webconf/images/icon_%s.png" % icon, title=None, cssclass="inline")
=======
        html.icon("/webconf/images/icon_%s.png" % icon, cssclass="inline")
>>>>>>> upstream/master
        html.write(text)
        html.close_a()
        html.br()
