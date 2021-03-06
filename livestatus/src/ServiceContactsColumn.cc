// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "ServiceContactsColumn.h"
<<<<<<< HEAD
#include "Row.h"

#ifdef CMC
#include "ContactList.h"
#include "Object.h"
#include "cmc.h"
#else
#include <unordered_set>
#include "nagios.h"
#endif

=======

#include "Row.h"

#ifdef CMC
#include "ContactList.h"
#include "Object.h"
#include "cmc.h"
#else
#include <functional>  // IWYU pragma: keep
#include <unordered_set>

#include "nagios.h"
#endif

>>>>>>> upstream/master
std::vector<std::string> ServiceContactsColumn::getValue(
    Row row, const contact* /*auth_user*/,
    std::chrono::seconds /*timezone_offset*/) const {
#ifdef CMC
<<<<<<< HEAD
    if (auto object = columnData<Object>(row)) {
=======
    if (const auto* object = columnData<Object>(row)) {
>>>>>>> upstream/master
        return object->_contact_list->contactNames();
    }
    return {};
#else
    std::unordered_set<std::string> names;
<<<<<<< HEAD
    if (auto svc = columnData<service>(row)) {
        for (auto cm = svc->contacts; cm != nullptr; cm = cm->next) {
            names.insert(cm->contact_ptr->name);
        }
        for (auto cgm = svc->contact_groups; cgm != nullptr; cgm = cgm->next) {
            for (auto cm = cgm->group_ptr->members; cm != nullptr;
=======
    if (const auto *svc = columnData<service>(row)) {
        for (auto *cm = svc->contacts; cm != nullptr; cm = cm->next) {
            names.insert(cm->contact_ptr->name);
        }
        for (auto *cgm = svc->contact_groups; cgm != nullptr; cgm = cgm->next) {
            for (auto *cm = cgm->group_ptr->members; cm != nullptr;
>>>>>>> upstream/master
                 cm = cm->next) {
                names.insert(cm->contact_ptr->name);
            }
        }
    }
    return std::vector<std::string>(names.begin(), names.end());
#endif
}
