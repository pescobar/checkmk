<<<<<<< HEAD
#!/usr/bin/env python
# encoding: utf-8

import pytest
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

>>>>>>> upstream/master
from testlib import CMKWebSession


def test_01_login_and_logout(site):
    web = CMKWebSession(site)

<<<<<<< HEAD
    r = web.get("wato.py", allow_redirect_to_login=True)
    assert "Global Settings" not in r.text

    web.login()
    web.set_language("en")
    r = web.get("wato.py")
    assert "Global Settings" in r.text

    web.logout()
    r = web.get("wato.py", allow_redirect_to_login=True)
    assert "Global Settings" not in r.text
=======
    r = web.get("wato.py?mode=globalvars", allow_redirect_to_login=True)
    assert "Global settings" not in r.text

    web.login()
    web.set_language("en")
    r = web.get("wato.py?mode=globalvars")
    assert "Global settings" in r.text

    web.logout()
    r = web.get("wato.py?mode=globalvars", allow_redirect_to_login=True)
    assert "Global settings" not in r.text
>>>>>>> upstream/master
