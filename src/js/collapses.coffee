$ () ->
	$('.collapsible').each () ->
		if $(this).attr('data-default') is 'hidden'
			$('> .js-reveal', @).hide()
		else
			$(@).addClass('active')

		$('> .js-head', this).click () =>
			$('> .js-reveal', @).stop().slideToggle()
			$(@).toggleClass('active')