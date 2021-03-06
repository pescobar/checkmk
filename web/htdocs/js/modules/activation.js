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
import * as async_progress from "async_progress";
import * as utils from "utils";
<<<<<<< HEAD
=======
import * as page_menu from "page_menu";
>>>>>>> upstream/master

//#.
//#   .-Activation---------------------------------------------------------.
//#   |              _        _   _            _   _                       |
//#   |             / \   ___| |_(_)_   ____ _| |_(_) ___  _ __            |
//#   |            / _ \ / __| __| \ \ / / _` | __| |/ _ \| '_ \           |
//#   |           / ___ \ (__| |_| |\ V / (_| | |_| | (_) | | | |          |
//#   |          /_/   \_\___|\__|_| \_/ \__,_|\__|_|\___/|_| |_|          |
//#   |                                                                    |
//#   +--------------------------------------------------------------------+
//#   | The WATO activation works this way:                                |
//#   | a) The user chooses one activation mode (affected sites, selected  |
//#   |    sites or a single site)                                         |
//#   | b) The JS GUI starts a single "worker" which calls the python code |
//#   |    first to locking the sites and creating the sync snapshot(s)    |
//#   | c) Then the snapshot is synced to the sites and activated on the   |
//#   |    sites indidivually.                                             |
//#   | d) Once a site finishes, it's changes are commited and the site is |
//#   |    unlocked individually.                                          |
//#   '--------------------------------------------------------------------'

<<<<<<< HEAD
export function activate_changes(mode, site_id)
{
=======
export function activate_changes(mode, site_id) {
>>>>>>> upstream/master
    var sites = [];

    if (mode == "selected") {
        var checkboxes = document.getElementsByClassName("site_checkbox");
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                // strip leading "site_" to get the site id
                sites.push(checkboxes[i].name.substr(5));
            }
        }

        if (sites.length == 0) {
            async_progress.show_error("You have to select a site.");
            return;
        }
<<<<<<< HEAD

=======
>>>>>>> upstream/master
    } else if (mode == "site") {
        sites.push(site_id);
    }

    var activate_until = document.getElementById("activate_until");
<<<<<<< HEAD
    if (!activate_until)
        return;

    var comment = "";
    var comment_field = document.getElementsByName("activate_p_comment")[0];
    if (comment_field.value != "")
        comment = comment_field.value;

    var activate_foreign = 0;
    var foreign_checkbox = document.getElementsByName("activate_p_foreign")[0];
    if (foreign_checkbox && foreign_checkbox.checked)
        activate_foreign = 1;
=======
    if (!activate_until) return;

    var comment = "";
    var comment_field = document.getElementsByName("activate_p_comment")[0];
    if (comment_field && comment_field.value != "") comment = comment_field.value;

    var activate_foreign = 0;
    var foreign_checkbox = document.getElementsByName("activate_p_foreign")[0];
    if (foreign_checkbox && foreign_checkbox.checked) activate_foreign = 1;
>>>>>>> upstream/master

    start_activation(sites, activate_until.value, comment, activate_foreign);
}

<<<<<<< HEAD
function start_activation(sites, activate_until, comment, activate_foreign)
{
    async_progress.show_info("Initializing activation...");

    var post_data = "activate_until=" + encodeURIComponent(activate_until)
                  + "&sites=" + encodeURIComponent(sites.join(","))
                  + "&comment=" + encodeURIComponent(comment)
                  + "&activate_foreign=" + encodeURIComponent(activate_foreign);

    ajax.call_ajax("ajax_start_activation.py", {
        response_handler : handle_start_activation,
        error_handler    : handle_start_activation_error,
        method           : "POST",
        post_data        : post_data,
        add_ajax_id      : false
    });

    lock_activation_controls(true);
    hide_last_results();
    show_details(false);
}

