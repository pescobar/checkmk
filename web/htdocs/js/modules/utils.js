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

import SimpleBar from "simplebar";
>>>>>>> upstream/master

import * as ajax from "ajax";
import * as selection from "selection";

<<<<<<< HEAD
export const browser = {
    agent: navigator.userAgent.toLowerCase(),
    is_opera: function() { return this.agent.indexOf("opera") != -1; },
    is_firefox: function() { return this.agent.indexOf("firefox") != -1 || this.agent.indexOf("namoroka") != -1; },
    is_ie_below_9: function() { return document.all && !document.addEventListener; }
=======
let g_content_scrollbar = null;

export const browser = {
    agent: navigator.userAgent.toLowerCase(),
    is_opera: function () {
        return this.agent.indexOf("opera") != -1;
    },
    is_firefox: function () {
        return this.agent.indexOf("firefox") != -1 || this.agent.indexOf("namoroka") != -1;
    },
    is_ie_below_9: function () {
        return document.all && !document.addEventListener;
    },
>>>>>>> upstream/master
};

// simple implementation of function default arguments when
// using objects as function parameters. Example:
// function xxx(args) {
//     args = merge_args({
//         'arg2': 'default_val',
//     });
// }
// xxx({
//   'arg1': 'val1',
//   'arg3': 'val3',
// })
<<<<<<< HEAD
export function merge_args(defaults, args = {})
{
    for (var name in args)
        defaults[name] = args[name];
=======
export function merge_args(defaults, args = {}) {
    for (var name in args) defaults[name] = args[name];
>>>>>>> upstream/master

    return defaults;
}

export function prevent_default_events(event) {
    event.preventDefault();
    event.stopPropagation();
    return false;
}

<<<<<<< HEAD

// Updates the contents of a snapin or dashboard container after get_url
export function update_contents(id, code)
{
=======
// Updates the contents of a snapin or dashboard container after get_url
export function update_contents(id, code) {
>>>>>>> upstream/master
    var obj = document.getElementById(id);
    if (obj) {
        obj.innerHTML = code;
        execute_javascript_by_object(obj);
    }
}

export var current_script = null;

<<<<<<< HEAD
export function execute_javascript_by_object(obj)
{
    var aScripts = obj.getElementsByTagName("script");
    for(var i = 0; i < aScripts.length; i++) {
=======
export function execute_javascript_by_object(obj) {
    var aScripts = obj.getElementsByTagName("script");
    for (var i = 0; i < aScripts.length; i++) {
>>>>>>> upstream/master
        if (aScripts[i].src && aScripts[i].src !== "") {
            var oScr = document.createElement("script");
            oScr.src = aScripts[i].src;
            document.getElementsByTagName("HEAD")[0].appendChild(oScr);
<<<<<<< HEAD
        }
        else {
=======
        } else {
>>>>>>> upstream/master
            try {
                current_script = aScripts[i];
                eval(aScripts[i].text);
                current_script = null;
<<<<<<< HEAD
            } catch(e) {
                //console.log(e);
=======
            } catch (e) {
>>>>>>> upstream/master
                alert(aScripts[i].text + "\nError:" + e.message);
            }
        }
    }
}

// Whether or not the current browser window/tab is visible to the user
<<<<<<< HEAD
export function is_window_active()
{
    return !has_class(document.body, "hidden");
}

export function has_class(o, cn) {
    if (typeof(o.className) === "undefined")
        return false;
    var parts = o.className.split(" ");
    for (var x=0; x<parts.length; x++) {
        if (parts[x] == cn)
            return true;
=======
export function is_window_active() {
    return !has_class(document.body, "hidden");
}

// Predicate analogous to that used in JQuery to check whether an element is visible:
// https://github.com/jquery/jquery/blob/master/src/css/hiddenVisibleSelectors.js
export function is_visible(elem) {
    return !!(elem.offsetWidth || elem.offsetHeight || elem.getClientRects().length);
}

export function has_class(o, cn) {
    if (typeof o.className === "undefined") return false;
    let classname = o.className;
    if (o.className.baseVal !== undefined)
        // SVG className
        classname = o.className.baseVal;

    var parts = classname.split(" ");
    for (var x = 0; x < parts.length; x++) {
        if (parts[x] == cn) return true;
>>>>>>> upstream/master
    }
    return false;
}

export function remove_class(o, cn) {
    var parts = o.className.split(" ");
    var new_parts = Array();
<<<<<<< HEAD
    for (var x=0; x<parts.length; x++) {
        if (parts[x] != cn)
            new_parts.push(parts[x]);
=======
    for (var x = 0; x < parts.length; x++) {
        if (parts[x] != cn) new_parts.push(parts[x]);
>>>>>>> upstream/master
    }
    o.className = new_parts.join(" ");
}

export function add_class(o, cn) {
<<<<<<< HEAD
    if (!has_class(o, cn))
        o.className += " " + cn;
=======
    if (!has_class(o, cn)) o.className += " " + cn;
>>>>>>> upstream/master
}

export function change_class(o, a, b) {
    remove_class(o, a);
    add_class(o, b);
}

<<<<<<< HEAD
// Adds document/window global event handlers
// TODO: Move the window fallback to the call sites (when necessary) and nuke this function
export function add_event_handler(type, func, obj) {
    obj = (typeof(obj) === "undefined") ? window : obj;
    obj.addEventListener(type, func, false);
}

=======
export function toggle_class(o, a, b) {
    if (has_class(o, a)) change_class(o, a, b);
    else change_class(o, b, a);
}

// Adds document/window global event handlers
// TODO: Move the window fallback to the call sites (when necessary) and nuke this function
export function add_event_handler(type, func, obj) {
    obj = typeof obj === "undefined" ? window : obj;
    obj.addEventListener(type, func, false);
}

export function del_event_handler(type, func, obj) {
    obj = typeof obj === "undefined" ? window : obj;

    if (obj.removeEventListener) {
        // W3 stadnard browsers
        obj.removeEventListener(type, func, false);
    } else if (obj.detachEvent) {
        // IE<9
        obj.detachEvent("on" + type, func);
    } else {
        obj["on" + type] = null;
    }
}
>>>>>>> upstream/master

export function get_target(event) {
    return event.target ? event.target : event.srcElement;
}

export function get_button(event) {
    if (event.which == null)
        /* IE case */
<<<<<<< HEAD
        return (event.button < 2) ? "LEFT" : ((event.button == 4) ? "MIDDLE" : "RIGHT");
    else
        /* All others */
        return (event.which < 2) ? "LEFT" : ((event.which == 2) ? "MIDDLE" : "RIGHT");
}

export function page_height() {
    if (window.innerHeight !== null && typeof window.innerHeight !== "undefined" && window.innerHeight !== 0)
        return window.innerHeight;
    else if (document.documentElement && document.documentElement.clientHeight)
        return document.documentElement.clientHeight;
    else if (document.body !== null)
        return document.body.clientHeight;
=======
        return event.button < 2 ? "LEFT" : event.button == 4 ? "MIDDLE" : "RIGHT";
    /* All others */ else return event.which < 2 ? "LEFT" : event.which == 2 ? "MIDDLE" : "RIGHT";
}

export function page_height() {
    if (
        window.innerHeight !== null &&
        typeof window.innerHeight !== "undefined" &&
        window.innerHeight !== 0
    )
        return window.innerHeight;
    else if (document.documentElement && document.documentElement.clientHeight)
        return document.documentElement.clientHeight;
    else if (document.body !== null) return document.body.clientHeight;
>>>>>>> upstream/master
    return null;
}

export function page_width() {
<<<<<<< HEAD
    if (window.innerWidth !== null && typeof window.innerWidth !== "undefined" && window.innerWidth !== 0)
        return window.innerWidth;
    else if (document.documentElement && document.documentElement.clientWidth)
        return document.documentElement.clientWidth;
    else if (document.body !== null)
        return document.body.clientWidth;
    return null;
}


export function update_header_timer() {
    var container = document.getElementById("headertime");
    if (!container)
        return;
=======
    if (
        window.innerWidth !== null &&
        typeof window.innerWidth !== "undefined" &&
        window.innerWidth !== 0
    )
        return window.innerWidth;
    else if (document.documentElement && document.documentElement.clientWidth)
        return document.documentElement.clientWidth;
    else if (document.body !== null) return document.body.clientWidth;
    return null;
}

// Whether or not an element is partially in the the visible viewport
export function is_in_viewport(element) {
    var rect = element.getBoundingClientRect(),
        window_height = window.innerHeight || document.documentElement.clientHeight,
        window_width = window.innerWidth || document.documentElement.clientWidth;

    return (
        rect.top <= window_height &&
        rect.top + rect.height >= 0 &&
        rect.left <= window_width &&
        rect.left + rect.width >= 0
    );
}

export function update_header_timer() {
    var container = document.getElementById("headertime");
    if (!container) return;
>>>>>>> upstream/master

    var t = new Date();

    var hours = t.getHours();
<<<<<<< HEAD
    if (hours < 10)
        hours = "0" + hours;

    var min = t.getMinutes();
    if (min < 10)
        min = "0" + min;
=======
    if (hours < 10) hours = "0" + hours;

    var min = t.getMinutes();
    if (min < 10) min = "0" + min;
>>>>>>> upstream/master

    container.innerHTML = hours + ":" + min;

    var date = document.getElementById("headerdate");
<<<<<<< HEAD
    if (!date)
        return;

    var day   = ("0" + t.getDate()).slice(-2);
    var month = ("0" + (t.getMonth() + 1)).slice(-2);
    var year  = t.getFullYear();
=======
    if (!date) return;

    var day = ("0" + t.getDate()).slice(-2);
    var month = ("0" + (t.getMonth() + 1)).slice(-2);
    var year = t.getFullYear();
>>>>>>> upstream/master
    var date_format = date.getAttribute("format");
    date.innerHTML = date_format.replace(/yyyy/, year).replace(/mm/, month).replace(/dd/, day);
}

<<<<<<< HEAD
export function update_header_info(text)
{
    var oDiv = document.getElementById("headinfo");
    if (oDiv) {
        oDiv.innerHTML = text;
=======
export function has_header_info() {
    return document.getElementById("headinfo") !== null;
}

export function get_header_info() {
    // Return the current text (minus the separator prepended by update_header_info())
    return document.getElementById("headinfo").innerHTML.substr(2);
}

export function update_header_info(text) {
    var container = document.getElementById("headinfo");
    if (container) {
        container.innerHTML = ", " + text;
>>>>>>> upstream/master
    }
}

// Function gets the value of the given url parameter
export function get_url_param(name, url) {
    name = name.replace("[", "\\[").replace("]", "\\]");
<<<<<<< HEAD
    url = (typeof url === "undefined") ? window.location : url;

    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)");
    var results = regex.exec(url);
    if(results === null)
        return "";
=======
    url = typeof url === "undefined" ? window.location : url;

    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)");
    var results = regex.exec(url);
    if (results === null) return "";
>>>>>>> upstream/master
    return results[1];
}

/**
 * Function creates a new cleaned up URL
 * - Can add/overwrite parameters
 * - Removes _* parameters
 */
<<<<<<< HEAD
export function makeuri(addvars, url) {
    url = (typeof(url) === "undefined") ? window.location.href : url;

    var tmp = url.split("?");
    var base = tmp[0];
    if(tmp.length > 1) {
=======
export function makeuri(addvars, url, filename) {
    url = typeof url === "undefined" ? window.location.href : url;

    var tmp = url.split("?");
    var base = typeof filename === "undefined" ? tmp[0] : filename;
    if (tmp.length > 1) {
>>>>>>> upstream/master
        // Remove maybe existing anchors
        tmp = tmp[1].split("#");
        // Split to array of param-strings (key=val)
        tmp = tmp[0].split("&");
    } else {
        // Uri has no parameters
        tmp = [];
    }

    var params = [];
    var pair = null;

    // Skip unwanted parmas
<<<<<<< HEAD
    for(var i = 0; i < tmp.length; i++) {
        pair = tmp[i].split("=");
        if(pair[0][0] == "_" && pair[0] != "_username" && pair[0] != "_secret") // Skip _<vars>
            continue;
        if(addvars.hasOwnProperty(pair[0])) // Skip vars present in addvars
=======
    for (var i = 0; i < tmp.length; i++) {
        pair = tmp[i].split("=");
        if (pair[0][0] == "_" && pair[0] != "_username" && pair[0] != "_secret")
            // Skip _<vars>
            continue;
        if (addvars.hasOwnProperty(pair[0]))
            // Skip vars present in addvars
>>>>>>> upstream/master
            continue;
        params.push(tmp[i]);
    }

    // Add new params
    for (var key in addvars) {
        params.push(encodeURIComponent(key) + "=" + encodeURIComponent(addvars[key]));
    }

    return base + "?" + params.join("&");
}

<<<<<<< HEAD
// Returns timestamp in seconds incl. subseconds as decimal
export function time() {
    return (new Date()).getTime() / 1000;
}

var g_sidebar_reload_timer = null;

// reload sidebar, but preserve quicksearch field value and focus
export function reload_sidebar()
{
    if (!parent || !parent.frames[0]) {
        return;
    }

    var val = "";
    var focused = false;
    var field = parent.frames[0].document.getElementById("mk_side_search_field");
    if (field) {
        val = field.value;
        focused = parent.frames[0].document.activeElement == field;
    }

    parent.frames[0].document.reloading = 1;
    parent.frames[0].document.location.reload();

    if (!field) {
        return;
    }

    g_sidebar_reload_timer = setInterval(function (value, has_focus) {
        return function() {
            if (!parent.frames[0].document.reloading
                && parent.frames[0].document.readyState === "complete") {
                var field = parent.frames[0].document.getElementById("mk_side_search_field");
                if (field) {
                    field.value = value;
                    if (has_focus) {
                        field.focus();

                        // Move caret to end
                        if (field.setSelectionRange !== undefined)
                            field.setSelectionRange(value.length, value.length);
                    }
                }

                clearInterval(g_sidebar_reload_timer);
                g_sidebar_reload_timer = null;
            }
        };
    }(val, focused), 50);

    field = null;
=======
export function makeuri_contextless(vars, filename) {
    var params = [];
    // Add new params
    for (var key in vars) {
        params.push(encodeURIComponent(key) + "=" + encodeURIComponent(vars[key]));
    }

    return filename + "?" + params.join("&");
}

// Changes a parameter in the current pages URL without reloading the page
export function update_url_parameter(name, value) {
    // Only a solution for browsers with history.replaceState support. Sadly we have no
    // F5/reload fix for others...
    if (!window.history.replaceState) return;

    // Handle two cases:
    // a) The page is opened without navigation:
    // http://[HOST]/[SITE]/check_mk/dashboard.py?name=main&edit=1
    // b) The page is opened with the navigation (within an iframe):
    // http://[HOST]/[SITE]/check_mk/index.py?start_url=%2F[SITE]%2Fcheck_mk%2Fdashboard.py%3Fname%3Dmain&edit=1
    // The URL computation needs to deal with both cases
    const url = window.location.href;
    let new_url;
    if (url.indexOf("start_url") !== -1) {
        var frame_url = decodeURIComponent(get_url_param("start_url", url));
        frame_url = makeuri({[name]: value}, frame_url);
        new_url = makeuri({start_url: frame_url}, url);
    } else {
        new_url = makeuri({[name]: value}, url);
    }

    window.history.replaceState({}, window.document.title, new_url);
}

// Returns timestamp in seconds incl. subseconds as decimal
export function time() {
    return new Date().getTime() / 1000;
}

// reload sidebar, but preserve quicksearch field value and focus
export function reload_sidebar() {
    window.top.cmk.sidebar.reset_sidebar_scheduler();
>>>>>>> upstream/master
}

//#.
//#   .-Page Reload--------------------------------------------------------.
//#   |        ____                    ____      _                 _       |
//#   |       |  _ \ __ _  __ _  ___  |  _ \ ___| | ___   __ _  __| |      |
//#   |       | |_) / _` |/ _` |/ _ \ | |_) / _ \ |/ _ \ / _` |/ _` |      |
//#   |       |  __/ (_| | (_| |  __/ |  _ <  __/ | (_) | (_| | (_| |      |
//#   |       |_|   \__,_|\__, |\___| |_| \_\___|_|\___/ \__,_|\__,_|      |
//#   |                   |___/                                            |
//#   +--------------------------------------------------------------------+
//#   |                                                                    |
//#   '--------------------------------------------------------------------'

// Stores the reload timer object (of views and also dashboards)
var g_reload_timer = null;
// This stores the refresh time of the page (But never 0)
var g_reload_interval = 0; // seconds
// This flag tells the handle_content_reload_error() function to add an
// error message about outdated data to the content container or not.
// The error message is only being added on the first error.
var g_reload_error = false;

<<<<<<< HEAD
// When called with one or more parameters parameters it reschedules the
// timer to the given interval. If the parameter is 0 the reload is stopped.
// When called with two parmeters the 2nd one is used as new url.
export function set_reload(secs, url)
{
    stop_reload_timer();
    set_reload_interval(secs);
    if (secs !== 0) {
        schedule_reload(url);
    }
}


// Issues the timer for the next page reload. If some timer is already
// running, this timer is terminated and replaced by the new one.
export function schedule_reload(url, milisecs)
{
    if (typeof url === "undefined")
        url = ""; // reload current page (or just the content)

    if (typeof milisecs === "undefined")
        milisecs = parseFloat(g_reload_interval) * 1000; // use default reload interval

    stop_reload_timer();

    g_reload_timer = setTimeout(function() {
        do_reload(url);
    }, milisecs);
}


export function stop_reload_timer()
{
=======
// Reschedule the global timer to the given interval.
export function set_reload(secs, url) {
    stop_reload_timer();
    set_reload_interval(secs);
    schedule_reload(url);
}

// Issues the timer for the next page reload. If some timer is already
// running, this timer is terminated and replaced by the new one.
export function schedule_reload(url, remaining_ms) {
    if (typeof url === "undefined") url = ""; // reload current page (or just the content)

    if (typeof remaining_ms === "undefined") {
        if (g_reload_interval === 0) {
            return; // the reload interval is set to "off"
        }

        // initialize the timer with the configured interval
        remaining_ms = parseFloat(g_reload_interval) * 1000;
    }

    update_page_state_reload_indicator(remaining_ms);

    if (remaining_ms <= 0) {
        // The time is over. Now trigger the desired actions
        do_reload(url);

        // Prepare for the next update interval
        remaining_ms = parseFloat(g_reload_interval) * 1000;
    }

    stop_reload_timer();
    g_reload_timer = setTimeout(function () {
        schedule_reload(url, remaining_ms - 1000);
    }, 1000);
}

function update_page_state_reload_indicator(remaining_ms) {
    let icon = document.getElementById("page_state_icon");
    if (!icon) return; // Not present, no update needed

    let perc = (remaining_ms / (g_reload_interval * 1000)) * 100;

    icon.style.clipPath = "circle(" + Math.floor(perc) + "% at 100%)";
    icon.title = "Remaining: " + Math.floor(remaining_ms / 1000) + " sec.";
}

export function stop_reload_timer() {
>>>>>>> upstream/master
    if (g_reload_timer) {
        clearTimeout(g_reload_timer);
        g_reload_timer = null;
    }
}

<<<<<<< HEAD
function do_reload(url)
{
    // Reschedule the reload in case the browser window / tab is not visible
    // for the user. Retry after short time.
    if (!is_window_active()) {
        setTimeout(function(){ do_reload(url); }, 250);
=======
function do_reload(url) {
    // Reschedule the reload in case the browser window / tab is not visible
    // for the user. Retry after short time.
    if (!is_window_active()) {
        setTimeout(function () {
            do_reload(url);
        }, 250);
>>>>>>> upstream/master
        return;
    }

    // Nicht mehr die ganze Seite neu laden, wenn es ein DIV "data_container" gibt.
    // In dem Fall wird die aktuelle URL aus "window.location.href" geholt, für den Refresh
    // modifiziert, der Inhalt neu geholt und in das DIV geschrieben.
    if (!document.getElementById("data_container") || url !== "") {
<<<<<<< HEAD
        if (url === "")
            window.location.reload(false);
        else
            window.location.href = url;
    }
    else {
=======
        if (url === "") window.location.reload(false);
        else window.location.href = url;
    } else {
>>>>>>> upstream/master
        // Enforce specific display_options to get only the content data.
        // All options in "opts" will be forced. Existing upper-case options will be switched.
        var display_options = get_url_param("display_options");
        // Removed "w" to reflect original rendering mechanism during reload
        // For example show the "Your query produced more than 1000 results." message
        // in views even during reload.
<<<<<<< HEAD
        var opts = [ "h", "t", "b", "f", "c", "o", "d", "e", "r", "u" ];
=======
        var opts = ["h", "t", "b", "f", "c", "o", "d", "e", "r", "u"];
>>>>>>> upstream/master
        var i;
        for (i = 0; i < opts.length; i++) {
            if (display_options.indexOf(opts[i].toUpperCase()) > -1)
                display_options = display_options.replace(opts[i].toUpperCase(), opts[i]);
<<<<<<< HEAD
            else
                display_options += opts[i];
        }

        // Add optional display_options if not defined in original display_options
        opts = [ "w" ];
        for (i = 0; i < opts.length; i++) {
            if (display_options.indexOf(opts[i].toUpperCase()) == -1)
                display_options += opts[i];
        }

        var params = {"_display_options": display_options};
        var real_display_options = get_url_param("display_options");
        if (real_display_options !== "")
            params["display_options"] = real_display_options;
=======
            else display_options += opts[i];
        }

        // Add optional display_options if not defined in original display_options
        opts = ["w"];
        for (i = 0; i < opts.length; i++) {
            if (display_options.indexOf(opts[i].toUpperCase()) == -1) display_options += opts[i];
        }

        var params = {_display_options: display_options};
        var real_display_options = get_url_param("display_options");
        if (real_display_options !== "") params["display_options"] = real_display_options;
>>>>>>> upstream/master

        params["_do_actions"] = get_url_param("_do_actions");

        // For dashlet reloads add a parameter to mark this request as reload
<<<<<<< HEAD
        if (window.location.href.indexOf("dashboard_dashlet.py") != -1)
            params["_reload"] = "1";

        if (selection.is_selection_enabled())
            params["selection"] = selection.get_selection_id();

        ajax.call_ajax(makeuri(params), {
            response_handler : handle_content_reload,
            error_handler    : handle_content_reload_error,
            method           : "GET"
=======
        if (window.location.href.indexOf("dashboard_dashlet.py") != -1) params["_reload"] = "1";

        if (selection.is_selection_enabled()) params["selection"] = selection.get_selection_id();

        ajax.call_ajax(makeuri(params), {
            response_handler: handle_content_reload,
            error_handler: handle_content_reload_error,
            method: "GET",
>>>>>>> upstream/master
        });
    }
}

function handle_content_reload(_unused, code) {
    g_reload_error = false;
    var o = document.getElementById("data_container");
    o.innerHTML = code;
    execute_javascript_by_object(o);

    // Update the header time
    update_header_timer();

    schedule_reload();
}

<<<<<<< HEAD

function handle_content_reload_error(_unused, status_code)
{
    if (!g_reload_error) {
        var o = document.getElementById("data_container");
        o.innerHTML = "<div class=error>Update failed (" + status_code
                      + "). The shown data might be outdated</div>" + o.innerHTML;
=======
function handle_content_reload_error(_unused, status_code) {
    if (!g_reload_error) {
        var o = document.getElementById("data_container");
        o.innerHTML =
            "<div class=error>Update failed (" +
            status_code +
            "). The shown data might be outdated</div>" +
            o.innerHTML;
>>>>>>> upstream/master
        g_reload_error = true;
    }

    // Continue update after the error
    schedule_reload();
}

export function set_reload_interval(secs) {
<<<<<<< HEAD
    update_foot_refresh(secs);
=======
>>>>>>> upstream/master
    if (secs !== 0) {
        g_reload_interval = secs;
    }
}

<<<<<<< HEAD
function update_foot_refresh(secs)
{
    var o = document.getElementById("foot_refresh");
    var o2 = document.getElementById("foot_refresh_time");
    if (!o) {
        return;
    }

    if(secs == 0) {
        o.style.display = "none";
    } else {
        o.style.display = "inline-block";
        if(o2) {
            o2.innerHTML = secs;
        }
    }
}

=======
>>>>>>> upstream/master
export function toggle_folding(img, to_be_opened) {
    if (to_be_opened) {
        change_class(img, "closed", "open");
    } else {
        change_class(img, "open", "closed");
    }
}

// Relative to viewport
export function mouse_position(event) {
    return {
        x: event.clientX,
<<<<<<< HEAD
        y: event.clientY
    };
}

export function wheel_event_delta(event)
{
    return event.deltaY ? event.deltaY : event.detail ? event.detail * (-120) : event.wheelDelta;
}

export function wheel_event_name()
{
    if ("onwheel" in window)
        return "wheel";
    else if (browser.is_firefox())
        return "DOMMouseScroll";
    else
        return "mousewheel";
}

export function count_context_button(oA)
{
    // Extract view name from id of parent div element
    var handler = ajax.call_ajax("count_context_button.py?id=" + oA.parentNode.id, {
        sync:true
    });
    return handler.responseText;
}

export function unhide_context_buttons(toggle_button)
{
    var cells = toggle_button.parentNode.parentNode;
    var children = cells.children;
    for (var i = 0; i < children.length; i++) {
        var node = children[i];
        if (node.tagName == "DIV" && !has_class(node, "togglebutton"))
            node.style.display = "";
    }
    toggle_button.parentNode.style.display = "none";
}

var g_tag_groups = {
    "host": {},
    "service": {}
=======
        y: event.clientY,
    };
}

export function wheel_event_delta(event) {
    return event.deltaY ? event.deltaY : event.detail ? event.detail * -120 : event.wheelDelta;
}

export function wheel_event_name() {
    if ("onwheel" in window) return "wheel";
    else if (browser.is_firefox()) return "DOMMouseScroll";
    else return "mousewheel";
}

var g_tag_groups = {
    host: {},
    service: {},
>>>>>>> upstream/master
};

export function set_tag_groups(object_type, grouped) {
    g_tag_groups[object_type] = grouped;
}

export function tag_update_value(object_type, prefix, grp) {
    var value_select = document.getElementById(prefix + "_val");

    // Remove all options
    value_select.options.length = 0;

<<<<<<< HEAD
    if(grp === "")
        return; // skip over when empty group selected
=======
    if (grp === "") return; // skip over when empty group selected
>>>>>>> upstream/master

    var opt = null;
    for (var i = 0, len = g_tag_groups[object_type][grp].length; i < len; i++) {
        opt = document.createElement("option");
        opt.value = g_tag_groups[object_type][grp][i][0];
<<<<<<< HEAD
        opt.text  = g_tag_groups[object_type][grp][i][1];
        value_select.appendChild(opt);
    }
}
=======
        opt.text = g_tag_groups[object_type][grp][i][1];
        value_select.appendChild(opt);
    }
}

export function toggle_more(trigger, toggle_id, dom_levels_up) {
    event.stopPropagation();
    let container = trigger;
    let state;
    for (var i = 0; i < dom_levels_up; i++) {
        container = container.parentNode;
        while (container.className.includes("simplebar-")) container = container.parentNode;
    }

    if (has_class(container, "more")) {
        change_class(container, "more", "less");
        state = "off";
    } else {
        change_class(container, "less", "more");
        // The class withanimation is used to fade in the formlery
        // hidden items - which must not be done when they are already
        // visible when rendering the page.
        add_class(container, "withanimation");
        state = "on";
    }

    ajax.get_url(
        "tree_openclose.py?tree=more_buttons" +
            "&name=" +
            encodeURIComponent(toggle_id) +
            "&state=" +
            encodeURIComponent(state)
    );
}

export function add_simplebar_scrollbar(scrollable_id) {
    return add_simplebar_scrollbar_to_object(document.getElementById(scrollable_id));
}

export function add_simplebar_scrollbar_to_object(obj) {
    return new SimpleBar(obj);
}

export function content_scrollbar(scrollable_id) {
    if (g_content_scrollbar === null) g_content_scrollbar = add_simplebar_scrollbar(scrollable_id);
    return g_content_scrollbar;
}
>>>>>>> upstream/master
