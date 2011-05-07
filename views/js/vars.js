/**
 * @author crispamares
 */

$(document).ready(function(){  
	$("#paco p").html("POADPOAPODAPDOPADO");
	

$.ajax({
	url: "http://localhost:8080/?year=2005&alg=dhont",
	dataType: "json",
	success: function(json) {
   		alert("JSON Data: " + json.total_seats);
	 }
});

	
	$.getJSON("http://localhost:8080/?year=2005&alg=dhont", function(json) {
   		alert("JSON Data: " + json.total_seats);
	 })

	
	$("#paco p").load("http://localhost:8080/?year=2005&alg=dhont"); 
	}
	);





/*
$.getJSON("http://127.0.0.1:8000/otrosgalloscantarian/src/processing/parlament_dist.json", function(json) {
   alert("JSON Data: " + json.total_seats);
 })
 .error(function() { alert("error"); });
*/

var max_diameter =  350;

var background_color = 150;

var Distribution = {
	"colors" : [[255,0,0], [123,45,78], [0,0,255]],
	"seats" : [25, 75, 30],
	"total_seats" : 130,
	};
	
var seats_percentages = function() {
	var percentages = [];
	var i = 0;
	for (i = 0; i < Distribution.seats.length; i += 1) {
		percentages.push(100.0 * Distribution.seats[i] / Distribution.total_seats);
	}
	return percentages;
};
