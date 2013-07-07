/**
 * Created with PyCharm.
 * User: grumps
 * Date: 6/16/13
 * Time: 11:03 AM
 * To change this template use File | Settings | File Templates.
 */
/** Baseline code from EchoNest Blog */
$(function() {
$("#song").attr('disabled', true);
$("#artist").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "http://developer.echonest.com/api/v4/artist/suggest",
                dataType: "jsonp",
                data: {
                    results: 12,
                    api_key: "KTPZMU3CDARU82WJO",
                    format: "jsonp",
                    name: request.term
                },
                success: function (data) {
                    response($.map(data.response.artists, function (item) {
                        return {
                            label: item.name,
                            value: item.name,
                            id: item.id
                        }
                    }));
                }
            });
        },
        minLength: 3,
        select: function (event, ui) {
            $("#log").empty();
            $("#log").append(ui.item ? ui.item.id + ' ' + ui.item.label : '(nothing)');
            $("#song").attr('disabled', false);
            $("#song").autocomplete("option", "source");
            var differ = jQuery.Deferred();
            differ.resolve(function () {
                $.ajax({
                    url: "http://developer.echonest.com/api/v4/artist/songs",
                    dataType: "jsonp",
                    data: {
                        results: 1,
                        api_key: "KTPZMU3CDARU82WJO",
                        format: "jsonp",
                        name: $("#artist").val(),
                    },
                    success: function (data) {
                        songTotal = data.response.total; //modify exit condition
                        console.log('hello  ' + songTotal);
                    }
                });
                return songTotal
            });

            differ.done( function(songTotal) {
                var startindex = 0;
                for (var j = 0; j <= songTotal;j++) {
                    console.log('numsongs  ' + songTotal);
                    (function(_startindex){
                        $.ajax({
                            url: "http://developer.echonest.com/api/v4/artist/songs",
                                dataType: "jsonp",
                            data: {
                                    results: 100,
                                    api_key: "KTPZMU3CDARU82WJO",
                                    format: "jsonp",
                            name: $("#artist").val(),
                            start: _startindex
                            },

                        success: function (data) {
                            var songs = data.response.songs;
                                for (var i = 0; i < songs.length; i++) {
                                     songsList.push(songs[i].title);
                                }
                        }
                        });
                    })(startindex);
                     startindex+=100;
                }
        });
        },
        change: function (event, ui) {

            if (!ui.item) {
                 $(this).val('');
             }
        }
});
var songsList = [];

function getSongs() {
    var startindex = 0;
    for (var j = 0; j <= songTotal;j++) {
        console.log('numsongs  ' + songTotal);
        (function(_startindex){
        $.ajax({
            url: "http://developer.echonest.com/api/v4/artist/songs",
            dataType: "jsonp",
            data: {
                results: 100,
                api_key: "KTPZMU3CDARU82WJO",
                format: "jsonp",
                name: $("#artist").val(),
                start: _startindex

            },

            success: function (data) {
                var songs = data.response.songs;
                for (var i = 0; i < songs.length; i++) {
                    songsList.push(songs[i].title);
                }

            }
        });
        })(startindex);
        startindex+=100;
    }
};



$("#song").autocomplete({
        source: songsList,


        minLength: 3,
        select: function (event, ui) {
            $("#log").empty();
            $("#log").append(ui.item ? ui.item.id + ' ' + ui.item.label : '(nothing)');
        },
        change: function (event, ui) {
            if (!ui.item) {
                 $(this).val('');
             }
        }
});
    });


