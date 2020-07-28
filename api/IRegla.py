from api.Cargador import Cargador


class IRegla:
    def verificarReglas():
        Cargador.getInstancia("Core").verificarReglas()

    def existeInstancia():
        if Cargador.getInstancia("Core") != None:
            return True
        else:
            return False
