import sys

sys.path.append("api/Api.zip")
from IDatosEntrada import IDatosEntrada
from IDatosSalida import IDatosSalida


class Core:
    def verificarReglas():
        print("Soy " + Core.__name__)

    def validarUsuario(usuario, contrasena):
        return str(IDatosSalida.validarUsuario(usuario, contrasena))

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
        )

    def eliminarMateria(nombre):
        return "No eliminada, no hay base de datos"

    def registrarUsuario(usuario, contrasena, email):
        return str(IDatosEntrada.registrarUsuario(usuario, contrasena, email))

    def getMaterias(usuario, mes):
        # print(usuario)
        # print(mes)
        lista = IDatosEntrada.getMaterias(mes, usuario)

        return lista
        """
        return [
            {
                "nombre": "Hacer mercado",
                "fechaInicio": "08/14/2020 10:20",
                "fechaFinal": "08/14/2020 10:20",
            },
            {
                "nombre": "Pagar factura",
                "fechaInicio": "08/15/2020 10:20",
                "fechaFinal": "08/15/2020 10:20",
            },
        ]
        """
