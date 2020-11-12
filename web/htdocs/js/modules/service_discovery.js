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
import * as async_progress from "async_progress";
<<<<<<< HEAD
=======
import * as page_menu from "page_menu";
>>>>>>> upstream/master

//#   +--------------------------------------------------------------------+
//#   | Handling of the asynchronous service discovery dialog              |
//#   '--------------------------------------------------------------------'

// Stores the latest discovery_result object which was used by the python
// code to render the current page. It will be sent back to the python
// code for further actions. It contains the check_table which actions of
// the user are based on.
var g_service_discovery_result = null;
var g_show_updating_timer = null;

<<<<<<< HEAD
export function start(host_name, folder_path, discovery_options, transid, request_vars)
{
    // When we receive no response for 2 seconds, then show the updating message
    g_show_updating_timer = setTimeout(function() {
        async_progress.show_info("Updating...");
    }, 2000);

    lock_controls(true);
    async_progress.monitor({
        "update_url" : "ajax_service_discovery.py",
        "host_name": host_name,
        "folder_path": folder_path,
        "transid": transid,
        "start_time" : utils.time(),
        "is_finished_function": is_finished,
        "update_function": update,
        "finish_function": finish,
        "error_function": error,
        "post_data": get_post_data(host_name, folder_path, discovery_options, transid, request_vars)
    });
}

function get_post_data(host_name, folder_path, discovery_options, transid, request_vars)
{
    var request = {
        "host_name": host_name,
        "folder_path": folder_path,
        "discovery_options": discovery_options,
        "discovery_result": g_service_discovery_result
=======
export function start(host_name, folder_path, discovery_options, transid, request_vars) {
    // When we receive no response for 2 seconds, then show the updating message
    g_show_updating_timer = setTimeout(function () {
        async_progress.show_info("Updating...");
    }, 2000);

    lock_controls(true, get_state_independent_controls().concat(get_page_menu_controls()));
    async_progress.monitor({
        update_url: "ajax_service_discovery.py",
        host_name: host_name,
        folder_path: folder_path,
        transid: transid,
        start_time: utils.time(),
        is_finished_function: is_finished,
        update_function: update,
        finish_function: finish,
        error_function: error,
        post_data: get_post_data(host_name, folder_path, discovery_options, transid, request_vars),
    });
}

function get_post_data(host_name, folder_path, discovery_options, transid, request_vars) {
    var request = {
        host_name: host_name,
        folder_path: folder_path,
        discovery_options: discovery_options,
        discovery_result: g_service_discovery_result,
>>>>>>> upstream/master
    };

    if (request_vars !== undefined && request_vars !== null) {
        request = Object.assign(request, request_vars);
    }

    if (discovery_options.action == "bulk_update") {
        var checked_checkboxes = [];
        var checkboxes = document.getElementsByClassName("service_checkbox");
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                checked_checkboxes.push(checkboxes[i].name);
            }
        }
        request["update_services"] = checked_checkboxes;
    }

    var post_data = "request=" + encodeURIComponent(JSON.stringify(request));

    // Can currently not be put into "request" because the generic transaction
    // manager relies on the HTTP var _transid.
<<<<<<< HEAD
    if (transid !== undefined)
        post_data += "&_transid=" + encodeURIComponent(transid);
=======
    if (transid !== undefined) post_data += "&_transid=" + encodeURIComponent(transid);
>>>>>>> upstream/master

    return post_data;
}

function is_finished(response) {
    return response.is_finished;
}

