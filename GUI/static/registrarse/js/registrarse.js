$(function() {
    $( "#btnRegistrarse" ).click(function() {
    $.ajax({
      url: '/login/registrarUsuario',
      type: 'GET',
      data: {usuario: $("#inputNombreRegistro").val(),
            contrasena:$("#inputContrasenaRegistro").val(),
            email:$("#inputEmailRegistro").val(),
            },
      success: function(data) {
    	if(data.registrado == "True"){
        alert("registrado!")
      }else{
        alert(data.usuario +"\n"+data.email+"\n" +data.registrado)
      }
      //Dependiendo de lo que salga aqui toca redireccionar o no

      },
      error: function(e) {
    	//called when there is an error
    	//console.log(e.message);
      }
    });
  });
});
