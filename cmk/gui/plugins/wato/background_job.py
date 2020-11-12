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

import traceback

import cmk.gui.gui_background_job as gui_background_job
from cmk.gui.exceptions import HTTPRedirect
from cmk.gui.i18n import _
from cmk.gui.globals import html
from cmk.gui.log import logger

from cmk.gui.plugins.wato import (
    main_module_registry,
    MainModule,
    WatoMode,
    mode_registry,
)


@main_module_registry.register
class MainModuleBackgroundJobs(MainModule):
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import Optional, Type, Iterator
import traceback

import cmk.gui.gui_background_job as gui_background_job
from cmk.gui.i18n import _
from cmk.gui.globals import html, request
from cmk.gui.log import logger
from cmk.gui.breadcrumb import Breadcrumb
from cmk.gui.page_menu import (
    PageMenu,
    PageMenuDropdown,
    PageMenuTopic,
    PageMenuEntry,
    make_simple_link,
)

from cmk.gui.plugins.wato import (
    main_module_registry,
    ABCMainModule,
    MainModuleTopicMaintenance,
    WatoMode,
    ActionResult,
    mode_registry,
    redirect,
    mode_url,
)

from cmk.gui.utils.urls import makeuri_contextless


@main_module_registry.register
class MainModuleBackgroundJobs(ABCMainModule):
>>>>>>> upstream/master
    @property
    def mode_or_url(self):
        return "background_jobs_overview"

    @property
<<<<<<< HEAD
=======
    def topic(self):
        return MainModuleTopicMaintenance

    @property
>>>>>>> upstream/master
    def title(self):
        return _("Background jobs")

    @property
    def icon(self):
        return "background_jobs"

    @property
    def permission(self):
        return "background_jobs.manage_jobs"

    @property
    def description(self):
<<<<<<< HEAD
        return _("Manage longer running tasks in the Check_MK GUI")

    @property
    def sort_index(self):
        return 90
=======
        return _("Manage longer running tasks in the Checkmk GUI")

    @property
    def sort_index(self):
        return 60

    @property
    def is_show_more(self):
        return True
>>>>>>> upstream/master


@mode_registry.register
class ModeBackgroundJobsOverview(WatoMode):
    @classmethod
    def name(cls):
        return "background_jobs_overview"

    @classmethod
    def permissions(cls):
        return ["background_jobs.manage_jobs"]

    def title(self):
        return _("Background jobs overview")

    def page(self):
        job_manager = gui_background_job.GUIBackgroundJobManager()

<<<<<<< HEAD
        back_url = html.makeuri_contextless([("mode", "background_jobs_overview")])
=======
        back_url = makeuri_contextless(request, [("mode", "background_jobs_overview")])
>>>>>>> upstream/master
        job_manager.show_status_of_job_classes(gui_background_job.job_registry.values(),
                                               job_details_back_url=back_url)

        if any(
                job_manager.get_running_job_ids(c)
                for c in gui_background_job.job_registry.values()):
            html.immediate_browser_redirect(0.8, "")

<<<<<<< HEAD
    def action(self):
        action_handler = gui_background_job.ActionHandler()
        action_handler.handle_actions()
=======
    # Mypy requires the explicit return, pylint does not like it.
    def action(self) -> ActionResult:  # pylint: disable=useless-return
        action_handler = gui_background_job.ActionHandler(self.breadcrumb())
        action_handler.handle_actions()
        return None
>>>>>>> upstream/master


@mode_registry.register
class ModeBackgroundJobDetails(WatoMode):
    @classmethod
    def name(cls):
        return "background_job_details"

    @classmethod
    def permissions(cls):
        return []

<<<<<<< HEAD
    def title(self):
        return _("Background job details")

    def buttons(self):
        if self._back_url():
            html.context_button(_("Back"), self._back_url(), "back")
=======
    @classmethod
    def parent_mode(cls) -> Optional[Type[WatoMode]]:
        return ModeBackgroundJobsOverview

    def title(self):
        return _("Background job details")

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
        back_url = self._back_url()
        # Small hack to not have a "up" and "back" link both pointing to the parent mode
        if back_url and "mode=background_jobs_overview" not in back_url:
            yield PageMenuEntry(
                title=_("Back"),
                icon_name="back",
                item=make_simple_link(back_url),
                is_shortcut=True,
                is_suggested=True,
            )
>>>>>>> upstream/master

    def _back_url(self):
        return html.get_url_input("back_url", deflt="")

    def page(self):
        job_id = html.request.var("job_id")

        job = gui_background_job.GUIBackgroundJob(job_id)
        if not job.exists():
<<<<<<< HEAD
            html.message(_("Background job info is not available"))
=======
            html.show_message(_("Background job info is not available"))
>>>>>>> upstream/master
            return

        try:
            # Race condition, the job might get deleted during snapshot generation
            job_snapshot = job.get_status_snapshot()
        except Exception:
<<<<<<< HEAD
            html.message(_("Background job info is not available"))
=======
            html.show_message(_("Background job info is not available"))
>>>>>>> upstream/master
            logger.error(traceback.format_exc())
            return

        job_manager = gui_background_job.GUIBackgroundJobManager()
        job_manager.show_job_details_from_snapshot(job_snapshot)
        if job_snapshot.is_active():
            html.immediate_browser_redirect(1, "")

<<<<<<< HEAD
    def action(self):
        action_handler = gui_background_job.ActionHandler()
        action_handler.handle_actions()
        if action_handler.did_delete_job():
            if self._back_url():
                raise HTTPRedirect(self._back_url())
            return "background_jobs_overview"
=======
    def action(self) -> ActionResult:
        action_handler = gui_background_job.ActionHandler(self.breadcrumb())
        action_handler.handle_actions()
        if action_handler.did_delete_job():
            if self._back_url():
                raise redirect(self._back_url())
            return redirect(mode_url("background_jobs_overview"))
        return None
>>>>>>> upstream/master
