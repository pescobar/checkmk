// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TableContactGroups_h
#define TableContactGroups_h

#include "config.h"  // IWYU pragma: keep

#include <string>
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Row.h"
#include "Table.h"
class MonitoringCore;
class Query;

class TableContactGroups : public Table {
public:
    explicit TableContactGroups(MonitoringCore *mc);

    [[nodiscard]] std::string name() const override;
    [[nodiscard]] std::string namePrefix() const override;
    void answerQuery(Query *query) override;
<<<<<<< HEAD
    Row findObject(const std::string &objectspec) const override;
=======
    [[nodiscard]] Row findObject(const std::string &objectspec) const override;
>>>>>>> upstream/master
};

#endif  // TableContactGroups_h
