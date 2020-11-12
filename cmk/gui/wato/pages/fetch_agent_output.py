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
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

import abc
import ast
import os
<<<<<<< HEAD
from typing import Dict  # pylint: disable=unused-import
import six
=======
from typing import Dict
from pathlib import Path
>>>>>>> upstream/master

import cmk.utils.store as store

import cmk.gui.config as config
import cmk.gui.watolib as watolib
import cmk.gui.gui_background_job as gui_background_job
import cmk.gui.background_job as background_job

<<<<<<< HEAD
from cmk.gui.globals import html
from cmk.gui.i18n import _
from cmk.gui.pages import page_registry, Page
from cmk.gui.exceptions import (
    MKGeneralException,
    HTTPRedirect,
)
=======
from cmk.gui.globals import html, request as global_request
from cmk.gui.i18n import _
from cmk.gui.pages import page_registry, Page
from cmk.gui.escaping import escape_attribute
from cmk.gui.exceptions import MKGeneralException, HTTPRedirect, MKUserError
from cmk.gui.plugins.views.utils import make_host_breadcrumb
from cmk.gui.breadcrumb import Breadcrumb, BreadcrumbItem
>>>>>>> upstream/master
from cmk.gui.watolib import (
    automation_command_registry,
    AutomationCommand,
)
<<<<<<< HEAD
=======
from cmk.gui.utils.urls import makeuri, makeuri_contextless
>>>>>>> upstream/master

#.
#   .--Agent-Output--------------------------------------------------------.
#   |     _                    _         ___        _               _      |
#   |    / \   __ _  ___ _ __ | |_      / _ \ _   _| |_ _ __  _   _| |_    |
#   |   / _ \ / _` |/ _ \ '_ \| __|____| | | | | | | __| '_ \| | | | __|   |
#   |  / ___ \ (_| |  __/ | | | ||_____| |_| | |_| | |_| |_) | |_| | |_    |
#   | /_/   \_\__, |\___|_| |_|\__|     \___/ \__,_|\__| .__/ \__,_|\__|   |
#   |         |___/                                    |_|                 |
#   +----------------------------------------------------------------------+
#   | Page for downloading the current agent output / SNMP walk of a host  |
#   '----------------------------------------------------------------------'
# TODO: This feature is used exclusively from the GUI. Why is the code in
#       wato.py? The only reason is because the WATO automation is used. Move
#       to better location.


<<<<<<< HEAD
class FetchAgentOutputRequest(object):
    def __init__(self, host, agent_type):
        # type: (watolib.Host, str) -> None
=======
class FetchAgentOutputRequest:
    def __init__(self, host: watolib.CREHost, agent_type: str) -> None:
>>>>>>> upstream/master
        self.host = host
        self.agent_type = agent_type

    @classmethod
<<<<<<< HEAD
    def deserialize(cls, serialized):
        # type: (Dict[str, str]) -> FetchAgentOutputRequest
=======
    def deserialize(cls, serialized: Dict[str, str]) -> 'FetchAgentOutputRequest':
>>>>>>> upstream/master
        host_name = serialized["host_name"]
        host = watolib.Host.host(host_name)
        if host is None:
            raise MKGeneralException(
                _("Host %s does not exist on remote site %s. This "
                  "may be caused by a failed configuration synchronization. Have a look at "
                  "the <a href=\"wato.py?folder=&mode=changelog\">activate changes page</a> "
                  "for further information.") % (host_name, config.omd_site()))
        host.need_permission("read")

        return cls(host, serialized["agent_type"])

<<<<<<< HEAD
    def serialize(self):
        # type: () -> Dict[str, str]
=======
    def serialize(self) -> Dict[str, str]:
>>>>>>> upstream/master
        return {
            "host_name": self.host.name(),
            "agent_type": self.agent_type,
        }


# TODO: Better use AjaxPage.handle_page() for standard AJAX call error handling. This
# would need larger refactoring of the generic html.popup_trigger() mechanism.
<<<<<<< HEAD
class AgentOutputPage(six.with_metaclass(abc.ABCMeta, Page)):
    def __init__(self):
        super(AgentOutputPage, self).__init__()
        self._from_vars()

    def _from_vars(self):
