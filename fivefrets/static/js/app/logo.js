define([
    "jquery", "raphael"
], function($, ra) {
    "use strict";

    var _logo = function(_id) {
            var _paper = new ra(_id, 110, 55);
            var _frets = _paper.set();
            _frets.push(_paper.rect(5, 5, 100, 25, 2), _paper.path("M5 10L105 10M5 15L105 15M5 20L105 20M5 25L105 25M27.82 5L27.82 30M46.57 5L46.57 30M66.57 5L66.57 30M87.66 5L87.66 30"), _paper.circle(56.57, 17.5, 0.75), _paper.circle(18.91, 17.5, 0.75));
            _frets.attr({stroke: "#ffffff"});
            var _brand = _paper.text(55, 40, "f i v e f r e t s")
            _brand.attr({stroke: "#ffffff", 'stroke-width': 0.5, 'fill': '#ffffff', 'stroke-opacity': 0, 'font-size': 16});
        },

        _select_id = function() {
            $("div[id^='fflogo_']").each(function() {
                _logo($(this).attr('id'));
            });
        },

        _apply_center_class = function() {
            $("div[id^='fflogo_'] > svg").addClass("ui centered image");
        },

        draw = function() {
            _select_id();
            _apply_center_class();
        };

    return {draw: draw};

});
