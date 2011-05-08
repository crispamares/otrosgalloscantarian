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
		//processingInstance.redraw();
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
		processingInstance.init();
		processingInstance.calculate_angles();
		show_info(Distribution, seats_percentages());
	 	startSketch();
	 });	
};

$(document).ready(function(){  
	draw_scene("/?year=2008&alg=dhont");
});


var max_diameter =  450;

var background_color = 255;
	
var seats_percentages = function() {
	var percentages = [];
	var i = 0;
	for (i = 0; i < Distribution.seats.length; i += 1) {
		percentages.push(100.0 * Distribution.seats[i] / Distribution.total_seats);
	}
	return percentages;
};

var show_info = function (desc, percentages) {
	var info_str = "<ul>";
	for (i=0; i < desc.parties.length; i += 1) {
		info_str += "<li id="+i+">";
		info_str += "<span class=partie>"+desc.parties[i]+": ["+desc.seats[i]+"]</span>" ;
		info_str += "<span class=partie_bars><span style=background-color:rgb("+desc.colors[i].toString()+");width:"+Math.ceil(percentages[i]*1.5)+"%>&nbsp;</span></span>";
		info_str += "</li> ";		
	}
	info_str += "</ul>";
	$("#grafico-info-adicional").html(info_str);
};


