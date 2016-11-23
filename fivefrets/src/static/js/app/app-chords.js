define(["jquery", "app/logo", "app/ui", "app/cdiagram", "app/player"], function($, logo, appui, cdia, player) {
    "use strict";

    var _event_registration = function() {
            $('#ffsidebarmenu').on('click', appui.sidebarmenu);
            $('#ff_transpose_plus').on('click', {
                step: '1'
            }, appui.transpose);
            $('#ff_transpose_minus').on('click', {
                step: '-1'
            }, appui.transpose);
        },

        init = function() {
            _event_registration();
            logo.draw();
            appui.cards_image();
            cdia.draw();
            player.init();
        };

    return {
        init: init
    }
});
