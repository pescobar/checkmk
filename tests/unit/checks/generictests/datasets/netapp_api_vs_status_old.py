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


checkname = 'netapp_api_vs_status'


info = [['kermit1_ng-mc', 'running'], ['bill_vm', 'stopped']]


discovery = {'': [('bill_vm', {}), ('kermit1_ng-mc', {})]}


checks = {'': [('bill_vm', {}, [(2, 'State: stopped', [])]),
<<<<<<< HEAD
               ('kermit1_ng-mc', {}, [(0, 'State: running', [])])]}
=======
               ('kermit1_ng-mc', {}, [(0, 'State: running', [])])]}
>>>>>>> upstream/master
