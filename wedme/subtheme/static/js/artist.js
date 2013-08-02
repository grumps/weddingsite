/**
 * Created with PyCharm.
 * User: grumps
 * Date: 6/16/13
 * Time: 11:03 AM
 * To change this template use File | Settings | File Templates.
 */
/** Baseline code from EchoNest Blog */

$(function () {
    //setter for current number of song inputs
    var currentField = 1;
    //disable add button.
$("#add").attr('disabled',true);
    //handler for add button
$("#add").unbind('click').click(function(event) {
    event.stopPropagation();
    //Bunch of crappy HTML variables.
    var maxFields = $('#id_song_set-MAX_NUM_FORMS').val();
    var songSet = 'song_set-' + currentField + '-song';
    var autoFill = 'autocomplete="off" role="textbox" aria-autocomplete="list" aria-haspopup="true">';
    var inputField = '<input id="' + songSet + '" type="text" class="song ui-autocomplete-input input-large" name="' + songSet + '"' + autoFill;
    console.log(inputField)
    var hiddenField = '<input type=\"hidden\" name=\"' + songSet + '_id\" id=\"'+ songSet + '_id">';
    var overLoad = '<div class="alert alert-block"> \
                    <button type="button" class="close" data-dismiss="alert">&times;</button> \
                    <h4>Warning!</h4> \
                    Best check yo self, 5 songs at at time. \
                    </div>';
    currentField ++;
    if (currentField < maxFields) {
        $(this).before(inputField);
        $(this).after(hiddenField);

    }
    else if (currentField == maxFields) {
        $(this).before(inputField);
        $(this).after(hiddenField);
        $('#add').hide();

    }
    else {
        $(this).before(overLoad)
    }

});
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
$('[class^="song"]').attr('disabled', true);

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
            artist.push(ui.item.value);
            this.value = artist;


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

        },
        change: function (event, ui) {
            if (!ui.item) {
                 $(this).val('');

             }
        }
});
$('[class^="song"]').live("keydown.autocomplete", function() {
    $(this).autocomplete(songComplete);
    });


        //class for song autocomplete
        var songComplete = {
            source: function (request, response) {
                    response($.ui.autocomplete.filter(
                        songsList, extractLast(request.term)
                    ));
            },
            minLength: 0,
            select: function (event, ui) {
                var terms = split(this.value);
                //remove the current input
                terms.pop();
                //add the selected value
                terms.push(ui.item.value);
                //add placeholder to get the comma-and-space at the end
                //terms.push("");
                this.value = terms;
                //enable add button*/
                $("#add").attr('disabled', false);
            },
            change: function (event, ui) {
                if (!ui.item) {
                    $(this).val('');
                    //disable add button
                    $("#add").attr('disabled', true);
                }
            }
        };
        }

);