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

import * as ajax from "ajax";
import * as utils from "utils";

//#.
//#   .-AsyncProg.---------------------------------------------------------.
//#   |           _                         ____                           |
//#   |          / \   ___ _   _ _ __   ___|  _ \ _ __ ___   __ _          |
//#   |         / _ \ / __| | | | '_ \ / __| |_) | '__/ _ \ / _` |         |
//#   |        / ___ \\__ \ |_| | | | | (__|  __/| | | (_) | (_| |_        |
//#   |       /_/   \_\___/\__, |_| |_|\___|_|   |_|  \___/ \__, (_)       |
//#   |                    |___/                            |___/          |
//#   +--------------------------------------------------------------------+
//#   | Generic asynchronous process handling used by activate changes and |
//#   | the service discovery dialogs                                      |
//#   '--------------------------------------------------------------------'

// Is called after the activation has been started (got the activation_id) and
// then in interval of 500 ms for updating the dialog state
<<<<<<< HEAD
export function monitor(handler_data)
{
    ajax.call_ajax(handler_data.update_url, {
        response_handler : handle_update,
        error_handler    : handle_error,
        handler_data     : handler_data,
        method           : "POST",
        post_data        : handler_data.post_data,
        add_ajax_id      : false
    });
}

function handle_update(handler_data, response_json)
{
=======
export function monitor(handler_data) {
    ajax.call_ajax(handler_data.update_url, {
        response_handler: handle_update,
        error_handler: handle_error,
        handler_data: handler_data,
        method: "POST",
        post_data: handler_data.post_data,
        add_ajax_id: false,
    });
}

function handle_update(handler_data, response_json) {
>>>>>>> upstream/master
    var response = JSON.parse(response_json);
    if (response.result_code == 1) {
        handler_data.error_function(response.result);
        return; // Abort on error!
    } else {
        handler_data.update_function(handler_data, response.result);

        if (!handler_data.is_finished_function(response.result)) {
<<<<<<< HEAD
            setTimeout(function() {
                return monitor(handler_data);
            }, 500);
        }
        else {
=======
            setTimeout(function () {
                return monitor(handler_data);
            }, 100);
        } else {
>>>>>>> upstream/master
            handler_data.finish_function(response.result);
        }
    }
}

<<<<<<< HEAD
function handle_error(handler_data, status_code, error_msg)
{
=======
function handle_error(handler_data, status_code, error_msg) {
>>>>>>> upstream/master
    if (utils.time() - handler_data.start_time <= 10 && status_code == 503) {
        show_info("Failed to fetch state. This may be normal for a period of some seconds.");
    } else if (status_code == 0) {
        return; // not really an error. Reached when navigating away from the page
    } else {
<<<<<<< HEAD
        show_error("Failed to fetch state ["+status_code+"]: " + error_msg + ". " +
                              "Retrying in 1 second." +
                              "<br><br>" +
                              "In case this error persists for more than some seconds, please verify that all " +
                              "processes of the site are running.");
    }

    setTimeout(function() {
=======
        show_error(
            "Failed to fetch state [" +
                status_code +
                "]: " +
                error_msg +
                ". " +
                "Retrying in 1 second." +
                "<br><br>" +
                "In case this error persists for more than some seconds, please verify that all " +
                "processes of the site are running."
        );
    }

    setTimeout(function () {
>>>>>>> upstream/master
        return monitor(handler_data);
    }, 1000);
}

<<<<<<< HEAD
export function show_error(text)
{
=======
export function show_error(text) {
>>>>>>> upstream/master
    var container = document.getElementById("async_progress_msg");
    container.style.display = "block";
    var msg = container.childNodes[0];

    utils.add_class(msg, "error");
    utils.remove_class(msg, "success");

    msg.innerHTML = text;
}

<<<<<<< HEAD
export function show_info(text)
{
=======
export function show_info(text) {
>>>>>>> upstream/master
    var container = document.getElementById("async_progress_msg");
    container.style.display = "block";
    var msg = container.childNodes[0];

    utils.add_class(msg, "success");
    utils.remove_class(msg, "error");

    msg.innerHTML = text;
}

<<<<<<< HEAD
export function hide_msg()
{
    var msg = document.getElementById("async_progress_msg");
    if (msg)
        msg.style.display = "none";
=======
export function hide_msg() {
    var msg = document.getElementById("async_progress_msg");
    if (msg) msg.style.display = "none";
>>>>>>> upstream/master
}
