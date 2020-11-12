<<<<<<< HEAD
#!/usr/bin/env python
# encoding: utf-8

import pytest

from cmk.gui.exceptions import MKUserError
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]

>>>>>>> upstream/master
from cmk.gui.globals import html
import cmk.gui.main
import cmk.gui.config


def test_get_start_url_default(register_builtin_html):
    assert cmk.gui.main._get_start_url() == "dashboard.py"


def test_get_start_url_default_config(monkeypatch, register_builtin_html):
    monkeypatch.setattr(cmk.gui.config, "start_url", "bla.py")
    assert cmk.gui.main._get_start_url() == "bla.py"


<<<<<<< HEAD
def test_get_start_url_user_config(monkeypatch, register_builtin_html):
    monkeypatch.setattr(cmk.gui.config, "start_url", "bla.py")

    monkeypatch.setattr(cmk.gui.config.user, "attributes", {
=======
def test_get_start_url_user_config(monkeypatch, module_wide_request_context):
    monkeypatch.setattr(cmk.gui.config, "start_url", "bla.py")

    monkeypatch.setattr(cmk.gui.config.user, "_attributes", {
>>>>>>> upstream/master
        "start_url": "user_url.py",
    })

    assert cmk.gui.main._get_start_url() == "user_url.py"


def test_get_start_url(register_builtin_html):
    start_url = "dashboard.py?name=mein_dashboard"
    html.request.set_var("start_url", start_url)

    assert cmk.gui.main._get_start_url() == start_url


@pytest.mark.parametrize("invalid_url", [
    "http://localhost/",
    "://localhost",
    "javascript:alert(1)",
    "javAscRiPt:alert(1)",
    "localhost:80/bla",
])
<<<<<<< HEAD
def test_get_start_url_invalid(register_builtin_html, invalid_url):
=======
def test_get_start_url_invalid(module_wide_request_context, invalid_url):
>>>>>>> upstream/master
    html.request.set_var("start_url", invalid_url)

    assert cmk.gui.main._get_start_url() == "dashboard.py"


<<<<<<< HEAD
def test_get_start_url_invalid_config(monkeypatch, register_builtin_html):
    monkeypatch.setattr(cmk.gui.config.user, "attributes", {
=======
def test_get_start_url_invalid_config(monkeypatch, module_wide_request_context):
    monkeypatch.setattr(cmk.gui.config.user, "_attributes", {
>>>>>>> upstream/master
        "start_url": "http://asdasd/",
    })
    assert cmk.gui.main._get_start_url() == "dashboard.py"
