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

from cmk.gui.i18n import _

from . import (
    multisite_builtin_views,)

# Painters used in list of services views
service_view_painters = [
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import Any, List, Optional, Tuple

import cmk.utils.version as cmk_version
from cmk.gui.i18n import _

from . import multisite_builtin_views

# Painters used in list of services views
service_view_painters: List[Tuple[Optional[str], ...]] = [
>>>>>>> upstream/master
    ('service_state', None),
    #    ('service_type_icon',   None),
    ('service_description', 'service'),
    ('service_icons', None),
    ('svc_plugin_output', None),
    ('svc_state_age', None),
    ('svc_check_age', None),
    ('perfometer', None),
]

<<<<<<< HEAD
=======
_host_host_painter: Tuple[Optional[str], ...] = ('host', 'host')

>>>>>>> upstream/master
# Same as list of services, but extended by the hostname
host_service_view_painters = service_view_painters[:]
host_service_view_painters.insert(1, ('host', 'host'))

host_view_painters = [
    ('host_state', None),
    #    ('host_type_icon',       None),
    ('host', 'host', 'host_addresses'),
    ('host_icons', None),
    ('num_services_ok', 'host_ok'),
    ('num_services_warn', 'host_warn'),
    ('num_services_unknown', 'host_unknown'),
    ('num_services_crit', 'host_crit'),
    ('num_services_pending', 'host_pending'),
]

multisite_builtin_views.update({
    'allhosts': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description':
            _('Overall state of all hosts, with counts of services in the various states.'),
        'group_painters': [('sitealias', None)],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'allhosts',
        'num_columns': 3,
        'owner': '',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [
<<<<<<< HEAD
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'host_in_service_period',
            'hoststate',
            'siteopt',
            'host_acknowledged',
            'hostregex',
            'host_notifications_enabled',
            'hostgroups',
            'opthostgroup',
            'host_check_command',
            'opthost_contactgroup',
            'hostalias',
            'host_labels',
            'host_tags',
=======
            'siteopt',
            'hostregex',
>>>>>>> upstream/master
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('All hosts'),
<<<<<<< HEAD
        'topic': _('Hosts'),
    },
    'starred_hosts': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _('Overall state of your favorite hosts'),
        'group_painters': [('sitealias', None)],
        'hard_filters': [],
        'hard_filtervars': [('is_host_favorites', '1')],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'allhosts',
        'num_columns': 3,
        'owner': '',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'hoststate',
            'siteopt',
            'host_acknowledged',
            'hostregex',
            'host_notifications_enabled',
            'hostgroups',
            'opthostgroup',
            'host_check_command',
            'opthost_contactgroup',
            'hostalias',
            'host_favorites',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Favorite hosts'),
        'topic': _('Hosts'),
    },
    'allhosts_mini': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _('Showing all hosts in a compact layout.'),
        'group_painters': [('sitealias', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('site', ''),
            ('host', ''),
            ('opthostgroup', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'allhosts_mini',
        'num_columns': 6,
        'owner': '',
        'painters': [
            ('host_state', None),
            ('host', 'host'),
            ('num_problems', 'problemsofhost'),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'hoststate',
            'siteopt',
            'host_acknowledged',
            'hostregex',
            'host_notifications_enabled',
            'opthostgroup',
            'host_check_command',
            'opthost_contactgroup',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('All hosts (Mini)'),
        'topic': _('Hosts'),
=======
        "topic": "overview",
        "sort_index": 20,
        'icon': 'folder',
>>>>>>> upstream/master
    },
    'unmonitored_services': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'service_discovery',
        'description': _('Services not being monitored due to configuration.'),
        'context': {
            'discovery_state': {
                'discovery_state_var0': 'on',
                'discovery_state_var1': '',
                'discovery_state_var2': 'on',
            }
        },
        'group_painters': [
            ('sitealias', None),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [('state', 'unmonitored')],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'service_discovery',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('service_discovery_service', None),
            ('service_discovery_check', None),
            ('service_discovery_state', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'hoststate',
            'siteopt',
            'host_acknowledged',
            'hostregex',
            'host_notifications_enabled',
            'opthostgroup',
            'host_check_command',
            'opthost_contactgroup',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Unmonitored services'),
<<<<<<< HEAD
        'topic': _('Services')
=======
        "topic": "analyze",
        "sort_index": 60,
        'icon': {
            'icon': 'services',
            'emblem': 'warning'
        },
>>>>>>> upstream/master
    },
    'pending_discovery': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'service_discovery',
        'description': _('Differences to currently monitored services on a host.'),
        'context': {
            'discovery_state': {
                'discovery_state_var0': '',
                'discovery_state_var1': 'on',
                'discovery_state_var2': 'on',
            }
        },
        'group_painters': [
            ('sitealias', None),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [('state', ['new', 'vanished'])],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'service_discovery',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('service_discovery_service', None),
            ('service_discovery_check', None),
            ('service_discovery_state', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'hoststate',
            'siteopt',
            'host_acknowledged',
            'hostregex',
            'host_notifications_enabled',
            'opthostgroup',
            'host_check_command',
            'opthost_contactgroup',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Pending service discovery'),
<<<<<<< HEAD
        'topic': _('Problems')
=======
        "topic": "analyze",
        "sort_index": 50,
        'icon': {
            'icon': 'service_discovery',
            'emblem': 'pending'
        },
>>>>>>> upstream/master
    },
    'allservices': {
        'browser_reload': 90,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All services grouped by hosts.'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_in_downtime', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('opthostgroup', ''),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
<<<<<<< HEAD
        'hidden': False,
=======
        'hidden': True,
>>>>>>> upstream/master
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'allservices',
        'num_columns': 1,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'service_in_service_period',
            'optservicegroup',
            'servicegroups',
            'service_notifications_enabled',
            'host_in_notification_period',
            'in_downtime',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'opthostgroup',
            'output',
            'service_is_flapping',
            'siteopt',
            'service_labels',
            'host_labels',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('All services'),
<<<<<<< HEAD
        'topic': _('Services')
=======
        'icon': 'services',
>>>>>>> upstream/master
    },
    'service_check_durations': {
        'browser_reload': 90,
        'column_headers': 'pergroup',
        'context': {
            'service_active_checks_enabled': {
                'is_service_active_checks_enabled': '1'
            },
        },
        'datasource': 'services',
        'description':
            _('All services ordered by their service check durations, grouped by their sites.\n'),
        'force_checkboxes': False,
        'group_painters': [('sitealias', 'sitehosts', None)],
        'hidden': False,
        'hidebutton': False,
<<<<<<< HEAD
        'icon': None,
        'layout': 'table',
        'linktitle': _('Service check durations'),
=======
        'layout': 'table',
>>>>>>> upstream/master
        'mobile': False,
        'mustsearch': False,
        'name': 'service_check_durations',
        'num_columns': 1,
        'painters': [
            ('service_state', None, None),
            ('service_description', 'service', None),
            ('service_icons', None, None),
            ('svc_plugin_output', None, None),
            ('svc_state_age', None, None),
            ('svc_check_age', None, None),
            ('svc_check_duration', None, None),
            ("svc_check_command", None, None),
        ],
        'play_sounds': False,
        'public': False,
        'single_infos': [],
        'sorters': [
            ('site', False),
            ('svc_check_duration', True),
        ],
<<<<<<< HEAD
        'title': _('Service check durations'),
        'topic': _('Services'),
        'user_sortable': True,
    },
    'starred_services': {
        'browser_reload': 90,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All of your favorites services by hosts.'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_in_downtime', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('opthostgroup', ''),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
            ('is_service_favorites', '1'),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'starred_services',
        'num_columns': 1,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'in_downtime',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'opthostgroup',
            'output',
            'service_is_flapping',
            'siteopt',
            'host_favorites',
            'service_favorites',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Favorite services'),
        'topic': _('Services')
=======
        'user_sortable': True,
        'title': _('Service check durations'),
        "topic": "history",
        "sort_index": 70,
        "is_show_more": True,
        'icon': 'service_duration',
>>>>>>> upstream/master
    },
    'comments': {
        'column_headers': 'pergroup',
        'datasource': 'comments',
        'description': _('All host- and service comments'),
        'group_painters': [('comment_what', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('host', ''),
            ('service', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'icon': 'comment',
        'layout': 'table',
        'mustsearch': False,
        'name': 'comments',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('comment_author', None),
            ('comment_time', None),
            ('comment_expires', None),
            ('comment_entry_type', None),
            ('comment_comment', None),
            ('host', None),
            ('service_description', 'service'),
            ('comment_id', None),
        ],
        'public': True,
        'show_filters': ['hostregex', 'comment_entry_time', 'serviceregex'],
        'sorters': [
            ('comment_type', False),
            ('comment_author', False),
        ],
<<<<<<< HEAD
        'title': _('Comments')
=======
        'title': _('Comments'),
        "topic": "overview",
        "sort_index": 85,
>>>>>>> upstream/master
    },
    'comments_of_host': {
        'column_headers': 'pergroup',
        'datasource': 'comments',
        'description': _('Linkable view showing all comments of a specific host'),
        'group_painters': [],
        'hard_filters': ['service'],
        'hard_filtervars': [('service', '')],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'icon': 'comment',
        'layout': 'table',
        'mustsearch': False,
        'name': 'comments_of_host',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('comment_author', None),
            ('comment_comment', None),
            ('comment_time', None),
            ('comment_expires', None),
            ('comment_entry_type', None),
        ],
        'public': True,
        'show_filters': [],
        'sorters': [],
<<<<<<< HEAD
        'linktitle': _('Host comments'),
        'title': _('Comments of host'),
=======
        'title': _('Comments of host'),
        "topic": "monitoring",
>>>>>>> upstream/master
    },
    'comments_of_service': {
        'column_headers': 'pergroup',
        'datasource': 'comments',
        'description': _('Linkable view showing all comments of a specific service'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['siteopt', 'host', 'service'],
        'icon': 'comment',
        'layout': 'table',
        'mustsearch': False,
        'name': 'comments_of_service',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('comment_author', None),
            ('comment_comment', None),
            ('comment_time', None),
            ('comment_expires', None),
            ('comment_entry_type', None),
        ],
        'public': True,
        'show_filters': [],
        'sorters': [],
<<<<<<< HEAD
        'linktitle': _('Comments'),
        'title': _('Comments of service'),
=======
        'title': _('Comments of service'),
        "topic": "monitoring",
>>>>>>> upstream/master
    },
    'downtimes': {
        'column_headers': 'pergroup',
        'datasource': 'downtimes',
        'description': _('All host- and service-downtimes'),
        'group_painters': [('downtime_what', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_service_scheduled_downtime_depth', '-1'),
            ('host', ''),
            ('service', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'icon': 'downtime',
        'layout': 'table',
        'mustsearch': False,
        'name': 'downtimes',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('host', 'host'),
            ('service_description', 'service'),
            ('downtime_origin', None),
            ('downtime_author', None),
            ('downtime_entry_time', None),
            ('downtime_start_time', None),
            ('downtime_end_time', None),
            ('downtime_fixed', None),
            ('downtime_duration', None),
            ('downtime_recurring', None),
            ('downtime_comment', None),
        ],
        'public': True,
        'show_filters': [
            'service_scheduled_downtime_depth',
            'hostregex',
            'downtime_entry_time',
            'serviceregex',
        ],
        'sorters': [
            ('downtime_what', False),
            ('downtime_start_time', False),
        ],
<<<<<<< HEAD
        'title': _('Downtimes')
=======
        'title': _('Scheduled downtimes'),
        "topic": "overview",
        "sort_index": 80,
>>>>>>> upstream/master
    },
    'downtime_history': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log_events',
        'description': _('All historic scheduled downtimes of hosts and services'),
        'group_painters': [('log_what', None)],
        'hard_filters': ['log_type'],
        'hard_filtervars': [
            ('logtime_from_range', '86400'),
            ('logtime_from', '60'),
            ('log_type', 'DOWNTIME ALERT'),
        ],
        'hidden': False,
        'hide_filters': [],
        'icon': 'downtime',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host Dt-History'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'num_columns': 1,
        'painters': [
            ('log_icon', None),
            ('log_time', None),
            ('host', 'host_dt_hist'),
            ('service_description', 'svc_dt_hist'),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
<<<<<<< HEAD
        'show_filters': ['logtime', 'hostregex', 'serviceregex', 'log_state_type'],
=======
        'show_filters': ['logtime', 'hostregex', 'serviceregex', 'log_state_info'],
>>>>>>> upstream/master
        'sorters': [
            ('log_what', True),
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('History of scheduled downtimes'),
        'topic': _('Other'),
=======
        'title': _('Downtime history'),
        "topic": "history",
        "sort_index": 30,
>>>>>>> upstream/master
    },
    'api_downtimes': {
        'column_headers': 'pergroup',
        'datasource': 'downtimes',
        'description': _('All host- and service-downtimes (including ids)'),
        'group_painters': [('downtime_what', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_service_scheduled_downtime_depth', '-1'),
            ('host', ''),
            ('service', ''),
        ],
        'hidden': True,
        'hide_filters': [],
        'icon': 'downtime',
        'layout': 'table',
        'mustsearch': False,
        'name': 'downtimes',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('host', 'host'),
            ('service_description', 'service'),
            ('downtime_origin', None),
            ('downtime_author', None),
            ('downtime_entry_time', None),
            ('downtime_start_time', None),
            ('downtime_end_time', None),
            ('downtime_fixed', None),
            ('downtime_duration', None),
            ('downtime_recurring', None),
            ('downtime_comment', None),
            ('downtime_id', None),
        ],
        'public': True,
        'show_filters': [
            'service_scheduled_downtime_depth',
            'hostregex',
            'serviceregex',
            'downtime_id',
        ],
        'sorters': [
            ('downtime_what', False),
            ('downtime_start_time', False),
        ],
        'title': _('Downtimes')
    },
    'downtimes_of_host': {
        'column_headers': 'pergroup',
        'datasource': 'downtimes',
        'description': _('Lists all host downtimes.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'icon': 'downtime',
        'layout': 'table',
        'mustsearch': False,
        'name': 'downtimes_of_host',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('downtime_origin', None),
            ('downtime_author', None),
            ('downtime_entry_time', None),
            ('downtime_start_time', None),
            ('downtime_end_time', None),
            ('downtime_fixed', None),
            ('downtime_duration', None),
            ('downtime_recurring', None),
            ('downtime_comment', None),
        ],
        'public': True,
        'show_filters': [],
        'sorters': [],
<<<<<<< HEAD
        'linktitle': _('Host downtimes'),
        'title': _('Downtimes of host')
=======
        'title': _('Downtimes of host'),
        'topic': "history",
>>>>>>> upstream/master
    },
    'downtimes_of_service': {
        'column_headers': 'pergroup',
        'datasource': 'downtimes',
        'description': _('Lists all downtimes for services.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['siteopt', 'service', 'host'],
        'icon': 'downtime',
        'layout': 'table',
        'mustsearch': False,
        'name': 'downtimes_of_service',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('downtime_origin', None),
            ('downtime_author', None),
            ('downtime_entry_time', None),
            ('downtime_start_time', None),
            ('downtime_end_time', None),
            ('downtime_fixed', None),
            ('downtime_duration', None),
            ('downtime_recurring', None),
            ('downtime_comment', None),
        ],
        'public': True,
        'show_filters': [],
        'sorters': [],
<<<<<<< HEAD
        'linktitle': _('Downtimes'),
        'title': _('Downtimes of service')
=======
        'title': _('Downtimes of service'),
        'topic': "history",
>>>>>>> upstream/master
    },
    'host': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description':
            _('All services of a given host. The host and site must be set via HTML variables.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
<<<<<<< HEAD
        'icon': 'status',
=======
        'icon': 'services',
>>>>>>> upstream/master
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'host',
        'num_columns': 2,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate', 'serviceregex'],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
<<<<<<< HEAD
        'linktitle': _('Services'),
        'title': _('Services of Host')
=======
        'title': _('Services of Host'),
        'topic': 'monitoring',
>>>>>>> upstream/master
    },
    'host_export': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description':
            _('All services of a given host. The host and site must be set via HTTP variables.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt', 'host'],
        'icon': 'services',
        'layout': 'boxed',
        'mustsearch': False,
        'num_columns': 1,
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('svc_perf_data', None),
            ('svc_check_command', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate', 'serviceregex'],
        'sorters': [('svcdescr', False)],
<<<<<<< HEAD
        'linktitle': _('Services'),
=======
>>>>>>> upstream/master
        'title': _('Services of Host')
    },
    'hosts': {
        'browser_reload': 30,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All services of hosts which match a name'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [('host', '')],
        'hidden': True,
        'hide_filters': [],
        'layout': 'boxed',
<<<<<<< HEAD
        'linktitle': _('Services of Hosts'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'hosts',
        'num_columns': 1,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['hostregex', 'svcstate', 'siteopt'],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Services of Hosts'),
<<<<<<< HEAD
        'topic': _('Other')
=======
>>>>>>> upstream/master
    },
    'host_ok': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All services of a given host that are in state OK'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': ['svcstate'],
        'hard_filtervars': [
            ('st0', 'on'),
            ('st1', ''),
            ('st2', ''),
            ('st3', ''),
            ('stp', ''),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': True,
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'host_lk',
        'num_columns': 2,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate'],
        'sorters': [('svcdescr', False)],
<<<<<<< HEAD
        'linktitle': _('Services: OK'),
=======
>>>>>>> upstream/master
        'title': _('OK Services of host')
    },
    'host_warn': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All services of a given host that are in state WARN'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': ['svcstate'],
        'hard_filtervars': [
            ('st0', ''),
            ('st1', 'on'),
            ('st2', ''),
            ('st3', ''),
            ('stp', ''),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': True,
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'host_warn',
        'num_columns': 2,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate'],
        'sorters': [('svcdescr', False)],
<<<<<<< HEAD
        'linktitle': _('Services: WARN'),
=======
>>>>>>> upstream/master
        'title': _('WARN Services of host')
    },
    'host_crit': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All services of a given host that are in state CRIT'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': ['svcstate'],
        'hard_filtervars': [
            ('st0', ''),
            ('st1', ''),
            ('st2', 'on'),
            ('st3', ''),
            ('stp', ''),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': True,
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'host_crit',
        'num_columns': 2,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate'],
        'sorters': [('svcdescr', False)],
<<<<<<< HEAD
        'linktitle': _('Services: CRIT'),
=======
>>>>>>> upstream/master
        'title': _('CRIT Services of host')
    },
    'host_unknown': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All services of a given host that are in state UNKNOWN'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': ['svcstate'],
        'hard_filtervars': [
            ('st0', ''),
            ('st1', ''),
            ('st2', ''),
            ('st3', 'on'),
            ('stp', ''),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': True,
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'host_unknown',
        'num_columns': 2,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate'],
        'sorters': [('svcdescr', False)],
<<<<<<< HEAD
        'linktitle': _('Services: UNKNOWN'),
=======
>>>>>>> upstream/master
        'title': _('UNKNOWN Services of host')
    },
    'host_pending': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All services of a given host that are PENDING'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': ['svcstate'],
        'hard_filtervars': [
            ('st0', ''),
            ('st1', ''),
            ('st2', ''),
            ('st3', ''),
            ('stp', 'on'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': True,
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'host_pending',
        'num_columns': 2,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate'],
        'sorters': [('svcdescr', False)],
<<<<<<< HEAD
        'linktitle': _('Services: PENDING'),
=======
>>>>>>> upstream/master
        'title': _('PENDING Services of host')
    },
    'problemsofhost': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _(
            'All problem services of a given host. The host and site must be set via HTTP variables.'
        ),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': ['svcstate'],
        'hard_filtervars': [
            ('st0', ''),
            ('st1', 'on'),
            ('st2', 'on'),
            ('st3', 'on'),
            ('stp', ''),
        ],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt', 'host'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'problemsofhost',
        'num_columns': 2,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svcstate'],
        'sorters': [('svcdescr', False)],
<<<<<<< HEAD
        'linktitle': _('Host Problems'),
=======
>>>>>>> upstream/master
        'title': _('Problems of host')
    },
    'hostgroup': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description':
            _('Lists members of a host group with the number of services in the different states.'),
        'group_painters': [
            ('site_icon', None),
            ('sitealias', 'sitehosts'),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'boxed',
<<<<<<< HEAD
        'linktitle': _('Host Group Overview'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'hostgroup',
        'num_columns': 2,
        'owner': 'admin',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Host Group'),
<<<<<<< HEAD
        'topic': _('hidden')
    },
    'hostgroupservices': {
        'browser_reload': 90,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All services of a certain hostgroup'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('is_in_downtime', '-1'),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'table',
        'linktitle': _('Services'),
        'mustsearch': False,
        'name': 'hostgroupservices',
        'num_columns': 2,
        'owner': 'admin',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('service_icons', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'in_downtime',
            'output',
            'service_is_flapping',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Services of Hostgroup'),
        'topic': _('hidden')
    },
    'hostgroupgrid': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hostsbygroup',
        'description': _('Hosts grouped by hostgroups, with a brief list of all services'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('hg_alias', 'hostgroup'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_host_scheduled_downtime_depth', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('site', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostgroupgrid',
        'num_columns': 2,
        'owner': '',
        'painters': [
            ('host', 'host'),
            ('host_services', None),
            ('host_icons', None),
        ],
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'siteopt',
        ],
        'sorters': [
            ('site', False),
            ('hostgroup', False),
            ('site_host', False),
        ],
        'title': _('Host Groups (Grid)'),
        'topic': _('Host Groups')
    },
    'hostgroups': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hostgroups',
        'description': _(
            'A short overview over all host groups, without an explicity listing of the actual hosts'
        ),
        'group_painters': [('sitealias', 'sitehosts')],
=======
    },
    'hostgroup_up': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'context': {
            'hoststate': {
                'hoststate_filled': '1',
                'hst0': 'on',
                'hst1': '',
                'hst2': '',
                'hstp': '',
            }
        },
        'datasource': 'hosts',
        'description': _(
            'Lists up members of a host group with the number of services in the different states.'
        ),
        'group_painters': [
            ('site_icon', None),
            ('sitealias', 'sitehosts'),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostgroup_up',
        'num_columns': 2,
        'owner': 'admin',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Host Group of Up Hosts'),
    },
    'hostgroup_down': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'context': {
            'hoststate': {
                'hoststate_filled': '1',
                'hst0': '',
                'hst1': 'on',
                'hst2': '',
                'hstp': '',
            }
        },
        'datasource': 'hosts',
        'description': _(
            'Lists down members of a host group with the number of services in the different states.'
        ),
        'group_painters': [
            ('site_icon', None),
            ('sitealias', 'sitehosts'),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostgroup_down',
        'num_columns': 2,
        'owner': 'admin',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Host Group of Down Hosts'),
    },
    'hostgroup_unreach': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'context': {
            'hoststate': {
                'hoststate_filled': '1',
                'hst0': '',
                'hst1': '',
                'hst2': 'on',
                'hstp': '',
            }
        },
        'datasource': 'hosts',
        'description': _(
            'Lists members of an unreachable host group with the number of services in the different states.'
        ),
        'group_painters': [
            ('site_icon', None),
            ('sitealias', 'sitehosts'),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostgroup_unreach',
        'num_columns': 2,
        'owner': 'admin',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Host Group of Unreachable Hosts'),
    },
    'hostgroup_pend': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'context': {
            'hoststate': {
                'hoststate_filled': '1',
                'hst0': '',
                'hst1': '',
                'hst2': '',
                'hstp': 'on',
            }
        },
        'datasource': 'hosts',
        'description': _(
            'Lists members of a pending host group with the number of services in the different states.'
        ),
        'group_painters': [
            ('site_icon', None),
            ('sitealias', 'sitehosts'),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostgroup',
        'num_columns': 2,
        'owner': 'admin',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Host Group of Pending'),
    },
    'hostgroupservices': {
        'browser_reload': 90,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All services of a certain hostgroup'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('is_in_downtime', '-1'),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'table',
        'mustsearch': False,
        'name': 'hostgroupservices',
        'num_columns': 2,
        'owner': 'admin',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('service_icons', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'in_downtime',
            'output',
            'service_is_flapping',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Services of Hostgroup'),
    },
    'hostgroupservices_ok': {
        'browser_reload': 60,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All ok services of a certain hostgroup'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('st0', 'on'),
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('is_in_downtime', '-1'),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'table',
        'mustsearch': False,
        'name': 'hostgroupservices_ok',
        'num_columns': 1,
        'owner': 'admin',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('service_icons', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'in_downtime',
            'output',
            'service_is_flapping',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('OK Services of Hostgroup'),
    },
    'hostgroupservices_warn': {
        'browser_reload': 60,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All warn services of a certain hostgroup'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('st1', 'on'),
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('is_in_downtime', '-1'),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'table',
        'mustsearch': False,
        'name': 'hostgroupservices_warn',
        'num_columns': 1,
        'owner': 'admin',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('service_icons', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'in_downtime',
            'output',
            'service_is_flapping',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('WARN Services of Hostgroup'),
    },
    'hostgroupservices_crit': {
        'browser_reload': 60,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All crit services of a certain hostgroup'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('st2', 'on'),
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('is_in_downtime', '-1'),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'table',
        'mustsearch': False,
        'name': 'hostgroupservices_crit',
        'num_columns': 1,
        'owner': 'admin',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('service_icons', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'in_downtime',
            'output',
            'service_is_flapping',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('CRIT Services of Hostgroup'),
    },
    'hostgroupservices_unknwn': {
        'browser_reload': 60,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All unknown services of a certain hostgroup'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('st3', 'on'),
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('is_in_downtime', '-1'),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'table',
        'mustsearch': False,
        'name': 'hostgroupservices_unknwn',
        'num_columns': 1,
        'owner': 'admin',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('service_icons', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'in_downtime',
            'output',
            'service_is_flapping',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('UNKNOWN Services of Hostgroup'),
    },
    'hostgroupservices_pend': {
        'browser_reload': 60,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All pending services of a certain hostgroup'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host_with_state', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('stp', 'on'),
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('is_in_downtime', '-1'),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': True,
        'hide_filters': ['hostgroup'],
        'layout': 'table',
        'mustsearch': False,
        'name': 'hostgroupservices_pend',
        'num_columns': 1,
        'owner': 'admin',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('service_icons', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'in_downtime',
            'output',
            'service_is_flapping',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('PEND Services of Hostgroup'),
    },
    'hostgroups': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'merged_hostgroups',
        'description': _(
            'A short overview over all host groups, without an explicity listing of the actual hosts'
        ),
        'group_painters': [],
>>>>>>> upstream/master
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostgroups',
        'num_columns': 3,
        'owner': '',
        'painters': [
            ('hg_name', 'hostgroup'),
            ('hg_alias', None),
<<<<<<< HEAD
            ('hg_num_hosts_up', None),
            ('hg_num_hosts_down', None),
            ('hg_num_hosts_unreach', None),
            ('hg_num_hosts_pending', None),
            ('hg_num_services_ok', None),
            ('hg_num_services_warn', None),
            ('hg_num_services_crit', None),
            ('hg_num_services_unknown', None),
            ('hg_num_services_pending', None),
=======
            ('hg_num_hosts_up', 'hostgroup_up'),
            ('hg_num_hosts_down', 'hostgroup_down'),
            ('hg_num_hosts_unreach', 'hostgroup_unreach'),
            ('hg_num_hosts_pending', 'hostgroup_pend'),
            ('hg_num_services_ok', 'hostgroupservices_ok'),
            ('hg_num_services_warn', 'hostgroupservices_warn'),
            ('hg_num_services_crit', 'hostgroupservices_crit'),
            ('hg_num_services_unknown', 'hostgroupservices_unknwn'),
            ('hg_num_services_pending', 'hostgroupservices_pend'),
>>>>>>> upstream/master
        ],
        'public': True,
        'show_filters': ['hostgroupnameregex', 'hostgroupvisibility'],
        'sorters': [],
<<<<<<< HEAD
        'title': _('Host Groups (Summary)'),
        'topic': _('Host Groups')
=======
        'title': _('Host groups'),
        "topic": "overview",
        'icon': "hostgroups",
        "sort_index": 60,
>>>>>>> upstream/master
    },
    'hostproblems': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _(
            'A complete list of all host problems with a search form for selecting handled and unhandled'
        ),
        'group_painters': [('host_state', None)],
        'hard_filters': ['host_scheduled_downtime_depth'],
        'hard_filtervars': [
            ('is_host_scheduled_downtime_depth', '0'),
            ('is_host_in_notification_period', '-1'),
            ('hst0', ''),
            ('hst1', 'on'),
            ('hst2', 'on'),
            ('hstp', ''),
            ('is_host_acknowledged', '-1'),
            ('host', ''),
            ('opthostgroup', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostproblems',
        'num_columns': 3,
        'owner': '',
        'painters': host_view_painters,
        'play_sounds': True,
        'public': True,
        'show_filters': [
            'host_in_notification_period', 'hoststate', 'hostregex', 'opthostgroup',
            'host_acknowledged'
        ],
        'sorters': [],
        'title': _('Host problems'),
<<<<<<< HEAD
        'topic': _('Problems')
    },
    'hostsbygroup': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hostsbygroup',
        'description': _('A complete listing of all host groups and each of their hosts'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('hg_alias', 'hostgroup'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_host_scheduled_downtime_depth', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('site', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostsbygroup',
        'num_columns': 2,
        'owner': '',
        'painters': host_view_painters,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'siteopt',
        ],
        'sorters': [
            ('site', False),
            ('hostgroup', False),
            ('site_host', False),
        ],
        'title': _('Host Groups'),
        'topic': _('Host Groups')
=======
        "topic": "problems",
        'icon': 'host_problems',
        "sort_index": 20,
>>>>>>> upstream/master
    },
    'hoststatus': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _('Shows details of a host.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'icon': 'status',
        'layout': 'dataset',
        'mustsearch': False,
        'name': 'hoststatus',
        'owner': '',
        'painters': [
            # 1. Identification and icons
            ('sitealias', None),
            ('host', 'host'),
            ('host_addresses', None),
            ('alias', None),
            ('host_labels', None),
            ('host_icons', None),

            # 2. State and metrics
            ('host_state', None),
            ('host_plugin_output', None),
            ('host_pnpgraph', None),
            ('host_perf_data', None),
            ('host_in_downtime', None),

            # 2b. Serivce statistics
            ('num_services', None),
            ('num_services_ok', 'host_ok'),
            ('num_services_warn', 'host_warn'),
            ('num_services_crit', 'host_crit'),
            ('num_services_unknown', 'host_unknown'),
            ('num_services_pending', 'host_pending'),

            # 3. Runtime data, timestamps
            ('host_attempt', None),
            ('host_state_age', None),
            ('host_check_age', None),
            ('host_next_check', None),
            ('host_check_latency', None),
            ('host_check_duration', None),

            # 4. Notification
            ('host_notifper', None),
            ('host_in_notifper', None),
            ('host_notification_number', None),
            ('host_last_notification', None),
            ('host_next_notification', None),
            ('host_notification_postponement_reason', None),

            # 5. Configuration
            ('host_parents', None),
            ('host_childs', None),
            ('host_check_interval', None),
            ('host_contact_groups', None),
            ('host_contacts', None),
            ('host_group_memberlist', None),
            ('host_servicelevel', None),
            ('host_check_command', None),
            ('host_custom_vars', None),
            ('host_custom_notes', None),
        ],
        'public': True,
        'show_filters': [],
        'sorters': [],
<<<<<<< HEAD
        'linktitle': _('Host status'),
        'title': _('Status of Host')
=======
        'title': _('Status of Host'),
        'topic': 'monitoring',
>>>>>>> upstream/master
    },
    'pendingsvc': {
        'browser_reload': 30,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('Lists all services in state PENDING.'),
        'group_painters': [('host', 'host')],
        'hard_filters': ['svcstate'],
        'hard_filtervars': [
            ('st0', ''),
            ('st1', ''),
            ('st2', ''),
            ('st3', ''),
            ('stp', 'on'),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Pending Services'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'pendingsvc',
        'num_columns': 5,
        'owner': '',
        'painters': [('service_description', 'service')],
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [],
<<<<<<< HEAD
        'title': _('Pending Services'),
        'topic': _('Problems')
=======
        'title': _('Pending services'),
        'topic': "analyze",
        'icon': {
            'icon': 'services',
            'emblem': 'pending'
        },
        "sort_index": 50,
        "is_show_more": True,
>>>>>>> upstream/master
    },
    'searchhost': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _('A form for searching hosts using flexible filters'),
        'group_painters': [('sitealias', None)],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': True,
        'name': 'searchhost',
        'num_columns': 3,
        'owner': '',
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'host_in_service_period',
            'hoststate',
            'siteopt',
            'hostregex',
            'hostgroups',
            'opthostgroup',
            'opthost_contactgroup',
            'host_check_command',
            'host_address',
            'host_notif_number',
            'host_staleness',
            'host_labels',
            'host_tags',
<<<<<<< HEAD
=======
            'host_auxtags',
>>>>>>> upstream/master
            'hostalias',
            'host_favorites',
            'host_num_services',
        ],
        'sorters': [],
        'title': _('Host search'),
<<<<<<< HEAD
        'topic': _('Hosts')
=======
        "topic": "overview",
        "sort_index": 30,
        'icon': {
            'icon': 'folder',
            'emblem': 'search'
        },
>>>>>>> upstream/master
    },
    'searchsvc': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description':
            _('Almost all available filters, used for searching services and maybe doing actions'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_service_in_notification_period', '-1'),
            ('optservicegroup', ''),
            ('is_service_notifications_enabled', '-1'),
            ('is_host_in_notification_period', '-1'),
            ('is_in_downtime', '-1'),
            ('is_service_scheduled_downtime_depth', '-1'),
            ('is_service_acknowledged', '-1'),
            ('host', ''),
            ('is_service_active_checks_enabled', '-1'),
            ('service', ''),
            ('check_command', ''),
            ('opthostgroup', ''),
            ('service_output', ''),
            ('is_service_is_flapping', '-1'),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': True,
        'name': 'searchsvc',
        'num_columns': 1,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'service_in_service_period',
            'optservicegroup',
            'optservice_contactgroup',
            'hostgroups',
            'servicegroups',
            'service_notifications_enabled',
            'host_in_notification_period',
            'in_downtime',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'host_address',
            'service_active_checks_enabled',
            'serviceregex',
            'service_display_name',
            'check_command',
            'hoststate',
            'svcstate',
            'svchardstate',
            'opthostgroup',
            'opthost_contactgroup',
            'output',
            'service_is_flapping',
            'svc_last_state_change',
            'svc_last_check',
            'siteopt',
            'aggr_service_used',
            'svc_notif_number',
            'service_staleness',
            'service_labels',
            'host_labels',
            'host_tags',
<<<<<<< HEAD
=======
            'host_auxtags',
>>>>>>> upstream/master
            'hostalias',
            'host_favorites',
            'service_favorites',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Service search'),
<<<<<<< HEAD
        'topic': _('Services')
=======
        "topic": "overview",
        'icon': {
            'icon': 'services',
            'emblem': 'search'
        },
        "sort_index": 40,
>>>>>>> upstream/master
    },
    'service': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('Status of a single service, to be used for linking'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['siteopt', 'service', 'host'],
        'layout': 'dataset',
        'mustsearch': False,
        'name': 'service',
        'num_columns': 1,
        'owner': '',
        'painters': [
            # 1. Identification and icons
            ('sitealias', None),
            ('host', 'hoststatus'),
            ('service_description', 'servicedesc'),
            ('service_labels', None),
            ('service_icons', None),

            # 2. State and metrics
            ('service_state', None),
            ('svc_plugin_output', None),
            ('svc_long_plugin_output', None),
            ('perfometer', None),
            ('svc_pnpgraph', None),
            ('svc_metrics', None),
            ('svc_in_downtime', None),

            # 3. Runtime data, timestamps
            ('svc_attempt', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
            ('svc_check_cache_info', None),
            ('svc_next_check', None),
            ('svc_last_time_ok', None),
            ('svc_check_latency', None),
            ('svc_check_duration', None),

            # 4. Notifications
            ('svc_notifper', None),
            ('svc_in_notifper', None),
            ('svc_notification_number', None),
            ('svc_last_notification', None),
            ('svc_next_notification', None),
            ('svc_notification_postponement_reason', None),

            # 5. Configuration
            ('svc_check_interval', None),
            ('svc_contact_groups', None),
            ('svc_contacts', None),
            ('svc_group_memberlist', None),
            ('svc_servicelevel', None),
            ('svc_check_command', None),
            ('svc_perf_data', None),
            ('svc_custom_vars', None),
            ('check_manpage', None),
            ('svc_custom_notes', None),
        ],
        'public': True,
        'show_filters': [],
        'sorters': [],
<<<<<<< HEAD
        'linktitle': _('Details'),
=======
>>>>>>> upstream/master
        'title': _('Service')
    },
    'servicedesc': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All Services with a certain description'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['service'],
        'layout': 'table',
        'icon': 'status',
        'mustsearch': False,
        'name': 'servicedesc',
        'num_columns': 2,
        'owner': '',
        'painters': [
            ('service_state', None),
            ('service_icons', None),
            ('host', 'service'),
            ('svc_plugin_output', None),
            ('perfometer', None),
        ],
        'public': True,
        'show_filters': ['hostregex', 'svcstate', 'opthostgroup'],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'user_sortable': 'on',
<<<<<<< HEAD
        'linktitle': _('Service globally'),
=======
>>>>>>> upstream/master
        'title': _('All Services with this description:')
    },
    'servicedescpnp': {
        'browser_reload': 90,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('Graphs for all Services with a certain description'),
        'group_painters': [('host', 'hostpnp')],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['service'],
        'icon': 'pnp',
        'layout': 'boxed',
<<<<<<< HEAD
        'linktitle': _('Graphs globally'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'servicedescpnp',
        'num_columns': 2,
        'owner': 'admin',
        'painters': [('svc_pnpgraph', None)],
        'play_sounds': False,
        'public': True,
        'show_filters': ['hostregex', 'svcstate', 'opthostgroup'],
        'sorters': [
            ('svcstate', False),
            ('site', False),
            ('site_host', False),
        ],
        'title': _('Graphs of services with description:'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        "topic": "history",
>>>>>>> upstream/master
    },
    'servicegroup': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('Services of a service group'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host', 'host'),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['servicegroup'],
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Service Group'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'servicegroup',
        'num_columns': 1,
        'owner': '',
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Service Group'),
<<<<<<< HEAD
        'topic': _('Other')
=======
>>>>>>> upstream/master
    },
    'sitehosts': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _('Link view showing all hosts of one site'),
        'group_painters': [
            ('site_icon', None),
            ('sitealias', 'sitesvcs'),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['site'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'sitehosts',
        'num_columns': 2,
        'owner': '',
        'painters': host_view_painters,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
<<<<<<< HEAD
        'linktitle': _('Complete site'),
        'title': _('All hosts of site')
    },
    'svcbygroups': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'servicesbygroup',
        'description': _(
            'Service grouped by service groups. Services not member of a group are not displayed. Services being in more groups, are displayed once for each group'
        ),
        'group_painters': [('sg_alias', 'servicegroup')],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'svcbygroups',
        'num_columns': 1,
        'owner': '',
        'painters': [('host', 'host')] + service_view_painters,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('servicegroup', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Services by group'),
        'topic': _('Service Groups')
    },
    'svcbyhgroups': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'servicesbyhostgroup',
        'description': _(
            'Service grouped by host groups. Services not member of a host group are not displayed. Services being in more groups, are displayed once for each group'
        ),
        'group_painters': [('hg_alias', 'hostgroup')],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'svcbyhgroups',
        'num_columns': 2,
        'owner': '',
        'painters': host_service_view_painters,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('hostgroup', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Serv. by host groups'),
        'topic': _('Services')
    },
    'svcgroups': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'servicegroups',
        'description': _(
            'A short overview over all service groups, without explicity listing of the actual hosts and services'
        ),
        'group_painters': [('sitealias', 'sitehosts')],
=======
        'title': _('All hosts of site')
    },
    'svcgroups': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'merged_servicegroups',
        'description': _(
            'A short overview over all service groups, without explicity listing of the actual hosts and services'
        ),
        'group_painters': [],
>>>>>>> upstream/master
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'svcgroups',
        'num_columns': 3,
        'owner': '',
        'painters': [
            ('sg_name', 'servicegroup'),
            ('sg_alias', None),
            ('sg_num_services_ok', None),
            ('sg_num_services_warn', None),
            ('sg_num_services_crit', None),
            ('sg_num_services_unknown', None),
            ('sg_num_services_pending', None),
        ],
        'public': True,
<<<<<<< HEAD
        'show_filters': ['servicegroupnameregex'],
        'sorters': [],
        'title': _('Service Groups (Summary)'),
        'topic': _('Service Groups')
    },
    'svcgroups_grid': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'servicegroups',
        'description': _(
            'A short overview over all service groups, without explicity listing of the actual hosts and services'
        ),
        'group_painters': [('sitealias', 'sitehosts')],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'svcgroups_grid',
        'num_columns': 3,
        'owner': '',
        'painters': [
            ('sg_name', 'servicegroup'),
            ('sg_alias', None),
            ('sg_services', None),
        ],
        'public': True,
        'show_filters': [],
        'sorters': [],
        'title': _('Service Groups (Grid)'),
        'topic': _('Service Groups'),
=======
        'show_filters': ['servicegroupnameregex'],
        'sorters': [],
        'title': _('Service groups'),
        "topic": "overview",
        'icon': 'servicegroups',
        "sort_index": 70,
>>>>>>> upstream/master
    },
    'svcproblems': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All problems of services not currently in a downtime.'),
        'group_painters': [('service_state', None)],
        'hard_filters': ['in_downtime'],
        'hard_filtervars': [
            ('is_in_downtime', '0'),
            ('st0', ''),
            ('st1', 'on'),
            ('st2', 'on'),
            ('st3', 'on'),
            ('stp', ''),
            ('hst0', 'on'),
            ('hst1', ''),
            ('hst2', ''),
            ('hstp', 'on'),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'svcproblems',
        'num_columns': 1,
        'owner': '',
        'painters': host_service_view_painters,
        'play_sounds': True,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'service_acknowledged',
            'svcstate',
            'svchardstate',
            'serviceregex',
            'host_labels',
            'host_tags',
<<<<<<< HEAD
=======
            'host_auxtags',
>>>>>>> upstream/master
            'hoststate',
        ],
        'sorters': [
            ('svcstate', True),
            ('stateage', False),
            ('svcdescr', False),
        ],
        'title': _('Service problems'),
<<<<<<< HEAD
        'topic': _('Problems')
    },
    'hosttiles': {
        'browser_reload': 30,
        'column_headers': 'off',
        'datasource': 'hostsbygroup',
        'description': _('Displays hosts in a tiled layout, where each host is a single tile.'),
        'group_painters': [
            ('hg_name', 'hostgroup'),
            ('hg_alias', None),
        ],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': False,
        'hide_filters': [],
        'layout': 'tiled',
        'mustsearch': False,
        'name': 'hosttiles',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('host', 'hoststatus'),
            ('host_address', None),
            ('host_icons', None),
            ('num_services', 'host'),
            ('num_problems', 'problemsofhost'),
            ('host_state', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_in_notification_period',
            'hoststate',
            'siteopt',
            'host_acknowledged',
            'hostregex',
            'host_notifications_enabled',
            'opthostgroup',
            'host_check_command',
            'opthost_contactgroup',
        ],
        'sorters': [],
        'title': _('All hosts (tiled)'),
        'topic': _('Hosts')
=======
        "topic": "problems",
        'icon': 'svc_problems',
        "sort_index": 30,
>>>>>>> upstream/master
    },
    'searchpnp': {
        'browser_reload': 90,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('Search for services and display their graphs'),
        'group_painters': [
            ('sitealias', 'sitehosts'),
            ('host', 'host'),
            ('service_description', 'service'),
        ],
        'hard_filters': [
            'service_process_performance_data',
            'has_performance_data',
        ],
        'hard_filtervars': [
            ('is_service_process_performance_data', '1'),
            ('is_has_performance_data', '1'),
        ],
        'hidden': False,
        'hide_filters': [],
<<<<<<< HEAD
        'icon': 'pnp',
=======
        'icon': {
            'icon': 'graph',
            'emblem': 'search'
        },
>>>>>>> upstream/master
        'layout': 'boxed',
        'mustsearch': True,
        'name': 'searchpnp',
        'num_columns': 2,
        'owner': '',
        'painters': [('svc_pnpgraph', None)],
        'play_sounds': False,
        'public': False,
        'show_filters': [
            'service_in_notification_period',
            'optservicegroup',
            'service_notifications_enabled',
            'host_in_notification_period',
            'service_scheduled_downtime_depth',
            'service_acknowledged',
            'hostregex',
            'service_active_checks_enabled',
            'serviceregex',
            'check_command',
            'svcstate',
            'opthostgroup',
            'in_downtime',
            'output',
            'service_is_flapping',
            'service_labels',
            'host_labels',
        ],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
<<<<<<< HEAD
        'title': _('Search Time Graphs'),
        'topic': _('Metrics')
=======
        'title': _('Search time graphs'),
        "topic": "history",
        "sort_index": 50,
        "is_show_more": True,
>>>>>>> upstream/master
    },
    'hostpnp': {
        'browser_reload': 90,
        'column_headers': 'off',
        'datasource': 'services',
        'description': _('All graphs for a certain host.'),
        'group_painters': [('service_description', 'service')],
        'hard_filters': ['service_process_performance_data', 'has_performance_data', 'svcstate'],
        'hard_filtervars': [
            ('is_service_process_performance_data', '1'),
            ('is_has_performance_data', '1'),
            ('st0', 'on'),
            ('st1', 'on'),
            ('st2', 'on'),
            ('st3', 'on'),
            ('stp', ''),
        ],
        'hidden': True,
        'icon': 'pnp',
        'hide_filters': ['siteopt', 'host'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'hostpnp',
        'num_columns': 2,
        'owner': '',
        'painters': [('svc_pnpgraph', None)],
        'play_sounds': False,
        'public': False,
        'show_filters': ['serviceregex', 'check_command'],
        'sorters': [
            ('site', False),
            ('site_host', False),
            ('svcdescr', False),
        ],
<<<<<<< HEAD
        'linktitle': _('Service graphs'),
        'title': _('Service graphs of host'),
=======
        'title': _('Service graphs of host'),
        "topic": "history",
>>>>>>> upstream/master
    },
    'recentsvc': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('Service whose state changed in the last 60 minutes'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [
            ('svc_last_state_change_from_range', '3600'),
            ('svc_last_state_change_from', '1'),
            ('st0', 'on'),
            ('st1', 'on'),
            ('st2', 'on'),
            ('st3', 'on'),
            ('stp', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Change ago:'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'svcrecent',
        'num_columns': 1,
        'owner': '',
        'painters': host_service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': ['svc_last_state_change', 'svcstate', 'siteopt'],
        'sorters': [('stateage', True)],
        'title': _('Recently changed services'),
<<<<<<< HEAD
        'topic': _('Services')
=======
        "topic": "history",
        "sort_index": 80,
        'icon': {
            'icon': 'services',
            'emblem': 'warning'
        },
>>>>>>> upstream/master
    },
    'uncheckedsvc': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _(
            'Services that have not been checked for too long according to their configured check intervals.'
        ),
        'group_painters': [('host', 'host')],
        'hard_filters': [
            'service_staleness',
            'service_scheduled_downtime_depth',
            'host_scheduled_downtime_depth',
        ],
        'hard_filtervars': [
            ('is_service_staleness', '1'),
            ('is_service_scheduled_downtime_depth', '0'),
            ('is_host_scheduled_downtime_depth', '0'),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': False,
<<<<<<< HEAD
        'icon': None,
=======
        'icon': 'stale',
>>>>>>> upstream/master
        'layout': 'table',
        'mobile': False,
        'mustsearch': False,
        'name': 'uncheckedsvc',
        'num_columns': 1,
        'painters': service_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
<<<<<<< HEAD
        'title': _('Stale services'),
        'topic': _('Problems'),
        'user_sortable': 'on',
=======
        'user_sortable': 'on',
        'title': _('Stale services'),
        "topic": "problems",
        "sort_index": 40,
        "is_show_more": True,
>>>>>>> upstream/master
    },
    'stale_hosts': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _('Hosts that have not been checked for too long.'),
        'group_painters': [('sitealias', None)],
        'hard_filters': ['host_staleness', 'host_scheduled_downtime_depth'],
        'hard_filtervars': [
            ('is_host_staleness', '1'),
            ('is_host_scheduled_downtime_depth', '0'),
        ],
        'hidden': True,
        'hide_filters': [],
        'hidebutton': False,
        'icon': None,
        'layout': 'boxed',
        'mobile': False,
        'mustsearch': False,
        'name': 'stale_hosts',
        'num_columns': 1,
        'painters': host_view_painters,
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [
            ('site_host', False),
            ('host_name', False),
        ],
        'title': _('Stale hosts'),
<<<<<<< HEAD
        'topic': _('Problems'),
=======
        'topic': 'problems',
>>>>>>> upstream/master
        'user_sortable': 'on',
    },
    'events': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log_events',
        'description': _('All historic events of hosts or services (alerts, downtimes, etc.)'),
        'group_painters': [('log_date', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('siteopt', ''),
            ('host', ''),
            ('service', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '7'),
            ('log_plugin_output', ''),
        ],
        'hidden': False,
        'hide_filters': [],
<<<<<<< HEAD
        'icon': 'history',
        'layout': 'table',
        'linktitle': _('Events'),
=======
        'icon': 'event',
        'layout': 'table',
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'events',
        'num_columns': 1,
        'owner': 'admin',
        'painters': [
            ('log_icon', None),
            ('log_time', None),
            ('log_type', None),
            ('host', 'hostsvcevents'),
            ('service_description', 'svcevents'),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'siteopt',
            'hostregex',
            'serviceregex',
            'logtime',
            'log_plugin_output',
            'log_state',
            'log_class',
            'log_notification_phase',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Host- and Service events'),
        'topic': _('Other')
=======
        'title': _('Host & service events'),
        "topic": "history",
        "sort_index": 10,
>>>>>>> upstream/master
    },
    'hostevents': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log_host_events',
        'description':
            _('All historic events concerning the state of a certain host (without services)'),
        'group_painters': [('log_date', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('logtime_from_range', '86400'),
            ('logtime_from', '7'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'icon': 'history',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host history'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'events',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('log_icon', None),
            ('log_time', None),
            ('log_type', None),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': ['logtime', 'log_state'],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Events of host')
=======
        'title': _('Events of host'),
        'topic': "history",
>>>>>>> upstream/master
    },
    'host_dt_hist': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log_events',
        'description': _('All historic scheduled downtimes of a certain host'),
        'group_painters': [],
        'hard_filters': ['log_type'],
        'hard_filtervars': [
            ('logtime_from_range', '86400'),
            ('logtime_from', '60'),
            ('log_type', 'HOST DOWNTIME ALERT'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'icon': 'downtime',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host Dt-History'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'num_columns': 1,
        'painters': [
            ('log_icon', None),
            ('log_time', None),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': ['logtime'],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Historic downtimes of host')
=======
        'title': _('Historic downtimes of host'),
        "topic": "history",
>>>>>>> upstream/master
    },
    'svcevents': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log_events',
        'description': _('All historic events concerning the state of a certain service'),
        'group_painters': [('log_date', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('logtime_from_range', '86400'),
            ('logtime_from', '7'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host', 'service'],
        'icon': 'history',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('History'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'events',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('log_icon', None),
            ('log_time', None),
            ('log_type', None),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': ['logtime', 'log_state'],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Events of service')
=======
        'title': _('Events of service'),
        'topic': "history",
>>>>>>> upstream/master
    },
    'svc_dt_hist': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log_events',
        'description': _('All historic scheduled downtimes of a certain service'),
        'group_painters': [],
        'hard_filters': ['log_type'],
        'hard_filtervars': [
            ('logtime_from_range', '86400'),
            ('logtime_from', '60'),
            ('log_type', '(HOST|SERVICE) DOWNTIME ALERT'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host', 'service'],
        'icon': 'downtime',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Downtime-History'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'num_columns': 1,
        'painters': [
            ('log_icon', None),
            ('log_time', None),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': ['logtime'],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Historic downtimes of service')
=======
        'title': _('Historic downtimes of service'),
        "topic": "history",
>>>>>>> upstream/master
    },
    'hostsvcevents': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log_events',
        'description':
            _('All historic events concerning the state of a certain host (including services)'),
        'group_painters': [('log_date', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('logtime_from_range', '86400'),
            ('logtime_from', '7'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'icon': 'history',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host/Svc history'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'events',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('log_icon', None),
            ('log_time', None),
            ('log_type', None),
            ('host', None),
            ('service_description', 'svcevents'),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': ['logtime', 'log_state', 'log_class', 'log_notification_phase'],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Events of host & services')
=======
        'title': _('Events of host & services'),
        'topic': "history",
>>>>>>> upstream/master
    },
    'logfile': {
        'browser_reload': 0,
        'column_headers': 'off',
        'datasource': 'log',
        'description': _('Displays entries from the logfile of the monitoring core.'),
        'group_painters': [('log_date', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('site', ''),
            ('logclass0', 'on'),
            ('logclass1', 'on'),
            ('logclass2', 'on'),
            ('logclass3', 'on'),
            ('logclass4', ''),
            ('logclass5', 'on'),
            ('logclass6', ''),
            ('logclass8', 'on'),
            ('host', ''),
            ('service', ''),
            ('opthostgroup', ''),
            ('neg_opthostgroup', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '7'),
        ],
        'hidden': False,
        'hide_filters': [],
<<<<<<< HEAD
        'icon': 'history',
        'layout': 'table',
        'linktitle': _('Search Global Logfile'),
=======
        'icon': {
            'icon': 'event',
            'emblem': 'search'
        },
        'layout': 'table',
>>>>>>> upstream/master
        'mustsearch': True,
        'name': 'logfile',
        'num_columns': 1,
        'owner': '',
        'painters': [
            ('log_icon', None),
            ('log_time', None),
            ('log_type', None),
            ('host', 'hostsvcevents'),
            ('service_description', 'svcevents'),
<<<<<<< HEAD
            ('log_state_type', None),
=======
            ('log_state_info', None),
>>>>>>> upstream/master
            ('log_plugin_output', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'optservicegroup',
            'siteopt',
            'log_class',
            'log_notification_phase',
            'hostregex',
            'serviceregex',
            'opthostgroup',
            'logtime',
            'log_state',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Search Global Logfile'),
        'topic': _('Other')
=======
        'title': _('Search history'),
        "topic": "history",
        "sort_index": 40,
        "is_show_more": True,
    },
    'sitesvcs_ok': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All OK services of a given site.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [('st0', 'on')],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'sitesvcs_ok',
        'num_columns': 2,
        'owner': 'maintenance',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
            ('service_icons', None),
            ('perfometer', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'optservicegroup',
            'hostregex',
            'serviceregex',
            'svcstate',
            'opthostgroup',
            'host_check_command',
            'output',
        ],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('OK Services of Site'),
    },
    'sitesvcs_warn': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All WARN services of a given site.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [('st1', 'on')],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'sitesvcs_warn',
        'num_columns': 2,
        'owner': 'maintenance',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
            ('service_icons', None),
            ('perfometer', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'optservicegroup',
            'hostregex',
            'serviceregex',
            'svcstate',
            'opthostgroup',
            'host_check_command',
            'output',
        ],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('WARN Services of Site'),
    },
    'sitesvcs_crit': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All CRIT services of a given site.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [('st2', 'on')],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'sitesvcs_crit',
        'num_columns': 2,
        'owner': 'maintenance',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
            ('service_icons', None),
            ('perfometer', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'optservicegroup',
            'hostregex',
            'serviceregex',
            'svcstate',
            'opthostgroup',
            'host_check_command',
            'output',
        ],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('CRIT Services of Site'),
    },
    'sitesvcs_unknwn': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All UNKNOWN services of a given site.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [('st3', 'on')],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'sitesvcs_unknwn',
        'num_columns': 2,
        'owner': 'maintenance',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
            ('service_icons', None),
            ('perfometer', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'optservicegroup',
            'hostregex',
            'serviceregex',
            'svcstate',
            'opthostgroup',
            'host_check_command',
            'output',
        ],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('UNKNOWN Services of Site'),
    },
    'sitesvcs_pend': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All pending services of a given site.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [('stp', 'on')],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt'],
        'layout': 'boxed',
        'mustsearch': False,
        'name': 'sitesvcs_pend',
        'num_columns': 2,
        'owner': 'maintenance',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
            ('service_icons', None),
            ('perfometer', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'optservicegroup',
            'hostregex',
            'serviceregex',
            'svcstate',
            'opthostgroup',
            'host_check_command',
            'output',
        ],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Pending Services of Site'),
>>>>>>> upstream/master
    },
    'sitesvcs': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('All services of a given site.'),
        'group_painters': [('host_with_state', 'hoststatus')],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hidebutton': True,
        'hide_filters': ['siteopt'],
        'layout': 'boxed',
<<<<<<< HEAD
        'linktitle': _('Services of Site'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'sitesvcs',
        'num_columns': 2,
        'owner': 'maintenance',
        'painters': [
            ('service_state', None),
            ('service_description', 'service'),
            ('svc_plugin_output', None),
            ('svc_state_age', None),
            ('svc_check_age', None),
            ('service_icons', None),
            ('perfometer', None),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'optservicegroup',
            'hostregex',
            'serviceregex',
            'svcstate',
            'opthostgroup',
            'host_check_command',
            'output',
        ],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Services of Site'),
<<<<<<< HEAD
        'topic': _('Services')
=======
>>>>>>> upstream/master
    },
    'alertstats': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'alert_stats',
        'description': _('Shows number of alerts grouped for each service.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [
            ('optservicegroup', ''),
            ('neg_optservicegroup', ''),
            ('site', ''),
            ('host', ''),
            ('service', ''),
            ('check_command', ''),
            ('log_plugin_output', ''),
            ('opthostgroup', ''),
            ('neg_opthostgroup', ''),
            ('host_check_command', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '31'),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': False,
        'layout': 'boxed',
<<<<<<< HEAD
        'linktitle': _('Alerts'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'alertstats',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('host', 'hostsvcevents'),
            ('service_description', 'svcevents'),
            ('alert_stats_crit', None),
            ('alert_stats_unknown', None),
            ('alert_stats_warn', None),
            ('alert_stats_problem', None),
        ],
        'play_sounds': False,
        'public': False,
        'show_filters': [
            'optservicegroup',
            'siteopt',
            'hostregex',
            'serviceregex',
            'check_command',
            'log_plugin_output',
            'opthostgroup',
            'host_check_command',
            'logtime',
            'log_state',
        ],
        'sorters': [
            ('alerts_crit', True),
            ('alerts_unknown', True),
            ('alerts_warn', True),
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Alert Statistics'),
<<<<<<< HEAD
        'topic': _('Problems')
=======
        "topic": "problems",
        "sort_index": 50,
        'icon': 'alert_statistics',
        "is_show_more": True,
>>>>>>> upstream/master
    },

    # Special views for NagStaMon
    'nagstamon_hosts': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _('The view is intended for NagStaMon as web service.'),
        'group_painters': [('host_state', None)],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': [],
        'hidebutton': True,
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host problems for NagStaMon'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'nagstamon_hosts',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('host', 'hoststatus', ''),
            ('host_icons', None, ''),
            ('host_check_age', None, ''),
            ('host_state_age', None, ''),
            ('host_attempt', None, ''),
            ('host_state', None, ''),
            ('host_plugin_output', None, ''),
            ('host_in_downtime', None, ''),
            ('host_acknowledged', None, ''),
            ('host_address', None, ''),
            ('host_in_downtime', None, ''),
            ('host_acknowledged', None, ''),
            ('sitename_plain', None, ''),
            ('host_flapping', None, ''),
            ('host_is_active', None, ''),
            ('host_notifications_enabled', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'host_active_checks_enabled',
            'hoststate',
            'host_acknowledged',
            'host_notifications_enabled',
        ],
        'sorters': [],
        'title': _('Host problems for NagStaMon'),
<<<<<<< HEAD
        'topic': None
=======
>>>>>>> upstream/master
    },
    'nagstamon_svc': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _('This view is intended for usage as web service for NagStaMon.'),
        'group_painters': [('service_state', None)],
        'hard_filters': [],
        'hard_filtervars': [
            ('st0', ''),
            ('st1', 'on'),
            ('st2', 'on'),
            ('st3', 'on'),
            ('stp', ''),
        ],
        'hidden': True,
        'hide_filters': [],
        'hidebutton': True,
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Service problems for NagStaMon'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'nagstamon_svc',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('host', 'hoststatus', ''),
            ('service_description', 'service', ''),
            ('service_icons', None, ''),
            ('service_state', None, ''),
            ('svc_check_age', None, ''),
            ('svc_state_age', None, ''),
            ('svc_attempt', None, ''),
            ('svc_plugin_output', None, ''),
            ('svc_flapping', None, ''),
            ('svc_notifications_enabled', None, ''),
            ('svc_is_active', None, ''),
            ('svc_in_downtime', None, ''),
            ('svc_acknowledged', None, ''),
            ('sitename_plain', None, ''),
            ('host_address', None, ''),
            ('svc_check_command', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'service_in_notification_period',
            'service_notifications_enabled',
            'hoststate',
            'service_acknowledged',
            'service_active_checks_enabled',
            'host_notifications_enabled',
            'svcstate',
            'in_downtime',
        ],
        'sorters': [
            ('svcstate', True),
            ('stateage', False),
            ('svcdescr', False),
        ],
        'title': _('Service problems for NagStaMon'),
<<<<<<< HEAD
        'topic': None,
=======
>>>>>>> upstream/master
    },
    'perf_matrix': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'context': {
            'serviceregex': {
                'service_regex': ''
            },
            'service_in_notification_period': {},
            'service_notifications_enabled': {},
            'hoststate': {},
            'service_acknowledged': {},
            'service_active_checks_enabled': {},
            'host_notifications_enabled': {},
            'svcstate': {},
            'in_downtime': {},
            'has_performance_data': {
                'is_has_performance_data': '1'
            },
        },
        'datasource': 'servicesbyhostgroup',
        'description':
            _('A Matrix of Performance data values from all hosts in a certain host group'),
        'group_painters': [('host', 'host', None)],
        'hidden': True,
        'hidebutton': False,
        'icon': 'matrix',
        'layout': 'matrix',
<<<<<<< HEAD
        'linktitle': _('Performance Matrix'),
=======
>>>>>>> upstream/master
        'num_columns': 12,
        'painters': [
            ('service_description', 'service', None),
            ('perfometer', None, None),
        ],
        'single_infos': ['hostgroup'],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
        'title': _('Matrix of Performance Data'),
        'user_sortable': True,
<<<<<<< HEAD
        'topic': None,
=======
>>>>>>> upstream/master
    },
    'perf_matrix_search': {
        'browser_reload': 60,
        'column_headers': 'pergroup',
        'context': {
            'service_in_notification_period': {},
            'service_in_service_period': {},
            'optservicegroup': {},
            'optservice_contactgroup': {},
            'hostgroups': {},
            'servicegroups': {},
            'service_notifications_enabled': {},
            'host_in_notification_period': {},
            'in_downtime': {},
            'service_scheduled_downtime_depth': {},
            'service_acknowledged': {},
            'hostregex': {},
            'host_address': {},
            'service_active_checks_enabled': {},
            'serviceregex': {},
            'service_display_name': {},
            'check_command': {},
            'hoststate': {},
            'svcstate': {},
            'svchardstate': {},
            'opthostgroup': {},
            'opthost_contactgroup': {},
            'output': {},
            'service_is_flapping': {},
            'svc_last_state_change': {},
            'svc_last_check': {},
            'siteopt': {},
            'aggr_service_used': {},
            'svc_notif_number': {},
            'service_staleness': {},
            'host_labels': {},
            'host_tags': {},
            'hostalias': {},
            'host_favorites': {},
            'service_favorites': {},
            'has_performance_data': {
                'is_has_performance_data': '1'
            },
            'service_labels': {},
        },
        'datasource': 'services',
        'description': _('A Matrix of performance data values, grouped by hosts and services'),
        'group_painters': [('host', 'host', None)],
        'hidden': False,
        'hidebutton': False,
        'icon': 'matrix',
        'layout': 'matrix',
        'num_columns': 12,
        'painters': [
            ('service_description', 'service', None),
            ('perfometer', None, None),
        ],
        'single_infos': [],
        'sorters': [
            ('site_host', False),
            ('svcdescr', False),
        ],
<<<<<<< HEAD
        'title': _('Search performance data'),
        'user_sortable': True,
        'topic': _("Metrics"),
        'mustsearch': True,
=======
        'user_sortable': True,
        'mustsearch': True,
        'title': _('Search performance data'),
        "topic": "history",
        "sort_index": 60,
>>>>>>> upstream/master
    },

    #
    #    ____            _
    #   | __ ) _   _ ___(_)_ __   ___  ___ ___
    #   |  _ \| | | / __| | '_ \ / _ \/ __/ __|
    #   | |_) | |_| \__ \ | | | |  __/\__ \__ \
    #   |____/ \__,_|___/_|_| |_|\___||___/___/
    #
    #    ___       _       _ _ _
    #   |_ _|_ __ | |_ ___| | (_) __ _  ___ _ __   ___ ___
    #    | || '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \ / __/ _ \
    #    | || | | | ||  __/ | | | (_| |  __/ | | | (_|  __/
    #   |___|_| |_|\__\___|_|_|_|\__, |\___|_| |_|\___\___|
    #                            |___/
    #

    # All Aggregations
    'aggr_all': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description': _('Displays all BI aggregations.'),
        'group_painters': [('aggr_group', 'aggr_group')],
        'hard_filters': [],
        'hard_filtervars': [
            ('host', ''),
            ('aggr_name_regex', ''),
            ('aggr_output', ''),
            ('birs0', 'on'),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', 'on'),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('birs-1', 'on'),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', 'on'),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('All Aggregations'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggr_all',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('aggr_state', None, ''),
            ('aggr_treestate', None, ''),
            ('aggr_hosts', None, ''),
        ],
        'play_sounds': False,
        'public': False,
        'show_filters': [
            'aggr_group',
            'aggr_group_tree',
            'aggr_hosts',
            'aggr_name_regex',
            'aggr_state',
            'aggr_output',
            'aggr_assumed_state',
            'aggr_effective_state',
        ],
        'sorters': [
            ('aggr_group', False),
            ('aggr_name', False),
        ],
        'title': _('All Aggregations'),
<<<<<<< HEAD
        'topic': _('Business Intelligence')
=======
        "topic": "bi",
        "sort_index": 10,
>>>>>>> upstream/master
    },

    # All aggregations of a certain group
    'aggr_group': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description': _('Displays all aggregations of a certain group.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [
            ('host', ''),
            ('aggr_name_regex', ''),
            ('aggr_output', ''),
            ('birs0', 'on'),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', 'on'),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('birs-1', 'on'),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', 'on'),
        ],
        'hidden': True,
        'hide_filters': ['aggr_group'],
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Aggregation group'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggr_group',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('aggr_state', None, ''),
            ('aggr_treestate', None, ''),
            ('aggr_hosts', None, ''),
        ],
        'play_sounds': False,
        'public': False,
        'show_filters': [
            'aggr_hosts',
            'aggr_name_regex',
            'aggr_state',
            'aggr_output',
            'aggr_assumed_state',
            'aggr_effective_state',
        ],
        'sorters': [('aggr_name', False)],
        'title': _('Aggregation group'),
<<<<<<< HEAD
        'topic': _('Business Intelligence')
=======
        'topic': "bi",
>>>>>>> upstream/master
    },

    # All host-only aggregations
    'aggr_singlehosts': {
        'browser_reload': 0,
        'column_headers': 'off',
        'datasource': 'bi_host_aggregations',
        'description': _('Lists all aggregations which only rely on information of one host.'),
        'group_painters': [('aggr_group', 'aggr_group')],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_host_scheduled_downtime_depth', '-1'),
            ('aggr_name_regex', ''),
            ('aggr_group', ''),
            ('birs0', 'on'),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', 'on'),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('birs-1', 'on'),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', 'on'),
            ('is_host_in_notification_period', '-1'),
            ('aggr_output', ''),
            ('site', ''),
            ('host', ''),
            ('opthostgroup', ''),
            ('neg_opthostgroup', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': True,
<<<<<<< HEAD
        'icon': 'aggr',
        'layout': 'table',
        'linktitle': _('Host Aggregations'),
=======
        'icon': 'aggr_single',
        'layout': 'table',
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggr_singlehosts',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('host', 'aggr_host', ''),
            ('host_icons', None, ''),
            ('aggr_treestate', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'aggr_name_regex',
            'aggr_group',
            'aggr_state',
            'host_in_notification_period',
            'aggr_output',
            'hoststate',
            'siteopt',
            'aggr_assumed_state',
            'hostregex',
            'opthostgroup',
            'aggr_effective_state',
        ],
        'sorters': [
            ('aggr_group', False),
            ('site_host', False),
        ],
<<<<<<< HEAD
        'title': _('Single-Host Aggregations'),
        'topic': _('Business Intelligence')
=======
        'title': _('Single host aggregations'),
        "topic": "bi",
        "sort_index": 40,
>>>>>>> upstream/master
    },

    # Aggregations that bear the name of a host
    'aggr_hostnameaggrs': {
        'browser_reload': 0,
        'column_headers': 'off',
        'datasource': 'bi_hostname_aggregations',
        'description': _('Host related aggregations'),
        'group_painters': [('aggr_group', 'aggr_group')],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_host_scheduled_downtime_depth', '-1'),
            ('aggr_name_regex', ''),
            ('aggr_group', ''),
            ('birs0', 'on'),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', 'on'),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('birs-1', 'on'),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', 'on'),
            ('is_host_in_notification_period', '-1'),
            ('aggr_output', ''),
            ('site', ''),
            ('host', ''),
            ('opthostgroup', ''),
            ('neg_opthostgroup', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': True,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host Aggregations'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('host', 'aggr_host', ''),
            ('host_icons', None, ''),
            ('aggr_treestate', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'aggr_name_regex',
            'aggr_group',
            'aggr_state',
            'host_in_notification_period',
            'aggr_output',
            'hoststate',
            'siteopt',
            'aggr_assumed_state',
            'hostregex',
            'opthostgroup',
            'aggr_effective_state',
        ],
        'sorters': [
            ('aggr_group', False),
            ('site_host', False),
        ],
<<<<<<< HEAD
        'title': _('Hostname Aggregations'),
        'topic': _('Business Intelligence')
=======
        'title': _('Hostname aggregations'),
        "topic": "bi",
        "sort_index": 20,
>>>>>>> upstream/master
    },

    # Single-Host Aggregations of a host
    'aggr_singlehost': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_host_aggregations',
        'description': _('A single host related aggregation'),
        'group_painters': [('aggr_name', None)],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host Aggregations'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggrhost',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('aggr_state', None, ''),
            ('aggr_treestate', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [],
        'sorters': [('aggr_name', False)],
        'title': _('Single-Host Aggregations of Host'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        'topic': "bi",
>>>>>>> upstream/master
    },

    # All aggregations affected by a certain host
    'aggr_host': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description': _('All aggregations the given host is part of'),
        'group_painters': [('aggr_group', 'aggr_group')],
        'hard_filters': [],
        'hard_filtervars': [
            ('aggr_name_regex', ''),
            ('aggr_output', ''),
            ('birs0', 'on'),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', 'on'),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('bias-1', 'on'),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', 'on'),
        ],
        'hidden': True,
        'hide_filters': [],
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Aggregations'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggr_host',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('aggr_state', None, ''),
            ('aggr_treestate', None, ''),
        ],
        'play_sounds': False,
        'public': False,
        'show_filters': [
            'aggr_group',
            'aggr_name_regex',
            'aggr_state',
            'aggr_output',
            'aggr_assumed_state',
            'aggr_effective_state',
            'aggr_hosts',
        ],
        'sorters': [('aggr_name', False)],
        'title': _('Aggregations Affected by Host'),
<<<<<<< HEAD
        'topic': _('Business Intelligence')
=======
        'topic': "bi",
>>>>>>> upstream/master
    },

    # All aggregations affected by a certain service (one one site/host!)
    'aggr_service': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description': _('All aggregations affected by a certain service'),
        'group_painters': [('aggr_group', 'aggr_group')],
        'hard_filters': [],
        'hard_filtervars': [
            ('aggr_name_regex', ''),
            ('aggr_output', ''),
            ('birs0', 'on'),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', 'on'),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('bias-1', 'on'),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', 'on'),
        ],
        'hidden': True,
        'hide_filters': [],
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Service Aggreg.'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggr_service',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('aggr_state', None, ''),
            ('aggr_treestate', None, ''),
        ],
        'play_sounds': False,
        'public': False,
        'show_filters': [
            'aggr_group',
            'aggr_name_regex',
            'aggr_state',
            'aggr_output',
            'aggr_assumed_state',
            'aggr_effective_state',
            'aggr_service',
        ],
        'sorters': [('aggr_name', False)],
        'title': _('Aggregations Affected by Service'),
<<<<<<< HEAD
        'topic': _('Business Intelligence')
=======
        'topic': "bi",
>>>>>>> upstream/master
    },

    # All Aggregations that have (real) problems
    'aggr_problems': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description': _('All aggregations that have a non-OK state (honoring state assumptions)'),
        'group_painters': [('aggr_group', 'aggr_group')],
        'hard_filters': [],
        'hard_filtervars': [
            ('host', ''),
            ('aggr_name_regex', ''),
            ('aggr_output', ''),
            ('birs0', ''),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', ''),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('bias-1', ''),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Problem Aggregations'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggr_all',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('aggr_state', None, ''),
            ('aggr_treestate', None, ''),
            ('aggr_hosts', None, ''),
        ],
        'play_sounds': True,
        'public': False,
        'show_filters': [
            'aggr_group',
            'aggr_hosts',
            'aggr_name_regex',
            'aggr_state',
            'aggr_output',
            'aggr_assumed_state',
            'aggr_effective_state',
        ],
        'sorters': [
            ('aggr_group', False),
            ('aggr_name', False),
        ],
<<<<<<< HEAD
        'title': _('Problem Aggregations'),
        'topic': _('Business Intelligence')
=======
        'title': _('Problem aggregations'),
        "topic": "bi",
        "sort_index": 30,
>>>>>>> upstream/master
    },

    # All single-host aggregations with problems
    'aggr_hostproblems': {
        'browser_reload': 0,
        'column_headers': 'off',
        'datasource': 'bi_host_aggregations',
        'description':
            _('All single-host aggregations that are in non-OK state (honoring state assumptions)'),
        'group_painters': [('aggr_group', 'aggr_group')],
        'hard_filters': [],
        'hard_filtervars': [
            ('is_host_scheduled_downtime_depth', '-1'),
            ('aggr_name_regex', ''),
            ('aggr_group', 'Hosts'),
            ('is_host_in_notification_period', '-1'),
            ('aggr_output', ''),
            ('birs0', 'on'),
            ('birs1', 'on'),
            ('birs2', 'on'),
            ('birs3', 'on'),
            ('birs-1', 'on'),
            ('bias0', 'on'),
            ('bias1', 'on'),
            ('bias2', 'on'),
            ('bias3', 'on'),
            ('bias-1', 'on'),
            ('biasn', 'on'),
            ('bies0', 'on'),
            ('bies1', 'on'),
            ('bies2', 'on'),
            ('bies3', 'on'),
            ('bies-1', 'on'),
            ('site', ''),
            ('host', ''),
            ('opthostgroup', ''),
            ('neg_opthostgroup', ''),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': True,
<<<<<<< HEAD
        'icon': 'aggr',
        'layout': 'table',
        'linktitle': _('Single-Host Problems'),
=======
        'icon': 'aggr_single_problem',
        'layout': 'table',
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'aggr_hostproblems',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('host', 'aggr_host', ''),
            ('host_icons', None, ''),
            ('aggr_treestate', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host_scheduled_downtime_depth',
            'aggr_name_regex',
            'aggr_group',
            'aggr_state',
            'host_in_notification_period',
            'aggr_output',
            'hoststate',
            'siteopt',
            'aggr_assumed_state',
            'hostregex',
            'opthostgroup',
            'aggr_effective_state',
        ],
        'sorters': [
            ('aggr_group', False),
            ('site_host', False),
        ],
<<<<<<< HEAD
        'title': _('Single-Host Problems'),
        'topic': _('Business Intelligence')
=======
        'title': _('Single host problems'),
        "topic": "bi",
        "sort_index": 50,
>>>>>>> upstream/master
    },

    # Shows a single aggregation which has to be set via aggr_name=<Name>
    'aggr_single': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description': _('Shows a single aggregation.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['aggr_name'],
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': 'All Aggregations',
=======
>>>>>>> upstream/master
        'mobile': False,
        'mustsearch': False,
        'name': 'aggr_single',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_icons', None, ''),
            ('aggr_state', None, ''),
            ('aggr_treestate', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_checkboxes': None,
        'show_filters': [],
        'sorters': [],
        'title': u'Single Aggregation',
<<<<<<< HEAD
        'topic': u'Business Intelligence',
=======
        'topic': "bi",
>>>>>>> upstream/master
        'user_sortable': None
    },

    # Shows minimal information about a multiple aggregation
    # Use together with output_format=python for API calls
    'aggr_all_api': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description': _(
            'List of all aggregations, containing the name of aggregations and state information'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': [],
        'hidebutton': True,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': 'All Aggregations',
=======
>>>>>>> upstream/master
        'mobile': False,
        'mustsearch': False,
        'name': 'aggr_all_api',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_group', None, ''),
            ('aggr_name', None, ''),
            ('aggr_state_num', None, ''),
            ('aggr_output', None, ''),
            ('aggr_treestate', None, ''),
            ('aggr_in_downtime', None, ''),
            ('aggr_acknowledged', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_checkboxes': None,
        'show_filters': [],
        'sorters': [],
        'title': u'List of all Aggregations for simple API calls',
<<<<<<< HEAD
        'topic': u'Business Intelligence',
=======
        'topic': "bi",
>>>>>>> upstream/master
        'user_sortable': None
    },

    # Shows minimal information about a single aggregation which has to be set via aggr_name=<Name>.
    # Use together with output_format=python for API calls
    'aggr_single_api': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'bi_aggregations',
        'description':
            _('Single Aggregation for simple API calls. Contains the state and state output.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': ['aggr_name'],
        'hidebutton': True,
        'icon': 'aggr',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': 'Single Aggregation',
=======
>>>>>>> upstream/master
        'mobile': False,
        'mustsearch': False,
        'name': 'aggr_single_api',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('aggr_state_num', None, ''),
            ('aggr_output', None, ''),
            ('aggr_in_downtime', None, ''),
            ('aggr_acknowledged', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_checkboxes': None,
        'show_filters': [],
        'sorters': [],
        'title': u'Single Aggregation for simple API calls',
<<<<<<< HEAD
        'topic': u'Business Intelligence',
=======
        'topic': "bi",
>>>>>>> upstream/master
        'user_sortable': None
    },

    # Summary of all aggregations for usage as web services
    'aggr_summary': {
        'browser_reload': 0,
        'column_headers': 'off',
        'datasource': 'bi_aggregations',
        'description':
            _('Simple summary page of all BI aggregates that is used as a web services.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': [],
        'hidebutton': True,
        'icon': None,
        'layout': 'boxed',
<<<<<<< HEAD
        'linktitle': u'BI Aggregations Summary State',
=======
>>>>>>> upstream/master
        'mobile': False,
        'mustsearch': False,
        'name': 'aggr_summary',
        'num_columns': 1,
        'painters': [
            ('aggr_name', None, ''),
            ('aggr_state', None, ''),
            ('aggr_output', None, ''),
        ],
        'play_sounds': False,
        'public': False,
        'show_checkboxes': None,
        'show_filters': [],
        'sorters': [],
        'title': u'BI Aggregations Summary State',
<<<<<<< HEAD
        'topic': u'Business Intelligence',
=======
        'topic': "bi",
>>>>>>> upstream/master
        'user_sortable': 'on',
    },

    # Hostgroup with boxed BIs for each host
    'aggr_hostgroup_boxed': {
        'browser_reload': 0,
        'column_headers': 'off',
        'context': {
            'aggr_group': {
                'aggr_group': ''
            },
            'hostregex': {
                'host_regex': ''
            },
        },
        'datasource': 'bi_hostnamebygroup_aggregations',
        'description': u'Hostgroup with boxed BIs for each host\n',
        'group_painters': [
            ('site_icon', '', None),
            ('sitealias', 'sitehosts', None),
        ],
        'hidden': True,
        'hidebutton': False,
        'icon': 'aggr',
        'layout': 'boxed',
<<<<<<< HEAD
        'linktitle': u'BI Boxes',
=======
>>>>>>> upstream/master
        'name': 'aggr_hostgroup_boxed',
        'num_columns': 2,
        'painters': [
            ('host_state', None, None),
            ('host', 'host', None),
            ('host_icons', None, None),
            ('alias', None, None),
            ('aggr_treestate_boxed', None, None),
        ],
        'public': True,
        'single_infos': ['hostgroup'],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
        'title': u'Hostgroup with BI state',
<<<<<<< HEAD
        'topic': u'hidden',
=======
>>>>>>> upstream/master
        'user_sortable': True
    },

    #   +----------------------------------------------------------------------+
    #   |       _   _       _   _  __ _           _   _                        |
    #   |      | \ | | ___ | |_(_)/ _(_) ___ __ _| |_(_) ___  _ __  ___        |
    #   |      |  \| |/ _ \| __| | |_| |/ __/ _` | __| |/ _ \| '_ \/ __|       |
    #   |      | |\  | (_) | |_| |  _| | (_| (_| | |_| | (_) | | | \__ \       |
    #   |      |_| \_|\___/ \__|_|_| |_|\___\__,_|\__|_|\___/|_| |_|___/       |
    #   |                                                                      |
    #   +----------------------------------------------------------------------+
    'hostnotifications': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log',
        'description': _('Notification events of hosts.'),
        'group_painters': [('log_date', None, '')],
        'hard_filters': ['log_class'],
        'hard_filtervars': [
            ('logclass0', ''),
            ('logclass1', ''),
            ('logclass2', ''),
            ('logclass3', 'on'),
            ('logclass4', ''),
            ('logclass5', ''),
            ('logclass6', ''),
            ('logclass8', ''),
            ('service', ''),
            ('log_plugin_output', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '90'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': False,
        'icon': 'notification',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host notifications'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'hostnotifications',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            (
                'log_icon',
                None,
            ),
            ('log_time', None, ''),
            ('log_contact_name', 'contactnotifications', ''),
            ('log_command', '', ''),
            ('log_state', None, ''),
            ('log_plugin_output', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'serviceregex',
            'log_plugin_output',
            'logtime',
            'log_state',
            'log_notification_phase',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
        'title': _('Notifications of host'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        'topic': "history",
>>>>>>> upstream/master
    },
    'hostsvcnotifications': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log',
        'description': _(
            'All notification events concerning the state of a certain host (including services)'),
        'group_painters': [('log_date', None, '')],
        'hard_filters': ['log_class'],
        'hard_filtervars': [
            ('logclass0', ''),
            ('logclass1', ''),
            ('logclass2', ''),
            ('logclass3', 'on'),
            ('logclass4', ''),
            ('logclass5', ''),
            ('logclass6', ''),
            ('logclass8', ''),
            ('service', ''),
            ('log_plugin_output', ''),
            ('log_plugin_output', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '90'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'host'],
        'hidebutton': False,
        'icon': 'notification',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Host/Svc notific.'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'hostsvcnotifications',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('log_icon', None),
            ('log_time', None, ''),
            ('log_contact_name', 'contactnotifications', ''),
            ('log_command', '', ''),
            ('log_type', None, ''),
            ('host', 'hostsvcnotifications', ''),
            ('service_description', 'svcnotifications', ''),
            ('log_state', None, ''),
            ('log_plugin_output', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'serviceregex',
            'log_plugin_output',
            'logtime',
            'log_state',
            'log_notification_phase',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
        'title': _('Notifications of host & services'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        'topic': "history",
>>>>>>> upstream/master
    },
    'notifications': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log',
        'description': _('All notification events of hosts or services.'),
        'group_painters': [('log_date', None, '')],
        'hard_filters': ['log_class'],
        'hard_filtervars': [
            ('logclass0', ''),
            ('logclass1', ''),
            ('logclass2', ''),
            ('logclass3', 'on'),
            ('logclass4', ''),
            ('logclass5', ''),
            ('logclass6', ''),
            ('logclass8', ''),
            ('site', ''),
            ('host', ''),
            ('service', ''),
            ('log_plugin_output', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '90'),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': False,
<<<<<<< HEAD
        'icon': 'notification',
        'layout': 'table',
        'linktitle': _('Notifications'),
=======
        'icon': 'notifications',
        'layout': 'table',
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'notifications',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('log_icon', None),
            ('log_time', None, ''),
            ('log_contact_name', 'contactnotifications', ''),
            ('log_command', '', ''),
            ('log_type', None, ''),
            ('host', 'hostsvcnotifications', ''),
            ('service_description', 'svcnotifications', ''),
            ('log_state', None, ''),
            ('log_plugin_output', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'siteopt',
            'hostregex',
            'serviceregex',
            'log_plugin_output',
            'logtime',
            'log_state',
            'log_notification_phase',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
<<<<<<< HEAD
        'title': _('Host- and Service notifications'),
        'topic': _('Other')
=======
        'title': _('Host & service history'),
        "topic": "history",
        "sort_index": 20,
>>>>>>> upstream/master
    },
    'failed_notifications': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log',
        'description': _('Failed notification events of hosts and services.'),
        'group_painters': [('log_date', None, '')],
        'hard_filters': ['log_class', 'log_type', 'log_state'],
        'hard_filtervars': [
            ('logclass0', ''),
            ('logclass1', ''),
            ('logclass2', ''),
            ('logclass3', 'on'),
            ('logclass4', ''),
            ('logclass5', ''),
            ('logclass6', ''),
            ('logclass8', ''),
            ('log_type', '.*NOTIFICATION RESULT$'),
            ('logst_h0', ''),
            ('logst_h1', 'on'),
            ('logst_h2', 'on'),
            ('logst_s0', ''),
            ('logst_s1', 'on'),
            ('logst_s2', 'on'),
            ('logst_s3', 'on'),
            ('site', ''),
            ('host', ''),
            ('service', ''),
            ('log_plugin_output', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '90'),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': True,
<<<<<<< HEAD
        'icon': 'notification',
        'layout': 'table',
        'linktitle': _('Notifications'),
=======
        'icon': {
            'icon': 'notifications',
            'emblem': 'warning'
        },
        'layout': 'table',
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'notifications',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('log_icon', None),
            ('log_time', None, ''),
            ('log_contact_name', 'contactnotifications', ''),
            ('log_command', '', ''),
            ('log_type', None, ''),
            ('host', 'hostsvcnotifications', ''),
            ('service_description', 'svcnotifications', ''),
            ('log_state', None, ''),
            ('log_plugin_output', None, ''),
            ('log_comment', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'siteopt',
            'hostregex',
            'serviceregex',
            'log_plugin_output',
            'logtime',
            'log_state',
            'log_notification_phase',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
        'title': _('Failed notifications'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        "topic": "analyze",
        "sort_index": 40,
>>>>>>> upstream/master
    },
    'svcnotifications': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log',
        'description': _('All notification events concerning the state of a certain service.'),
        'group_painters': [('log_date', None, '')],
        'hard_filters': ['log_class'],
        'hard_filtervars': [
            ('logclass0', ''),
            ('logclass1', ''),
            ('logclass2', ''),
            ('logclass3', 'on'),
            ('logclass4', ''),
            ('logclass5', ''),
            ('logclass6', ''),
            ('logclass8', ''),
            ('log_plugin_output', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '90'),
        ],
        'hidden': True,
        'hide_filters': ['siteopt', 'service', 'host'],
        'hidebutton': False,
        'icon': 'notification',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Notifications'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'svcnotifications',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('log_icon', None),
            ('log_time', None, ''),
            ('log_contact_name', 'contactnotifications', ''),
            ('log_command', '', ''),
            ('host', None, ''),
            ('log_state', None, ''),
            ('log_plugin_output', None, ''),
        ],
        'show_filters': [
            'log_plugin_output',
            'logtime',
            'log_state',
            'log_notification_phase',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
        'title': _('Service Notifications'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        'topic': "history",
>>>>>>> upstream/master
    },
    'contactnotifications': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log',
        'description': _('All notification events sent to'),
        'group_painters': [('log_date', None, '')],
        'hard_filters': ['log_class'],
        'hard_filtervars': [
            ('logclass0', ''),
            ('logclass1', ''),
            ('logclass2', ''),
            ('logclass3', 'on'),
            ('logclass4', ''),
            ('logclass5', ''),
            ('logclass6', ''),
            ('logclass8', ''),
            ('host', ''),
            ('service', ''),
            ('log_plugin_output', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '90'),
        ],
        'hidden': True,
        'hide_filters': ['log_contact_name'],
        'hidebutton': False,
        'icon': 'notification',
        'layout': 'table',
<<<<<<< HEAD
        'linktitle': _('Contact notification'),
=======
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'contactnotifications',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('log_icon', None),
            ('log_time', None, ''),
            ('log_command', '', ''),
            ('log_type', None, ''),
            ('host', 'hostsvcnotifications', ''),
            ('service_description', 'svcnotifications', ''),
            ('log_state', None, ''),
            ('log_plugin_output', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'host',
            'serviceregex',
            'log_plugin_output',
            'logtime',
            'log_state',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
        'title': _('Notifications of contact'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        'topic': "history",
>>>>>>> upstream/master
    },
    #   +----------------------------------------------------------------------+
    #   |     _    _           _     _                     _ _                 |
    #   |    / \  | | ___ _ __| |_  | |__   __ _ _ __   __| | | ___ _ __ ___   |
    #   |   / _ \ | |/ _ \ '__| __| | '_ \ / _` | '_ \ / _` | |/ _ \ '__/ __|  |
    #   |  / ___ \| |  __/ |  | |_  | | | | (_| | | | | (_| | |  __/ |  \__ \  |
    #   | /_/   \_\_|\___|_|   \__| |_| |_|\__,_|_| |_|\__,_|_|\___|_|  |___/  |
    #   |                                                                      |
    #   +----------------------------------------------------------------------+
    'alerthandlers': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'log',
        'description': _('All alert handler executions.'),
        'group_painters': [('log_date', None, '')],
        'hard_filters': ['log_class'],
        'hard_filtervars': [
            ('logclass0', ''),
            ('logclass1', ''),
            ('logclass2', ''),
            ('logclass3', ''),
            ('logclass4', ''),
            ('logclass5', ''),
            ('logclass6', ''),
            ('logclass8', 'on'),
            ('site', ''),
            ('host', ''),
            ('service', ''),
            ('log_plugin_output', ''),
            ('logtime_from_range', '86400'),
            ('logtime_from', '90'),
        ],
        'hidden': False,
        'hide_filters': [],
        'hidebutton': False,
<<<<<<< HEAD
        'icon': 'notification',
        'layout': 'table',
        'linktitle': _('Notifications'),
=======
        'icon': 'alert_handlers',
        'layout': 'table',
>>>>>>> upstream/master
        'mustsearch': False,
        'name': 'notifications',
        'num_columns': 1,
        'owner': 'cmkadmin',
        'painters': [
            ('log_icon', None),
            ('log_time', None, ''),
            ('log_command', '', ''),
            ('log_type', None, ''),
            ('host', 'hoststatus', ''),
            ('service_description', 'service', ''),
            ('log_state', None, ''),
            ('log_plugin_output', None, ''),
        ],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'siteopt',
            'hostregex',
            'serviceregex',
            'log_plugin_output',
            'logtime',
            'log_state',
            'log_notification_phase',
        ],
        'sorters': [
            ('log_time', True),
            ('log_lineno', True),
        ],
        'title': _('Alert handler executions'),
<<<<<<< HEAD
        'topic': _('Other')
=======
        "topic": "analyze",
        "sort_index": 20,
>>>>>>> upstream/master
    },
})

_host_view_context = {
    'host_acknowledged': {
        'is_host_acknowledged': '-1'
    },
    'host_check_command': {
        'host_check_command': ''
    },
    'host_in_notification_period': {
        'is_host_in_notification_period': '-1'
    },
    'host_in_service_period': {
        'is_host_in_service_period': '-1'
    },
    'host_notifications_enabled': {
        'is_host_notifications_enabled': '-1'
    },
    'host_scheduled_downtime_depth': {
        'is_host_scheduled_downtime_depth': '-1'
    },
    'host_tags': {
        'host_tag_0_grp': '',
        'host_tag_0_op': '',
        'host_tag_0_val': '',
        'host_tag_1_grp': '',
        'host_tag_1_op': '',
        'host_tag_1_val': '',
        'host_tag_2_grp': '',
        'host_tag_2_op': '',
        'host_tag_2_val': ''
    },
    'hostalias': {
        'hostalias': '',
        'neg_hostalias': ''
    },
    'hostgroups': {
        'hostgroups': '',
        'neg_hostgroups': ''
    },
    'hostregex': {
        'host_regex': '',
        'neg_host_regex': ''
    },
    'hoststate': {
        'hoststate_filled': '1',
        'hst0': 'on',
        'hst1': 'on',
        'hst2': 'on',
        'hstp': 'on'
    },
    'opthost_contactgroup': {
        'neg_opthost_contact_group': '',
        'opthost_contact_group': ''
    },
    'opthostgroup': {
        'neg_opthost_group': '',
        'opthost_group': ''
    },
    'siteopt': {
        'site': ''
    }
}


def _simple_host_view(custom_attributes, add_context=None):
    context = _host_view_context.copy()
    if add_context:
        context.update(add_context)

    view_spec = {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'force_checkboxes': False,
        'hidden': False,
        'hidebutton': False,
        'icon': None,
        'layout': 'table',
        'mobile': False,
        'mustsearch': False,
        'num_columns': 1,
        'play_sounds': False,
        'user_sortable': True,
        'context': context,
        'group_painters': [('sitealias', '', None),],
        'painters': [],
        'single_infos': [],
        'sorters': [
            ('site', False),
            ('site_host', False),
        ],
    }

    view_spec.update(custom_attributes)
    return view_spec


multisite_builtin_views["docker_nodes"] = _simple_host_view(
    {
        'title': _('Docker nodes'),
<<<<<<< HEAD
        'topic': _('Applications'),
=======
        "topic": "applications",
        'icon': 'docker',
        "sort_index": 10,
>>>>>>> upstream/master
        'description':
            _('Overall state of all docker nodes, with counts of services in the various states.'),
        'add_context_to_title': False,
        'painters': host_view_painters + [
            ('inv_software_applications_docker_version', None, None),
            ('inv_software_applications_docker_num_containers_total', None, None),
            ('inv_software_applications_docker_num_containers_running', None, None),
            ('inv_software_applications_docker_num_containers_paused', None, None),
            ('inv_software_applications_docker_num_containers_stopped', None, None),
        ],
    },
    add_context={
        'host_labels': {
            'host_label': '[{"value":"cmk/docker_object:node"}]'
        },
    },
)

multisite_builtin_views["docker_containers"] = _simple_host_view(
    {
        'title': _('Docker containers'),
<<<<<<< HEAD
        'topic': _('Applications'),
=======
        "topic": "applications",
        'icon': 'docker',
        "sort_index": 20,
>>>>>>> upstream/master
        'description': _(
            'Overall state of all docker containers, with counts of services in the various states.'
        ),
        'add_context_to_title': False,
        'painters': host_view_painters + [
            ('host_docker_node', None, None),
            ('perfometer', None, '', 'CPU utilization'),
            ('perfometer', None, '', 'Memory used'),
            ('perfometer', None, '', 'Uptime'),
        ],
    },
    add_context={
        'host_labels': {
            'host_label': '[{"value":"cmk/docker_object:container"}]'
        },
    },
)

multisite_builtin_views["vsphere_servers"] = _simple_host_view(
    {
        'title': _('vSphere Servers'),
<<<<<<< HEAD
        'topic': _('Applications'),
=======
        "topic": "applications",
        'icon': 'vsphere',
        "sort_index": 30,
>>>>>>> upstream/master
        'description': _(
            'Overall state of all vSphere servers, with counts of services in the various states.'),
        'add_context_to_title': False,
        'painters': host_view_painters
    },
    add_context={
        'host_labels': {
            'host_label': '[{"value":"cmk/vsphere_object:server"}]'
        },
    },
)

multisite_builtin_views["vpshere_vms"] = _simple_host_view(
    {
        'title': _('vSphere VMs'),
<<<<<<< HEAD
        'topic': _('Applications'),
        'description': _('Overall state of all vSphere based virtual machines.'),
        'add_context_to_title': False,
        'painters': host_view_painters + [
            ('svc_plugin_output', None, None, u'ESX Hostsystem', u'Server'),
            ('perfometer', None, '', 'CPU utilization'),
            ('perfometer', None, '', 'ESX Memory'),
            ('svc_plugin_output', None, None, u'ESX Guest Tools', u'Guest tools'),
=======
        "topic": "applications",
        'icon': 'vsphere',
        "sort_index": 40,
        'description': _('Overall state of all vSphere based virtual machines.'),
        'add_context_to_title': False,
        'painters': host_view_painters + [
            ('svc_plugin_output', None, None, 'ESX Hostsystem', 'Server'),
            ('perfometer', None, '', 'CPU utilization'),
            ('perfometer', None, '', 'ESX Memory'),
            ('svc_plugin_output', None, None, 'ESX Guest Tools', 'Guest tools'),
>>>>>>> upstream/master
        ],
    },
    add_context={
        'host_labels': {
            'host_label': '[{"value":"cmk/vsphere_object:vm"}]'
        },
    },
)
<<<<<<< HEAD
=======

multisite_builtin_views['crash_reports'] = {
    'description': _('List crash reports of all sites'),
    'title': _('Crash reports'),
    'browser_reload': 0,
    'column_headers': 'pergroup',
    'context': {},
    'datasource': 'crash_reports',
    'force_checkboxes': False,
    'group_painters': [('sitealias', '', None),],
    'hidden': False,
    'hidebutton': False,
    'icon': 'crash',
    'layout': 'table',
    'mobile': False,
    'mustsearch': False,
    'name': 'crash_reports',
    'num_columns': 1,
    'painters': [
        ('crash_ident', None, None),
        ('crash_type', None, None),
        ('crash_version', None, None),
        ('crash_time', None, None),
        ('crash_exception', None, None),
    ],
    'play_sounds': False,
    'single_infos': [],
    'sorters': [('sitealias', False), ('crash_time', True)],
    'user_sortable': True,
    "topic": "analyze",
    "sort_index": 30,
    "is_show_more": True,
}

multisite_builtin_views['cmk_servers'] = {
    'add_context_to_title': False,
    'browser_reload': 0,
    'column_headers': 'pergroup',
    'context': {
        'host_labels': {
            'host_label': '[{"value":"cmk/check_mk_server:yes"}]'
        }
    },
    'datasource': 'hosts',
    'description': u'Displaying the overall state of Checkmk servers\n',
    'force_checkboxes': False,
    'group_painters': [],
    'hidden': False,
    'hidebutton': True,
    'icon': "checkmk",
    'layout': 'table',
    'mobile': False,
    'mustsearch': False,
    'name': 'cmk_servers',
    'num_columns': 1,
    'painters': [
        (('host', {
            'color_choices': [
                'colorize_up', 'colorize_down', 'colorize_unreachable', 'colorize_pending',
                'colorize_downtime'
            ]
        }), 'host', 'host_addresses'),
        (('inv_software_os_name', {
            'use_short': True
        }), None, None),
        (('inv_hardware_cpu_cores', {
            'use_short': True
        }), None, None),
        (('inv_hardware_memory_total_ram_usable', {
            'use_short': True
        }), None, None),
        ('perfometer', None, None, u'CPU utilization'),
        ('perfometer', None, None, u'CPU load'),
        ('perfometer', None, None, u'Memory'),
        ('perfometer', None, None, u'Disk IO SUMMARY'),
    ],
    'play_sounds': False,
    'single_infos': [],
    'sorters': [('sitealias', False), ('host_name', False)],
    'user_sortable': True,
    'title': u'Checkmk servers',
    "topic": "applications",
    "sort_index": 50,
}


def cmk_sites_painters():
    service_painters: List[Any] = []
    if not cmk_version.is_raw_edition():
        service_painters += [
            ('invcmksites_cmc', None, None),
            ('invcmksites_dcd', None, None),
            ('invcmksites_liveproxyd', None, None),
            ('invcmksites_mknotifyd', None, None),
        ]
    else:
        service_painters += [
            ('invcmksites_nagios', None, None),
        ]

    service_painters += [
        ('invcmksites_mkeventd', None, None),
        ('invcmksites_apache', None, None),
        ('invcmksites_rrdcached', None, None),
        ('invcmksites_xinetd', None, None),
        ('invcmksites_crontab', None, None),
        ('invcmksites_stunnel', None, None),
    ]

    if cmk_version.is_raw_edition():
        service_painters += [
            ('invcmksites_npcd', None, None),
        ]

    return [
        (('host', {
            'color_choices': [
                'colorize_up', 'colorize_down', 'colorize_unreachable', 'colorize_pending',
                'colorize_downtime'
            ]
        }), 'host', 'host_addresses'),
        ('invcmksites_site', None, None),
        ('invcmksites_used_version', None, None),
        ('invcmksites_num_hosts', None, None),
        ('invcmksites_num_services', None, None),
        ('invcmksites_check_helper_usage', None, None),
        ('invcmksites_check_mk_helper_usage', None, None),
        ('invcmksites_livestatus_usage', None, None),
    ] + service_painters


multisite_builtin_views['cmk_sites'] = {
    'add_context_to_title': False,
    'browser_reload': 0,
    'column_headers': 'pergroup',
    'context': {
        'host_labels': {
            'host_label': '[{"value":"cmk/check_mk_server:yes"}]'
        },
    },
    'datasource': 'invcmksites',
    'description': u'Displaying the state of Checkmk sites\n',
    'force_checkboxes': False,
    'group_painters': [],
    'hidden': False,
    'hidebutton': True,
    'icon': "checkmk",
    'layout': 'table',
    'mobile': False,
    'mustsearch': False,
    'name': 'cmk_sites',
    'num_columns': 1,
    'painters': cmk_sites_painters(),
    'play_sounds': False,
    'single_infos': [],
    'sorters': [('sitealias', False), ('host_name', False)],
    'user_sortable': True,
    'title': u'Checkmk sites',
    "topic": "applications",
    "sort_index": 60,
}

multisite_builtin_views['cmk_sites_of_host'] = {
    'add_context_to_title': True,
    'browser_reload': 0,
    'column_headers': 'pergroup',
    'context': {},
    'datasource': 'invcmksites',
    'description': u'Displaying the state of Checkmk sites of the given host\n',
    'force_checkboxes': False,
    'group_painters': [],
    'hidden': True,
    'hidebutton': True,
    'icon': "checkmk",
    'layout': 'table',
    'mobile': False,
    'mustsearch': False,
    'name': 'cmk_sites',
    'num_columns': 1,
    'painters': cmk_sites_painters(),
    'play_sounds': False,
    'single_infos': ['host'],
    'sorters': [('sitealias', False), ('host_name', False)],
    'user_sortable': True,
    'title': u'Checkmk sites of host',
    'topic': 'applications',
}
>>>>>>> upstream/master
