// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TableHosts_h
#define TableHosts_h

#include "config.h"  // IWYU pragma: keep

#include <string>
<<<<<<< HEAD
#include "Row.h"
#include "Table.h"
#include "contact_fwd.h"
=======

#include "Row.h"
#include "Table.h"
#include "contact_fwd.h"
class ColumnOffsets;
>>>>>>> upstream/master
class MonitoringCore;
class Query;

class TableHosts : public Table {
public:
    explicit TableHosts(MonitoringCore *mc);
    static void addColumns(Table *table, const std::string &prefix,
<<<<<<< HEAD
                           int indirect_offset, int extra_offset);
=======
                           const ColumnOffsets &offsets);
>>>>>>> upstream/master

    [[nodiscard]] std::string name() const override;
    [[nodiscard]] std::string namePrefix() const override;
    void answerQuery(Query *query) override;
    bool isAuthorized(Row row, const contact *ctc) const override;
<<<<<<< HEAD
    Row findObject(const std::string &objectspec) const override;
=======
    [[nodiscard]] Row findObject(const std::string &objectspec) const override;
>>>>>>> upstream/master
};

#endif  // TableHosts_h
