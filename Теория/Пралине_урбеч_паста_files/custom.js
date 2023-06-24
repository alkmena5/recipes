$(function () {

	$('body')
		.on('click', '.article__head-likes', function (e) {
			e.preventDefault();
			var target = e.target,
				c = $(".count").html();
			if ($(target).hasClass("is-active")) {
				$(target).removeClass("is-active"); 
				$(target).text(" Запомнить статью");
				c = c-1;
				$(".count").html(c);
			} else {
				$(target).addClass("is-active");
				$(target).text(" Убрать из избранных");
				c = c-1+2;
				$(".count").html(c);
			}
            var article_id = $(target).data('article_id');
            var action = "remember"; //$(target).data('action');
            var query = 'id=' + article_id + '&action=' + action;
			var data = { action : action, id : article_id };
			$.ajax({
				url: "/baza/ajax/remember.php",
				data: data,
				dataType: "json",
			}).done(function(data){
				if (data.status === true){
					console.log("success");
				} else {
					console.log(data);
				}
			}).fail(function(err){
				console.log("error remember");
			});
		})
		.on('click', '.locked__btn', function (e) {
			window.location = '/baza/subscribes.php';
		})
	;
});
