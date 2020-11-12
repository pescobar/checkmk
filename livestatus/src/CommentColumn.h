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

#ifndef CommentColumn_h
#define CommentColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <chrono>
#include <string>
#include <vector>
=======

#include <chrono>
#include <string>
#include <utility>
#include <vector>

#include "Column.h"
>>>>>>> upstream/master
#include "ListColumn.h"
#include "contact_fwd.h"
struct CommentData;
class MonitoringCore;
class RowRenderer;
class Row;

class CommentColumn : public ListColumn {
public:
    CommentColumn(const std::string &name, const std::string &description,
<<<<<<< HEAD
                  int indirect_offset, int extra_offset, int extra_extra_offset,
                  int offset, MonitoringCore *mc, bool is_service,
                  bool with_info, bool with_extra_info)
        : ListColumn(name, description, indirect_offset, extra_offset,
                     extra_extra_offset, offset)
=======
                  ColumnOffsets offsets, MonitoringCore *mc, bool is_service,
                  bool with_info, bool with_extra_info)
        : ListColumn(name, description, std::move(offsets))
>>>>>>> upstream/master
        , _mc(mc)
        , _is_service(is_service)
        , _with_info(with_info)
        , _with_extra_info(with_extra_info) {}

    void output(Row row, RowRenderer &r, const contact *auth_user,
                std::chrono::seconds timezone_offset) const override;

    std::vector<std::string> getValue(
        Row row, const contact *auth_user,
        std::chrono::seconds timezone_offset) const override;

private:
    MonitoringCore *_mc;
    bool _is_service;
    bool _with_info;
    bool _with_extra_info;

<<<<<<< HEAD
    std::vector<CommentData> comments_for_row(Row row) const;
=======
    [[nodiscard]] std::vector<CommentData> comments_for_row(Row row) const;
>>>>>>> upstream/master
};

#endif  // CommentColumn_h
