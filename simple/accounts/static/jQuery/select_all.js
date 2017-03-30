$(document).ready(function(){
	$('#select_all').click(function(){
		$('input:checkbox').not(this).prop('checked', this.checked);
	});
});