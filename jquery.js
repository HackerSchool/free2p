
const POLL_INTERVAL = 2000; // in milliseconds

$( document ).ready(function() {

	checkOccupation();
	setInterval(function () {checkOccupation()}, POLL_INTERVAL);

	function checkOccupation() {
		$.get("occupation", function(data){
			if(data == "free") {
				$("#status-light").css("background-color", "limegreen");
			} else if(data == "busy") {
				$("#status-light").css("background-color", "red");
			}
		}).fail(function() {
			$("#status-light").css("background-color", "lightgray");
		});
	}
});
