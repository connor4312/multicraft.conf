$ () ->

	beforeSubmit = ($form) ->
		data = []
		$('#js-customstable tr.js-datasource').each () ->
			insert = {}
			$('input', @).each () ->
				insert[ $(@).attr('data-name') ] = $(@).val()
			data.push insert

		content = ''
		for item in data
			content += '<input type="hidden" name="' + item.section + '_' + item.property + '" value="' + item.value + '">'

		$('#js-customadds', $form).html content

	$('#js-previewgen').on 'click', (e) ->

		$form = $('#js-generateform')
		beforeSubmit $form

		$form.ajaxSubmit
			url: $(@).attr('data-url')
			type: 'POST'
			success: (data) ->
				$('code', $form).remove()
				$el = $('<code class="language-ini" />')
				$el.html(data).appendTo($form);
				Prism.highlightAll();

				$('body').animate
					scrollTop: $('code', $form).position().top

		return false; 

	$('#js-postbutton').on 'click', (e) ->

		$form = $('#js-generateform')
		beforeSubmit $form

		$form.ajaxSubmit
			url: $(@).attr('data-url')
			type: 'POST'
			success: (data) ->
				if data is 'OK'
					$form.submit()
				else
					$('#js-errorbox').html $('<div class="alert alert-danger" />').html(data)
					$('body').animate
						scrollTop: 0

		return false; 

	$('#js-addrow').click () ->
		$el = $('<tr class="js-datasource">
			<td><input data-name="section" class="form-control" type="text" placeholder="Section"></td>
			<td><input data-name="property" class="form-control" type="text" placeholder="Property"></td>
			<td><input data-name="value" class="form-control" type="text" placeholder="Value"></td>
		</tr>');

		$el.insertBefore($(@).closest('tr'));

		return false;