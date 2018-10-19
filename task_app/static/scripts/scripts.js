/**/$(document).ready(function() {

	/*show show_task_button*/
	$('.date_input').click(function() {
		$('#show_task_button').slideDown();
	});

	/*$('#show_task_button').click(function() {
		
		let date = $('.date_input').val();

		if (date === '' ) {
			alert('Choose some date!');
		}; 
	});*/


	/*hide add_task form*/
	$('#hide_add_task_button').click(function() {

		$('#add_task_div').slideUp();
	});

	/* reload page for set up date cookie */
/*	$('#show_tasks_button > input').click(function() {
		console.log('show button');
		location.reload(true);
	});
*/

	$('#login_input').addClass('login_input');


});