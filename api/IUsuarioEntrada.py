from api.Cargador import Cargador

# COMUNICACION DEL ORQUESTADOR HACIA EL CORE
class IUsuarioEntrada:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Core").validarUsuario(usuario, contrasena)

    def agregarMateria(nombre, descripcion, horaInicio, horaFinal):
        return Cargador.getInstancia("Core").agregarMateria(
            nombre, descripcion, horaInicio, horaFinal
        )

    def eliminarMateria(nombre):
        return Cargador.getInstancia("Core").eliminarMateria(nombre)
