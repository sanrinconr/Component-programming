import pymysql
import time
import datetime


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
        except Exception as e:
            print(e)
            raise

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
        except Exception as e:
            print(e)
            raise

    # Adicion de actividades
    def ingresar_actividad(
        self,
        seRealizo,
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
        idHorario,
    ):
        fechaI = datetime.datetime(
            year=añoI,
            month=mesI,
            day=diaI,
            hour=HoraI,
            minute=MinutoI,
            second=SegundoI,
            microsecond=0,
            tzinfo=None,
            fold=0,
        )
        fechaF = datetime.datetime(
            year=añoF,
            month=mesF,
            day=diaF,
            hour=HoraF,
            minute=MinutoF,
            second=SegundoF,
            microsecond=0,
            tzinfo=None,
            fold=0,
        )
        sql = "INSERT INTO actividad (seRealizo,Descripcion,HoraInicio,HoraFin,idHorario) VALUES (%s,%s,%s,%s,%s)"
        valores = (
            seRealizo,
            Descripcion,
            fechaI.strftime("%Y-%m-%d %H:%M:%S"),
            fechaF.strftime("%Y-%m-%d %H:%M:%S"),
            idHorario,
        )
        try:
            self.cursor.execute(sql, valores)
            self.connection.commit()
        except Exception as e:
            print(e)
            raise


# database.Iniciar_sesion('20172020141','1234')
# database.Crear_horario('HorarioJuan','Horario de universidad',20172020141)
# database.ingresar_actividad('n','matematicas', 2020,8,8,20,20,20,2020,8,8,21,20,10,1)
