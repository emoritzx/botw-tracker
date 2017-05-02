/**
 * Form utilities
 * 
 * Copyright (c) 2017, Evan Moritz.
 * 
 * botw-tracker is an open source software project released under the MIT License.
 * See the accompanying LICENSE file for terms.
 */
define(['jquery'], function($) {

    'use strict';

    /**
     * Create and submit a dynamic form
     * 
     * Adapted from user submission on http://stackoverflow.com/a/13937065
     * 
     * @param {string} action Target url
     * @param {string} method HTTP method type
     * @param {object} input Object containing key: value pairs of data
     */
    function submit(action, method, input) {
        var form = $('<form />', {
            action: action,
            method: method,
            style: 'display: none;'
        });
        if (typeof input !== 'undefined' && input !== null) {
            $.each(input, function (name, value) {
                $('<input />', {
                    type: 'hidden',
                    name: name,
                    value: value
                }).appendTo(form);
            });
        }
        form.appendTo('body').submit();
    }

    // define module
    var module = new Object();
    Object.defineProperties(module, {
        submit: {
            get: function() {
                return submit;
            }
        }
    });
    return module;
});