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


checkname = 'elasticsearch_nodes'


info = [[u'DGfRL2s', u'open_file_descriptors', u'462'],
        [u'DGfRL2s', u'max_file_descriptors', u'4096'],
        [u'DGfRL2s', u'cpu_percent', u'0'],
        [u'DGfRL2s', u'cpu_total_in_millis', u'157950'],
        [u'DGfRL2s', u'mem_total_virtual_in_bytes', u'7135776768'],
        [u'fKw8YbK', u'open_file_descriptors', u'442'],
        [u'fKw8YbK', u'max_file_descriptors', u'4096'],
        [u'fKw8YbK', u'cpu_percent', u'0'],
        [u'fKw8YbK', u'cpu_total_in_millis', u'94820'],
        [u'fKw8YbK', u'mem_total_virtual_in_bytes', u'7106904064'],
        [u'ZwGy2o7', u'open_file_descriptors', u'453'],
        [u'ZwGy2o7', u'max_file_descriptors', u'4096'],
        [u'ZwGy2o7', u'cpu_percent', u'0'],
        [u'ZwGy2o7', u'cpu_total_in_millis', u'97700'],
        [u'ZwGy2o7', u'mem_total_virtual_in_bytes', u'7123750912'],
        [u'huh3AiI', u'open_file_descriptors', u'453'],
        [u'huh3AiI', u'max_file_descriptors', u'4096'],
        [u'huh3AiI', u'cpu_percent', u'0'],
        [u'huh3AiI', u'cpu_total_in_millis', u'96740'],
        [u'huh3AiI', u'mem_total_virtual_in_bytes', u'7106514944'],
        [u'g8YT0-P', u'open_file_descriptors', u'447'],
        [u'g8YT0-P', u'max_file_descriptors', u'4096'],
        [u'g8YT0-P', u'cpu_percent', u'0'],
        [u'g8YT0-P', u'cpu_total_in_millis', u'104530'],
        [u'g8YT0-P', u'mem_total_virtual_in_bytes', u'7122513920']]


discovery = {'': [(u'DGfRL2s', {}),
                  (u'ZwGy2o7', {}),
                  (u'fKw8YbK', {}),
                  (u'g8YT0-P', {}),
                  (u'huh3AiI', {})]}


checks = {'': [(u'DGfRL2s',
                {'cpu_levels': (75.0, 90.0)},
                [(0, 'CPU used: 0%', [('cpu_percent', 0.0, None, None, None, None)]),
                 (0,
                  'CPU total in ms: 157950',
                  [('cpu_total_in_millis', 157950, None, None, None, None)]),
                 (0,
                  'Total virtual memory: 6.65 GB',
                  [('mem_total_virtual_in_bytes',
                    7135776768,
                    None,
                    None,
                    None,
                    None)]),
                 (0,
                  'Open file descriptors: 462',
                  [('open_file_descriptors', 462, None, None, None, None)]),
                 (0,
                  'Max file descriptors: 4096',
                  [('max_file_descriptors', 4096, None, None, None, None)])]),
               (u'ZwGy2o7',
                {'cpu_levels': (75.0, 90.0)},
                [(0, 'CPU used: 0%', [('cpu_percent', 0.0, None, None, None, None)]),
                 (0,
                  'CPU total in ms: 97700',
                  [('cpu_total_in_millis', 97700, None, None, None, None)]),
                 (0,
                  'Total virtual memory: 6.63 GB',
                  [('mem_total_virtual_in_bytes',
                    7123750912,
                    None,
                    None,
                    None,
                    None)]),
                 (0,
                  'Open file descriptors: 453',
                  [('open_file_descriptors', 453, None, None, None, None)]),
                 (0,
                  'Max file descriptors: 4096',
                  [('max_file_descriptors', 4096, None, None, None, None)])]),
               (u'fKw8YbK',
                {'cpu_levels': (75.0, 90.0)},
                [(0, 'CPU used: 0%', [('cpu_percent', 0.0, None, None, None, None)]),
                 (0,
                  'CPU total in ms: 94820',
                  [('cpu_total_in_millis', 94820, None, None, None, None)]),
                 (0,
                  'Total virtual memory: 6.62 GB',
                  [('mem_total_virtual_in_bytes',
                    7106904064,
                    None,
                    None,
                    None,
                    None)]),
                 (0,
                  'Open file descriptors: 442',
                  [('open_file_descriptors', 442, None, None, None, None)]),
                 (0,
                  'Max file descriptors: 4096',
                  [('max_file_descriptors', 4096, None, None, None, None)])]),
               (u'g8YT0-P',
                {'cpu_levels': (75.0, 90.0)},
                [(0, 'CPU used: 0%', [('cpu_percent', 0.0, None, None, None, None)]),
                 (0,
                  'CPU total in ms: 104530',
                  [('cpu_total_in_millis', 104530, None, None, None, None)]),
                 (0,
                  'Total virtual memory: 6.63 GB',
                  [('mem_total_virtual_in_bytes',
                    7122513920,
                    None,
                    None,
                    None,
                    None)]),
                 (0,
                  'Open file descriptors: 447',
                  [('open_file_descriptors', 447, None, None, None, None)]),
                 (0,
                  'Max file descriptors: 4096',
                  [('max_file_descriptors', 4096, None, None, None, None)])]),
               (u'huh3AiI',
                {'cpu_levels': (75.0, 90.0)},
                [(0, 'CPU used: 0%', [('cpu_percent', 0.0, None, None, None, None)]),
                 (0,
                  'CPU total in ms: 96740',
                  [('cpu_total_in_millis', 96740, None, None, None, None)]),
                 (0,
                  'Total virtual memory: 6.62 GB',
                  [('mem_total_virtual_in_bytes',
                    7106514944,
                    None,
                    None,
                    None,
                    None)]),
                 (0,
                  'Open file descriptors: 453',
                  [('open_file_descriptors', 453, None, None, None, None)]),
                 (0,
                  'Max file descriptors: 4096',
<<<<<<< HEAD
                  [('max_file_descriptors', 4096, None, None, None, None)])])]}
=======
                  [('max_file_descriptors', 4096, None, None, None, None)])])]}
>>>>>>> upstream/master
