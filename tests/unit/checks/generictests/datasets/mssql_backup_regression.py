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

checkname = "mssql_backup"


info = [
     ['MSSQL_SQL0x4', 'master', '2016-07-08 20:20:27', 'D'],
     ['MSSQL_SQL0x4', 'model', '2016-07-08 20:20:28', 'D'],
     ['MSSQL_SQL0x4', 'model', '2016-07-12 09:09:42', 'L'],
     ['MSSQL_SQL0x4', 'model', '2016-07-11 20:20:07', 'I'],
     ['MSSQL_SQL0x4', 'msdb', '2016-07-08', '20:20:43', 'D'],
     ['MSSQL_SQL0x4', 'msdb', '-', '-', '-', 'no backup found'],
     ['MSSQL_SQL0x4', 'foo'],
     ['MSSQL_SQL0x4', 'bar', '12345678'],
     ['MSSQL_Parrot', 'Polly', '-', '-', '-', 'ERROR: Polly has no crackers']
]


discovery = {
    '': [
        ("MSSQL_SQL0x4 master", {}),
        ("MSSQL_SQL0x4 model", {}),
        ("MSSQL_SQL0x4 msdb", {}),
        ("MSSQL_SQL0x4 bar", {}),
        ("MSSQL_Parrot Polly", {}),
    ],
    'per_type': [],
}
