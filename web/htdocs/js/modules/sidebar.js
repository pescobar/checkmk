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
import * as quicksearch from "quicksearch";

<<<<<<< HEAD
var g_content_loc   = null;
var g_sidebar_folded = false;

export function register_event_handlers() {
    window.addEventListener("mousemove", function(e) {
        snapinDrag(e);
        dragScroll(e);
        return false;
    }, false);
    window.addEventListener("mousedown", startDragScroll, false);
    window.addEventListener("mouseup", stopDragScroll,  false);
    window.addEventListener("wheel", scrollWheel, false);
=======
var g_content_loc = null;
var g_scrollbar = null;

export function initialize_sidebar(update_interval, refresh, restart, static_) {
    if (restart) {
        sidebar_restart_time = Math.floor(Date.parse(new Date()) / 1000);
    }

    sidebar_update_interval = update_interval;

    register_edge_listeners();

    refresh_snapins = refresh;
    restart_snapins = restart;
    static_snapins = static_;

    execute_sidebar_scheduler();

    g_scrollbar = utils.add_simplebar_scrollbar("side_content");
    g_scrollbar.getScrollElement().addEventListener(
        "scroll",
        function () {
            store_scroll_position();
            return false;
        },
        false
    );
    register_event_handlers();
    if (is_content_frame_accessible()) {
        update_content_location();
    }
}

export function register_event_handlers() {
    window.addEventListener(
        "mousemove",
        function (e) {
            snapinDrag(e);
            return false;
        },
        false
    );
>>>>>>> upstream/master
}

// This ends drag scrolling when moving the mouse out of the sidebar
// frame while performing a drag scroll.
// This is no 100% solution. When moving the mouse out of browser window
// without moving the mouse over the edge elements the dragging is not ended.
export function register_edge_listeners(obj) {
<<<<<<< HEAD
    var edges;
    if (!obj)
        edges = [ parent.frames[1], document.getElementById("side_header"), document.getElementById("side_footer") ];
    else
        edges = [ obj ];

    for(var i = 0; i < edges.length; i++) {
        // It is possible to open other domains in the content frame - don't register
        // the event in that case. It is not permitted by most browsers!
        if(!is_content_frame_accessible())
            continue;

        if (window.addEventListener)
            edges[i].addEventListener("mousemove", on_mouse_leave, false);
        else
            edges[i].onmousemove = on_mouse_leave;
    }
}

function on_mouse_leave(e) {
    if (typeof(quicksearch.close_popup) != "undefined")
        quicksearch.close_popup();
=======
    // It is possible to open other domains in the content frame - don't register
    // the event in that case. It is not permitted by most browsers!
    if (!is_content_frame_accessible()) return;

    const edge = obj ? obj : parent.frames[0];
    if (window.addEventListener) edge.addEventListener("mousemove", on_mouse_leave, false);
    else edge.onmousemove = on_mouse_leave;
}

function on_mouse_leave(e) {
    if (typeof quicksearch.close_popup != "undefined") quicksearch.close_popup();
>>>>>>> upstream/master
    return stop_snapin_dragging(e);
}

function stop_snapin_dragging(e) {
<<<<<<< HEAD
    stopDragScroll(e);
=======
>>>>>>> upstream/master
    snapinTerminateDrag(e);
    return false;
}

/************************************************
 * snapin drag/drop code
 *************************************************/

<<<<<<< HEAD
var snapinDragging = false;
var snapinOffset   = [ 0, 0 ];
var snapinStartPos = [ 0, 0 ];
var snapinScrollTop = 0;

export function snapin_start_drag(event) {
    if (!event)
        event = window.event;

    var target = utils.get_target(event);
    var button = utils.get_button(event);

    // Skip calls when already dragging or other button than left mouse
    if (snapinDragging !== false || button != "LEFT" || target.tagName != "DIV")
        return true;

    event.cancelBubble = true;

    snapinDragging = target.parentNode;

    // Save relative offset of the mouse to the snapin title to prevent flipping on drag start
    snapinOffset   = [ event.clientY - target.parentNode.offsetTop,
        event.clientX - target.parentNode.offsetLeft ];
    snapinStartPos = [ event.clientY, event.clientX ];
    snapinScrollTop = document.getElementById("side_content").scrollTop;
=======
var g_snapin_dragging = false;
var g_snapin_offset = [0, 0];
var g_snapin_start_pos = [0, 0];
var g_snapin_scroll_top = 0;

export function snapin_start_drag(event) {
    if (!event) event = window.event;

    const target = utils.get_target(event);
    const button = utils.get_button(event);

    // Skip calls when already dragging or other button than left mouse
    if (g_snapin_dragging !== false || button != "LEFT" || target.tagName != "DIV") return true;

    event.cancelBubble = true;

    g_snapin_dragging = target.parentNode;

    // Save relative offset of the mouse to the snapin title to prevent flipping on drag start
    g_snapin_offset = [
        event.clientY - target.parentNode.offsetTop,
        event.clientX - target.parentNode.offsetLeft,
    ];
    g_snapin_start_pos = [event.clientY, event.clientX];
    g_snapin_scroll_top = document.getElementById("side_content").scrollTop;
>>>>>>> upstream/master

    // Disable the default events for all the different browsers
    return utils.prevent_default_events(event);
}

function snapinDrag(event) {
<<<<<<< HEAD
    if (!event)
        event = window.event;

    if (snapinDragging === false)
        return true;
=======
    if (!event) event = window.event;

    if (g_snapin_dragging === false) return true;
>>>>>>> upstream/master

    // Is the mouse placed of the title bar of the snapin?
    // It can move e.g. if the scroll wheel is wheeled during dragging...

    // Drag the snapin
<<<<<<< HEAD
    snapinDragging.style.position = "absolute";
    var newTop = event.clientY  - snapinOffset[0] - snapinScrollTop;
    newTop += document.getElementById("side_content").scrollTop;
    snapinDragging.style.top      = newTop + "px";
    snapinDragging.style.left     = (event.clientX - snapinOffset[1]) + "px";
    snapinDragging.style.zIndex   = 200;
=======
    utils.add_class(g_snapin_dragging, "dragging");
    let newTop = event.clientY - g_snapin_offset[0] - g_snapin_scroll_top;
    newTop += document.getElementById("side_content").scrollTop;
    g_snapin_dragging.style.top = newTop + "px";
    g_snapin_dragging.style.left = event.clientX - g_snapin_offset[1] + "px";
>>>>>>> upstream/master

    // Refresh the drop marker
    removeSnapinDragIndicator();

<<<<<<< HEAD
    var line = document.createElement("div");
    line.setAttribute("id", "snapinDragIndicator");
    var o = getSnapinTargetPos();
    if (o != null) {
        snapinAddBefore(o.parentNode, o, line);
    } else {
        snapinAddBefore(snapinDragging.parentNode, null, line);
=======
    const line = document.createElement("div");
    line.setAttribute("id", "snapinDragIndicator");
    const o = getSnapinTargetPos();
    if (o != null) {
        snapinAddBefore(o.parentNode, o, line);
    } else {
        snapinAddBefore(g_snapin_dragging.parentNode, null, line);
>>>>>>> upstream/master
    }
    return true;
}

function snapinAddBefore(par, o, add) {
    if (o != null) {
        par.insertBefore(add, o);
    } else {
<<<<<<< HEAD
        par.appendChild(add);
=======
        par.insertBefore(add, document.getElementById("add_snapin"));
>>>>>>> upstream/master
    }
}

function removeSnapinDragIndicator() {
<<<<<<< HEAD
    var o = document.getElementById("snapinDragIndicator");
=======
    const o = document.getElementById("snapinDragIndicator");
>>>>>>> upstream/master
    if (o) {
        o.parentNode.removeChild(o);
    }
}

function snapinDrop(event, targetpos) {
<<<<<<< HEAD
    if (snapinDragging == false)
        return true;

    // Reset properties
    snapinDragging.style.top      = "";
    snapinDragging.style.left     = "";
    snapinDragging.style.position = "";

    // Catch quick clicks without movement on the title bar
    // Don't reposition the object in this case.
    if (snapinStartPos[0] == event.clientY && snapinStartPos[1] == event.clientX) {
        return utils.prevent_default_events(event);
    }

    var par = snapinDragging.parentNode;
    par.removeChild(snapinDragging);
    snapinAddBefore(par, targetpos, snapinDragging);

    // Now send the new information to the backend
    var thisId = snapinDragging.id.replace("snapin_container_", "");

    var before = "";
    if (targetpos != null)
        before = "&before=" + targetpos.id.replace("snapin_container_", "");
=======
    if (g_snapin_dragging === false) return true;

    // Reset properties
    utils.remove_class(g_snapin_dragging, "dragging");
    g_snapin_dragging.style.top = "";
    g_snapin_dragging.style.left = "";

    // Catch quick clicks without movement on the title bar
    // Don't reposition the object in this case.
    if (g_snapin_start_pos[0] == event.clientY && g_snapin_start_pos[1] == event.clientX) {
        return utils.prevent_default_events(event);
    }

    const par = g_snapin_dragging.parentNode;
    par.removeChild(g_snapin_dragging);
    snapinAddBefore(par, targetpos, g_snapin_dragging);

    // Now send the new information to the backend
    const thisId = g_snapin_dragging.id.replace("snapin_container_", "");

    let before = "";
    if (targetpos != null) before = "&before=" + targetpos.id.replace("snapin_container_", "");
>>>>>>> upstream/master
    ajax.get_url("sidebar_move_snapin.py?name=" + thisId + before);
}

function snapinTerminateDrag() {
<<<<<<< HEAD
    if (snapinDragging == false)
        return true;
    removeSnapinDragIndicator();
    // Reset properties
    snapinDragging.style.top      = "";
    snapinDragging.style.left     = "";
    snapinDragging.style.position = "";
    snapinDragging = false;
}

export function snapin_stop_drag(event) {
    if (!event)
        event = window.event;

    removeSnapinDragIndicator();
    snapinDrop(event, getSnapinTargetPos());
    snapinDragging = false;
}

function getDivChildNodes(node) {
    var children = [];
    var childNodes = node.childNodes;
    for (var i = 0; i < childNodes.length; i++)
        if(childNodes[i].tagName === "DIV")
            children.push(childNodes[i]);
=======
    if (g_snapin_dragging == false) return true;
    removeSnapinDragIndicator();
    // Reset properties
    utils.remove_class(g_snapin_dragging, "dragging");
    g_snapin_dragging.style.top = "";
    g_snapin_dragging.style.left = "";
    g_snapin_dragging = false;
}

export function snapin_stop_drag(event) {
    if (!g_snapin_dragging) return;

    if (!event) event = window.event;

    removeSnapinDragIndicator();
    snapinDrop(event, getSnapinTargetPos());
    g_snapin_dragging = false;
}

function getDivChildNodes(node) {
    const children = [];
    for (const child of node.childNodes) {
        if (child.tagName === "DIV") {
            children.push(child);
        }
    }
>>>>>>> upstream/master
    return children;
}

function getSnapinList() {
<<<<<<< HEAD
    if (snapinDragging === false)
        return true;

    var l = [];
    var childs = getDivChildNodes(snapinDragging.parentNode);
    for(var i = 0; i < childs.length; i++) {
        var child = childs[i];
        // Skip
        // - non snapin objects
        // - currently dragged object
        if (child.id && child.id.substr(0, 7) == "snapin_" && child.id != snapinDragging.id)
            l.push(child);
    }

=======
    const l = [];
    for (const child of getDivChildNodes(g_snapin_dragging.parentNode)) {
        // Skip non snapin objects and the currently dragged object
        if (child.id && child.id.substr(0, 7) == "snapin_" && child.id != g_snapin_dragging.id) {
            l.push(child);
        }
    }
>>>>>>> upstream/master
    return l;
}

function getSnapinCoords(obj) {
<<<<<<< HEAD
    var snapinTop = snapinDragging.offsetTop;
    // + document.getElementById("side_content").scrollTop;

    var bottomOffset = obj.offsetTop + obj.clientHeight - snapinTop;
    if (bottomOffset < 0)
        bottomOffset = -bottomOffset;

    var topOffset = obj.offsetTop - snapinTop;
    if (topOffset < 0)
        topOffset = -topOffset;

    var offset = topOffset;
    var corner = 0;
=======
    const snapinTop = g_snapin_dragging.offsetTop;
    // + document.getElementById("side_content").scrollTop;

    let bottomOffset = obj.offsetTop + obj.clientHeight - snapinTop;
    if (bottomOffset < 0) bottomOffset = -bottomOffset;

    let topOffset = obj.offsetTop - snapinTop;
    if (topOffset < 0) topOffset = -topOffset;

    let offset = topOffset;
    let corner = 0;
>>>>>>> upstream/master
    if (bottomOffset < topOffset) {
        offset = bottomOffset;
        corner = 1;
    }

<<<<<<< HEAD
    return [ bottomOffset, topOffset, offset, corner ];
}

function getSnapinTargetPos() {
    var childs = getSnapinList();
    var objId = -1;
    var objCorner = -1;

    // Find the nearest snapin to current left/top corner of
    // the currently dragged snapin
    for(var i = 0; i < childs.length; i++) {
        var child = childs[i];

        if (!child.id || child.id.substr(0, 7) != "snapin_" || child.id == snapinDragging.id)
            continue;
=======
    return [bottomOffset, topOffset, offset, corner];
}

function getSnapinTargetPos() {
    const childs = getSnapinList();
    let objId = -1;
    let objCorner = -1;

    // Find the nearest snapin to current left/top corner of
    // the currently dragged snapin
    for (let i = 0; i < childs.length; i++) {
        const child = childs[i];
>>>>>>> upstream/master

        // Initialize with the first snapin in the list
        if (objId === -1) {
            objId = i;
<<<<<<< HEAD
            var coords = getSnapinCoords(child);
=======
            const coords = getSnapinCoords(child);
>>>>>>> upstream/master
            objCorner = coords[3];
            continue;
        }

        // First check which corner is closer. Upper left or
        // the bottom left.
<<<<<<< HEAD
        var curCoords = getSnapinCoords(childs[objId]);
        var newCoords = getSnapinCoords(child);
=======
        const curCoords = getSnapinCoords(childs[objId]);
        const newCoords = getSnapinCoords(child);
>>>>>>> upstream/master

        // Is the upper left corner closer?
        if (newCoords[2] < curCoords[2]) {
            objCorner = newCoords[3];
            objId = i;
        }
    }

    // Is the dragged snapin dragged above the first one?
<<<<<<< HEAD
    if (objId == 0 && objCorner == 0)
        return childs[0];
    else
        return childs[(parseInt(objId)+1)];
=======
    return objId === 0 && objCorner === 0 ? childs[0] : childs[objId + 1];
>>>>>>> upstream/master
}

/************************************************
 * misc sidebar stuff
 *************************************************/

// Checks if the sidebar can access the content frame. It might be denied
// by the browser since it blocks cross domain access.
export function is_content_frame_accessible() {
    try {
<<<<<<< HEAD
        parent.frames[1].document;
=======
        parent.frames[0].document;
>>>>>>> upstream/master
        return true;
    } catch (e) {
        return false;
    }
}

export function update_content_location() {
<<<<<<< HEAD
    // init the original frameset title
    if (typeof(window.parent.orig_title) == "undefined") {
        window.parent.orig_title = window.parent.document.title;
    }

    var content_frame = window.parent.frames[1];

    // Change the title to add the right frame title to reflect the
    // title of the content URL in the framesets title (window title or tab title)
    var page_title;
=======
    // initialize the original title
    if (typeof window.parent.orig_title == "undefined") {
        window.parent.orig_title = window.parent.document.title;
    }

    const content_frame = parent.frames[0];

    // Change the title to add the frame title to reflect the
    // title of the content URL title (window title or tab title)
    let page_title;
>>>>>>> upstream/master
    if (content_frame.document.title != "") {
        page_title = window.parent.orig_title + " - " + content_frame.document.title;
    } else {
        page_title = window.parent.orig_title;
    }
    window.parent.document.title = page_title;

    // Construct the URL to be called on page reload
<<<<<<< HEAD
    var parts = window.parent.location.pathname.split("/");
    parts.pop();
    var cmk_path = parts.join("/");
    var rel_url = content_frame.location.pathname + content_frame.location.search + content_frame.location.hash;
    var index_url = cmk_path + "/index.py?start_url=" + encodeURIComponent(rel_url);

    if (window.parent.history.replaceState) {
        if (rel_url && rel_url != "blank") {
            // Update the URL to be called on reload, e.g. via F5, to make the
            // frameset switch to exactly this URL
=======
    const parts = window.parent.location.pathname.split("/");
    parts.pop();
    const cmk_path = parts.join("/");
    const rel_url =
        content_frame.location.pathname +
        content_frame.location.search +
        content_frame.location.hash;
    const index_url = cmk_path + "/index.py?start_url=" + encodeURIComponent(rel_url);

    if (window.parent.history.replaceState) {
        if (rel_url && rel_url != "blank") {
            // Update the URL to be called on reload, e.g. via F5, to switch to exactly this URL
>>>>>>> upstream/master
            window.parent.history.replaceState({}, page_title, index_url);

            // only update the internal flag var if the url was not blank and has been updated
            //otherwise try again on next scheduler run
<<<<<<< HEAD
            g_content_loc = parent.frames[1].document.location.href;
=======
            g_content_loc = content_frame.document.location.href;
>>>>>>> upstream/master
        }
    } else {
        // Only a browser without history.replaceState support reaches this. Sadly
        // we have no F5/reload fix for them...
<<<<<<< HEAD
        g_content_loc = parent.frames[1].document.location.href;
    }
}

// Set the size of the sidebar_content div to fit the whole screen
// but without scrolling. The height of the header and footer divs need
// to be treated here.
export function set_sidebar_size() {
    var oHeader  = document.getElementById("side_header");
    var oContent = document.getElementById("side_content");
    var oFooter  = document.getElementById("side_footer");
    var height   = utils.page_height();

    // Don't handle zero heights
    if (height == 0)
        return;

    // -2 -> take outer border of oHeader and oFooter into account
    oContent.style.height = (height - oHeader.clientHeight - oFooter.clientHeight - 2) + "px";
}

var scrolling = true;

export function scroll_window(speed){
    var c = document.getElementById("side_content");

    if (scrolling) {
        c.scrollTop += speed;
        setTimeout("cmk.sidebar.scroll_window("+speed+")", 10);
    }
}

/************************************************
 * drag/drop scrollen
 *************************************************/

var dragging = false;
var startY = 0;

function startDragScroll(event) {
    if (!event)
        event = window.event;

    var target = utils.get_target(event);
    var button = utils.get_button(event);

    if (button != "LEFT")
        return true; // only care about left clicks!

    if (g_sidebar_folded) {
        unfold_sidebar();
        return utils.prevent_default_events(event);
    }
    else if (!g_sidebar_folded && event.clientX < 10 && target.tagName != "OPTION") {
        // When clicking on an <option> of the "core performance" snapins, an event
        // with event.clientX equal 0 is triggered, don"t know why. Filter out clicks
        // on OPTION tags.
        fold_sidebar();
        return utils.prevent_default_events(event);
    }

    if (dragging === false
        && target.tagName != "A"
        && target.tagName != "INPUT"
        && target.tagName != "SELECT"
        && target.tagName != "OPTION"
        && !(target.tagName == "DIV" && target.className == "heading")) {

        dragging = event;
        startY = event.clientY;

        return utils.prevent_default_events(event);
    }

    return true;
}

function stopDragScroll(){
    dragging = false;
}

function dragScroll(event) {
    if (!event)
        event = window.event;

    if (dragging === false)
        return true;

    event.cancelBubble = true;

    var inhalt = document.getElementById("side_content");
    var diff = startY - event.clientY;

    inhalt.scrollTop += diff;

    // Opera does not fire onunload event which is used to store the scroll
    // position. So call the store function manually here.
    if (utils.browser.is_opera())
        store_scroll_position();

    startY = event.clientY;

    dragging = event;
    return utils.prevent_default_events(event);
}

function sidebar_width()
{
    if (g_sidebar_folded)
        return 10;
    else
        return 280;
}

export function fold_sidebar()
{
    g_sidebar_folded = true;
    document.getElementById("check_mk_sidebar").style.position = "relative";
    document.getElementById("check_mk_sidebar").style.left = "-265px";
    document.getElementById("side_footer").style.display = "none";
    var version = document.getElementById("side_version");
    if (version)
        version.style.display = "none";
    parent.document.body.cols = sidebar_width() + ",*";
    ajax.get_url("sidebar_fold.py?fold=yes");
}


function unfold_sidebar()
{
    g_sidebar_folded = false;
    document.getElementById("check_mk_sidebar").style.position = "";
    document.getElementById("check_mk_sidebar").style.left = "0";
    document.getElementById("side_footer").style.display = "";
    var version = document.getElementById("side_version");
    if (version)
        version.style.display = "";
    parent.document.body.cols = sidebar_width() + ",*";
    ajax.get_url("sidebar_fold.py?fold=");
}



/************************************************
 * Mausrad scrollen
 *************************************************/

function handle_scroll(delta) {
    scrolling = true;
    scroll_window(-delta*20);
    scrolling = false;
}

/** Event handler for mouse wheel event.
 */
function scrollWheel(event){
    // TODO: It's not reliable to detect the scrolling direction with wheel events:
    // https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent
    handle_scroll(event.deltaY < 0 ? 1: -1);

    // Opera does not fire onunload event which is used to store the scroll
    // position. So call the store function manually here.
    if (utils.browser.is_opera())
        store_scroll_position();
}


=======
        g_content_loc = content_frame.document.location.href;
    }
}

var g_scrolling = true;

export function scroll_window(speed) {
    const c = document.getElementById("side_content");

    if (g_scrolling) {
        c.scrollTop += speed;
        setTimeout("cmk.sidebar.scroll_window(" + speed + ")", 10);
    }
}

export function toggle_sidebar() {
    const sidebar = document.getElementById("check_mk_sidebar");
    if (utils.has_class(sidebar, "folded")) unfold_sidebar();
    else fold_sidebar();
}

export function fold_sidebar() {
    const sidebar = document.getElementById("check_mk_sidebar");
    utils.add_class(sidebar, "folded");
    const button = document.getElementById("side_fold");
    utils.add_class(button, "folded");

    ajax.get_url("sidebar_fold.py?fold=yes");
}

function unfold_sidebar() {
    const sidebar = document.getElementById("check_mk_sidebar");
    utils.remove_class(sidebar, "folded");
    const button = document.getElementById("side_fold");
    utils.remove_class(button, "folded");

    ajax.get_url("sidebar_fold.py?fold=");
}

>>>>>>> upstream/master
//
// Sidebar ajax stuff
//

// The refresh snapins do reload after a defined amount of time
var refresh_snapins = null;
// The restart snapins are notified about the restart of the nagios instance(s)
var restart_snapins = null;
<<<<<<< HEAD
=======
// Snapins that only have to be reloaded on demand
var static_snapins = null;
>>>>>>> upstream/master
// Contains a timestamp which holds the time of the last nagios restart handling
var sidebar_restart_time = null;
// Configures the number of seconds to reload all snapins which request it
var sidebar_update_interval = null;

<<<<<<< HEAD
export function set_restart_snapins(snapins) {
    restart_snapins = snapins;
}

export function set_refresh_snapins(snapins) {
    refresh_snapins = snapins;
}

export function set_sidebar_update_interval(interval) {
    sidebar_update_interval = interval;
}

export function set_sidebar_restart_time(t) {
    sidebar_restart_time = t;
}

// Removes the snapin from the current sidebar and informs the server for persistance
export function remove_sidebar_snapin(oLink, url)
{
    var container = oLink.parentNode.parentNode.parentNode;
    var id = container.id.replace("snapin_container_", "");

    ajax.call_ajax(url, {
        handler_data     : "snapin_" + id,
        response_handler : function (id) {
            remove_snapin(id);
        },
        method           : "GET"
    });
}


// Removes a snapin from the sidebar without reloading anything
function remove_snapin(id)
{
    var container = document.getElementById(id).parentNode;
    var myparent = container.parentNode;
    myparent.removeChild(container);

    // remove this snapin from the refresh list, if it is contained
    for (var i in refresh_snapins) {
        var name    = refresh_snapins[i][0];
        if (id == "snapin_" + name) {
            refresh_snapins.splice(i, 1);
            break;
        }
    }

    // reload main frame if it is currently displaying the "add snapin" page
    if (parent.frames[1]) {
        var href = encodeURIComponent(parent.frames[1].location);
        if (href.indexOf("sidebar_add_snapin.py") > -1)
            parent.frames[1].location.reload();
    }
}


export function toggle_sidebar_snapin(oH2, url) {
    // oH2 can also be an <a>. In that case it is the minimize
    // image itself

    var childs;
    if (oH2.tagName == "A")
        childs = oH2.parentNode.parentNode.parentNode.childNodes;
    else
        childs = oH2.parentNode.parentNode.childNodes;
    for (var i in childs) {
        var child = childs[i];
        if (child.tagName == "DIV" && child.className == "content")
            var oContent = child;
        else if (child.tagName == "DIV" && (child.className == "head open" || child.className == "head closed"))
            var oHead = child;
    }

    // FIXME: Does oContent really exist?
    var closed = oContent.style.display == "none";
    if (closed) {
        oContent.style.display = "block";
        utils.change_class(oHead, "closed", "open");
    }
    else {
=======
export function add_snapin(name) {
    ajax.call_ajax("sidebar_ajax_add_snapin.py?name=" + name, {
        response_handler: function (_data, response) {
            const data = JSON.parse(response);
            if (data.result_code !== 0) {
                return;
            }

            const result = data.result;

            if (result.refresh) {
                const entry = [result.name, result.url];
                if (refresh_snapins.indexOf(entry) === -1) {
                    refresh_snapins.push(entry);
                }
            }

            if (result.restart) {
                const entry = result.name;
                if (restart_snapins.indexOf(entry) === -1) {
                    restart_snapins.push(entry);
                }
            }

            if (!result.refresh && !result.restart) {
                const entry = result.name;
                if (static_snapins.indexOf(entry) === -1) {
                    static_snapins.push(entry);
                }
            }

            const sidebar_content = g_scrollbar.getContentElement();
            if (sidebar_content) {
                var tmp = document.createElement("div");
                tmp.innerHTML = result.content;
                utils.execute_javascript_by_object(tmp);

                const add_button = sidebar_content.lastChild;
                while (tmp.childNodes.length) {
                    add_button.insertAdjacentElement("beforebegin", tmp.childNodes[0]);
                }
            }

            const add_snapin_page = window.frames[0] ? window.frames[0].document : document;
            const preview = add_snapin_page.getElementById("snapin_container_" + name);
            if (preview) {
                const container = preview.parentElement.parentElement;
                container.remove();
            }
        },
    });
}

// Removes the snapin from the current sidebar and informs the server for persistance
export function remove_sidebar_snapin(oLink, url) {
    const container = oLink.parentNode.parentNode.parentNode.parentNode;
    const id = container.id.replace("snapin_container_", "");

    ajax.call_ajax(url, {
        handler_data: "snapin_" + id,
        response_handler: function (id) {
            remove_snapin(id);
        },
        method: "GET",
    });
}

// Removes a snapin from the sidebar without reloading anything
function remove_snapin(id) {
    const container = document.getElementById(id).parentNode;
    const myparent = container.parentNode;
    myparent.removeChild(container);

    const name = id.replace("snapin_", "");

    const refresh_index = refresh_snapins.indexOf(name);
    if (refresh_index !== -1) {
        refresh_snapins.splice(refresh_index, 1);
    }

    const restart_index = restart_snapins.indexOf(name);
    if (restart_index !== -1) {
        restart_snapins.splice(refresh_index, 1);
    }

    const static_index = static_snapins.indexOf(name);
    if (static_index !== -1) {
        static_snapins.splice(static_index, 1);
    }

    // reload main frame if it is currently displaying the "add snapin" page
    if (parent.frames[0]) {
        const href = encodeURIComponent(parent.frames[0].location);
        if (href.indexOf("sidebar_add_snapin.py") > -1) parent.frames[0].location.reload();
    }
}

export function toggle_sidebar_snapin(oH2, url) {
    // oH2 is a <b> if it is the snapin title otherwise it is the minimize button.
    let childs =
        oH2.tagName == "B"
            ? oH2.parentNode.parentNode.childNodes
            : oH2.parentNode.parentNode.parentNode.childNodes;

    let oContent, oHead;
    for (const i in childs) {
        const child = childs[i];
        if (child.tagName == "DIV" && child.className == "content") oContent = child;
        else if (
            child.tagName == "DIV" &&
            (child.className == "head open" || child.className == "head closed")
        )
            oHead = child;
    }

    // FIXME: Does oContent really exist?
    const closed = oContent.style.display == "none";
    if (closed) {
        oContent.style.display = "block";
        utils.change_class(oHead, "closed", "open");
    } else {
>>>>>>> upstream/master
        oContent.style.display = "none";
        utils.change_class(oHead, "open", "closed");
    }
    /* make this persistent -> save */
    ajax.get_url(url + (closed ? "open" : "closed"));
}

function reload_main_plus_sidebar() {
<<<<<<< HEAD
    parent.frames[1].location.reload(); /* reload main frame */
    parent.frames[0].location.reload(); /* reload side bar */
=======
    window.top.location.reload();
>>>>>>> upstream/master
}

// TODO move to managed/web/htdocs/js
export function switch_customer(customer_id, switch_state) {
<<<<<<< HEAD
    ajax.get_url("switch_customer.py?_customer_switch=" + customer_id + ":" + switch_state,
        reload_main_plus_sidebar, null);
=======
    ajax.get_url(
        "switch_customer.py?_customer_switch=" + customer_id + ":" + switch_state,
        reload_main_plus_sidebar,
        null
    );
>>>>>>> upstream/master
}

export function switch_site(url) {
    ajax.get_url(url, reload_main_plus_sidebar, null);
}

<<<<<<< HEAD
function bulk_update_contents(ids, codes)
{
    codes = eval(codes);
    for (var i = 0, len = ids.length; i < len; i++) {
=======
function bulk_update_contents(ids, codes) {
    codes = eval(codes);
    for (let i = 0; i < ids.length; i++) {
>>>>>>> upstream/master
        if (restart_snapins.indexOf(ids[i].replace("snapin_", "")) !== -1) {
            // Snapins which rely on the restart time of nagios receive
            // an empty code here when nagios has not been restarted
            // since sidebar rendering or last update, skip it
<<<<<<< HEAD
            if(codes[i] != "") {
=======
            if (codes[i] !== "") {
>>>>>>> upstream/master
                utils.update_contents(ids[i], codes[i]);
                sidebar_restart_time = Math.floor(Date.parse(new Date()) / 1000);
            }
        } else {
            utils.update_contents(ids[i], codes[i]);
        }
    }
}

<<<<<<< HEAD

var g_seconds_to_update = null;

export function refresh_single_snapin(name) {
    var url = "sidebar_snapin.py?names=" + name;
    var ids = [ "snapin_" + name ];
    ajax.get_url(url, bulk_update_contents, ids);
}

export function execute_sidebar_scheduler() {
    if (g_seconds_to_update == null)
        g_seconds_to_update = sidebar_update_interval;
    else
        g_seconds_to_update -= 1;
=======
var g_seconds_to_update = null;
var g_sidebar_scheduler_timer = null;
var g_sidebar_full_reload = false;

export function refresh_single_snapin(name) {
    const url = "sidebar_snapin.py?names=" + name;
    const ids = ["snapin_" + name];
    ajax.get_url(url, bulk_update_contents, ids);
}

export function reset_sidebar_scheduler() {
    if (g_sidebar_scheduler_timer !== null) {
        clearTimeout(g_sidebar_scheduler_timer);
        g_sidebar_scheduler_timer = null;
    }
    g_seconds_to_update = 1;
    g_sidebar_full_reload = true;
    execute_sidebar_scheduler();
}

export function execute_sidebar_scheduler() {
    g_seconds_to_update =
        g_seconds_to_update !== null ? g_seconds_to_update - 1 : sidebar_update_interval;
>>>>>>> upstream/master

    // Stop reload of the snapins in case the browser window / tab is not visible
    // for the user. Retry after short time.
    if (!utils.is_window_active()) {
<<<<<<< HEAD
        setTimeout(function(){ execute_sidebar_scheduler(); }, 250);
        return;
    }

    var to_be_updated = [];

    var i, url;
    for (i = 0; i < refresh_snapins.length; i++) {
        var name = refresh_snapins[i][0];
        if (refresh_snapins[i][1] != "") {
=======
        g_sidebar_scheduler_timer = setTimeout(function () {
            execute_sidebar_scheduler();
        }, 250);
        return;
    }

    const to_be_updated = [];

    let url;
    for (let i = 0; i < refresh_snapins.length; i++) {
        const name = refresh_snapins[i][0];
        if (refresh_snapins[i][1] !== "") {
>>>>>>> upstream/master
            // Special handling for snapins like the nagvis maps snapin which request
            // to be updated from a special URL, use direct update of those snapins
            // from this url
            url = refresh_snapins[i][1];

            if (g_seconds_to_update <= 0) {
                ajax.get_url(url, utils.update_contents, "snapin_" + name);
            }
        } else {
            // Internal update handling, use bulk update
            to_be_updated.push(name);
        }
    }

<<<<<<< HEAD
    // Are there any snapins to be bulk updates?
    if(to_be_updated.length > 0) {
        if (g_seconds_to_update <= 0) {
            url = "sidebar_snapin.py?names=" + to_be_updated.join(",");
            if (sidebar_restart_time !== null)
                url += "&since=" + sidebar_restart_time;

            var ids = [], len = to_be_updated.length;
            for (i = 0; i < len; i++) {
                ids.push("snapin_" + to_be_updated[i]);
            }

            ajax.get_url(url, bulk_update_contents, ids);
        }
    }

    if (g_sidebar_notify_interval !== null) {
        var timestamp = Date.parse(new Date()) / 1000;
=======
    if (g_sidebar_full_reload) {
        g_sidebar_full_reload = false;
        for (const name of static_snapins) {
            to_be_updated.push(name);
        }
    }

    // Are there any snapins to be bulk updated?
    if (to_be_updated.length > 0 && g_seconds_to_update <= 0) {
        url = "sidebar_snapin.py?names=" + to_be_updated.join(",");
        if (sidebar_restart_time !== null) url += "&since=" + sidebar_restart_time;

        const ids = [],
            len = to_be_updated.length;
        for (let i = 0; i < len; i++) {
            ids.push("snapin_" + to_be_updated[i]);
        }

        ajax.get_url(url, bulk_update_contents, ids);
    }

    if (g_sidebar_notify_interval !== null) {
        const timestamp = Date.parse(new Date()) / 1000;
>>>>>>> upstream/master
        if (timestamp % g_sidebar_notify_interval == 0) {
            update_messages();
        }
    }

    // Detect page changes and re-register the mousemove event handler
    // in the content frame. another bad hack ... narf
<<<<<<< HEAD
    if(is_content_frame_accessible() && g_content_loc != parent.frames[1].document.location.href) {
        register_edge_listeners(parent.frames[1]);
        update_content_location();
    }

    if (g_seconds_to_update <= 0)
        g_seconds_to_update = sidebar_update_interval;

    setTimeout(function(){execute_sidebar_scheduler();}, 1000);
=======
    if (is_content_frame_accessible() && g_content_loc != parent.frames[0].document.location.href) {
        register_edge_listeners(parent.frames[0]);
        update_content_location();
    }

    if (g_seconds_to_update <= 0) g_seconds_to_update = sidebar_update_interval;

    g_sidebar_scheduler_timer = setTimeout(function () {
        execute_sidebar_scheduler();
    }, 1000);
>>>>>>> upstream/master
}

/************************************************
 * Save/Restore scroll position
 *************************************************/

<<<<<<< HEAD
function setCookie(cookieName, value,expiredays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + expiredays);
    document.cookie = cookieName + "=" + encodeURIComponent(value) +
        ((expiredays == null) ? "" : ";expires=" + exdate.toUTCString());
}

function getCookie(cookieName) {
    if(document.cookie.length == 0)
        return null;

    var cookieStart = document.cookie.indexOf(cookieName + "=");
    if(cookieStart == -1)
        return null;

    cookieStart = cookieStart + cookieName.length + 1;
    var cookieEnd = document.cookie.indexOf(";", cookieStart);
    if(cookieEnd == -1)
        cookieEnd = document.cookie.length;
=======
function setCookie(cookieName, value, expiredays) {
    const exdate = new Date();
    exdate.setDate(exdate.getDate() + expiredays);
    document.cookie =
        cookieName +
        "=" +
        encodeURIComponent(value) +
        (expiredays == null ? "" : ";expires=" + exdate.toUTCString() + ";SameSite=Lax");
}

function getCookie(cookieName) {
    if (document.cookie.length == 0) return null;

    let cookieStart = document.cookie.indexOf(cookieName + "=");
    if (cookieStart == -1) return null;

    cookieStart = cookieStart + cookieName.length + 1;
    let cookieEnd = document.cookie.indexOf(";", cookieStart);
    if (cookieEnd == -1) cookieEnd = document.cookie.length;
>>>>>>> upstream/master
    return decodeURIComponent(document.cookie.substring(cookieStart, cookieEnd));
}

export function initialize_scroll_position() {
<<<<<<< HEAD
    var scrollPos = getCookie("sidebarScrollPos");
    if(!scrollPos)
        scrollPos = 0;
    document.getElementById("side_content").scrollTop = scrollPos;
}

export function store_scroll_position() {
    setCookie("sidebarScrollPos", document.getElementById("side_content").scrollTop, null);
=======
    let scrollPos = getCookie("sidebarScrollPos");
    if (!scrollPos) scrollPos = 0;
    g_scrollbar.getScrollElement().scrollTop = scrollPos;
}

function store_scroll_position() {
    setCookie("sidebarScrollPos", g_scrollbar.getScrollElement().scrollTop, null);
>>>>>>> upstream/master
}

/************************************************
 * WATO Folders snapin handling
 *************************************************/

// FIXME: Make this somehow configurable - use the start url?
<<<<<<< HEAD
var g_last_view   = "dashboard.py?name=main";
=======
var g_last_view = "dashboard.py?name=main";
>>>>>>> upstream/master
var g_last_folder = "";

// highlight the followed link (when both needed snapins are available)
function highlight_link(link_obj, container_id) {
<<<<<<< HEAD
    var this_snapin = document.getElementById(container_id);
    var other_snapin;
    if (container_id == "snapin_container_wato_folders")
        other_snapin = document.getElementById("snapin_container_views");
    else
        other_snapin = document.getElementById("snapin_container_wato_folders");

    if (this_snapin && other_snapin) {
        var links;
        if (this_snapin.getElementsByClassName)
            links = this_snapin.getElementsByClassName("link");
        else
            links = document.getElementsByClassName("link", this_snapin);

        for (var i = 0; i < links.length; i++) {
=======
    const this_snapin = document.getElementById(container_id);
    let other_snapin;
    if (container_id == "snapin_container_wato_folders")
        other_snapin = document.getElementById("snapin_container_views");
    else other_snapin = document.getElementById("snapin_container_wato_folders");

    if (this_snapin && other_snapin) {
        let links;
        if (this_snapin.getElementsByClassName) links = this_snapin.getElementsByClassName("link");
        else links = document.getElementsByClassName("link", this_snapin);

        for (let i = 0; i < links.length; i++) {
>>>>>>> upstream/master
            links[i].style.fontWeight = "normal";
        }

        link_obj.style.fontWeight = "bold";
    }
}

export function wato_folders_clicked(link_obj, folderpath) {
    g_last_folder = folderpath;
    highlight_link(link_obj, "snapin_container_wato_folders");
<<<<<<< HEAD
    parent.frames[1].location = g_last_view + "&wato_folder=" + encodeURIComponent(g_last_folder);
=======
    parent.frames[0].location = g_last_view + "&wato_folder=" + encodeURIComponent(g_last_folder);
>>>>>>> upstream/master
}

export function wato_views_clicked(link_obj) {
    g_last_view = link_obj.href;

    highlight_link(link_obj, "snapin_container_views");
    highlight_link(link_obj, "snapin_container_dashboards");

    if (g_last_folder != "") {
        // Navigate by using javascript, cancel following the default link
<<<<<<< HEAD
        parent.frames[1].location = g_last_view + "&wato_folder=" + encodeURIComponent(g_last_folder);
=======
        parent.frames[0].location =
            g_last_view + "&wato_folder=" + encodeURIComponent(g_last_folder);
>>>>>>> upstream/master
        return false;
    } else {
        // Makes use the url stated in href attribute
        return true;
    }
}

/************************************************
 * WATO Foldertree (Standalone) snapin handling
 *************************************************/

/* Foldable Tree in snapin */
export function wato_tree_click(link_obj, folderpath) {
<<<<<<< HEAD
    var topic  = document.getElementById("topic").value;
    var target = document.getElementById("target_" + topic).value;

    var href;
    if(target.substr(0, 9) == "dashboard") {
        var dashboard_name = target.substr(10, target.length);
=======
    const topic = document.getElementById("topic").value;
    const target = document.getElementById("target_" + topic).value;

    let href;
    if (target.substr(0, 9) == "dashboard") {
        const dashboard_name = target.substr(10, target.length);
>>>>>>> upstream/master
        href = "dashboard.py?name=" + encodeURIComponent(dashboard_name);
    } else {
        href = "view.py?view_name=" + encodeURIComponent(target);
    }

    href += "&wato_folder=" + encodeURIComponent(folderpath);

<<<<<<< HEAD
    parent.frames[1].location = href;
=======
    parent.frames[0].location = href;
>>>>>>> upstream/master
}

export function wato_tree_topic_changed(topic_field) {
    // First toggle the topic dropdown field
<<<<<<< HEAD
    var topic = topic_field.value;

    // Hide all select fields but the wanted one
    var select_fields = document.getElementsByTagName("select");
    for(var i = 0; i < select_fields.length; i++) {
        if(select_fields[i].id && select_fields[i].id.substr(0, 7) == "target_") {
            select_fields[i].selected = "";
            if(select_fields[i].id == "target_" + topic) {
=======
    const topic = topic_field.value;

    // Hide all select fields but the wanted one
    const select_fields = document.getElementsByTagName("select");
    for (let i = 0; i < select_fields.length; i++) {
        if (select_fields[i].id && select_fields[i].id.substr(0, 7) == "target_") {
            select_fields[i].selected = "";
            if (select_fields[i].id == "target_" + topic) {
>>>>>>> upstream/master
                select_fields[i].style.display = "inline";
            } else {
                select_fields[i].style.display = "none";
            }
        }
    }

    // Then send the info to python code via ajax call for persistance
    ajax.get_url("ajax_set_foldertree.py?topic=" + encodeURIComponent(topic) + "&target=");
}

export function wato_tree_target_changed(target_field) {
<<<<<<< HEAD
    var topic = target_field.id.substr(7, target_field.id.length);
    var target = target_field.value;

    // Send the info to python code via ajax call for persistance
    ajax.get_url("ajax_set_foldertree.py?topic=" + encodeURIComponent(topic) + "&target=" + encodeURIComponent(target));
=======
    const topic = target_field.id.substr(7, target_field.id.length);
    const target = target_field.value;

    // Send the info to python code via ajax call for persistance
    ajax.get_url(
        "ajax_set_foldertree.py?topic=" +
            encodeURIComponent(topic) +
            "&target=" +
            encodeURIComponent(target)
    );
>>>>>>> upstream/master
}

/************************************************
 * Event console site selection
 *************************************************/

export function set_snapin_site(event, ident, select_field) {
<<<<<<< HEAD
    if (!event)
        event = window.event;

    ajax.get_url("sidebar_ajax_set_snapin_site.py?ident=" + encodeURIComponent(ident)
          + "&site=" + encodeURIComponent(select_field.value));
    location.reload();
=======
    if (!event) event = window.event;

    ajax.get_url(
        "sidebar_ajax_set_snapin_site.py?ident=" +
            encodeURIComponent(ident) +
            "&site=" +
            encodeURIComponent(select_field.value),
        function (handler_data, response_body) {
            refresh_single_snapin(ident);
        }
    );
>>>>>>> upstream/master
    return utils.prevent_default_events(event);
}

/************************************************
 * Render the nagvis snapin contents
 *************************************************/

export function fetch_nagvis_snapin_contents() {
<<<<<<< HEAD
    // Needs to be fetched via JS from NagVis because it needs to
    // be done in the user context.
    var nagvis_url = "../nagvis/server/core/ajax_handler.php?mod=Multisite&act=getMaps";
=======
    var nagvis_snapin_update_interval = 30;

    // Stop reload of the snapin content in case the browser window / tab is
    // not visible for the user. Retry after short time.
    if (!utils.is_window_active()) {
        setTimeout(function () {
            fetch_nagvis_snapin_contents();
        }, 250);
        return;
    }

    // Needs to be fetched via JS from NagVis because it needs to
    // be done in the user context.
    const nagvis_url = "../nagvis/server/core/ajax_handler.php?mod=Multisite&act=getMaps";
>>>>>>> upstream/master
    ajax.call_ajax(nagvis_url, {
        add_ajax_id: false,
        response_handler: function (_unused_handler_data, ajax_response) {
            // Then hand over the data to the python code which is responsible
            // to render the data.
            ajax.call_ajax("ajax_nagvis_maps_snapin.py", {
                method: "POST",
                add_ajax_id: false,
                post_data: "request=" + encodeURIComponent(ajax_response),
                response_handler: function (_unused_handler_data, snapin_content_response) {
                    utils.update_contents("snapin_nagvis_maps", snapin_content_response);
                },
            });
<<<<<<< HEAD
        },
        error_handler: function (_unused, status_code) {
            var msg = document.createElement("div");
            msg.classList.add("message", "error");
            msg.innerHTML = "Failed to update NagVis maps: " + status_code;
            utils.update_contents("snapin_nagvis_maps", msg.outerHTML);
        },
        method: "GET"
    });
}

=======

            setTimeout(function () {
                fetch_nagvis_snapin_contents();
            }, nagvis_snapin_update_interval * 1000);
        },
        error_handler: function (_unused, status_code) {
            const msg = document.createElement("div");
            msg.classList.add("message", "error");
            msg.innerHTML = "Failed to update NagVis maps: " + status_code;
            utils.update_contents("snapin_nagvis_maps", msg.outerHTML);

            setTimeout(function () {
                fetch_nagvis_snapin_contents();
            }, nagvis_snapin_update_interval * 1000);
        },
        method: "GET",
    });
}

/************************************************
 * Bookmark snapin
 *************************************************/

export function add_bookmark() {
    const url = parent.frames[0].location;
    const title = parent.frames[0].document.title;
    ajax.get_url(
        "add_bookmark.py?title=" + encodeURIComponent(title) + "&url=" + encodeURIComponent(url),
        utils.update_contents,
        "snapin_bookmarks"
    );
}

/************************************************
 * Wiki search snapin
 *************************************************/

export function wiki_search(omd_site) {
    const oInput = document.getElementById("wiki_search_field");
    top.frames["main"].location.href =
        "/" + encodeURIComponent(omd_site) + "/wiki/doku.php?do=search&id=" + escape(oInput.value);
    utils.prevent_default_events();
}

/************************************************
 * Wiki search snapin
 *************************************************/

var g_needle_timeout = null;

export function speedometer_show_speed(last_perc, program_start, scheduled_rate) {
    const url =
        "sidebar_ajax_speedometer.py" +
        "?last_perc=" +
        last_perc +
        "&scheduled_rate=" +
        scheduled_rate +
        "&program_start=" +
        program_start;

    ajax.call_ajax(url, {
        response_handler: function (handler_data, response_body) {
            let data;
            try {
                data = JSON.parse(response_body);

                let oDiv = document.getElementById("speedometer");

                // Terminate reschedule when the speedometer div does not exist anymore
                // (e.g. the snapin has been removed)
                if (!oDiv) return;

                oDiv.title = data.title;
                oDiv = document.getElementById("speedometerbg");
                oDiv.title = data.title;

                move_needle(data.last_perc, data.percentage); // 50 * 100ms = 5s = refresh time
            } catch (ie) {
                // Ignore errors during re-rendering. Proceed with reschedule...
                data = handler_data;
            }

            setTimeout(
                (function (data) {
                    return function () {
                        speedometer_show_speed(
                            data.percentage,
                            data.program_start,
                            data.scheduled_rate
                        );
                    };
                })(data),
                5000
            );
        },
        error_handler: function (handler_data, status_code, error_msg) {
            setTimeout(
                (function (data) {
                    return function () {
                        return speedometer_show_speed(
                            data.percentage,
                            data.program_start,
                            data.scheduled_rate
                        );
                    };
                })(handler_data),
                5000
            );
        },
        method: "GET",
        handler_data: {
            percentage: last_perc,
            last_perc: last_perc,
            program_start: program_start,
            scheduled_rate: scheduled_rate,
        },
    });
}

function show_speed(percentage) {
    const canvas = document.getElementById("speedometer");
    if (!canvas) return;

    const context = canvas.getContext("2d");
    if (!context) return;

    if (percentage > 100.0) percentage = 100.0;

    const orig_x = 116;
    const orig_y = 181;
    const angle_0 = 232.0;
    const angle_100 = 307.0;
    const angle = angle_0 + ((angle_100 - angle_0) * percentage) / 100.0;
    const angle_rad = (angle / 360.0) * Math.PI * 2;
    const length = 120;
    const end_x = orig_x + Math.cos(angle_rad) * length;
    const end_y = orig_y + Math.sin(angle_rad) * length;

    context.clearRect(0, 0, 228, 136);
    context.beginPath();
    context.moveTo(orig_x, orig_y);
    context.lineTo(end_x, end_y);
    context.closePath();
    context.shadowOffsetX = 2;
    context.shadowOffsetY = 2;
    context.shadowBlur = 2;
    context.strokeStyle = "#000000";
    context.stroke();
}

function move_needle(from_perc, to_perc) {
    const new_perc = from_perc * 0.9 + to_perc * 0.1;

    show_speed(new_perc);

    if (g_needle_timeout != null) clearTimeout(g_needle_timeout);

    g_needle_timeout = setTimeout(
        (function (new_perc, to_perc) {
            return function () {
                move_needle(new_perc, to_perc);
            };
        })(new_perc, to_perc),
        50
    );
}

>>>>>>> upstream/master
/************************************************
 * Popup Message Handling
 *************************************************/

// integer representing interval in seconds or <null> when disabled.
var g_sidebar_notify_interval;

export function init_messages(interval) {
    g_sidebar_notify_interval = interval;

    // Are there pending messages? Render the initial state of
    // trigger button
    update_message_trigger();
}

function handle_update_messages(_unused, code) {
    // add new messages to container
<<<<<<< HEAD
    var c = document.getElementById("messages");
=======
    const c = document.getElementById("messages");
>>>>>>> upstream/master
    if (c) {
        c.innerHTML = code;
        utils.execute_javascript_by_object(c);
        update_message_trigger();
    }
}

function update_messages() {
    // Remove all pending messages from container
<<<<<<< HEAD
    var c = document.getElementById("messages");
=======
    const c = document.getElementById("messages");
>>>>>>> upstream/master
    if (c) {
        c.innerHTML = "";
    }

    // retrieve new messages
    ajax.get_url("sidebar_get_messages.py", handle_update_messages);
}

function get_hint_messages(c) {
<<<<<<< HEAD
    var hints;
    if (c.getElementsByClassName)
        hints = c.getElementsByClassName("popup_msg");
    else
        hints = document.getElementsByClassName("popup_msg", c);
=======
    let hints;
    if (c.getElementsByClassName) hints = c.getElementsByClassName("popup_msg");
    else hints = document.getElementsByClassName("popup_msg", c);
>>>>>>> upstream/master
    return hints;
}

function update_message_trigger() {
<<<<<<< HEAD
    var c = document.getElementById("messages");
    if (c) {
        var b = document.getElementById("msg_button");
        var hints = get_hint_messages(c);
=======
    const c = document.getElementById("messages");
    if (c) {
        const b = document.getElementById("msg_button");
        const hints = get_hint_messages(c);
>>>>>>> upstream/master
        if (hints.length > 0) {
            // are there pending messages? make trigger visible
            b.style.display = "inline";

            // Create/Update a blinking number label
<<<<<<< HEAD
            var l = document.getElementById("msg_label");
=======
            let l = document.getElementById("msg_label");
>>>>>>> upstream/master
            if (!l) {
                l = document.createElement("span");
                l.setAttribute("id", "msg_label");
                b.appendChild(l);
            }

            l.innerHTML = "" + hints.length;
        } else {
            // no messages: hide the trigger
            b.style.display = "none";
        }
    }
}

export function mark_message_read(msg_id) {
    ajax.get_url("sidebar_message_read.py?id=" + msg_id);

    // Update the button state
    update_message_trigger();
}

export function read_message() {
<<<<<<< HEAD
    var c = document.getElementById("messages");
    if (!c)
        return;

    // extract message from the message container
    var hints = get_hint_messages(c);
    var msg = hints[0];
=======
    const c = document.getElementById("messages");
    if (!c) return;

    // extract message from the message container
    const hints = get_hint_messages(c);
    const msg = hints[0];
>>>>>>> upstream/master
    c.removeChild(msg);

    // open the next message in a window
    c.parentNode.appendChild(msg);

    // tell server that the message has been read
<<<<<<< HEAD
    var msg_id = msg.id.replace("message-", "");
=======
    const msg_id = msg.id.replace("message-", "");
>>>>>>> upstream/master
    mark_message_read(msg_id);
}

export function message_close(msg_id) {
<<<<<<< HEAD
    var m = document.getElementById("message-" + msg_id);
=======
    const m = document.getElementById("message-" + msg_id);
>>>>>>> upstream/master
    if (m) {
        m.parentNode.removeChild(m);
    }
}
<<<<<<< HEAD
=======

/************************************************
 * user menu callbacks
 *************************************************/

// for quick access options in user menu

export function toggle_user_attribute(mode) {
    ajax.call_ajax(mode, {
        method: "POST",
        response_handler: function (handler_data, ajax_response) {
            const data = JSON.parse(ajax_response);
            if (data.result_code == 0) {
                window.location.reload();
            }
        },
    });
}
>>>>>>> upstream/master
