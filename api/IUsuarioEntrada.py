import sys

sys.path.append("Api.zip")
from Cargador import Cargador

# COMUNICACION DEL ORQUESTADOR HACIA EL CORE
class IUsuarioEntrada:
    def validarUsuario(usuario, contrasena):
        return Cargador.getInstancia("Core").validarUsuario(usuario, contrasena)

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
        return Cargador.getInstancia("Core").agregarMateria(
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
        return Cargador.getInstancia("Core").eliminarMateria(nombre)

    def registrarUsuario(usuario, contrasena, email):
        return Cargador.getInstancia("Core").registrarUsuario(
            usuario, contrasena, email
        )

    def getMaterias(usuario, mes):
        return Cargador.getInstancia("Core").getMaterias(usuario, mes)
