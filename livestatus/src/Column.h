// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef Column_h
#define Column_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <chrono>
#include <cstddef>
#include <functional>
#include <memory>
#include <string>
<<<<<<< HEAD
#include "Filter.h"
=======
#include <vector>

#include "Filter.h"
#include "Logger.h"
>>>>>>> upstream/master
#include "Row.h"
#include "contact_fwd.h"
#include "opids.h"
class Aggregation;
class Aggregator;
<<<<<<< HEAD
class Logger;
=======
>>>>>>> upstream/master
class RowRenderer;

template <typename T>
const T *offset_cast(const void *ptr, size_t offset) {
    // cppcheck is too dumb to see that this is just pointer arithmetic... :-/
    // cppcheck-suppress invalidPointerCast
    return reinterpret_cast<const T *>(reinterpret_cast<const char *>(ptr) +
                                       offset);
}

enum class ColumnType { int_, double_, string, list, time, dict, blob, null };

using AggregationFactory = std::function<std::unique_ptr<Aggregation>()>;

<<<<<<< HEAD
class Column {
public:
    Column(std::string name, std::string description, int indirect_offset,
           int extra_offset, int extra_extra_offset, int offset);
    virtual ~Column() = default;

    std::string name() const { return _name; }
    std::string description() const { return _description; }

    template <typename T>
    const T *columnData(Row row) const {
        return static_cast<const T *>(shiftPointer(row));
    }

    virtual ColumnType type() const = 0;

    virtual void output(Row row, RowRenderer &r, const contact *auth_user,
                        std::chrono::seconds timezone_offset) const = 0;

    virtual std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const = 0;

    virtual std::unique_ptr<Aggregator> createAggregator(
        AggregationFactory factory) const = 0;
=======
class ColumnOffsets {
public:
    using shifter = std::function<const void *(Row)>;
    [[nodiscard]] ColumnOffsets add(const shifter &shifter) const;
    [[nodiscard]] const void *shiftPointer(Row row) const;

private:
    std::vector<shifter> shifters_;
};

class Column {
public:
    Column(std::string name, std::string description, ColumnOffsets offsets);
    virtual ~Column() = default;

    [[nodiscard]] std::string name() const { return _name; }
    [[nodiscard]] std::string description() const { return _description; }

    template <typename T>
    [[nodiscard]] const T *columnData(Row row) const {
        return static_cast<const T *>(shiftPointer(row));
    }
>>>>>>> upstream/master

    [[nodiscard]] virtual ColumnType type() const = 0;

    virtual void output(Row row, RowRenderer &r, const contact *auth_user,
                        std::chrono::seconds timezone_offset) const = 0;

    [[nodiscard]] virtual std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const = 0;

    [[nodiscard]] virtual std::unique_ptr<Aggregator> createAggregator(
        AggregationFactory factory) const = 0;

    [[nodiscard]] Logger *logger() const { return &_logger; }

private:
    mutable ContextLogger _logger;
    std::string _name;
    std::string _description;
<<<<<<< HEAD
    int _indirect_offset;
    int _extra_offset;
    int _extra_extra_offset;
    int _offset;

    const void *shiftPointer(Row row) const;
=======
    ColumnOffsets _offsets;

    [[nodiscard]] const void *shiftPointer(Row row) const;
>>>>>>> upstream/master
};

#endif  // Column_h