function handle_start_activation(_unused, response_json)
{
=======
function start_activation(sites, activate_until, comment, activate_foreign) {
    async_progress.show_info("Initializing activation...");

    var post_data =
        "activate_until=" +
        encodeURIComponent(activate_until) +
        "&sites=" +
        encodeURIComponent(sites.join(",")) +
        "&comment=" +
        encodeURIComponent(comment) +
        "&activate_foreign=" +
        encodeURIComponent(activate_foreign);

    ajax.call_ajax("ajax_start_activation.py", {
        response_handler: handle_start_activation,
        error_handler: handle_start_activation_error,
        method: "POST",
        post_data: post_data,
        add_ajax_id: false,
    });

    lock_activation_controls(true);
}

function handle_start_activation(_unused, response_json) {
>>>>>>> upstream/master
    var response = JSON.parse(response_json);

    if (response.result_code == 1) {
        async_progress.show_error(response.result);
        lock_activation_controls(false);
    } else {
        async_progress.show_info("Activating...");
        async_progress.monitor({
<<<<<<< HEAD
            "update_url" : "ajax_activation_state.py?activation_id=" + encodeURIComponent(response.result.activation_id),
            "start_time" : utils.time(),
            "update_function": update_activation_state,
            "is_finished_function": is_activation_progress_finished,
            "finish_function": finish_activation,
            "error_function": function(response) {
                async_progress.show_error(response);
            },
            "post_data": ""
=======
            update_url:
                "ajax_activation_state.py?activation_id=" +
                encodeURIComponent(response.result.activation_id),
            start_time: utils.time(),
            update_function: update_activation_state,
            is_finished_function: is_activation_progress_finished,
            finish_function: finish_activation,
            error_function: function (response) {
                async_progress.show_error(response);
            },
            post_data: "",
>>>>>>> upstream/master
        });
    }
}

<<<<<<< HEAD
function handle_start_activation_error(_unused, status_code, error_msg)
{
    async_progress.show_error("Failed to start activation ["+status_code+"]: " + error_msg);
    finish_activation();
}

function lock_activation_controls(lock)
{
    var elements = [];
    elements.push(document.getElementById("activate_affected"));
    elements.push(document.getElementById("activate_selected"));
    // TODO: Remove once new changes mechanism has been implemented
    elements.push(document.getElementById("discard_changes_button"));

    elements = elements.concat(Array.prototype.slice.call(document.getElementsByName("activate_p_comment"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("site_checkbox"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("activate_site"), 0));

    for (var i = 0; i < elements.length; i++) {
        if (!elements[i])
            continue;

        if (lock)
            utils.add_class(elements[i], "disabled");
        else
            utils.remove_class(elements[i], "disabled");

        elements[i].disabled = lock ? "disabled" : false;
    }
}

function hide_last_results()
{
    var elements = [];
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("last_result"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("header_last_result"), 0));

    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = "none";
    }
}

function show_details(show)
{
    var elements = [];
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("details"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("header_details"), 0));

    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = show ? "table-cell" : "none";
    }
}

// Make the cells visible which are needed during sync
function show_progress(show)
{
    var elements = [];
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("repprogress"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("header_repprogress"), 0));

    for (var i = 0; i < elements.length; i++) {
        elements[i].style.display = show ? "table-cell" : "none";
    }
}

