<<<<<<< HEAD
// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// tails.  You should have received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.
>>>>>>> upstream/master

import * as utils from "utils";

// Stores the reload pause timer object once the regular reload has
// been paused e.g. by modifying a graphs timerange or vertical axis.
var g_reload_pause_timer = null;

// Sets the reload timer in pause mode for X seconds. This is shown to
// the user with a pause overlay icon. The icon also shows the time when
// the pause ends. Once the user clicks on the pause icon or the time
// is reached, the whole page is reloaded.
<<<<<<< HEAD
export function pause(seconds)
{
=======
export function pause(seconds) {
>>>>>>> upstream/master
    utils.stop_reload_timer();
    draw_overlay(seconds);
    set_timer(seconds);
}

<<<<<<< HEAD

export function stop()
{
    if (!g_reload_pause_timer)
        return;
=======
export function stop() {
    if (!g_reload_pause_timer) return;
>>>>>>> upstream/master

    clearTimeout(g_reload_pause_timer);
    g_reload_pause_timer = null;

    var counter = document.getElementById("reload_pause_counter");
<<<<<<< HEAD
    if (counter)
        counter.style.display = "none";
}


function set_timer(seconds)
{
    if (g_reload_pause_timer)
        clearTimeout(g_reload_pause_timer);
=======
    if (counter) counter.style.display = "none";
}

function set_timer(seconds) {
    if (g_reload_pause_timer) clearTimeout(g_reload_pause_timer);
>>>>>>> upstream/master

    g_reload_pause_timer = setTimeout(function () {
        update_timer(seconds);
    }, 1000);
}

<<<<<<< HEAD

function update_timer(seconds_left)
{
=======
function update_timer(seconds_left) {
>>>>>>> upstream/master
    seconds_left -= 1;

    if (seconds_left <= 0) {
        window.location.reload(false);
<<<<<<< HEAD
    }
    else {
=======
    } else {
>>>>>>> upstream/master
        // update the pause counter
        var counter = document.getElementById("reload_pause_counter");
        if (counter) {
            counter.innerHTML = seconds_left;
        }

<<<<<<< HEAD
        g_reload_pause_timer = setTimeout(function() {
=======
        g_reload_pause_timer = setTimeout(function () {
>>>>>>> upstream/master
            update_timer(seconds_left);
        }, 1000);
    }
}

<<<<<<< HEAD

function draw_overlay(seconds)
{
=======
function draw_overlay(seconds) {
>>>>>>> upstream/master
    var container = document.getElementById("reload_pause");
    var counter;
    if (container) {
        // only render once. Just update the counter.
        counter = document.getElementById("reload_pause_counter");
        counter.innerHTML = seconds;
        return;
    }

    container = document.createElement("a");
    container.setAttribute("id", "reload_pause");
    container.href = "javascript:window.location.reload(false)";
    // FIXME: Localize
    container.title = "Page update paused. Click for reload.";

    var p1 = document.createElement("div");
    p1.className = "pause_bar p1";
    container.appendChild(p1);

    var p2 = document.createElement("div");
    p2.className = "pause_bar p2";
    container.appendChild(p2);

    container.appendChild(document.createElement("br"));

    counter = document.createElement("a");
    counter.setAttribute("id", "reload_pause_counter");
    // FIXME: Localize
    counter.title = "Click to stop the countdown.";
    counter.href = "javascript:cmk.reload_pause.stop()";
    container.appendChild(counter);

    document.body.appendChild(container);
}
