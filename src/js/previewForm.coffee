$ () ->

	$('#js-previewgen').on 'click', (e) ->

		$form = $('#js-generateform')

		$form.ajaxSubmit
			url: $(this).attr('data-url')
			type: 'POST'
			success: (data) ->
				$('code', $form).remove()
				$el = $('<code class="language-ini" />')
				$el.html(data).appendTo($form);
				Prism.highlightAll();

				$('body').animate
					scrollTop: $('code', $form).position().top

		return false; 
