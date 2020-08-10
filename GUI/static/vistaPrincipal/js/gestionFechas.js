//Cuando esta todo cargado se ejecuta esta parte del script
$(function(){
  var fecha = new Date()
  setMesCalendario(fecha.getMonth())
  llenarDias()
})

//Actualizar el texto del mes mostrado en el calendario
function setMesCalendario(nombre){
  let meses = ["Enero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
  $("#mesActual").replaceWith("<h3 id=\"mesActual\">"+ meses[nombre-1]+ "</h3>")
}
function llenarDias(inicio){
  let contador = inicio
  $('.diaMes').each(function(){
    console.log("entro")
    $(this).find('span').text(contador)
    contador+=1
  });
}
function llenarColumnaInicial(){
  let dia = new Date()
  var diaInicio = getDayName(1, dia.getMonth(), dia.getYear())
  console.log(diaInicio)
}

function getDayName(dia,mes,anio, locale)
{
    var date = new Date(dia+"/"+mes+"/"+anio);
    return date.toLocaleDateString(locale, { weekday: 'long' });
}
