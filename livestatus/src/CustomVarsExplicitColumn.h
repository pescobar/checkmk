// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef CustomVarsExplicitColumn_h
#define CustomVarsExplicitColumn_h

#include "config.h"  // IWYU pragma: keep

#include <string>

#include "StringColumn.h"
<<<<<<< HEAD
=======
class ColumnOffsets;
>>>>>>> upstream/master
class MonitoringCore;
class Row;

class CustomVarsExplicitColumn : public StringColumn {
public:
    CustomVarsExplicitColumn(const std::string &name,
                             const std::string &description,
<<<<<<< HEAD
                             int indirect_offset, int extra_offset,
                             int extra_extra_offset, int offset,
                             const MonitoringCore *mc, const char *varname)
        : StringColumn(name, description, indirect_offset, extra_offset,
                       extra_extra_offset, offset)
        , _mc(mc)
        , _varname(varname) {}
    std::string getValue(Row row) const override;
=======
                             const ColumnOffsets &offsets,
                             const MonitoringCore *mc, const char *varname)
        : StringColumn(name, description, offsets)
        , _mc(mc)
        , _varname(varname) {}
    [[nodiscard]] std::string getValue(Row row) const override;
>>>>>>> upstream/master

private:
    const MonitoringCore *const _mc;
    std::string _varname;
};

#endif  // CustomVarsExplicitColumn_h
