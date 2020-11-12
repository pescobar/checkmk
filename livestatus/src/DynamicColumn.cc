// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "DynamicColumn.h"

<<<<<<< HEAD
DynamicColumn::DynamicColumn(std::string name, std::string description,
                             int indirect_offset, int extra_offset,
                             int extra_extra_offset)
    : _name(std::move(name))
    , _description(std::move(description))
    , _indirect_offset(indirect_offset)
    , _extra_offset(extra_offset)
    , _extra_extra_offset(extra_extra_offset) {}
=======
#include <utility>

DynamicColumn::DynamicColumn(std::string name, std::string description,
                             ColumnOffsets offsets)
    : _name(std::move(name))
    , _description(std::move(description))
    , _offsets(std::move(offsets)) {}
>>>>>>> upstream/master

DynamicColumn::~DynamicColumn() = default;

std::string DynamicColumn::name() const { return _name; }
