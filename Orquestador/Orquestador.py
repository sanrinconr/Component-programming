class Orquestador:
    def mostrar():

        # Se intenta cargar la GUI
        try:
            from front.Gui import Gui

            Gui.desplegarInformacion()
            Gui.recibirInformacion()
        except Exception:
            pass
        # Se intenta cargar el core
        try:
            from back.Core import Core

            Core.quienSoy()
        except Exception:
            pass

    def main():
        Orquestador.mostrar()


# Ejecucion del main, el punto de inicio en otras palabras
if __name__ == "__main__":
    Orquestador.main()
