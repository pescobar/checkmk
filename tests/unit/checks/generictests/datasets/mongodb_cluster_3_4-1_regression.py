<<<<<<< HEAD
# -*- encoding: utf-8
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


checkname = 'mongodb_cluster'


info = [[u'{"settings":{"chunkSize":67108864},"shards":{"shard01":{"host":"shard01/shard01a:27018,shard01b:27018","state":1}},"balancer":{"numBalancerRounds":5200,"balancer_enabled":true,"mode":"full","inBalancerRound":false},"databases":{"shardedDB1":{"collstats":{"collections1":{"count":10000,"unique":false,"storageSize":270336,"ok":1.0,"avgObjSize":40.0,"dropped":false,"nchunks":1,"shards":{"shard01":{"count":10000,"ns":"shardedDB1.collections1","ok":1.0,"avgObjSize":40,"totalIndexSize":286720,"capped":false,"numberOfJumbos":0,"numberOfChunks":2,"nindexes":2,"storageSize":270336,"size":407428}},"totalIndexSize":286720,"sharded":true,"capped":false,"nindexes":2,"ns":"shardedDB1.collections1","size":407428},"collections2":{"count":10000,"unique":false,"storageSize":262144,"ok":1.0,"avgObjSize":39.0,"dropped":false,"nchunks":1,"shards":{"shard01":{"count":10000,"ns":"shardedDB1.collections2","ok":1.0,"avgObjSize":39,"totalIndexSize":286720,"capped":false,"numberOfJumbos":0,"numberOfChunks":2,"nindexes":2,"storageSize":262144,"size":399923}},"totalIndexSize":286720,"sharded":true,"capped":false,"nindexes":2,"ns":"shardedDB1.collections2","size":399923}},"collections":["collections1","collections2"],"primary":"shard01","partitioned":true},"shardedDB2":{"collstats":{"collections2":{"count":100000,"unique":false,"storageSize":2703360,"ok":1.0,"avgObjSize":40.0,"dropped":false,"nchunks":1,"shards":{"shard01":{"count":100000,"ns":"shardedDB2.collections2","ok":1.0,"avgObjSize":40,"totalIndexSize":3002368,"capped":false,"numberOfJumbos":0,"numberOfChunks":2,"nindexes":2,"storageSize":2703360,"size":4074555}},"totalIndexSize":3002368,"sharded":true,"capped":false,"nindexes":2,"ns":"shardedDB2.collections2","size":4074555}},"collections":["collections2"],"primary":"shard01","partitioned":true},"jumboDB1":{"collstats":{"collections1":{"count":0,"unique":false,"storageSize":4096,"ok":1.0,"avgObjSize":0.0,"dropped":false,"nchunks":1,"shards":{"shard01":{"count":0,"storageSize":4096,"ok":1.0,"totalIndexSize":8192,"capped":false,"numberOfJumbos":0,"numberOfChunks":2,"nindexes":2,"ns":"jumboDB1.collections1","size":0}},"totalIndexSize":8192,"sharded":true,"capped":false,"nindexes":2,"ns":"jumboDB1.collections1","size":0}},"collections":["collections1"],"primary":"shard01","partitioned":true},"unshardedDB1":{"collstats":{"collections1":{"count":1000,"storageSize":32768,"ok":1.0,"avgObjSize":35,"primary":"shard01","totalIndexSize":20480,"sharded":false,"capped":false,"nindexes":1,"ns":"unshardedDB1.collections1","size":35000}},"collections":["collections1"],"primary":"shard01","partitioned":true},"unshardedDB2":{"collstats":{"collections1":{"count":3000,"storageSize":61440,"ok":1.0,"avgObjSize":34,"primary":"shard01","totalIndexSize":40960,"sharded":false,"capped":false,"nindexes":1,"ns":"unshardedDB2.collections1","size":102000},"collections2":{"count":666,"storageSize":24576,"ok":1.0,"avgObjSize":36,"primary":"shard01","totalIndexSize":20480,"sharded":false,"capped":false,"nindexes":1,"ns":"unshardedDB2.collections2","size":23976}},"collections":["collections1","collections2"],"primary":"shard01","partitioned":false},"noColDB1":{"collstats":{},"collections":[],"primary":"shard01","partitioned":false}}}']]


