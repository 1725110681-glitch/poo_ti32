class Transporte:
    def __init__(self):
        pass

    def abrir_puertas(self):
        print("Las puertas se están abriendo")

    def iniciar_ruta(self):
        print("El motor ha encendido")

    def anunciar_parada(self):
        print("Próxima parada: Centro los Pastes")

    def frenar(self):
        print("Disminuyendo la velocidad")

    def finalizar_viaje(self):
        print("Hemos llegado al final de la ruta")

Autobus = Transporte()
Autobus.abrir_puertas()
Autobus.iniciar_ruta()
Autobus.anunciar_parada()
Autobus.frenar()
Autobus.finalizar_viaje()