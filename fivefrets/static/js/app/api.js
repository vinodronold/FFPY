define([
    "jquery", "semantic_ui", "app/ui", "app/cdiagram", "app/player"
], function($, ui, appui, cdia, player) {
    "use strict";
    var _song_player = $('#songs_player'),

        _player_process_status_success,

        _ajax_TO,

        _event_registration = function() {
            $('#ffsidebarmenu').on('click', appui.sidebarmenu);
            $('#ff_transpose_plus').on('click', {
                step: '1'
            }, appui.transpose);
            $('#ff_transpose_minus').on('click', {
                step: '-1'
            }, appui.transpose);
        },

        _apply_player_config = function() {
            _event_registration();
            cdia.draw();
            player.init();
        },

        get_player_content = function() {
            _player_process_status_success = $('#player_process_status_success');
            if (!_player_process_status_success.length) {
                (function _ajax_pull() {
                    _ajax_TO = setTimeout(function() {
                        if (_song_player.length) {
                            $.ajax({
                                url: '/songs/ajax/' + _song_player.data('ytid'),
                                success: function(response) {
                                    _song_player.html(response);
                                    _apply_player_config();
                                    _player_process_status_success = $('#player_process_status_success');
                                    if (!_player_process_status_success.length) {
                                        _ajax_pull(); // recurse
                                    }
                                }
                            });
                        }
                    }, 5000);
                })();
            };
            _apply_player_config();
        },

        yt_search = function() {
            if ($('.ui.search.authenticated').length) {
                $('.ui.search').search({
                    minCharacters: 5,
                    apiSettings: {
                        onResponse: function(youtubeResponse) {
                            var response = {
                                results: []
                            };
                            // translate YouTube API response to work with search
                            $.each(youtubeResponse.items, function(index, item) {
                                response.results.push({
                                    title: item.snippet.title,
                                    url: '/songs/play/' + item.id.videoId,
                                    image: item.snippet.thumbnails.default.url
                                });
                            });
                            return response;
                        },
                        url: 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={query}&type=video&videoCategoryId=10&fields=items(id,snippet/title,snippet/thumbnails/default/url)&key=AIzaSyBreuZkq35jobxJekOwTMlKTEdUXfIJ17w'
                    }
                });
            } else {
                $('.ui.search').search({
                    source: [
                        {
                            title: '',
                            description: ''
                        }
                    ],
                    searchFullText: false,
                    error: {
                        noResults: 'To search, you must login.'
                    }
                });
            }
        };

    return {get_player_content: get_player_content, yt_search: yt_search};
});
