class Librobiblioteca:

    def __init__(self,portada,letras,pasta,hojas,imagenes,autor,tipografia,dedicatoria,personajes,indice):

        self.portada = portada
        self.letras = letras
        self.pasta = pasta
        self.hojas = hojas
        self.imagenes = imagenes 
        self.autor = autor
        self.tipografia = tipografia
        self.dedicatoria = dedicatoria
        self.personajes = personajes
        self.indice = indice 

        print(f"Portada:{self.portada}")
        print(f"Letras:{self.letras}")
        print(f"Pasta:{self.pasta}")
        print(f"Hojas:{self.hojas}")
        print(f"Imagenes:{self.imagenes}")
        print(f"Autor:{self.autor}")
        print(f"Tipografia:{self.tipografia}")
        print(f"Dedicatoria:{self.dedicatoria}")
        print(f"Personajes:{self.personajes}")
        print(f"Indice:{self.indice}")

    def leer(self):
        print("Leer el libro")

    def imaginar(self):
        print("Imaginando las escenas del libro")

    def aprender(self):
        print("Adqueriendo nuevos conocimientos")

    def reflexionar(self):
        print("Reflexionando sobre la lectura")
         
    def coleccionar(self):
        print("Guardando el libro en mi coleccion personal")  
          
el_principito = Librobiblioteca( "portada.JPG", "75,000", "Blanda", "96", "imagenes.jpg", "Antoine de Saint Exupery", "Granjon, Manuscrito", "A Leon Werth cuando era niño", "El Principito, El Aviador, El Zorro, La Rosa", "capitulo I-IX: El Aviador en el desierto, la vida en el Asteroide B-612, capitulo X: El planeta del Rey, capitulo XI: El planeta del vanidoso" )
el_principito.leer()
el_principito.imaginar()
el_principito.aprender()
el_principito.reflexionar()
el_principito.coleccionar()
