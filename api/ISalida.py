import sys

sys.path.append("Api.zip")
from Cargador import Cargador


class ISalida:
    def desplegarInformacion():
        Cargador.getInstancia("Gui").desplegarInformacion()

    def iniciarGui():
        Cargador.getInstancia("Gui").extraerNecesarios()
        Cargador.getInstancia("Gui").iniciar()

    def existeInstancia():
        if Cargador.getInstancia("Gui") != None:
            return True
        else:
            return False
