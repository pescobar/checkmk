<<<<<<< HEAD
# Following import is used to trigger plugin loading
import cmk.gui.wato  # pylint: disable=unused-import
import cmk.gui.plugins.wato.utils.main_menu as main_menu


def test_registered_modules():
    module_names = [m.mode_or_url for m in main_menu.get_modules()]
    assert module_names == [
        'agents',
        'folder',
        'tags',
        'globalvars',
        'ruleeditor',
        'static_checks',
        'check_plugins',
        'host_groups',
        'users',
        'roles',
        'contact_groups',
        'notifications',
        'timeperiods',
        'mkeventd_rule_packs',
        'bi_packs',
        'sites',
        'backup',
        'passwords',
        'alert_handlers',
        'analyze_config',
        'background_jobs_overview',
        'mkps',
        'pattern_editor',
        'icons',
    ]


def test_register_module(monkeypatch):
    monkeypatch.setattr(main_menu, "main_module_registry", main_menu.ModuleRegistry())
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest

from cmk.gui.watolib.main_menu import ModuleRegistry
import cmk.gui.plugins.wato.utils.main_menu as main_menu

pytestmark = pytest.mark.usefixtures("load_plugins")


def test_register_modules(monkeypatch):
    monkeypatch.setattr(main_menu, "main_module_registry", ModuleRegistry())
>>>>>>> upstream/master
    module = main_menu.WatoModule(
        mode_or_url="dang",
        description='descr',
        permission='icons',
        title='Custom DING',
        sort_index=100,
        icon='icons',
    )
    main_menu.register_modules(module)

    modules = main_menu.get_modules()
    assert len(modules) == 1
    registered = modules[0]
<<<<<<< HEAD
    assert isinstance(registered, main_menu.MainModule)
=======
    assert isinstance(registered, main_menu.ABCMainModule)
>>>>>>> upstream/master
    assert registered.mode_or_url == "dang"
    assert registered.description == 'descr'
    assert registered.permission == 'icons'
    assert registered.title == 'Custom DING'
    assert registered.sort_index == 100
    assert registered.icon == 'icons'
<<<<<<< HEAD
=======
    assert registered.is_show_more is False
    assert registered.topic == main_menu.MainModuleTopicCustom
>>>>>>> upstream/master
