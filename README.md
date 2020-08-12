# Programacion por componentes en python
## Integrantes
- Santiago Rincón 20172020084
- Juan David Montes 20172020141
- Josué Nuñez  20172020071

## Requisitos
Se debe tener instalado el framework flask (conexion python con web) y el framework pymysql (conexion con la db). Para instalarlos:
```sh
pip install flask
```
```sh
pip install pymysql
```
## Como ejecutar
Para ejecutar el programa se deben crear todos lo binarios, esto se logra ejecutando el archivo despliegeProduccion.py el cual generara la carpeta Produccion/
```sh
python3 despliegeProduccion.py
```
Ahora tan solo resta entrar a la carpeta Produccion y ejecutar el main que se encuentra en Orquestador.pyc

```sh
python3 Orquestador.pyc
```

## Como editar el codigo
Ya que cada componente se encuentra aislado es necesario desplegarlos y "acoplarlos", para ello se ejecuta el archivo desplegarDesarrollo.py
```sh
python3 desplegarDesarrollo.py
```
Una vez realizado el despliegue en Orquestador/ se tienen todos los binarios de los componentes y el archivo Orquestador.py listo para usar los componentes como se desee.

### Modificar los componentes
En caso de querer modificar el funcionamiento de los componentes se debe ir al respectivo componente modificarlo y volver a desplegar con desplegarDesarrollo.py para actualizar los binarios

#### Ejemplo, modificando gui
Si se desea modificar un elemento de la Gui, entonces en la carpeta GUI/, se modifica lo que necesita. Posteriormente se procede a ejecutar despliegeDesarrollo.py para actualizar el binario que se tiene en Orquestador/
```sh
python3 desplegarDesarrollo.py
```
Y luego se vuelve a ejecutar el orquestador el cual posee ya el componente Gui actualizado
```sh
python3 Orquestador.py
```

