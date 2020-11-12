<<<<<<< HEAD
// .------------------------------------------------------------------------.
// |                ____ _               _        __  __ _  __              |
// |               / ___| |__   ___  ___| | __   |  \/  | |/ /              |
// |              | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /               |
// |              | |___| | | |  __/ (__|   <    | |  | | . \               |
// |               \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\              |
// |                                        |_____|                         |
// |             _____       _                       _                      |
// |            | ____|_ __ | |_ ___ _ __ _ __  _ __(_)___  ___             |
// |            |  _| | '_ \| __/ _ \ '__| '_ \| '__| / __|/ _ \            |
// |            | |___| | | | ||  __/ |  | |_) | |  | \__ \  __/            |
// |            |_____|_| |_|\__\___|_|  | .__/|_|  |_|___/\___|            |
// |                                     |_|                                |
// |                     _____    _ _ _   _                                 |
// |                    | ____|__| (_) |_(_) ___  _ __                      |
// |                    |  _| / _` | | __| |/ _ \| '_ \                     |
// |                    | |__| (_| | | |_| | (_) | | | |                    |
// |                    |_____\__,_|_|\__|_|\___/|_| |_|                    |
// |                                                                        |
// | mathias-kettner.com                                 mathias-kettner.de |
// '------------------------------------------------------------------------'
//  This file is part of the Check_MK Enterprise Edition (CEE).
//  Copyright by Mathias Kettner and Mathias Kettner GmbH.  All rights reserved.
//
//  Distributed under the Check_MK Enterprise License.
//
//  You should have  received  a copy of the Check_MK Enterprise License
//  along with Check_MK. If not, email to mk@mathias-kettner.de
//  or write to the postal address provided at www.mathias-kettner.de

#include "Average.h"
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "Average.h"

>>>>>>> upstream/master
#include <cmath>

namespace {
constexpr double percentile = 0.50;
constexpr double horizon = 10;  // seconds
<<<<<<< HEAD
}  // namespace

// Please look at check_mk_base.py:get_average for details on the averaging
// algorithm. It's the same as here.
void Average::update(double value) {
    auto now = std::chrono::steady_clock::now();
    if (_last_update == std::chrono::steady_clock::time_point()) {
        _average = value;
    } else {
        double timedif =
            std::chrono::duration<double>(now - _last_update).count();
        if (timedif == 0) {
            // Force at least halve a second. Can happen e.g. for latency
            // updates
            timedif = 0.5;
        }
        double weight_per_second = pow(1.0 - percentile, 1.0 / horizon);
=======
const double weight_per_second = pow(1.0 - percentile, 1.0 / horizon);
}  // namespace

// TODO (sk): unit tests
// Please look at check_mk_base.py:get_average for details on the averaging
// algorithm. It's the same as here.
void Average::update(double value) {
    using std::chrono::duration;
    using std::chrono::steady_clock;

    auto now = steady_clock::now();

    std::scoped_lock l(_lock);
    if (_last_update == steady_clock::time_point()) {
        _average = value;
    } else {
        auto timedif = duration<double>(now - _last_update).count();
        if (timedif == 0) {
            // Force at least half a second. Can happen e.g. for latency
            // updates
            timedif = 0.5;
        }
>>>>>>> upstream/master
        double weight = pow(weight_per_second, timedif);
        _average = _average * weight + value * (1 - weight);
    }
    _last_update = now;
}
