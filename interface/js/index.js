$(document).ready(function(){
	$("#menu-toggle").on('click',function(){
		$("#menu-toggle").toggleClass("active");
		$('#theMenu').toggleClass('menu-open');
	});
});