from os import listdir
from importlib import import_module
from os import scandir, getcwd, path


class Cargador:
    clases = []

    def importDinamico():
        directorios = ["back", "front"]
        # Se recorren los directorio de las arquitecturas
        for directorio in directorios:
            # Se ingresan todos los pyc de la arquitectura a la lista
            listaArch = Cargador.ls(directorio)
            # Se importa y se agrega a las clases disponibles de cargador
            for archivo in listaArch:
                Cargador.agregarClase(Cargador.import_from(directorio, archivo))
        Cargador.agregarClase(Cargador.import_from(".", "Orquestador"))

    def agregarClase(clase):
        Cargador.clases.append(clase)

    def getInstancia(clase):
        for i in Cargador.clases:
            if i.__name__ == clase:
                return i
        return None

    def import_from(seccion, archivo):

        archivo = archivo.strip(".pyc")
        # Se importa el paquete
        if seccion != ".":
            imp = import_module(seccion + "." + archivo)
        else:
            imp = import_module(archivo)
        # Se obtiene la instancia de la clase
        clase = getattr(imp, archivo)
        return clase
    
    def test():
        print(path.join(getcwd(),"back"))
    def ls(ruta):
        archivos = []

        for arch in scandir(path.join(getcwd(),ruta)):
            if arch.is_file():
                if ".pyc" in arch.name:
                    archivos.append(arch.name)
        return archivos
