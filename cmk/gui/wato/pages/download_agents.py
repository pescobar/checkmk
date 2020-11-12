<<<<<<< HEAD
#!/usr/bin/env python
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
"""Simple download page for the builtin agents and plugins"""

import os
import glob
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Simple download page for the builtin agents and plugins"""

import os
import abc
import glob
import fnmatch
from typing import List, Iterator
>>>>>>> upstream/master

import cmk.utils.paths
import cmk.utils.render

import cmk.gui.watolib as watolib
import cmk.gui.forms as forms
from cmk.gui.i18n import _
from cmk.gui.globals import html
<<<<<<< HEAD
=======
from cmk.gui.breadcrumb import Breadcrumb
from cmk.gui.page_menu import (
    PageMenu,
    PageMenuDropdown,
    PageMenuTopic,
    PageMenuEntry,
    make_simple_link,
)
>>>>>>> upstream/master

from cmk.gui.plugins.wato import (
    WatoMode,
    mode_registry,
<<<<<<< HEAD
    global_buttons,
)


@mode_registry.register
class ModeDownloadAgents(WatoMode):
    @classmethod
    def name(cls):
        return "download_agents"

    @classmethod
    def permissions(cls):
        return ["download_agents"]

    def title(self):
        return _("Agents and Plugins")

    def buttons(self):
        global_buttons()
        if watolib.has_agent_bakery():
            html.context_button(_("Baked agents"),
                                watolib.folder_preserving_link([("mode", "agents")]),
                                "download_agents")
        html.context_button(_("Release Notes"), "version.py", "mk")

    def page(self):
        html.open_div(class_="rulesets")
        packed = glob.glob(cmk.utils.paths.agents_dir + "/*.deb") \
                + glob.glob(cmk.utils.paths.agents_dir + "/*.rpm") \
                + glob.glob(cmk.utils.paths.agents_dir + "/windows/c*.msi")

        self._download_table(_("Packaged Agents"), {}, packed)

        titles = {
            '': _('Linux/Unix Agents'),
            '/plugins': _('Linux/Unix Agents - Plugins'),
            '/cfg_examples': _('Linux/Unix Agents - Example Configurations'),
            '/cfg_examples/systemd': _('Linux Agent - Example configuration using with systemd'),
            '/windows': _('Windows Agent'),
            '/windows/plugins': _('Windows Agent - Plugins'),
            '/windows/mrpe': _('Windows Agent - MRPE Scripts'),
            '/windows/cfg_examples': _('Windows Agent - Example Configurations'),
            '/windows/ohm': _('Windows Agent - OpenHardwareMonitor (headless)'),
=======
    folder_preserving_link,
)


class ABCModeDownloadAgents(WatoMode):
    @classmethod
    def permissions(cls) -> List[str]:
        return ["download_agents"]

    def page_menu(self, breadcrumb: Breadcrumb) -> PageMenu:
        return PageMenu(
            dropdowns=[
                PageMenuDropdown(
                    name="related",
                    title=_("Related"),
                    topics=[
                        PageMenuTopic(
                            title=_("Setup"),
                            entries=list(self._page_menu_entries_related()),
                        ),
                    ],
                ),
            ],
            breadcrumb=breadcrumb,
        )

    def _page_menu_entries_related(self) -> Iterator[PageMenuEntry]:
        if watolib.has_agent_bakery():
            yield PageMenuEntry(
                title=_("Windows, Linux, Solaris, AIX"),
                icon_name="agents",
                item=make_simple_link(watolib.folder_preserving_link([("mode", "agents")])),
            )

        if self.name() != "download_agents_windows":
            yield PageMenuEntry(
                title=_("Windows files"),
                icon_name="download_agents",
                item=make_simple_link(folder_preserving_link([("mode", "download_agents_windows")
                                                             ])),
            )

        if self.name() != "download_agents_linux":
            yield PageMenuEntry(
                title=_("Linux, Solaris, AIX files"),
                icon_name="download_agents",
                item=make_simple_link(folder_preserving_link([("mode", "download_agents_linux")])),
            )

        if self.name() != "download_agents":
            yield PageMenuEntry(
                title=_("Other operating systems"),
                icon_name="download_agents",
                item=make_simple_link(folder_preserving_link([("mode", "download_agents")])),
            )

    @abc.abstractmethod
    def _packed_agents(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def _walk_base_dir(self):
        raise NotImplementedError()

    def _exclude_file_glob_patterns(self):
        return []

    def _exclude_paths(self):
        return set([
            '/bakery',
            '/special',
            '/windows/baked_container.msi',
            '/windows/plugins/.gitattributes',
        ])

    def page(self) -> None:
        html.open_div(class_="rulesets")

        packed = self._packed_agents()
        if packed:
            self._download_table(_("Packaged Agents"), packed)

        titles = {
            '': _('Agents'),
            '/plugins': _('Plugins'),
            '/cfg_examples': _('Example Configurations'),
            '/cfg_examples/systemd': _('Example configuration for systemd'),
            '/windows': _('Windows Agent'),
            '/windows/plugins': _('Plugins'),
            '/windows/mrpe': _('Scripts to integrate Nagios plugis'),
            '/windows/cfg_examples': _('Example Configurations'),
            '/windows/ohm': _('OpenHardwareMonitor (headless)'),
>>>>>>> upstream/master
            '/z_os': _('z/OS'),
            '/sap': _('SAP R/3'),
        }

<<<<<<< HEAD
        banned_paths = [
            '/bakery',
            '/special',
            '/windows/msibuild',
            '/windows/msibuild/patches',
            '/windows/sections',
        ]

        file_titles = {}
        other_sections = []
        for root, _dirs, files in os.walk(cmk.utils.paths.agents_dir):
            file_paths = []
            relpath = root.split('agents')[1]
            if relpath not in banned_paths:
                title = titles.get(relpath, relpath)
                for filename in files:
                    if filename == "CONTENTS":
                        file_titles.update(self._read_agent_contents_file(root))

                    path = root + '/' + filename
                    if path not in packed and 'deprecated' not in path:
                        file_paths.append(path)

                other_sections.append((title, file_paths))

        other_sections.sort()

        for title, file_paths in other_sections:
            useful_file_paths = [
                p for p in file_paths
                if file_titles.get(p, "") is not None \
                    and not p.endswith("/CONTENTS")
            ]
            file_titles.update(self._read_plugin_inline_comments(useful_file_paths))
            if useful_file_paths:
                self._download_table(title, file_titles, sorted(useful_file_paths))
        html.close_div()

    def _download_table(self, title, file_titles, paths):
=======
        banned_paths = self._exclude_paths()

        other_sections = []
        for root, _dirs, files in os.walk(self._walk_base_dir()):
            file_paths = []
            relpath = root.split('agents')[1]
            if relpath in banned_paths:
                continue

            title = titles.get(relpath, relpath)
            for filename in files:
                rel_file_path = relpath + '/' + filename
                if rel_file_path in banned_paths:
                    continue

                if self._exclude_by_pattern(rel_file_path):
                    continue

                path = root + '/' + filename
                if path not in packed and 'deprecated' not in path:
                    file_paths.append(path)

            other_sections.append((title, file_paths))

        for title, file_paths in sorted(other_sections):
            useful_file_paths = [p for p in file_paths if not p.endswith("/CONTENTS")]
            if useful_file_paths:
                self._download_table(title, sorted(useful_file_paths))
        html.close_div()

    def _exclude_by_pattern(self, rel_file_path):
        for exclude_pattern in self._exclude_file_glob_patterns():
            if fnmatch.fnmatch(rel_file_path, exclude_pattern):
                return True
        return False

    def _download_table(self, title: str, paths: List[str]) -> None:
>>>>>>> upstream/master
        forms.header(title)
        forms.container()
        for path in paths:
            os_path = path
            relpath = path.replace(cmk.utils.paths.agents_dir + '/', '')
            filename = path.split('/')[-1]
<<<<<<< HEAD
            title = file_titles.get(os_path, filename)
=======
>>>>>>> upstream/master

            file_size = os.stat(os_path).st_size

            # FIXME: Rename classes etc. to something generic
            html.open_div(class_="ruleset")
            html.open_div(style="width:300px;", class_="text")
<<<<<<< HEAD
            html.a(title, href="agents/%s" % relpath)
            html.span("." * 100, class_="dots")
=======
            html.a(filename, href="agents/%s" % relpath)
            html.span("." * 200, class_="dots")
>>>>>>> upstream/master
            html.close_div()
            html.div(cmk.utils.render.fmt_bytes(file_size), style="width:60px;", class_="rulecount")
            html.close_div()
            html.close_div()
        forms.end()

<<<<<<< HEAD
    def _read_plugin_inline_comments(self, file_paths):
        comment_prefixes = ["# ", "REM ", "$!# "]
        windows_bom = "\xef\xbb\xbf"
        file_titles = {}
        for path in file_paths:
            first_bytes = open(path).read(500)
            if first_bytes.startswith(windows_bom):
                first_bytes = first_bytes[len(windows_bom):]
            first_lines = first_bytes.splitlines()
            for line in first_lines:
                for prefix in comment_prefixes:
                    if line.startswith(prefix) and len(line) > len(prefix) and line[len(
                            prefix)].isalpha():
                        file_titles[path] = line[len(prefix):].strip()
                        break
                if path in file_titles:
                    break
        return file_titles

    def _read_agent_contents_file(self, root):
        file_titles = {}
        for line in open(root + "/CONTENTS"):
            line = line.strip()
            if line and not line.startswith("#"):
                file_name, title = line.split(None, 1)
                if title == "(hide)":
                    file_titles[root + "/" + file_name] = None
                else:
                    file_titles[root + "/" + file_name] = title
        return file_titles
=======

@mode_registry.register
class ModeDownloadAgentsOther(ABCModeDownloadAgents):
    @classmethod
    def name(cls) -> str:
        return "download_agents"

    def title(self) -> str:
        return _("Other operating systems")

    def _packed_agents(self):
        return []

    def _walk_base_dir(self):
        return cmk.utils.paths.agents_dir

    def _exclude_file_glob_patterns(self):
        return [
            "*.rpm",
            "*.deb",
            "*.aix",
            "*.linux",
            "*.solaris",
        ]

    def _exclude_paths(self):
        exclude = super()._exclude_paths()
        exclude.add("/cfg_examples/systemd")
        exclude.add("/sap")
        exclude.add("/windows")
        exclude.add("/windows/cfg_examples")
        exclude.add("/windows/mrpe")
        exclude.add("/windows/mrpe")
        exclude.add("/windows/ohm")
        exclude.add("/windows/plugins")
        return exclude


@mode_registry.register
class ModeDownloadAgentsWindows(ABCModeDownloadAgents):
    @classmethod
    def name(cls) -> str:
        return "download_agents_windows"

    def title(self) -> str:
        return _("Windows files")

    def _packed_agents(self):
        return glob.glob(cmk.utils.paths.agents_dir + "/windows/c*.msi")

    def _walk_base_dir(self):
        return cmk.utils.paths.agents_dir + "/windows"


@mode_registry.register
class ModeDownloadAgentsLinux(ABCModeDownloadAgents):
    @classmethod
    def name(cls) -> str:
        return "download_agents_linux"

    def title(self) -> str:
        return _("Linux, Solaris, AIX files")

    def _packed_agents(self):
        return glob.glob(cmk.utils.paths.agents_dir +
                         "/*.deb") + glob.glob(cmk.utils.paths.agents_dir + "/*.rpm")

    def _walk_base_dir(self):
        return cmk.utils.paths.agents_dir

    def _exclude_file_glob_patterns(self):
        return [
            "*.hpux",
            "*.macosx",
            "*.freebsd",
            "*.openbsd",
            "*.netbsd",
            "*.openwrt",
            "*.openvms",
            "hpux_*",
        ]

    def _exclude_paths(self):
        exclude = super()._exclude_paths()
        exclude.add("/z_os")
        exclude.add("/sap")
        exclude.add("/windows")
        exclude.add("/windows/cfg_examples")
        exclude.add("/windows/mrpe")
        exclude.add("/windows/mrpe")
        exclude.add("/windows/ohm")
        exclude.add("/windows/plugins")
        return exclude
>>>>>>> upstream/master
