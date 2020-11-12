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


@pytest.mark.parametrize('params,expected_args', [
    (
        (None, {
            'onredirect': 'follow',
            'port': 80,
            'uri': '/images',
            'urlize': True,
            'virthost': ('www.test123.de', True)
        }),
        [
            '-u',
            '/images',
            '--onredirect=follow',
            '-L',
<<<<<<< HEAD
            '-H',
            'www.test123.de',
=======
>>>>>>> upstream/master
            '--sni',
            '-p',
            '80',
            'www.test123.de',
<<<<<<< HEAD
=======
            'www.test123.de',
>>>>>>> upstream/master
        ],
    ),
    (
        (None, {
            'extended_perfdata': True,
            'method': 'CONNECT',
            'port': 3128,
            'proxy': '163.172.86.64',
            'ssl': 'auto',
            'uri': '/images',
            'virthost': ('www.test123.de', True)
        }),
        [
            '-u',
            '/images',
            '--ssl',
            '--extended-perfdata',
            '-j',
            'CONNECT',
<<<<<<< HEAD
            '-H',
            'www.test123.de',
=======
>>>>>>> upstream/master
            '--sni',
            '163.172.86.64',
            'www.test123.de:3128',
        ],
    ),
    (
        (None, {
            'cert_days': (10, 20),
            'cert_host': 'www.test123.com',
            'port': '42',
        }),
<<<<<<< HEAD
        ['-C', '10,20', '-H', 'www.test123.com', '--sni', '-p', '42', 'www.test123.com'],
=======
        [
            '-C',
            '10,20',
            '--sni',
            '-p',
            '42',
            'www.test123.com',
            'www.test123.com',
        ],
>>>>>>> upstream/master
    ),
    (
        (None, {
            'cert_days': (10, 20),
            'cert_host': 'www.test123.com',
            'port': '42',
            'proxy': 'p.roxy',
        }),
<<<<<<< HEAD
        [
            '-C', '10,20', '--ssl', '-j', 'CONNECT', '-H', 'www.test123.com', '--sni', 'p.roxy',
            'www.test123.com:42'
        ],
=======
        ['-C', '10,20', '--ssl', '-j', 'CONNECT', '--sni', 'p.roxy', 'www.test123.com:42'],
>>>>>>> upstream/master
    ),
    (
        (None, {
            'cert_days': (10, 20),
            'cert_host': 'www.test123.com',
            'port': '42',
            'proxy': 'p.roxy:23',
        }),
        [
<<<<<<< HEAD
            '-C', '10,20', '--ssl', '-j', 'CONNECT', '-H', 'www.test123.com', '--sni', '-p', '23',
            'p.roxy', 'www.test123.com:42'
=======
            '-C', '10,20', '--ssl', '-j', 'CONNECT', '--sni', '-p', '23', 'p.roxy',
            'www.test123.com:42'
>>>>>>> upstream/master
        ],
    ),
    (
        (None, {
            'cert_days': (10, 20),
            'cert_host': 'www.test123.com',
            'port': '42',
            'proxy': '[dead:beef::face]:23',
        }),
        [
<<<<<<< HEAD
            '-C', '10,20', '--ssl', '-j', 'CONNECT', '-H', 'www.test123.com', '--sni', '-p', '23',
            '[dead:beef::face]', 'www.test123.com:42'
=======
            '-C', '10,20', '--ssl', '-j', 'CONNECT', '--sni', '-p', '23', '[dead:beef::face]',
            'www.test123.com:42'
>>>>>>> upstream/master
        ],
    ),
    (
        {
            'host': {
                "address": 'www.test123.com',
                "port": 42,
                "address_family": 'ipv6'
            },
            'proxy': {
                "address": '[dead:beef::face]',
                "port": 23
            },
            'mode': ('cert', {
                'cert_days': (10, 20)
            }),
            'disable_sni': True
        },
        [
<<<<<<< HEAD
            '-C', '10,20', '--ssl', '-j', 'CONNECT', '-H', 'www.test123.com', '-6', '-p', '23',
            '[dead:beef::face]', 'www.test123.com:42'
        ],
    ),
    (
=======
            '-C', '10,20', '--ssl', '-j', 'CONNECT', '-6', '-p', '23', '[dead:beef::face]',
            'www.test123.com:42'
        ],
    ),
    (
        {
            'host': {
                "address": 'www.test123.com',
            },
            'mode': ('url', {
                'ssl': "auto"
            }),
        },
        ['--ssl', '--sni', 'www.test123.com'],
    ),
    (
>>>>>>> upstream/master
        (None, {
            'virthost': ("virtual.host", True),
            'proxy': "foo.bar",
        }),
<<<<<<< HEAD
        ['-H', 'virtual.host', '--sni', 'foo.bar', 'virtual.host'],
=======
        ['--sni', 'foo.bar', 'virtual.host'],
>>>>>>> upstream/master
    ),
    (
        (None, {
            'virthost': ("virtual.host", False),
            'proxy': "foo.bar",
        }),
<<<<<<< HEAD
        ['-H', 'virtual.host', '--sni', 'foo.bar', 'virtual.host'],
=======
        ['--sni', 'foo.bar', 'virtual.host'],
>>>>>>> upstream/master
    ),
    (
        (None, {
            'virthost': ("virtual.host", True),
        }),
<<<<<<< HEAD
        ['-H', 'virtual.host', '--sni', 'virtual.host'],
=======
        ['--sni', 'virtual.host', 'virtual.host'],
>>>>>>> upstream/master
    ),
    (
        (None, {
            'virthost': ("virtual.host", False),
        }),
<<<<<<< HEAD
        ['-H', 'virtual.host', '--sni', '$_HOSTADDRESS_4$'],
    ),
])
def test_check_http_argument_parsing(check_manager, params, expected_args):
    """Tests if all required arguments are present."""
    active_check = check_manager.get_active_check('check_http')
=======
        ['--sni', '$_HOSTADDRESS_4$', 'virtual.host'],
    ),
])
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_http_argument_parsing(params, expected_args):
    """Tests if all required arguments are present."""
    active_check = ActiveCheck('check_http')
>>>>>>> upstream/master
    assert active_check.run_argument_function(params) == expected_args


@pytest.mark.parametrize('params,expected_description', [
    (
        (u'No SSL Test', {}),
        u'HTTP No SSL Test',
    ),
    (
        (u'Test with SSL', {
            'ssl': "auto"
        }),
        u'HTTPS Test with SSL',
    ),
    (
        (u'^No Prefix Test', {}),
        u'No Prefix Test',
    ),
])
<<<<<<< HEAD
def test_check_http_service_description(check_manager, params, expected_description):
    active_check = check_manager.get_active_check('check_http')
=======
@pytest.mark.usefixtures("config_load_all_checks")
def test_check_http_service_description(params, expected_description):
    active_check = ActiveCheck('check_http')
>>>>>>> upstream/master
    assert active_check.run_service_description(params) == expected_description
