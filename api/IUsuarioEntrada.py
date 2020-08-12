import sys

sys.path.append("Api.zip")
from Cargador import Cargador

# COMUNICACION DEL ORQUESTADOR HACIA EL CORE
class IUsuarioEntrada:
    def validarUsuario(usuario, contrasena):
        clase = Cargador.getInstancia("Core")
        if clase != None:
            return clase.validarUsuario(usuario, contrasena)
        else:
            return None

    def agregarMateria(
        nombre,
        descripcion,
        anioInicio,
        mesInicio,
        diaInicio,
        horaInicio,
        minutoInicio,
        segundoInicio,
        anioFinal,
        mesFinal,
        diaFinal,
        horaFinal,
        minutoFinal,
        segundoFinal,
    ):
        clase = Cargador.getInstancia("Core")
        if clase != None:
            return clase.agregarMateria(
                nombre,
                descripcion,
                anioInicio,
                mesInicio,
                diaInicio,
                horaInicio,
                minutoInicio,
                segundoInicio,
                anioFinal,
                mesFinal,
                diaFinal,
                horaFinal,
                minutoFinal,
                segundoFinal,
            )
        else:
            return None

    def eliminarMateria(usuario, nombre):
        clase = Cargador.getInstancia("Core")
        if clase != None:
            return clase.eliminarMateria(usuario, nombre)
        else:
            return None

    def registrarUsuario(usuario, contrasena, email):
        clase = Cargador.getInstancia("Core")
        if clase != None:
            return clase.registrarUsuario(usuario, contrasena, email)
        else:
            return None

    def getMaterias(usuario, mes):
        clase = Cargador.getInstancia("Core")
        if clase != None:
            return clase.getMaterias(usuario, mes)
        else:
            return None
