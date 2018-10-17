function initDateFields () {
	$('.dateinput').datetimepicker({

		'format': 'YYYY-MM-DD'
                   
	}).on('dp.hide', function(event) {
		$(this).blur();
	});
}

$(document).ready(function() {
	initDateFields();
});