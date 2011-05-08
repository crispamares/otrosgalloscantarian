/**
 * @author crispamares
 */


var Distribution = {};

var waiting = true;


var processingInstance;

function startSketch() {
    switchSketchState(true);
}

function stopSketch() {
    switchSketchState(false);
}

function switchSketchState(on) {
    if (!processingInstance) {
        processingInstance = Processing.getInstanceById('parlam_canvas');
    }

    if (on) {
		processingInstance.diameter = 0;
		processingInstance.redraw();
        processingInstance.loop();  // call Processing loop() function
    } else {
        processingInstance.noLoop(); // stop animation, call noLoop()
    }
}

var draw_scene = function(url) {
		$.getJSON(url, function(json) {
		Distribution.colors = json.colors;
		Distribution.seats = json.seats;
		Distribution.total_seats = json.total_seats;
		Distribution.parties = json.parties;
		
		waiting = false;
		processingInstance = Processing.getInstanceById('parlam_canvas');
		processingInstance.calculate_angles();
	 	startSketch();
	 });	
};

$(document).ready(function(){  
	draw_scene("/?year=2008&alg=manoli");
});


var max_diameter =  350;

var background_color = 245;
	
var seats_percentages = function() {
	var percentages = [];
	var i = 0;
	for (i = 0; i < Distribution.seats.length; i += 1) {
		percentages.push(100.0 * Distribution.seats[i] / Distribution.total_seats);
	}
	return percentages;
};


