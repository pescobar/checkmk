<<<<<<< HEAD
import pytest
from cmk_base.check_api import MKCounterWrapped
from checktestlib import BasicCheckResult, CheckResult, DiscoveryResult, assertDiscoveryResultsEqual, PerfValue

pytestmark = pytest.mark.checks

agent_info = [
    [
        ['cpu_busy', '8362860064'],
        ['num_processors', '2'],
    ],
    [
        ['cpu-info clu1-01', 'num_processors 2'],
        ['cpu-info clu1-02', 'num_processors 2'],
        ['cpu-info clu1-01', 'cpu_busy 5340000', 'nvram-battery-status battery_ok'],
        ['cpu-info clu1-02', 'cpu_busy 5400000', 'nvram-battery-status battery_ok'],
    ],
]

result_parsed = [
    {
        '7mode': {
            'cpu_busy': '8362860064',
            'num_processors': '2'
        }
    },
    {
        'clustermode': {
            'clu1-01': {
                'cpu_busy': '5340000',
                'num_processors': '2',
                'nvram-battery-status': 'battery_ok'
            },
            'clu1-02': {
                'cpu_busy': '5400000',
                'num_processors': '2',
                'nvram-battery-status': 'battery_ok'
            }
        }
    },
]
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest  # type: ignore[import]
from testlib import Check  # type: ignore[import]
from cmk.base.check_api import MKCounterWrapped

pytestmark = pytest.mark.checks
>>>>>>> upstream/master

result_parsed_over_time = [
    {
        'clustermode': {
            'clu1-01': {
                'cpu_busy': '0',
                'num_processors': '2',
                'nvram-battery-status': 'battery_ok'
            },
        },
    },
    {
        'clustermode': {
            'clu1-01': {
                'cpu_busy': '8000000',
                'num_processors': '2',
                'nvram-battery-status': 'battery_ok'
            }
        }
    },
    {
        'clustermode': {
            'clu1-01': {
                'cpu_busy': '9000000',
                'num_processors': '2',
                'nvram-battery-status': 'battery_ok'
            }
        }
    },
]


<<<<<<< HEAD
@pytest.mark.parametrize("info, result_parsed", zip(agent_info, result_parsed))
def test_parse_function(check_manager, info, result_parsed):
    check = check_manager.get_check("netapp_api_cpu")
    parsed = check.run_parse(info)
    assert parsed == result_parsed


=======
>>>>>>> upstream/master
@pytest.mark.parametrize("params, first_result_change, second_result_change", [
    (
        {
            'levels': (80.0, 90.0)
        },
        (0, 'Total CPU: 13.33%, 2 CPUs', [('util', 13.333333333333334, 80.0, 90.0, 0, 2)]),
        (0, 'Total CPU: 0.83%, 2 CPUs', [('util', 0.8333333333333334, 80.0, 90.0, 0, 2)]),
    ),
    (
        {
            'levels': (10.0, 90.0)
        },
        (1, 'Total CPU: 13.33% (warn/crit at 10.0%/90.0%), 2 CPUs', [
            ('util', 13.333333333333334, 10.0, 90.0, 0, 2)
        ]),
        (0, 'Total CPU: 0.83%, 2 CPUs', [('util', 0.8333333333333334, 10.0, 90.0, 0, 2)]),
    ),
    (
        {
            'levels': (80.0, 90.0),
            'average': 2,
        },
<<<<<<< HEAD
        (0, '2min average: 0%, 2 CPUs', [('util', 13.333333333333334, 80.0, 90.0, 0, 2),
                                         ('util_average', 0, 80.0, 90.0, 0, 100)]),
        (0, '2min average: 0.42%, 2 CPUs', [('util', 0.8333333333333334, 80.0, 90.0, 0, 2),
                                            ('util_average', 0.4166666666666666, 80.0, 90.0, 0, 100)
                                           ]),
    ),
])
def test_cluster_mode_check_function(check_manager, monkeypatch, params, first_result_change,
                                     second_result_change):
    check = check_manager.get_check("netapp_api_cpu")
=======
        (0, 'Total CPU (2min average): 0%, 2 CPUs', [('util', 13.333333333333334, 80.0, 90.0, 0, 2),
                                                     ('util_average', 0, 80.0, 90.0, 0, 100)]),
        (0, 'Total CPU (2min average): 0.42%, 2 CPUs', [
            ('util', 0.8333333333333334, 80.0, 90.0, 0, 2),
            ('util_average', 0.4166666666666667, 80.0, 90.0, 0, 100)
        ]),
    ),
])
@pytest.mark.usefixtures("config_load_all_checks")
def test_cluster_mode_check_function(monkeypatch, params, first_result_change,
                                     second_result_change):
    check = Check("netapp_api_cpu")
>>>>>>> upstream/master
    monkeypatch.setattr('time.time', lambda: 0)
    try:
        check.run_check('clu1-01', params, result_parsed_over_time[0])
    except MKCounterWrapped:
        pass
    monkeypatch.setattr('time.time', lambda: 60)
    result = check.run_check('clu1-01', params, result_parsed_over_time[1])
    assert result == first_result_change
    monkeypatch.setattr('time.time', lambda: 180)
    result = check.run_check('clu1-01', params, result_parsed_over_time[2])
    assert result == second_result_change
