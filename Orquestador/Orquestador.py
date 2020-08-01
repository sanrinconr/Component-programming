from api.ISalida import ISalida
from api.IUsuarioEntrada import IUsuarioEntrada

from api.Cargador import Cargador


class Orquestador:
    def mostrar(self):
        #Cargador.test()
        Cargador.importDinamico()
        ISalida.iniciarGui()

    def validarUsuario(usuario, contrasena):
        return IUsuarioEntrada.validarUsuario(usuario, contrasena)


# Ejecucion del main, el punto de inicio en otras palabras
if __name__ == "__main__":
    orq = Orquestador()
    orq.mostrar()
