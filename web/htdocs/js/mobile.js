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

/* Disable data-ajax per default, as it makes problems in most
   of our cases */

<<<<<<< HEAD
require('script-loader!../jquery/jquery-1.6.4.min.js');
require('script-loader!../jquery/jquery.mobile-1.0.min.js');

$(document).ready(function() {
=======
require("script-loader!../jquery/jquery-1.8.3.min.js");
require("script-loader!../jquery/jquery.mobile-1.2.1.min.js");

// Optional import is currently not possible using the ES6 imports
var graphs;
try {
    graphs = require("graphs");
} catch (e) {
    graphs = null;
}

$(document).ready(function () {
>>>>>>> upstream/master
    $("a").attr("data-ajax", "false");
    $("form").attr("data-ajax", "false");
    $("div.error").addClass("ui-shadow");
    $("div.success").addClass("ui-shadow");
    $("div.really").addClass("ui-shadow");
    $("div.warning").addClass("ui-shadow");
});

$(document).bind("mobileinit", function () {
    $.mobile.ajaxEnabled = false;
    $.mobile.hashListeningEnabled = false;
});

export const cmk_export = {
    cmk: {
        graphs: graphs,
    },
};
