$(document).ready(function() {
	$('.bigLetter').hover(function() {
		$(this).find(".menuItem").slideToggle("slow");
		$(this).toggleClass('red')
	});
	$('.menuItem').click(function() {
		var link = $(this).attr("link");
		$('#title').animate({
			marginTop: "0vh"
		}, 1000);
		$.get(link, function(data) {
			$("#content").html(data)
		});
	});
});