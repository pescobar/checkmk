<<<<<<< HEAD
import pytest
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]
from testlib import SpecialAgent  # type: ignore[import]
>>>>>>> upstream/master

pytestmark = pytest.mark.checks


@pytest.mark.parametrize('params,expected_args', [
    (('user', 'password'), ["address", "user", "password"]),
])
<<<<<<< HEAD
def test_innovaphone_argument_parsing(check_manager, params, expected_args):
    """Tests if all required arguments are present."""
    agent = check_manager.get_special_agent('agent_innovaphone')
=======
@pytest.mark.usefixtures("config_load_all_checks")
def test_innovaphone_argument_parsing(params, expected_args):
    """Tests if all required arguments are present."""
    agent = SpecialAgent('agent_innovaphone')
>>>>>>> upstream/master
    arguments = agent.argument_func(params, "host", "address")
    assert arguments == expected_args
