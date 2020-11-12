// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "ServiceListStateColumn.h"
<<<<<<< HEAD
#include "LogEntry.h"
=======

>>>>>>> upstream/master
#include "Row.h"

#ifdef CMC
#include <memory>
<<<<<<< HEAD
=======

>>>>>>> upstream/master
#include "Service.h"
#include "State.h"
#else
#include "auth.h"
#endif

int32_t ServiceListStateColumn::getValue(Row row,
                                         const contact *auth_user) const {
#ifdef CMC
<<<<<<< HEAD
    if (auto p = columnData<Host::services_t>(row)) {
=======
    if (const auto *p = columnData<Host::services_t>(row)) {
>>>>>>> upstream/master
        return getValueFromServices(_mc, _logictype, p, auth_user);
    }
    return 0;
#else
    servicesmember *mem = nullptr;
<<<<<<< HEAD
    if (auto p = columnData<servicesmember *>(row)) {
=======
    if (const auto *p = columnData<servicesmember *>(row)) {
>>>>>>> upstream/master
        mem = *p;
    }
    return getValueFromServices(_mc, _logictype, mem, auth_user);
#endif
}

// static
int32_t ServiceListStateColumn::getValueFromServices(MonitoringCore *mc,
                                                     Type logictype,
                                                     service_list mem,
                                                     const contact *auth_user) {
    int32_t result = 0;
#ifdef CMC
    (void)mc;
    if (mem != nullptr) {
        for (const auto &svc : *mem) {
            if (auth_user == nullptr || svc->hasContact(auth_user)) {
<<<<<<< HEAD
                update(logictype, svc.get(), result);
=======
                const auto *state = svc->state();
                update(logictype,
                       static_cast<ServiceState>(state->_current_state),
                       static_cast<ServiceState>(state->_last_hard_state),
                       state->_has_been_checked,
                       state->_acknowledged ||
                           state->_scheduled_downtime_depth > 0,
                       result);
>>>>>>> upstream/master
            }
        }
    }
#else
    for (; mem != nullptr; mem = mem->next) {
        service *svc = mem->service_ptr;
        if (auth_user == nullptr ||
            is_authorized_for(mc, auth_user, svc->host_ptr, svc)) {
<<<<<<< HEAD
            update(logictype, svc, result);
=======
            update(logictype, static_cast<ServiceState>(svc->current_state),
                   static_cast<ServiceState>(svc->last_hard_state),
                   svc->has_been_checked != 0,
                   svc->problem_has_been_acknowledged != 0 ||
                       svc->scheduled_downtime_depth > 0,
                   result);
>>>>>>> upstream/master
        }
    }
#endif
    return result;
}

// static
<<<<<<< HEAD
void ServiceListStateColumn::update(Type logictype, service *svc,
                                    int32_t &result) {
#ifdef CMC
    uint32_t last_hard_state = svc->state()->_last_hard_state;
    uint32_t current_state = svc->state()->_current_state;
    bool has_been_checked = svc->state()->_has_been_checked;
#else
    int last_hard_state = svc->last_hard_state;
    int current_state = svc->current_state;
    bool has_been_checked = svc->has_been_checked != 0;
#endif
    int service_state;
    Type lt;
    if (static_cast<int>(logictype) >= 60) {
        service_state = last_hard_state;
        lt = static_cast<Type>(static_cast<int>(logictype) - 64);
    } else {
        service_state = current_state;
        lt = logictype;
    }
    switch (lt) {
        case Type::worst_state:
            if (worse(static_cast<ServiceState>(service_state),
                      static_cast<ServiceState>(result))) {
                result = service_state;
            }
            break;
=======
void ServiceListStateColumn::update(Type logictype, ServiceState current_state,
                                    ServiceState last_hard_state,
                                    bool has_been_checked, bool handled,
                                    int32_t &result) {
    switch (logictype) {
>>>>>>> upstream/master
        case Type::num:
            result++;
            break;
        case Type::num_pending:
            if (!has_been_checked) {
                result++;
            }
            break;
<<<<<<< HEAD
        default:
            if (has_been_checked && service_state == static_cast<int>(lt)) {
                result++;
            }
            break;
=======
        case Type::num_handled_problems:
            if (has_been_checked && current_state != ServiceState::ok &&
                handled) {
                result++;
            }
            break;
        case Type::num_unhandled_problems:
            if (has_been_checked && current_state != ServiceState::ok &&
                !handled) {
                result++;
            }
            break;
        case Type::num_ok:
            if (has_been_checked && current_state == ServiceState::ok) {
                result++;
            }
            break;
        case Type::num_warn:
            if (has_been_checked && current_state == ServiceState::warning) {
                result++;
            }
            break;
        case Type::num_crit:
            if (has_been_checked && current_state == ServiceState::critical) {
                result++;
            }
            break;
        case Type::num_unknown:
            if (has_been_checked && current_state == ServiceState::unknown) {
                result++;
            }
            break;
        case Type::worst_state:
            if (worse(current_state, static_cast<ServiceState>(result))) {
                result = static_cast<int32_t>(current_state);
            }
            break;
        case Type::num_hard_ok:
            if (has_been_checked && last_hard_state == ServiceState::ok) {
                result++;
            }
            break;
        case Type::num_hard_warn:
            if (has_been_checked && last_hard_state == ServiceState::warning) {
                result++;
            }
            break;
        case Type::num_hard_crit:
            if (has_been_checked && last_hard_state == ServiceState::critical) {
                result++;
            }
            break;
        case Type::num_hard_unknown:
            if (has_been_checked && last_hard_state == ServiceState::unknown) {
                result++;
            }
            break;
        case Type::worst_hard_state:
            if (worse(last_hard_state, static_cast<ServiceState>(result))) {
                result = static_cast<int32_t>(last_hard_state);
            }
            break;
>>>>>>> upstream/master
    }
}
