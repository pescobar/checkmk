// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TableEventConsole_h
#define TableEventConsole_h

#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <ctime>
=======

#include <cstdint>
>>>>>>> upstream/master
#include <map>
#include <string>
#include <utility>
#include <vector>
<<<<<<< HEAD
#include "Column.h"
#include "DoubleColumn.h"
#include "IntColumn.h"
#include "ListColumn.h"
#include "MonitoringCore.h"
#include "Row.h"
#include "StringColumn.h"
#include "StringUtils.h"
#include "Table.h"
#include "TimeColumn.h"
#include "nagios.h"
=======

#include "DoubleLambdaColumn.h"  // IWYU pragma: keep
#include "IntLambdaColumn.h"     // IWYU pragma: keep
#include "ListLambdaColumn.h"    // IWYU pragma: keep
#include "MonitoringCore.h"
#include "StringLambdaColumn.h"  // IWYU pragma: keep
#include "Table.h"
#include "TimeLambdaColumn.h"  // IWYU pragma: keep
#include "nagios.h"
class ColumnOffsets;
>>>>>>> upstream/master
class Query;
class Row;

<<<<<<< HEAD
class TableEventConsole : public Table {
public:
    explicit TableEventConsole(MonitoringCore *mc);

    void answerQuery(Query *query) override;

    struct ECRow {
        std::map<std::string, std::string> _map;
        MonitoringCore::Host *_host;
    };

protected:
    static std::string getRaw(Row row, const Column &column,
                              const std::string &default_value) {
        if (auto r = column.columnData<ECRow>(row)) {
            auto it = r->_map.find(column.name());
            if (it != r->_map.end()) {
                return it->second;
            }
        }
        return default_value;
    }

    struct StringEventConsoleColumn : public StringColumn {
        StringEventConsoleColumn(const std::string &name,
                                 const std::string &description)
            : StringColumn(name, description, -1, -1, -1, 0) {}

        std::string getValue(Row row) const override {
            return getRaw(row, *this, "");
        }
    };

    struct IntEventConsoleColumn : public IntColumn {
        IntEventConsoleColumn(const std::string &name,
                              const std::string &description)
            : IntColumn(name, description, -1, -1, -1, 0) {}

        int32_t getValue(Row row,
                         const contact * /* auth_user */) const override {
            return static_cast<int32_t>(atol(getRaw(row, *this, "0").c_str()));
        }
    };

    struct DoubleEventConsoleColumn : public DoubleColumn {
        DoubleEventConsoleColumn(const std::string &name,
                                 const std::string &description)
            : DoubleColumn(name, description, -1, -1, -1, 0) {}

        double getValue(Row row) const override {
            return atof(getRaw(row, *this, "0").c_str());
        }
    };

    struct TimeEventConsoleColumn : public TimeColumn {
        TimeEventConsoleColumn(const std::string &name,
                               const std::string &description)
            : TimeColumn(name, description, -1, -1, -1, 0) {}

    private:
        std::chrono::system_clock::time_point getRawValue(
            Row row) const override {
            return std::chrono::system_clock::from_time_t(
                static_cast<std::time_t>(
                    atof(getRaw(row, *this, "0").c_str())));
        }
    };

    struct ListEventConsoleColumn : public ListColumn {
        ListEventConsoleColumn(const std::string &name,
                               const std::string &description)
            : ListColumn(name, description, -1, -1, -1, 0) {}

        std::vector<std::string> getValue(
            Row row, const contact * /*auth_user*/,
            std::chrono::seconds /*timezone_offset*/) const override {
            auto result = getRaw(row, *this, "");
            return result.empty() || result == "\002"
                       ? std::vector<std::string>()
                       : mk::split(result.substr(1), '\001');
        }

        bool isNone(Row row) const { return getRaw(row, *this, "") == "\002"; }
    };

    bool isAuthorizedForEvent(Row row, const contact *ctc) const;

=======
// NOTE: We have a few "keep" pragmas above to avoid the insane handling of
// template foward declarations, when the templates have parameters with
// defaults. Yet another example "simple things gone wrong"... :-/

class ECRow {
public:
    ECRow(MonitoringCore *mc, const std::vector<std::string> &headers,
          const std::vector<std::string> &columns);

    static std::unique_ptr<StringLambdaColumn<ECRow>> makeStringColumn(
        const std::string &name, const std::string &description,
        const ColumnOffsets &offsets);
    static std::unique_ptr<IntLambdaColumn<ECRow>> makeIntColumn(
        const std::string &name, const std::string &description,
        const ColumnOffsets &offsets);
    static std::unique_ptr<DoubleLambdaColumn<ECRow>> makeDoubleColumn(
        const std::string &name, const std::string &description,
        const ColumnOffsets &offsets);
    static std::unique_ptr<TimeLambdaColumn<ECRow>> makeTimeColumn(
        const std::string &name, const std::string &description,
        const ColumnOffsets &offsets);
    static std::unique_ptr<ListLambdaColumn<ECRow>> makeListColumn(
        const std::string &name, const std::string &description,
        const ColumnOffsets &offsets);

    [[nodiscard]] std::string getString(const std::string &column_name) const;
    [[nodiscard]] int32_t getInt(const std::string &column_name) const;
    [[nodiscard]] double getDouble(const std::string &column_name) const;

    [[nodiscard]] const MonitoringCore::Host *host() const;

private:
    std::map<std::string, std::string> map_;
    MonitoringCore::Host *host_;

    [[nodiscard]] std::string get(const std::string &column_name,
                                  const std::string &default_value) const;
};

class TableEventConsole : public Table {
public:
    explicit TableEventConsole(MonitoringCore *mc);

    void answerQuery(Query *query) override;

protected:
    bool isAuthorizedForEvent(Row row, const contact *ctc) const;

>>>>>>> upstream/master
private:
    bool isAuthorizedForEventViaContactGroups(
        const MonitoringCore::Contact *ctc, Row row, bool &result) const;
    bool isAuthorizedForEventViaHost(const MonitoringCore::Contact *ctc,
                                     Row row, bool &result) const;
};

#endif  // TableEventConsole_h
