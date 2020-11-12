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
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master
"""Provides the user with hints about his setup. Performs different
checks and tells the user what could be improved."""

import traceback
<<<<<<< HEAD
=======
from typing import Dict, Type, Iterator, Optional, List, Any
>>>>>>> upstream/master

from livestatus import LocalConnection
import cmk.utils.defines

import cmk.gui.sites
import cmk.gui.config as config
<<<<<<< HEAD
from cmk.gui.i18n import _
from cmk.gui.log import logger
from cmk.gui.exceptions import MKGeneralException
from cmk.gui.globals import html
=======
import cmk.gui.escaping as escaping
from cmk.gui.i18n import _
from cmk.gui.log import logger
from cmk.gui.exceptions import MKGeneralException
>>>>>>> upstream/master

from cmk.gui.watolib.global_settings import load_configuration_settings
from cmk.gui.watolib.sites import SiteManagementFactory
from cmk.gui.plugins.watolib.utils import ABCConfigDomain
from cmk.gui.watolib.automation_commands import (
    AutomationCommand,
    automation_command_registry,
)


<<<<<<< HEAD
class ACResult(object):
    status = None

    def __init__(self, text):
=======
class ACResult:
    status: Optional[int] = None

    def __init__(self, text: str) -> None:
>>>>>>> upstream/master
        super(ACResult, self).__init__()
        self.text = text
        self.site_id = config.omd_site()

    def from_test(self, test):
        self.test_id = test.id()
        self.category = test.category()
        self.title = test.title()
        self.help = test.help()

    @classmethod
    def merge(cls, *results):
        """Create a new result object from the given result objects.

        a) use the worst state
        b) concatenate the texts
        """
        texts, worst_cls = [], ACResultOK
        for result in results:
            text = result.text
            if result.status != 0:
                text += " (%s)" % ("!" * result.status)
            texts.append(text)

            if result.status > worst_cls.status:
                worst_cls = result.__class__

        return worst_cls(", ".join(texts))

<<<<<<< HEAD
    def status_name(self):
        return cmk.utils.defines.short_service_state_name(self.status)

    @classmethod
    def from_repr(cls, repr_data):
=======
    def status_name(self) -> str:
        if self.status is None:
            return u""
        return cmk.utils.defines.short_service_state_name(self.status)

    @classmethod
    def from_repr(cls, repr_data: Dict[str, Any]) -> 'ACResult':
>>>>>>> upstream/master
        result_class_name = repr_data.pop("class_name")
        result = globals()[result_class_name](repr_data["text"])

        for key, val in repr_data.items():
            setattr(result, key, val)

        return result

<<<<<<< HEAD
    def __repr__(self):
=======
    def __repr__(self) -> str:
>>>>>>> upstream/master
        return repr({
            "site_id": self.site_id,
            "class_name": self.__class__.__name__,
            "text": self.text,
            # These fields are be static - at least for the current version, but
            # we transfer them to the central system to be able to handle test
            # results of tests not known to the central site.
            "test_id": self.test_id,
            "category": self.category,
            "title": self.title,
            "help": self.help,
        })


class ACResultNone(ACResult):
    status = -1


class ACResultCRIT(ACResult):
    status = 2


class ACResultWARN(ACResult):
    status = 1


class ACResultOK(ACResult):
    status = 0


<<<<<<< HEAD
class ACTestCategories(object):
=======
class ACTestCategories:
    connectivity = "connectivity"
>>>>>>> upstream/master
    usability = "usability"
    performance = "performance"
    security = "security"
    reliability = "reliability"
    deprecations = "deprecations"

    @classmethod
    def title(cls, ident):
        return {
<<<<<<< HEAD
=======
            "connectivity": _("Connectivity"),
>>>>>>> upstream/master
            "usability": _("Usability"),
            "performance": _("Performance"),
            "security": _("Security"),
            "reliability": _("Reliability"),
            "deprecations": _("Deprecations"),
        }[ident]


<<<<<<< HEAD
class ACTest(object):
    def __init__(self):
        self._executed = False
        self._results = []

    def id(self):
        return self.__class__.__name__

    def category(self):
        """Return the internal name of the category the BP test is associated with"""
        raise NotImplementedError()

    def title(self):
        raise NotImplementedError()

    def help(self):
        raise NotImplementedError()

    def is_relevant(self):
=======
class ACTest:
    def __init__(self) -> None:
        self._executed = False
        self._results: List[ACResult] = []

    def id(self) -> str:
        return self.__class__.__name__

    def category(self) -> str:
        """Return the internal name of the category the BP test is associated with"""
        raise NotImplementedError()

    def title(self) -> str:
        raise NotImplementedError()

    def help(self) -> str:
        raise NotImplementedError()

    def is_relevant(self) -> bool:
