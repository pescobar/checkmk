// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "TableTimeperiods.h"
<<<<<<< HEAD
#include <memory>
#include "Column.h"
#include "OffsetStringColumn.h"
#include "Query.h"
#include "Row.h"
#include "TimeperiodColumn.h"
#include "nagios.h"

extern timeperiod *timeperiod_list;

TableTimeperiods::TableTimeperiods(MonitoringCore *mc) : Table(mc) {
    addColumn(std::make_unique<OffsetStringColumn>(
        "name", "The name of the timeperiod", -1, -1, -1,
        DANGEROUS_OFFSETOF(timeperiod, name)));
    addColumn(std::make_unique<OffsetStringColumn>(
        "alias", "The alias of the timeperiod", -1, -1, -1,
        DANGEROUS_OFFSETOF(timeperiod, alias)));
    addColumn(std::make_unique<TimeperiodColumn>(
        "in", "Wether we are currently in this period (0/1)", -1, -1, -1, 0));
=======

#include <cstdint>
#include <memory>

#include "BoolLambdaColumn.h"
#include "Column.h"
#include "Query.h"
#include "Row.h"
#include "StringLambdaColumn.h"
#include "TimeperiodsCache.h"
#include "nagios.h"

TableTimeperiods::TableTimeperiods(MonitoringCore* mc) : Table(mc) {
    ColumnOffsets offsets{};
    addColumn(std::make_unique<StringLambdaColumn<timeperiod>>(
        "name", "The name of the timeperiod", offsets,
        [](const timeperiod& tp) { return tp.name; }));
    addColumn(std::make_unique<StringLambdaColumn<timeperiod>>(
        "alias", "The alias of the timeperiod", offsets,
        [](const timeperiod& tp) { return tp.alias; }));
    // unknown timeperiod is assumed to be 24X7
    addColumn(std::make_unique<BoolLambdaColumn<timeperiod, true>>(
        "in", "Wether we are currently in this period (0/1)", offsets,
        [](const timeperiod& tp) {
            extern TimeperiodsCache* g_timeperiods_cache;
            return g_timeperiods_cache->inTimeperiod(&tp);
        }));
>>>>>>> upstream/master
    // TODO(mk): add days and exceptions
}

std::string TableTimeperiods::name() const { return "timeperiods"; }

std::string TableTimeperiods::namePrefix() const { return "timeperiod_"; }

<<<<<<< HEAD
void TableTimeperiods::answerQuery(Query *query) {
    for (timeperiod *tp = timeperiod_list; tp != nullptr; tp = tp->next) {
        if (!query->processDataset(Row(tp))) {
=======
void TableTimeperiods::answerQuery(Query* query) {
    extern timeperiod* timeperiod_list;
    for (const timeperiod* tp = timeperiod_list; tp != nullptr; tp = tp->next) {
        if (!query->processDataset(Row{tp})) {
>>>>>>> upstream/master
            break;
        }
    }
}
