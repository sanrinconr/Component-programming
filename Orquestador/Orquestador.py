from api.IRegla import IRegla
from api.IEntrada import IEntrada
from api.ISalida import ISalida
from api.Cargador import Cargador


class Orquestador:
    def mostrar(self):
        Cargador.importDinamico()

        if IEntrada.existeInstancia():
            IEntrada.recibirInformacion()

        if ISalida.existeInstancia():
            ISalida.desplegarInformacion()

        if IRegla.existeInstancia():
            IRegla.verificarReglas()


# Ejecucion del main, el punto de inicio en otras palabras
if __name__ == "__main__":
    orq = Orquestador()
    orq.mostrar()
