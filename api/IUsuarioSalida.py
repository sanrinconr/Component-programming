import sys

sys.path.append("Api.zip")
from Cargador import Cargador

##COMUNICACION DE LA GUI HACIA EL ORQUESTADOR
class IUsuarioSalida:
    def validarUsuario(usuario, contrasena):
        clase = Cargador.getInstancia("Orquestador")
        if clase != None:
            return clase.validarUsuario(usuario, contrasena)
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
        nombreUsuario,
    ):
        clase = Cargador.getInstancia("Orquestador")
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
                nombreUsuario,
            )
        else:
            return None

    def eliminarMateria(usuario, nombre):
        clase = Cargador.getInstancia("Orquestador")
        if clase != None:
            return clase.eliminarMateria(usuario, nombre)
        else:
            return None

    def registrarUsuario(usuario, contrasena, email):
        clase = Cargador.getInstancia("Orquestador")
        if clase != None:
            return clase.registrarUsuario(usuario, contrasena, email)
        else:
            return None

    def getMaterias(usuario, mes):
        clase = Cargador.getInstancia("Orquestador")
        if clase != None:
            return clase.getMaterias(usuario, mes)
        else:
            return None
