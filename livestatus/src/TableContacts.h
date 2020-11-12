// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TableContacts_h
#define TableContacts_h

#include "config.h"  // IWYU pragma: keep

#include <string>
<<<<<<< HEAD
#include "Row.h"
#include "Table.h"
=======

#include "Row.h"
#include "Table.h"
class ColumnOffsets;
>>>>>>> upstream/master
class MonitoringCore;
class Query;

class TableContacts : public Table {
public:
    explicit TableContacts(MonitoringCore *mc);

    [[nodiscard]] std::string name() const override;
    [[nodiscard]] std::string namePrefix() const override;
    void answerQuery(Query *query) override;
<<<<<<< HEAD
    Row findObject(const std::string &objectspec) const override;

    static void addColumns(Table *table, const std::string &prefix,
                           int indirect_offset);
=======
    [[nodiscard]] Row findObject(const std::string &objectspec) const override;

    static void addColumns(Table *table, const std::string &prefix,
                           const ColumnOffsets &offsets);
>>>>>>> upstream/master
};

#endif  // TableContacts_h
