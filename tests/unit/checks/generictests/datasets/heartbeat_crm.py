<<<<<<< HEAD
# yapf: disable
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

>>>>>>> upstream/master


checkname = 'heartbeat_crm'


freeze_time = '2019-04-11 12:38:36'


info = [[u'Stack:', u'corosync'],
        [u'Current',
         u'DC:',
         u'hrssc61i02',
         u'(version',
         u'1.1.19+20180928.0d2680780-1.8-1.1.19+20180928.0d2680780)',
         u'-',
         u'partition',
         u'with',
         u'quorum'],
        [u'Last', u'updated:', u'Mon', u'Mar', u'11', u'14:17:33', u'2019'],
        [u'Last',
         u'change:',
         u'Thu',
         u'Feb',
         u'28',
         u'17:40:07',
         u'2019',
         u'by',
         u'hacluster',
         u'via',
         u'cibadmin',
         u'on',
         u'hrssc61i01'],
        [u'2', u'nodes', u'configured'],
        [u'10', u'resources', u'configured'],
        [u'Online:', u'[', u'hrssc61i01', u'hrssc61i02', u']'],
        [u'Full', u'list', u'of', u'resources:'],
        [u'Resource', u'Group:', u'grp_IFG_ASCS22'],
        [u'_',
         u'rsc_ip_IFG_ASCS22',
         u'(ocf::heartbeat:IPaddr2):',
         u'Started',
         u'hrssc61i01'],
        [u'_',
         u'rsc_sap_IFG_ASCS22',
         u'(ocf::heartbeat:SAPInstance):',
         u'Started',
         u'hrssc61i01'],
        [u'Resource', u'Group:', u'grp_IFG_ERS23'],
        [u'_',
         u'rsc_ip_IFG_ERS23',
         u'(ocf::heartbeat:IPaddr2):',
         u'Started',
         u'hrssc61i02'],
        [u'_',
         u'rsc_sap_IFG_ERS23',
         u'(ocf::heartbeat:SAPInstance):',
         u'Started',
         u'hrssc61i02'],
        [u'Clone', u'Set:', u'clone_nfs_sapmnt_IFG', u'[nfs_sapmnt_IFG]'],
        [u'_', u'Started:', u'[', u'hrssc61i01', u'hrssc61i02', u']'],
        [u'Clone', u'Set:', u'clone_nfs_usr_sap_IFG', u'[nfs_usr_sap_IFG]'],
        [u'_', u'Started:', u'[', u'hrssc61i01', u'hrssc61i02', u']'],
        [u'st-vmware', u'(stonith:fence_vmware_rest):', u'Started', u'hrssc61i02'],
        [u'st-vmware2', u'(stonith:fence_vmware_rest):', u'Started', u'hrssc61i01'],
        [u'Failed', u'Resource', u'Actions:'],
        [u'*',
         u'st-vmware_monitor_20000',
         u'on',
         u'hrssc61i02',
         u"'unknown",
         u"error'",
         u'(1):',
         u'call=43,',
         u'status=Error,',
         u"exitreason='',"],
        [u'_',
         u"last-rc-change='Mon",
         u'Mar',
         u'4',
         u'09:29:54',
         u"2019',",
         u'queued=0ms,',
         u'exec=11096ms'],
        [u'*',
         u'st-vmware2_monitor_20000',
         u'on',
         u'hrssc61i01',
         u"'unknown",
         u"error'",
         u'(1):',
         u'call=43,',
         u'status=Error,',
         u"exitreason='',"],
        [u'_',
         u"last-rc-change='Mon",
         u'Mar',
         u'4',
         u'09:29:54',
         u"2019',",
         u'queued=0ms,',
         u'exec=11088ms']]


discovery = {'': [(None, {'num_nodes': 2, 'num_resources': 10})],
             'resources': [(u'clone_nfs_sapmnt_IFG', None),
                           (u'clone_nfs_usr_sap_IFG', None),
                           (u'grp_IFG_ASCS22', None),
                           (u'grp_IFG_ERS23', None),
                           (u'st-vmware', None),
                           (u'st-vmware2', None)]}


checks = {'': [(None,
                {'max_age': 60, 'num_nodes': 2, 'num_resources': 10},
<<<<<<< HEAD
                [(3, 'Ignoring reported data (Status output too old: 31 d)', [])])],
          'resources': [(u'clone_nfs_sapmnt_IFG',
                         {},
                         [(0,
                           u"clone_nfs_sapmnt_IFG Clone Started [u'hrssc61i01', u'hrssc61i02']",
=======
                [(2, 'Ignoring reported data (Status output too old: 31 d)', [])])],
          'resources': [(u'clone_nfs_sapmnt_IFG',
                         {},
                         [(0,
                           u"clone_nfs_sapmnt_IFG Clone Started hrssc61i01, hrssc61i02",
>>>>>>> upstream/master
                           [])]),
                        (u'clone_nfs_usr_sap_IFG',
                         {},
                         [(0,
<<<<<<< HEAD
                           u"clone_nfs_usr_sap_IFG Clone Started [u'hrssc61i01', u'hrssc61i02']",
=======
                           u"clone_nfs_usr_sap_IFG Clone Started hrssc61i01, hrssc61i02",
>>>>>>> upstream/master
                           [])]),
                        (u'grp_IFG_ASCS22',
                         {},
                         [(0,
                           u'rsc_ip_IFG_ASCS22 (ocf::heartbeat:IPaddr2): Started hrssc61i01',
                           []),
                          (0,
                           u'rsc_sap_IFG_ASCS22 (ocf::heartbeat:SAPInstance): Started hrssc61i01',
                           [])
                          ]),
                        (u'grp_IFG_ERS23',
                         {},
                         [(0,
                           u'rsc_ip_IFG_ERS23 (ocf::heartbeat:IPaddr2): Started hrssc61i02',
                           []),
                          (0,
                           u'rsc_sap_IFG_ERS23 (ocf::heartbeat:SAPInstance): Started hrssc61i02',
                           [])]),
                        (u'st-vmware',
                         {},
                         [(0,
                           u'st-vmware (stonith:fence_vmware_rest): Started hrssc61i02',
                           [])]),
                        (u'st-vmware2',
                         {},
                         [(0,
                           u'st-vmware2 (stonith:fence_vmware_rest): Started hrssc61i01',
<<<<<<< HEAD
                           [])])]}
=======
                           [])])]}
>>>>>>> upstream/master
