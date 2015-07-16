var POLL_PERIOD = 2000; // in milliseconds

$( document ).ready(function() {

	checkOccupation();
	setInterval(function () {checkOccupation();}, POLL_PERIOD);

	function checkOccupation() {
		$.get("occupation", function(data){
			if(data == "free") {
				$("#status-light").css("background-color", "limegreen");
				favicon.change('/favgreen.png');
		   		
			} else if(data == "busy") {
				$("#status-light").css("background-color", "red");
				favicon.change('/favred.png');
			}
		}).fail(function() {
			$("#status-light").css("background-color", "lightgray");
			favicon.change('/favblack.png');
		});
	}
});
