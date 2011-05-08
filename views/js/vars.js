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
		Distribution.places = json.places;
		
		waiting = false;
		processingInstance = Processing.getInstanceById('parlam_canvas');
		processingInstance.init();
		processingInstance.calculate_angles();
		show_info(Distribution, seats_percentages());
	 	startSketch();
		var svg = $('#grafico2').svg('get');
		for (j =0; j < modified.length; j+= 1) {
			$(modified[j], svg.root()).attr('style', provStyle);
		}
	 });	
};

$(document).ready(function(){  
	draw_scene("/?year=2008&alg=dhont");
	draw_map();
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

var draw_map = function() {
    var svg = $('#grafico2').svg({loadURL: 'mapa.svg'});
};

var select_partie = function (i) {
    $("#grafico-info-adicional li").removeClass("seleccionado");
    $("#grafico-info-adicional #"+i ).addClass("seleccionado");
	draw_map_selection(Distribution, i);
};

var provStyle = "fill:#ffffd0;fill-opacity:1;fill-rule:nonzero;stroke:#000000;stroke-width:0.2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none";
var provStyle2 = "fill:#00ff00;fill-opacity:1;fill-rule:nonzero;stroke:#000000;stroke-width:0.2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none";
var preStyle = "fill:";
var midStyle = ";fill-opacity:1;fill-rule:nonzero;stroke:#000000;stroke-width:0.2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none";
var postStyle = ";fill-opacity:1;fill-rule:nonzero;stroke:#000000;stroke-width:0.2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none";

var modified = [];

var draw_map_selection = function(dist, i) {
	var places = dist.places[i];
	var svg = $('#grafico2').svg('get');
	
	for (j =0; j < modified.length; j+= 1) {
		$(modified[j], svg.root()).attr('style', provStyle);
	}

	modified = [];

	var totalValue = 0;
	for (j =0; j < places.length; j += 1) {
		totalValue = totalValue + places[j][1];
	}

	for (j =0; j < places.length; j += 1) {
		var place = '#' + places[j][0];
		var quantity = places[j][1]/totalValue;

		modified.push(place);
		
		//var svg = $('#grafico2').svg('get');
		var r = dist.colors[i][0];
		var margin = 50;
		if (r > margin)
		{
			r = parseInt(quantity*margin + r-margin);
		}
		var g = dist.colors[i][1];
		if (g > margin)
		{
			g = parseInt(quantity*margin + g-margin);
		}
		var b = dist.colors[i][2];
		if (b > margin)
		{
			b = parseInt(quantity*margin + b-margin);
		}
		var style = preStyle + "rgb(" + r + "," + g + "," + b + ")" + postStyle;

		$(place, svg.root()).attr('style', style);
	}
};
