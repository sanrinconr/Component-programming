$(function(){
  obtenerDatos("8")

  // DateTime picker for Dates
  $( "#btnAnadirEvento" ).click(function() {
    var $datepickerInicio = $('#datepickerInicio').datepicker();
    var $timepickerInicio = $('#timepickerInicio').timepicker();
    var $datepickerFinal = $('#datepickerFinal').datepicker();
    var $timepickerFinal = $('#timepickerFinal').timepicker();

    let fechaInicio = parseDate($datepickerInicio.val()+" "+$timepickerInicio.val())
    let fechaFinal = parseDate($datepickerFinal.val()+" "+$timepickerFinal.val())
    $.ajax({
      url: '/vistaPrincipal/agregarMateria',
      type: 'GET',
      dataType : 'json',
      data: {nombre: $("#inputNombreMateria").val(),
            descripcion:$("#inputDescripcionMateria").val(),
            anioInicio:fechaInicio.getYear()+1900,
            mesInicio:fechaInicio.getMonth()+1,
            diaInicio:fechaInicio.getDate(),
            horaInicio:fechaInicio.getHours(),
            minutoInicio:fechaInicio.getMinutes(),
            segundoInicio:fechaInicio.getSeconds(),
            anioFinal:fechaFinal.getYear()+1900,
            mesFinal:fechaFinal.getMonth()+1,
            diaFinal:fechaFinal.getDate(),
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
        __actualizarCalendario(data,mes)
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
  console.log("FECHAENTRADA"+str1)
  // str1 format should be dd/mm/yyyy. Separator can be anything e.g. / or -. It wont effect
var mon1   = parseInt(str1.substring(0,2));
var dt1  = parseInt(str1.substring(3,5));
var yr1   = parseInt(str1.substring(6,10));
var hora = parseInt(str1.substring(11,13));
var minuto = parseInt(str1.substring(14,16));
console.log("FECHASALIDA")
console.log("mes: "+mon1)
console.log("dia: "+dt1)
console.log("anio: "+yr1)

var date1 = new Date(yr1, mon1-1, dt1, hora, minuto);

return date1;
}
function getDia(str1){
  // str1 format should be dd/mm/yyyy. Separator can be anything e.g. / or -. It wont effect
var dt1  = parseInt(str1.substring(3,5));

return dt1;
}
function obtenerDatos(m){
  $.ajax({
    url: '/vistaPrincipal/getMaterias',
    type: 'GET',
    dataType : 'json',
    data: {mes: m,
    },
    success: function(data) {
      console.log(data)

     for (var i = 0 ; i<data.length ; i++){
        graficar(data[i].nombre, sqlToJs(data[i].fechaInicio).getDate())
      }
    },
    error: function(e) {
    //called when there is an error
    //console.log(e.message);
    }
  });
}
function graficar(nombre,dia){
  $('.dia').each(function(){
    if($(this).find('.numero').find("span").text() == dia.toString()){
      $(this).find('.eventos').append(nombre)
    }
  });
}
function sqlToJs(fechaSql) {
  var mon1   = parseInt(fechaSql.substring(5,7));
  var dt1  = parseInt(fechaSql.substring(8,10));
  var yr1   = parseInt(fechaSql.substring(0,5));
  var hora = parseInt(fechaSql.substring(11,13));
  var minuto = parseInt(fechaSql.substring(14,16));
  console.log("MES"+mon1)
  console.log("dia"+dt1)
  console.log("anio"+yr1)
  console.log("hora"+hora)
  console.log("min"+minuto)

  return new Date(yr1, mon1-1, dt1, hora, minuto);

}
