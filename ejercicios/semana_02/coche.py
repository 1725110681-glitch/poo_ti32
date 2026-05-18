class Coche:
    def __init__(self,marca,modelo,color,placa,kilometraje,motor,num_puertas,combustible,transmision,ano):
        
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa
        self.kilometraje = kilometraje
        self.motor = motor
        self.num_puertas = num_puertas
        self.combustible = combustible
        self.transmision = transmision
        self.ano = ano

        print(f"Marca:{self.marca}")
        print(f"Modelo:{self.modelo}")
        print(f"Color:{self.color}")
        print(f"Placa:{self.placa}")
        print(f"Kilometraje:{self.kilometraje}")
        print(f"Motor:{self.motor}")
        print(f"Numero de Puertas:{self.num_puertas}")
        print(f"Combustible:{self.combustible}")
        print(f"Transmision:{self.transmision}")
        print(f"Ano:{self.ano}")

porsche = Coche( "porsche", "911 carrera", "negro", "porsche_911", "12500", "3.0L biturbo", "2", "gasolina", "automatica PDK", "2025" )

class Coche:
    def encender(self):
        print("Encendiendo el motor del Porsche")
    def frenar (self):
        print("El coche esta frenando con precision")
    def cargar_combustible (self):
        print("Llenando el tanque de gasolina")
    def acelerar (self):
        print("Acelerando a maxima potencia")
    def encender_luces (self):
        print("Encendiendo las luces del carro") 

porsche = Coche()
porsche.encender()
porsche.frenar()
porsche.cargar_combustible()
porsche.acelerar()
porsche.encender_luces() 