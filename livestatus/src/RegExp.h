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

#ifndef RegExp_h
#define RegExp_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <memory>
#include <string>

class RegExp {
public:
    enum class Case { ignore, respect };
    enum class Syntax { pattern, literal };

    // Standard pimpl boileplate code, see Scott Meyer's "Effective Modern C++",
    // item 22: "When using the Pimpl Idiom, define special member functions in
    // the implementation file."
    RegExp(const std::string &str, Case c, Syntax s);
    ~RegExp();
    RegExp(const RegExp &rhs) = delete;
    RegExp &operator=(const RegExp &rhs) = delete;
    RegExp(RegExp &&rhs) noexcept;
    RegExp &operator=(RegExp &&rhs) noexcept;

<<<<<<< HEAD
    std::string replace(const std::string &str,
                        const std::string &replacement) const;
    bool match(const std::string &str) const;
    bool search(const std::string &str) const;
=======
    [[nodiscard]] std::string replace(const std::string &str,
                                      const std::string &replacement) const;
    [[nodiscard]] bool match(const std::string &str) const;
    [[nodiscard]] bool search(const std::string &str) const;
>>>>>>> upstream/master

    static std::string engine();

private:
    class Impl;
    std::unique_ptr<Impl> _impl;
};

#endif  // RegExp_h
