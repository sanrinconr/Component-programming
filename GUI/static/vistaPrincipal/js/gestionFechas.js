//Cuando esta todo cargado se ejecuta esta parte del script
$(function(){
  var fecha = new Date()
  setMesCalendario(fecha.getMonth())
  llenarColumnaInicial(fecha.getMonth(), fecha.getYear())
})

//Actualizar el texto del mes mostrado en el calendario
function setMesCalendario(nombre){
  let meses = ["Enero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
  $("#mesActual").replaceWith("<h3 id=\"mesActual\">"+ meses[nombre-1]+ "</h3>")
}
//Funcion encargada de llenar las otras columnas mas bajas
function __llenarDias(inicio){
  let contador = inicio
  let hoy = new Date()
  let diasDelMes = function(month,year) {
         return new Date(year, month, 0).getDate();
      };
  $('.diaMes').each(function(){
    if(contador<=diasDelMes(hoy.getMonth(), hoy.getYear())){
      $(this).find('span').text(contador)
      contador+=1
    }else{
      return false;
    }
  });
}
//Funcion encargada de calcula en que dia empezara el dia 1, y luego llena los demas
function llenarColumnaInicial(mes, anio){
  console.log(mes+":::::"+anio)
  let dias = ["lunes","martes","miercoles","jueves","viernes","sábado","domingo"]
  let contador = 1
  var diaInicio = getDayName(1, mes-1, anio)
  let dondeEmpezar
  for (i in dias){
    if(dias[i] == diaInicio){
      console.log(i)
      dondeEmpezar=contador
      break;
    }
    contador+=1
  }
  contador = 1
  var diaActual = 1
  $('.diaPrimeraCol').each(function(){
    if(contador >= dondeEmpezar){
      $(this).find('span').text(diaActual)
      diaActual+=1
    }
    contador+=1
  });
  console.log("conta:"+diaActual)
  __llenarDias(diaActual)

}

//Obtener el nombre de un numero de dia
function getDayName(dia,mes,anio, locale)
{
    var date = new Date(dia+"/"+mes+"/"+anio);
    return date.toLocaleDateString(locale, { weekday: 'long' });
}
