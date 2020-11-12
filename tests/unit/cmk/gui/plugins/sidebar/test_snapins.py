<<<<<<< HEAD
# Needed to trigger plugin loading
import cmk.gui.sidebar  # pylint: disable=unused-import

from cmk.gui.plugins.sidebar.utils import snapin_registry


def test_registered_snapins():
    assert sorted(snapin_registry.keys()) == sorted([
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]

import cmk.utils.version as cmk_version

from cmk.gui.plugins.sidebar.utils import snapin_registry

pytestmark = pytest.mark.usefixtures("load_plugins")


def test_registered_snapins():
    expected_snapins = [
>>>>>>> upstream/master
        'about',
        'admin',
        'admin_mini',
        'biaggr_groups',
        'biaggr_groups_tree',
        'bookmarks',
<<<<<<< HEAD
        'cmc_stats',
=======
>>>>>>> upstream/master
        'custom_links',
        'dashboards',
        'hostgroups',
        'hostmatrix',
        'hosts',
        'master_control',
        'mkeventd_performance',
        'nagios_legacy',
        'nagvis_maps',
        'performance',
        'problem_hosts',
<<<<<<< HEAD
        'reports',
=======
>>>>>>> upstream/master
        'search',
        'servicegroups',
        'sitestatus',
        'speedometer',
        'tactical_overview',
        'tag_tree',
        'time',
        'views',
        'wato_folders',
        'wato_foldertree',
<<<<<<< HEAD
        'wiki',
    ])


def test_refresh_snapins():
    refresh_snapins = [s.type_name() for s in snapin_registry.values() if s.refresh_regularly()]
    assert sorted(refresh_snapins) == sorted([
        'admin',
        'admin_mini',
        'cmc_stats',
        'performance',
        'hostmatrix',
        'mkeventd_performance',
        'nagvis_maps',
=======
    ]

    if not cmk_version.is_raw_edition():
        expected_snapins += [
            'cmc_stats',
            'reports',
        ]

    if cmk_version.is_managed_edition():
        expected_snapins += [
            "customers",
        ]

    assert sorted(snapin_registry.keys()) == sorted(expected_snapins)


def test_refresh_snapins():
    expected_refresh_snapins = [
        'admin',
        'admin_mini',
        'performance',
        'hostmatrix',
        'mkeventd_performance',
        'problem_hosts',
>>>>>>> upstream/master
        'sitestatus',
        'tactical_overview',
        'tag_tree',
        'time',
<<<<<<< HEAD
    ])
=======
    ]

    if not cmk_version.is_raw_edition():
        expected_refresh_snapins += [
            'cmc_stats',
        ]

    refresh_snapins = [s.type_name() for s in snapin_registry.values() if s.refresh_regularly()]
    assert sorted(refresh_snapins) == sorted(expected_refresh_snapins)
>>>>>>> upstream/master
