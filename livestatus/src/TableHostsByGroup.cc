// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "TableHostsByGroup.h"

#include "Column.h"
#include "MonitoringCore.h"
#include "Query.h"
#include "Row.h"
#include "TableHostGroups.h"
#include "TableHosts.h"
#include "auth.h"
#include "nagios.h"

extern host *host_list;
extern hostgroup *hostgroup_list;

namespace {
struct hostbygroup {
<<<<<<< HEAD
    host hst;
    // cppcheck is too dumb to see usage in the DANGEROUS_OFFSETOF macro
    // cppcheck-suppress unusedStructMember
    hostgroup *host_group;
=======
    const host *hst;
    const hostgroup *host_group;
>>>>>>> upstream/master
};
}  // namespace

TableHostsByGroup::TableHostsByGroup(MonitoringCore *mc) : Table(mc) {
<<<<<<< HEAD
    TableHosts::addColumns(this, "", -1, -1);
    TableHostGroups::addColumns(this, "hostgroup_",
                                DANGEROUS_OFFSETOF(hostbygroup, host_group));
=======
    ColumnOffsets offsets{};
    TableHosts::addColumns(this, "", offsets.add([](Row r) {
        return r.rawData<hostbygroup>()->hst;
    }));
    TableHostGroups::addColumns(this, "hostgroup_", offsets.add([](Row r) {
        return r.rawData<hostbygroup>()->host_group;
    }));
>>>>>>> upstream/master
}

std::string TableHostsByGroup::name() const { return "hostsbygroup"; }

std::string TableHostsByGroup::namePrefix() const { return "host_"; }

void TableHostsByGroup::answerQuery(Query *query) {
    bool requires_authcheck =
        query->authUser() != nullptr &&
        core()->groupAuthorization() == AuthorizationKind::strict;

<<<<<<< HEAD
    for (hostgroup *hg = hostgroup_list; hg != nullptr; hg = hg->next) {
=======
    for (const hostgroup *hg = hostgroup_list; hg != nullptr; hg = hg->next) {
>>>>>>> upstream/master
        if (requires_authcheck &&
            !is_authorized_for_host_group(core(), hg, query->authUser())) {
            continue;
        }

<<<<<<< HEAD
        for (hostsmember *m = hg->members; m != nullptr; m = m->next) {
            hostbygroup hbg = {*m->host_ptr, hg};
=======
        for (const hostsmember *m = hg->members; m != nullptr; m = m->next) {
            hostbygroup hbg{m->host_ptr, hg};
>>>>>>> upstream/master
            if (!query->processDataset(Row(&hbg))) {
                return;
            }
        }
    }
}

bool TableHostsByGroup::isAuthorized(Row row, const contact *ctc) const {
<<<<<<< HEAD
    return is_authorized_for(core(), ctc, &rowData<hostbygroup>(row)->hst,
=======
    return is_authorized_for(core(), ctc, rowData<hostbygroup>(row)->hst,
>>>>>>> upstream/master
                             nullptr);
}
