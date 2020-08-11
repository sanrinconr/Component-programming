import sys

##Se establece que va a importar del zip
sys.path.append("api/Api.zip")
from ISalida import ISalida
from IUsuarioEntrada import IUsuarioEntrada
from IDatosEntrada import IDatosEntrada
from Cargador import Cargador


class Orquestador:
    def mostrar(self):
        # Cargador.test()
        Cargador.importDinamico()
        ISalida.iniciarGui()

    def validarUsuario(usuario, contrasena):
        return IUsuarioEntrada.validarUsuario(usuario, contrasena)

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
        return IDatosEntrada.agregarMateria(
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

    def eliminarMateria(nombre):
        return IUsuarioEntrada.eliminarMateria(nombre)

    def registrarUsuario(usuario, contrasena, email):
        return IUsuarioEntrada.registrarUsuario(usuario, contrasena, email)

    def getMaterias(usuario, mes):
        return IUsuarioEntrada.getMaterias(usuario, mes)


# Ejecucion del main, el punto de inicio en otras palabras
if __name__ == "__main__":
    orq = Orquestador()
    orq.mostrar()
