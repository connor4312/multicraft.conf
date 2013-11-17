$ () ->
	$("select").each () ->
		$(@).selectpicker
			style: $(@).attr('data-style') ? 'btn-default'
			menuStyle: $(@).attr('data-menuStyle') ? 'dropdown-inverse'

	$("input, textarea").placeholder();
	$("[data-toggle='switch']").wrap('<div class="switch" />').parent().bootstrapSwitch();