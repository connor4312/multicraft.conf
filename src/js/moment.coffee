$ () ->
	$('span.js-timeago').each () ->
		$(@).html moment($(@).html(), 'YYYY-MM-DD HH:mm:ss Z').fromNow()