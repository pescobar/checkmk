// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef ServiceSpecialDoubleColumn_h
#define ServiceSpecialDoubleColumn_h

#include "config.h"  // IWYU pragma: keep

#include <string>
<<<<<<< HEAD
#include "DoubleColumn.h"
=======

#include "DoubleColumn.h"
class ColumnOffsets;
>>>>>>> upstream/master
class Row;

class ServiceSpecialDoubleColumn : public DoubleColumn {
public:
    enum class Type { staleness };

    ServiceSpecialDoubleColumn(const std::string& name,
<<<<<<< HEAD
                               const std::string& description, int indirect,
                               int extra_offset, int extra_extra_offset,
                               int offset, Type ssdc_type)
        : DoubleColumn(name, description, indirect, extra_offset,
                       extra_extra_offset, offset)
        , _type(ssdc_type) {}

    double getValue(Row row) const override;
=======
                               const std::string& description,
                               const ColumnOffsets& offsets, Type ssdc_type)
        : DoubleColumn(name, description, offsets), _type(ssdc_type) {}

    [[nodiscard]] double getValue(Row row) const override;
>>>>>>> upstream/master

private:
    const Type _type;
};

#endif  // ServiceSpecialDoubleColumn_h
