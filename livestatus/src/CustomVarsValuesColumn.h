// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef CustomVarsValuesColumn_h
#define CustomVarsValuesColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <chrono>
#include <string>
#include <vector>
#include "ListColumn.h"
#include "contact_fwd.h"
enum class AttributeKind;
=======

#include <chrono>
#include <string>
#include <vector>

#include "ListColumn.h"
#include "contact_fwd.h"
enum class AttributeKind;
class ColumnOffsets;
>>>>>>> upstream/master
class MonitoringCore;
class Row;

class CustomVarsValuesColumn : public ListColumn {
public:
    CustomVarsValuesColumn(const std::string &name,
<<<<<<< HEAD
                           const std::string &description, int indirect_offset,
                           int extra_offset, int extra_extra_offset, int offset,
                           const MonitoringCore *mc, AttributeKind kind)
        : ListColumn(name, description, indirect_offset, extra_offset,
                     extra_extra_offset, offset)
        , _mc(mc)
        , _kind(kind) {}
=======
                           const std::string &description,
                           const ColumnOffsets &offsets,
                           const MonitoringCore *mc, AttributeKind kind)
        : ListColumn(name, description, offsets), _mc(mc), _kind(kind) {}
>>>>>>> upstream/master

    std::vector<std::string> getValue(
        Row row, const contact *auth_user,
        std::chrono::seconds timezone_offset) const override;

private:
    const MonitoringCore *const _mc;
    const AttributeKind _kind;
};

#endif  // CustomVarsValuesColumn_h
