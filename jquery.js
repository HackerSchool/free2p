const POLL_PERIOD = 5000; // in milliseconds

function changeFavicon(src {
	var link = document.createElement('link'),
		oldLink = document.getElementById('dynamic-favicon');
	link.id = 'dynamic-favicon';
	link.rel = 'icon';
	link.href = src;
	toggled = !toggled;
	if (oldLink) {
	 document.head.removeChild(oldLink);
	}
	document.head.appendChild(link);
}

$( document ).ready(function() {

	checkOccupation();
	setInterval(function () {checkOccupation()}, POLL_PERIOD);

	function checkOccupation() {
		$.get("occupation", function(data){
			if(data == "free") {
				$("#status-light").css("background-color", "limegreen");
				function() {
		    		changeFavicon('/favgreen.png');
		   		};
			} else if(data == "busy") {
				$("#status-light").css("background-color", "red");
				function() {
		    		changeFavicon('/favred.png');
		   		};
			}
		}).fail(function() {
			$("#status-light").css("background-color", "lightgray");
			function() {
		    		changeFavicon('/favblack.png');
		   		};
		});
	}
});
