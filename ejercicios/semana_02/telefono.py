class Telefono:
   
    def __init__(self,pantalla,bocinas,ram,procesador,bateria,botones_laterales,placa_madre,microfono,puerto_de_carga,color):

        self.pantalla = pantalla
        self.bocinas = bocinas
        self.ram = ram
        self.procesador = procesador
        self.bateria = bateria 
        self.botones_laterales = botones_laterales
        self.placa_madre = placa_madre
        self.microfono = microfono
        self.puerto_de_carga = puerto_de_carga
        self.color = color

        print(f"Pantalla:{self.pantalla}")
        print(f"Bocinas:{self.bocinas}")
        print(f"Ram:{self.ram}")
        print(f"Procesador:{self.procesador}")
        print(f"Bateria:{self.bateria}")
        print(f"Botones_laterales:{self.botones_laterales}")
        print(f"Placa Madre:{self.placa_madre}")
        print(f"Microfono:{self.microfono}")
        print(f"Puerto de Carga:{self.puerto_de_carga}")
        print(f"Color:{self.color}")
    
    def desbloquear():
        print("El usuario esta presionando el boton para desbloquear el telefono")

    def abrirApp():
        print("El usuario esta abriendo una aplicacion pesada")

    def cargarBateria():
        print("Conectando el cargador al puerto del telefono")

    def hacerVideollamada():
        print("Iniciando una videollamada con la camara y el microfono")

    def enseñarTelefono():
        print("El usuario esta mostrando el diseño y color de su telefono")

iphone_17 = Telefono ("OLED Super Retina XDR de 6.3 pulgadas","Estéreo con Audio Espacial","8 GB","Apple A19","3,692 mAh","bloqueo/encendido",None,None,"USB-C","Negro")
Telefono.desbloquear()
Telefono.abrirApp()
Telefono.cargarBateria()
Telefono.hacerVideollamada()
Telefono.presumirTelefono()
