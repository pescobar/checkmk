<<<<<<< HEAD
#!/usr/bin/env python
# encoding: utf-8

import os
import stat
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import os
>>>>>>> upstream/master


def test_basic_commands(site):
    commands = [
        "bin/mkp",
        "bin/check_mk",
        "bin/cmk",
        "bin/omd",
        "bin/stunnel",
        "bin/cmk-update-config",
    ]

<<<<<<< HEAD
=======
    if site.version.edition() == "enterprise":
        commands.append("bin/fetcher")

>>>>>>> upstream/master
    for rel_path in commands:
        path = os.path.join(site.root, rel_path)
        assert os.path.exists(path)
