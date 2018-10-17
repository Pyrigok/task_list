function initTaskSelector() {

	$('table tr').click(function(event) {

		/*find current choose task*/
		var task_detail = $(this).find('input').val();

		if (task_detail) {

			/*create cookie named 'current_task' and pass task.id named 'task_detail'*/
			$.cookie('current_task', task_detail, {'path': '/', 'expires': 365});
		} else {
			$.removeCookie('current_task', {'path': '/'});
		}
		location.reload(true);
		return true;
	});
}

/*function initDateSelector() {
	$('#date_row  #date_div').click(function(event) {

		var spec_date = $(this).find('input').val();

		if (spec_date) {
			$.cookie('specific_date', spec_date, {'path': '/', 'expires': 365});
		} else {
			$.removeCookie('specific_date', {'path': '/'})
		}
		location.reload(true);
		return true;
	});
}*/

$(document).ready(function() {
	initTaskSelector();
	/*initDateSelector();*/
});