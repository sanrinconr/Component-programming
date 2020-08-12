import sys

sys.path.append("Api.zip")
from Cargador import Cargador


class ISalida:
    def desplegarInformacion():
        clase = Cargador.getInstancia("Gui")
        if clase != None:
            clase.desplegarInformacion()
        else:
            pass

    def iniciarGui():
        clase = Cargador.getInstancia("Gui")
        if clase != None:
            clase.extraerNecesarios()
            clase.iniciar()
        else:
            pass

    def existeInstancia():
        if Cargador.getInstancia("Gui") != None:
            return True
        else:
            return False
