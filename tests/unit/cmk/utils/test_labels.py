<<<<<<< HEAD
# encoding: utf-8
# pylint: disable=redefined-outer-name

import pytest  # type: ignore
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# pylint: disable=redefined-outer-name

import pytest  # type: ignore[import]
>>>>>>> upstream/master
import cmk.utils.paths
from cmk.utils.labels import DiscoveredHostLabelsStore

# Manager is currently not tested explicitly. Indirect tests can be found
<<<<<<< HEAD
# at tests/unit/cmk_base/test_config.py::test_host_config_labels*
=======
# at tests/unit/cmk/base/test_config.py::test_host_config_labels*
>>>>>>> upstream/master


@pytest.fixture()
def discovered_host_labels_dir(tmp_path, monkeypatch):
    path = tmp_path / "var" / "check_mk" / "discovered_host_labels"
    monkeypatch.setattr(cmk.utils.paths, "discovered_host_labels_dir", path)
    return path


def test_discovered_host_labels_store_file_path(discovered_host_labels_dir):
    assert DiscoveredHostLabelsStore("host").file_path == discovered_host_labels_dir / "host.mk"


def test_discovered_host_labels_store_load_default(discovered_host_labels_dir):
    store = DiscoveredHostLabelsStore("host")
<<<<<<< HEAD
    assert not store.file_path.exists()  # pylint: disable=no-member
=======
    assert not store.file_path.exists()
>>>>>>> upstream/master
    assert store.load() == {}
