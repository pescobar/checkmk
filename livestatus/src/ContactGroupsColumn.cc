// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "ContactGroupsColumn.h"
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Row.h"

#ifdef CMC
#include "ContactList.h"
#include "Object.h"
#include "cmc.h"
#else
#include "nagios.h"
#endif

std::vector<std::string> ContactGroupsColumn::getValue(
    Row row, const contact * /*auth_user*/,
    std::chrono::seconds /*timezone_offset*/) const {
    std::vector<std::string> names;
#ifdef CMC
<<<<<<< HEAD
    if (auto object = columnData<Object>(row)) {
=======
    if (const auto *object = columnData<Object>(row)) {
>>>>>>> upstream/master
        for (const auto &name : object->_contact_list->groupNames()) {
            names.push_back(name);
        }
    }
#else
<<<<<<< HEAD
    if (auto p = columnData<contactgroupsmember *>(row)) {
        for (auto cgm = *p; cgm != nullptr; cgm = cgm->next) {
=======
    if (const auto *p = columnData<contactgroupsmember *>(row)) {
        for (auto *cgm = *p; cgm != nullptr; cgm = cgm->next) {
>>>>>>> upstream/master
            names.emplace_back(cgm->group_ptr->group_name);
        }
    }
#endif
    return names;
}
