<<<<<<< HEAD
# Triggers plugin loading of plugins.wato which registers all the plugins
import cmk.gui.wato  # pylint: disable=unused-import
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# Triggers plugin loading of plugins.wato which registers all the plugins
import cmk.utils.version as cmk_version
import cmk.gui.wato  # noqa: F401 # pylint: disable=unused-import
>>>>>>> upstream/master
import cmk.gui.watolib as watolib


def test_registered_ac_tests():
<<<<<<< HEAD
    registered_plugins = sorted(watolib.ac_test_registry.keys())
    assert registered_plugins == sorted([
=======
    expected_ac_tests = [
>>>>>>> upstream/master
        'ACTestAlertHandlerEventTypes',
        'ACTestApacheNumberOfProcesses',
        'ACTestApacheProcessUsage',
        'ACTestBackupConfigured',
        'ACTestBackupNotEncryptedConfigured',
        'ACTestBrokenGUIExtension',
        'ACTestCheckMKHelperUsage',
<<<<<<< HEAD
=======
        'ACTestCheckMKFetcherUsage',
        'ACTestCheckMKCheckerUsage',
        'ACTestConnectivity',
>>>>>>> upstream/master
        'ACTestESXDatasources',
        'ACTestGenericCheckHelperUsage',
        'ACTestHTTPSecured',
        'ACTestLDAPSecured',
        'ACTestLiveproxyd',
        'ACTestLivestatusUsage',
        'ACTestLivestatusSecured',
        'ACTestNumberOfUsers',
        'ACTestOldDefaultCredentials',
        'ACTestPersistentConnections',
        'ACTestRulebasedNotifications',
<<<<<<< HEAD
        'ACTestSecureAgentUpdaterTransport',
        'ACTestSecureNotificationSpoolerMessages',
        'ACTestSizeOfExtensions',
        'ACTestTmpfs',
    ])
=======
        'ACTestSizeOfExtensions',
        'ACTestTmpfs',
        'ACTestUnexpectedAllowedIPRanges',
    ]

    if not cmk_version.is_raw_edition():
        expected_ac_tests += [
            'ACTestSecureAgentUpdaterTransport',
            'ACTestSecureNotificationSpoolerMessages',
        ]

    registered_plugins = sorted(watolib.ac_test_registry.keys())
    assert registered_plugins == sorted(expected_ac_tests)
>>>>>>> upstream/master
