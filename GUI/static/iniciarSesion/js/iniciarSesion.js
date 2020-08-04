/*$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});*/
$(function() {
    $( "#btnLogin" ).click(function() {
    $.ajax({
      url: '/login/validarLogin',
      type: 'GET',
      data: {user: "test",
            contrasena:"test"
            },
      success: function(data) {
    	//called when successful
    	alert(data.valido)
      //Dependiendo de lo que salga aqui toca redireccionar o no
  
      },
      error: function(e) {
    	//called when there is an error
    	//console.log(e.message);
      }
    });
  });
});
