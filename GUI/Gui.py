from api.IUsuarioSalida import IUsuarioSalida

# Dependencias web
from flask import Flask, render_template


class Gui:

    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template(
            "index.html"
        )

    @app.route("/iniciarSesion")
    def iniciarSesion():
        return render_template("iniciarSesion.html")

    @app.route("/registrarse")
    def registrarse():
        return render_template("registrarse.html")

    @app.route("/login/validarLogin")
    def validarUsuario(user=None, contrasena=None):
        return IUsuarioSalida.validarUsuario(user, contrasena)

    @app.route("/vistaPrincipal")
    def vistaPrincipal():
        return render_template("vistaPrincipal.html")

    def iniciar():
        Gui.app.run()
