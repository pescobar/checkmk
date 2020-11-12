<<<<<<< HEAD
#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.
"""Helper functions for dealing with Checkmk labels of all kind"""

import sys
import abc
from typing import Any, Dict, Text, List  # pylint: disable=unused-import
import six

# Explicitly check for Python 3 (which is understood by mypy)
if sys.version_info[0] >= 3:
    from pathlib import Path  # pylint: disable=import-error,unused-import
else:
    from pathlib2 import Path

import cmk.utils.paths
import cmk.utils.store
from cmk.utils.rulesets.ruleset_matcher import RulesetMatcher, RulesetMatchObject  # pylint: disable=unused-import


class LabelManager(object):
    """Helper class to manage access to the host and service labels"""
    def __init__(self, explicit_host_labels, host_label_rules, service_label_rules,
                 autochecks_manager):
        # type: (Dict, List, List, Any) -> None
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Helper functions for dealing with Checkmk labels of all kind"""

import abc
from pathlib import Path
from typing import Callable, List, Dict

import cmk.utils.paths
import cmk.utils.store as store
from cmk.utils.rulesets.ruleset_matcher import RulesetMatcher, RulesetMatchObject
from cmk.utils.type_defs import HostName, ServiceName, Labels, LabelSources


class LabelManager:
    """Helper class to manage access to the host and service labels"""
    def __init__(self, explicit_host_labels: Dict, host_label_rules: List,
                 service_label_rules: List,
                 discovered_labels_of_service: Callable[[HostName, ServiceName], Labels]) -> None:
>>>>>>> upstream/master
        super(LabelManager, self).__init__()
        self._explicit_host_labels = explicit_host_labels
        self._host_label_rules = host_label_rules
        self._service_label_rules = service_label_rules
<<<<<<< HEAD
        self._autochecks_manager = autochecks_manager

    def labels_of_host(self, ruleset_matcher, hostname):
        # type: (RulesetMatcher, str) -> Dict
=======
        self._discovered_labels_of_service = discovered_labels_of_service

    def labels_of_host(self, ruleset_matcher: RulesetMatcher, hostname: HostName) -> Labels:
>>>>>>> upstream/master
        """Returns the effective set of host labels from all available sources

        1. Discovered labels
        2. Ruleset "Host labels"
        3. Explicit labels (via host/folder config)

        Last one wins.
        """
<<<<<<< HEAD
        labels = {}
=======
        labels: Labels = {}
>>>>>>> upstream/master
        labels.update(self._discovered_labels_of_host(hostname))
        labels.update(self._ruleset_labels_of_host(ruleset_matcher, hostname))
        labels.update(self._explicit_host_labels.get(hostname, {}))
        return labels

<<<<<<< HEAD
    def label_sources_of_host(self, ruleset_matcher, hostname):
        # type: (RulesetMatcher, str) -> Dict[str, str]
        """Returns the effective set of host label keys with their source
        identifier instead of the value Order and merging logic is equal to
        _get_host_labels()"""
        labels = {}
=======
    def label_sources_of_host(self, ruleset_matcher: RulesetMatcher,
                              hostname: HostName) -> LabelSources:
        """Returns the effective set of host label keys with their source
        identifier instead of the value Order and merging logic is equal to
        _get_host_labels()"""
        labels: LabelSources = {}
>>>>>>> upstream/master
        labels.update({k: "discovered" for k in self._discovered_labels_of_host(hostname).keys()})
        labels.update(
            {k: "ruleset" for k in self._ruleset_labels_of_host(ruleset_matcher, hostname)})
        labels.update({k: "explicit" for k in self._explicit_host_labels.get(hostname, {}).keys()})
        return labels

<<<<<<< HEAD
    def _ruleset_labels_of_host(self, ruleset_matcher, hostname):
        # type: (RulesetMatcher, str) -> Dict
        match_object = RulesetMatchObject(hostname, service_description=None)
        return ruleset_matcher.get_host_ruleset_merged_dict(match_object, self._host_label_rules)

    def _discovered_labels_of_host(self, hostname):
        # type: (str) -> Dict
        return {
            label_id: label["value"]
            for label_id, label in DiscoveredHostLabelsStore(hostname).load().iteritems()
        }

    def labels_of_service(self, ruleset_matcher, hostname, service_desc):
        # type: (RulesetMatcher, str, Text) -> Dict
=======
    def _ruleset_labels_of_host(self, ruleset_matcher: RulesetMatcher,
                                hostname: HostName) -> Labels:
        match_object = RulesetMatchObject(hostname, service_description=None)
        return ruleset_matcher.get_host_ruleset_merged_dict(match_object, self._host_label_rules)

    def _discovered_labels_of_host(self, hostname: HostName) -> Labels:
        return {
            label_id: label["value"]
            for label_id, label in DiscoveredHostLabelsStore(hostname).load().items()
        }

    def labels_of_service(self, ruleset_matcher: RulesetMatcher, hostname: HostName,
                          service_desc: ServiceName) -> Labels:
>>>>>>> upstream/master
        """Returns the effective set of service labels from all available sources

        1. Discovered labels
        2. Ruleset "Host labels"

        Last one wins.
        """
<<<<<<< HEAD
        labels = {}
=======
        labels: Labels = {}
>>>>>>> upstream/master
        labels.update(self._discovered_labels_of_service(hostname, service_desc))
        labels.update(self._ruleset_labels_of_service(ruleset_matcher, hostname, service_desc))

        return labels

<<<<<<< HEAD
    def label_sources_of_service(self, ruleset_matcher, hostname, service_desc):
        # type: (RulesetMatcher, str, Text) -> Dict[str, str]
        """Returns the effective set of host label keys with their source
        identifier instead of the value Order and merging logic is equal to
        _get_host_labels()"""
        labels = {}
=======
    def label_sources_of_service(self, ruleset_matcher: RulesetMatcher, hostname: HostName,
                                 service_desc: ServiceName) -> LabelSources:
        """Returns the effective set of host label keys with their source
        identifier instead of the value Order and merging logic is equal to
        _get_host_labels()"""
        labels: LabelSources = {}
>>>>>>> upstream/master
        labels.update(
            {k: "discovered" for k in self._discovered_labels_of_service(hostname, service_desc)})
        labels.update({
            k: "ruleset"
            for k in self._ruleset_labels_of_service(ruleset_matcher, hostname, service_desc)
        })

        return labels

<<<<<<< HEAD
    def _ruleset_labels_of_service(self, ruleset_matcher, hostname, service_desc):
        # type: (RulesetMatcher, str, Text) -> Dict
=======
    def _ruleset_labels_of_service(self, ruleset_matcher: RulesetMatcher, hostname: HostName,
                                   service_desc: ServiceName) -> Labels:
>>>>>>> upstream/master
        match_object = RulesetMatchObject(hostname, service_description=service_desc)
        return ruleset_matcher.get_service_ruleset_merged_dict(match_object,
                                                               self._service_label_rules)

<<<<<<< HEAD
    def _discovered_labels_of_service(self, hostname, service_desc):
        # type: (str, Text) -> Dict
        return self._autochecks_manager.discovered_labels_of(hostname, service_desc).to_dict()


class ABCDiscoveredLabelsStore(six.with_metaclass(abc.ABCMeta, object)):
    """Managing persistance of discovered labels"""
    @abc.abstractproperty
    def file_path(self):
        # type () -> Path
        raise NotImplementedError()

    def load(self):
        # type: () -> Dict
        # Skip labels discovered by the previous HW/SW inventory approach (which was addded+removed in 1.6 beta)
        return {
            k: v for k, v in cmk.utils.store.load_data_from_file(str(
                self.file_path), default={}).iteritems() if isinstance(v, dict)
        }

    def save(self, labels):
        # type: (Dict) -> None
=======

class ABCDiscoveredLabelsStore(metaclass=abc.ABCMeta):
    """Managing persistance of discovered labels"""
    @abc.abstractproperty
    def file_path(self) -> Path:
        raise NotImplementedError()

    def load(self) -> Dict:
        # Skip labels discovered by the previous HW/SW inventory approach (which was addded+removed in 1.6 beta)
        return {
            k: v
            for k, v in store.load_object_from_file(str(self.file_path), default={}).items()
            if isinstance(v, dict)
        }

    def save(self, labels: Dict) -> None:
>>>>>>> upstream/master
        if not labels:
            if self.file_path.exists():
                self.file_path.unlink()
            return

<<<<<<< HEAD
        self.file_path.parent.mkdir(parents=True, exist_ok=True)  # pylint: disable=no-member
        cmk.utils.store.save_data_to_file(str(self.file_path), labels)


class DiscoveredHostLabelsStore(ABCDiscoveredLabelsStore):
    def __init__(self, hostname):
        # type: (str) -> None
=======
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        store.save_object_to_file(str(self.file_path), labels)


class DiscoveredHostLabelsStore(ABCDiscoveredLabelsStore):
    def __init__(self, hostname: str) -> None:
>>>>>>> upstream/master
        super(DiscoveredHostLabelsStore, self).__init__()
        self._hostname = hostname

    @property
<<<<<<< HEAD
    def file_path(self):
        # type () -> Path
=======
    def file_path(self) -> Path:
>>>>>>> upstream/master
        return (cmk.utils.paths.discovered_host_labels_dir / self._hostname).with_suffix(".mk")
