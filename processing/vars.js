/**
 * @author crispamares
 */
var max_diameter =  350;

var background_color = 50;

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
