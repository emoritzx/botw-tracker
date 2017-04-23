requirejs.config({
    paths: {
        "jquery": "/static/lib/jquery-3.2.1.min"
    }
});

requirejs(['jquery'], function($) {
    var ATTRIBUTE = 'data-quests-active';
    var hashchangeEvent = $(window).on('hashchange', function() {
        var hash = location.hash.substr(1);
        $('[' + ATTRIBUTE + ']').each(function(index, container) {
            $(container).attr(ATTRIBUTE, 'False');
        });
        $("#" + hash).attr(ATTRIBUTE, 'True');
    });
    if (location.hash) {
        hashchangeEvent.trigger('hashchange');
    }
});