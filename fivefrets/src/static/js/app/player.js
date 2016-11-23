define(["jquery", "semantic_ui"], function($, ui) {
    "use strict";

    var _player,
        _playing = false,
        _ffchordlist = {},
        _ffchordlist_len = 0,
        _chordTransition_TO,
        _seek_to_postn_TO,
        _CurTime,
        _startTime = 0,
        _startPos = 0,
        _chordInRow = 8,
        _activeChord = 'orange inverted',
        _chordSegment = $('.ui.segment.chords'),

        _embed_YT = function() {
            $('.embed > iframe').attr('id', 'ff_ytplayer');
            $.getScript('//www.youtube.com/iframe_api');
            window.onYouTubeIframeAPIReady = function() {
                console.log('onYouTubeIframeAPIReady');
                _player = new YT.Player('ff_ytplayer', {
                    events: {
                        'onReady': _onPlayerReady,
                        'onStateChange': _onPlayerStateChange
                    }
                });
            };
            _chordSegment.scrollTop(0);
            $(".chordslist").each(function(index) {
                var _ffchordlist_item = {};
                _ffchordlist_item.curr = $(this);
                _ffchordlist_item.curr.on('click', _seek_to_postn);
                if (index > 0) {
                    _ffchordlist_item.prev = _ffchordlist[Number($(this).data('chordidx')) - 1].curr;
                } else {
                    _ffchordlist_item.prev = null;
                }
                _ffchordlist[$(this).data('chordidx')] = _ffchordlist_item;
                _ffchordlist_len++;
            });
        },

        _setting = function() {
            $.fn.embed.settings.sources = {
                youtube: {
                    name: 'youtube',
                    type: 'video',
                    icon: 'video play',
                    domain: 'youtube.com',
                    url: '//www.youtube.com/embed/{id}',
                    parameters: function(settings) {
                        return {
                            autohide: !settings.showUI,
                            autoplay: settings.autoplay,
                            color: settings.colors || undefined,
                            hq: settings.hd,
                            jsapi: settings.api,
                            modestbranding: 1,
                            fs: 0,
                            rel: 0,
                            showinfo: 0,
                            playsinline: 1,
                            enablejsapi: 1
                        };
                    }
                }
            };
        },

        _embed_player = function() {
            $('.ui.embed').embed({
                onDisplay: _embed_YT
            });
        },

        _set_startPos = function() {
            var startPos_chordslist = $('.chordslist.' + _activeChord.replace(' ', '.'));
            _startPos = startPos_chordslist.data('chordidx');
            _startTime = startPos_chordslist.data('postn');
            if (!_startPos) {
                _startPos = 1;
                _startTime = 0;
            };
            _scroll_chords();
            console.log('Starting from : ', _startPos, _startTime);
        },

        _scroll_chords = function() {
            _chordSegment.animate({
                    // scrollTop: (((_startPos / _chordInRow) - 1) * 77)
                    scrollTop: ((Math.floor(_startPos / _chordInRow) - 1) * 77) + (Math.floor(_startPos / (_chordInRow * 13)) * 10)
                },
                500);
        },

        _detect_manual_seek = function() {
            if (Math.abs(_CurTime - _startTime) > 3) {
                clearInterval(_chordTransition_TO);
                $.each(_ffchordlist, function(idx) {
                    if ($(this)[0].curr.data('postn') > _CurTime) {
                        console.log('Manual Seek to ', $(this)[0].curr.data('postn'));
                        $(this)[0].curr.click();
                        return false;
                    }
                });
            }
        },

        _moveChord = function() {
            _CurTime = _player.getCurrentTime();
            if (_CurTime >= _startTime) {
                //console.log(_startPos);
                _ffchordlist[_startPos].curr.addClass(_activeChord);
                if (_startPos > 1) {
                    _ffchordlist[_startPos].prev.removeClass(_activeChord);
                }
                if (_startPos > _chordInRow && (_startPos % _chordInRow) == 1) {
                    _scroll_chords();
                }
                if (_startPos >= _ffchordlist_len) {
                    clearInterval(_chordTransition_TO);
                    return;
                }
                _startPos++;
                _startTime = _ffchordlist[_startPos].curr.data('postn');
            };
            _detect_manual_seek();
        },

        _chordTransition = function() {
            _set_startPos();
            _chordTransition_TO = setInterval(_moveChord, 20)
        },

        _seek_to_postn = function() {
            if (_player) {
                _seek_to_postn_TO = setTimeout(function(thisObj) {
                    console.log('_seek_to_postn_TO - ', thisObj.data('postn'));
                    if ($('.chordslist.' + _activeChord.replace(' ', '.')).length) {
                        clearInterval(_chordTransition_TO);
                        _ffchordlist[_startPos].curr.removeClass(_activeChord);
                        _ffchordlist[_startPos].prev.removeClass(_activeChord);
                        _player.seekTo(thisObj.data('postn'), true);
                        if (Number(thisObj.data('postn')) > 0) {
                            _ffchordlist[thisObj.data('chordidx')].curr.addClass(_activeChord);
                        }
                        clearTimeout(_seek_to_postn_TO);
                    };
                }($(this)), 20);
            };
        },

        _play_pause = function() {
            if (!_player) {
                $('.ui.embed > i.video.play').click();
            } else {
                if (_playing === true) {
                    _player.pauseVideo();
                } else {
                    _player.playVideo();
                }
            };
        },

        _register_player_event = function() {
            $('#ff_play').on('click', _play_pause);
            $('#ff_start').on('click', _seek_to_postn);
        };

    function _onPlayerReady() {
        console.log('onPlayerReady');
        _player.setPlaybackQuality('tiny');
    };

    function _onPlayerStateChange(e) {
        switch (e.data) {
            case YT.PlayerState.PLAYING:
                _chordTransition();
                _playing = true;
                $('#ff_play').html('<i class="pause icon"></i>');
                //console.log('PLAYING');
                break;
            case YT.PlayerState.PAUSED:
                clearInterval(_chordTransition_TO);
                _playing = false;
                $('#ff_play').html('<i class="play icon"></i>');
                //console.log('PAUSED');
                break;
            case YT.PlayerState.ENDED:
                clearInterval(_chordTransition_TO);
                _ffchordlist[_ffchordlist_len].curr.removeClass(_activeChord);
                _playing = false;
                $('#ff_play').html('<i class="play icon"></i>');
                //console.log('ENDED');
                break;
            case YT.PlayerState.BUFFERING:
                _playing = false;
                //console.log('BUFFERING');
                break;
            case YT.PlayerState.CUED:
                //console.log('CUED');
        }
    };

    var init = function() {
        _setting();
        _embed_player();
        _register_player_event();
    };

    return {
        init: init
    }

});
