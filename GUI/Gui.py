# Dependencias web
from flask import Flask, render_template


class Gui:

    app = Flask(__name__)

    @app.route("/")
    def holis():
        return render_template("pruebilla.html", variables=["a1", "a2"])

    def iniciar():
        Gui.app.run()
