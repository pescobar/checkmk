// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef LogwatchListColumn_h
#define LogwatchListColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <chrono>
#include <filesystem>
#include <string>
#include <vector>
<<<<<<< HEAD
#include "ListColumn.h"
#include "contact_fwd.h"
class MonitoringCore;
class Row;

class LogwatchListColumn : public ListColumn {
public:
    LogwatchListColumn(const std::string &name, const std::string &description,
                       int indirect_offset, int extra_offset,
                       int extra_extra_offset, int offset, MonitoringCore *mc)
        : ListColumn(name, description, indirect_offset, extra_offset,
                     extra_extra_offset, offset)
        , _mc(mc) {}
=======

#include "ListColumn.h"
#include "contact_fwd.h"
class ColumnOffsets;
class MonitoringCore;
class Row;

class LogwatchListColumn : public ListColumn {
public:
    LogwatchListColumn(const std::string &name, const std::string &description,
                       const ColumnOffsets &offsets, MonitoringCore *mc)
        : ListColumn(name, description, offsets), _mc(mc) {}
>>>>>>> upstream/master

    std::vector<std::string> getValue(
        Row row, const contact *auth_user,
        std::chrono::seconds timezone_offset) const override;

private:
    MonitoringCore *_mc;

<<<<<<< HEAD
    std::filesystem::path getDirectory(Row row) const;
    std::string getHostName(Row row) const;
=======
    [[nodiscard]] std::filesystem::path getDirectory(Row row) const;
    [[nodiscard]] std::string getHostName(Row row) const;
>>>>>>> upstream/master
};

#endif  // LogwatchListColumn_h