discovery = {'': [('jumboDB1', {}),
                  ('noColDB1', {}),
                  ('shardedDB1', {}),
                  ('shardedDB2', {}),
                  ('unshardedDB1', {}),
                  ('unshardedDB2', {})],
             'balancer': [(None, {})],
             'collections': [(u'jumboDB1.collections1', {}),
                             (u'shardedDB1.collections1', {}),
                             (u'shardedDB1.collections2', {}),
                             (u'shardedDB2.collections2', {}),
                             (u'unshardedDB1.collections1', {}),
                             (u'unshardedDB2.collections1', {}),
                             (u'unshardedDB2.collections2', {})]}


checks = {'': [('jumboDB1',
                {},
                [(0, 'Partitioned: true', []),
                 (0, 'Collections: 1', []),
                 (0, u'Primary: shard01', [])]),
               ('noColDB1',
                {},
                [(0, 'Partitioned: false', []),
                 (1, 'Collections: 0', []),
                 (0, u'Primary: shard01', [])]),
               ('shardedDB1',
                {},
                [(0, 'Partitioned: true', []),
                 (0, 'Collections: 2', []),
                 (0, u'Primary: shard01', [])]),
               ('shardedDB2',
                {},
                [(0, 'Partitioned: true', []),
                 (0, 'Collections: 1', []),
                 (0, u'Primary: shard01', [])]),
               ('unshardedDB1',
                {},
                [(0, 'Partitioned: true', []),
                 (0, 'Collections: 1', []),
                 (0, u'Primary: shard01', [])]),
               ('unshardedDB2',
                {},
                [(0, 'Partitioned: false', []),
                 (0, 'Collections: 2', []),
                 (0, u'Primary: shard01', [])])],
          'balancer': [(None, {}, [(0, 'Balancer: enabled', [])])],
          'collections': [(u'jumboDB1.collections1',
                           {'levels_number_jumbo': (1, 2)},
                           [(0, 'Collection: sharded', []),
                            (0, 'Chunks: balanced', []),
                            (0, 'Balancer: enabled', []),
                            (0, 'Jumbo: 0', []),
                            (0,
                             u'\nCollection\n- Shards: 1\n- Chunks: 1 (Default chunk size: 64.00 MB)\n- Docs: 0\n- Size: 0.00 B\n- Storage: 4.00 kB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 0 (0.00%)\n--- per chunk: \u2248 0\n- Size: 0.00 B (0.00%)\n--- per chunk: \u2248 0.00 B\n- Host: shard01/shard01a:27018,shard01b:27018',
                             [('mongodb_collection_size',
                               0,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_collection_storage_size',
                               4096,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_document_count',
                               0,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_chunk_count', 1, None, None, None, None),
                              ('mongodb_jumbo_chunk_count', 0, 1, 2, None, None)])]),
                          (u'shardedDB1.collections1',
                           {'levels_number_jumbo': (1, 2)},
                           [(0, 'Collection: sharded', []),
                            (0, 'Chunks: balanced', []),
                            (0, 'Balancer: enabled', []),
                            (0, 'Jumbo: 0', []),
                            (0,
                             u'\nCollection\n- Shards: 1\n- Chunks: 1 (Default chunk size: 64.00 MB)\n- Docs: 10000\n- Size: 397.88 kB\n- Storage: 264.00 kB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 10000 (100.00%)\n--- per chunk: \u2248 5000\n- Size: 397.88 kB (100.00%)\n--- per chunk: \u2248 198.94 kB\n- Host: shard01/shard01a:27018,shard01b:27018',
                             [('mongodb_collection_size',
                               407428,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_collection_storage_size',
                               270336,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_document_count',
                               10000,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_chunk_count', 1, None, None, None, None),
                              ('mongodb_jumbo_chunk_count', 0, 1, 2, None, None)])]),
                          (u'shardedDB1.collections2',
                           {'levels_number_jumbo': (1, 2)},
                           [(0, 'Collection: sharded', []),
                            (0, 'Chunks: balanced', []),
                            (0, 'Balancer: enabled', []),
                            (0, 'Jumbo: 0', []),
                            (0,
                             u'\nCollection\n- Shards: 1\n- Chunks: 1 (Default chunk size: 64.00 MB)\n- Docs: 10000\n- Size: 390.55 kB\n- Storage: 256.00 kB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 10000 (100.00%)\n--- per chunk: \u2248 5000\n- Size: 390.55 kB (100.00%)\n--- per chunk: \u2248 195.27 kB\n- Host: shard01/shard01a:27018,shard01b:27018',
                             [('mongodb_collection_size',
                               399923,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_collection_storage_size',
                               262144,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_document_count',
                               10000,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_chunk_count', 1, None, None, None, None),
                              ('mongodb_jumbo_chunk_count', 0, 1, 2, None, None)])]),
                          (u'shardedDB2.collections2',
                           {'levels_number_jumbo': (1, 2)},
                           [(0, 'Collection: sharded', []),
                            (0, 'Chunks: balanced', []),
                            (0, 'Balancer: enabled', []),
                            (0, 'Jumbo: 0', []),
                            (0,
                             u'\nCollection\n- Shards: 1\n- Chunks: 1 (Default chunk size: 64.00 MB)\n- Docs: 100000\n- Size: 3.89 MB\n- Storage: 2.58 MB\n- Balancer: enabled\n\nShard shard01 (primary)\n- Chunks: 2\n- Jumbos: 0\n- Docs: 100000 (100.00%)\n--- per chunk: \u2248 50000\n- Size: 3.89 MB (100.00%)\n--- per chunk: \u2248 1.94 MB\n- Host: shard01/shard01a:27018,shard01b:27018',
                             [('mongodb_collection_size',
                               4074555,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_collection_storage_size',
                               2703360,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_document_count',
                               100000,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_chunk_count', 1, None, None, None, None),
                              ('mongodb_jumbo_chunk_count', 0, 1, 2, None, None)])]),
                          (u'unshardedDB1.collections1',
                           {'levels_number_jumbo': (1, 2)},
                           [(0, 'Collection: unsharded', []),
                            (0,
                             '\nCollection\n- Docs: 1000\n- Size: 34.18 kB\n- Storage: 32.00 kB\n',
                             [('mongodb_collection_size',
                               35000,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_collection_storage_size',
                               32768,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_document_count',
                               1000,
                               None,
                               None,
                               None,
                               None)])]),
                          (u'unshardedDB2.collections1',
                           {'levels_number_jumbo': (1, 2)},
                           [(0, 'Collection: unsharded', []),
                            (0,
                             '\nCollection\n- Docs: 3000\n- Size: 99.61 kB\n- Storage: 60.00 kB\n',
                             [('mongodb_collection_size',
                               102000,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_collection_storage_size',
                               61440,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_document_count',
                               3000,
                               None,
                               None,
                               None,
                               None)])]),
                          (u'unshardedDB2.collections2',
                           {'levels_number_jumbo': (1, 2)},
                           [(0, 'Collection: unsharded', []),
                            (0,
                             '\nCollection\n- Docs: 666\n- Size: 23.41 kB\n- Storage: 24.00 kB\n',
                             [('mongodb_collection_size',
                               23976,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_collection_storage_size',
                               24576,
                               None,
                               None,
                               None,
                               None),
                              ('mongodb_document_count',
                               666,
                               None,
                               None,
                               None,
<<<<<<< HEAD
                               None)])])]}
=======
                               None)])])]}
>>>>>>> upstream/master
