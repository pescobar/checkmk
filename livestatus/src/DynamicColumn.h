// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef DynamicColumn_h
#define DynamicColumn_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <memory>
#include <string>
class Column;
=======

#include <memory>
#include <string>

#include "Column.h"
>>>>>>> upstream/master

class DynamicColumn {
public:
    DynamicColumn(std::string name, std::string description,
<<<<<<< HEAD
                  int indirect_offset, int extra_offset,
                  int extra_extra_offset);
    virtual ~DynamicColumn();
    std::string name() const;
=======
                  ColumnOffsets offsets);
    virtual ~DynamicColumn();
    [[nodiscard]] std::string name() const;
>>>>>>> upstream/master
    virtual std::unique_ptr<Column> createColumn(
        const std::string &name, const std::string &arguments) = 0;

protected:
    const std::string _name;
    const std::string _description;  // Note: Currently unused!
<<<<<<< HEAD
    const int _indirect_offset;
    const int _extra_offset;
    const int _extra_extra_offset;
=======
    ColumnOffsets _offsets;
>>>>>>> upstream/master
};

#endif  // DynamicColumn_h
