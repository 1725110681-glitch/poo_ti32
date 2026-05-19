class Silla:
    def __init__(self,tipo,material,color,ruedas,peso,marca,precio,estabilidad,altura,respaldo):

        self.tipo = tipo
        self.material = material
        self.color = color
        self.ruedas = ruedas
        self.peso = peso
        self.marca = marca
        self.precio = precio
        self.estabilidad = estabilidad
        self.altura = altura
        self.respaldo = respaldo

        print(f"Tipo:{self.tipo}")
        print(f"Material:{self.material}") 
        print(f"Color:{self.color}")
        print(f"Ruedas:{self.ruedas}")
        print(f"Peso:{self.peso}")
        print(f"Marca:{self.marca}")
        print(f"Precio:{self.precio}")
        print(f"Estabilidad:{self.estabilidad}")
        print(f"Altura:{self.altura}")
        print(f"Respaldo:{self.respaldo}")
    
    def reclinar(self):
        print("La silla es reclinable")
    def soportarPeso (self):
        print("La silla soporta 50kg")
    def desplazar (self):
        print("La silla se puede mover a donde sea")
    def ajustarAltura (self):
        print("La silla se puede hacer mas alta")
    def girar (self):
        print("La silla tiene un mecanismo para que se pueda girar")

silla_oficina = Silla("Ejecutiva", "Malla y Plástico", "Negro", "5 ruedas", "12kg", "Herman Miller", "$3500", "Alta", "1.10m", "Ergonómico Reclinable")
silla_oficina.reclinar()
silla_oficina.soportarPeso()
silla_oficina.desplazar()
silla_oficina.ajustarAltura()
silla_oficina.girar()