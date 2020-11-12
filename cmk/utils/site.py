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

import os


def get_omd_config(key):
    for l in open(os.environ["OMD_ROOT"] + "/etc/omd/site.conf"):
        if l.startswith(key + "="):
            return l.split("=")[-1].strip("'\n")
    return None


def get_apache_port():
    port = get_omd_config("CONFIG_APACHE_TCP_PORT")
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from pathlib import Path
from typing import Dict, Optional

import cmk.utils.paths

OMDConfig = Dict[str, str]


def get_omd_config(omd_root: Optional[Path] = None) -> OMDConfig:
    if omd_root is None:
        omd_root = Path(cmk.utils.paths.omd_root)

    site_conf = omd_root / "etc" / "omd" / "site.conf"

    omd_config: OMDConfig = {}
    with site_conf.open(encoding="utf-8") as f:
        for line in f:
            key, value = line.split("=")
            omd_config[key.strip()] = value.strip("'\n")
    return omd_config


def get_apache_port(omd_root: Optional[Path] = None) -> int:
    port = get_omd_config(omd_root).get("CONFIG_APACHE_TCP_PORT")
>>>>>>> upstream/master
    if port is None:
        return 80
    return int(port)
