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

// fetch_url: dynamically load content of opened element.
export function toggle(treename, id, fetch_url) {
    var img = document.getElementById("treeimg." + treename + "." + id);
    var box = document.getElementById("tree." + treename + "." + id);

    toggle_tree_state(treename, id, box, fetch_url);
<<<<<<< HEAD
    if (img)
        utils.toggle_folding(img, !utils.has_class(box, "closed"));
}

function toggle_tree_state(tree, name, oContainer, fetch_url) {
    var state;
    if (utils.has_class(oContainer, "closed")) {
        utils.change_class(oContainer, "closed", "open");

        if (fetch_url && !oContainer.innerHTML) {
            ajax.call_ajax(fetch_url, {
                method           : "GET",
                response_handler : function(handler_data, response_body) {
                    handler_data.container.innerHTML = response_body;
                },
                handler_data     : {
                    container: oContainer
                }
=======
    if (img) utils.toggle_folding(img, !utils.has_class(box, "closed"));
}

function toggle_tree_state(tree, name, oContainer, fetch_url) {
    var outer_container = oContainer.parentNode;
    var state;

    if (utils.has_class(oContainer, "closed")) {
        utils.change_class(oContainer, "closed", "open");
        utils.change_class(outer_container, "closed", "open");

        if (fetch_url && !oContainer.innerHTML) {
            ajax.call_ajax(fetch_url, {
                method: "GET",
                response_handler: function (handler_data, response_body) {
                    handler_data.container.innerHTML = response_body;
                },
                handler_data: {
                    container: oContainer,
                },
>>>>>>> upstream/master
            });
        }

        state = "on";
<<<<<<< HEAD
    }
    else {
        utils.change_class(oContainer, "open", "closed");
=======
    } else {
        utils.change_class(oContainer, "open", "closed");
        utils.change_class(outer_container, "open", "closed");
>>>>>>> upstream/master
        state = "off";
    }

    persist_tree_state(tree, name, state);
}

<<<<<<< HEAD
export function persist_tree_state(tree, name, state)
{
    ajax.get_url("tree_openclose.py?tree=" + encodeURIComponent(tree)
            + "&name=" + encodeURIComponent(name) + "&state=" + state);
=======
export function persist_tree_state(tree, name, state) {
    ajax.get_url(
        "tree_openclose.py?tree=" +
            encodeURIComponent(tree) +
            "&name=" +
            encodeURIComponent(name) +
            "&state=" +
            state
    );
>>>>>>> upstream/master
}