<<<<<<< HEAD
function finish(response)
{
    if (response.job_state == "exception"
        || response.job_state == "stopped") {
=======
function finish(response) {
    if (response.job_state == "exception" || response.job_state == "stopped") {
>>>>>>> upstream/master
        async_progress.show_error(response.message);
    } else {
        //async_progress.hide_msg();
    }
<<<<<<< HEAD
    lock_controls(false);
}

function error(response)
{
=======

    // Only unlock the "per service" actions here. The page menu entries are unlocked by individual
    // calls to enable_page_menu_entry depending on the state of the page.
    lock_controls(false, get_state_independent_controls());
}

function error(response) {
>>>>>>> upstream/master
    if (g_show_updating_timer) {
        clearTimeout(g_show_updating_timer);
    }
    async_progress.show_error(response);
}

<<<<<<< HEAD

=======
>>>>>>> upstream/master
function update(handler_data, response) {
    if (g_show_updating_timer) {
        clearTimeout(g_show_updating_timer);
    }

    if (response.message) {
        async_progress.show_info(response.message);
    } else {
        async_progress.hide_msg();
    }

    g_service_discovery_result = response.discovery_result;
<<<<<<< HEAD
    handler_data.post_data = get_post_data(handler_data.host_name, handler_data.folder_path, response.discovery_options, handler_data.transid);

=======
    handler_data.post_data = get_post_data(
        handler_data.host_name,
        handler_data.folder_path,
        response.discovery_options,
        handler_data.transid
    );

    // Update the page menu
    var page_menu_bar = document.getElementById("page_menu_bar");
    page_menu_bar.outerHTML = response.page_menu;
    utils.execute_javascript_by_object(page_menu_bar);

    // Update the content table
>>>>>>> upstream/master
    var container = document.getElementById("service_container");
    container.style.display = "block";
    container.innerHTML = response.body;
    utils.execute_javascript_by_object(container);

<<<<<<< HEAD
    update_activate_changes_button(response);
}

function update_activate_changes_button(response)
{
    var tmp_container = document.createElement("div");
    tmp_container.innerHTML = response.changes_button;
    var context_buttons_container = document.getElementsByClassName("contextlinks")[0];
    var cur_changes_button = context_buttons_container.childNodes[0];
    context_buttons_container.replaceChild(tmp_container.childNodes[0].childNodes[0], cur_changes_button);
}

function lock_controls(lock)
{
    var elements = [];
    //elements.push(document.getElementById("activate_affected"));
    //elements.push(document.getElementById("activate_selected"));
    //// TODO: Remove once new changes mechanism has been implemented
    //elements.push(document.getElementById("discard_changes_button"));

    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("service_checkbox"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("button"), 0));
    elements = elements.concat(Array.prototype.slice.call(document.getElementsByClassName("service_button"), 0));

    for (var i = 0; i < elements.length; i++) {
        if (!elements[i])
            continue;

        if (lock)
            utils.add_class(elements[i], "disabled");
        else
            utils.remove_class(elements[i], "disabled");

        elements[i].disabled = lock;
    }
}

export function execute_active_check(site, folder_path, hostname, checktype, item, divid)
{
    var oDiv = document.getElementById(divid);
    var url = "wato_ajax_execute_check.py?" +
           "site="       + encodeURIComponent(site) +
           "&folder="    + encodeURIComponent(folder_path) +
           "&host="      + encodeURIComponent(hostname)  +
           "&checktype=" + encodeURIComponent(checktype) +
           "&item="      + encodeURIComponent(item);
    ajax.get_url(url, handle_execute_active_check, oDiv);
}


function handle_execute_active_check(oDiv, response_json)
{
=======
    page_menu.update_page_state_top_line(response.pending_changes_info);

    // Also execute delayed active checks once to trigger delayed checks that are initially visible.
    trigger_delayed_active_checks();
}

function get_state_independent_controls() {
    var elements = [];
    elements = elements.concat(
        Array.prototype.slice.call(document.getElementsByClassName("service_checkbox"), 0)
    );
    elements = elements.concat(
        Array.prototype.slice.call(document.getElementsByClassName("service_button"), 0)
    );
    elements = elements.concat(
        Array.prototype.slice.call(document.getElementsByClassName("toggle"), 0)
    );
    return elements;
}

function get_page_menu_controls() {
    return Array.prototype.slice.call(document.getElementsByClassName("action"), 0);
}

function lock_controls(lock, elements) {
    let element;
    for (var i = 0; i < elements.length; i++) {
        element = elements[i];
        if (!element) continue;

        if (lock) utils.add_class(element, "disabled");
        else utils.remove_class(element, "disabled");

        element.disabled = lock;
    }
}

var g_delayed_active_checks = [];

export function register_delayed_active_check(site, folder_path, hostname, checktype, item, divid) {
    // Register event listeners on first call
    if (g_delayed_active_checks.length == 0) {
        utils
            .content_scrollbar()
            .getScrollElement()
            .addEventListener("scroll", trigger_delayed_active_checks);
        utils.add_event_handler("resize", trigger_delayed_active_checks);
    }

    g_delayed_active_checks.push({
        site: site,
        folder_path: folder_path,
        hostname: hostname,
        checktype: checktype,
        item: item,
        divid: divid,
    });
}

// Is executed on scroll / resize events in case at least one graph is
// using the delayed graph rendering mechanism
function trigger_delayed_active_checks() {
    var num_delayed = g_delayed_active_checks.length;
    if (num_delayed == 0) return; // no delayed graphs: Nothing to do

    var i = num_delayed;
    while (i--) {
        var entry = g_delayed_active_checks[i];
        if (utils.is_in_viewport(document.getElementById(entry.divid))) {
            execute_active_check(entry);
            g_delayed_active_checks.splice(i, 1);
        }
    }
    return true;
}

export function execute_active_check(entry) {
    var div = document.getElementById(entry.divid);
    var url =
        "wato_ajax_execute_check.py?" +
        "site=" +
        encodeURIComponent(entry.site) +
        "&folder=" +
        encodeURIComponent(entry.folder_path) +
        "&host=" +
        encodeURIComponent(entry.hostname) +
        "&checktype=" +
        encodeURIComponent(entry.checktype) +
        "&item=" +
        encodeURIComponent(entry.item);
    ajax.get_url(url, handle_execute_active_check, div);
}

function handle_execute_active_check(oDiv, response_json) {
>>>>>>> upstream/master
    var response = JSON.parse(response_json);

    var state, statename, output;
    if (response.result_code == 1) {
        state = 3;
        statename = "UNKN";
        output = response.result;
    } else {
        state = response.result.state;
<<<<<<< HEAD
        if (state == -1)
            state = "p"; // Pending
        statename = response.result.state_name;
        output    = response.result.output;
=======
        if (state == -1) state = "p"; // Pending
        statename = response.result.state_name;
        output = response.result.output;
>>>>>>> upstream/master
    }

    oDiv.innerHTML = output;

    // Change name and class of status columns
    var oTr = oDiv.parentNode.parentNode;
<<<<<<< HEAD
    if (utils.has_class(oTr, "even0"))
        utils.add_class(oTr, "even" + state);
    else
        utils.add_class(oTr, "odd" + state);
=======
    if (utils.has_class(oTr, "even0")) utils.add_class(oTr, "even" + state);
    else utils.add_class(oTr, "odd" + state);
>>>>>>> upstream/master

    var oTdState = oTr.getElementsByClassName("state")[0];
    utils.remove_class(oTdState, "statep");
    utils.add_class(oTdState, "state" + state);

    oTdState.innerHTML = statename;
}
