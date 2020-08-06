import compileall
import os, shutil, glob
from zipfile import ZipFile
from os.path import basename

# Se compilan todos los archivos de api, en este directorio se generan los pyc
compileall.compile_dir("./api/", legacy=True, force=True)

# De donde se van a agregar los archivos al zip
origen = "api/"

# Hacia donde se va a guardar el zip
destino = "Orquestador/api/"

# Se intenta crear el directorio de destino si no existe
try:
    os.makedirs(destino)
    ## it creates the destination folder
except:
    pass

# Se elimina cualquier zip en el orquestador
for parent, dirnames, filenames in os.walk(destino):
    for fn in filenames:
        if fn.lower().endswith(".zip"):
            os.remove(os.path.join(parent, fn))

##Creacion del zip
zipObj = ZipFile("Api.zip", "w")

# Se agregan al zip todos los pyc
for dirname, subdirs, files in os.walk(origen):
    for filename in files:
        if filename.lower().endswith(".pyc"):
            zipObj.write(os.path.join(dirname, filename), arcname=filename)
zipObj.close()

# Se elimina cualquier .pyc de componente
for parent, dirnames, filenames in os.walk(origen):
    for fn in filenames:
        if fn.lower().endswith(".pyc"):
            os.remove(os.path.join(parent, fn))

# Se mueve el zip a la ubicacion destino
shutil.move("Api.zip", destino)
