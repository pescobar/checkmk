// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef HostGroupsColumn_h
#define HostGroupsColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <chrono>
#include <string>
#include <vector>
#include "ListColumn.h"
#include "contact_fwd.h"
=======

#include <chrono>
#include <string>
#include <vector>

#include "ListColumn.h"
#include "contact_fwd.h"
class ColumnOffsets;
>>>>>>> upstream/master
class MonitoringCore;
class Row;

class HostGroupsColumn : public ListColumn {
public:
    HostGroupsColumn(const std::string &name, const std::string &description,
<<<<<<< HEAD
                     int indirect_offset, int extra_offset,
                     int extra_extra_offset, int offset, MonitoringCore *mc)
        : ListColumn(name, description, indirect_offset, extra_offset,
                     extra_extra_offset, offset)
        , _mc(mc) {}
=======
                     const ColumnOffsets &offsets, MonitoringCore *mc)
        : ListColumn(name, description, offsets), _mc(mc) {}
>>>>>>> upstream/master

    std::vector<std::string> getValue(
        Row row, const contact *auth_user,
        std::chrono::seconds timezone_offset) const override;

private:
    MonitoringCore *const _mc;
};

#endif  // HostGroupsColumn_h
