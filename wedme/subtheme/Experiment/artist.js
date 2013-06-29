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
            getSongs();


        },
        change: function (event, ui) {

            if (!ui.item) {
                 $(this).val('');
             }
        }
});
var songsList = [];

function getSongs() {
    var numsongs = 2; //at least 2 runs.
    var startindex = 0;
    runonceloop: //<~~~~Referenced in question
    for (var j = 0; j <= _numsongs;j++) {
        console.log('numsongs  ' + numsongs);
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
                _numsongs = data.response.total; //modify exit condition
                for (var i = 0; i < songs.length; i++) {
                    songsList.push(songs[i].title);

                }

            }
        });
        })(startindex);
        startindex+=100;
        if (j <= numsongs) {
            break
        }
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


