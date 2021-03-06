<<<<<<< HEAD
import pytest
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]
from testlib import Check  # type: ignore[import]
>>>>>>> upstream/master

pytestmark = pytest.mark.checks


@pytest.mark.parametrize("info, item_expected, data_expected", [
    ([[u'29', u'0']], 'Board', {}),
    ([[u'0', u'29']], 'CPU', {}),
])
<<<<<<< HEAD
def test_inventory_function(check_manager, info, item_expected, data_expected):
    """
    Verifies if the item is detected corresponding to info content.
    """
    check = check_manager.get_check("alcatel_temp")
    result = check.run_discovery(info)
    result = [r for r in result]
=======
@pytest.mark.usefixtures("config_load_all_checks")
def test_inventory_function(info, item_expected, data_expected):
    """
    Verifies if the item is detected corresponding to info content.
    """
    check = Check("alcatel_temp")
    result = list(check.run_discovery(info))
>>>>>>> upstream/master
    assert result[0][0] == item_expected
    assert result[0][1] == data_expected


@pytest.mark.parametrize(
    "parameters, item, info, state_expected, infotext_expected, perfdata_expected", [
        ((30, 40), u'Slot 1 Board', [[u'29', u'0']], 0, '29', [('temp', 29, 30, 40)]),
        ((30, 40), u'Slot 1 Board', [[u'31', u'0']], 1, '31', [('temp', 31, 30, 40)]),
        ((30, 40), u'Slot 1 Board', [[u'41', u'0']], 2, '41', [('temp', 41, 30, 40)]),
        ((30, 40), u'Slot 1 CPU', [[u'0', u'29']], 0, '29', [('temp', 29, 30, 40)]),
        ((30, 40), u'Slot 1 CPU', [[u'0', u'31']], 1, '31', [('temp', 31, 30, 40)]),
        ((30, 40), u'Slot 1 CPU', [[u'0', u'41']], 2, '41', [('temp', 41, 30, 40)]),
    ])
<<<<<<< HEAD
def test_check_function(check_manager, parameters, item, info, state_expected, infotext_expected,
=======
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_function(parameters, item, info, state_expected, infotext_expected,
>>>>>>> upstream/master
                        perfdata_expected):
    """
    Verifies if check function asserts warn and crit Board and CPU temperature levels.
    """
<<<<<<< HEAD
    check = check_manager.get_check("alcatel_temp")
=======
    check = Check("alcatel_temp")
>>>>>>> upstream/master
    state, infotext, perfdata = check.run_check(item, parameters, info)
    assert state == state_expected
    assert infotext_expected in infotext
    assert perfdata == perfdata_expected
