// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "HostGroupsColumn.h"
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Row.h"

#ifdef CMC
#include "Object.h"
#include "ObjectGroup.h"
#include "cmc.h"
#else
#include "auth.h"
#include "nagios.h"
#endif

std::vector<std::string> HostGroupsColumn::getValue(
    Row row, const contact *auth_user,
    std::chrono::seconds /*timezone_offset*/) const {
    std::vector<std::string> group_names;
#ifdef CMC
<<<<<<< HEAD
    (void)_mc; // HACK
    if (auto object = columnData<Object>(row)) {
=======
    (void)_mc;  // HACK
    if (const auto *object = columnData<Object>(row)) {
>>>>>>> upstream/master
        for (const auto &og : object->_groups) {
            if (og->isContactAuthorized(auth_user)) {
                group_names.push_back(og->name());
            }
        }
    }
#else
<<<<<<< HEAD
    if (auto p = columnData<objectlist *>(row)) {
        for (objectlist *list = *p; list != nullptr; list = list->next) {
            auto hg = static_cast<hostgroup *>(list->object_ptr);
=======
    if (const auto *p = columnData<objectlist *>(row)) {
        for (objectlist *list = *p; list != nullptr; list = list->next) {
            auto *hg = static_cast<hostgroup *>(list->object_ptr);
>>>>>>> upstream/master
            if (is_authorized_for_host_group(_mc, hg, auth_user)) {
                group_names.emplace_back(hg->group_name);
            }
        }
    }
#endif
    return group_names;
}
