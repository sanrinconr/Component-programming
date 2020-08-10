import sys

sys.path.append("api/Api.zip")
from IDatosEntrada import IDatosEntrada
from IDatosSalida import IDatosSalida


class Core:
    def verificarReglas():
        print("Soy " + Core.__name__)

    def validarUsuario(usuario, contrasena):
        return str(IDatosSalida.validarUsuario(usuario, contrasena))

    def agregarMateria(nombre, descripcion, horaIncio, horaFinal, color):
        return "No agregada, falta base de datos"

    def eliminarMateria(nombre):
        return "No eliminada, no hay base de datos"

    def registrarUsuario(usuario, contrasena, email):
        return "No agregado, no hay base datos :C"

    def getMaterias(usuario):
        return [
            {"nombre": "prueba1", "horaInicio": "10:20 PM", "horaFinal": "10:40 PM"},
            {"nombre": "prueba2", "horaInicio": "10:40 PM", "horaFinal": "10:59 PM"},
        ]
