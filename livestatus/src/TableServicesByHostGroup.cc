// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "TableServicesByHostGroup.h"
<<<<<<< HEAD
=======

#include "Column.h"
>>>>>>> upstream/master
#include "Query.h"
#include "Row.h"
#include "TableHostGroups.h"
#include "TableServices.h"
#include "auth.h"
#include "nagios.h"

extern hostgroup *hostgroup_list;

namespace {
struct servicebyhostgroup {
<<<<<<< HEAD
    service svc;
    // cppcheck is too dumb to see usage in the DANGEROUS_OFFSETOF macro
    // cppcheck-suppress unusedStructMember
    hostgroup *host_group;
=======
    const service *svc;
    const hostgroup *host_group;
>>>>>>> upstream/master
};
}  // namespace

TableServicesByHostGroup::TableServicesByHostGroup(MonitoringCore *mc)
    : Table(mc) {
<<<<<<< HEAD
    TableServices::addColumns(this, "", -1, true);
    TableHostGroups::addColumns(
        this, "hostgroup_", DANGEROUS_OFFSETOF(servicebyhostgroup, host_group));
=======
    ColumnOffsets offsets{};
    TableServices::addColumns(this, "", offsets.add([](Row r) {
        return r.rawData<servicebyhostgroup>()->svc;
    }),
                              true);
    TableHostGroups::addColumns(this, "hostgroup_", offsets.add([](Row r) {
        return r.rawData<servicebyhostgroup>()->host_group;
    }));
>>>>>>> upstream/master
}

std::string TableServicesByHostGroup::name() const {
    return "servicesbyhostgroup";
}

std::string TableServicesByHostGroup::namePrefix() const { return "service_"; }

void TableServicesByHostGroup::answerQuery(Query *query) {
    for (const hostgroup *hg = hostgroup_list; hg != nullptr; hg = hg->next) {
        for (const hostsmember *mem = hg->members; mem != nullptr;
             mem = mem->next) {
            for (const servicesmember *smem = mem->host_ptr->services;
                 smem != nullptr; smem = smem->next) {
<<<<<<< HEAD
                servicebyhostgroup sbhg = {*smem->service_ptr, hg};
=======
                servicebyhostgroup sbhg{smem->service_ptr, hg};
>>>>>>> upstream/master
                if (!query->processDataset(Row(&sbhg))) {
                    return;
                }
            }
        }
    }
}

bool TableServicesByHostGroup::isAuthorized(Row row, const contact *ctc) const {
<<<<<<< HEAD
    auto svc = &rowData<servicebyhostgroup>(row)->svc;
=======
    const auto *svc = rowData<servicebyhostgroup>(row)->svc;
>>>>>>> upstream/master
    return is_authorized_for(core(), ctc, svc->host_ptr, svc);
}
