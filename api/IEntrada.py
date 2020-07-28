from api.Cargador import Cargador


class IEntrada:
    def recibirInformacion():
        Cargador.getInstancia("Gui").recibirInformacion()

    def existeInstancia():
        if Cargador.getInstancia("Gui") != None:
            return True
        else:
            return False
