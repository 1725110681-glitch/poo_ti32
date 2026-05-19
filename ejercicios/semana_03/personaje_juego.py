class Personaje_Juego:
    def __init__(self,color_del_traje,cantidad__de_vida,villano,nivel_de_personaje,tipo_de_telaraña,nivel_de_daño,gadget,simbolo,altura,tipo_de_traje):
        
        self.color_del_traje = color_del_traje
        self.cantidad__de_vida = cantidad__de_vida
        self.villano = villano
        self.nivel_de_personaje = nivel_de_personaje
        self.tipo_de_telaraña = tipo_de_telaraña
        self.nivel_de_daño = nivel_de_daño
        self.gadget = gadget
        self.simbolo = simbolo
        self.altura = altura
        self.tipo_de_traje = tipo_de_traje

        print(f"Color del traje:{self.color_del_traje}")
        print(f"Cantidad de vida:{self.cantidad__de_vida}") 
        print(f"Villano:{self.villano}")
        print(f"Nivel del Personaje:{self.nivel_de_personaje}")
        print(f"Tipo de Telaraña:{self.tipo_de_telaraña}")
        print(f"Nivel de Daño:{self.nivel_de_daño}")
        print(f"Gadget:{self.gadget}")
        print(f"Simbolo:{self.simbolo}")
        print(f"Altura:{self.altura}")
        print(f"Tipo de Traje:{self.tipo_de_traje}")
    
    def balancearse(self):
        print("Spiderman se balancea por Nueva York")
    def remate (self):
        print("Spiderman tiene como remate enrredar en telaraña a los villanos")
    def sentidoAracnido (self):
        print("Spiderman puede esquivar objetos con su sentido aracnido")
    def esquivar (self):
        print("Spiderman puede esquivar golpes facilmente")
    def atacar (self):
        print("Spiderman ataca a sus villanos") 

spiderman_ps4 = Personaje_Juego("Rojo y Azul", "100%", "Doctor Octopus", "Nivel 25", "Eléctrica", "85", "Disparador de ráfagas", "Araña Blanca", "1.78m", "Traje Avanzado")
spiderman_ps4.balancearse()
spiderman_ps4.remate()
spiderman_ps4.sentidoAracnido()
spiderman_ps4.esquivar()
spiderman_ps4.atacar()