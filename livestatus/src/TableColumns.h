// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TableColumns_h
#define TableColumns_h

#include "config.h"  // IWYU pragma: keep

#include <string>
#include <vector>
<<<<<<< HEAD
#include "ColumnsColumn.h"
=======

>>>>>>> upstream/master
#include "Table.h"
class Column;
class MonitoringCore;
class Query;

class TableColumns : public Table {
public:
<<<<<<< HEAD
    explicit TableColumns(MonitoringCore *mc);
=======
    enum class Type { table, name, description, type };
>>>>>>> upstream/master

    explicit TableColumns(MonitoringCore *mc);

    [[nodiscard]] std::string name() const override;
    [[nodiscard]] std::string namePrefix() const override;
    void answerQuery(Query *query) override;

    void addTable(const Table &table);
<<<<<<< HEAD
    std::string getValue(const Column *column,
                         ColumnsColumn::Type colcol) const;
    std::string tableNameOf(const Column *column) const;
=======
    std::string getValue(const Column &column, Type colcol) const;
    std::string tableNameOf(const Column &column) const;
>>>>>>> upstream/master

private:
    std::vector<const Table *> _tables;
};

#endif  // TableColumns_h
