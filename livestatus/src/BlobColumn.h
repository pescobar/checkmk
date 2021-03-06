// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef BlobColumn_h
#define BlobColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <chrono>
#include <memory>
#include <string>
#include <vector>

#include "Column.h"
#include "Filter.h"
#include "contact_fwd.h"
#include "opids.h"
class Aggregator;
class Row;
class RowRenderer;

class BlobColumn : public Column {
public:
<<<<<<< HEAD
    BlobColumn(const std::string &name, const std::string &description,
               int indirect_offset, int extra_offset, int extra_extra_offset,
               int offset)
        : Column(name, description, indirect_offset, extra_offset,
                 extra_extra_offset, offset) {}

    ColumnType type() const override { return ColumnType::blob; }
=======
    using Column::Column;
    [[nodiscard]] ColumnType type() const override { return ColumnType::blob; }
>>>>>>> upstream/master

    void output(Row row, RowRenderer &r, const contact *auth_user,
                std::chrono::seconds timezone_offset) const override;

<<<<<<< HEAD
    std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const override;

    std::unique_ptr<Aggregator> createAggregator(
        AggregationFactory factory) const override;

    virtual std::unique_ptr<std::vector<char>> getValue(Row row) const = 0;
=======
    [[nodiscard]] std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const override;

    [[nodiscard]] std::unique_ptr<Aggregator> createAggregator(
        AggregationFactory factory) const override;

    [[nodiscard]] virtual std::unique_ptr<std::vector<char>> getValue(
        Row row) const = 0;
>>>>>>> upstream/master
};

#endif  // BlobColumn_h
