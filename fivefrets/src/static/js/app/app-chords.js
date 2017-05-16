define([
    "jquery", "app/ui", "app/api"
], function($, appui, aapi) {
    "use strict";

    var init = function() {
        appui.cards_image();
        aapi.yt_search();
        aapi.get_player_content();
    };

    return {init: init}
});
