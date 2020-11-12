// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef Query_h
#define Query_h

// NOTE: We need the 2nd "keep" pragma for deleting Query. Is this
// an IWYU bug?
#include "config.h"  // IWYU pragma: keep
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include <bitset>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <functional>
#include <list>
#include <map>
#include <memory>
#include <optional>
#include <string>
#include <unordered_set>
#include <vector>
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Aggregator.h"  // IWYU pragma: keep
#include "Filter.h"
#include "Renderer.h"
#include "RendererBrokenCSV.h"
#include "Row.h"
#include "StatsColumn.h"
#include "Triggers.h"
#include "contact_fwd.h"
#include "data_encoding.h"
class Column;
class Logger;
class OutputBuffer;
class Table;

class Query {
public:
    Query(const std::list<std::string> &lines, Table &table,
          Encoding data_encoding, size_t max_response_size,
          OutputBuffer &output, Logger *logger);

    bool process();

    // NOTE: We cannot make this 'const' right now, it increments _current_line
    // and calls the non-const getAggregatorsFor() member function.
    bool processDataset(Row row);

    bool timelimitReached() const;
    void invalidRequest(const std::string &message) const;

    const contact *authUser() const { return _auth_user; }
    std::chrono::seconds timezoneOffset() const { return _timezone_offset; }

    std::unique_ptr<Filter> partialFilter(
        const std::string &message,
        std::function<bool(const Column &)> predicate) const;
    std::optional<std::string> stringValueRestrictionFor(
        const std::string &column_name) const;
    std::optional<int32_t> greatestLowerBoundFor(
        const std::string &column_name) const;
    std::optional<int32_t> leastUpperBoundFor(
        const std::string &column_name) const;
    std::optional<std::bitset<32>> valueSetLeastUpperBoundFor(
        const std::string &column_name) const;

    const std::unordered_set<std::shared_ptr<Column>> &allColumns() const {
        return _all_columns;
    }

private:
    using LogicalConnective =
        std::function<std::unique_ptr<Filter>(Filter::Kind, const Filters &)>;

    const Encoding _data_encoding;
    const size_t _max_response_size;
    OutputBuffer &_output;
    QueryRenderer *_renderer_query;
    Table &_table;
    bool _keepalive;
    using FilterStack = Filters;
    std::unique_ptr<Filter> _filter;
    const contact *_auth_user;
    std::unique_ptr<Filter> _wait_condition;
    std::chrono::milliseconds _wait_timeout;
    Triggers::Kind _wait_trigger;
    Row _wait_object;
    CSVSeparators _separators;
    bool _show_column_headers;
    OutputFormat _output_format;
    int _limit;
    int _time_limit;
    time_t _time_limit_timeout;
    unsigned _current_line;
    std::chrono::seconds _timezone_offset;
    Logger *const _logger;
    std::vector<std::shared_ptr<Column>> _columns;
    std::vector<std::unique_ptr<StatsColumn>> _stats_columns;
    std::map<RowFragment, std::vector<std::unique_ptr<Aggregator>>>
        _stats_groups;
    std::unordered_set<std::shared_ptr<Column>> _all_columns;

    bool doStats() const;
    void doWait();
    void parseFilterLine(char *line, FilterStack &filters);
    void parseStatsLine(char *line);
    void parseStatsGroupLine(char *line);
    void parseAndOrLine(char *line, Filter::Kind kind,
                        const LogicalConnective &connective,
                        FilterStack &filters);
    void parseNegateLine(char *line, FilterStack &filters);
    void parseStatsAndOrLine(char *line, const LogicalConnective &connective);
    void parseStatsNegateLine(char *line);
    void parseColumnsLine(char *line);
    void parseColumnHeadersLine(char *line);
    void parseLimitLine(char *line);
    void parseTimelimitLine(char *line);
    void parseSeparatorsLine(char *line);
    void parseOutputFormatLine(char *line);
    void parseKeepAliveLine(char *line);
    void parseResponseHeaderLine(char *line);
    void parseAuthUserHeader(char *line);
    void parseWaitTimeoutLine(char *line);
    void parseWaitTriggerLine(char *line);
    void parseWaitObjectLine(char *line);
    void parseLocaltimeLine(char *line);
    void start(QueryRenderer &q);
    void finish(QueryRenderer &q);

    // NOTE: We cannot make this 'const' right now, it adds entries into
    // _stats_groups.
    const std::vector<std::unique_ptr<Aggregator>> &getAggregatorsFor(
        const RowFragment &groupspec);
};

#endif  // Query_h
