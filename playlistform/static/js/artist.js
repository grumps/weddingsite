/**
 * Created with PyCharm.
 * User: grumps
 * Date: 6/16/13
 * Time: 11:03 AM
 * Readme:
 * Original Code for artistComplete was found on the Echonest Blog.
 * This my first work with JavaScript and JQuery.  It's ugly. I'd like to re-do it but there's no time.
 */



$(function () {

    /**
     *Bunch of global variables here, and "utility functions."
     */
    //setter for current number of song inputs
    var currentField = 1;
    //disable add button.
    $("#add").attr('disabled',true);
    //Song total set
    var songTotal;
    //List of Songs By Artist ordered by "hottttnesss" if over 1000 songs by artist songs of hotness < 1000 wont' be available.
    var songsList = [];
    var songsListClean = [];
    var selectedSongs = [];
    function cleanList () {
                var arr = songsList.sort();
                var Clean = [arr[0]];
                for (var k = 1; k < arr.length; k++) { // start loop at 1 as element 0 can never be a duplicate
                    if (arr[k-1] !== arr[k]) {
                        songsListClean.push(arr[k]);
                    }
                }

    }
    var match = '<div class="alert span6"> \
                 <button type="button" class="close" data-dismiss="alert">&times;</button> \
                 <strong>Duplicate Entry!</strong> \
                 Best check your self. We heard you the first time.\
                 </div>';
        //Split s.t. all items added have a comma separator.
    function split ( val ) {
        return val.split(/,\s*/);
    }


 /**
  *
  * Event handlers
  *
 */

     //event handler for page load
$('[class^="song"]').attr('disabled', true);

    //event for "artist"
$("#artist").on("keydown.autocomplete", function(){
    //events clean song in case user changes artist
    $('[class^="song"]').val('');
    $('[class^="song"]').attr('disabled', true);

    $(this).autocomplete(artistComplete);
    });

    //event for "song"
$(document).on("keydown.autocomplete",'[class^="song"]', function() {
    $("#artist").attr('disabled', true);
    $(this).autocomplete(songComplete);
    });


    //event for add button
$("#add").unbind('click').click(function(event) {
    event.stopPropagation();
    //Bunch of crappy HTML variables.
    var maxFields = $('#id_song_set-MAX_NUM_FORMS').val();
    var songSet = 'song_set-' + currentField + '-song';
    var autoFill = 'autocomplete="off" role="textbox" aria-autocomplete="list" aria-haspopup="true"> ';
    var inputField = '<input id="' + songSet + '" type="text" class="song ui-autocomplete-input input-large" name="' + songSet + '"' + autoFill;
    var overLoad = '<div class="alert alert-block"> \
                    <button type="button" class="close" data-dismiss="alert">&times;</button> \
                    <h4>Warning!</h4> \
                    Best check yo self, 5 songs at at time. \
                    </div>';

    currentField ++;
    if (currentField < maxFields) {
        $(this).before(inputField);
        //$(this).after(hiddenField);
        $('[class^="song"]:last').focus();
        $("#artist").attr('disabled', true);
        $('#id_song_set-TOTAL_FORMS').val(currentField);
    }
    else if (currentField == maxFields) {
        $(this).before(inputField).focus();
        $(this).after(hiddenField);
        $('#add').hide();
        $('[class^="song"]:last').focus();

    }
    else {
        $(this).before(overLoad)
    }
    $("#add").attr('disabled', true);
});

    /**
     *
     * Class for handling Artist autocomplete.
     * class looks up input and returns suggested artist. Upon completion builds array of songs by the artist.
     *
     */
    var artistComplete = {
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
            $('[class^="song"]').attr('disabled', false);
            //remove the current input
            artist.pop();
            //add the selected value
            artist.push(ui.item.value);
            this.value = artist;
            $('#id_artist_id').val(ui.item.id);
            console.log(ui.item.id);
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
                            url: "http://developer.echonest.com/api/v4/artist/songs",
                                dataType: "jsonp",
                            data: {
                                    results: 100,
                                    api_key: "KTPZMU3CDARU82WJO",
                                    format: "jsonp",
                            name: ui.item.value,
                            start: _startindex,
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
        },//End of Artist Select.
        change: function (event, ui) {
            if (!ui.item) {
                 $(this).val('');
                $('[class^="song"]').val('');
                $('[class^="song"]').attr('disabled', true);
                songsListClean = [];
                songsList = [];

             }
        }
    };
    //class for song autocomplete
    var songComplete = {
            source: function (request, response) {
                //Cleans the songsList array s.t. there are no duplicates.
                if (songsListClean.length === 0) {
                    cleanList();
                }
                var re = $.ui.autocomplete.escapeRegex(request.term);
                var matcher = new RegExp( "^" + re, "i" );
                var a = $.grep( songsListClean, function(item,index){
                    return matcher.test(item);
                });
                response(a);

            },
            minLength: 2,
            select: function (event, ui) {
                var terms = split(this.value);
                //Check to make sure it's not a duplicate
                if ($.inArray(ui.item.value,selectedSongs) > -1) {
                    $('[id="add"]:last').after(match);
                    ui.item.value = '';

                }
                else {
                    //remove the current input
                    terms.pop();
                    //add the selected value
                    terms.push(ui.item.value);
                    selectedSongs.push(ui.item.value);
                    this.value = terms;
                    //enable add button
                    $("#add").attr('disabled', false);

                }
            },
            change: function (event, ui) {
                if (!ui.item) {
                    $(this).val('');
                    //disable add button
                    $("#add").attr('disabled', true);
                    //remove item from selected array
                    selectedSongs.splice(($.inArray(ui.item ,selectedSongs)),1);
                }
            }
        };
});
$(document).ready(function(){
        //event for submit action
    $('#target').submit(function(){
        $('#artist').removeAttr('disabled');
    });
});