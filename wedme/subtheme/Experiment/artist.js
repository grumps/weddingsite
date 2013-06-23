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

        },
        change: function (event, ui) {

            if (!ui.item) {
                 $(this).val('');
             }
        }
});


$("#song").autocomplete({

        source: function (request, response) {

            $.ajax({
                url: "http://developer.echonest.com/api/v4/artist/songs",
                dataType: "jsonp",
                data: {

                    results: 5,
                    api_key: "KTPZMU3CDARU82WJO",
                    format: "jsonp",
                    name: $("#artist").val(),

                    /**artist: "radiohead",*/
                    title: request.term
                },
                success: function (data) {
                    response($.map(data.response.songs, function (item) {
                        return {
                            label: item.title,
                            value: item.title,
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

        },
        change: function (event, ui) {
            if (!ui.item) {
                 $(this).val('');
             }
        }
});
});