=======
class AgentOutputPage(Page, metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        super(AgentOutputPage, self).__init__()
        self._from_vars()

    def _from_vars(self) -> None:
>>>>>>> upstream/master
        config.user.need_permission("wato.download_agent_output")

        host_name = html.request.var("host")
        if not host_name:
            raise MKGeneralException(_("The host is missing."))

        ty = html.request.var("type")
        if ty not in ["walk", "agent"]:
            raise MKGeneralException(_("Invalid type specified."))

        self._back_url = html.get_url_input("back_url", deflt="") or None

        watolib.init_wato_datastructures(with_wato_lock=True)

        host = watolib.Folder.current().host(host_name)
        if not host:
            raise MKGeneralException(
                _("Host is not managed by WATO. "
<<<<<<< HEAD
                  "Click <a href=\"%s\">here</a> to go back.") %
                html.escaper.escape_attribute(self._back_url))
=======
                  "Click <a href=\"%s\">here</a> to go back.") % escape_attribute(self._back_url))
>>>>>>> upstream/master
        host.need_permission("read")

        self._request = FetchAgentOutputRequest(host=host, agent_type=ty)

    @staticmethod
<<<<<<< HEAD
    def file_name(request):
        # type: (FetchAgentOutputRequest) -> str
=======
    def file_name(request: FetchAgentOutputRequest) -> str:
>>>>>>> upstream/master
        return "%s-%s-%s.txt" % (request.host.site_id(), request.host.name(), request.agent_type)


@page_registry.register_page("fetch_agent_output")
class PageFetchAgentOutput(AgentOutputPage):
<<<<<<< HEAD
    def page(self):
        html.header(_("%s: Download agent output") % self._request.host.name())

        html.begin_context_buttons()
        if self._back_url:
            html.context_button(_("Back"), self._back_url, "back")
        html.end_context_buttons()
=======
    def page(self) -> None:
        title = self._title()
        html.header(title, self._breadcrumb(title))
>>>>>>> upstream/master

        self._action()

        if html.request.has_var("_start"):
            self._start_fetch()
        self._show_status()

        html.footer()

<<<<<<< HEAD
    def _action(self):
        if not html.transaction_valid():
            return

        action_handler = gui_background_job.ActionHandler()

        if action_handler.handle_actions() and action_handler.did_delete_job():
            raise HTTPRedirect(
                html.makeuri_contextless([
                    ("host", self._request.host.name()),
                    ("type", self._request.agent_type),
                    ("back_url", self._back_url),
                ]))

    def _show_status(self):
=======
    def _title(self) -> str:
        return _("%s: Download agent output") % self._request.host.name()

    def _breadcrumb(self, title: str) -> Breadcrumb:
        breadcrumb = make_host_breadcrumb(self._request.host.name())
        breadcrumb.append(
            BreadcrumbItem(
                title=title,
                url="javascript:document.location.reload(false)",
            ))
        return breadcrumb

    def _action(self) -> None:
        if not html.transaction_valid():
            return

        action_handler = gui_background_job.ActionHandler(self._breadcrumb(self._title()))

        if action_handler.handle_actions() and action_handler.did_delete_job():
            raise HTTPRedirect(
                makeuri_contextless(
                    global_request,
                    [
                        ("host", self._request.host.name()),
                        ("type", self._request.agent_type),
                        ("back_url", self._back_url),
                    ],
                ))

    def _show_status(self) -> None:
>>>>>>> upstream/master
        job_status = self._get_job_status()

        html.h3(_("Job status"))
        if job_status["is_active"]:
<<<<<<< HEAD
            html.immediate_browser_redirect(0.8, html.makeuri([]))
=======
            html.immediate_browser_redirect(0.8, makeuri(global_request, []))
>>>>>>> upstream/master

        job = FetchAgentOutputBackgroundJob(self._request)
        gui_background_job.JobRenderer.show_job_details(job.get_job_id(), job_status)

<<<<<<< HEAD
    def _start_fetch(self):
        # type: () -> None
=======
    def _start_fetch(self) -> None:
