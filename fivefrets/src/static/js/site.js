// fivefrets js
/*
$(document).ready(function() {
    function Logo(id) {
        var paper = new Raphael(id, 110, 55);
        var frets = paper.set();
        frets.push(
            paper.rect(5, 5, 100, 25, 2),
            paper.path("M5 10L105 10M5 15L105 15M5 20L105 20M5 25L105 25M27.82 5L27.82 30M46.57 5L46.57 30M66.57 5L66.57 30M87.66 5L87.66 30"),
            paper.circle(56.57, 17.5, 0.75),
            paper.circle(18.91, 17.5, 0.75)
        );
        frets.attr({
            stroke: "#ffffff"
        });
        var brand = paper.text(55, 40, "f i v e f r e t s")
        brand.attr({
            stroke: "#ffffff",
            'stroke-width': 0.5,
            'fill': '#ffffff',
            'stroke-opacity': 0,
            'font-size': 16
        });
    }
    $("div[id^='fflogo_']").each(function(index) {
        Logo($(this).attr('id'));
    });
    $("div[id^='fflogo_'] > svg").addClass("ui centered image");
});

$(document).ready(function() {
    $("div[id^='ffcdia_']").each(function(index) {
        var startx = 15,
            starty = 10,
            stringSpace = 10,
            fretSpace = 15,
            strings = 6,
            frets = 4,
            padding = 5,
            //position = [1,0,0,3,3,3,0]; // [BARRE, STRING6, STRING5, STRING4, STRING3, STRING2, STRING1]
            ffcdia = $(this).data('ffcdia').split(","); // [START_FRET, BARRE, STRING6, STRING5, STRING4, STRING3, STRING2, STRING1]
        var paperx = startx + (stringSpace * (strings - 1)) + padding,
            papery = starty + (fretSpace * frets) + padding,
            fretWidth = stringSpace * (strings - 1),
            chordNamex = startx + ((stringSpace * (strings - 1)) / 2),
            chordNamey = starty - padding,
            startFretNum = ffcdia.slice(0, 1),
            position = ffcdia.slice(1, 8),
            stringPath,
            fretPath;
        stringPath = "";
        for (cnt = 1; cnt < strings - 1; cnt++) {
            var stringStartx = (startx + (stringSpace * cnt));
            stringPath = stringPath + "M" + stringStartx + " " + starty + " " + "L" + stringStartx + " " + (starty + (fretSpace * frets));
        }
        fretPath = "";
        if (startFretNum == 1) {
            fretPath = fretPath + "M" + startx + " " + (starty + 1) + "L" + (startx + fretWidth) + " " + (starty + 1);
        }
        for (cnt = 1; cnt < frets; cnt++) {
            var fretStarty = starty + (fretSpace * cnt);
            fretPath = fretPath + "M" + startx + " " + fretStarty + "L" + (startx + fretWidth) + " " + fretStarty;
        }
        var cdia = new Raphael($(this).attr('id'), paperx, papery);
        cdia.setViewBox(0, 0, paperx, paperx, 1)
        var cdia_frets = cdia.set();
        cdia_frets.push(
            cdia.text(chordNamex, chordNamey, $(this).data('ffcdianame')),
            cdia.rect(startx, starty, fretWidth, (fretSpace * frets), 2),
            cdia.path(stringPath + fretPath)
        );
        for (cnt = 0; cnt < frets; cnt++) {
            cdia_frets.push(
                cdia.text(padding, starty + ((fretSpace * cnt) + (fretSpace / 2)), (Number(startFretNum[0]) + cnt))
            );
        }

        var cdia_finger = cdia.set();
        if (position[0] > 0 && position[0] <= frets) {
            var barreStarty = starty + (fretSpace * (position[0] - 1)) + (fretSpace / 3);
            var barrePath = "M" + startx + " " + barreStarty +
                "L" + (startx + fretWidth) + " " + barreStarty +
                "A1 1 0 0 1 " + (startx + fretWidth) + " " + (barreStarty + 5) +
                "L" + startx + " " + (barreStarty + 5) +
                "A1 1 0 0 1 " + startx + " " + barreStarty;
            cdia_finger.push(
                cdia.path(barrePath)
            );
        }
        $.each(position, function(index, value) {
            if (index > 0 && value > 0) {
                cdia_finger.push(
                    cdia.circle((startx + (stringSpace * (index - 1))), (starty + (fretSpace * (value - 1)) + (fretSpace / 2)), 3)
                );
            }

        })
        cdia_finger.attr({
            stroke: '#333',
            'fill': '#333'
        });
    });
    $("div[id^='ffcdia_'] > svg").addClass("ui fluid centered image");
});
*/
$(document).ready(function() {
    /*
      $.fn.embed.settings.sources = {
          ff_youtube: {
              name: 'ff_youtube',
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
      */
    /*
    $('#ffsidebarmenu').click(function() {
        $('.ui.sidebar')
            .sidebar('setting', 'transition', 'overlay')
            .sidebar('toggle');
    });
    $('.special.cards .image').dimmer({
        on: 'hover'
    });
    */
    /*
        $('#ff_transpose_plus').click(function() {
            $(".ui.segment.chordslist").each(function(index) {
                var m_chordid = $(this).attr('data-chordid');
                if (m_chordid != 'N') {
                    if (m_chordid == '12') {
                        m_chordid = 0;
                    }
                    m_chordid = Number(m_chordid) + 1;
                    $(this).attr('data-chordid', m_chordid);
                }
            });
            var transpose_num = $("#ff_transpose_num").text();
            $("#ff_transpose_num").text(Number(transpose_num) + 1);
        });

        $('#ff_transpose_minus').click(function() {
            $(".ui.segment.chordslist").each(function(index) {
                var m_chordid = $(this).attr('data-chordid');
                if (m_chordid != 'N') {
                    if (m_chordid == '1') {
                        m_chordid = 13;
                    }
                    m_chordid = Number(m_chordid) - 1;
                    $(this).attr('data-chordid', m_chordid);
                }
            });
            var transpose_num = $("#ff_transpose_num").text();
            $("#ff_transpose_num").text(Number(transpose_num) - 1);
        });
    */
    $('.ui.search')
        .search({
            //type          : 'youtube',
            minCharacters: 3,
            apiSettings: {
                onResponse: function(youtubeResponse) {
                    var response = {
                        results: []
                    };
                    // translate YouTube API response to work with search
                    $.each(youtubeResponse.items, function(index, item) {
                        response.results.push({
                            title: item.snippet.title,
                            url: '/chords/display/' + item.id.videoId,
                            //description : item.snippet.description,
                            image: item.snippet.thumbnails.default.url
                        });
                    });
                    return response;
                },
                url: 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={query}&type=video&videoCategoryId=10&key=AIzaSyCpVWdjX0SBFRSfsYcxltR50IhOncXl0YU'
            }
        });

    // youtube api
    var player;
    $('.ui.embed').embed({
        onDisplay: function() {
            $('.embed > iframe').attr('id', 'ff_ytplayer');
            var tag = document.createElement('script');
            tag.id = 'iframe-demo';
            tag.src = 'https://www.youtube.com/iframe_api';
            var firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        }
    });
    window.onYouTubeIframeAPIReady = function() {
        console.log('onYouTubeIframeAPIReady');
        player = new YT.Player('ff_ytplayer', {
            events: {
                'onReady': onPlayerReady,
                'onStateChange': onPlayerStateChange
            }
        });
    };
    if (typeof ffchordlist === 'undefined' || ffchordlist === null) {
        var ffchordlist = {};
    };

    $(".chordslist").each(function(index) {
        var ffchordlist_item = {};
        ffchordlist_item.curr = $(this);
        if (index > 0) {
            ffchordlist_item.prev = ffchordlist[Number($(this).data('chordidx')) - 1].curr;
        } else {
            ffchordlist_item.prev = null;
        }
        ffchordlist[$(this).data('chordidx')] = ffchordlist_item;
        //console.log(index, $(this).data('chordidx'), $(this).data('postn'));
    });
    var no_of_chords = 8,
        chordSegment = $(".ui.segment.chords");
    chordSegment.scrollTop(0);

    var chord_transition_t,
        ffstart_time = 0,
        startpos = 0;
    var chord_transition = function(stop_transition) {
        startpos = $('.chordslist.orange.inverted').data('chordidx');
        if (!startpos) {
            startpos = 1;
        }
        if (typeof chord_transition_int === 'undefined' || chord_transition_int === null) {
            var chord_transition_int = function() {
                chord_transition_t = setInterval(function() {
                    var ffCurTime = player.getCurrentTime();
                    if (ffCurTime > ffstart_time) {
                        ffchordlist[startpos].curr.addClass("orange inverted");
                        if (startpos > 1) {
                            ffchordlist[startpos].prev.removeClass("orange inverted");
                        }
                        if (startpos > no_of_chords && (startpos % no_of_chords) == 1) {
                            // chordSegment.scrollTop(((startpos / no_of_chords) - 1) * 77);
                            chordSegment.animate({
                                scrollTop: (((startpos / no_of_chords) - 1) * 77)
                            }, 200);
                        }
                        startpos++;
                        if (typeof ffchordlist[startpos] === 'undefined') {
                            console.log('transition ended');
                            clearInterval(chord_transition_t);
                        } else {
                            ffstart_time = ffchordlist[startpos].curr.data('postn');
                        }
                    }
                    if (Math.abs(ffCurTime - ffstart_time) > 3 && startpos > 2) {
                        //console.log('seek occurred');
                        $.each(ffchordlist, function(idx) {
                            if ($(this)[0].curr.data('postn') > ffCurTime) {
                                console.log('seek occurred', ffCurTime, ffstart_time);
                                //clearInterval(chord_transition_t);
                                seekToClickPostn($(this)[0].curr, true);
                                //chord_transition_int();
                                startpos = $(this)[0].curr.data('chordidx');
                                ffstart_time = ffchordlist[Number(startpos) + 1].curr.data('postn');
                                console.log(idx, $(this)[0].curr.data('postn'));
                                return false;
                            }
                        });
                    }
                }, 20);
            }
        }
        if (stop_transition === false) {
            console.log('start chord_transition', startpos);
            clearInterval(chord_transition_t);
            chord_transition_int();
        } else {
            console.log('stop chord_transition', startpos);
            clearInterval(chord_transition_t);
        }
    }
    var seekToClickPostn = function(obj, seekFromVideo) {
        var seekToClickPostn_tout = setTimeout(function() {
            if ($('.chordslist.orange.inverted').length) {
                $('.chordslist.orange.inverted').removeClass('orange inverted');
                if (obj) {
                    obj.addClass('orange inverted');
                    if (seekFromVideo === false) {
                        if (Number(obj.data('postn')) <= no_of_chords) {
                            chordSegment.scrollTop(0);
                        }
                        player.seekTo(Number(obj.data('postn')), true);
                    }
                } else {
                    if (seekFromVideo === false) {
                        player.seekTo(0, true);
                    }
                };
                clearTimeout(seekToClickPostn_tout);
                console.log('removed Highlight');
            }
        }, 20);
    }
    if (typeof playing === 'undefined' || playing === null) {
        var playing = false;
    };
    var pausingVideo = function(triggerPause) {
        if (triggerPause === true) {
            player.pauseVideo();
        };
        $('#ff_play').html('<i class="play icon"></i>');
        playing = false;
        console.log('pausingVideo');
    };
    var playingVideo = function(triggerPlay) {
        if (triggerPlay === true) {
            player.playVideo();
        }
        $('#ff_play').html('<i class="pause icon"></i>');
        playing = true;
        console.log('playingVideo');
        if (typeof ffchordlist[startpos] === 'undefined') {
            console.log('REPLAY');
            seekToClickPostn(ffchordlist[1].curr, true);
        }
    };
    $('#ff_start').click(function() {
        if (player) {
            chord_transition(true, 0);
            chordSegment.scrollTop(0);
            seekToClickPostn('', false);
        }
    });
    $('#ff_play').click(function() {
        if (!player) {
            $('.ui.embed > i.video.play').click();
        } else {
            if (playing === true) {
                pausingVideo(true);
            } else {
                playingVideo(true);
            }
        };
    });
    $('.ui.segment.chordslist').click(function() {
        console.log('seek to ', $(this).data('postn'));
        if (player) {
            chord_transition(true, 0);
            seekToClickPostn($(this), false);
        }
    });

    function onPlayerReady() {
        player.setPlaybackQuality('tiny');
    }

    function onPlayerStateChange(event) {
        if (event.data == -1) {
            console.log('unstarted'); // unstarted = gray
        } else if (event.data == YT.PlayerState.ENDED) {
            pausingVideo(false);
            console.log('ENDED');
        } else if (event.data == YT.PlayerState.PLAYING) {
            playingVideo(false);
            chord_transition(false, 0);
            console.log('PLAYING');
        } else if (event.data == YT.PlayerState.PAUSED) {
            chord_transition(true, 0);
            pausingVideo(false);
            console.log('PAUSED');
        } else if (event.data == YT.PlayerState.BUFFERING) {
            pausingVideo(false);
            console.log('BUFFERING');
        } else if (event.data == YT.PlayerState.CUED) {
            console.log('video cued'); // video cued = orange
        }
    }

});
