// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef AndingFilter_h
#define AndingFilter_h

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
#include <utility>
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Filter.h"
#include "contact_fwd.h"
class Column;
class Row;

class AndingFilter : public Filter {
    struct Secret {};

public:
    static std::unique_ptr<Filter> make(Kind kind, const Filters &subfilters);
    bool accepts(Row row, const contact *auth_user,
                 std::chrono::seconds timezone_offset) const override;
    std::unique_ptr<Filter> partialFilter(
        std::function<bool(const Column &)> predicate) const override;
<<<<<<< HEAD
    std::optional<std::string> stringValueRestrictionFor(
        const std::string &column_name) const override;
    std::optional<int32_t> greatestLowerBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;
    std::optional<int32_t> leastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;
    std::optional<std::bitset<32>> valueSetLeastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;
    std::unique_ptr<Filter> copy() const override;
    std::unique_ptr<Filter> negate() const override;
    bool is_tautology() const override;
    bool is_contradiction() const override;
    Filters disjuncts() const override;
    Filters conjuncts() const override;
=======
    [[nodiscard]] std::optional<std::string> stringValueRestrictionFor(
        const std::string &column_name) const override;
    [[nodiscard]] std::optional<int32_t> greatestLowerBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;
    [[nodiscard]] std::optional<int32_t> leastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;
    [[nodiscard]] std::optional<std::bitset<32>> valueSetLeastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;
    [[nodiscard]] std::unique_ptr<Filter> copy() const override;
    [[nodiscard]] std::unique_ptr<Filter> negate() const override;
    [[nodiscard]] bool is_tautology() const override;
    [[nodiscard]] bool is_contradiction() const override;
    [[nodiscard]] Filters disjuncts() const override;
    [[nodiscard]] Filters conjuncts() const override;
>>>>>>> upstream/master

    // NOTE: This is effectively private, but it can't be declared like this
    // because of std::make_unique.
    AndingFilter(Kind kind, Filters subfilters, Secret /*unused*/)
        : Filter(kind), _subfilters(std::move(subfilters)) {}

private:
    Filters _subfilters;

    std::ostream &print(std::ostream &os) const override;
};

#endif  // AndingFilter_h
