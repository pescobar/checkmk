// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "CustomVarsValuesColumn.h"
<<<<<<< HEAD
#include <algorithm>
#include <iterator>
#include <unordered_map>
#include "MonitoringCore.h"
#include "Row.h"

#ifndef CMC
// TODO(sp) Why on earth is "contact_fwd.h" not enough???
#include "nagios.h"
#endif

=======

#include <algorithm>
#include <iterator>
#include <unordered_map>

#include "MonitoringCore.h"
#include "Row.h"

#ifndef CMC
// TODO(sp) Why on earth is "contact_fwd.h" not enough???
#include "nagios.h"
#endif

>>>>>>> upstream/master
std::vector<std::string> CustomVarsValuesColumn::getValue(
    Row row, const contact * /*auth_user*/,
    std::chrono::seconds /*timezone_offset*/) const {
    std::vector<std::string> values;
<<<<<<< HEAD
    if (auto p = columnData<void>(row)) {
=======
    if (const auto *const p = columnData<void>(row)) {
>>>>>>> upstream/master
        auto attrs = _mc->customAttributes(p, _kind);
        std::transform(attrs.begin(), attrs.end(), std::back_inserter(values),
                       [](const auto &entry) { return entry.second; });
    }
    return values;
}
