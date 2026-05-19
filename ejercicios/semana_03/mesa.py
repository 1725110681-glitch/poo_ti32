class Mesa:
    def __init__(self,material,color,altura,largo,ancho,numero_de_patas,forma,peso_soportado,compartimentos,estilo):
        
        self.material = material
        self.color = color
        self.altura = altura
        self.largo = largo
        self.ancho = ancho
        self.numero_de_patas = numero_de_patas
        self.forma = forma
        self.peso_soportado = peso_soportado
        self.compartimentos = compartimentos
        self.estilo = estilo

        print(f"Material:{self.material}")
        print(f"Color:{self.color}") 
        print(f"Altura:{self.altura}")
        print(f"Largo:{self.largo}")
        print(f"Ancho:{self.ancho}")
        print(f"Numero de Patas:{self.numero_de_patas}")
        print(f"Forma:{self.forma}")
        print(f"Peso Soportado:{self.peso_soportado}")
        print(f"Compartimentos:{self.compartimentos}")
        print(f"Estilo:{self.estilo}")

    def sostenerObjetos(self):
        print("La mesa tiene unos libros, una computadora y una lampara")
    def mover (self):
        print("La mesa se puede mover a cualquier lado")
    def limpiar (self):
        print("Hay que limpiar la mesa que esta sucia")
    def armar (self):
        print("Se tiene que armar la mesa")
    def comedor (self):
        print("La mesa se puede ocupar para comer en familia")

mi_mesa = Mesa("Madera", "Marrón", "75 cm",  "1.80 m", "90 cm",  4,"Rectangular", "80 kg", "2 cajones", "Rústico")
mi_mesa.reclinar()
mi_mesa.soportarPeso()
mi_mesa.desplazar()
mi_mesa.ajustarAltura()
mi_mesa.girar()