from api.Cargador import Cargador

##COMUNICACION DE LA GUI HACIA EL ORQUESTADOR
class IUsuarioSalida:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Orquestador").validarUsuario(usuario, contrasena)

    def agregarMateria(nombre, descripcion, horaInicio, horaFinal):
        return Cargador.getInstancia("Orquestador").agregarMateria(
            nombre, descripcion, horaInicio, horaFinal
        )

    def eliminarMateria(nombre):
        return Cargador.getInstancia("Orquestador").agregarMateria(nombre)
