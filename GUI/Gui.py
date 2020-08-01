from api.IUsuarioSalida import IUsuarioSalida

# Dependencias web
from flask import Flask, render_template


class Gui:

    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template(
            "inde.html", variables=["a1", "a2", Gui.validarUsuario("a", "a")]
        )

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/login/validarLogin")
    def validarUsuario(user=None, contrasena=None):
        return IUsuarioSalida.validarUsuario(user, contrasena)

    def iniciar():
        Gui.app.run()
