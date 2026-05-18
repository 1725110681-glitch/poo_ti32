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