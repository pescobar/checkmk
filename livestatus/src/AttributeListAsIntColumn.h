// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef AttributeListAsIntColumn_h
#define AttributeListAsIntColumn_h

#include "config.h"  // IWYU pragma: keep

#include <cstdint>
#include <memory>
#include <string>
#include <vector>
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Filter.h"
#include "IntColumn.h"
#include "contact_fwd.h"
#include "opids.h"
class Row;

class AttributeListAsIntColumn : public IntColumn {
public:
<<<<<<< HEAD
    AttributeListAsIntColumn(const std::string &name,
                             const std::string &description,
                             int indirect_offset, int extra_offset,
                             int extra_extra_offset, int offset)
        : IntColumn(name, description, indirect_offset, extra_offset,
                    extra_extra_offset, offset) {}

    std::unique_ptr<Filter> createFilter(
=======
    using IntColumn::IntColumn;

    [[nodiscard]] std::unique_ptr<Filter> createFilter(
>>>>>>> upstream/master
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const override;

    int32_t getValue(Row row, const contact *auth_user) const override;

<<<<<<< HEAD
    std::vector<std::string> getAttributes(Row row) const;
=======
    [[nodiscard]] std::vector<std::string> getAttributes(Row row) const;

    static std::vector<std::string> decode(unsigned long mask);
>>>>>>> upstream/master
};

#endif  // AttributeListAsIntColumn_h
