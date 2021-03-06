// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef HostSpecialDoubleColumn_h
#define HostSpecialDoubleColumn_h

#include "config.h"  // IWYU pragma: keep

#include <string>

#include "DoubleColumn.h"
<<<<<<< HEAD
=======
class ColumnOffsets;
>>>>>>> upstream/master
class Row;

#ifdef CMC
class Object;
#endif

class HostSpecialDoubleColumn : public DoubleColumn {
public:
    enum class Type { staleness };

    HostSpecialDoubleColumn(const std::string& name,
<<<<<<< HEAD
                            const std::string& description, int indirect,
                            int extra_offset, int extra_extra_offset,
                            int offset, Type hsdc_type)
        : DoubleColumn(name, description, indirect, extra_offset,
                       extra_extra_offset, offset)
        , _type(hsdc_type) {}

    double getValue(Row row) const override;
=======
                            const std::string& description,
                            const ColumnOffsets& offsets, Type hsdc_type)
        : DoubleColumn(name, description, offsets), _type(hsdc_type) {}

    [[nodiscard]] double getValue(Row row) const override;
>>>>>>> upstream/master

#ifdef CMC
    static double staleness(const Object* object);
#endif

private:
    const Type _type;
};

#endif  // HostSpecialDoubleColumn_h
