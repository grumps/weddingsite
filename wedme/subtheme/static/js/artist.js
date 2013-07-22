/**
 * Created with PyCharm.
 * User: grumps
 * Date: 6/16/13
 * Time: 11:03 AM
 * To change this template use File | Settings | File Templates.
 */
/** Baseline code from EchoNest Blog */
$(function () {
//Song total Initialization
    var songTotal;
//List of Songs By Artist ordered by "hottttnesss" if over 1000 songs by artist songs of hotness < 1000 wont' be available.
    var songsList = [];

    //Split s.t. all items added have a comma separator.
    function split ( val ) {
        return val.split(/,\s*/);
    }
    function extractLast ( term ) {
        return split( term).pop();
    }
$("#song").attr('disabled', true);

//function looks up input and returns suggested artist. Upon completion builds array of songs by the artist.
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
            var artist = split(this.value)
            //Unlock Song Field.
            $("#song").attr('disabled', false);

            //remove the current input
            artist.pop();
            //add the selected value
            artist.push( ui.item.value)
            this.value = artist
            //add placeholder to get the comma-and-space at the end

            //Gets total # of songs first, then uses search api to return songs in order of hottness.
            var getSongs = $.ajax({
                    url: "http://developer.echonest.com/api/v4/artist/songs",
                    dataType: "jsonp",
                    data: {
                        results: 1,
                        api_key: "KTPZMU3CDARU82WJO",
                        format: "jsonp",
                        name: ui.item.value
                    },
                    success: function (data) {
                        songTotal = data.response.total;
                        console.log('hello  ' + songTotal);
                    }
            //Key to sequencing is actually calling 'done' since ajax is a promise.
            }).done(function() {
                //Ensures array is empty. Required if user changes artist.
                songsList = [];
                //clears any input in songs field.
                $("#song").val('');
                var startindex = 0;
                for (; startindex <= songTotal;) {
                    console.log('numsongs  ' + songTotal);
                    (function(_startindex){
                        $.ajax({
                            url: "http://developer.echonest.com/api/v4/song/search",
                                dataType: "jsonp",
                            data: {
                                    results: 100,
                                    api_key: "KTPZMU3CDARU82WJO",
                                    format: "jsonp",
                            artist: ui.item.value,
                            start: _startindex,
                            sort: 'song_hotttnesss-desc'
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
            return false;
            //$("#song").autocomplete("option", "source");
        },
        change: function (event, ui) {
            if (!ui.item) {
                 $(this).val('');

             }
        }
});
$("#song").autocomplete({
        source: function( request, response ) {
                response($.ui.autocomplete.filter(
                    songsList, extractLast (request.term)
                ));
        },
        minLength: 0,
        select: function (event, ui) {
            var terms = split(this.value)
            //remove the current input
            terms.pop();
            //add the selected value
            terms.push( ui.item.value)
            //add placeholder to get the comma-and-space at the end
            terms.push("");
            this.value = terms.join( ", ")
            return false;
            //$("#log").empty();
            //$("#log").append(ui.item ? ui.item.id + ' ' + ui.item.label : '(nothing)');
        },
        change: function (event, ui) {
            if (!ui.item) {
                 $(this).val('');
             }
        }
    });

});