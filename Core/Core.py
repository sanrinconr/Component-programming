class Core:
    def verificarReglas():
        print("Soy " + Core.__name__)

    def validarUsuario(usuario, contrasena):
        if usuario == "test" and contrasena == "test":
            return True
        ##Aqui el core hace la llamada a la DB
        return "No es posible validar, no hay base de datos"

    def agregarMateria(nombre, descripcion, horaIncio, horaFinal, color):
        return "No agregada, falta base de datos"

    def eliminarMateria(nombre):
        return "No eliminada, no hay base de datos"

    def registrarUsuario(usuario, contrasena, email):
        return "No agregado, no hay base datos :C"
