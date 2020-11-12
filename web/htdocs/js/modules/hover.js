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

//#   +--------------------------------------------------------------------+
//#   | Mouseover hover menu, used for performance graph popups            |
//#   '--------------------------------------------------------------------'

var g_hover_menu = null;

<<<<<<< HEAD
export function hide()
{
=======
export function hide() {
>>>>>>> upstream/master
    if (!g_hover_menu) {
        return;
    }

    var hover_menu = g_hover_menu;
    g_hover_menu = null;
    hover_menu.parentNode.removeChild(hover_menu);
}

<<<<<<< HEAD
export function show(event, code)
{
=======
export function show(event, code) {
>>>>>>> upstream/master
    event = event || window.event;
    add();
    update_content(code);
    update_position(event);
}

<<<<<<< HEAD
export function add()
{
=======
export function add() {
>>>>>>> upstream/master
    if (g_hover_menu) {
        return;
    }

    g_hover_menu = document.createElement("div");
    g_hover_menu.setAttribute("id", "hover_menu");
    document.body.appendChild(g_hover_menu);
}

<<<<<<< HEAD
export function update_content(code)
{
=======
export function update_content(code) {
>>>>>>> upstream/master
    if (!g_hover_menu) {
        return;
    }

    g_hover_menu.innerHTML = code;
    utils.execute_javascript_by_object(g_hover_menu);
}

<<<<<<< HEAD
export function update_position(event)
{
=======
export function update_position(event) {
>>>>>>> upstream/master
    if (!g_hover_menu) {
        return;
    }

    var hoverSpacer = 5;

    // document.body.scrollTop does not work in IE
<<<<<<< HEAD
    var scrollTop = document.body.scrollTop ? document.body.scrollTop :
        document.documentElement.scrollTop;
    var scrollLeft = document.body.scrollLeft ? document.body.scrollLeft :
        document.documentElement.scrollLeft;
=======
    var scrollTop = document.body.scrollTop
        ? document.body.scrollTop
        : document.documentElement.scrollTop;
    var scrollLeft = document.body.scrollLeft
        ? document.body.scrollLeft
        : document.documentElement.scrollLeft;
>>>>>>> upstream/master

    var x = event.clientX;
    var y = event.clientY;

    // hide the menu first to avoid an "up-then-over" visual effect
    g_hover_menu.style.display = "block";
<<<<<<< HEAD
    g_hover_menu.style.left = (x + hoverSpacer + scrollLeft) + "px";
    g_hover_menu.style.top = (y + hoverSpacer + scrollTop) + "px";
=======
    g_hover_menu.style.left = x + hoverSpacer + scrollLeft + "px";
    g_hover_menu.style.top = y + hoverSpacer + scrollTop + "px";
>>>>>>> upstream/master

    /**
     * Check if the menu is "in screen" or too large.
     * If there is some need for reposition try to reposition the hover menu
     */

    var hoverPosAndSizeOk = true;
    if (!is_on_screen(g_hover_menu, hoverSpacer)) {
        hoverPosAndSizeOk = false;
    }

    if (!hoverPosAndSizeOk) {
<<<<<<< HEAD
        g_hover_menu.style.left = (x - hoverSpacer - g_hover_menu.clientWidth) + "px";
=======
        g_hover_menu.style.left = x - hoverSpacer - g_hover_menu.clientWidth + "px";
>>>>>>> upstream/master

        if (is_on_screen(g_hover_menu, hoverSpacer)) {
            hoverPosAndSizeOk = true;
        }
    }

    // And if the hover menu is still not on the screen move it to the left edge
    // and fill the whole screen width
    if (!is_on_screen(g_hover_menu, hoverSpacer)) {
        g_hover_menu.style.left = hoverSpacer + scrollLeft + "px";
<<<<<<< HEAD
        g_hover_menu.style.width = utils.page_width() - (2*hoverSpacer) + "px";
=======
        g_hover_menu.style.width = utils.page_width() - 2 * hoverSpacer + "px";
>>>>>>> upstream/master
    }

    var hoverTop = parseInt(g_hover_menu.style.top.replace("px", ""));
    // Only move the menu to the top when the new top will not be
    // out of sight
<<<<<<< HEAD
    if (hoverTop +g_hover_menu.clientHeight > utils.page_height() && hoverTop -g_hover_menu.clientHeight >= 0) {
        g_hover_menu.style.top = hoverTop -g_hover_menu.clientHeight - hoverSpacer + "px";
    }
}

function is_on_screen(hoverMenu, hoverSpacer)
{
    var hoverLeft = parseInt(hoverMenu.style.left.replace("px", ""));
    var scrollLeft = document.body.scrollLeft ? document.body.scrollLeft :
        document.documentElement.scrollLeft;
=======
    if (
        hoverTop + g_hover_menu.clientHeight > utils.page_height() &&
        hoverTop - g_hover_menu.clientHeight >= 0
    ) {
        g_hover_menu.style.top = hoverTop - g_hover_menu.clientHeight - hoverSpacer + "px";
    }
}

function is_on_screen(hoverMenu, hoverSpacer) {
    var hoverLeft = parseInt(hoverMenu.style.left.replace("px", ""));
    var scrollLeft = document.body.scrollLeft
        ? document.body.scrollLeft
        : document.documentElement.scrollLeft;
>>>>>>> upstream/master

    if (hoverLeft + hoverMenu.clientWidth >= utils.page_width() - scrollLeft) {
        return false;
    }

    if (hoverLeft - hoverSpacer < 0) {
        return false;
    }

    return true;
}
