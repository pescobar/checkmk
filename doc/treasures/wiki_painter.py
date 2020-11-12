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

import cmk.utils.paths


def paint_wiki_notes(row):
    host = row["host_name"]
    svc = row.get("service_description")
    svc = svc.replace(':', '')
    svc = svc.replace('/', '')
    svc = svc.replace('\\', '')
    svc = svc.replace(' ', '_')
    svc = svc.lower()
    host = host.lower()
    filename = cmk.utils.paths.omd_root + '/var/dokuwiki/data/pages/docu/%s/%s.txt' % (host, svc)
    if not os.path.isfile(filename):
        filename = cmk.utils.paths.omd_root + '/var/dokuwiki/data/pages/docu/default/%s.txt' % (
            svc,)

    text = u"<a href='../wiki/doku.php?id=docu:default:%s'>Edit Default Instructions</a> - " % svc
    text += u"<a href='../wiki/doku.php?id=docu:%s:%s'>Edit Host Instructions</a> <hr> " % (host,
                                                                                            svc)

    try:
<<<<<<< HEAD
        from pathlib2 import Path
=======
        from pathlib import Path
>>>>>>> upstream/master
        with Path(filename).open(encoding="utf-8") as fp:
            text += fp.read()
    except IOError:
        text += "No instructions found in " + filename

    return "", text + "<br /><br />"


multisite_painters["svc_wiki_notes"] = {
    "title": _("Instructions"),
    "short": _("Instr"),
    "columns": ["host_name", "service_description"],
    "paint": paint_wiki_notes,
}
