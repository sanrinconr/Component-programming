import sys

sys.path.append("Api.zip")
from Cargador import Cargador

##COMUNICACION DE LA GUI HACIA EL ORQUESTADOR
class IUsuarioSalida:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Orquestador").validarUsuario(usuario, contrasena)

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
        return Cargador.getInstancia("Orquestador").agregarMateria(
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

    def eliminarMateria(nombre):
        return Cargador.getInstancia("Orquestador").eliminarMateria(nombre)

    def registrarUsuario(usuario, contrasena, email):
        return Cargador.getInstancia("Orquestador").registrarUsuario(
            usuario, contrasena, email
        )

    def getMaterias(usuario, mes):
        return Cargador.getInstancia("Orquestador").getMaterias(usuario, mes)
