import sys

sys.path.append("Api.zip")
from Cargador import Cargador

# COMUNICACION DEL ORQUESTADOR HACIA EL CORE
class IUsuarioEntrada:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Core").validarUsuario(usuario, contrasena)

    def agregarMateria(nombre, descripcion, horaInicio, horaFinal, color):
        return Cargador.getInstancia("Core").agregarMateria(
            nombre, descripcion, horaInicio, horaFinal, color
        )

    def eliminarMateria(nombre):
        return Cargador.getInstancia("Core").eliminarMateria(nombre)

    def registrarUsuario(usuario, contrasena, email):
        return Cargador.getInstancia("Core").registrarUsuario(
            usuario, contrasena, email
        )

    def getMaterias(usuario):
        return Cargador.getInstancia("Core").getMaterias(usuario)
