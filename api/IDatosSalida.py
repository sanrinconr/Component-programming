import sys

sys.path.append("Api.zip")
from Cargador import Cargador


class IDatosSalida:
    def validarUsuario(usuario, contrasena):
        baseDatos = Cargador.getInstancia("baseDatos")
        if baseDatos != None:
            instancia = baseDatos()
            salida = instancia.iniciar_sesion(usuario, contrasena)
            # print(salida)
            return salida
        else:
            return None
