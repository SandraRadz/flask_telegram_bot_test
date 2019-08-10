$( document ).ready(function() {
	$("#btn").click(
		function sendAjaxForm() {

			//validation
			var values = {};
			$.each($('#ajax_form').serializeArray(), function(i, field) {
				values[field.name] = field.value;
			});
			var my_num = Number(values["number"])
			if (!my_num || my_num<0){
				$('#result_form').html('Please print positive number');
				return false;
			}

			//send request
			$.ajax({
				url: window.location.href,
				type: "POST",
				dataType: "html",
				data: $("#ajax_form").serialize(),
				success: function () {
					$('#result_form').html('Done');
				},
				error: function () {
					$('#result_form').html('Error. Try again');
				}
			});
		})
})
