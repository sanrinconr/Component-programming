$(function(){
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
