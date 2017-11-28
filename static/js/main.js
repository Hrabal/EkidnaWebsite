$(document).ready(function() {
	$('.bigLetter').hover(function() {
		$(this).find(".menuItem").slideToggle("slow");
	});
	$('.menuItem').click(function() {
		$('#title').animate({
			marginTop: "0vh"
		}, 1000);
	});
});