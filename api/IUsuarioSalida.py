from api.Cargador import Cargador


class IUsuarioSalida:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Orquestador").validarUsuario(usuario, contrasena)
