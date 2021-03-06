// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "TableComments.h"

#include <chrono>
#include <cstdint>
#include <memory>
#include <utility>
<<<<<<< HEAD
#include "Column.h"
#include "DowntimeOrComment.h"
#include "DowntimesOrComments.h"
#include "MonitoringCore.h"
#include "OffsetBoolColumn.h"
#include "OffsetIntColumn.h"
#include "OffsetSStringColumn.h"
#include "OffsetTimeColumn.h"
#include "Query.h"
#include "Row.h"
#include "Store.h"
=======

#include "BoolLambdaColumn.h"
#include "Column.h"
#include "DowntimeOrComment.h"
#include "DowntimesOrComments.h"
#include "IntLambdaColumn.h"
#include "MonitoringCore.h"
#include "Query.h"
#include "Row.h"
#include "Store.h"
#include "StringLambdaColumn.h"
>>>>>>> upstream/master
#include "TableHosts.h"
#include "TableServices.h"
#include "TimeLambdaColumn.h"
#include "auth.h"
#include "nagios.h"

// TODO(sp): the dynamic data in this table must be locked with a mutex

TableComments::TableComments(MonitoringCore *mc) : Table(mc) {
<<<<<<< HEAD
    addColumn(std::make_unique<OffsetSStringColumn>(
        "author", "The contact that entered the comment", -1, -1, -1,
        DANGEROUS_OFFSETOF(Comment, _author_name)));
    addColumn(std::make_unique<OffsetSStringColumn>(
        "comment", "A comment text", -1, -1, -1,
        DANGEROUS_OFFSETOF(Comment, _comment)));
    addColumn(std::make_unique<OffsetIntColumn>(
        "id", "The id of the comment", -1, -1, -1,
        DANGEROUS_OFFSETOF(Comment, _id)));
    addColumn(std::make_unique<OffsetTimeColumn>(
        "entry_time", "The time the entry was made as UNIX timestamp", -1, -1,
        -1, DANGEROUS_OFFSETOF(Comment, _entry_time)));
    addColumn(std::make_unique<OffsetIntColumn>(
        "type", "The type of the comment: 1 is host, 2 is service", -1, -1, -1,
        DANGEROUS_OFFSETOF(Comment, _type)));
    addColumn(std::make_unique<OffsetBoolColumn>(
        "is_service",
        "0, if this entry is for a host, 1 if it is for a service", -1, -1, -1,
        DANGEROUS_OFFSETOF(Comment, _is_service)));

    addColumn(std::make_unique<OffsetIntColumn>(
        "persistent", "Whether this comment is persistent (0/1)", -1, -1, -1,
        DANGEROUS_OFFSETOF(Comment, _persistent)));
    addColumn(std::make_unique<OffsetIntColumn>(
        "source", "The source of the comment (0 is internal and 1 is external)",
        -1, -1, -1, DANGEROUS_OFFSETOF(Comment, _source)));
    addColumn(std::make_unique<OffsetIntColumn>(
        "entry_type",
        "The type of the comment: 1 is user, 2 is downtime, 3 is flap and 4 is acknowledgement",
        -1, -1, -1, DANGEROUS_OFFSETOF(Comment, _entry_type)));
    addColumn(std::make_unique<OffsetIntColumn>(
        "expires", "Whether this comment expires", -1, -1, -1,
        DANGEROUS_OFFSETOF(Comment, _expires)));
    addColumn(std::make_unique<OffsetTimeColumn>(
        "expire_time", "The time of expiry of this comment as a UNIX timestamp",
        -1, -1, -1, DANGEROUS_OFFSETOF(Comment, _expire_time)));

    TableHosts::addColumns(this, "host_", DANGEROUS_OFFSETOF(Comment, _host),
                           -1);
    TableServices::addColumns(this, "service_",
                              DANGEROUS_OFFSETOF(Comment, _service),
=======
    ColumnOffsets offsets{};
    addColumn(std::make_unique<StringLambdaColumn<Comment>>(
        "author", "The contact that entered the comment", offsets,
        [](const Comment &r) { return r._author_name; }));
    addColumn(std::make_unique<StringLambdaColumn<Comment>>(
        "comment", "A comment text", offsets,
        [](const Comment &r) { return r._comment; }));
    addColumn(std::make_unique<IntLambdaColumn<Comment>>(
        "id", "The id of the comment", offsets,
        [](const Comment &r) { return r._id; }));
    addColumn(std::make_unique<TimeLambdaColumn<Comment>>(
        "entry_time", "The time the entry was made as UNIX timestamp", offsets,
        [](const Comment &r) {
            return std::chrono::system_clock::from_time_t(r._entry_time);
        }));
    addColumn(std::make_unique<IntLambdaColumn<Comment>>(
        "type", "The type of the comment: 1 is host, 2 is service", offsets,
        [](const Comment &r) { return r._type; }));
    addColumn(std::make_unique<BoolLambdaColumn<Comment>>(
        "is_service",
        "0, if this entry is for a host, 1 if it is for a service", offsets,
        [](const Comment &r) { return r._is_service; }));

    addColumn(std::make_unique<IntLambdaColumn<Comment>>(
        "persistent", "Whether this comment is persistent (0/1)", offsets,
        [](const Comment &r) { return r._persistent; }));
    addColumn(std::make_unique<IntLambdaColumn<Comment>>(
        "source", "The source of the comment (0 is internal and 1 is external)",
        offsets, [](const Comment &r) { return r._source; }));
    addColumn(std::make_unique<IntLambdaColumn<Comment>>(
        "entry_type",
        "The type of the comment: 1 is user, 2 is downtime, 3 is flapping and 4 is acknowledgement",
        offsets, [](const Comment &r) { return r._entry_type; }));
    addColumn(std::make_unique<IntLambdaColumn<Comment>>(
        "expires", "Whether this comment expires", offsets,
        [](const Comment &r) { return r._expires; }));
    addColumn(std::make_unique<TimeLambdaColumn<Comment>>(
        "expire_time", "The time of expiry of this comment as a UNIX timestamp",
        offsets, [](const Comment &r) {
            return std::chrono::system_clock::from_time_t(r._expire_time);
        }));

    TableHosts::addColumns(this, "host_", offsets.add([](Row r) {
        return r.rawData<Comment>()->_host;
    }));
    TableServices::addColumns(this, "service_", offsets.add([](Row r) {
        return r.rawData<Comment>()->_service;
    }),
>>>>>>> upstream/master
                              false /* no hosts table */);
}

std::string TableComments::name() const { return "comments"; }

std::string TableComments::namePrefix() const { return "comment_"; }

void TableComments::answerQuery(Query *query) {
    for (const auto &entry : core()->impl<Store>()->_comments) {
<<<<<<< HEAD
        if (!query->processDataset(Row(entry.second.get()))) {
=======
        // NOTE: Our typing is horrible here, so we need a downcast. Use
        // templates instead?
        const auto *r = static_cast<const Comment *>(entry.second.get());
        if (!query->processDataset(Row(r))) {
>>>>>>> upstream/master
            break;
        }
    }
}

bool TableComments::isAuthorized(Row row, const contact *ctc) const {
<<<<<<< HEAD
    auto dtc = rowData<DowntimeOrComment>(row);
=======
    const auto *dtc = rowData<DowntimeOrComment>(row);
>>>>>>> upstream/master
    return is_authorized_for(core(), ctc, dtc->_host, dtc->_service);
}
