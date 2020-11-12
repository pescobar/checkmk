// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "Column.h"
<<<<<<< HEAD
=======

#include <ostream>
>>>>>>> upstream/master
#include <utility>

<<<<<<< HEAD
Column::Column(std::string name, std::string description, int indirect_offset,
               int extra_offset, int extra_extra_offset, int offset)
    : _logger(Logger::getLogger("cmk.livestatus"))
    , _name(std::move(name))
    , _description(std::move(description))
    , _indirect_offset(indirect_offset)
    , _extra_offset(extra_offset)
    , _extra_extra_offset(extra_extra_offset)
    , _offset(offset) {}

namespace {
const void *add(const void *data, int offset) {
    return (data == nullptr || offset < 0) ? data
                                           : offset_cast<void>(data, offset);
}

const void *shift(const void *data, int offset) {
    return (data == nullptr || offset < 0)
               ? data
               : *offset_cast<const void *>(data, offset);
=======
#include "POSIXUtils.h"

Column::Column(std::string name, std::string description, ColumnOffsets offsets)
    : _logger(Logger::getLogger("cmk.livestatus"),
              [](std::ostream &os) { os << "[" << getThreadName() << "] "; })
    , _name(std::move(name))
    , _description(std::move(description))
    , _offsets(std::move(offsets)) {}

const void *Column::shiftPointer(Row row) const {
    return _offsets.shiftPointer(row);
}

ColumnOffsets ColumnOffsets::add(const shifter &shifter) const {
    ColumnOffsets result{*this};
    result.shifters_.emplace_back(shifter);
    return result;
>>>>>>> upstream/master
}
}  // namespace

<<<<<<< HEAD
const void *Column::shiftPointer(Row row) const {
    return add(shift(shift(shift(row.rawData<const void>(), _indirect_offset),
                           _extra_offset),
                     _extra_extra_offset),
               _offset);
=======
const void *ColumnOffsets::shiftPointer(Row row) const {
    for (const auto &s : shifters_) {
        // TODO(sp) Figure out what is actually going on regarding nullptr...
        if (row.isNull()) {
            break;
        }
        row = Row{s(row)};
    }
    return row.rawData<void>();
>>>>>>> upstream/master
}
