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
checkname = 'dotnet_clrmemory'

info = [[
    u'AllocatedBytesPersec', u'Caption', u'Description', u'FinalizationSurvivors',
    u'Frequency_Object', u'Frequency_PerfTime', u'Frequency_Sys100NS', u'Gen0heapsize',
    u'Gen0PromotedBytesPerSec', u'Gen1heapsize', u'Gen1PromotedBytesPerSec', u'Gen2heapsize',
    u'LargeObjectHeapsize', u'Name', u'NumberBytesinallHeaps', u'NumberGCHandles',
    u'NumberGen0Collections', u'NumberGen1Collections', u'NumberGen2Collections',
    u'NumberInducedGC', u'NumberofPinnedObjects', u'NumberofSinkBlocksinuse',
    u'NumberTotalcommittedBytes', u'NumberTotalreservedBytes', u'PercentTimeinGC',
    u'PercentTimeinGC_Base', u'ProcessID', u'PromotedFinalizationMemoryfromGen0',
    u'PromotedMemoryfromGen0', u'PromotedMemoryfromGen1', u'Timestamp_Object',
    u'Timestamp_PerfTime', u'Timestamp_Sys100NS'
],
        [
            u'687389776176', u'', u'', u'1498', u'0', u'2734511', u'10000000', u'893649480',
            u'8245000', u'19597152', u'386480', u'66266864', u'10647216', u'_Global_', u'96511232',
            u'113029', u'128183', u'116842', u'4553', u'67', u'616', u'36628', u'233213952',
            u'22950764544', u'108935240', u'-1', u'0', u'588533', u'8245000', u'386480', u'0',
            u'12303331941741', u'131097013721920000'
        ],
        [
            u'661680', u'', u'', u'0', u'0', u'2734511', u'10000000', u'4194304', u'0', u'24', u'0',
            u'164512', u'34600', u'MonitoringHost', u'199136', u'42', u'16', u'16', u'16', u'16',
            u'5', u'6', u'401408', u'402644992', u'2', u'38453536', u'16060', u'0', u'0', u'0',
            u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'60848840', u'', u'', u'7', u'0', u'2734511', u'10000000', u'28891128', u'672',
            u'163960', u'384', u'3008248', u'132648', u'MonitoringHost#1', u'3304856', u'897',
            u'18', u'16', u'16', u'16', u'7', u'12', u'28057600', u'402644992', u'45', u'38453511',
            u'33276', u'672', u'672', u'384', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'2187714616', u'', u'', u'71', u'0', u'2734511', u'10000000', u'39878560', u'1454488',
            u'1454512', u'380984', u'4513576', u'3215032', u'MonitoringHost#2', u'9183120', u'1241',
            u'136', u'68', u'52', u'18', u'9', u'192', u'40366080', u'402644992', u'66761',
            u'308982', u'28536', u'20600', u'1454488', u'380984', u'0', u'12303331941741',
            u'131097013721920000'
        ],
        [
            u'297254747960', u'', u'', u'775', u'0', u'2734511', u'10000000', u'44739248',
            u'6555512', u'17536048', u'0', u'14616016', u'2746568', u'MonitoringHost#3',
            u'34898632', u'6881', u'9101', u'3366', u'2166', u'17', u'10', u'4032', u'92631040',
            u'402644992', u'167213', u'695370', u'19124', u'384482', u'6555512', u'0', u'0',
            u'12303331941741', u'131097013721920000'
        ],
        [
            u'0', u'', u'', u'0', u'0', u'2734511', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
            u'DTExec', u'0', u'549', u'0', u'0', u'0', u'0', u'0', u'178', u'0', u'0', u'0', u'0',
            u'0', u'0', u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'2935446472', u'', u'', u'14', u'0', u'2734511', u'10000000', u'4194304', u'6592',
            u'6616', u'1960', u'461680', u'480264', u'SQLAGENT', u'948560', u'323', u'512', u'256',
            u'256', u'0', u'147', u'3', u'5337088', u'402644992', u'4609', u'-1832862225', u'30168',
            u'5974', u'6592', u'1960', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'13492140976', u'', u'', u'380', u'0', u'2734511', u'10000000', u'4194304', u'197832',
            u'406064', u'0', u'42306592', u'2590216', u'WmiPrvSE', u'45302872', u'99735', u'3154',
            u'297', u'34', u'0', u'3', u'32163', u'49672192', u'402644992', u'13', u'114325298',
            u'8016', u'147879', u'197832', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'1226195984', u'', u'', u'119', u'0', u'2734511', u'10000000', u'4194304', u'11720',
            u'11144', u'480', u'318368', u'443592', u'SQLAGENT#1', u'773104', u'1213', u'345',
            u'71', u'69', u'0', u'144', u'11', u'5226496', u'402644992', u'8', u'36869171', u'6368',
            u'11424', u'11720', u'480', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'0', u'', u'', u'0', u'0', u'2734511', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
            u'SQLAGENT#2', u'0', u'160', u'0', u'0', u'0', u'0', u'0', u'2', u'0', u'0', u'0', u'0',
            u'0', u'0', u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'0', u'', u'', u'0', u'0', u'2734511', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
            u'SQLAGENT#3', u'0', u'160', u'0', u'0', u'0', u'0', u'0', u'2', u'0', u'0', u'0', u'0',
            u'0', u'0', u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'0', u'', u'', u'0', u'0', u'2734511', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
            u'SQLAGENT#4', u'0', u'160', u'0', u'0', u'0', u'0', u'0', u'2', u'0', u'0', u'0', u'0',
            u'0', u'0', u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'21479757040', u'', u'', u'13', u'0', u'2734511', u'10000000', u'4194304', u'6464',
            u'6488', u'2192', u'461072', u'463880', u'SQLAGENT#5', u'931440', u'325', u'3750',
            u'1875', u'1875', u'0', u'147', u'4', u'5320704', u'402644992', u'3199', u'1641551612',
            u'5508', u'6078', u'6464', u'2192', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'1226023960', u'', u'', u'119', u'0', u'2734511', u'10000000', u'4194304', u'11720',
            u'11144', u'480', u'318352', u'435536', u'SQLAGENT#6', u'765032', u'1219', u'345',
            u'71', u'69', u'0', u'144', u'11', u'5218304', u'402644992', u'6', u'36869223', u'6100',
            u'11424', u'11720', u'480', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'823606512', u'', u'', u'0', u'0', u'2734511', u'10000000', u'251658240', u'0', u'384',
            u'0', u'32816', u'34960', u'sqlservr', u'68160', u'24', u'23819', u'23819', u'0', u'0',
            u'0', u'2', u'327680', u'6442319872', u'212', u'359397718', u'4596', u'0', u'0', u'0',
            u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'1004853904', u'', u'', u'0', u'0', u'2734511', u'10000000', u'251658240', u'0',
            u'384', u'0', u'32816', u'34960', u'sqlservr#1', u'68160', u'24', u'29061', u'29061',
            u'0', u'0', u'0', u'2', u'327680', u'6442319872', u'213', u'179493968', u'2340', u'0',
            u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'2002890144', u'', u'', u'0', u'0', u'2734511', u'10000000', u'251658240', u'0',
            u'384', u'0', u'32816', u'34960', u'sqlservr#2', u'68160', u'24', u'57926', u'57926',
            u'0', u'0', u'0', u'2', u'327680', u'6442319872', u'215', u'179584857', u'3588', u'0',
            u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'0', u'', u'', u'0', u'0', u'2734511', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
            u'sqlservr#3', u'0', u'26', u'0', u'0', u'0', u'0', u'0', u'2', u'0', u'0', u'0', u'0',
            u'0', u'0', u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ],
        [
            u'0', u'', u'', u'0', u'0', u'2734511', u'10000000', u'0', u'0', u'0', u'0', u'0', u'0',
            u'sqlservr#4', u'0', u'26', u'0', u'0', u'0', u'0', u'0', u'2', u'0', u'0', u'0', u'0',
            u'0', u'0', u'0', u'0', u'0', u'12303331941741', u'131097013721920000'
        ]]

discovery = {'': [(u'_Global_', 'dotnet_clrmemory_defaultlevels')]}

checks = {
<<<<<<< HEAD
    '': [(u'_Global_', {
        "upper": (10.0, 15.0)
    }, [(0, '2.54% time in GC', [('percent', 2.5363462051694157, 10.0, 15.0, 0, 100)])])]
=======
    '': [
        (u'_Global_', {"upper": (10.0, 15.0)}, [
            (0, 'Time in GC: 2.54%', [
                ('percent', 2.5363462051694157, 10.0, 15.0, 0, 100),
            ]),
        ]),
    ],
>>>>>>> upstream/master
}
