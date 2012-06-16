/**
* Modifica la categoría de un tweet
* Nota: Deshabilita el boton durante el proceso y lo habilita al terminar
**/
function changeTweetCategory(object, tweetId, categoryId)
{
	event.preventDefault();
	//Coger texto del elemento seleccionado
	var text = $(object).children('a').html();

	var button = $(object).parent().prev().children('span.dropdown-text').parent();
	var buttonText = $(object).parent().prev().children('span.dropdown-text');
	
	if(buttonText.html() != text)
	{
		//TODO: Enviar peticion AJAX para cambiar categoría
		button.addClass("disabled");
		buttonText.html("cargando...");

		$.ajax(
		{
			url: '/ajax/changeTweetCategory/'+ tweetId +'/'+ categoryId +'/',
			success: function(data)
			{
				$("#success_alert").css("display",'');
				button.removeClass("disabled");
				buttonText.html(text);
			}
		});
	}
}

function getTweetsFromTwitter(btn)
{
	$(btn).button('loading');

	$.ajax(
	{
		url: '/ajax/getTweetsFromTwitter/',
		success: function(data)
		{
			document.location.href = document.location.href;
		}
	});
}

function sendTweetResponse(author, text)
{
	//TODO: Comprobar autor en el texto y enviar tweet a través de AJAX
}

function showSendTweetResponseDialog(author, authorText)
{
	$("#modal-send-tweet-response .modal-author-username").html(author);
	$("#modal-send-tweet-response .modal-author-tweet-text").html(authorText);
	
	$('#modal-send-tweet-response').modal();
	$("#modal-response-textarea").focus();
	$("#modal-response-textarea").val(author+" ");

	$('#modal-send-tweet-response-button').click(function()
	{
		$(this).button('loading');
		$(this).addClass('disabled');
		setTimeout(function()
		{
			sendTweetResponse(author, $("#modal-response-textarea").html());
			$('#modal-send-tweet-response-button').button('reset');
			$('#modal-send-tweet-response').modal('hide');
			showAlert("Tweet enviado con éxito","alert-info");
		},1000);
	});
}

function showAlert(text, type)
{

	if(type)
		$("#alert-info").addClass(type);
	$("#alert-info").html(text);
	$("#alert-info").slideDown();

	setTimeout(function()
	{
		$("#alert-info").slideUp('normal',function()
			{
				if(type)
					$("#alert-info").removeClass(type);
			});
	},3000);
}