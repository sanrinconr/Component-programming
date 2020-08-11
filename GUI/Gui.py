# Dependencias web
from flask import Flask, render_template

# Usado para manejar peticiones GET
from flask import request

# Para hacer mas entendibles las salidas de la app
from flask import jsonify

# Implementacion de las sesiones
from flask import Flask, session

# redireccionar
from flask import Flask, redirect, url_for

# Gestion de zip
import zipfile

##Se establece que va a importar del zip la api
import sys
import os

sys.path.append("api/Api.zip")
from IUsuarioEntrada import IUsuarioEntrada
from IUsuarioSalida import IUsuarioSalida


class Gui:

    # Se define la ruta personalizada de las templates
    # las que se descomprimen del zip
    app = Flask(
        __name__,
        template_folder=os.path.abspath("front/__web__/GUI/templates/"),
        static_folder=os.path.abspath("front/__web__/GUI/static/"),
    )

    ################VISTAS####################
    ##########################################
    ##########################################
    # Vista de entrada, cualquiera puede verla
    @app.route("/")
    def index():
        return render_template("index.html")

    # Vista de login
    @app.route("/iniciarSesion")
    def iniciarSesion():
        return render_template("iniciarSesion.html")

    # Vista de registro
    @app.route("/registrarse")
    def registrarse():
        return render_template("registrarse.html")

    # Vista de gestion donde el usuario podra organizar su horario
    @app.route("/vistaPrincipal")
    def vistaPrincipal():
        try:
            # Se intenta obtener la variable usuario
            usuario = session["usuario"]
            return render_template("vistaPrincipal.html")
        except:
            # Si no existe entonces se retorna al login
            return redirect(url_for("iniciarSesion"))

    ###########################################################
    ##################################LOGICA###################
    ###########################################################

    ###########################################################
    ##################LOGIN###################################
    # Se le pide al orquestador que valide al usuario
    @app.route("/login/validarLogin")
    def validarUsuario(user=None, contrasena=None):
        user = request.args.get("usuario")
        contrasena = request.args.get("contrasena")
        valido = str(IUsuarioSalida.validarUsuario(user, contrasena))
        salida = {"usuario": user, "valido": valido}
        print(salida)
        if valido == "True":
            session.clear()
            session["usuario"] = user

        else:
            session.clear()
        return jsonify(salida)

    @app.route("/vistaPrincipal/cerrarSesion")
    def cerrarSesion():
        try:
            session.clear()
            return str(True)
        except:
            return str(False)

    ########################################################
    ##################REGISTRO##############################
    ########################################################

    @app.route("/login/registrarUsuario")
    def registrarUsuario(user=None, contrasena=None, email=None):
        user = request.args.get("usuario")
        contrasena = request.args.get("contrasena")
        email = request.args.get("email")
        registrado = str(IUsuarioSalida.registrarUsuario(user, contrasena, email))
        salida = {"usuario": user, "email": email, "registrado": registrado}
        if registrado == "True":
            session.clear()
            session["usuario"] = user
        else:
            session.clear()
        return jsonify(salida)

    ########################################################
    ##################GESTOR PRINCIPAL #####################
    ########################################################

    # Se le pide al orquestador que agrege una nueva materia
    @app.route("/vistaPrincipal/agregarMateria")
    def agregarMateria(
        nombre=None,
        descripcion=None,
        anioInicio=None,
        mesInicio=None,
        diaInicio=None,
        horaInicio=None,
        minutoInicio=None,
        segundoInicio=None,
        anioFinal=None,
        mesFinal=None,
        diaFinal=None,
        horaFinal=None,
        minutoFinal=None,
        segundoFinal=None,
    ):

        nombre = request.args.get("nombre")
        descripcion = request.args.get("descripcion")

        anioInicio = request.args.get("anioInicio")
        mesInicio = request.args.get("mesInicio")
        diaInicio = request.args.get("diaInicio")
        horaInicio = request.args.get("horaInicio")
        minutoInicio = request.args.get("minutoInicio")
        segundoInicio = request.args.get("segundoInicio")
        anioFinal = request.args.get("anioFinal")
        mesFinal = request.args.get("mesFinal")
        diaFinal = request.args.get("diaFinal")
        horaFinal = request.args.get("horaFinal")
        minutoFinal = request.args.get("minutoFinal")
        segundoFinal = request.args.get("segundoFinal")
        seAgrego = str(
            IUsuarioSalida.agregarMateria(
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
        )
        salida = {
            "nombre": nombre,
            "descripcion": descripcion,
            "agregada": seAgrego,
        }
        return jsonify(salida)

    # Se le pide al orquestador que elimine una materia
    @app.route("/vistaPrincipal/eliminarMateria")
    def eliminarMateria(nombre=None):
        nombre = request.args.get("nombre")
        seElimino = str(IUsuarioSalida.eliminarMateria(nombre))
        salida = {
            "nombre": nombre,
            "eliminada": seElimino,
        }
        return jsonify(salida)

    @app.route("/vistaPrincipal/getMaterias")
    def getMaterias(nombre=None):
        try:
            usuario = session["usuario"]
            resultado = IUsuarioSalida.getMaterias(usuario)

            return jsonify(resultado)
        except:
            return jsonify("Sin iniciar sesion")

    def extraerNecesarios():
        with zipfile.ZipFile("front/Gui.zip", "r") as zip_ref:
            zip_ref.extractall("front/__web__/")

    # Punto de entrada
    def iniciar():
        Gui.app.secret_key = "1234"
        Gui.app.run(debug=True)
