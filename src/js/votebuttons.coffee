$ () ->
	$('#js-votebuttons button').on 'click', () ->

		$.ajax
			url: $(@).attr('data-url')
			type: 'POST'
			success: (data) =>
				if data is 'OK'
					$(@).html('Vote Recorded')
					$('#js-votebuttons button').attr('disabled', 'true')

					$inc = $ $(@).attr('data-increment')
					$inc.html parseInt($inc.html(), 10) + 1
				else
					alert(data);