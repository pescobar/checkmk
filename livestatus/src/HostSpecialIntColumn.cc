// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "HostSpecialIntColumn.h"
<<<<<<< HEAD
#include "MonitoringCore.h"
#include "Row.h"
#include "mk_inventory.h"

#ifdef CMC
#include "Host.h"
=======

#include <filesystem>

#include "MonitoringCore.h"
#include "Row.h"
#include "mk_inventory.h"

#ifdef CMC
#include "Host.h"
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

int32_t HostSpecialIntColumn::getValue(Row row,
<<<<<<< HEAD
                                       const contact* /* auth_user */) const {
#ifdef CMC
    if (auto object = columnData<Object>(row)) {
=======
                                       const contact * /* auth_user */) const {
#ifdef CMC
    if (const auto *object = columnData<Object>(row)) {
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
            case Type::mk_inventory_last:
                return static_cast<int32_t>(mk_inventory_last(
                    _mc->mkInventoryPath() + "/" + object->host()->name()));
        }
    }
#else
    if (auto hst = columnData<host>(row)) {
=======
                return object->rrdInfo().names.empty() ? 0 : 1;
            case Type::mk_inventory_last:
                return static_cast<int32_t>(mk_inventory_last(
                    _mc->mkInventoryPath() / object->host()->name()));
        }
    }
#else
    if (const auto* hst = columnData<host>(row)) {
>>>>>>> upstream/master
        switch (_type) {
            case Type::real_hard_state:
                if (hst->current_state == HOST_UP) {
                    return 0;
                }
                return hst->state_type == HARD_STATE ? hst->current_state
                                                     : hst->last_hard_state;
            case Type::pnp_graph_present:
                return pnpgraph_present(_mc, hst->name,
                                        dummy_service_description());
            case Type::mk_inventory_last:
<<<<<<< HEAD
                return static_cast<int32_t>(mk_inventory_last(
                    _mc->mkInventoryPath() + "/" + hst->name));
=======
                return static_cast<int32_t>(
                    mk_inventory_last(_mc->mkInventoryPath() / hst->name));
>>>>>>> upstream/master
        }
    }
#endif
    return 0;
}
