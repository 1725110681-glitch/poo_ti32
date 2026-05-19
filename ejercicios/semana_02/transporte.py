class Transporte:
    def __init__(self, tipo, capacidad, velocidad_max, empresa, ruta, estado, id_unidad, tarifa, gasolina, ano):
        
        self.tipo = tipo
        self.capacidad = capacidad
        self.velocidad_max = velocidad_max
        self.empresa = empresa
        self.ruta = ruta
        self.estado = estado
        self.id_unidad = id_unidad
        self.tarifa = tarifa
        self.gasolina = gasolina
        self.ano = ano

        print(f"Tipo = {self.tipo}")
        print(f"Capacidad = {self.capacidad}")
        print(f"Velocidad Máxima = {self.velocidad_max}")
        print(f"Empresa = {self.empresa}")
        print(f"Ruta = {self.ruta}")
        print(f"Estado = {self.estado}")
        print(f"Id Unidad = {self.id_unidad}")
        print(f"Tarifa = {self.tarifa}")
        print(f"Gasolina = {self.gasolina}")
        print(f"Ano = {self.ano}")

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


autobus = Transporte("Autobús","20 pasajeros","90 km/h","Transportes Pachuca","Ruta 47","Activo","RT47-2026","$12.00","Diésel","2025")
autobus.abrir_puertas()
autobus.iniciar_ruta()
autobus.anunciar_parada()
autobus.frenar()
autobus.finalizar_viaje()