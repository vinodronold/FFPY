
define(["jquery", "raphael"], function($, ra) {
    "use strict";

    var _cnt = 0,

        _config = {},

        _set_config = function(startx, starty, stringSpace, fretSpace, strings, frets, padding) {
            _config.startx = startx;
            _config.starty = starty;
            _config.stringSpace = stringSpace;
            _config.fretSpace = fretSpace;
            _config.strings = strings;
            _config.frets = frets;
            _config.padding = padding;
            _config.paperx = startx + (stringSpace * (strings - 1)) + padding;
            _config.papery = starty + (fretSpace * frets) + padding;
            _config.fretWidth = stringSpace * (strings - 1);
            _config.chordNamex = startx + ((stringSpace * (strings - 1)) / 2);
            _config.chordNamey = starty - padding;

            _config.stringPath = "";
            for (_cnt = 1; _cnt < strings - 1; _cnt++) {
                var stringStartx = (startx + (stringSpace * _cnt));
                _config.stringPath = _config.stringPath + "M" + stringStartx + " " + starty + " " + "L" + stringStartx + " " + (starty + (fretSpace * frets));
            }
            _config.fretPath = "";
            for (_cnt = 1; _cnt < frets; _cnt++) {
                var fretStarty = starty + (fretSpace * _cnt);
                _config.fretPath = _config.fretPath + "M" + startx + " " + fretStarty + "L" + (startx + _config.fretWidth) + " " + fretStarty;
            }

        },

        _draw_n_plot = function(thisObj) {
            var ffcdia = thisObj.data('ffcdia').split(","), // [START_FRET, BARRE, STRING6, STRING5, STRING4, STRING3, STRING2, STRING1]
                startFretNum = ffcdia[0],
                position = ffcdia.slice(1, 8),
                first_fret;
            if (Number(startFretNum) === 1) {
                first_fret = "M" + _config.startx + " " + (_config.starty + 1) + "L" + (_config.startx + _config.fretWidth) + " " + (_config.starty + 1);
            }
            var cdia = new ra(thisObj.attr('id'), _config.paperx, _config.papery);
            cdia.setViewBox(0, 0, _config.paperx, _config.paperx, 1)
            var cdia_frets = cdia.set();
            cdia_frets.push(
                cdia.text(_config.chordNamex, _config.chordNamey, thisObj.data('ffcdianame')),
                cdia.rect(_config.startx, _config.starty, _config.fretWidth, (_config.fretSpace * _config.frets), 2),
                cdia.path(_config.stringPath + _config.fretPath + first_fret)
            );
            for (_cnt = 0; _cnt < _config.frets; _cnt++) {
                cdia_frets.push(
                    cdia.text(_config.padding, _config.starty + ((_config.fretSpace * _cnt) + (_config.fretSpace / 2)), (Number(startFretNum[0]) + _cnt))
                );
            }

            var cdia_finger = cdia.set();
            if (position[0] > 0 && position[0] <= _config.frets) {
                var barreStarty = _config.starty + (_config.fretSpace * (position[0] - 1)) + (_config.fretSpace / 3);
                var barrePath = "M" + _config.startx + " " + barreStarty +
                    "L" + (_config.startx + _config.fretWidth) + " " + barreStarty +
                    "A1 1 0 0 1 " + (_config.startx + _config.fretWidth) + " " + (barreStarty + 5) +
                    "L" + _config.startx + " " + (barreStarty + 5) +
                    "A1 1 0 0 1 " + _config.startx + " " + barreStarty;
                cdia_finger.push(
                    cdia.path(barrePath)
                );
            }
            $.each(position, function(index, value) {
                if (index > 0 && value > 0) {
                    cdia_finger.push(
                        cdia.circle((_config.startx + (_config.stringSpace * (index - 1))), (_config.starty + (_config.fretSpace * (value - 1)) + (_config.fretSpace / 2)), 3)
                    );
                }

            })
            cdia_finger.attr({
                stroke: '#333',
                'fill': '#333'
            });
        },

        _centered_image = function() {
            $("div[id^='ffcdia_'] > svg").addClass("ui fluid centered image");
        },

        _guitar_chord = function() {
            _set_config(15, 10, 10, 15, 6, 4, 5);
            $("div[id^='ffcdia_']").each(function() {
                _draw_n_plot($(this))
            });
        },

        draw = function() {
            _guitar_chord();
            _centered_image();
        };

    return {
        draw: draw
    };

});
