import compileall
import os, shutil, glob
from zipfile import ZipFile
from os.path import basename

compileall.compile_dir("./Core/", legacy=True, force=True)

origen = "Core/"
## Edit this

destino = "Orquestador/back/"
## Edit this

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
zipObj = ZipFile("Core.zip", "w")

# Se agregan al zip todos los pyc
for dirname, subdirs, files in os.walk(origen):
    for filename in files:
        if filename.lower().endswith(".pyc"):
            zipObj.write(os.path.join(dirname, filename), arcname=filename)
zipObj.close()

# Se elimina cualquier .pyc del componentes
for parent, dirnames, filenames in os.walk(origen):
    for fn in filenames:
        if fn.lower().endswith(".pyc"):
            os.remove(os.path.join(parent, fn))
# Se mueve el zip a la ubicacion
shutil.move("Core.zip", destino)
