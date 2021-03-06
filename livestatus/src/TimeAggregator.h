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

#ifndef TimeAggregator_h
#define TimeAggregator_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <chrono>
=======

#include <chrono>

>>>>>>> upstream/master
#include "Aggregator.h"
#include "TimeColumn.h"
#include "contact_fwd.h"
class Row;
class RowRenderer;

class TimeAggregator : public Aggregator {
public:
    TimeAggregator(const AggregationFactory &factory, const TimeColumn *column)
        : _aggregation(factory()), _column(column) {}

    void consume(Row row, const contact * /*auth_user*/,
                 std::chrono::seconds timezone_offset) override {
        _aggregation->update(std::chrono::system_clock::to_time_t(
            _column->getValue(row, timezone_offset)));
    }

    void output(RowRenderer &r) const override {
        r.output(_aggregation->value());
    }

private:
    std::unique_ptr<Aggregation> _aggregation;
    const TimeColumn *const _column;
};

#endif  // TimeAggregator_h
