$(document).ready(function() {
    var headers = $('header');
    for (var i = 0; i < $(headers).length; i++) {
        if (i % 2 == 0){
            $($(headers[i])).css('color', 'navy');
        } else{
            $($(headers[i]).css('color','green'))
        }
    }

});
$("section").mouseover(function () {
    // get its original background colour
    var bgColour = $(this).css('background-color');
    // parse the bgColour to red, green, blue, alpha
    var rgbaValues = bgColour.match(/\d+/g);
    var red = 255;
    var green = 244;
    var blue = 233;
    // change alpha from its current value to 1
    var alpha = 1;
    // construct the new color string with modified components
    var newBgColour = 'rgba(' + red + ', ' + green + ', ' + blue + ', ' + alpha + ')';
    // Apply the new background colour to the current section
    $(this).css('background-color', newBgColour);
});
$("section").mouseout(function () {
    // get its original background colour

    $(this).css('background-color', '#100c3c70');
});