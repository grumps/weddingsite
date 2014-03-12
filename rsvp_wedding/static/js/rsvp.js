//Fade in extras on Y condition
$('#id_will_attend').on('change', function(e) {
    if ($(this).val() === "Y") {
        $('.collapse').collapse('show')
        }
    else if ($(this).val() === "N") {
        $('.collapse').collapse('hide')
        //TODO scalable code needed.
        $('#id_is_vegetarian').val('N')
        $('#id_will_arrive_thursday').val('N')
        $('#id_will_stay_saturday').val('N')
    }});
//Show extras in the event the user is updating.
$(document).ready(function(){
    if($('#id_will_attend').val() === "Y"){
        $('.collapse').collapse('show')
    }
});