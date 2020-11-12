// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef DoubleColumn_h
#define DoubleColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <chrono>
#include <memory>
#include <string>

#include "Column.h"
#include "Filter.h"
#include "contact_fwd.h"
#include "opids.h"
class Aggregator;
class Row;
class RowRenderer;

class DoubleColumn : public Column {
public:
<<<<<<< HEAD
    DoubleColumn(const std::string &name, const std::string &description,
                 int indirect_offset, int extra_offset, int extra_extra_offset,
                 int offset)
        : Column(name, description, indirect_offset, extra_offset,
                 extra_extra_offset, offset) {}
    virtual double getValue(Row row) const = 0;
    void output(Row row, RowRenderer &r, const contact *auth_user,
                std::chrono::seconds timezone_offset) const override;
    ColumnType type() const override { return ColumnType::double_; }
    std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const override;
    std::unique_ptr<Aggregator> createAggregator(
=======
    using Column::Column;
    [[nodiscard]] virtual double getValue(Row row) const = 0;
    void output(Row row, RowRenderer &r, const contact *auth_user,
                std::chrono::seconds timezone_offset) const override;
    [[nodiscard]] ColumnType type() const override {
        return ColumnType::double_;
    }
    [[nodiscard]] std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const override;
    [[nodiscard]] std::unique_ptr<Aggregator> createAggregator(
>>>>>>> upstream/master
        AggregationFactory factory) const override;
};

#endif  // DoubleColumn_h
