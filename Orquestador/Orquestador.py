from api.IRegla import IRegla
from api.IEntrada import IEntrada
from api.ISalida import ISalida


class Orquestador:
    def mostrar(self):

        IEntrada.recibirInformacion()
        ISalida.desplegarInformacion()
        IRegla.verificarReglas()


# Ejecucion del main, el punto de inicio en otras palabras
if __name__ == "__main__":
    orq = Orquestador()
    orq.mostrar()
