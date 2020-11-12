// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TableLog_h
#define TableLog_h

#include "config.h"  // IWYU pragma: keep

#include <ctime>
#include <memory>
#include <string>
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Logfile.h"
#include "Table.h"
#include "contact_fwd.h"
class Column;
class LogCache;
class MonitoringCore;
class Query;
class Row;

class TableLog : public Table {
public:
    TableLog(MonitoringCore *mc, LogCache *log_cache);

<<<<<<< HEAD
    std::string name() const override;
    std::string namePrefix() const override;
    void answerQuery(Query *query) override;
    bool isAuthorized(Row row, const contact *ctc) const override;
    std::shared_ptr<Column> column(std::string colname) const override;
=======
    [[nodiscard]] std::string name() const override;
    [[nodiscard]] std::string namePrefix() const override;
    void answerQuery(Query *query) override;
    bool isAuthorized(Row row, const contact *ctc) const override;
    [[nodiscard]] std::shared_ptr<Column> column(
        std::string colname) const override;
>>>>>>> upstream/master

private:
    LogCache *_log_cache;
    bool answerQueryReverse(const logfile_entries_t *entries, Query *query,
                            time_t since, time_t until);
};

#endif  // TableLog_h
