$( document ).ready(function() {

	$("button").click(function(){
		$.get("occupation", function(data, status){
			alert("Data: " + data + "\nStatus: " + status);
		});
	});

});
