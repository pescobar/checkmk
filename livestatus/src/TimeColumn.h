<<<<<<< HEAD
// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// tails. You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.
>>>>>>> upstream/master

#ifndef TimeColumn_h
#define TimeColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <chrono>
#include <memory>
#include <string>
=======

#include <chrono>
#include <memory>
#include <string>

>>>>>>> upstream/master
#include "Column.h"
#include "Filter.h"
#include "contact_fwd.h"
#include "opids.h"
class Aggregator;
class Row;
class RowRenderer;

class TimeColumn : public Column {
public:
<<<<<<< HEAD
    TimeColumn(const std::string &name, const std::string &description,
               int indirect_offset, int extra_offset, int extra_extra_offset,
               int offset)
        : Column(name, description, indirect_offset, extra_offset,
                 extra_extra_offset, offset) {}

    ColumnType type() const override { return ColumnType::time; }
=======
    using Column::Column;

    [[nodiscard]] ColumnType type() const override { return ColumnType::time; }
>>>>>>> upstream/master

    void output(Row row, RowRenderer &r, const contact *auth_user,
                std::chrono::seconds timezone_offset) const override;

<<<<<<< HEAD
    std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const override;

    std::unique_ptr<Aggregator> createAggregator(
        AggregationFactory factory) const override;

    std::chrono::system_clock::time_point getValue(
        Row row, std::chrono::seconds timezone_offset) const;

private:
    virtual std::chrono::system_clock::time_point getRawValue(
=======
    [[nodiscard]] std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const override;

    [[nodiscard]] std::unique_ptr<Aggregator> createAggregator(
        AggregationFactory factory) const override;

    [[nodiscard]] std::chrono::system_clock::time_point getValue(
        Row row, std::chrono::seconds timezone_offset) const;

private:
    [[nodiscard]] virtual std::chrono::system_clock::time_point getRawValue(
>>>>>>> upstream/master
        Row row) const = 0;
};

#endif  // TimeColumn_h
