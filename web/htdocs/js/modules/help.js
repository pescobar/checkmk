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
import * as ajax from "ajax";

//#   .-Help Toggle--------------------------------------------------------.
//#   |          _   _      _         _____                 _              |
//#   |         | | | | ___| |_ __   |_   _|__   __ _  __ _| | ___         |
//#   |         | |_| |/ _ \ | '_ \    | |/ _ \ / _` |/ _` | |/ _ \        |
//#   |         |  _  |  __/ | |_) |   | | (_) | (_| | (_| | |  __/        |
//#   |         |_| |_|\___|_| .__/    |_|\___/ \__, |\__, |_|\___|        |
//#   |                      |_|                |___/ |___/                |
//#   '--------------------------------------------------------------------'

<<<<<<< HEAD
export function enable()
{
    var help = document.getElementById("helpbutton");
    help.style.display = "inline-block";
}

export function toggle()
{
    var help = document.getElementById("helpbutton");
    if (utils.has_class(help, "active")) {
        utils.remove_class(help, "active");
        utils.add_class(help, "passive");
        switch_help(false);
    } else {
        utils.add_class(help, "active");
        utils.remove_class(help, "passive");
=======
function is_help_active() {
    const helpdivs = document.getElementsByClassName("help");
    return helpdivs.length !== 0 && helpdivs[0].style.display === "block";
}

export function toggle() {
    if (is_help_active()) {
        switch_help(false);
    } else {
>>>>>>> upstream/master
        switch_help(true);
    }
}

<<<<<<< HEAD
function switch_help(how)
{
    // recursive scan for all div class=help elements
    var helpdivs = document.getElementsByClassName("help");
    var i;
    for (i=0; i<helpdivs.length; i++) {
=======
function switch_help(how) {
    // recursive scan for all div class=help elements
    var helpdivs = document.getElementsByClassName("help");
    var i;
    for (i = 0; i < helpdivs.length; i++) {
>>>>>>> upstream/master
        helpdivs[i].style.display = how ? "block" : "none";
    }

    // small hack for wato ruleset lists, toggle the "float" and "nofloat"
    // classes on those objects to make the layout possible
    var rulesetdivs = document.getElementsByClassName("ruleset");
    for (i = 0; i < rulesetdivs.length; i++) {
        if (how) {
            if (utils.has_class(rulesetdivs[i], "float")) {
                utils.remove_class(rulesetdivs[i], "float");
                utils.add_class(rulesetdivs[i], "nofloat");
            }
        } else {
            if (utils.has_class(rulesetdivs[i], "nofloat")) {
                utils.remove_class(rulesetdivs[i], "nofloat");
                utils.add_class(rulesetdivs[i], "float");
            }
        }
    }

    ajax.get_url("ajax_switch_help.py?enabled=" + (how ? "yes" : ""));
}
