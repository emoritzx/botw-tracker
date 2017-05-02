/**
 * botw-tracker user profile scripts
 *
 * Copyright (c) 2017, Evan Moritz.
 * 
 * botw-tracker is an open source software project released under the MIT License.
 * See the accompanying LICENSE file for terms.
 */

// setup
requirejs.config({
    paths: {
        "jquery": "/static/lib/jquery-3.2.1.min"
    }
});

// begin application
requirejs(['jquery', 'cookies', 'forms'], function($, Cookies, Forms) {

    // listen to hash change event
    var ATTRIBUTE = 'data-quests-active';
    var hashchangeEvent = $(window).on('hashchange', function() {
        var hash = location.hash.substr(1);
        $('[' + ATTRIBUTE + ']').each(function(index, container) {
            $(container).attr(ATTRIBUTE, 'False');
        });
        $("#" + hash).attr(ATTRIBUTE, 'True');
    });

    // on page load
    $(document).ready(function() {
        // add AJAX requests to quest links
        $("[data-botw-action]").each(function(index, el) {
            $(el).click(function() {
                var action = $(el).attr('data-botw-action');
                if (action !== "remove" || confirm("Are you sure you want to remove this quest?")) {
                    Forms.submit(el.href, "POST", {
                        csrfmiddlewaretoken: Cookies.get('csrftoken'),
                        action: action,
                        id: $(el).attr('data-botw-id')
                    });
                }
                return false;
            });
        });
        // add dynamic view changes to quest types
        $(".quests-undiscovered-dropdown").each(function(index, el) {
            var quest_type = $(el).attr('data-quest-type');
            $(el).click(function() {
                var block = $(".quests-undiscovered[data-quest-type=" + quest_type + "]");
                if (block.css("display") === "block") {
                    $(el).text("+");
                    block.css("display", "none");
                } else {
                    $(el).text("-");
                    block.css("display", "block");
                }
            });
        });
        // activate current quest type
        if (location.hash) {
            hashchangeEvent.trigger('hashchange');
        }
        // activate first quest type
        else {
            location.hash = $("#quests-container :first-child").attr('id');
        }
    });
});