>>>>>>> upstream/master
        """Start the job on the site the host is monitored by"""
        if config.site_is_local(self._request.host.site_id()):
            start_fetch_agent_job(self._request)
            return

        watolib.do_remote_automation(config.site(self._request.host.site_id()),
                                     "fetch-agent-output-start", [
                                         ("request", repr(self._request.serialize())),
                                     ])

<<<<<<< HEAD
    def _get_job_status(self):
        # type: () -> Dict
=======
    def _get_job_status(self) -> Dict:
>>>>>>> upstream/master
        if config.site_is_local(self._request.host.site_id()):
            return get_fetch_agent_job_status(self._request)

        return watolib.do_remote_automation(config.site(self._request.host.site_id()),
                                            "fetch-agent-output-get-status", [
                                                ("request", repr(self._request.serialize())),
                                            ])


<<<<<<< HEAD
class ABCAutomationFetchAgentOutput(six.with_metaclass(abc.ABCMeta, AutomationCommand)):
    # NOTE: This class is obviously still abstract, but pylint fails to see
    # this, even in the presence of the meta class assignment below, see
    # https://github.com/PyCQA/pylint/issues/179.

    # pylint: disable=abstract-method
    def get_request(self):
        # type: () -> FetchAgentOutputRequest
        config.user.need_permission("wato.download_agent_output")

        return FetchAgentOutputRequest.deserialize(ast.literal_eval(
            html.get_ascii_input("request")))
=======
class ABCAutomationFetchAgentOutput(AutomationCommand, metaclass=abc.ABCMeta):
    def get_request(self) -> FetchAgentOutputRequest:
        config.user.need_permission("wato.download_agent_output")

        ascii_input = html.request.get_ascii_input("request")
        if ascii_input is None:
            raise MKUserError("request", _("The parameter \"%s\" is missing.") % "request")
        return FetchAgentOutputRequest.deserialize(ast.literal_eval(ascii_input))
>>>>>>> upstream/master


@automation_command_registry.register
class AutomationFetchAgentOutputStart(ABCAutomationFetchAgentOutput):
    """Is called by AgentOutputPage._start_fetch() to execute the background job on a remote site"""
<<<<<<< HEAD
    def command_name(self):
        return "fetch-agent-output-start"

    def execute(self, request):
        # type: (FetchAgentOutputRequest) -> None
=======
    def command_name(self) -> str:
        return "fetch-agent-output-start"

    def execute(self, request: FetchAgentOutputRequest) -> None:
>>>>>>> upstream/master
        start_fetch_agent_job(request)


def start_fetch_agent_job(request):
    job = FetchAgentOutputBackgroundJob(request)
    try:
        job.start()
    except background_job.BackgroundJobAlreadyRunning:
        pass


@automation_command_registry.register
class AutomationFetchAgentOutputGetStatus(ABCAutomationFetchAgentOutput):
    """Is called by AgentOutputPage._get_job_status() to execute the background job on a remote site"""
    def command_name(self):
        return "fetch-agent-output-get-status"

<<<<<<< HEAD
    def execute(self, request):
        # type: (FetchAgentOutputRequest) -> Dict
        return get_fetch_agent_job_status(request)


def get_fetch_agent_job_status(request):
    # type: (FetchAgentOutputRequest) -> Dict
=======
    def execute(self, request: FetchAgentOutputRequest) -> Dict:
        return get_fetch_agent_job_status(request)


def get_fetch_agent_job_status(request: FetchAgentOutputRequest) -> Dict:
>>>>>>> upstream/master
    job = FetchAgentOutputBackgroundJob(request)
    return job.get_status_snapshot().get_status_as_dict()[job.get_job_id()]


@gui_background_job.job_registry.register
class FetchAgentOutputBackgroundJob(watolib.WatoBackgroundJob):
    """The background job is always executed on the site where the host is located on"""
    job_prefix = "agent-output-"

    @classmethod
<<<<<<< HEAD
    def gui_title(cls):
        return _("Fetch agent output")

    def __init__(self, request):
        # type: (FetchAgentOutputRequest) -> None
