
$(document).ready(function(){

$('#ACTUALIZAR').css({"pointer-events":"none"});
});


/*--------------------------------------------*/
function mostrar_pie_chart()
{
	var op="mostrar_pie"
	var parametros={
		op:op
	}
    $.ajax({
           url: '/grafica',
					 data: parametros,
					 type: 'POST',
           success: function(datos){
						var obj = jQuery.parseJSON(datos);
						 $('#pie_chart').html(obj)


					},
					error: function(error){
						console.log(error);
					}
        })
        return false;
}


//-----------------------------------------------------------------//

function mostrar_persona()
{
	var op="mostrar"
	var parametros={
		op:op
	}
    $.ajax({
           url: '/proceso',
					 data: parametros,
					 type: 'POST',
           success: function(datos){
						var obj = jQuery.parseJSON(datos);
						 console.log(obj)
console.log(typeof(obj))
						 $('#example').DataTable( {
    			 		data: obj
							} );


					},
					error: function(error){
						console.log(error);
					}
        })
        return false;
}

//------------------------------------------------------------------//
function guardar_datos()
{
 
	var nombres=$("#nombres").val();
	var apellidoP=$("#apellidoP").val();
	var apellidoM=$("#apellidoM").val();
	var direccion=$("#direccion").val();
	var id_cargo=$("#cargo option:selected").val();
	var condicion="agregar"

	//------------------------------------------//
 

//--Almacenamos todos variables y parametros en un diccionario----//
	var parametros={
		nombres:nombres,
		apellidoP: apellidoP,
		apellidoM: apellidoM,
		direccion: direccion,
		id_cargo:id_cargo,
		op:condicion
	}
	console.log(parametros)
	//-----------------------------------------------//

	$.ajax({
		url: '/proceso',
		data: parametros,
		type: 'POST',
		success: function(datos){
			alert('successful process')
			mostrar_persona()
			setTimeout(function () {
  window.location.href = "/";
}, 1000);
			

		},
		error: function(error){
			console.log(error);
		}
	});
	//--Capturamos los valores de entrada en dinamico---//
	

}


function actualizar_datos()
{
	var id_tra=$("#ID_IND").val(); 	
	var nombres=$("#nombres").val();
	var apellidoP=$("#apellidoP").val();
	var apellidoM=$("#apellidoM").val();
	var direccion=$("#direccion").val();
	var id_cargo=$("#cargo option:selected").val();
	var condicion="actualizar"

	//------------------------------------------//
 

//--Almacenamos todos variables y parametros en un diccionario----//
	var parametros={
		id_tra:id_tra,
		nombres:nombres,
		apellidoP: apellidoP,
		apellidoM: apellidoM,
		direccion: direccion,
		id_cargo:id_cargo,
		op:condicion
	}

		$.ajax({
		url: '/proceso',
		data: parametros,
		type: 'POST',
		success: function(datos){
			mostrar_persona()
			setTimeout(function () {
  window.location.href = "/";
}, 1000);
		},
		error: function(error){
			console.log(error);
		}
	});


}

function nuevo()
{

setTimeout(function () {
  window.location.href = "/";
}, 100);

}

function setear(ID_IND)
{
	
	var op="setar"
	var parametros={
		op:op,
		ID_IND:ID_IND
	}

	$.ajax({
		url: '/proceso',
		data: parametros,
		type: 'POST',
		success: function(datos){
			arreglo=jQuery.parseJSON(datos)
			$('#GUARDAR').css({"pointer-events":"none"});
			$('#ACTUALIZAR').css({"pointer-events":"auto"});
			 $("#ID_IND").val(arreglo[0][0]);
			 $("#nombres").val(arreglo[0][1]);
			 $("#apellidoP").val(arreglo[0][2]);
			 $("#apellidoM").val(arreglo[0][3]);
			  $("#direccion").val(arreglo[0][4]);
			   $("#cargo").val(arreglo[0][5]);
			
		},
		error: function(error){
			console.log(error);
		}
	});

}

function eliminar(ID_IND)
{
	
	var op="eliminar"
	var parametros={
		op:op,
		ID_IND:ID_IND
	}

	$.ajax({
		url: '/proceso',
		data: parametros,
		type: 'POST',
		success: function(datos){
			mostrar_persona()
			setTimeout(function () {
  window.location.href = "/";
}, 1000);
		},
		error: function(error){
			console.log(error);
		}
	});

}




function removeModel() {

  
	$('#dv_grf').remove();

}

