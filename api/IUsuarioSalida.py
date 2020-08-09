import sys

sys.path.append("Api.zip")
from Cargador import Cargador

##COMUNICACION DE LA GUI HACIA EL ORQUESTADOR
class IUsuarioSalida:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Orquestador").validarUsuario(usuario, contrasena)

    def agregarMateria(nombre, descripcion, horaInicio, horaFinal, color):
        return Cargador.getInstancia("Orquestador").agregarMateria(
            nombre, descripcion, horaInicio, horaFinal, color
        )

    def eliminarMateria(nombre):
        return Cargador.getInstancia("Orquestador").eliminarMateria(nombre)

    def registrarUsuario(usuario, contrasena, email):
        return Cargador.getInstancia("Orquestador").registrarUsuario(
            usuario, contrasena, email
        )

    def getMaterias(usuario):
        return Cargador.getInstancia("Orquestador").getMaterias(usuario)