=======
    def gui_title(cls) -> str:
        return _("Fetch agent output")

    def __init__(self, request: FetchAgentOutputRequest) -> None:
>>>>>>> upstream/master
        self._request = request

        host = self._request.host
        job_id = "%s%s-%s-%s" % (self.job_prefix, host.site_id(), host.name(),
                                 self._request.agent_type)
        title = _("Fetching %s of %s / %s") % (self._request.agent_type, host.site_id(),
                                               host.name())
<<<<<<< HEAD
        super(FetchAgentOutputBackgroundJob, self).__init__(job_id, title=title, deletable=False)
=======
        super(FetchAgentOutputBackgroundJob, self).__init__(job_id, title=title)
>>>>>>> upstream/master

        self.set_function(self._fetch_agent_output)

    def _fetch_agent_output(self, job_interface):
        job_interface.send_progress_update(_("Fetching '%s'...") % self._request.agent_type)

        success, output, agent_data = watolib.check_mk_automation(
            self._request.host.site_id(), "get-agent-output",
            [self._request.host.name(), self._request.agent_type])

        if not success:
            job_interface.send_progress_update(_("Failed: %s") % output)

        preview_filepath = os.path.join(job_interface.get_work_dir(),
                                        AgentOutputPage.file_name(self._request))
        store.save_file(preview_filepath, agent_data)

<<<<<<< HEAD
        download_url = html.makeuri_contextless([("host", self._request.host.name()),
                                                 ("type", self._request.agent_type)],
                                                filename="download_agent_output.py")
=======
        download_url = makeuri_contextless(
            global_request,
            [("host", self._request.host.name()), ("type", self._request.agent_type)],
            filename="download_agent_output.py",
        )
>>>>>>> upstream/master

        button = html.render_icon_button(download_url, _("Download"), "agent_output")
        job_interface.send_progress_update(_("Finished. Click on the icon to download the data."))
        job_interface.send_result_message(_("%s Finished.") % button)


@page_registry.register_page("download_agent_output")
class PageDownloadAgentOutput(AgentOutputPage):
<<<<<<< HEAD
    def page(self):
=======
    def page(self) -> None:
>>>>>>> upstream/master
        file_name = self.file_name(self._request)
        file_content = self._get_agent_output_file()

        html.set_output_format("text")
        html.response.headers["Content-Disposition"] = "Attachment; filename=%s" % file_name
<<<<<<< HEAD
        html.write(file_content)

    def _get_agent_output_file(self):
        # type: () -> str
=======
        html.write_binary(file_content)

    def _get_agent_output_file(self) -> bytes:
>>>>>>> upstream/master
        if config.site_is_local(self._request.host.site_id()):
            return get_fetch_agent_output_file(self._request)

        return watolib.do_remote_automation(config.site(self._request.host.site_id()),
                                            "fetch-agent-output-get-file", [
                                                ("request", repr(self._request.serialize())),
                                            ])


@automation_command_registry.register
class AutomationFetchAgentOutputGetFile(ABCAutomationFetchAgentOutput):
<<<<<<< HEAD
    def command_name(self):
        return "fetch-agent-output-get-file"

    def execute(self, request):
        # type: (FetchAgentOutputRequest) -> str
        return get_fetch_agent_output_file(request)


def get_fetch_agent_output_file(request):
    # type: (FetchAgentOutputRequest) -> str
    job = FetchAgentOutputBackgroundJob(request)
    filepath = os.path.join(job.get_work_dir(), AgentOutputPage.file_name(request))
    with open(filepath) as f:
=======
    def command_name(self) -> str:
        return "fetch-agent-output-get-file"

    def execute(self, request: FetchAgentOutputRequest) -> bytes:
        return get_fetch_agent_output_file(request)


def get_fetch_agent_output_file(request: FetchAgentOutputRequest) -> bytes:
    job = FetchAgentOutputBackgroundJob(request)
    filepath = Path(job.get_work_dir(), AgentOutputPage.file_name(request))
    # The agent output need to be treated as binary data since each agent section can have an
    # individual encoding
    with filepath.open("rb") as f:
>>>>>>> upstream/master
        return f.read()
