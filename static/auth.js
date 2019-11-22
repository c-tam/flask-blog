// delete user
$(document).ready(function(){
	$(".deleteuser").on("click", function(){
		var userId = $(this).attr("user_id")
		if (confirm("Delete User #"+userId +"?")) {
            console.log("deleteevenmt");
			$.ajax({
				url: "/_deleteuser",
                type: "POST",
                contentType: "application/json",
                dataType: 'json',
				data: JSON.stringify({id: userId})
			})
            .done(function(data) {
                if (data.message) {
                    $('#main-content').html($(data).find('#main-content').html());
                    $('#alert').show();
                    $('#alert #alert-text').text(data.message);	
                }
            });
		} 
	});
});

//change user password
$(document).ready(function(event){
	$(".newpass").on("click", function(){
        var userId = $(this).attr("user_id")
        var password = document.getElementById("newpass"+userId).value;
        if (!password){
            $('#alert').show();
            $('#alert #alert-text').text("Enter a password");
        } else {
            $('#alert').hide();
            if (confirm("Change User #"+userId +"'s password?")) {
                $.ajax({
                    url: "/blog/edituser",
                    type: "POST",
                    contentType: "application/json",
                    dataType: 'json',
                    data: JSON.stringify({id: userId, password: password})
                })
                .done(function(data) {
                    if (data.message) {
                        $('#main-content').html($(data).find('#main-content').html());;
                        document.getElementById("newpass"+userId).value = "";
                        $('#alert').show();
                        $('#alert #alert-text').text(data.message); 	
                    }
                });
            }	
        }
    
	});
});