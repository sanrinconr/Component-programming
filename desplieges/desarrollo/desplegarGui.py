import compileall
import os, shutil, glob
from zipfile import ZipFile
from os.path import basename


compileall.compile_dir("./GUI/", legacy=True, force=True)

origen = "GUI/"
## Edit this

destino = "Orquestador/front/"
## Edit this

# Se elimina cualquier zip en el orquestador

try:
    shutil.rmtree(destino)
except:
    pass
try:
    os.makedirs(destino)
    ## it creates the destination folder
except:
    pass


##Creacion del zip
zipObj = ZipFile("Gui.zip", "w")

# Se agregan al zip todos los pyc
for dirname, subdirs, files in os.walk(origen):
    for filename in files:
        if filename.lower().endswith(".pyc"):
            zipObj.write(os.path.join(dirname, filename), arcname=filename)

# Se agrega la carpeta templates al zip
for dirname, subdirs, files in os.walk(origen + "/templates"):
    for filename in files:
        zipObj.write(os.path.join(dirname, filename))

# Se agrega la carpeta static al zip
for dirname, subdirs, files in os.walk(origen + "/static"):
    for filename in files:
        zipObj.write(os.path.join(dirname, filename))
zipObj.close()

# Se elimina cualquier .pyc del componentes
for parent, dirnames, filenames in os.walk(origen):
    for fn in filenames:
        if fn.lower().endswith(".pyc"):
            os.remove(os.path.join(parent, fn))
# Se mueve el zip a la ubicacion
shutil.move("Gui.zip", destino)
