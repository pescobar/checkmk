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

import time
import copy
import json
<<<<<<< HEAD
from typing import (  # pylint: disable=unused-import
    Any, Dict, Optional,
)
import six
=======
from typing import cast, Set, Dict, Optional, Tuple, Type, List, Union, Callable, Iterator

from six import ensure_str

import cmk.utils.version as cmk_version
from cmk.gui.utils.html import HTML
from cmk.utils.exceptions import MKException
>>>>>>> upstream/master

import cmk.gui.pages
import cmk.gui.notify as notify
import cmk.gui.config as config
import cmk.gui.visuals as visuals
<<<<<<< HEAD
import cmk.gui.watolib as watolib
import cmk.gui.forms as forms
import cmk.gui.utils as utils
from cmk.gui.valuespec import (
    Transform,
    Dictionary,
    TextUnicode,
    DropdownChoice,
    Checkbox,
    FixedValue,
)
import cmk.gui.i18n
from cmk.gui.i18n import _u, _
from cmk.gui.log import logger
from cmk.gui.globals import html
=======
import cmk.gui.forms as forms
import cmk.gui.utils as utils
import cmk.gui.crash_reporting as crash_reporting
from cmk.gui.type_defs import InfoName, VisualContext
from cmk.gui.valuespec import (
    Transform,
    Dictionary,
    DropdownChoice,
    Checkbox,
)
from cmk.gui.valuespec import ValueSpec, ValueSpecValidateFunc, DictionaryEntry
import cmk.gui.i18n
from cmk.gui.i18n import _
from cmk.gui.log import logger
from cmk.gui.globals import html, request
from cmk.gui.pagetypes import PagetypeTopics
from cmk.gui.main_menu import mega_menu_registry
from cmk.gui.views import ABCAjaxInitialFilters
from cmk.gui.pages import page_registry
from cmk.gui.breadcrumb import (
    make_topic_breadcrumb,
    Breadcrumb,
    BreadcrumbItem,
    make_current_page_breadcrumb_item,
)
from cmk.gui.page_menu import (
    PageMenu,
    PageMenuDropdown,
    PageMenuTopic,
    PageMenuEntry,
    PageMenuSidePopup,
    make_simple_link,
    make_simple_form_page_menu,
    make_javascript_link,
    make_display_options_dropdown,
)
>>>>>>> upstream/master

from cmk.gui.exceptions import (
    HTTPRedirect,
    MKGeneralException,
    MKAuthException,
    MKUserError,
)
from cmk.gui.permissions import (
    declare_permission,
    permission_section_registry,
    PermissionSection,
)
from cmk.gui.plugins.visuals.utils import (
    visual_info_registry,
    visual_type_registry,
    VisualType,
)

import cmk.gui.plugins.dashboard

<<<<<<< HEAD
if not cmk.is_raw_edition():
    import cmk.gui.cee.plugins.dashboard

if cmk.is_managed_edition():
    import cmk.gui.cme.plugins.dashboard

from cmk.gui.plugins.views.utils import (
    data_source_registry,
    get_permitted_views,
    get_all_views,
)
from cmk.gui.plugins.dashboard.utils import (
    builtin_dashboards,
    GROW,
    MAX,
    dashlet_types,
    dashlet_registry,
    Dashlet,
)

loaded_with_language = False
builtin_dashboards_transformed = False
=======
if not cmk_version.is_raw_edition():
    import cmk.gui.cee.plugins.dashboard  # pylint: disable=no-name-in-module

if cmk_version.is_managed_edition():
    import cmk.gui.cme.plugins.dashboard  # pylint: disable=no-name-in-module

from cmk.gui.plugins.views.utils import data_source_registry
from cmk.gui.plugins.dashboard.utils import (builtin_dashboards, GROW, dashlet_types,
                                             dashlet_registry, Dashlet, get_all_dashboards,
                                             save_all_dashboards, get_permitted_dashboards,
                                             copy_view_into_dashlet, dashboard_breadcrumb,
                                             dashlet_vs_general_settings)
# Can be used by plugins
from cmk.gui.plugins.dashboard.utils import (  # noqa: F401 # pylint: disable=unused-import
    DashletType, DashletTypeName, DashletRefreshInterval, DashletRefreshAction, DashletConfig,
    DashboardConfig, DashboardName, DashletSize, DashletInputFunc, DashletHandleInputFunc,
    DashletId,
)
from cmk.gui.plugins.metrics.html_render import title_info_elements, render_title_elements
from cmk.gui.node_visualization import get_topology_view_and_filters

from cmk.gui.utils.urls import makeuri, makeuri_contextless

loaded_with_language: Union[None, bool, str] = False
>>>>>>> upstream/master

# These settings might go into the config module, sometime in future,
# in order to allow the user to customize this.

<<<<<<< HEAD
screen_margin = 5  # Distance from the left border of the main-frame to the dashboard area
dashlet_padding = 34, 4, -2, 4, 4  # Margin (N, E, S, W, N w/o title) between outer border of dashlet and its content
#dashlet_padding  = 23, 2, 2, 2, 2 # Margin (N, E, S, W, N w/o title) between outer border of dashlet and its content
=======
screen_margin = 12  # Distance from the left border of the main-frame to the dashboard area
dashlet_padding = 26, 4, 4, 4, 4  # Margin (N, E, S, W, N w/o title) between outer border of dashlet and its content
>>>>>>> upstream/master
raster = 10  # Raster the dashlet coords are measured in (px)


@visual_type_registry.register
class VisualTypeDashboards(VisualType):
    @property
    def ident(self):
        return "dashboards"

    @property
    def title(self):
        return _("dashboard")

    @property
    def plural_title(self):
        return _("dashboards")

    @property
    def ident_attr(self):
        return "name"

    @property
    def multicontext_links(self):
        return False

    @property
    def show_url(self):
        return "dashboard.py"

<<<<<<< HEAD
    def popup_add_handler(self, add_type):
        if not config.user.may("general.edit_dashboards"):
            return []
=======
    def page_menu_add_to_entries(self, add_type: str) -> Iterator[PageMenuEntry]:
        if not config.user.may("general.edit_dashboards"):
            return
>>>>>>> upstream/master

        if add_type in ["availability", "graph_collection"]:
            return

<<<<<<< HEAD
        load_dashboards()
        return [(name, board["title"]) for (name, board) in available_dashboards.items()]
=======
        for name, board in get_permitted_dashboards().items():
            yield PageMenuEntry(
                title=board["title"],
                icon_name="dashboard",
                item=make_javascript_link("cmk.popup_menu.add_to_visual('dashboards', %s)" %
                                          json.dumps(name)),
            )
>>>>>>> upstream/master

    def add_visual_handler(self, target_visual_name, add_type, context, parameters):
        if not config.user.may("general.edit_dashboards"):
            # Exceptions do not work here.
            return

        if add_type == "pnpgraph" and context is None:
            # Raw Edition graphs are added correctly by htdocs/js/checkmk.js create_pnp_graph().
            # Enterprise Edition graphs:
            #
            # Context will always be None here, but the specification (in parameters)
            # will contain it. Transform the data to the format needed by the dashlets.
            #
            # Example:
            # parameters = [ 'template', {'service_description': 'CPU load', 'site': 'mysite',
            #                         'graph_index': 0, 'host_name': 'server123'}])
            specification = parameters["definition"]["specification"]
            if specification[0] == "template":
                context = {"host": specification[1]["host_name"]}
                if specification[1].get("service_description") != "_HOST_":
                    context["service"] = specification[1]["service_description"]
                parameters = {"source": specification[1]["graph_index"] + 1}

            elif specification[0] == "custom":
                # Override the dashlet type here. It would be better to get the
                # correct dashlet type from the menu. But this does not seem to
                # be a trivial change.
                add_type = "custom_graph"
                context = {}
                parameters = {
                    "custom_graph": specification[1],
                }

            else:
<<<<<<< HEAD
                raise MKGeneralException(_("Invalid graph type '%s'") % specification[0])

        load_dashboards(lock=True)

        if target_visual_name not in available_dashboards:
            return
        dashboard = load_dashboard_with_cloning(target_visual_name)

        dashlet = default_dashlet_definition(add_type)

        dashlet["context"] = context
        if add_type == 'view':
            view_name = parameters['name']
        else:
            dashlet.update(parameters)
=======
                raise MKGeneralException(
                    _("Graph specification '%s' is insuficient for Dashboard. "
                      "Please save your graph as a custom graph first, then "
                      'add that one to the dashboard.') % specification[0])

        permitted_dashboards = get_permitted_dashboards()
        dashboard = _load_dashboard_with_cloning(permitted_dashboards, target_visual_name)

        dashlet_spec = default_dashlet_definition(add_type)

        dashlet_spec["context"] = context
        if add_type == 'view':
            view_name = parameters['name']
        else:
            dashlet_spec.update(parameters)
>>>>>>> upstream/master

        # When a view shal be added to the dashboard, load the view and put it into the dashlet
        # FIXME: Mave this to the dashlet plugins
        if add_type == 'view':
            # save the original context and override the context provided by the view
