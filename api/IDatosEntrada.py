import sys

sys.path.append("Api.zip")
from Cargador import Cargador


class IDatosEntrada:
    def registrarUsuario(usuario, contrasena, email):
        clase = Cargador.getInstancia("baseDatos")
        instancia = clase()
        return instancia.ingresar_Estudiante(usuario, "NA", "NA", contrasena, email)
