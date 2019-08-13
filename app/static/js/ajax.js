$( document ).ready(function() {
	$("#btn").click(
		function sendAjaxForm() {

			//validation
			var values = {};
			$.each($('#ajax_form').serializeArray(), function(i, field) {
				values[field.name] = field.value;
			});
			var my_num = values["number"]

			if (!/^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$/.test(my_num)){
				$('#result_form').html('Please print correct number');
				return false;
			}

			//send request
			$.ajax({
				url: window.location.href,
				type: "POST",
				dataType: "html",
				data: $("#ajax_form").serialize(),
				success: function () {
					$('#number').val('');
					$('#result_form').html('Done');
				},
				error: function () {
					$('#result_form').html('Error. Try again');
				}
			});
		})
})
