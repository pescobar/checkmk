// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "ServiceSpecialIntColumn.h"
<<<<<<< HEAD
#include "Row.h"

#ifdef CMC
=======

#include "Row.h"

#ifdef CMC
#include "Metric.h"
>>>>>>> upstream/master
#include "Object.h"
#include "RRDInfo.h"
#include "State.h"
#include "cmc.h"
#else
#include "nagios.h"
#include "pnp4nagios.h"
#endif

int32_t ServiceSpecialIntColumn::getValue(
<<<<<<< HEAD
    Row row, const contact* /* auth_user */) const {
#ifdef CMC
    (void)_mc;
    if (auto object = columnData<Object>(row)) {
=======
    Row row, const contact * /* auth_user */) const {
#ifdef CMC
    (void)_mc;
    if (const auto *const object = columnData<Object>(row)) {
>>>>>>> upstream/master
        switch (_type) {
            case Type::real_hard_state: {
                if (object->isCurrentStateOK()) {
                    return 0;
                }
<<<<<<< HEAD
                auto state = object->state();
=======
                const auto *const state = object->state();
>>>>>>> upstream/master
                return state->_state_type == StateType::hard
                           ? state->_current_state
                           : state->_last_hard_state;
            }
            case Type::pnp_graph_present:
<<<<<<< HEAD
                return object->rrdInfo().names_.empty() ? 0 : 1;
        }
    }
#else
    if (auto svc = columnData<service>(row)) {
=======
                return object->rrdInfo().names.empty() ? 0 : 1;
        }
    }
#else
    if (const auto* const svc = columnData<service>(row)) {
>>>>>>> upstream/master
        switch (_type) {
            case Type::real_hard_state:
                if (svc->current_state == STATE_OK) {
                    return 0;
                }
                return svc->state_type == HARD_STATE ? svc->current_state
                                                     : svc->last_hard_state;
            case Type::pnp_graph_present:
                return pnpgraph_present(_mc, svc->host_ptr->name,
                                        svc->description);
        }
    }
#endif
    return 0;
}