>>>>>>> upstream/master
        """A test can check whether or not is relevant for the current evnironment.
        In case this method returns False, the check will not be executed and not
        be shown to the user."""
        raise NotImplementedError()

<<<<<<< HEAD
    def execute(self):
=======
    def execute(self) -> Iterator[ACResult]:
>>>>>>> upstream/master
        """Implement the test logic here. The method needs to add one or more test
        results like this:

        yield ACResultOK(_("it's fine"))
        """
        raise NotImplementedError()

<<<<<<< HEAD
    def run(self):
=======
    def run(self) -> Iterator[ACResult]:
>>>>>>> upstream/master
        self._executed = True
        try:
            # Do not merge results that have been gathered on one site for different sites
            results = list(self.execute())
            num_sites = len(set(r.site_id for r in results))
            if num_sites > 1:
                for result in results:
                    result.from_test(self)
                    yield result
                return

            # Merge multiple results produced for a single site
            total_result = ACResult.merge(*list(self.execute()))
            total_result.from_test(self)
            yield total_result
        except Exception:
            logger.exception("error executing configuration test %s", self.__class__.__name__)
            result = ACResultCRIT(
                "<pre>%s</pre>" % _("Failed to execute the test %s: %s") %
<<<<<<< HEAD
                (html.attrencode(self.__class__.__name__), traceback.format_exc()))
            result.from_test(self)
            yield result

    def status(self):
        return max([0] + [r.status for r in self.results])

    def status_name(self):
        return cmk.utils.defines.short_service_state_name(self.status())

    @property
    def results(self):
=======
                (escaping.escape_attribute(self.__class__.__name__), traceback.format_exc()))
            result.from_test(self)
            yield result

    def status(self) -> int:
        return max([0] + [(r.status or 0) for r in self.results])

    def status_name(self) -> str:
        return cmk.utils.defines.short_service_state_name(self.status())

    @property
    def results(self) -> List[ACResult]:
>>>>>>> upstream/master
        if not self._executed:
            raise MKGeneralException(_("The test has not been executed yet"))
        return self._results

<<<<<<< HEAD
    def _uses_microcore(self):
=======
    def _uses_microcore(self) -> bool:
>>>>>>> upstream/master
        """Whether or not the local site is using the CMC"""
        local_connection = LocalConnection()
        version = local_connection.query_value("GET status\nColumns: program_version\n", deflt="")
        return version.startswith("Check_MK")

<<<<<<< HEAD
    def _get_effective_global_setting(self, varname):
=======
    def _get_effective_global_setting(self, varname: str) -> Any:
>>>>>>> upstream/master
        global_settings = load_configuration_settings()
        default_values = ABCConfigDomain.get_all_default_globals()

        if cmk.gui.config.is_wato_slave_site():
            current_settings = load_configuration_settings(site_specific=True)
        else:
            sites = SiteManagementFactory.factory().load_sites()
            current_settings = sites[config.omd_site()].get("globals", {})

        if varname in current_settings:
<<<<<<< HEAD
            value = current_settings[varname]
        elif varname in global_settings:
            value = global_settings[varname]
        else:
            value = default_values[varname]

        return value


class ACTestRegistry(cmk.utils.plugin_registry.ClassRegistry):
    def plugin_base_class(self):
        return ACTest

    def plugin_name(self, plugin_class):
        return plugin_class.__name__
=======
            return current_settings[varname]
        if varname in global_settings:
            return global_settings[varname]
        return default_values[varname]


class ACTestRegistry(cmk.utils.plugin_registry.Registry[Type[ACTest]]):
    def plugin_name(self, instance: Type[ACTest]) -> str:
        return instance.__name__
>>>>>>> upstream/master


ac_test_registry = ACTestRegistry()


@automation_command_registry.register
class AutomationCheckAnalyzeConfig(AutomationCommand):
<<<<<<< HEAD
    def command_name(self):
=======
    def command_name(self) -> str:
>>>>>>> upstream/master
        return "check-analyze-config"

    def get_request(self):
        return None

<<<<<<< HEAD
    def execute(self, _unused_request):
        results = []
=======
    def execute(self, _unused_request: None) -> List[ACResult]:
        results: List[ACResult] = []
>>>>>>> upstream/master
        for test_cls in ac_test_registry.values():
            test = test_cls()

            if not test.is_relevant():
                continue

            for result in test.run():
                results.append(result)

        return results
