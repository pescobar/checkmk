<<<<<<< HEAD
import pytest
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]
from testlib import ActiveCheck  # type: ignore[import]
>>>>>>> upstream/master

pytestmark = pytest.mark.checks


@pytest.mark.parametrize("params,expected_args", [
<<<<<<< HEAD
    ((1, {}), ["-p", 1, "-H", "'$HOSTADDRESS$'"]),
])
def test_check_tcp_argument_parsing(check_manager, params, expected_args):
    """Tests if all required arguments are present."""
    active_check = check_manager.get_active_check("check_tcp")
=======
    ((1, {}), ["-p", "1", "-H", "$HOSTADDRESS$"]),
])
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_tcp_argument_parsing(params, expected_args):
    """Tests if all required arguments are present."""
    active_check = ActiveCheck("check_tcp")
>>>>>>> upstream/master
    assert active_check.run_argument_function(params) == expected_args
