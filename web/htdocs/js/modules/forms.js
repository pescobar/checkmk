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

import $ from "jquery";
import "select2";
import Tagify from "@yaireo/tagify";
<<<<<<< HEAD
=======
import "element-closest-polyfill";
import Swal from "sweetalert2";
>>>>>>> upstream/master

import * as utils from "utils";
import * as ajax from "ajax";

<<<<<<< HEAD
export function enable_dynamic_form_elements(container=null) {
=======
export function enable_dynamic_form_elements(container = null) {
>>>>>>> upstream/master
    enable_select2_dropdowns(container);
    enable_label_input_fields(container);
}

// html.dropdown() adds the .select2-enable class for all dropdowns
// that should use the select2 powered dropdowns
export function enable_select2_dropdowns(container) {
    let elements;
<<<<<<< HEAD
    if (!container)
        container = $(document);

    elements = $(container).find(".select2-enable").not(".vlof_prototype .select2-enable");
    elements.select2({
        dropdownAutoWidth : true,
        minimumResultsForSearch: 5
=======
    if (!container) container = $(document);

    elements = $(container).find(".select2-enable").not(".vlof_prototype .select2-enable");
    elements.select2({
        dropdownAutoWidth: true,
        minimumResultsForSearch: 5,
>>>>>>> upstream/master
    });
}

function enable_label_input_fields(container) {
<<<<<<< HEAD
    if (!container)
        container = document;
=======
    if (!container) container = document;
>>>>>>> upstream/master

    let elements = container.querySelectorAll("input.labels");
    elements.forEach(element => {
        // Do not tagify objects that are part of a ListOf valuespec template
        if (element.closest(".vlof_prototype") !== null) {
            return;
        }

        let max_labels = element.getAttribute("data-max-labels");
        let world = element.getAttribute("data-world");

        let ajax_obj;
        let tagify_args = {
            pattern: /^[^:]+:[^:]+$/,
        };

        if (max_labels !== null) {
            tagify_args["maxTags"] = max_labels;
        }

        let tagify = new Tagify(element, tagify_args);

<<<<<<< HEAD
        tagify.on("invalid", function(e) {
=======
        tagify.on("invalid", function (e) {
>>>>>>> upstream/master
            let message;
            if (e.type == "invalid" && e.detail.message == "number of tags exceeded") {
                message = "Only one tag allowed";
            } else {
<<<<<<< HEAD
                message = "Labels need to be in the format <tt>[KEY]:[VALUE]</tt>. For example <tt>os:windows</tt>.</div>";
=======
                message =
                    "Labels need to be in the format <tt>[KEY]:[VALUE]</tt>. For example <tt>os:windows</tt>.</div>";
>>>>>>> upstream/master
            }

            $("div.label_error").remove(); // Remove all previous errors

            // Print a validation error message
            var msg = document.createElement("div");
            msg.classList.add("message", "error", "label_error");

            msg.innerHTML = message;
            element.parentNode.insertBefore(msg, element.nextSibling);
        });

<<<<<<< HEAD
        tagify.on("add", function() {
=======
        tagify.on("add", function () {
>>>>>>> upstream/master
            $("div.label_error").remove(); // Remove all previous errors
        });

        // Realize the auto completion dropdown field by using an ajax call
<<<<<<< HEAD
        tagify.on("input", function(e) {
=======
        tagify.on("input", function (e) {
>>>>>>> upstream/master
            $("div.label_error").remove(); // Remove all previous errors

            var value = e.detail;
            tagify.settings.whitelist.length = 0; // reset the whitelist

<<<<<<< HEAD
            var post_data = "request=" + encodeURIComponent(JSON.stringify({
                "search_label": value,
                "world": world,
            }));

            if (ajax_obj)
                ajax_obj.abort();
=======
            var post_data =
                "request=" +
                encodeURIComponent(
                    JSON.stringify({
                        search_label: value,
                        world: world,
                    })
                );

            if (ajax_obj) ajax_obj.abort();
>>>>>>> upstream/master

            ajax_obj = ajax.call_ajax("ajax_autocomplete_labels.py", {
                method: "POST",
                post_data: post_data,
<<<<<<< HEAD
                response_handler: function(handler_data, ajax_response) {
=======
                response_handler: function (handler_data, ajax_response) {
>>>>>>> upstream/master
                    var response = JSON.parse(ajax_response);
                    if (response.result_code != 0) {
                        console.log("Error [" + response.result_code + "]: " + response.result); // eslint-disable-line
                        return;
                    }

                    handler_data.tagify.settings.whitelist = response.result;
                    handler_data.tagify.dropdown.show.call(handler_data.tagify, handler_data.value);
                },
                handler_data: {
                    value: value,
                    tagify: tagify,
                },
            });
        });
    });
}

// Handle Enter key in textfields
export function textinput_enter_submit(e, submit) {
<<<<<<< HEAD
    if (!e)
        e = window.event;
=======
    if (!e) e = window.event;
>>>>>>> upstream/master

    var keyCode = e.which || e.keyCode;
    if (keyCode == 13) {
        if (submit) {
            var button = document.getElementById(submit);
<<<<<<< HEAD
            if (button)
                button.click();
=======
            if (button) button.click();
>>>>>>> upstream/master
        }
        return utils.prevent_default_events(e);
    }
}

<<<<<<< HEAD
=======
// Helper function to display nice popup confirm dialogs
// TODO: This needs to be styled to match the current user theme
export function confirm_dialog(optional_args, confirm_handler) {
    let args = utils.merge_args(
        {
            icon: "question",
            showCancelButton: true,
            confirmButtonColor: "#444",
            cancelButtonColor: "#444",
            confirmButtonText: "Yes",
            cancelButtonText: "No",
        },
        optional_args
    );

    Swal.fire(args).then(result => {
        if (result.value) {
            confirm_handler();
        }
    });
}

// Makes a form submittable after explicit confirmation
export function add_confirm_on_submit(form_id, message) {
    utils.add_event_handler(
        "submit",
        e => {
            confirm_dialog({html: message}, () => {
                document.getElementById(form_id).submit();
            });
            return utils.prevent_default_events(e);
        },
        document.getElementById(form_id)
    );
}

// Used as onclick handler on links to confirm following the link or not
export function confirm_link(url, message) {
    confirm_dialog({html: message}, () => {
        location.href = url;
    });
}
>>>>>>> upstream/master
