// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TableEventConsoleReplication_h
#define TableEventConsoleReplication_h

#include "config.h"  // IWYU pragma: keep

#include <string>

#include "Table.h"
class MonitoringCore;
class Query;

class TableEventConsoleReplication : public Table {
public:
    explicit TableEventConsoleReplication(MonitoringCore *mc);
<<<<<<< HEAD
    std::string name() const override;
    std::string namePrefix() const override;
=======
    [[nodiscard]] std::string name() const override;
    [[nodiscard]] std::string namePrefix() const override;
>>>>>>> upstream/master
    void answerQuery(Query *query) override;
};

#endif  // TableEventConsoleReplication_h
