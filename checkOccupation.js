var POLL_PERIOD = 2000; // in milliseconds

$( document ).ready(function() {

	checkOccupation();
	setInterval(function () {checkOccupation();}, POLL_PERIOD);

	function checkOccupation() {
		$.get("occupation", function(data){
			if(data == "free") {
			//	$("#status-light").css("background-color", "limegreen");
				document.body.style.background="green";
				favicon.change('/favgreen.png');
		   		
			} else if(data == "busy") {
			//	$("#status-light").css("background-color", "red");
				document.body.style.background="red";
				favicon.change('/favred.png');
			}
		}).fail(function() {
			//$("#status-light").css("background-color", "lightgray");
			document.body.style.background="lightgray";
			favicon.change('/favblack.png');
		});
	}
});
