// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef Filter_h
#define Filter_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <bitset>
#include <chrono>
#include <cstdint>
#include <functional>
#include <iosfwd>
#include <memory>
#include <optional>
#include <string>
#include <vector>
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "contact_fwd.h"
class Column;
class Filter;
class Row;

using Filters = std::vector<std::unique_ptr<Filter>>;

/// A propositional formula over column value relations, kept in negation normal
/// form.
class Filter {
public:
    enum Kind { row, stats, wait_condition };

    explicit Filter(Kind kind) : _kind(kind) {}
    virtual ~Filter();
<<<<<<< HEAD
    Kind kind() const { return _kind; }
=======
    [[nodiscard]] Kind kind() const { return _kind; }
>>>>>>> upstream/master
    virtual bool accepts(Row row, const contact *auth_user,
                         std::chrono::seconds timezone_offset) const = 0;
    virtual std::unique_ptr<Filter> partialFilter(
        std::function<bool(const Column &)> predicate) const = 0;

    // TODO(sp) We might be able to unify all the methods below if we make the
    // underlying lattice structure explicit, i.e. provide a set type and
    // corresponding meet/join operations. Perhaps we can even get rid of the
    // std::optional by making the lattice bounded, i.e. by providing bottom/top
    // values.
<<<<<<< HEAD
    virtual std::optional<std::string> stringValueRestrictionFor(
        const std::string &column_name) const;
    virtual std::optional<int32_t> greatestLowerBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const;
    virtual std::optional<int32_t> leastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const;
    virtual std::optional<std::bitset<32>> valueSetLeastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const;

    virtual std::unique_ptr<Filter> copy() const = 0;
    virtual std::unique_ptr<Filter> negate() const = 0;

    /// Checks for a *syntactic* tautology.
    virtual bool is_tautology() const = 0;

    /// Checks for a *syntactic* contradiction.
    virtual bool is_contradiction() const = 0;

    /// Combining the returned filters with *or* yields a filter equivalent to
    /// the current one.
    virtual Filters disjuncts() const = 0;

    /// Combining the returned filters with *and* yields a filter equivalent to
    /// the current one.
    virtual Filters conjuncts() const = 0;
=======
    [[nodiscard]] virtual std::optional<std::string> stringValueRestrictionFor(
        const std::string &column_name) const;
    [[nodiscard]] virtual std::optional<int32_t> greatestLowerBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const;
    [[nodiscard]] virtual std::optional<int32_t> leastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const;
    [[nodiscard]] virtual std::optional<std::bitset<32>>
    valueSetLeastUpperBoundFor(const std::string &column_name,
                               std::chrono::seconds timezone_offset) const;

    [[nodiscard]] virtual std::unique_ptr<Filter> copy() const = 0;
    [[nodiscard]] virtual std::unique_ptr<Filter> negate() const = 0;

    /// Checks for a *syntactic* tautology.
    [[nodiscard]] virtual bool is_tautology() const = 0;

    /// Checks for a *syntactic* contradiction.
    [[nodiscard]] virtual bool is_contradiction() const = 0;

    /// Combining the returned filters with *or* yields a filter equivalent to
    /// the current one.
    [[nodiscard]] virtual Filters disjuncts() const = 0;

    /// Combining the returned filters with *and* yields a filter equivalent to
    /// the current one.
    [[nodiscard]] virtual Filters conjuncts() const = 0;
>>>>>>> upstream/master

    friend std::ostream &operator<<(std::ostream &os, const Filter &filter) {
        return filter.print(os);
    }

private:
    const Kind _kind;
    virtual std::ostream &print(std::ostream &os) const = 0;
};

#endif  // Filter_h
