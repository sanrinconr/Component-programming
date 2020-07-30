from api.Cargador import Cargador


class IUsuarioEntrada:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Core").validarUsuario(usuario, contrasena)
