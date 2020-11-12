// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef HostListStateColumn_h
#define HostListStateColumn_h

#include "config.h"  // IWYU pragma: keep

#include <cstdint>
#include <string>
#include <utility>

#include "Column.h"
#include "IntColumn.h"
#include "LogEntry.h"
#include "ServiceListStateColumn.h"
class MonitoringCore;
class Row;

#ifdef CMC
#include "cmc.h"
#else
#include "nagios.h"
#endif

class HostListStateColumn : public IntColumn {
public:
<<<<<<< HEAD
    // TODO(sp) Remove the magic arithmetic
    enum class Type {
        num_svc = static_cast<int>(ServiceListStateColumn::Type::num),
        num_svc_pending =
            static_cast<int>(ServiceListStateColumn::Type::num_pending),
        num_svc_ok = static_cast<int>(ServiceListStateColumn::Type::num_ok),
        num_svc_warn = static_cast<int>(ServiceListStateColumn::Type::num_warn),
        num_svc_crit = static_cast<int>(ServiceListStateColumn::Type::num_crit),
        num_svc_unknown =
            static_cast<int>(ServiceListStateColumn::Type::num_unknown),
        worst_svc_state =
            static_cast<int>(ServiceListStateColumn::Type::worst_state),
        num_svc_hard_ok =
            static_cast<int>(ServiceListStateColumn::Type::num_hard_ok),
        num_svc_hard_warn =
            static_cast<int>(ServiceListStateColumn::Type::num_hard_warn),
        num_svc_hard_crit =
            static_cast<int>(ServiceListStateColumn::Type::num_hard_crit),
        num_svc_hard_unknown =
            static_cast<int>(ServiceListStateColumn::Type::num_hard_unknown),
        worst_svc_hard_state =
            static_cast<int>(ServiceListStateColumn::Type::worst_hard_state),
        num_hst_up = 10,
        num_hst_down = 11,
        num_hst_unreach = 12,
        num_hst_pending = 13,
        num_hst = -11,
        worst_hst_state = -12,
    };

    HostListStateColumn(const std::string &name, const std::string &description,
                        int indirect_offset, int extra_offset,
                        int extra_extra_offset, int offset, MonitoringCore *mc,
                        Type logictype)
        : IntColumn(name, description, indirect_offset, extra_offset,
                    extra_extra_offset, offset)
=======
    enum class Type {
        num_hst,
        num_hst_pending,
        num_hst_handled_problems,
        num_hst_unhandled_problems,
        //
        num_hst_up,
        num_hst_down,
        num_hst_unreach,
        worst_hst_state,
        //
        num_svc,
        num_svc_pending,
        num_svc_handled_problems,
        num_svc_unhandled_problems,
        //
        num_svc_ok,
        num_svc_warn,
        num_svc_crit,
        num_svc_unknown,
        worst_svc_state,
        //
        num_svc_hard_ok,
        num_svc_hard_warn,
        num_svc_hard_crit,
        num_svc_hard_unknown,
        worst_svc_hard_state,
    };

    HostListStateColumn(const std::string &name, const std::string &description,
                        ColumnOffsets offsets, MonitoringCore *mc,
                        Type logictype)
        : IntColumn(name, description, std::move(offsets))
>>>>>>> upstream/master
        , _mc(mc)
        , _logictype(logictype) {}

    int32_t getValue(Row row, const contact *auth_user) const override;

private:
    MonitoringCore *_mc;
    const Type _logictype;

<<<<<<< HEAD
    void update(host *hst, const contact *auth_user, int32_t &result) const;
=======
    void update(const contact *auth_user, HostState current_state,
                bool has_been_checked,
                ServiceListStateColumn::service_list services, bool handled,
                int32_t &result) const;
>>>>>>> upstream/master
};

#endif  // HostListStateColumn_h
