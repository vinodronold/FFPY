define(["jquery"], function($) {
    "use strict";

    var _song_player = $('#songs_player_success'),

        get_player_content = function() {
            console.log('get_player_content');
            if (_song_player.length) {
                // $.ajax({
                //     url: '/ajax/' + _song_player.data('ytid')
                // });
                console.log('ytid', _song_player.data('ytid'));
            }
        }

    return {get_player_content: get_player_content};

});
