$(document).ready(function(){
	$("#regiones").change(function(){
		$("#regiones option:selected").each(function(){
			var region = document.formulario.regiones.options[document.formulario.regiones.selectedIndex].value
			$.ajax({
				url: 'http://localhost:8000/regional/provincia/'+region+'/',
				type: 'GET',
				datatype: 'json',
				success : function(json){
					var test = JSON.parse(json)
					$('#provincia').empty();
					$.each(test, function(i, value){
						$('#provincia').append($('<option>').text(value.nombre_provincia).attr('value',value.id));				
					});
				},
				error : function(xhr, status){
					console.log('ocurrio un error')
				}
			});
		})
	});

	$("#provincia").change(function(){
		$("#provincia option:selected").each(function(){
			console.log('ESTAMOS CARGANDO LAS COMUNAS');
		    var id_provincia = document.formulario.provincia.options[document.formulario.provincia.selectedIndex].value
		    console.log('el id de la provincia es:',id_provincia)
		    $.ajax({
		    	url: 'http://localhost:8000/regional/comuna/'+id_provincia+'/',
		    	type: 'GET',
		    	datatype: 'json',
		    	success: function(json){
		    		var data = JSON.parse(json)
		    		$('#comuna').empty();
		    		$.each(data, function(i,value){
		    			console.log(value.nombre_comuna)
		    			$('#comuna').append($('<option>').text(value.nombre_comuna).attr('value',value.id));
		    		});

		    	},
		    	error : function(xhr, status){
		    		console.log('error en comunas')
		    	}


		    });
		})
	});
})