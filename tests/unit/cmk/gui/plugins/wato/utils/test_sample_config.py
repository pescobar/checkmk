<<<<<<< HEAD
# Following import is used to trigger plugin loading
import cmk.gui.wato  # pylint: disable=unused-import
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import cmk.utils.version as cmk_version
# Following import is used to trigger plugin loading
import cmk.gui.wato  # noqa: F401 # pylint: disable=unused-import
>>>>>>> upstream/master
import cmk.gui.plugins.wato.utils as utils


def test_registered_generators():
<<<<<<< HEAD
    assert sorted(utils.sample_config_generator_registry.keys()) == sorted([
        'acknowledge_initial_werks',
        'basic_wato_config',
        'cee_agent_bakery',
        'cee_basic_config',
        'create_automation_user',
        'ec_sample_rule_pack',
    ])


def test_get_sorted_generators():
    assert [g.ident() for g in utils.sample_config_generator_registry.get_generators()] == [
        'basic_wato_config',
        'cee_basic_config',
        'cee_agent_bakery',
        'acknowledge_initial_werks',
        'ec_sample_rule_pack',
        'create_automation_user',
    ]
=======
    expected_generators = [
        'acknowledge_initial_werks',
        'basic_wato_config',
        'create_automation_user',
        'ec_sample_rule_pack',
        'search_index',
    ]

    if not cmk_version.is_raw_edition():
        expected_generators += [
            'cee_agent_bakery',
            'cee_basic_config',
        ]

    assert sorted(utils.sample_config_generator_registry.keys()) == sorted(expected_generators)


def test_get_sorted_generators():
    expected = [
        'basic_wato_config',
    ]

    if not cmk_version.is_raw_edition():
        expected += [
            'cee_basic_config',
            'cee_agent_bakery',
        ]

    expected += [
        'acknowledge_initial_werks',
        'ec_sample_rule_pack',
        'create_automation_user',
        'search_index',
    ]

    assert [g.ident() for g in utils.sample_config_generator_registry.get_generators()] == expected
>>>>>>> upstream/master
