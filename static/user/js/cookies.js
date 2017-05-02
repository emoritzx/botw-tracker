/**
 * Cookie utilities
 * 
 * Copyright (c) 2017, Evan Moritz.
 * 
 * botw-tracker is an open source software project released under the MIT License.
 * See the accompanying LICENSE file for terms.
 */
define(['jquery'], function($) {

    'use strict';

    /**
     * Cookie accessor
     * 
     * Adapted from example code on https://docs.djangoproject.com/en/1.11/ref/csrf/#ajax
     * 
     * @param {string} name Name of cookie
     * @returns {string} Value of cookie
     */
    function get(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // define module
    var module = new Object();
    Object.defineProperties(module, {
        get: {
            get: function() {
                return get;
            }
        }
    });
    return module;
});