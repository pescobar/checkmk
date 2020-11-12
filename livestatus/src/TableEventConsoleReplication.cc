// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "TableEventConsoleReplication.h"
<<<<<<< HEAD
#include <memory>
=======

#include <memory>

#include "Column.h"
>>>>>>> upstream/master
#include "DynamicColumn.h"
#include "DynamicEventConsoleReplicationColumn.h"
#include "Query.h"
#include "Row.h"

TableEventConsoleReplication::TableEventConsoleReplication(MonitoringCore *mc)
    : Table(mc) {
<<<<<<< HEAD
    addDynamicColumn(std::make_unique<DynamicEventConsoleReplicationColumn>(
        "value", "The replication value", mc, -1, -1, -1));
=======
    ColumnOffsets offsets{};
    addDynamicColumn(std::make_unique<DynamicEventConsoleReplicationColumn>(
        "value", "The replication value", mc, offsets));
>>>>>>> upstream/master
}

std::string TableEventConsoleReplication::name() const {
    return "eventconsolereplication";
}

std::string TableEventConsoleReplication::namePrefix() const {
    return "eventconsolereplication_";
}

void TableEventConsoleReplication::answerQuery(Query *query) {
    query->processDataset(Row(nullptr));
}
