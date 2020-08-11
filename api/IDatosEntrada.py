import sys

sys.path.append("Api.zip")
from Cargador import Cargador


class IDatosEntrada:
    def registrarUsuario(usuario, contrasena, email):
        clase = Cargador.getInstancia("baseDatos")
        instancia = clase()
        return instancia.ingresar_Estudiante(usuario, "NA", "NA", contrasena, email)

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
        clase = Cargador.getInstancia("baseDatos")
        instancia = clase()

        return instancia.ingresar_actividad(
            "n",
            nombre,
            descripcion,
            int(anioInicio),
            int(mesInicio),
            int(diaInicio),
            int(horaInicio),
            int(minutoInicio),
            int(segundoInicio),
            int(anioFinal),
            int(mesFinal),
            int(diaFinal),
            int(horaFinal),
            int(minutoFinal),
            int(segundoFinal),
            1,
        )