function is_activation_progress_finished(response)
{
    for (var site_id in response["sites"]) {
        // skip loop if the property is from prototype
        if (!response["sites"].hasOwnProperty(site_id))
            continue;

        var site_state = response["sites"][site_id];
        if (site_state["_phase"] != "done")
            return false;
=======
function handle_start_activation_error(_unused, status_code, error_msg) {
    async_progress.show_error("Failed to start activation [" + status_code + "]: " + error_msg);
}

function lock_activation_controls(lock) {
    var elements = [];

    elements = elements.concat(
        Array.prototype.slice.call(document.getElementsByName("activate_p_comment"), 0)
    );
    elements = elements.concat(
        Array.prototype.slice.call(document.getElementsByClassName("site_checkbox"), 0)
    );
    elements = elements.concat(
        Array.prototype.slice.call(document.getElementsByClassName("activate_site"), 0)
    );

    for (var i = 0; i < elements.length; i++) {
        if (!elements[i]) continue;

        if (lock) utils.add_class(elements[i], "disabled");
        else utils.remove_class(elements[i], "disabled");

        elements[i].disabled = lock ? "disabled" : false;
    }

    page_menu.enable_menu_entry("activate_affected", !lock);
    page_menu.enable_menu_entry("activate_selected", !lock);
    page_menu.enable_menu_entry("discard_changes", !lock);
}

function is_activation_progress_finished(response) {
    for (var site_id in response["sites"]) {
        // skip loop if the property is from prototype
        if (!response["sites"].hasOwnProperty(site_id)) continue;

        var site_state = response["sites"][site_id];
        if (site_state["_phase"] != "done") return false;
>>>>>>> upstream/master
    }

    return true;
}

<<<<<<< HEAD
function update_activation_state(_unused_handler_data, response)
{
    for (var site_id in response["sites"]) {
        // skip loop if the property is from prototype
        if (!response["sites"].hasOwnProperty(site_id))
            continue;
=======
function update_activation_state(_unused_handler_data, response) {
    for (var site_id in response["sites"]) {
        // skip loop if the property is from prototype
        if (!response["sites"].hasOwnProperty(site_id)) continue;
>>>>>>> upstream/master

        var site_state = response["sites"][site_id];

        // Catch empty site states
        var is_empty = true;
        for (var prop in site_state) {
            if (site_state.hasOwnProperty(prop)) {
                is_empty = false;
                break;
            }
        }

<<<<<<< HEAD
        if (is_empty)
            throw "Empty site state for " + site_id;
=======
        // Due to the asynchroneous nature of the activate changes site scheduler
        // the site state file may not be present within the first seconds
        if (is_empty) continue;
>>>>>>> upstream/master

        update_site_activation_state(site_state);
    }
}

<<<<<<< HEAD
function update_site_activation_state(site_state)
{
=======
export function update_site_activation_state(site_state) {
>>>>>>> upstream/master
    // Show status text (overlay text on the progress bar)
    var msg = document.getElementById("site_" + site_state["_site_id"] + "_status");
    msg.innerHTML = site_state["_status_text"];

    if (site_state["_phase"] == "done") {
<<<<<<< HEAD
        utils.add_class(msg, "state_" + site_state["_state"]);
=======
        utils.remove_class(msg, "in_progress");
        utils.add_class(msg, "state_" + site_state["_state"]);
    } else {
        utils.add_class(msg, "in_progress");
>>>>>>> upstream/master
    }

    // Show status details
    if (site_state["_status_details"]) {
<<<<<<< HEAD
        show_details(true);

=======
>>>>>>> upstream/master
        msg = document.getElementById("site_" + site_state["_site_id"] + "_details");
        msg.innerHTML = site_state["_status_details"];
    }

    update_site_progress(site_state);
}

<<<<<<< HEAD
function update_site_progress(site_state)
{
    var max_width = 160;

    var progress = document.getElementById("site_" + site_state["_site_id"] + "_progress");
    show_progress(true);

    if (site_state["_phase"] == "done") {
        progress.style.width = max_width + "px";
        utils.add_class(progress, "state_" + site_state["_state"]);
        return;
=======
function update_site_progress(site_state) {
    var max_width = 160;

    var progress = document.getElementById("site_" + site_state["_site_id"] + "_progress");

    if (site_state["_phase"] == "done") {
        progress.style.width = max_width + "px";

        utils.remove_class(progress, "in_progress");
        utils.add_class(progress, "state_" + site_state["_state"]);
        return;
    } else {
        utils.add_class(progress, "in_progress");
>>>>>>> upstream/master
    }

    // TODO: Visualize overdue

    var duration = parseFloat(utils.time() - site_state["_time_started"]);

    var expected_duration = site_state["_expected_duration"];
<<<<<<< HEAD
    var duration_percent = duration * 100.0 / expected_duration;
    var width = parseInt(parseFloat(max_width) * duration_percent / 100);

    if (width > max_width)
        width = max_width;
=======
    var duration_percent = (duration * 100.0) / expected_duration;
    var width = parseInt((parseFloat(max_width) * duration_percent) / 100);

    if (width > max_width) width = max_width;
>>>>>>> upstream/master

    progress.style.width = width + "px";
}

<<<<<<< HEAD
function finish_activation()
{
    async_progress.show_info("Activation has finished. Reloading in 1 second.");
    lock_activation_controls(false);

    // Maybe change this not to make a reload and only update the relevant
    // parts of the activate changes page.
    utils.schedule_reload("", 1000);
=======
function finish_activation(result) {
    utils.schedule_reload(utils.makeuri({_finished: "1"}), 1000);
>>>>>>> upstream/master

    // Trigger a reload of the sidebar (to update changes in WATO snapin)
    utils.reload_sidebar();
}
