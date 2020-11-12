<<<<<<< HEAD
import pytest
import os

import cmk


def test_version():
    assert isinstance(cmk.__version__, str)


def test_is_enterprise_edition(monkeypatch):
    monkeypatch.setattr(cmk, "omd_version", lambda: "1.4.0i1.cre")
    assert cmk.is_enterprise_edition() == False
    monkeypatch.setattr(cmk, "omd_version", lambda: "1.4.0i1.cee")
    assert cmk.is_enterprise_edition() == True
    monkeypatch.setattr(cmk, "omd_version", lambda: "2016.09.22.cee")
    assert cmk.is_enterprise_edition() == True
    monkeypatch.setattr(cmk, "omd_version", lambda: "2016.09.22.cee.demo")
    assert cmk.is_enterprise_edition() == True


def test_is_raw_edition(monkeypatch):
    monkeypatch.setattr(cmk, "omd_version", lambda: "1.4.0i1.cre")
    assert cmk.is_raw_edition() == True
    monkeypatch.setattr(cmk, "omd_version", lambda: "1.4.0i1.cee")
    assert cmk.is_raw_edition() == False
    monkeypatch.setattr(cmk, "omd_version", lambda: "2016.09.22.cee")
    assert cmk.is_raw_edition() == False
    monkeypatch.setattr(cmk, "omd_version", lambda: "2016.09.22.cee.demo")
    assert cmk.is_raw_edition() == False


def test_is_demo(monkeypatch):
    monkeypatch.setattr(cmk, "omd_version", lambda: "1.4.0i1.cre")
    assert cmk.is_demo() == False
    monkeypatch.setattr(cmk, "omd_version", lambda: "1.4.0i1.cee")
    assert cmk.is_demo() == False
    monkeypatch.setattr(cmk, "omd_version", lambda: "2016.09.22.cee")
    assert cmk.is_demo() == False
    monkeypatch.setattr(cmk, "omd_version", lambda: "2016.09.22.cee.demo")
    assert cmk.is_demo() == True
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import cmk.utils.version as cmk_version


def test_version():
    assert isinstance(cmk_version.__version__, str)


def test_is_enterprise_edition(monkeypatch):
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "1.4.0i1.cre")
    assert cmk_version.is_enterprise_edition() is False
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "1.4.0i1.cee")
    assert cmk_version.is_enterprise_edition() is True
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "2016.09.22.cee")
    assert cmk_version.is_enterprise_edition() is True
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "2016.09.22.cee.demo")
    assert cmk_version.is_enterprise_edition() is True


def test_is_raw_edition(monkeypatch):
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "1.4.0i1.cre")
    assert cmk_version.is_raw_edition() is True
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "1.4.0i1.cee")
    assert cmk_version.is_raw_edition() is False
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "2016.09.22.cee")
    assert cmk_version.is_raw_edition() is False
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "2016.09.22.cee.demo")
    assert cmk_version.is_raw_edition() is False


def test_is_demo(monkeypatch):
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "1.4.0i1.cre")
    assert cmk_version.is_demo() is False
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "1.4.0i1.cee")
    assert cmk_version.is_demo() is False
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "2016.09.22.cee")
    assert cmk_version.is_demo() is False
    monkeypatch.setattr(cmk_version, "omd_version", lambda: "2016.09.22.cee.demo")
    assert cmk_version.is_demo() is True
>>>>>>> upstream/master
