class Universidad:

    def __init__(self,logo,oferta_educativa,localidad,sistema_informativo,modalidad,servicios,ubicacion,talleres,cantidad_salones,rector):

        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informativo = sistema_informativo
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres
        self.cantidad_salones = cantidad_salones
        self.rector = rector

        print(f"Logotipo de la Universidad:{self.logo}")
        print(f"oferta educativa:{self.oferta_educativa}")
        print(f"localidad:{self.localidad}")
        print(f"sistema informativo:{self.sistema_informativo}")
        print(f"modadlidad:{self.modalidad}")
        print(f"servicios:{self.servicios}")
        print(f"ubicacion:{self.ubicacion}")
        print(f"talleres:{self.talleres}")
        print(f"cantidad de salones:{self.cantidad_salones}")
        print(f"rector:{self.rector}")

unideh = Universidad ("logotipo.jpg","Ing software,Turismo alternativo","San Miguel","CADU","Virtual","Bibliotecas digitales","Santa Catarina",None,None,"Octavio Castillo")