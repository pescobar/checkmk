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

var width;
var height;
var netto_width;
var netto_height;
var from_time;
var until_time;
var v_min;
var v_max;
var canvas_id;

<<<<<<< HEAD
var left_border   = 90;
var right_border  = 50;
var top_border    = 40;
var bottom_border = 50;

export function create_graph(cid, ft, ut, vmi, vma)
{
=======
var left_border = 90;
var right_border = 50;
var top_border = 40;
var bottom_border = 50;

export function create_graph(cid, ft, ut, vmi, vma) {
>>>>>>> upstream/master
    // Keep important data as global variables, needed by
    // render_curve()
    canvas_id = cid;
    var canvas = document.getElementById(canvas_id);
    from_time = ft;
    until_time = ut;
    v_min = vmi;
    v_max = vma;

    width = canvas.width;
    height = canvas.height;
    netto_width = width - left_border - right_border;
    netto_height = height - top_border - bottom_border;
}

<<<<<<< HEAD
function arrow_up(c, cx, cy, length, size, color)
{
=======
function arrow_up(c, cx, cy, length, size, color) {
>>>>>>> upstream/master
    c.strokeStyle = color;
    c.moveTo(cx, cy);
    c.lineTo(cx, cy - length);
    c.stroke();

    c.fillColor = color;
<<<<<<< HEAD
    c.moveTo(cx - size/2, cy - length);
    c.lineTo(cx + size/2, cy - length);
=======
    c.moveTo(cx - size / 2, cy - length);
    c.lineTo(cx + size / 2, cy - length);
>>>>>>> upstream/master
    c.lineTo(cx, cy - size - length);
    c.fill();
}

<<<<<<< HEAD
function arrow_right(c, cx, cy, length, size, color)
{
    c.strokeStyle = color;
    c.moveTo(cx, cy);
    c.lineTo(cx+length, cy);
    c.stroke();

    c.fillColor = color;
    c.moveTo(cx+length, cy - size/2);
    c.lineTo(cx+length, cy + size/2);
    c.lineTo(cx+length + size, cy);
    c.fill();
}


=======
function arrow_right(c, cx, cy, length, size, color) {
    c.strokeStyle = color;
    c.moveTo(cx, cy);
    c.lineTo(cx + length, cy);
    c.stroke();

    c.fillColor = color;
    c.moveTo(cx + length, cy - size / 2);
    c.lineTo(cx + length, cy + size / 2);
    c.lineTo(cx + length + size, cy);
    c.fill();
}

>>>>>>> upstream/master
var linea = "#888888";
var lineb = "#bbbbbb";
var linec = "#bbbbbb";

<<<<<<< HEAD

export function render_coordinates(v_scala, t_scala)
{
=======
export function render_coordinates(v_scala, t_scala) {
>>>>>>> upstream/master
    // Create canvas
    var canvas = document.getElementById(canvas_id);
    var c = canvas.getContext("2d");
    c.font = "20px sans-serif";

    // Convert the coordinate system in a way, that we can directly
    // work with our native time and value.
    // x_scale = 1.0 * width / (until_time - from_time);
    // y_scale = 1.0 * -height / (v_max - v_min);
    // c.scale(x_scale, y_scale);
    // c.translate(-from_time, -v_max);

    var t;
    c.strokeStyle = linec;
    c.lineWidth = 0.5;
<<<<<<< HEAD
    for (t = from_time; t <= until_time ; t += 1800) {
        if ((t % 7200) == 0)
            c.strokeStyle = linea;
        else if ((t % 3600) == 0)
            c.strokeStyle = lineb;
        else
            c.strokeStyle = linec;
=======
    for (t = from_time; t <= until_time; t += 1800) {
        if (t % 7200 == 0) c.strokeStyle = linea;
        else if (t % 3600 == 0) c.strokeStyle = lineb;
        else c.strokeStyle = linec;
>>>>>>> upstream/master
        line(c, t, v_min, t, v_max);
    }

    c.strokeStyle = lineb;
    c.lineWidth = 1;
<<<<<<< HEAD
    for (t = from_time; t <= until_time ; t += 7200) {
=======
    for (t = from_time; t <= until_time; t += 7200) {
>>>>>>> upstream/master
        line(c, t, v_min, t, v_max);
    }

    var i;
<<<<<<< HEAD
    c.fillStyle="#000000";

    // Value scala (vertical)
    var val, txt, p, w;
    for (i=0; i<v_scala.length; i++) {
=======
    c.fillStyle = "#000000";

    // Value scala (vertical)
    var val, txt, p, w;
    for (i = 0; i < v_scala.length; i++) {
>>>>>>> upstream/master
        val = v_scala[i][0];
        txt = v_scala[i][1];
        p = point(0, val);
        w = c.measureText(txt).width;
        c.fillText(txt, left_border - w - 16, p[1] + 6);
<<<<<<< HEAD
        if (i%2)
            c.strokeStyle = lineb;
        else
            c.strokeStyle = linea;
=======
        if (i % 2) c.strokeStyle = lineb;
        else c.strokeStyle = linea;
>>>>>>> upstream/master
        line(c, from_time, val, until_time, val);
    }

    // Time scala (horizontal)
<<<<<<< HEAD
    for (i=0; i<t_scala.length; i++) {
=======
    for (i = 0; i < t_scala.length; i++) {
>>>>>>> upstream/master
        t = t_scala[i][0];
        txt = t_scala[i][1];
        p = point(t, 0);
        w = c.measureText(txt).width;
<<<<<<< HEAD
        c.fillText(txt, p[0] - (w/2), height - bottom_border + 28);
        if (i%2)
            c.strokeStyle = lineb;
        else
            c.strokeStyle = linea;
=======
        c.fillText(txt, p[0] - w / 2, height - bottom_border + 28);
        if (i % 2) c.strokeStyle = lineb;
        else c.strokeStyle = linea;
>>>>>>> upstream/master
    }

    // Paint outlines and arrows
    c.strokeStyle = "#000000";
    line(c, from_time, 0, until_time, 0);
    line(c, from_time, v_min, from_time, v_max);
    line(c, from_time, v_min, until_time, v_min);
    arrow_up(c, left_border, top_border, 1, 8, "#000000");
    arrow_right(c, width - right_border, height - bottom_border, 8, 8, "#000000");
}

<<<<<<< HEAD
function point(t, v)
{
    return [ left_border + (t - from_time) / (until_time - from_time) * netto_width,
        height - bottom_border - ((v - v_min) / (v_max - v_min) * netto_height) ];
}

function line(c, t0, v0, t1, v1)
{
=======
function point(t, v) {
    return [
        left_border + ((t - from_time) / (until_time - from_time)) * netto_width,
        height - bottom_border - ((v - v_min) / (v_max - v_min)) * netto_height,
    ];
}

function line(c, t0, v0, t1, v1) {
>>>>>>> upstream/master
    var p0 = point(t0, v0);
    var p1 = point(t1, v1);
    c.beginPath();
    c.moveTo(p0[0], p0[1]);
    c.lineTo(p1[0], p1[1]);
    c.stroke();
}

<<<<<<< HEAD
export function render_point(t, v, color)
{
=======
export function render_point(t, v, color) {
>>>>>>> upstream/master
    var canvas = document.getElementById(canvas_id);
    var c = canvas.getContext("2d");
    var p = point(t, v);
    c.beginPath();
    c.lineWidth = 4;
    c.strokeStyle = color;
<<<<<<< HEAD
    c.moveTo(p[0]-6, p[1]-6);
    c.lineTo(p[0]+6, p[1]+6);
    c.moveTo(p[0]+6, p[1]-6);
    c.lineTo(p[0]-6, p[1]+6);
    c.stroke();
}


export function render_curve(points, color, w, square)
{
=======
    c.moveTo(p[0] - 6, p[1] - 6);
    c.lineTo(p[0] + 6, p[1] + 6);
    c.moveTo(p[0] + 6, p[1] - 6);
    c.lineTo(p[0] - 6, p[1] + 6);
    c.stroke();
}

export function render_curve(points, color, w, square) {
>>>>>>> upstream/master
    var canvas = document.getElementById(canvas_id);
    var c = canvas.getContext("2d");

    c.beginPath();
    c.strokeStyle = color;
    c.lineWidth = w;

    var op;
    var time_step = (until_time - from_time) / points.length;
    var first = true;
<<<<<<< HEAD
    for (var i=0; i<points.length; i++) {
=======
    for (var i = 0; i < points.length; i++) {
>>>>>>> upstream/master
        if (points[i] == null) {
            c.stroke();
            first = true;
            continue;
        }
        var p = point(from_time + time_step * i, points[i]);
        if (first) {
            c.moveTo(p[0], p[1]);
            first = false;
<<<<<<< HEAD
        }
        else {
            if (square)
                c.lineTo(p[0], op[1]);
=======
        } else {
            if (square) c.lineTo(p[0], op[1]);
>>>>>>> upstream/master
            c.lineTo(p[0], p[1]);
        }
        op = p;
    }
    c.stroke();
}

<<<<<<< HEAD
export function render_area(points, color, alpha)
{
    render_dual_area(null, points, color, alpha);
}

export function render_area_reverse(points, color, alpha)
{
    render_dual_area(points, null, color, alpha);
}

export function render_dual_area(lower_points, upper_points, color, alpha)
{
=======
export function render_area(points, color, alpha) {
    render_dual_area(null, points, color, alpha);
}

export function render_area_reverse(points, color, alpha) {
    render_dual_area(points, null, color, alpha);
}

export function render_dual_area(lower_points, upper_points, color, alpha) {
>>>>>>> upstream/master
    var canvas = document.getElementById(canvas_id);
    var c = canvas.getContext("2d");

    c.fillStyle = color;
    c.globalAlpha = alpha;
    var num_points;
<<<<<<< HEAD
    if (lower_points)
        num_points = lower_points.length;
    else
        num_points = upper_points.length;

    var time_step = 1.0 * (until_time - from_time) / num_points;
    var pix_step = 1.0 * netto_width / num_points;

    var x, yl, yu, h;
    for (var i=0; i<num_points; i++) {
        x = point(from_time + time_step * i, 0)[0];
        if (lower_points)
            yl = point(0, lower_points[i])[1];
        else
            yl = height - bottom_border;

        if (upper_points)
            yu = point(0, upper_points[i])[1];
        else
            yu = top_border;
=======
    if (lower_points) num_points = lower_points.length;
    else num_points = upper_points.length;

    var time_step = (1.0 * (until_time - from_time)) / num_points;
    var pix_step = (1.0 * netto_width) / num_points;

    var x, yl, yu, h;
    for (var i = 0; i < num_points; i++) {
        x = point(from_time + time_step * i, 0)[0];
        if (lower_points) yl = point(0, lower_points[i])[1];
        else yl = height - bottom_border;

        if (upper_points) yu = point(0, upper_points[i])[1];
        else yu = top_border;
>>>>>>> upstream/master
        h = yu - yl;
        c.fillRect(x, yl, pix_step, h);
    }
    c.globalAlpha = 1;
}
