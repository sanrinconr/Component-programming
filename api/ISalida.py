from api.Cargador import Cargador


class ISalida:
    def desplegarInformacion():
        Cargador.getInstancia("Gui").desplegarInformacion()

    def iniciarGui():
        Cargador.getInstancia("Gui").iniciar()

    def existeInstancia():
        if Cargador.getInstancia("Gui") != None:
            return True
        else:
            return False
