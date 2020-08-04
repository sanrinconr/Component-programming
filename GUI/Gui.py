from api.IUsuarioSalida import IUsuarioSalida

# Dependencias web
from flask import Flask, render_template

# Usado para manejar peticiones GET
from flask import request

# Para hacer mas entendibles las salidas de la app
from flask import jsonify


class Gui:

    app = Flask(__name__)

    ######VISTAS#############################
    #########################################3
    #########################################
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
        return render_template("vistaPrincipal.html")

    ###########################################################
    ##################################LOGICA###################
    ###########################################################

    # Se le pide al orquestador que valide al usuario
    @app.route("/login/validarLogin")
    def validarUsuario(user=None, contrasena=None):
        user = request.args.get("usuario")
        contrasena = request.args.get("contrasena")
        valido = str(IUsuarioSalida.validarUsuario(user, contrasena))
        salida = {"usuario": user, "valido": valido}
        return jsonify(salida)

    # Se le pide al orquestador que agrege una nueva materia
    @app.route("/vistaPrincipal/agregarMateria")
    def agregarMateria(nombre=None, descripcion=None, horaInicio=None, horaFinal=None):
        nombre = request.args.get("nombre")
        descripcion = request.args.get("descripcion")
        horaInicio = request.args.get("horaInicio")
        horaFinal = request.args.get("horaFinal")
        seAgrego = str(
            IUsuarioSalida.agregarMateria(nombre, descripcion, horaInicio, horaFinal)
        )
        salida = {
            "nombre": nombre,
            "descripcion": descripcion,
            "horaInicio": horaInicio,
            "horaFinal": horaFinal,
            "agregada": seAgrego,
        }
        return jsonify(salida)

    # Punto de entrada
    def iniciar():
        Gui.app.run(debug=True)
