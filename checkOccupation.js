var POLL_PERIOD = 2000; // in milliseconds

$( document ).ready(function() {

	checkOccupation();
	setInterval(function () {checkOccupation();}, POLL_PERIOD);

	function checkOccupation() {
		$.get("occupation", function(data){
			if(data == "free") {
			$("#mycoolstuff").css("background-color", "green");
			favicon.change('/favgreen.png');
		   		
			} else if(data == "busy") {
			$("#mycoolstuff").css("background-color", "darkred");
			favicon.change('/favred.png');
			}
		}).fail(function() {
			$("#mycoolstuff").css("background-color", "gray");
			favicon.change('/favgray.png');
		});
	}
});
