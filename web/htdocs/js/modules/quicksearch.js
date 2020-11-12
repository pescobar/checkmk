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

import { get_url } from "ajax";
=======
// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.

import {get_url} from "ajax";
>>>>>>> upstream/master

var iCurrent = null;
var oCurrent = null;
var oldValue = "";
var g_ajax_obj = null;

// Register an input field to be a search field and add eventhandlers
export function register_search_field(field) {
    var oField = document.getElementById(field);
<<<<<<< HEAD
    if(oField) {
        oField.onkeydown = function(e) { if (!e) e = window.event; return mkSearchKeyDown(e, oField); };
        oField.onkeyup   = function(e) { if (!e) e = window.event; return mkSearchKeyUp(e, oField); };
        oField.onclick   = function() { close_popup(); return true; };

        // On doubleclick toggle the list
        oField.ondblclick  = function() { toggle_popup(oField); };
=======
    if (oField) {
        oField.onkeydown = function (e) {
            if (!e) e = window.event;
            return mkSearchKeyDown(e, oField);
        };
        oField.onkeyup = function (e) {
            if (!e) e = window.event;
            return mkSearchKeyUp(e, oField);
        };
        oField.onclick = function () {
            close_popup();
            return true;
        };

        // On doubleclick toggle the list
        oField.ondblclick = function () {
            toggle_popup(oField);
        };
>>>>>>> upstream/master
    }
}

// On key release event handler
function mkSearchKeyUp(e, oField) {
    var keyCode = e.which || e.keyCode;

    switch (keyCode) {
        // 18: Return/Enter
        // 27: Escape
        case 13:
        case 27:
            close_popup();
            e.returnValue = false;
            e.cancelBubble = true;
            break;

        // Other keys
        default:
            if (oField.value == "") {
                e.returnValue = false;
                e.cancelBubble = true;
                close_popup();
<<<<<<< HEAD
            }
            else {
=======
            } else {
>>>>>>> upstream/master
                mkSearch(oField);
            }
            break;
    }
}

// On key press down event handler
export function on_search_click() {
    var oField = document.getElementById("mk_side_search_field");
<<<<<<< HEAD
    var ev = { "which" : 0, "keyCode" : 13 };
=======
    var ev = {which: 0, keyCode: 13};
>>>>>>> upstream/master
    return mkSearchKeyDown(ev, oField);
}

function search_dropdown_value() {
<<<<<<< HEAD
    if (oCurrent)
        return oCurrent.id.replace("result_", "");
    else
        return null;
=======
    if (oCurrent) return oCurrent.id.replace("result_", "");
    else return null;
>>>>>>> upstream/master
}

function mkSearchKeyDown(e, oField) {
    var keyCode = e.which || e.keyCode;

    switch (keyCode) {
        // Return/Enter
        case 13:
            if (oCurrent != null) {
                mkSearchNavigate();
                oField.value = search_dropdown_value();
                close_popup();
            } else {
                if (oField.value == "")
                    return; /* search field empty, rather not show all services! */
                // When nothing selected, navigate with the current contents of the field
<<<<<<< HEAD
                top.frames["main"].location.href = "search_open.py?q=" + encodeURIComponent(oField.value);
=======
                top.frames["main"].location.href =
                    "search_open.py?q=" + encodeURIComponent(oField.value);
>>>>>>> upstream/master
                mkTermSearch();
                close_popup();
            }

            e.returnValue = false;
            e.cancelBubble = true;
            break;

        // Escape
        case 27:
            close_popup();
            e.returnValue = false;
            e.cancelBubble = true;
            break;

        // Tab
        case 9:
<<<<<<< HEAD
            if(mkSearchResultShown()) {
=======
            if (mkSearchResultShown()) {
>>>>>>> upstream/master
                close_popup();
            }
            return;

        // Up/Down arrow (Must not be handled in onkeyup since this does not fire repeated events)
        case 38:
        case 40:
<<<<<<< HEAD
            if(!mkSearchResultShown()) {
=======
            if (!mkSearchResultShown()) {
>>>>>>> upstream/master
                mkSearch(oField);
            }

            mkSearchMoveElement(keyCode == 38 ? -1 : 1);

            e.preventDefault();
            return false;
    }
    oldValue = oField.value;
}

// Navigate to the target of the selected event
function mkSearchNavigate() {
    top.frames["main"].location.href = oCurrent.href;
}

// Move one step of given size in the result list
function mkSearchMoveElement(step) {
<<<<<<< HEAD
    if(iCurrent == null) {
=======
    if (iCurrent == null) {
>>>>>>> upstream/master
        iCurrent = -1;
    }

    iCurrent += step;

    var oResults = document.getElementById("mk_search_results");
<<<<<<< HEAD
    if (!oResults)
        return;

    if(iCurrent < 0)
        iCurrent = oResults.children.length-1;

    if(iCurrent > oResults.children.length-1)
        iCurrent = 0;
=======
    if (!oResults) return;

    if (iCurrent < 0) iCurrent = oResults.children.length - 1;

    if (iCurrent > oResults.children.length - 1) iCurrent = 0;
>>>>>>> upstream/master

    oResults = oResults.childNodes;

    var a = 0;
<<<<<<< HEAD
    for(var i = 0; i < oResults.length; i++) {
        if(oResults[i].tagName == "A") {
            if(a == iCurrent) {
=======
    for (var i = 0; i < oResults.length; i++) {
        if (oResults[i].tagName == "A") {
            if (a == iCurrent) {
>>>>>>> upstream/master
                oCurrent = oResults[i];
                oResults[i].setAttribute("class", "active");
            } else {
                oResults[i].setAttribute("class", "inactive");
            }
            a++;
        }
    }
}

// Is the result list shown at the moment?
function mkSearchResultShown() {
    return document.getElementById("mk_search_results") ? true : false;
}

// Toggle the result list
function toggle_popup(oField) {
<<<<<<< HEAD
    if(mkSearchResultShown()) {
=======
    if (mkSearchResultShown()) {
>>>>>>> upstream/master
        close_popup();
    } else {
        mkSearch(oField);
    }
}

// Close the result list
export function close_popup() {
    var oContainer = document.getElementById("mk_search_results");
<<<<<<< HEAD
    if(oContainer) {
=======
    if (oContainer) {
>>>>>>> upstream/master
        oContainer.parentNode.removeChild(oContainer);
    }

    iCurrent = null;
    oCurrent = null;
}

function handle_search_response(oField, code) {
    if (code != "") {
        var oContainer = document.getElementById("mk_search_results");
<<<<<<< HEAD
        if(!oContainer) {
=======
        if (!oContainer) {
>>>>>>> upstream/master
            oContainer = document.createElement("div");
            oContainer.setAttribute("id", "mk_search_results");
            oField.parentNode.appendChild(oContainer);
        }

        oContainer.innerHTML = code;
    } else {
        close_popup();
    }
}

function mkTermSearch() {
    // Terminate eventually already running request
    if (g_ajax_obj) {
        g_ajax_obj.abort();
        g_ajax_obj = null;
    }
}

// Build a new result list and show it up
function mkSearch(oField) {
<<<<<<< HEAD
    if(oField == null)
        return;

    var val = oField.value;
    if (mkSearchResultShown() && val == oldValue)
        return; // nothing changed, no new search
    oldValue = val;

    mkTermSearch();
    g_ajax_obj = get_url("ajax_search.py?q=" + encodeURIComponent(val), handle_search_response, oField);
=======
    if (oField == null) return;

    var val = oField.value;
    if (mkSearchResultShown() && val == oldValue) return; // nothing changed, no new search
    oldValue = val;

    mkTermSearch();
    g_ajax_obj = get_url(
        "ajax_search.py?q=" + encodeURIComponent(val),
        handle_search_response,
        oField
    );
>>>>>>> upstream/master
}