<<<<<<< HEAD
            context = dashlet['context']
            load_view_into_dashlet(dashlet,
=======
            context = dashlet_spec['context']
            copy_view_into_dashlet(dashlet_spec,
>>>>>>> upstream/master
                                   len(dashboard['dashlets']),
                                   view_name,
                                   add_context=context)

        elif add_type in ["pnpgraph", "custom_graph"]:
            # The "add to visual" popup does not provide a timerange information,
            # but this is not an optional value. Set it to 25h initially.
<<<<<<< HEAD
            dashlet.setdefault("timerange", "1")

        add_dashlet(dashlet, dashboard)
=======
            dashlet_spec.setdefault("timerange", "1")

        add_dashlet(dashlet_spec, dashboard)
>>>>>>> upstream/master

        # Directly go to the dashboard in edit mode. We send the URL as an answer
        # to the AJAX request
        html.write('OK dashboard.py?name=' + target_visual_name + '&edit=1')

    def load_handler(self):
<<<<<<< HEAD
        load_dashboards()

    @property
    def permitted_visuals(self):
        return permitted_dashboards()
=======
        pass

    @property
    def permitted_visuals(self):
        return get_permitted_dashboards()
>>>>>>> upstream/master


@permission_section_registry.register
class PermissionSectionDashboard(PermissionSection):
    @property
    def name(self):
        return "dashboard"

    @property
    def title(self):
        return _("Dashboards")

    @property
    def do_sort(self):
        return True


# Load plugins in web/plugins/dashboard and declare permissions,
# note: these operations produce language-specific results and
# thus must be reinitialized everytime a language-change has
# been detected.
<<<<<<< HEAD
def load_plugins(force):
    global loaded_with_language, dashboards, builtin_dashboards_transformed
=======
def load_plugins(force: bool) -> None:
    global loaded_with_language
>>>>>>> upstream/master
    if loaded_with_language == cmk.gui.i18n.get_current_language() and not force:
        return

    # Load plugins for dashboards. Currently these files
    # just may add custom dashboards by adding to builtin_dashboards.
<<<<<<< HEAD
    builtin_dashboards_transformed = False
=======
>>>>>>> upstream/master
    utils.load_web_plugins("dashboard", globals())

    _transform_old_dict_based_dashlets()

    # This must be set after plugin loading to make broken plugins raise
    # exceptions all the time and not only the first time (when the plugins
    # are loaded).
    loaded_with_language = cmk.gui.i18n.get_current_language()

<<<<<<< HEAD
    # Clear this structure to prevent users accessing dashboard structures created
    # by other users, make them see these dashboards
    dashboards = {}

=======
>>>>>>> upstream/master
    visuals.declare_visual_permissions('dashboards', _("dashboards"))

    # Declare permissions for all dashboards
    for name, board in builtin_dashboards.items():
        declare_permission(
            "dashboard.%s" % name,
            board["title"],
            board.get("description", ""),
            config.builtin_role_ids,
        )

    # Make sure that custom views also have permissions
    config.declare_dynamic_permissions(lambda: visuals.declare_custom_permissions('dashboards'))


class LegacyDashlet(cmk.gui.plugins.dashboard.IFrameDashlet):
    """Helper to be able to handle pre 1.6 dashlet_type declared dashlets"""
<<<<<<< HEAD
    _type_name = ""
    _spec = {}  # type: Dict[str, Any]

    @classmethod
    def type_name(cls):
        return cls._type_name

    @classmethod
    def title(cls):
        return cls._spec["title"]

    @classmethod
    def description(cls):
        return cls._spec["description"]

    @classmethod
    def sort_index(cls):
        return cls._spec["sort_index"]

    @classmethod
    def infos(cls):
        return cls._spec.get("infos", [])

    @classmethod
    def single_infos(cls):
        return cls._spec.get("single_infos", [])

    @classmethod
    def is_selectable(cls):
        return cls._spec.get("selectable", True)

    @classmethod
    def is_resizable(cls):
        return cls._spec.get("resizable", True)

    @classmethod
    def is_iframe_dashlet(cls):
        return "iframe_render" in cls._spec or "iframe_urlfunc" in cls._spec

    @classmethod
    def initial_size(cls):
        return cls._spec.get("size", Dashlet.minimum_size)

    @classmethod
    def vs_parameters(cls):
        return cls._spec.get("parameters", None)

    @classmethod
    def opt_parameters(cls):
        """List of optional parameters in case vs_parameters() returns a list"""
        return cls._spec.get("opt_params")

    @classmethod
    def validate_parameters_func(cls):
=======
    _type_name: DashletTypeName = ""
    _spec: DashletConfig = {}

    @classmethod
    def type_name(cls) -> str:
        return cls._type_name

    @classmethod
    def title(cls) -> str:
        return cls._spec["title"]

    @classmethod
    def description(cls) -> str:
        return cls._spec["description"]

    @classmethod
    def sort_index(cls) -> int:
        return cls._spec["sort_index"]

    @classmethod
    def single_infos(cls) -> List[str]:
        return cls._spec.get("single_infos", [])

    @classmethod
    def is_selectable(cls) -> bool:
        return cls._spec.get("selectable", True)

    @classmethod
    def is_resizable(cls) -> bool:
        return cls._spec.get("resizable", True)

    @classmethod
    def is_iframe_dashlet(cls) -> bool:
        return "iframe_render" in cls._spec or "iframe_urlfunc" in cls._spec

    @classmethod
    def initial_size(cls) -> DashletSize:
        return cls._spec.get("size", Dashlet.minimum_size)

    @classmethod
    def vs_parameters(
        cls
    ) -> Union[None, List[DictionaryEntry], ValueSpec, Tuple[DashletInputFunc,
                                                             DashletHandleInputFunc]]:
        return cls._spec.get("parameters", None)

    @classmethod
    def opt_parameters(cls) -> Union[bool, List[str]]:
        """List of optional parameters in case vs_parameters() returns a list"""
        return cls._spec.get("opt_params", False)

    @classmethod
    def validate_parameters_func(cls) -> Optional[ValueSpecValidateFunc]:
>>>>>>> upstream/master
        """Optional validation function in case vs_parameters() returns a list"""
        return cls._spec.get("validate_params")

    @classmethod
<<<<<<< HEAD
    def initial_refresh_interval(cls):
        return cls._spec.get("refresh", False)

    @classmethod
    def allowed_roles(cls):
        return cls._spec.get("allowed", config.builtin_role_ids)

    @classmethod
    def styles(cls):
        return cls._spec.get("styles")

    @classmethod
    def script(cls):
        return cls._spec.get("script")

    @classmethod
    def add_url(cls):
=======
    def initial_refresh_interval(cls) -> DashletRefreshInterval:
        return cls._spec.get("refresh", False)

    @classmethod
    def allowed_roles(cls) -> List[str]:
        return cls._spec.get("allowed", config.builtin_role_ids)

    @classmethod
    def styles(cls) -> Optional[str]:
        return cls._spec.get("styles")

    @classmethod
    def script(cls) -> Optional[str]:
        return cls._spec.get("script")

    @classmethod
    def add_url(cls) -> str:
>>>>>>> upstream/master
        if "add_urlfunc" in cls._spec:
            return cls._spec["add_urlfunc"]()
        return super(LegacyDashlet, cls).add_url()

<<<<<<< HEAD
    def display_title(self):
=======
    def infos(self) -> List[str]:
        return self._spec.get("infos", [])

    def display_title(self) -> str:
>>>>>>> upstream/master
        title_func = self._spec.get("title_func")
        if title_func:
            return title_func(self._dashlet_spec)
        return self.title()

<<<<<<< HEAD
    def on_resize(self):
=======
    def on_resize(self) -> Optional[str]:
>>>>>>> upstream/master
        on_resize_func = self._spec.get("on_resize")
        if on_resize_func:
            return on_resize_func(self._dashlet_id, self._dashlet_spec)
        return None

<<<<<<< HEAD
    def on_refresh(self):
=======
    def on_refresh(self) -> Optional[str]:
>>>>>>> upstream/master
        on_refresh_func = self._spec.get("on_refresh")
        if on_refresh_func:
            return on_refresh_func(self._dashlet_id, self._dashlet_spec)
        return None

<<<<<<< HEAD
    def update(self):
=======
    def update(self) -> None:
>>>>>>> upstream/master
        if self.is_iframe_dashlet():
            self._spec['iframe_render'](self._dashlet_id, self._dashlet_spec)
        else:
            self._spec['render'](self._dashlet_id, self._dashlet_spec)

<<<<<<< HEAD
    def show(self):
=======
    def show(self) -> None:
>>>>>>> upstream/master
        if "render" in self._spec:
            self._spec['render'](self._dashlet_id, self._dashlet_spec)

        elif self.is_iframe_dashlet():
            self._show_initial_iframe_container()

<<<<<<< HEAD
    def _get_iframe_url(self):
        # type: () -> Optional[str]
=======
    def _get_iframe_url(self) -> Optional[str]:
>>>>>>> upstream/master
        if not self.is_iframe_dashlet():
            return None

        if "iframe_urlfunc" in self._spec:
            # Optional way to render a dynamic iframe URL
            url = self._spec["iframe_urlfunc"](self._dashlet_spec)
            return url

        return super(LegacyDashlet, self)._get_iframe_url()


<<<<<<< HEAD
# Pre Check_MK 1.6 the dashlets were declared with dictionaries like this:
=======
# Pre Checkmk 1.6 the dashlets were declared with dictionaries like this:
>>>>>>> upstream/master
#
# dashlet_types["hoststats"] = {
#     "title"       : _("Host Statistics"),
#     "sort_index"  : 45,
#     "description" : _("Displays statistics about host states as globe and a table."),
#     "render"      : dashlet_hoststats,
#     "refresh"     : 60,
#     "allowed"     : config.builtin_role_ids,
#     "size"        : (30, 18),
#     "resizable"   : False,
# }
#
# Convert it to objects to be compatible
# TODO: Deprecate this one day.
<<<<<<< HEAD
def _transform_old_dict_based_dashlets():
=======
def _transform_old_dict_based_dashlets() -> None:
>>>>>>> upstream/master
    for dashlet_type_id, dashlet_spec in dashlet_types.items():

        @dashlet_registry.register
        class LegacyDashletType(LegacyDashlet):
            _type_name = dashlet_type_id
            _spec = dashlet_spec

<<<<<<< HEAD
        _it_is_really_used = LegacyDashletType  # help pylint


dashboards = {}  # type: Dict
available_dashboards = {}  # type: Dict


def load_dashboards(lock=False):
    global dashboards, available_dashboards
    transform_builtin_dashboards()
    dashboards = visuals.load('dashboards', builtin_dashboards, lock=lock)
    transform_dashboards(dashboards)
    available_dashboards = visuals.available('dashboards', dashboards)


# During implementation of the dashboard editor and recode of the visuals
# we had serveral different data structures, for example one where the
# views in user dashlets were stored with a context_type instead of the
# "single_info" key, which is the currently correct one.
#
# This code transforms views from user_dashboards.mk which have been
# migrated/created with daily snapshots from 2014-08 till beginning 2014-10.
# FIXME: Can be removed one day. Mark as incompatible change or similar.
def transform_dashboards(boards):
    for dashboard in boards.itervalues():
        visuals.transform_old_visual(dashboard)

        # Also transform dashlets
        for dashlet in dashboard['dashlets']:
            visuals.transform_old_visual(dashlet)

            if dashlet['type'] == 'pnpgraph':
                if 'service' not in dashlet['single_infos']:
                    dashlet['single_infos'].append('service')
                if 'host' not in dashlet['single_infos']:
                    dashlet['single_infos'].append('host')


# be compatible to old definitions, where even internal dashlets were
# referenced by url, e.g. dashboard['url'] = 'hoststats.py'
# FIXME: can be removed one day. Mark as incompatible change or similar.
def transform_builtin_dashboards():
    global builtin_dashboards_transformed
    if builtin_dashboards_transformed:
        return  # Only do this once
    for name, dashboard in builtin_dashboards.items():
        # Do not transform dashboards which are already in the new format
        if 'context' in dashboard:
            continue

        # Transform the dashlets
        for nr, dashlet in enumerate(dashboard['dashlets']):
            dashlet.setdefault('show_title', True)

            if dashlet.get('url', '').startswith('dashlet_hoststats') or \
                dashlet.get('url', '').startswith('dashlet_servicestats'):

                # hoststats and servicestats
                dashlet['type'] = dashlet['url'][8:].split('.', 1)[0]

                if '?' in dashlet['url']:
                    # Transform old parameters:
                    # wato_folder
                    # host_contact_group
                    # service_contact_group
                    paramstr = dashlet['url'].split('?', 1)[1]
                    dashlet['context'] = {}
                    for key, val in [p.split('=', 1) for p in paramstr.split('&')]:
                        if key == 'host_contact_group':
                            dashlet['context']['opthost_contactgroup'] = {
                                'neg_opthost_contact_group': '',
                                'opthost_contact_group': val,
                            }
                        elif key == 'service_contact_group':
                            dashlet['context']['optservice_contactgroup'] = {
                                'neg_optservice_contact_group': '',
                                'optservice_contact_group': val,
                            }
                        elif key == 'wato_folder':
                            dashlet['context']['wato_folder'] = {
                                'wato_folder': val,
                            }

                del dashlet['url']

            elif dashlet.get('urlfunc') and not isinstance(dashlet['urlfunc'], str):
                raise MKGeneralException(
                    _('Unable to transform dashlet %d of dashboard %s: '
                      'the dashlet is using "urlfunc" which can not be '
                      'converted automatically.') % (nr, name))

            elif dashlet.get('url', '') != '' or dashlet.get('urlfunc') or dashlet.get('iframe'):
                # Normal URL based dashlet
                dashlet['type'] = 'url'

                if dashlet.get('iframe'):
                    dashlet['url'] = dashlet['iframe']
                    del dashlet['iframe']

            elif dashlet.get('view', '') != '':
                # Transform views
                # There might be more than the name in the view definition
                view_name = dashlet['view'].split('&')[0]

                # Copy the view definition into the dashlet
                load_view_into_dashlet(dashlet, nr, view_name, load_from_all_views=True)
                del dashlet['view']

            else:
                raise MKGeneralException(
                    _('Unable to transform dashlet %d of dashboard %s. '
                      'You will need to migrate it on your own. Definition: %r') %
                    (nr, name, html.attrencode(dashlet)))

            dashlet.setdefault('context', {})
            dashlet.setdefault('single_infos', [])

        # the modification time of builtin dashboards can not be checked as on user specific
        # dashboards. Set it to 0 to disable the modification chech.
        dashboard.setdefault('mtime', 0)

        dashboard.setdefault('show_title', True)
        if dashboard['title'] is None:
            dashboard['title'] = _('No title')
            dashboard['show_title'] = False

        dashboard.setdefault('single_infos', [])
        dashboard.setdefault('context', {})
        dashboard.setdefault('topic', _('Overview'))
        dashboard.setdefault('description', dashboard.get('title', ''))
    builtin_dashboards_transformed = True


def load_view_into_dashlet(dashlet, nr, view_name, add_context=None, load_from_all_views=False):
    permitted_views = get_permitted_views()

    # it is random which user is first accessing
    # an apache python process, initializing the dashboard loading and conversion of
    # old dashboards. In case of the conversion we really try hard to make the conversion
    # work in all cases. So we need all views instead of the views of the user.
    if load_from_all_views and view_name not in permitted_views:
        # This is not really 100% correct according to the logic of visuals.available(),
        # but we do this for the rare edge case during legacy dashboard conversion, so
        # this should be sufficient
        view = None
        for (_u, n), this_view in get_all_views().iteritems():
            # take the first view with a matching name
            if view_name == n:
                view = this_view
                break

        if not view:
            raise MKGeneralException(
                _("Failed to convert a builtin dashboard which is referencing "
                  "the view \"%s\". You will have to migrate it to the new "
                  "dashboard format on your own to work properly.") % view_name)
    else:
        view = permitted_views[view_name]

    view = copy.deepcopy(view)  # Clone the view
    dashlet.update(view)
    if add_context:
        dashlet['context'].update(add_context)

    # Overwrite the views default title with the context specific title
    dashlet['title'] = visuals.visual_title('view', view)
    dashlet['title_url'] = html.makeuri_contextless([('view_name', view_name)] +
                                                    visuals.get_singlecontext_vars(view).items(),
                                                    filename='view.py')

    dashlet['type'] = 'view'
    dashlet['name'] = 'dashlet_%d' % nr
    dashlet['show_title'] = True
    dashlet['mustsearch'] = False


def save_dashboards(us):
    visuals.save('dashboards', dashboards)


def permitted_dashboards():
    return available_dashboards
=======
        # help pylint
        _it_is_really_used = LegacyDashletType  # noqa: F841
>>>>>>> upstream/master


# HTML page handler for generating the (a) dashboard. The name
# of the dashboard to render is given in the HTML variable 'name'.
# This defaults to "main".
@cmk.gui.pages.register("dashboard")
<<<<<<< HEAD
def page_dashboard():
    load_dashboards()

=======
def page_dashboard() -> None:
>>>>>>> upstream/master
    name = html.request.var("name")
    if not name:
        name = "main"
        html.request.set_var("name", name)  # make sure that URL context is always complete
<<<<<<< HEAD
    if name not in available_dashboards:
=======
    if name not in get_permitted_dashboards():
>>>>>>> upstream/master
        raise MKUserError("name", _('The requested dashboard does not exist.'))

    draw_dashboard(name)


<<<<<<< HEAD
def load_dashboard_with_cloning(name, edit=True):
    board = available_dashboards[name]
=======
def _load_dashboard_with_cloning(permitted_dashboards: Dict[DashboardName, DashboardConfig],
                                 name: DashboardName,
                                 edit: bool = True) -> DashboardConfig:
    board = permitted_dashboards[name]
>>>>>>> upstream/master
    if edit and board['owner'] != config.user.id:
        # This dashboard which does not belong to the current user is about to
        # be edited. In order to make this possible, the dashboard is being
        # cloned now!
        board = copy.deepcopy(board)
        board['owner'] = config.user.id
        board['public'] = False

<<<<<<< HEAD
        dashboards[(config.user.id, name)] = board
        available_dashboards[name] = board
        visuals.save('dashboards', dashboards)
=======
        all_dashboards = get_all_dashboards()
        all_dashboards[(config.user.id, name)] = board
        permitted_dashboards[name] = board
        save_all_dashboards()
>>>>>>> upstream/master

    return board


# Actual rendering function
<<<<<<< HEAD
def draw_dashboard(name):
=======
def draw_dashboard(name: DashboardName) -> None:
>>>>>>> upstream/master
    mode = 'display'
    if html.request.var('edit') == '1':
        mode = 'edit'

    if mode == 'edit' and not config.user.may("general.edit_dashboards"):
        raise MKAuthException(_("You are not allowed to edit dashboards."))

<<<<<<< HEAD
    board = load_dashboard_with_cloning(name, edit=mode == 'edit')

    # The dashboard may be called with "wato_folder" set. In that case
    # the dashboard is assumed to restrict the shown data to a specific
    # WATO subfolder or file. This could be a configurable feature in
    # future, but currently we assume, that *all* dashboards are filename
    # sensitive.
    wato_folder = html.request.var("wato_folder")
=======
    permitted_dashboards = get_permitted_dashboards()
    board = _load_dashboard_with_cloning(permitted_dashboards, name, edit=mode == 'edit')
    board = _add_context_to_dashboard(board)

    # Like _dashboard_info_handler we assume that only host / service filters are relevant
    board_context = visuals.get_merged_context(
        visuals.get_context_from_uri_vars(["host", "service"], board["single_infos"]),
        board["context"])
>>>>>>> upstream/master

    title = visuals.visual_title('dashboard', board)

    # Distance from top of the screen to the lower border of the heading
<<<<<<< HEAD
    header_height = 55

    # The title of the dashboard needs to be prefixed with the WATO path,
    # in order to make it clear to the user, that he is seeing only partial
    # data.
=======
    header_height = 104

>>>>>>> upstream/master
    if not board.get('show_title'):
        # Remove the whole header line
        html.set_render_headfoot(False)
        header_height = 0

<<<<<<< HEAD
    elif wato_folder is not None:
        title = watolib.get_folder_title(wato_folder) + " - " + title

    html.add_body_css_class("dashboard")
    html.header(title)
=======
    # In case we have a dashboard / dashlet that requires context information that is not available
    # yet, display a message to the user to insert the missing information.
    missing_mandatory_context_filters = not set(board_context.keys()).issuperset(
        set(board["mandatory_context_filters"]))

    dashlets = _get_dashlets(name, board)

    missing_single_infos: Set[InfoName] = set()
    unconfigured_single_infos: Set[InfoName] = set()
    for dashlet in dashlets:
        missing_single_infos.update(dashlet.missing_single_infos())
        unconfigured_single_infos.update(dashlet.unconfigured_single_infos())

    html.add_body_css_class("dashboard")
    breadcrumb = dashboard_breadcrumb(name, board, title)
    html.header(title,
                breadcrumb=breadcrumb,
                page_menu=_page_menu(breadcrumb, name, board, board_context,
                                     unconfigured_single_infos, mode))
>>>>>>> upstream/master

    html.open_div(class_=["dashboard_%s" % name], id_="dashboard")  # Container of all dashlets

    dashlet_javascripts(board)
    dashlet_styles(board)

<<<<<<< HEAD
    refresh_dashlets = []  # Dashlets with automatic refresh, for Javascript
    dashlet_coords = []  # Dimensions and positions of dashlet
    on_resize_dashlets = {}  # javascript function to execute after ressizing the dashlet
    for nr, dashlet in enumerate(board["dashlets"]):
        dashlet_content_html = ""
        dashlet_title_html = ""
        try:
            dashlet_type = get_dashlet_type(dashlet)
            dashlet_instance = dashlet_type(name, board, nr, dashlet, wato_folder)

            refresh = get_dashlet_refresh(dashlet_instance)
            if refresh:
                refresh_dashlets.append(refresh)

            on_resize = get_dashlet_on_resize(dashlet_instance)
            if on_resize:
                on_resize_dashlets[nr] = on_resize

            dashlet_title_html = render_dashlet_title_html(dashlet_instance)
            dashlet_content_html = render_dashlet_content(dashlet_instance, is_update=False)

        except Exception as e:
            dashlet_content_html = render_dashlet_exception_content(dashlet_instance, nr, e)

        # Now after the dashlet content has been calculated render the whole dashlet
        dashlet_container_begin(nr, dashlet)
        draw_dashlet(dashlet_instance, dashlet_content_html, dashlet_title_html)
        dashlet_container_end()
        dashlet_coords.append(get_dashlet_dimensions(dashlet_instance))

    dashboard_edit_controls(name, board)

    dashboard_properties = {
        "MAX": MAX,
=======
    for dashlet in dashlets:
        dashlet_title, content = _render_dashlet(
            board,
            dashlet,
            is_update=False,
            mtime=board["mtime"],
            missing_mandatory_context_filters=missing_mandatory_context_filters,
        )

        # Now after the dashlet content has been calculated render the whole dashlet
        dashlet_container_begin(dashlet)
        draw_dashlet(dashlet, content, dashlet_title)
        dashlet_container_end()

    # Display the dialog during initial rendering when required context information is missing.
    if missing_single_infos or missing_mandatory_context_filters:
        html.final_javascript("cmk.page_menu.open_popup('popup_filters');")

    html.close_div()

    dashboard_properties = {
>>>>>>> upstream/master
        "GROW": GROW,
        "grid_size": raster,
        "header_height": header_height,
        "screen_margin": screen_margin,
        "dashlet_padding": dashlet_padding,
        "dashlet_min_size": Dashlet.minimum_size,
<<<<<<< HEAD
        "refresh_dashlets": refresh_dashlets,
        "on_resize_dashlets": on_resize_dashlets,
        "dashboard_name": name,
        "dashboard_mtime": board['mtime'],
        "dashlets": dashlet_coords,
=======
        "refresh_dashlets": _get_refresh_dashlets(dashlets),
        "on_resize_dashlets": _get_resize_dashlets(dashlets),
        "dashboard_name": name,
        "dashboard_mtime": board['mtime'],
        "dashlets": _get_dashlet_coords(dashlets),
>>>>>>> upstream/master
    }

    html.javascript("""
cmk.dashboard.set_dashboard_properties(%s);
cmk.dashboard.calculate_dashboard();
window.onresize = function () { cmk.dashboard.calculate_dashboard(); }
cmk.dashboard.execute_dashboard_scheduler(1);
cmk.dashboard.register_event_handlers();
    """ % json.dumps(dashboard_properties))

    if mode == 'edit':
<<<<<<< HEAD
        html.javascript('cmk.dashboard.toggle_dashboard_edit(true)')
=======
        html.javascript('cmk.dashboard.toggle_dashboard_edit()')
>>>>>>> upstream/master

    html.body_end()  # omit regular footer with status icons, etc.


<<<<<<< HEAD
def dashlet_container_begin(nr, dashlet):
    dashlet_type = get_dashlet_type(dashlet)

    classes = ['dashlet', dashlet['type']]
    if dashlet_type.is_resizable():
        classes.append('resizable')

    html.open_div(id_="dashlet_%d" % nr, class_=classes)


def dashlet_container_end():
    html.close_div()


def render_dashlet_title_html(dashlet_instance):
    title = dashlet_instance.display_title()
    if title is not None and dashlet_instance.show_title():
        url = dashlet_instance.title_url()
        if url:
            title = html.render_a(_u(title), url)
        else:
            title = _u(title)
    return title


def render_dashlet_content(dashlet_instance, is_update, stash_html_vars=True):
    def update_or_show():
        visuals.add_context_to_uri_vars(dashlet_instance.dashlet_spec)
        if dashlet_instance.wato_folder is not None:
            html.request.set_var("wato_folder", dashlet_instance.wato_folder)
        with html.plugged():
            if is_update:
                dashlet_instance.update()
            else:
                dashlet_instance.show()
            return html.drain()

    if stash_html_vars:
        with html.stashed_vars():
            html.request.del_vars()
            html.request.set_var("name", dashlet_instance.dashboard_name)
            return update_or_show()
    else:
        return update_or_show()


def render_dashlet_exception_content(dashlet_instance, nr, e):
    logger.exception("Problem while rendering dashlet %d of type %s", nr,
                     dashlet_instance.type_name())

    # Unify different string types from exception messages to a unicode string
    try:
        exc_txt = six.text_type(e)
    except UnicodeDecodeError:
        exc_txt = str(e).decode("utf-8")

    return html.render_error(
        _("Problem while rendering dashlet %d of type %s: %s. Have a look at <tt>var/log/web.log</tt> for "
          "further information.") % (nr, dashlet_instance.type_name(), exc_txt))


def dashboard_edit_controls(name, board):
    # Show the edit menu to all users which are allowed to edit dashboards
    if not config.user.may("general.edit_dashboards"):
        return

    html.open_ul(style="display:none;", class_=["menu"], id_="controls")

=======
def _get_dashlets(name: DashboardName, board: DashboardConfig) -> List[Dashlet]:
    """Return dashlet instances of the dashboard"""
    dashlets: List[Dashlet] = []
    for nr, dashlet_spec in enumerate(board["dashlets"]):
        try:
            dashlet_type = get_dashlet_type(dashlet_spec)
            dashlet = dashlet_type(name, board, nr, dashlet_spec)
        except Exception:
            dashlet = _fallback_dashlet(name, board, dashlet_spec, nr)

        dashlets.append(dashlet)

    return dashlets


def _get_refresh_dashlets(
    dashlets: List[Dashlet]
) -> List[Tuple[DashletId, DashletRefreshInterval, DashletRefreshAction]]:
    """Return information for dashlets with automatic refresh"""
    refresh_dashlets = []
    for dashlet in dashlets:
        refresh = get_dashlet_refresh(dashlet)
        if refresh:
            refresh_dashlets.append(refresh)
    return refresh_dashlets


def _get_resize_dashlets(dashlets: List[Dashlet]) -> Dict[DashletId, str]:
    """Get list of javascript functions to execute after resizing the dashlets"""
    on_resize_dashlets: Dict[DashletId, str] = {}
    for dashlet in dashlets:
        on_resize = get_dashlet_on_resize(dashlet)
        if on_resize:
            on_resize_dashlets[dashlet.dashlet_id] = on_resize
    return on_resize_dashlets


def _get_dashlet_coords(dashlets: List[Dashlet]) -> List[Dict[str, int]]:
    """Return a list of all dashlets dimensions and positions"""
    return [get_dashlet_dimensions(dashlet) for dashlet in dashlets]


def dashlet_container_begin(dashlet: Dashlet) -> None:
    classes = ['dashlet', dashlet.type_name()]
    if dashlet.is_resizable():
        classes.append('resizable')

    html.open_div(id_="dashlet_%d" % dashlet.dashlet_id, class_=classes)


def dashlet_container_end() -> None:
    html.close_div()


def _render_dashlet(board: DashboardConfig, dashlet: Dashlet, is_update: bool, mtime: int,
                    missing_mandatory_context_filters: bool) -> Tuple[Union[str, HTML], str]:
    content = ""
    title: Union[str, HTML] = ""
    try:
        missing_single_infos = dashlet.missing_single_infos()
        if missing_single_infos or missing_mandatory_context_filters:
            return (
                _("Filter context missing"),
                str(
                    html.render_warning(
                        _("Unable to render this dashlet, "
                          "because we miss some required context information (%s). Please update the "
                          "form on the right to make this dashlet render.") %
                        ", ".join(sorted(missing_single_infos)))))

        title = _render_dashlet_title(dashlet)
        content = _render_dashlet_content(board, dashlet, is_update=False, mtime=board["mtime"])

    except Exception as e:
        content = render_dashlet_exception_content(dashlet, e)

    return title, content


def _render_dashlet_title(dashlet: Dashlet) -> Union[str, HTML]:
    title = dashlet.display_title()
    title_elements = []
    title_format = dashlet._dashlet_spec.get("title_format", ["plain"])

    if dashlet.show_title() and title and "plain" in title_format:
        title_elements.append((title, dashlet.title_url()))

    if dashlet.type_name() == "pnpgraph":
        title_elements.extend(
            title_info_elements(dashlet._dashlet_spec["_graph_identification"][1], title_format))

    return render_title_elements(title_elements)


def _render_dashlet_content(board: DashboardConfig, dashlet: Dashlet, is_update: bool,
                            mtime: int) -> str:

    # All outer variables are completely reset for the dashlets to have a clean, well known state.
    # The context that has been built based on the relevant HTTP variables is applied again.
    dashlet_context = dashlet.context if dashlet.has_context() else {}
    with visuals.context_uri_vars(dashlet_context, dashlet.single_infos()):
        # Set some dashboard related variables that are needed by some dashlets
        html.request.set_var("name", dashlet.dashboard_name)
        html.request.set_var("mtime", str(mtime))

        return _update_or_show(board, dashlet, is_update, mtime)


def _update_or_show(board: DashboardConfig, dashlet: Dashlet, is_update: bool, mtime: int) -> str:
    with html.plugged():
        if is_update:
            dashlet.update()
        else:
            dashlet.show()

        if mtime < board['mtime']:
            # prevent reloading on the dashboard which already has the current mtime,
            # this is normally the user editing this dashboard. All others: reload
            # the whole dashboard once.
            html.javascript('if (cmk.dashboard.dashboard_properties.dashboard_mtime < %d) {\n'
                            '    parent.location.reload();\n'
                            '}' % board['mtime'])

        return html.drain()


def render_dashlet_exception_content(dashlet: Dashlet, e: Exception) -> str:

    if not isinstance(e, MKUserError):
        # Do not write regular error messages related to normal user interaction and validation to
        # the web.log
        logger.exception("Problem while rendering dashlet %d of type %s", dashlet.dashlet_id,
                         dashlet.type_name())

    with html.plugged():
        if isinstance(e, MKException):
            # Unify different string types from exception messages to a unicode string
            try:
                exc_txt = str(e)
            except UnicodeDecodeError:
                exc_txt = ensure_str(str(e))

            html.show_error(
                _("Problem while rendering dashlet %d of type %s: %s. Have a look at "
                  "<tt>var/log/web.log</tt> for further information.") %
                (dashlet.dashlet_id, dashlet.type_name(), exc_txt))
            return html.drain()

        crash_reporting.handle_exception_as_gui_crash_report(
            details={
                "dashlet_id": dashlet.dashlet_id,
                "dashlet_type": dashlet.type_name(),
                "dashlet_spec": dashlet.dashlet_spec,
            })
        return html.drain()


def _fallback_dashlet(name: DashboardName, board: DashboardConfig, dashlet_spec: DashletConfig,
                      dashlet_id: int) -> Dashlet:
    """Create some place holder dashlet instance in case the dashlet could not be
    initialized"""
    dashlet_spec = dashlet_spec.copy()
    dashlet_spec.update({"type": "nodata", "text": ""})

    dashlet_type = get_dashlet_type(dashlet_spec)
    return dashlet_type(name, board, dashlet_id, dashlet_spec)


def _get_mandatory_filters(board: DashboardConfig,
                           unconfigured_single_infos: Set[str]) -> List[Tuple[str, ValueSpec]]:
    mandatory_filters: List[Tuple[str, ValueSpec]] = []

    # Get required single info keys (the ones that are not set by the config)
    for info_key in unconfigured_single_infos:
        info = visuals.visual_info_registry[info_key]()
        mandatory_filters += info.single_spec

    # Get required context filters set in the dashboard config
    if board["mandatory_context_filters"]:
        for filter_key in board["mandatory_context_filters"]:
            mandatory_filters.append((filter_key, visuals.VisualFilter(filter_key)))

    return mandatory_filters


def _page_menu(breadcrumb: Breadcrumb, name: DashboardName, board: DashboardConfig,
               board_context: VisualContext, unconfigured_single_infos: Set[str],
               mode: str) -> PageMenu:

    html.close_ul()
    menu = PageMenu(
        dropdowns=[
            PageMenuDropdown(
                name="dashboard",
                title=_("Dashboard"),
                topics=[
                    PageMenuTopic(
                        title=_("Edit"),
                        entries=list(_dashboard_edit_entries(name, board, mode)),
                    ),
                ],
            ),
            PageMenuDropdown(
                name="add_dashlets",
                title=_("Add"),
                topics=[
                    PageMenuTopic(
                        title=_("Views"),
                        entries=list(_dashboard_add_views_dashlet_entries(name, board, mode)),
                    ),
                    PageMenuTopic(
                        title=_("Graphs"),
                        entries=list(_dashboard_add_graphs_dashlet_entries(name, board, mode)),
                    ),
                    PageMenuTopic(
                        title=_("Metrics"),
                        entries=list(_dashboard_add_metrics_dashlet_entries(name, board, mode)),
                    ),
                    PageMenuTopic(
                        title=_("Checkmk"),
                        entries=list(_dashboard_add_checkmk_dashlet_entries(name, board, mode)),
                    ),
                    PageMenuTopic(
                        title=_("Ntop"),
                        entries=list(_dashboard_add_ntop_dashlet_entries(name, board, mode)),
                    ),
                    PageMenuTopic(
                        title=_("Other"),
                        entries=list(_dashboard_add_other_dashlet_entries(name, board, mode)),
                    ),
                ],
                is_enabled=True,
            ),
        ],
        breadcrumb=breadcrumb,
    )
    _extend_display_dropdown(menu, board, board_context, unconfigured_single_infos)

    return menu


def _dashboard_edit_entries(name: DashboardName, board: DashboardConfig,
                            mode: str) -> Iterator[PageMenuEntry]:
    if not config.user.may("general.edit_dashboards"):
        return

>>>>>>> upstream/master
    if board['owner'] != config.user.id:
        # Not owned dashboards must be cloned before being able to edit. Do not switch to
        # edit mode using javascript, use the URL with edit=1. When this URL is opened,
        # the dashboard will be cloned for this user
<<<<<<< HEAD
        html.li(html.render_a(_("Edit Dashboard"), href=html.makeuri([("edit", 1)])))

    else:
        #
        # Add dashlet menu
        #
        html.open_li(class_=["sublink"],
                     id_="control_add",
                     style="display:%s;" % ("block" if html.request.var("edit") == '1' else "none"),
                     onmouseover="cmk.dashboard.show_submenu(\'control_add\');")
        html.open_a(href="javascript:void(0)")
        html.icon(title=_("Add dashlet"), icon="dashboard_menuarrow")
        html.write_text(_("Add dashlet"))
        html.close_a()

        # The dashlet types which can be added to the view
        html.open_ul(style="display:none", class_=["menu", "sub"], id_="control_add_sub")

        # TODO: Why is this done like this? Looks like a dirty hack.
        # - Mypy does not understand this. We could probably use type(..., ..., ...) here instead.
        # - Or event better: Just produce a new menu entry below without registering something new
        #   to the dashlet registry.
        class ExistingView(dashlet_registry['view']):  # type: ignore
            @classmethod
            def title(cls):
                return _('Existing View')

            @classmethod
            def add_url(cls):
                return 'create_view_dashlet.py?name=%s&create=0&back=%s' % \
                            (html.urlencode(name), html.urlencode(html.makeuri([('edit', '1')])))

        dashlet_registry.register(ExistingView)

        for ty, dashlet_type in sorted(dashlet_registry.items(), key=lambda x: x[1].sort_index()):
            if dashlet_type.is_selectable():
                url = dashlet_type.add_url()
                html.open_li()
                html.open_a(href=url)
                html.icon(title=dashlet_type.title(), icon="dashlet_%s" % ty)
                html.write(dashlet_type.title())
                html.close_a()
                html.close_li()
        html.close_ul()

        html.close_li()

        #
        # Properties link
        #
        html.open_li()
        html.open_a(href="edit_dashboard.py?load_name=%s&back=%s" %
                    (name, html.urlencode(html.makeuri([]))),
                    onmouseover="cmk.dashboard.hide_submenus();")
        html.icon(title="", icon="trans")
        html.write(_('Properties'))
        html.close_a()
        html.close_li()

        #
        # Stop editing
        #
        html.open_li(style="display:%s;" % ("block" if html.request.var("edit") == '1' else "none"),
                     id_="control_view")
        html.open_a(href="javascript:void(0)",
                    onclick="cmk.dashboard.toggle_dashboard_edit(false)",
                    onmouseover="cmk.dashboard.hide_submenus();")
        html.icon(title="", icon="trans")
        html.write(_('Stop Editing'))
        html.close_a()
        html.close_li()

        #
        # Enable editing link
        #
        html.open_li(style="display:%s;" % ("none" if html.request.var("edit") == '1' else "block"),
                     id_="control_edit")
        html.open_a(href="javascript:void(0)", onclick="cmk.dashboard.toggle_dashboard_edit(true);")
        html.icon(title="", icon="trans")
        html.write(_('Edit Dashboard'))
        html.close_a()
        html.close_li()

    html.close_ul()

    html.icon_button(None,
                     _('Edit the Dashboard'),
                     'dashboard_controls',
                     'controls_toggle',
                     onclick='void(0)')

    html.close_div()
=======
        yield PageMenuEntry(
            title=_("Customize builtin dashboard"),
            icon_name="edit",
            item=make_simple_link(makeuri(request, [("edit", 1)])),
        )
        return

    edit_text = _("Leave layout mode")
    display_text = _("Enter layout mode")

    yield PageMenuEntry(
        title=edit_text if mode == "edit" else display_text,
        icon_name="trans",
        item=make_javascript_link('cmk.dashboard.toggle_dashboard_edit("%s", "%s")' %
                                  (edit_text, display_text)),
        is_shortcut=True,
        name="toggle_edit",
    )

    yield PageMenuEntry(
        title=_("Properties"),
        icon_name="properties",
        item=make_simple_link(
            makeuri_contextless(
                request,
                [
                    ("load_name", name),
                    ("back", html.urlencode(makeuri(request, []))),
                ],
                filename="edit_dashboard.py",
            )),
    )


def _extend_display_dropdown(menu: PageMenu, board: DashboardConfig, board_context: VisualContext,
                             unconfigured_single_infos: Set[str]) -> None:
    display_dropdown = menu.get_dropdown_by_name("display", make_display_options_dropdown())

    mandatory_filters = _get_mandatory_filters(board, unconfigured_single_infos)
    # Like _dashboard_info_handler we assume that only host / service filters are relevant
    info_list = ["host", "service"]

    display_dropdown.topics.insert(
        0,
        PageMenuTopic(title=_("Filter"),
                      entries=[
                          PageMenuEntry(
                              title=_("Filter"),
                              icon_name="filters",
                              item=PageMenuSidePopup(
                                  visuals.render_filter_form(info_list, mandatory_filters,
                                                             board_context, board["name"],
                                                             "ajax_initial_dashboard_filters")),
                              name="filters",
                              is_shortcut=True,
                          ),
                      ]))


@page_registry.register_page("ajax_initial_dashboard_filters")
class AjaxInitialDashboardFilters(ABCAjaxInitialFilters):
    def _get_context(self, page_name: str) -> Dict:
        dashboard_name = page_name
        board = _load_dashboard_with_cloning(get_permitted_dashboards(), dashboard_name, edit=False)
        board = _add_context_to_dashboard(board)

        # For the topology dashboard filters are retrieved from a corresponding view context
        if page_name == "topology":
            _view, show_filters = get_topology_view_and_filters()
            return {
                f.ident: board["context"][f.ident] if f.ident in board["context"] else {}
                for f in show_filters
                if f.available()
            }
        return board["context"]


def _dashboard_add_views_dashlet_entries(name: DashboardName, board: DashboardConfig,
                                         mode: str) -> Iterator[PageMenuEntry]:
    yield PageMenuEntry(
        title=_('Copy existing view'),
        icon_name="dashlet_view",
        item=make_simple_link(
            'create_view_dashlet.py?name=%s&create=0&back=%s' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
        is_show_more=True,
    )

    yield PageMenuEntry(
        title=_('View'),
        icon_name='dashlet_view',
        item=make_simple_link(
            'create_view_dashlet.py?name=%s&create=0&back=%s' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title=_('Link existing view'),
        icon_name='dashlet_linked_view',
        item=make_simple_link(
            'create_link_view_dashlet.py?name=%s&create=0&back=%s' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )


def _dashboard_add_graphs_dashlet_entries(name: DashboardName, board: DashboardConfig,
                                          mode: str) -> Iterator[PageMenuEntry]:

    yield PageMenuEntry(
        title='Performance Graph',
        icon_name='dashlet_pnpgraph',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=pnpgraph' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Custom Graph',
        icon_name='dashlet_custom_graph',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=custom_graph' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )


def _dashboard_add_metrics_dashlet_entries(name: DashboardName, board: DashboardConfig,
                                           mode: str) -> Iterator[PageMenuEntry]:

    yield PageMenuEntry(
        title='Average scatterplot',
        icon_name='dashlet_average_scatterplot',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=average_scatterplot' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Barplot',
        icon_name='dashlet_barplot',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=barplot' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Gauge',
        icon_name='dashlet_gauge',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=gauge' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Single metric',
        icon_name='dashlet_single_metric',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=single_metric' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )


def _dashboard_add_checkmk_dashlet_entries(name: DashboardName, board: DashboardConfig,
                                           mode: str) -> Iterator[PageMenuEntry]:

    yield PageMenuEntry(
        title='Host Statistics',
        icon_name='dashlet_hoststats',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=hoststats' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Service Statistics',
        icon_name='dashlet_servicestats',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=servicestats' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Notification timeline',
        icon_name='dashlet_notifications_bar_chart',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=notifications_bar_chart' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Alert timeline',
        icon_name='dashlet_alerts_bar_chart',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=alerts_bar_chart' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='User notifications',
        icon_name='dashlet_notify_users',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=notify_users' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Sidebar Snapin',
        icon_name='dashlet_snapin',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=snapin' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
        is_show_more=True,
    )


def _dashboard_add_ntop_dashlet_entries(name: DashboardName, board: DashboardConfig,
                                        mode: str) -> Iterator[PageMenuEntry]:

    yield PageMenuEntry(
        title='Alerts',
        icon_name='dashlet_ntop_alerts',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=ntop_alerts' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )

    yield PageMenuEntry(
        title='Ntop: Flows',
        icon_name='dashlet_ntop_flows',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=ntop_flows' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
    )


def _dashboard_add_other_dashlet_entries(name: DashboardName, board: DashboardConfig,
                                         mode: str) -> Iterator[PageMenuEntry]:

    yield PageMenuEntry(
        title='Custom URL',
        icon_name='dashlet_url',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=url' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
        is_show_more=True,
    )

    yield PageMenuEntry(
        title='Static text',
        icon_name='dashlet_nodata',
        item=make_simple_link(
            'edit_dashlet.py?name=%s&create=0&back=%s&type=nodata' %
            (html.urlencode(name), html.urlencode(makeuri(request, [('edit', '1')])))),
        is_show_more=True,
    )
>>>>>>> upstream/master


# Render dashlet custom scripts
def dashlet_javascripts(board):
    scripts = '\n'.join([ty.script() for ty in used_dashlet_types(board) if ty.script()])
    if scripts:
        html.javascript(scripts)


# Render dashlet custom styles
def dashlet_styles(board):
    styles = '\n'.join([ty.styles() for ty in used_dashlet_types(board) if ty.styles()])
    if styles:
        html.style(styles)


def used_dashlet_types(board):
    type_names = list({d['type'] for d in board['dashlets']})
    return [dashlet_registry[ty] for ty in type_names]


# dashlets using the 'url' method will be refreshed by us. Those
# dashlets using static content (such as an iframe) will not be
# refreshed by us but need to do that themselves.
# TODO: Refactor this to Dashlet or later Dashboard class
<<<<<<< HEAD
def get_dashlet_refresh(dashlet_instance):
    if dashlet_instance.type_name() == "url" or (not dashlet_instance.is_iframe_dashlet() and
                                                 dashlet_instance.refresh_interval()):
        refresh = dashlet_instance.refresh_interval()
        if not refresh:
            return

        action = dashlet_instance.get_refresh_action()
        if action:
            return [dashlet_instance.dashlet_id, refresh, action]
=======
def get_dashlet_refresh(
        dashlet: Dashlet
) -> Optional[Tuple[DashletId, DashletRefreshInterval, DashletRefreshAction]]:
    if dashlet.type_name() == "url" or (not dashlet.is_iframe_dashlet() and
                                        dashlet.refresh_interval()):
        refresh = dashlet.refresh_interval()
        if not refresh:
            return None

        action = dashlet.get_refresh_action()
        if action:
            return (dashlet.dashlet_id, refresh, action)
>>>>>>> upstream/master
    return None


# TODO: Refactor this to Dashlet or later Dashboard class
<<<<<<< HEAD
def get_dashlet_on_resize(dashlet_instance):
    on_resize = dashlet_instance.on_resize()
=======
def get_dashlet_on_resize(dashlet: Dashlet) -> Optional[str]:
    on_resize = dashlet.on_resize()
>>>>>>> upstream/master
    if on_resize:
        return '(function() {%s})' % on_resize
    return None


# TODO: Refactor this to Dashlet or later Dashboard class
<<<<<<< HEAD
def get_dashlet_dimensions(dashlet_instance):
    dimensions = {}
    dimensions['x'], dimensions['y'] = dashlet_instance.position()
    dimensions['w'], dimensions['h'] = dashlet_instance.size()
    return dimensions


def get_dashlet_type(dashlet):
    return dashlet_registry[dashlet["type"]]


def get_dashlet(board, ident):
    if board not in available_dashboards:
        raise MKUserError("name", _('The requested dashboard does not exist.'))
    dashboard = available_dashboards[board]
=======
def get_dashlet_dimensions(dashlet: Dashlet) -> Dict[str, int]:
    dimensions = {}
    dimensions['x'], dimensions['y'] = dashlet.position()
    dimensions['w'], dimensions['h'] = dashlet.size()
    return dimensions


def get_dashlet_type(dashlet_spec: DashletConfig) -> Type[Dashlet]:
    return dashlet_registry[dashlet_spec["type"]]


def get_dashlet(board: DashboardName, ident: DashletId) -> DashletConfig:
    try:
        dashboard = get_permitted_dashboards()[board]
    except KeyError:
        raise MKUserError("name", _('The requested dashboard does not exist.'))
>>>>>>> upstream/master

    try:
        return dashboard['dashlets'][ident]
    except IndexError:
        raise MKGeneralException(_('The dashlet does not exist.'))


<<<<<<< HEAD
def draw_dashlet(dashlet_instance, dashlet_content_html, dashlet_title_html):
=======
def draw_dashlet(dashlet: Dashlet, content: str, title: Union[str, HTML]) -> None:
>>>>>>> upstream/master
    """Draws the initial HTML code for one dashlet

    Each dashlet has an id "dashlet_%d", where %d is its index (in
    board["dashlets"]).  Javascript uses that id for the resizing. Within that
    div there is an inner div containing the actual dashlet content. This content
    is updated later using the dashboard_dashlet.py ajax call.
    """
<<<<<<< HEAD
    if dashlet_title_html is not None and dashlet_instance.show_title():
        html.div(html.render_span(dashlet_title_html),
                 id_="dashlet_title_%d" % dashlet_instance.dashlet_id,
                 class_=["title"])

    css = ["dashlet_inner"]
    if dashlet_instance.show_background():
        css.append("background")

    html.open_div(id_="dashlet_inner_%d" % dashlet_instance.dashlet_id, class_=css)
    html.write_html(dashlet_content_html)
=======
    if all((
            dashlet.type_name() not in [
                'single_metric', 'average_scatterplot', 'gauge', 'barplot', 'average_scatterplot',
                'alerts_bar_chart', 'notifications_bar_chart'
            ],
            title is not None,
            dashlet.show_title(),
    )):
        title_background = ["highlighted"] if dashlet.show_title() is True else []
        html.div(html.render_span(title),
                 id_="dashlet_title_%d" % dashlet.dashlet_id,
                 class_=["title"] + title_background)

    css = ["dashlet_inner"]
    if dashlet.show_background():
        css.append("background")

    html.open_div(id_="dashlet_inner_%d" % dashlet.dashlet_id, class_=css)
    html.write_html(HTML(content))
>>>>>>> upstream/master
    html.close_div()


#.
#   .--Draw Dashlet--------------------------------------------------------.
#   |     ____                       ____            _     _      _        |
#   |    |  _ \ _ __ __ ___      __ |  _ \  __ _ ___| |__ | | ___| |_      |
#   |    | | | | '__/ _` \ \ /\ / / | | | |/ _` / __| '_ \| |/ _ \ __|     |
#   |    | |_| | | | (_| |\ V  V /  | |_| | (_| \__ \ | | | |  __/ |_      |
#   |    |____/|_|  \__,_| \_/\_/   |____/ \__,_|___/_| |_|_|\___|\__|     |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | Draw dashlet HTML code which are rendered by the multisite dashboard |
#   '----------------------------------------------------------------------'


@cmk.gui.pages.register("dashboard_dashlet")
<<<<<<< HEAD
def ajax_dashlet():
=======
def ajax_dashlet() -> None:
>>>>>>> upstream/master
    name = html.request.var('name')
    if not name:
        raise MKUserError("name", _('The name of the dashboard is missing.'))

<<<<<<< HEAD
    ident = html.get_integer_input("id")

    load_dashboards()

    if name not in available_dashboards:
        raise MKUserError("name", _('The requested dashboard does not exist.'))
    board = available_dashboards[name]

    mtime = html.get_integer_input('mtime', 0)
    if mtime < board['mtime']:
        # prevent reloading on the dashboard which already has the current mtime,
        # this is normally the user editing this dashboard. All others: reload
        # the whole dashboard once.
        html.javascript('if (cmk.dashboard.dashboard_properties.dashboard_mtime < %d) {\n'
                        '    parent.location.reload();\n'
                        '}' % board['mtime'])

    the_dashlet = None
    for nr, dashlet in enumerate(board['dashlets']):
        if nr == ident:
            the_dashlet = dashlet
            break

    if not the_dashlet:
        raise MKUserError("id", _('The dashlet can not be found on the dashboard.'))

    if the_dashlet['type'] not in dashlet_registry:
        raise MKUserError("id", _('The requested dashlet type does not exist.'))

    wato_folder = html.request.var("wato_folder")

    dashlet_type = get_dashlet_type(the_dashlet)
    dashlet_instance = dashlet_type(name, board, ident, the_dashlet, wato_folder)

    try:
        dashlet_content_html = render_dashlet_content(dashlet_instance,
                                                      stash_html_vars=False,
                                                      is_update=True)
    except Exception as e:
        dashlet_content_html = render_dashlet_exception_content(dashlet_instance, ident, e)

    html.write_html(dashlet_content_html)
=======
    ident = html.request.get_integer_input_mandatory("id")

    try:
        board = get_permitted_dashboards()[name]
    except KeyError:
        raise MKUserError("name", _('The requested dashboard does not exist.'))

    board = _add_context_to_dashboard(board)

    dashlet_spec = None
    for nr, this_dashlet_spec in enumerate(board['dashlets']):
        if nr == ident:
            dashlet_spec = this_dashlet_spec
            break

    if not dashlet_spec:
        raise MKUserError("id", _('The dashlet can not be found on the dashboard.'))

    if dashlet_spec['type'] not in dashlet_registry:
        raise MKUserError("id", _('The requested dashlet type does not exist.'))

    mtime = html.request.get_integer_input_mandatory('mtime', 0)

    dashlet = None
    try:
        dashlet_type = get_dashlet_type(dashlet_spec)
        dashlet = dashlet_type(name, board, ident, dashlet_spec)

        content = _render_dashlet_content(board, dashlet, is_update=True, mtime=mtime)
    except Exception as e:
        if dashlet is None:
            dashlet = _fallback_dashlet(name, board, dashlet_spec, ident)
        content = render_dashlet_exception_content(dashlet, e)

    html.write_html(HTML(content))


def _add_context_to_dashboard(board: DashboardConfig) -> DashboardConfig:
    board = copy.deepcopy(board)
    board.setdefault("single_infos", [])
    board.setdefault("context", {})
    board.setdefault("mandatory_context_filters", [])
    return board
>>>>>>> upstream/master


#.
#   .--Dashboard List------------------------------------------------------.
#   |           ____            _     _        _     _     _               |
#   |          |  _ \  __ _ ___| |__ | |__    | |   (_)___| |_             |
#   |          | | | |/ _` / __| '_ \| '_ \   | |   | / __| __|            |
#   |          | |_| | (_| \__ \ | | | |_) |  | |___| \__ \ |_             |
#   |          |____/ \__,_|___/_| |_|_.__(_) |_____|_|___/\__|            |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


@cmk.gui.pages.register("edit_dashboards")
<<<<<<< HEAD
def page_edit_dashboards():
    load_dashboards(lock=html.is_transaction())
    visuals.page_list('dashboards', _("Edit Dashboards"), dashboards)
=======
def page_edit_dashboards() -> None:
    visuals.page_list('dashboards', _("Edit Dashboards"), get_all_dashboards())
>>>>>>> upstream/master


#.
#   .--Create Dashb.-------------------------------------------------------.
#   |      ____                _         ____            _     _           |
#   |     / ___|_ __ ___  __ _| |_ ___  |  _ \  __ _ ___| |__ | |__        |
#   |    | |   | '__/ _ \/ _` | __/ _ \ | | | |/ _` / __| '_ \| '_ \       |
#   |    | |___| | |  __/ (_| | ||  __/ | |_| | (_| \__ \ | | | |_) |      |
#   |     \____|_|  \___|\__,_|\__\___| |____/ \__,_|___/_| |_|_.__(_)     |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   | When clicking on create dashboard, this page is opened to make the   |
#   | context type of the new dashboard selectable.                        |
#   '----------------------------------------------------------------------'


@cmk.gui.pages.register("create_dashboard")
<<<<<<< HEAD
def page_create_dashboard():
=======
def page_create_dashboard() -> None:
>>>>>>> upstream/master
    visuals.page_create_visual('dashboards', visual_info_registry.keys())


#.
#   .--Dashb. Config-------------------------------------------------------.
#   |     ____            _     _         ____             __ _            |
#   |    |  _ \  __ _ ___| |__ | |__     / ___|___  _ __  / _(_) __ _      |
#   |    | | | |/ _` / __| '_ \| '_ \   | |   / _ \| '_ \| |_| |/ _` |     |
#   |    | |_| | (_| \__ \ | | | |_) |  | |__| (_) | | | |  _| | (_| |     |
#   |    |____/ \__,_|___/_| |_|_.__(_)  \____\___/|_| |_|_| |_|\__, |     |
#   |                                                           |___/      |
#   +----------------------------------------------------------------------+
#   | Configures the global settings of a dashboard.                       |
#   '----------------------------------------------------------------------'

<<<<<<< HEAD
vs_dashboard = None


@cmk.gui.pages.register("edit_dashboard")
def page_edit_dashboard():
    global vs_dashboard
    load_dashboards(lock=html.is_transaction())

    # This is not defined here in the function in order to be l10n'able
    vs_dashboard = Dictionary(
        title=_('Dashboard Properties'),
        render='form',
        optional_keys=None,
        elements=[
            ('show_title',
             Checkbox(
                 title=_('Display dashboard title'),
                 label=_('Show the header of the dashboard with the configured title.'),
                 default_value=True,
             )),
        ],
    )

    visuals.page_edit_visual('dashboards',
                             dashboards,
                             create_handler=create_dashboard,
                             custom_field_handler=custom_field_handler)


def custom_field_handler(dashboard):
    vs_dashboard.render_input('dashboard', dashboard and dashboard or None)


def create_dashboard(old_dashboard, dashboard):
=======

@cmk.gui.pages.register("edit_dashboard")
def page_edit_dashboard() -> None:
    visuals.page_edit_visual('dashboards',
                             get_all_dashboards(),
                             create_handler=create_dashboard,
                             custom_field_handler=custom_field_handler,
                             info_handler=_dashboard_info_handler)


def _dashboard_info_handler(visual):
    # We could use all available infos here, but there is a lot of normally unused stuff. For better
    # usability reduce the list to the (assumed) relevant used ones.
    return ["host", "service"]


def custom_field_handler(dashboard: DashboardConfig) -> None:
    _vs_dashboard().render_input('dashboard', dashboard and dashboard or None)


def create_dashboard(old_dashboard: DashboardConfig, dashboard: DashboardConfig) -> DashboardConfig:
    vs_dashboard = _vs_dashboard()
>>>>>>> upstream/master
    board_properties = vs_dashboard.from_html_vars('dashboard')
    vs_dashboard.validate_value(board_properties, 'dashboard')
    dashboard.update(board_properties)

    # Do not remove the dashlet configuration during general property editing
    dashboard['dashlets'] = old_dashboard.get('dashlets', [])
    dashboard['mtime'] = int(time.time())

    return dashboard


<<<<<<< HEAD
=======
def _vs_dashboard() -> Dictionary:
    return Dictionary(
        title=_('Dashboard Properties'),
        render='form',
        optional_keys=False,
        elements=[
            ('show_title',
             Checkbox(
                 title=_('Display dashboard title'),
                 label=_('Show the header of the dashboard with the configured title.'),
                 default_value=True,
             )),
            (
                "mandatory_context_filters",
                visuals.FilterChoices(
                    # Like _dashboard_info_handler we assume that only host / service filters are relevant
                    infos=["host", "service"],
                    title=_("Required context filters"),
                    help=_(
                        "Show the dialog that can be used to update the dashboard context "
                        "on initial dashboard rendering and enforce the user to provide the "
                        "context filters that are set here. This can be useful in case you want "
                        "the users to first provide some context before rendering the dashboard."),
                )),
        ],
    )


>>>>>>> upstream/master
#.
#   .--Dashlet Editor------------------------------------------------------.
#   |    ____            _     _      _     _____    _ _ _                 |
#   |   |  _ \  __ _ ___| |__ | | ___| |_  | ____|__| (_) |_ ___  _ __     |
#   |   | | | |/ _` / __| '_ \| |/ _ \ __| |  _| / _` | | __/ _ \| '__|    |
#   |   | |_| | (_| \__ \ | | | |  __/ |_  | |__| (_| | | || (_) | |       |
#   |   |____/ \__,_|___/_| |_|_|\___|\__| |_____\__,_|_|\__\___/|_|       |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
@cmk.gui.pages.register("create_view_dashlet")
def page_create_view_dashlet():
    create = html.request.var('create', '1') == '1'
    name = html.request.var('name')

    if create:
        import cmk.gui.views as views
        url = html.makeuri([('back', html.makeuri([]))], filename="create_view_dashlet_infos.py")
        views.page_create_view(next_url=url)

    else:
        # Choose an existing view from the list of available views
        choose_view(name)


@cmk.gui.pages.register("create_view_dashlet_infos")
def page_create_view_dashlet_infos():
    ds_name = html.request.var('datasource')
=======
@cmk.gui.pages.register("create_link_view_dashlet")
def page_create_link_view_dashlet() -> None:
    """Choose an existing view from the list of available views"""
    name = html.request.get_str_input_mandatory('name')
    choose_view(name, _('Embed existing view'), _create_linked_view_dashlet_spec)


def _create_linked_view_dashlet_spec(dashlet_id: int, view_name: str) -> Dict:
    dashlet_spec = default_dashlet_definition("linked_view")
    dashlet_spec["name"] = view_name
    return dashlet_spec


@cmk.gui.pages.register("create_view_dashlet")
def page_create_view_dashlet() -> None:
    create = html.request.var('create', '1') == '1'
    name = html.request.get_str_input_mandatory('name')

    if create:
        import cmk.gui.views as views  # pylint: disable=import-outside-toplevel
        url = makeuri(
            request,
            [('back', makeuri(request, []))],
            filename="create_view_dashlet_infos.py",
        )
        views.show_create_view_dialog(next_url=url)

    else:
        # Choose an existing view from the list of available views
        choose_view(name, _('Copy existing view'), _create_cloned_view_dashlet_spec)


def _create_cloned_view_dashlet_spec(dashlet_id: int, view_name: str) -> Dict:
    dashlet_spec = default_dashlet_definition('view')

    # save the original context and override the context provided by the view
    copy_view_into_dashlet(dashlet_spec, dashlet_id, view_name)
    return dashlet_spec


@cmk.gui.pages.register("create_view_dashlet_infos")
def page_create_view_dashlet_infos() -> None:
    ds_name = html.request.get_str_input_mandatory('datasource')
>>>>>>> upstream/master
    if ds_name not in data_source_registry:
        raise MKUserError("datasource", _('The given datasource is not supported'))

    # Create a new view by choosing the datasource and the single object types
    visuals.page_create_visual('views',
                               data_source_registry[ds_name]().infos,
<<<<<<< HEAD
                               next_url=html.makeuri_contextless([
                                   ('name', html.request.var('name')),
                                   ('type', 'view'),
                                   ('datasource', ds_name),
                                   ('back', html.makeuri([])),
                                   ('next',
                                    html.makeuri_contextless([('name', html.request.var('name')),
                                                              ('edit', '1')], 'dashboard.py')),
                               ],
                                                                 filename='edit_dashlet.py'))


def choose_view(name):
    import cmk.gui.views as views
    vs_view = DropdownChoice(
        title=_('View Name'),
=======
                               next_url=makeuri_contextless(request, [
                                   ('name', html.request.var('name')),
                                   ('type', 'view'),
                                   ('datasource', ds_name),
                                   ('back', makeuri(request, [])),
                                   ('next',
                                    makeuri_contextless(
                                        request,
                                        [('name', html.request.var('name')), ('edit', '1')],
                                        'dashboard.py',
                                    )),
                               ],
                                                            filename='edit_dashlet.py'))


def choose_view(name: DashboardName, title: str, create_dashlet_spec_func: Callable) -> None:
    import cmk.gui.views as views  # pylint: disable=import-outside-toplevel
    vs_view = DropdownChoice(
        title=_('View name'),
>>>>>>> upstream/master
        choices=views.view_choices,
        sorted=True,
    )

<<<<<<< HEAD
    html.header(_('Create Dashlet from existing View'))
    html.begin_context_buttons()
    back_url = html.get_url_input(
        "back", "dashboard.py?edit=1&name=%s" % html.urlencode(html.request.var('name')))
    html.context_button(_("Back"), back_url, "back")
    html.end_context_buttons()
=======
    dashboard = get_permitted_dashboards()[name]

    breadcrumb = _dashlet_editor_breadcrumb(name, dashboard, title)
    html.header(title, breadcrumb=breadcrumb, page_menu=_choose_view_page_menu(breadcrumb))
>>>>>>> upstream/master

    if html.request.var('save') and html.check_transaction():
        try:
            view_name = vs_view.from_html_vars('view')
            vs_view.validate_value(view_name, 'view')

<<<<<<< HEAD
            load_dashboards(lock=True)
            dashboard = available_dashboards[name]

            # Add the dashlet!
            dashlet = default_dashlet_definition('view')

            # save the original context and override the context provided by the view
            dashlet_id = len(dashboard['dashlets'])
            load_view_into_dashlet(dashlet, dashlet_id, view_name)
            add_dashlet(dashlet, dashboard)

            raise HTTPRedirect('edit_dashlet.py?name=%s&id=%d' % (name, dashlet_id))
=======
            dashlet_id = len(dashboard['dashlets'])
            dashlet_spec = create_dashlet_spec_func(dashlet_id, view_name)
            add_dashlet(dashlet_spec, dashboard)

            raise HTTPRedirect(
                makeuri_contextless(
                    request,
                    [
                        ("name", name),
                        ("id", str(dashlet_id)),
                        ("back", html.get_url_input('back')),
                    ],
                    filename="edit_dashlet.py",
                ))
>>>>>>> upstream/master
        except MKUserError as e:
            html.user_error(e)

    html.begin_form('choose_view')
<<<<<<< HEAD
    forms.header(_('Select View'))
=======
    forms.header(_('Select view'))
>>>>>>> upstream/master
    forms.section(vs_view.title())
    vs_view.render_input('view', '')
    html.help(vs_view.help())
    forms.end()

<<<<<<< HEAD
    html.button('save', _('Continue'), 'submit')

=======
>>>>>>> upstream/master
    html.hidden_fields()
    html.end_form()
    html.footer()


<<<<<<< HEAD
@cmk.gui.pages.register("edit_dashlet")
def page_edit_dashlet():
=======
def _choose_view_page_menu(breadcrumb: Breadcrumb) -> PageMenu:
    return make_simple_form_page_menu(breadcrumb,
                                      form_name="choose_view",
                                      button_name="save",
                                      save_title=_("Continue"))


@cmk.gui.pages.register("edit_dashlet")
def page_edit_dashlet() -> None:
>>>>>>> upstream/master
    if not config.user.may("general.edit_dashboards"):
        raise MKAuthException(_("You are not allowed to edit dashboards."))

    board = html.request.var('name')
    if not board:
        raise MKUserError("name", _('The name of the dashboard is missing.'))

<<<<<<< HEAD
    ty = html.request.var('type')

    if html.request.has_var('id'):
        ident = html.get_integer_input("id")
    else:
        ident = None

    if ident is None and not ty:
        raise MKUserError("id", _('The ID of the dashlet is missing.'))

    load_dashboards(lock=html.is_transaction())

    if board not in available_dashboards:
        raise MKUserError("name", _('The requested dashboard does not exist.'))
    dashboard = available_dashboards[board]

    if ident is None:
=======
    ident = html.request.get_integer_input("id")

    try:
        dashboard = get_permitted_dashboards()[board]
    except KeyError:
        raise MKUserError("name", _('The requested dashboard does not exist.'))

    if ident is None:
        type_name = html.request.get_str_input_mandatory('type')
>>>>>>> upstream/master
        mode = 'add'
        title = _('Add Dashlet')

        try:
<<<<<<< HEAD
            dashlet_type = dashlet_registry[ty]
=======
            dashlet_type = cast(Dashlet, dashlet_registry[type_name])
>>>>>>> upstream/master
        except KeyError:
            raise MKUserError("type", _('The requested dashlet type does not exist.'))

        # Initial configuration
<<<<<<< HEAD
        dashlet = {
            'position': dashlet_type.initial_position(),
            'size': dashlet_type.initial_size(),
            'single_infos': dashlet_type.single_infos(),
            'type': ty,
        }
        ident = len(dashboard['dashlets'])

        single_infos_raw = html.request.var('single_infos')
        single_infos = []
=======
        dashlet_spec = {
            'position': dashlet_type.initial_position(),
            'size': dashlet_type.initial_size(),
            'single_infos': dashlet_type.single_infos(),
            'type': type_name,
        }
        dashlet_spec.update(dashlet_type.default_settings())

        if dashlet_type.has_context():
            dashlet_spec["context"] = {}

        ident = len(dashboard['dashlets'])

        single_infos_raw = html.request.var('single_infos')
        single_infos: List[InfoName] = []
>>>>>>> upstream/master
        if single_infos_raw:
            single_infos = single_infos_raw.split(',')
            for key in single_infos:
                if key not in visual_info_registry:
                    raise MKUserError('single_infos', _('The info %s does not exist.') % key)

        if not single_infos:
            single_infos = dashlet_type.single_infos()

<<<<<<< HEAD
        dashlet['single_infos'] = single_infos
=======
        dashlet_spec['single_infos'] = single_infos
>>>>>>> upstream/master
    else:
        mode = 'edit'
        title = _('Edit Dashlet')

        try:
<<<<<<< HEAD
            dashlet = dashboard['dashlets'][ident]
        except IndexError:
            raise MKUserError("id", _('The dashlet does not exist.'))

        ty = dashlet['type']
        dashlet_type = dashlet_registry[ty]
        single_infos = dashlet['single_infos']

    html.header(title)

    html.begin_context_buttons()
    back_url = html.get_url_input('back', 'dashboard.py?name=%s&edit=1' % board)
    next_url = html.get_url_input('next', back_url)
    html.context_button(_('Back'), back_url, 'back')
    html.context_button(_('All Dashboards'), 'edit_dashboards.py', 'dashboard')
    html.end_context_buttons()

    vs_general = Dictionary(
        title=_('General Settings'),
        render='form',
        optional_keys=['title', 'title_url'],
        elements=[
            ('type', FixedValue(
                ty,
                totext=dashlet_type.title(),
                title=_('Dashlet Type'),
            )),
            visuals.single_infos_spec(single_infos),
            ('background',
             Checkbox(
                 title=_('Colored Background'),
                 label=_('Render background'),
                 help=_('Render gray background color behind the dashlets content.'),
                 default_value=True,
             )),
            ('show_title',
             Checkbox(
                 title=_('Show Title'),
                 label=_('Render the titlebar above the dashlet'),
                 help=_('Render the titlebar including title and link above the dashlet.'),
                 default_value=True,
             )),
            ('title',
             TextUnicode(
                 title=_('Custom Title') + '<sup>*</sup>',
                 help=_(
                     'Most dashlets have a hard coded default title. For example the view snapin '
                     'has even a dynamic title which defaults to the real title of the view. If you '
                     'like to use another title, set it here.'),
                 size=50,
             )),
            ('title_url',
             TextUnicode(
                 title=_('Link of Title'),
                 help=_('The URL of the target page the link of the dashlet should link to.'),
                 size=50,
             )),
        ],
    )

    def dashlet_info_handler(dashlet):
        if dashlet['type'] == 'view':
            import cmk.gui.views as views
            return views.get_view_infos(dashlet)
        return dashlet_registry[dashlet['type']].infos()

    context_specs = visuals.get_context_specs(dashlet, info_handler=dashlet_info_handler)

    vs_type = None
=======
            dashlet_spec = dashboard['dashlets'][ident]
        except IndexError:
            raise MKUserError("id", _('The dashlet does not exist.'))

        type_name = cast(str, dashlet_spec['type'])
        dashlet_type = cast(Dashlet, dashlet_registry[type_name])
        single_infos = cast(List[str], dashlet_spec['single_infos'])

    breadcrumb = _dashlet_editor_breadcrumb(board, dashboard, title)
    html.header(title, breadcrumb=breadcrumb, page_menu=_dashlet_editor_page_menu(breadcrumb))

    vs_general = dashlet_vs_general_settings(dashlet_type, single_infos)

    def dashlet_info_handler(dashlet_spec: DashletConfig) -> List[str]:
        assert board is not None
        assert isinstance(ident, int)
        dashlet_type = dashlet_registry[dashlet_spec['type']]
        dashlet = dashlet_type(board, dashboard, ident, dashlet_spec)
        return dashlet.infos()

    context_specs = visuals.get_context_specs(dashlet_spec, info_handler=dashlet_info_handler)

    vs_type: Optional[ValueSpec] = None
>>>>>>> upstream/master
    params = dashlet_type.vs_parameters()
    render_input_func = None
    handle_input_func = None
    if isinstance(params, list):
        # TODO: Refactor all params to be a Dictionary() and remove this special case
        vs_type = Dictionary(
            title=_('Properties'),
            render='form',
            optional_keys=dashlet_type.opt_parameters(),
            validate=dashlet_type.validate_parameters_func(),
            elements=params,
        )

    elif isinstance(params, (Dictionary, Transform)):
        vs_type = params

<<<<<<< HEAD
    elif hasattr(params, '__call__'):
        # It's a tuple of functions which should be used to render and parse the params
        render_input_func, handle_input_func = params()
=======
    elif isinstance(params, tuple):
        # It's a tuple of functions which should be used to render and parse the params
        render_input_func, handle_input_func = params

    # Check disjoint option on known valuespecs
    if isinstance(vs_type, Dictionary):
        settings_elements = set(el[0] for el in vs_general._elements)
        pe = vs_type._elements() if callable(vs_type._elements) else vs_type._elements
        properties_elements = set(el[0] for el in pe)
        assert settings_elements.isdisjoint(
            properties_elements), "Dashlet settings and properties have a shared option name"
>>>>>>> upstream/master

    if html.request.var('save') and html.transaction_valid():
        try:
            general_properties = vs_general.from_html_vars('general')
            vs_general.validate_value(general_properties, 'general')
<<<<<<< HEAD
            dashlet.update(general_properties)
            # Remove unset optional attributes
            if 'title' not in general_properties and 'title' in dashlet:
                del dashlet['title']
=======
            dashlet_spec.update(general_properties)

            # Remove unset optional attributes
            optional_properties = set(e[0] for e in vs_general._get_elements()) - set(
                vs_general._required_keys)
            for option in optional_properties:
                if option not in general_properties and option in dashlet_spec:
                    del dashlet_spec[option]
>>>>>>> upstream/master

            if vs_type:
                type_properties = vs_type.from_html_vars('type')
                vs_type.validate_value(type_properties, 'type')
<<<<<<< HEAD
                dashlet.update(type_properties)
=======
                dashlet_spec.update(type_properties)
>>>>>>> upstream/master

            elif handle_input_func:
                # The returned dashlet must be equal to the parameter! It is not replaced/re-added
                # to the dashboard object. FIXME TODO: Clean this up!
<<<<<<< HEAD
                dashlet = handle_input_func(ident, dashlet)

            if context_specs:
                dashlet['context'] = visuals.process_context_specs(context_specs)

            if mode == "add":
                dashboard['dashlets'].append(dashlet)

            visuals.save('dashboards', dashboards)

            html.immediate_browser_redirect(1, next_url)
            if mode == 'edit':
                html.message(_('The dashlet has been saved.'))
            else:
                html.message(_('The dashlet has been added to the dashboard.'))
=======
                dashlet_spec = handle_input_func(ident, dashlet_spec)

            if context_specs:
                dashlet_spec['context'] = visuals.process_context_specs(context_specs)

            if mode == "add":
                dashboard['dashlets'].append(dashlet_spec)

            save_all_dashboards()

            next_url = html.get_url_input('next', html.get_url_input('back'))
            html.immediate_browser_redirect(1, next_url)
            if mode == 'edit':
                html.show_message(_('The dashlet has been saved.'))
            else:
                html.show_message(_('The dashlet has been added to the dashboard.'))
>>>>>>> upstream/master
            html.reload_sidebar()
            html.footer()
            return

        except MKUserError as e:
            html.user_error(e)

    html.begin_form("dashlet", method="POST")
<<<<<<< HEAD
    vs_general.render_input("general", dashlet)

    if vs_type:
        vs_type.render_input("type", dashlet)
    elif render_input_func:
        render_input_func(dashlet)

    visuals.render_context_specs(dashlet, context_specs)
=======
    vs_general.render_input("general", dashlet_spec)

    if vs_type:
        vs_type.render_input("type", dashlet_spec)
    elif render_input_func:
        render_input_func(dashlet_spec)

    visuals.render_context_specs(dashlet_spec, context_specs)
>>>>>>> upstream/master

    forms.end()
    html.show_localization_hint()
    html.button("save", _("Save"))
    html.hidden_fields()
    html.end_form()

    html.footer()


<<<<<<< HEAD
@cmk.gui.pages.register("delete_dashlet")
def page_delete_dashlet():
=======
def _dashlet_editor_page_menu(breadcrumb: Breadcrumb) -> PageMenu:
    return make_simple_form_page_menu(breadcrumb, form_name="dashlet", button_name="save")


def _dashlet_editor_breadcrumb(name: str, board: DashboardConfig, title: str) -> Breadcrumb:
    breadcrumb = make_topic_breadcrumb(mega_menu_registry.menu_monitoring(),
                                       PagetypeTopics.get_topic(board["topic"]))
    breadcrumb.append(
        BreadcrumbItem(
            visuals.visual_title('dashboard', board),
            html.get_url_input('back'),
        ))

    breadcrumb.append(make_current_page_breadcrumb_item(title))

    return breadcrumb


@cmk.gui.pages.register("clone_dashlet")
def page_clone_dashlet() -> None:
>>>>>>> upstream/master
    if not config.user.may("general.edit_dashboards"):
        raise MKAuthException(_("You are not allowed to edit dashboards."))

    board = html.request.var('name')
    if not board:
        raise MKUserError("name", _('The name of the dashboard is missing.'))

<<<<<<< HEAD
    ident = html.get_integer_input("id")

    load_dashboards(lock=True)

    if board not in available_dashboards:
        raise MKUserError("name", _('The requested dashboard does not exist.'))
    dashboard = available_dashboards[board]

    try:
        _dashlet = dashboard['dashlets'][ident]
    except IndexError:
        raise MKUserError("id", _('The dashlet does not exist.'))

    html.header(_('Confirm Dashlet Deletion'))

    html.begin_context_buttons()
    back_url = html.get_url_input('back', 'dashboard.py?name=%s&edit=1' % board)
    html.context_button(_('Back'), back_url, 'back')
    html.end_context_buttons()

    result = html.confirm(_('Do you really want to delete this dashlet?'),
                          method='GET',
                          add_transid=True)
    if result is False:
        html.footer()
        return  # confirm dialog shown
    elif result is True:  # do it!
        try:
            dashboard['dashlets'].pop(ident)
            dashboard['mtime'] = int(time.time())
            visuals.save('dashboards', dashboards)

            html.message(_('The dashlet has been deleted.'))
        except MKUserError as e:
            html.div(e.message, class_="error")
            return

    html.immediate_browser_redirect(1, back_url)
    html.reload_sidebar()
    html.footer()
=======
    ident = html.request.get_integer_input_mandatory("id")

    try:
        dashboard = get_permitted_dashboards()[board]
    except KeyError:
        raise MKUserError("name", _('The requested dashboard does not exist.'))

    try:
        dashlet_spec = dashboard['dashlets'][ident]
    except IndexError:
        raise MKUserError("id", _('The dashlet does not exist.'))

    new_dashlet_spec = dashlet_spec.copy()
    dashlet_type = get_dashlet_type(new_dashlet_spec)
    new_dashlet_spec["position"] = dashlet_type.initial_position()

    dashboard['dashlets'].append(new_dashlet_spec)
    dashboard['mtime'] = int(time.time())
    save_all_dashboards()

    raise HTTPRedirect(html.get_url_input('back'))


@cmk.gui.pages.register("delete_dashlet")
def page_delete_dashlet() -> None:
    if not config.user.may("general.edit_dashboards"):
        raise MKAuthException(_("You are not allowed to edit dashboards."))

    board = html.request.var('name')
    if not board:
        raise MKUserError("name", _('The name of the dashboard is missing.'))

    ident = html.request.get_integer_input_mandatory("id")

    try:
        dashboard = get_permitted_dashboards()[board]
    except KeyError:
        raise MKUserError("name", _('The requested dashboard does not exist.'))

    try:
        _dashlet_spec = dashboard['dashlets'][ident]  # noqa: F841
    except IndexError:
        raise MKUserError("id", _('The dashlet does not exist.'))

    dashboard['dashlets'].pop(ident)
    dashboard['mtime'] = int(time.time())
    save_all_dashboards()

    raise HTTPRedirect(html.get_url_input('back'))
>>>>>>> upstream/master


#.
#   .--Ajax Updater--------------------------------------------------------.
#   |       _     _              _   _           _       _                 |
#   |      / \   (_) __ ___  __ | | | |_ __   __| | __ _| |_ ___ _ __      |
#   |     / _ \  | |/ _` \ \/ / | | | | '_ \ / _` |/ _` | __/ _ \ '__|     |
#   |    / ___ \ | | (_| |>  <  | |_| | |_) | (_| | (_| | ||  __/ |        |
#   |   /_/   \_\/ |\__,_/_/\_\  \___/| .__/ \__,_|\__,_|\__\___|_|        |
#   |          |__/                   |_|                                  |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


<<<<<<< HEAD
def check_ajax_update():
    if not config.user.may("general.edit_dashboards"):
        raise MKAuthException(_("You are not allowed to edit dashboards."))

    board = html.request.var('name')
    if not board:
        raise MKUserError("name", _('The name of the dashboard is missing.'))

    ident = html.get_integer_input("id")

    load_dashboards(lock=True)

    if board not in available_dashboards:
        raise MKUserError("name", _('The requested dashboard does not exist.'))
    dashboard = available_dashboards[board]

    try:
        dashlet = dashboard['dashlets'][ident]
    except IndexError:
        raise MKUserError("id", _('The dashlet does not exist.'))

    return dashlet, dashboard


@cmk.gui.pages.register("ajax_dashlet_pos")
def ajax_dashlet_pos():
    dashlet, board = check_ajax_update()

    board['mtime'] = int(time.time())

    dashlet['position'] = int(html.request.var('x')), int(html.request.var('y'))
    dashlet['size'] = int(html.request.var('w')), int(html.request.var('h'))
    visuals.save('dashboards', dashboards)
=======
def check_ajax_update() -> Tuple[DashletConfig, DashboardConfig]:
    if not config.user.may("general.edit_dashboards"):
        raise MKAuthException(_("You are not allowed to edit dashboards."))

    board = html.request.get_str_input_mandatory('name')
    ident = html.request.get_integer_input_mandatory("id")

    try:
        dashboard = get_permitted_dashboards()[board]
    except KeyError:
        raise MKUserError("name", _('The requested dashboard does not exist.'))

    try:
        dashlet_spec = dashboard['dashlets'][ident]
    except IndexError:
        raise MKUserError("id", _('The dashlet does not exist.'))

    return dashlet_spec, dashboard


@cmk.gui.pages.register("ajax_dashlet_pos")
def ajax_dashlet_pos() -> None:
    dashlet_spec, board = check_ajax_update()

    board['mtime'] = int(time.time())

    dashlet_spec['position'] = (html.request.get_integer_input_mandatory("x"),
                                html.request.get_integer_input_mandatory("y"))
    dashlet_spec['size'] = (html.request.get_integer_input_mandatory("w"),
                            html.request.get_integer_input_mandatory("h"))
    save_all_dashboards()
>>>>>>> upstream/master
    html.write('OK %d' % board['mtime'])


@cmk.gui.pages.register("ajax_delete_user_notification")
<<<<<<< HEAD
def ajax_delete_user_notification():
    msg_id = html.request.var("id")
=======
def ajax_delete_user_notification() -> None:
    msg_id = html.request.get_str_input_mandatory("id")
>>>>>>> upstream/master
    notify.delete_gui_message(msg_id)


#.
#   .--Dashlet Popup-------------------------------------------------------.
#   |   ____            _     _      _     ____                            |
#   |  |  _ \  __ _ ___| |__ | | ___| |_  |  _ \ ___  _ __  _   _ _ __     |
#   |  | | | |/ _` / __| '_ \| |/ _ \ __| | |_) / _ \| '_ \| | | | '_ \    |
#   |  | |_| | (_| \__ \ | | | |  __/ |_  |  __/ (_) | |_) | |_| | |_) |   |
#   |  |____/ \__,_|___/_| |_|_|\___|\__| |_|   \___/| .__/ \__,_| .__/    |
#   |                                                |_|         |_|       |
#   +----------------------------------------------------------------------+
#   |                                                                      |
#   '----------------------------------------------------------------------'


# TODO: Move this to the Dashlet class
<<<<<<< HEAD
def default_dashlet_definition(ty):
=======
def default_dashlet_definition(ty: DashletTypeName) -> DashletConfig:
>>>>>>> upstream/master
    return {
        'type': ty,
        'position': dashlet_registry[ty].initial_position(),
        'size': dashlet_registry[ty].initial_size(),
        'show_title': True,
    }


<<<<<<< HEAD
def add_dashlet(dashlet, dashboard):
    dashboard['dashlets'].append(dashlet)
    dashboard['mtime'] = int(time.time())
    visuals.save('dashboards', dashboards)
=======
def add_dashlet(dashlet_spec: DashletConfig, dashboard: DashboardConfig) -> None:
    dashboard['dashlets'].append(dashlet_spec)
    dashboard['mtime'] = int(time.time())
    save_all_dashboards()
>>>>>>> upstream/master
