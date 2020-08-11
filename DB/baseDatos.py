import pymysql
import time
from datetime import datetime


class baseDatos:
    def __init__(self):
        # Conexion a la base de datos
        self.connection = pymysql.connect(
            host="localhost", user="root", password="12345", db="fis",
        )

        self.cursor = self.connection.cursor()

    def test(self):
        return "wef"

    # Seleccionar un Estudiante
    def select_user(self, id):
        sql = "SELECT idEstudiante,Nombre FROM Estudiante WHERE idEstudiante='{}'".format(
            id
        )
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[1])

        except Exception as e:
            print(e)
            raise

    # REGISTRO DE ESTUDIANTE
    def ingresar_Estudiante(self, idEstudiante, nombre, apellido, clave, correo):
        sql = "INSERT INTO Estudiante (idEstudiante,Nombre,Apellido,Clave,Correo) VALUES (%s,%s,%s,%s,%s)"
        valores = (idEstudiante, nombre, apellido, clave, correo)
        try:
            self.cursor.execute(sql, valores)
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)

    # LOG IN
    def iniciar_sesion(self, usuario, contrasena):
        sql = "SELECT idEstudiante FROM Estudiante WHERE idEstudiante='{}' AND Clave='{}'".format(
            usuario, contrasena
        )
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            if user[0]:
                return True
            else:
                return False

        except Exception as e:
            return str(e)

    # Creacion de un nuevo horario
    def Crear_horario(self, nombre, descripcion, idEstudiante):
        sql = "INSERT INTO horario (Nombre,Descripcion,idEstudiante) VALUES (%s,%s,%s)"
        valores = (nombre, descripcion, idEstudiante)
        try:
            self.cursor.execute(sql, valores)
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)

    # Adicion de actividades
    def ingresar_actividad(
        self,
        SeRealizo,
        Nombre,
        Descripcion,
        anoI,
        mesI,
        diaI,
        HoraI,
        MinutoI,
        SegundoI,
        anoF,
        mesF,
        diaF,
        HoraF,
        MinutoF,
        SegundoF,
        idEstudiante,
    ):
        fechaI = datetime(
            year=anoI,
            month=mesI,
            day=diaI,
            hour=HoraI,
            minute=MinutoI,
            second=SegundoI,
            microsecond=0,
            tzinfo=None,
            fold=0,
        )
        fechaF = datetime(
            year=anoF,
            month=mesF,
            day=diaF,
            hour=HoraF,
            minute=MinutoF,
            second=SegundoF,
            microsecond=0,
            tzinfo=None,
            fold=0,
        )
        sql = "INSERT INTO Actividad (SeRealizo,Nombre,Descripcion,HoraInicio,HoraFin,idEstudiante) VALUES (%s,%s,%s,%s,%s,%s)"
        valores = (
            SeRealizo,
            Nombre,
            Descripcion,
            fechaI.strftime("%Y-%m-%d %H:%M:%S"),
            fechaF.strftime("%Y-%m-%d %H:%M:%S"),
            idEstudiante,
        )
        try:
            self.cursor.execute(sql, valores)
            self.connection.commit()
            return str(True)
        except Exception as e:
            return str(e)
            raise

    def obtener_actividades_mes(self, idEstudiante, mesI):
        sql = "SELECT Nombre,Descripcion,HoraInicio, HoraFin FROM Actividad WHERE idEstudiante='{}' AND MONTH(HoraInicio)={}".format(
            str(idEstudiante), int(mesI)
        )
        self.cursor.execute(sql)
        user = self.cursor.fetchall()
        salida = []
        for i in user:
            temp = {
                "nombre": str(i[0]),
                "descripcion": str(i[1]),
                "fechaInicio": str(i[2]),
                "fechaFinal": str(i[3]),
            }
            salida.append(temp)
        return salida

    # Borrar actividad
    def borrar_actividad(self, idActividad):
        sql = "DELETE FROM Actividad WHERE idActividad={}".format(idActividad)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)
            raise

    def cambiar_hora_actividad(
        self,
        anoI,
        mesI,
        diaI,
        HoraI,
        MinutoI,
        SegundoI,
        anoF,
        mesF,
        diaF,
        HoraF,
        MinutoF,
        SegundoF,
        idEstudiante,
    ):
        fechaI = datetime(
            year=anoI,
            month=mesI,
            day=diaI,
            hour=HoraI,
            minute=MinutoI,
            second=SegundoI,
            microsecond=0,
            tzinfo=None,
            fold=0,
        )
        fechaF = datetime(
            year=anoF,
            month=mesF,
            day=diaF,
            hour=HoraF,
            minute=MinutoF,
            second=SegundoF,
            microsecond=0,
            tzinfo=None,
            fold=0,
        )
        sql = "UPDATE Actividad SET HoraInicio='{}',HoraFin='{}' WHERE idEstudiante='{}'".format(
            fechaI.strftime("%Y-%m-%d %H:%M:%S"),
            fechaF.strftime("%Y-%m-%d %H:%M:%S"),
            idEstudiante,
        )
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)
            raise


if __name__ == "__main__":
    db = baseDatos()
    li = db.obtener_actividades_mes("test", "8")
    print(li[0][3])
# database.ingresar_Estudiante('20172020141','juan','montes','1234','juancho')
# database.Iniciar_sesion('20172020141','1234')
# database.ingresar_actividad('n','matematicas','Clase de calculo', 2020,8,8,20,20,20,2020,8,8,21,20,10,20172020141)
# database.obtener_actividades_mes(8,20172020141)
# database.borrar_actividad(1)
# database.cambiar_hora_actividad(2019,8,8,20,20,20,2019,8,8,21,20,10,20172020141)
# database.close()
