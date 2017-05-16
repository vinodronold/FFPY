define([
    "jquery", "semantic_ui", "app/player"
], function($, ui, ytp) {
    "use strict";

    var sidebarmenu = function(e) {
            $('.ui.sidebar').sidebar('setting', 'transition', 'overlay').sidebar('toggle');
            e.preventDefault();
        },

        cards_image = function() {
            $('.special.cards .image').dimmer({on: 'hover'});
        },

        transpose = function(e) {
            $('.ui.segment.chordslist').each(function() {
                var m_chordid = $(this).attr('data-chordid');
                if (m_chordid != 'N') {
                    var m_chordid = Number(m_chordid) + Number(e.data.step);
                    if (m_chordid === 13) {
                        m_chordid = 1;
                    } else if (m_chordid === 0) {
                        m_chordid = 12;
                    }
                    $(this).attr('data-chordid', m_chordid);
                }
            });
            $("#ff_transpose_num").text(Number($("#ff_transpose_num").text()) + Number(e.data.step));
        };

    return {sidebarmenu: sidebarmenu, cards_image: cards_image, transpose: transpose};

});
