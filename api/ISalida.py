from api.Cargador import Cargador


class ISalida:
    def desplegarInformacion():
        Cargador.getInstancia("Gui").desplegarInformacion()

    def existeInstancia():
        if Cargador.getInstancia("Gui") != None:
            return True
        else:
            return False
