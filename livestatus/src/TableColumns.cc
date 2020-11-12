// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "TableColumns.h"
<<<<<<< HEAD
#include <map>
#include <memory>
=======

#include <map>
#include <memory>

>>>>>>> upstream/master
#include "Column.h"
#include "Query.h"
#include "Row.h"
<<<<<<< HEAD

TableColumns::TableColumns(MonitoringCore *mc) : Table(mc) {
    addColumn(std::make_unique<ColumnsColumn>(
        "table", "The name of the table", -1, -1, -1, 0,
        ColumnsColumn::Type::table, *this));
    addColumn(std::make_unique<ColumnsColumn>(
        "name", "The name of the column within the table", -1, -1, -1, 0,
        ColumnsColumn::Type::name, *this));
    addColumn(std::make_unique<ColumnsColumn>(
        "description", "A description of the column", -1, -1, -1, 0,
        ColumnsColumn::Type::description, *this));
    addColumn(std::make_unique<ColumnsColumn>(
        "type", "The data type of the column (int, float, string, list)", -1,
        -1, -1, 0, ColumnsColumn::Type::type, *this));
=======
#include "StringLambdaColumn.h"

TableColumns::TableColumns(MonitoringCore *mc) : Table(mc) {
    ColumnOffsets offsets{};
    addColumn(std::make_unique<StringLambdaColumn<Column>>(
        "table", "The name of the table", offsets, [this](const Column &col) {
            return this->getValue(col, Type::table);
        }));
    addColumn(std::make_unique<StringLambdaColumn<Column>>(
        "name", "The name of the column within the table", offsets,
        [this](const Column &col) { return this->getValue(col, Type::name); }));
    addColumn(std::make_unique<StringLambdaColumn<Column>>(
        "description", "A description of the column", offsets,
        [this](const Column &col) {
            return this->getValue(col, Type::description);
        }));
    addColumn(std::make_unique<StringLambdaColumn<Column>>(
        "type", "The data type of the column (int, float, string, list)",
        offsets,
        [this](const Column &col) { return this->getValue(col, Type::type); }));
>>>>>>> upstream/master
}

std::string TableColumns::name() const { return "columns"; }

std::string TableColumns::namePrefix() const { return "column_"; }

void TableColumns::addTable(const Table &table) { _tables.push_back(&table); }

void TableColumns::answerQuery(Query *query) {
<<<<<<< HEAD
    for (auto table : _tables) {
=======
    for (const auto *const table : _tables) {
>>>>>>> upstream/master
        table->any_column([&](const auto &c) {
            return !query->processDataset(Row(c.get()));
        });
    }
}

<<<<<<< HEAD
std::string TableColumns::getValue(const Column *column,
                                   ColumnsColumn::Type colcol) const {
=======
std::string TableColumns::getValue(const Column &column, Type colcol) const {
>>>>>>> upstream/master
    static const char *typenames[8] = {"int",  "float", "string", "list",
                                       "time", "dict",  "blob",   "null"};

    switch (colcol) {
<<<<<<< HEAD
        case ColumnsColumn::Type::table:
            return tableNameOf(column);
        case ColumnsColumn::Type::name:
            return column->name();
        case ColumnsColumn::Type::description:
            return column->description();
        case ColumnsColumn::Type::type:
            return typenames[static_cast<int>(column->type())];
=======
        case Type::table:
            return tableNameOf(column);
        case Type::name:
            return column.name();
        case Type::description:
            return column.description();
        case Type::type:
            return typenames[static_cast<int>(column.type())];
>>>>>>> upstream/master
    }
    return "";
}

<<<<<<< HEAD
std::string TableColumns::tableNameOf(const Column *column) const {
    for (auto table : _tables) {
        if (table->any_column(
                [&](const auto &c) { return c.get() == column; })) {
=======
std::string TableColumns::tableNameOf(const Column &column) const {
    for (const auto *const table : _tables) {
        if (table->any_column(
                [&](const auto &c) { return c.get() == &column; })) {
>>>>>>> upstream/master
            return table->name();
        }
    }
    return "";  // never reached if no bug
}
