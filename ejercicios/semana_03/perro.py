class Perro:
    def __init__(self,nombre,raza,edad,color,peso,tamano,genero,historial_de_vacunas,tipo_de_orejas,tipo_de_cola):

        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso
        self.tamano = tamano
        self.genero = genero
        self.historial_de_vacunas = historial_de_vacunas
        self.tipo_de_orejas = tipo_de_orejas
        self.tipo_de_cola = tipo_de_cola

        print(f"Nombre:{self.nombre}")
        print(f"Raza:{self.raza}")
        print(f"Edad:{self.edad}")
        print(f"Color:{self.color}")
        print(f"Peso:{self.peso}")
        print(f"Tamaño:{self.tamano}")
        print(f"Genero:{self.genero}")
        print(f"Historial de Vacunas:{self.historial_de_vacunas}")
        print(f"Tipo de Orejas:{self.tipo_de_orejas}")
        print(f"Tipo de Cola:{self.tipo_de_cola}")

    def ladrar(self):
        print("El Peroo esta ladrando muy Fuerte")
    def comer(self):
        print("El perro esta comiendo sus croquetas")
    def correr(self):
        print("El perro esta corriendo en el parque")
    def dormir(self):
        print("El perro esta dormido en su cama")
    def moverLaCola(self):
        print("El perro mueve la cola porque esta feliz")

mi_perro = Perro("Max", "Golden Retriever", "3 años", "Dorado", "30kg", "Grande", "Macho", "Completo", "Caídas", "Larga y peluda")
mi_perro.ladrar()
mi_perro.comer()
mi_perro.correr()
mi_perro.dormir()
mi_perro.moverLaCola()