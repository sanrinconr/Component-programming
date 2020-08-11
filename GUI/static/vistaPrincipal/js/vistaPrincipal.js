$(function(){
  // DateTime picker for Dates
  $( "#btnAnadirEvento" ).click(function() {
    var $datepickerInicio = $('#datepickerInicio').datepicker();
    var $timepickerInicio = $('#timepickerInicio').timepicker();
    var $datepickerFinal = $('#datepickerFinal').datepicker();
    var $timepickerFinal = $('#timepickerFinal').timepicker();

    let fechaInicio = parseDate($datepickerInicio.val()+" "+$timepickerInicio.val())
    let fechaFinal = parseDate($datepickerFinal.val()+" "+$timepickerFinal.val())
    console.log(fechaFinal.getHours())
    $.ajax({
      url: '/vistaPrincipal/agregarMateria',
      type: 'GET',
      dataType : 'json',
      data: {nombre: $("#inputNombreMateria").val(),
            descripcion:$("#inputDescripcionMateria").val(),
            anioInicio:fechaInicio.getYear()+1900,
            mesInicio:fechaInicio.getMonth()+1,
            diaInicio:fechaInicio.getDay(),
            horaInicio:fechaInicio.getHours(),
            minutoInicio:fechaInicio.getMinutes(),
            segundoInicio:fechaInicio.getSeconds(),
            anioFinal:fechaFinal.getYear()+1900,
            mesFinal:fechaFinal.getMonth()+1,
            diaFinal:fechaFinal.getDay(),
            horaFinal:fechaFinal.getHours(),
            minutoFinal:fechaFinal.getMinutes(),
            segundoFinal:fechaFinal.getSeconds(),
            },
      success: function(data) {
        console.log(data)
      },
      error: function(e) {
      //called when there is an error
      //console.log(e.message);
      }
    });
  });

  $( "#btnCerrarSesion" ).click(function() {
    $.ajax({
      url: '/vistaPrincipal/cerrarSesion',
      type: 'GET',
      success: function(data) {
      //called when successful
      alert("Sesion cerrada")
      location.href = '/';
      //Dependiendo de lo que salga aqui toca redireccionar o no

      },
      error: function(e) {
      //called when there is an error
      //console.log(e.message);
      }
    });
  });
  $( "#btnSubirMateria" ).click(function() {
    $.ajax({
      url: '/vistaPrincipal/agregarMateria',
      type: 'GET',
      data: {nombre: $("#inputNombreMateria").val(),
            descripcion:$("#inputDescripcionMateria").val(),
            horaInicio:$("#inputHoraInicio").val(),
            horaFinal:$("#inputHoraFinal").val(),
            color:$("#inputColor").children("option:selected").val(),
            },
      success: function(data) {
      //called when successful
      alert(data.nombre+"\n"+data.descripcion +"\n" +data.agregada+"\n"+data.color)
      //Dependiendo de lo que salga aqui toca redireccionar o no

      },
      error: function(e) {
      //called when there is an error
      //console.log(e.message);
      }
    });
  });

  $( "#btnGetMaterias" ).click(function() {
    $.ajax({
      url: '/vistaPrincipal/getMaterias',
      type: 'GET',
      dataType : 'json',
      success: function(data) {
        alert(JSON.stringify(data))
        console.log(data)
      },
      error: function(e) {
      //called when there is an error
      //console.log(e.message);
      }
    });
  });
  eliminarSesionBarra()

});

function eliminarSesionBarra(){
  $("#elementoIniciarSesion").remove()
  $("#elementoRegistrarse").remove()

}
function parseDate(str1){
  console.log("FECHA ENTRADA: "+str1)
  // str1 format should be dd/mm/yyyy. Separator can be anything e.g. / or -. It wont effect
var mon1   = parseInt(str1.substring(0,2));
var dt1  = parseInt(str1.substring(3,5));
var yr1   = parseInt(str1.substring(6,10));
var hora = parseInt(str1.substring(11,13));
var minuto = parseInt(str1.substring(14,16));

var date1 = new Date(yr1, mon1-1, dt1, hora, minuto);
console.log("FECHA FORMATEADA")
console.log("MES: "+date1.getMonth())
console.log("DIA: "+date1.getDay())
console.log("ANIO: "+date1.getYear())

return date1;
}
