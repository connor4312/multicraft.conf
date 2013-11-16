$ () ->
	$('#js-previewgen').on 'click', (e) ->

		$form = $('#js-generateform')

		$form.ajaxSubmit
			url: $(this).attr('data-url')
			type: 'POST'
			success: (data) ->
				$('pre', $form).remove()
				$el = $('<pre />')
				$el.html(data).appendTo($form)

				$('body').animate
					scrollTop: $('pre', $form).position().top

		return false; 
