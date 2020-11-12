// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef ServiceContactsColumn_h
#define ServiceContactsColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <chrono>
#include <string>
#include <vector>
=======

#include <chrono>
#include <string>
#include <vector>

>>>>>>> upstream/master
#include "ListColumn.h"
#include "contact_fwd.h"
class Row;

class ServiceContactsColumn : public ListColumn {
public:
<<<<<<< HEAD
    ServiceContactsColumn(const std::string& name,
                          const std::string& description, int indirect_offset,
                          int extra_offset, int extra_extra_offset, int offset)
        : ListColumn(name, description, indirect_offset, extra_offset,
                     extra_extra_offset, offset) {}

=======
    using ListColumn::ListColumn;
>>>>>>> upstream/master
    std::vector<std::string> getValue(
        Row row, const contact* auth_user,
        std::chrono::seconds timezone_offset) const override;
};

#endif  // ServiceContactsColumn_h
