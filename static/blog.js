function addDeleteEvent() {
	var buttons = document.querySelectorAll('#blog-container .deletepost');
	for (var button of buttons) {
		$(button).on("click", deletePost);
	}
}
addDeleteEvent()

function deletePost(event) {
	var postId = event.currentTarget.id
	if (confirm("Delete Post #"+postId +"?")) {
		$.ajax({
			url: "/_delete",
			type: "POST",
			contentType: "application/json",
			dataType: 'json',
			data: JSON.stringify({id: postId}),
		})
		.done(function(data) {
			if (data.message) {
                $.ajax({
                    url:blogUrl,
                    type:'GET',
                    success: function(data){
                        $('#blog-container').html($(data).find('#blog-container').html());
                        addDeleteEvent();
                        $('#alert').show();
				        $('#alert #alert-text').text("Deleted post");
                    }
                 });
			}
	});
	event.preventDefault();
	} 
}

$(document).ready(function(){
	$('#addForm').on('submit', function(event) {
		$.ajax({
			data: JSON.stringify({
				title : $('#title').val(),
				author : $('#author').val(),
				content: $('#content').val(),
				tag: tags
			}),
			type : 'POST',
			url : '/blog/add',
			contentType: "application/json",
			dataType: 'json'
		})
		.done(function(data) {
			if (data.error == true) {
				$('#alert').show();
				$('#alert #alert-text').text(data.message);
			}
			else {
				$('#alert').show();
				$('#alert #alert-text').text("Success");
				document.getElementById("addForm").reset();
				clearTags();
			}
		});
		event.preventDefault();
	});
});
