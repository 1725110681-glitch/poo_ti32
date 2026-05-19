class Alumno:
    def __init__(self,matricula,nombre,apellido,edad,cuatrimestre,carrera,promedio_general,correo_institucional,turno,estatus):
        
        self.matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cuatrimestre = cuatrimestre
        self.carrera = carrera
        self.promedio_general = promedio_general
        self.correo_institucional = correo_institucional
        self.turno = turno
        self.estatus = estatus

        print(f"Matricula:{self.matricula}")
        print(f"Nombre:{self.nombre}")
        print(f"Apellido:{self.apellido}")
        print(f"Edad:{self.edad}")
        print(f"Cuatrimestre:{self.cuatrimestre}")
        print(f"Carrera:{self.carrera}")
        print(f"Promedio General:{self.promedio_general}")
        print(f"Correo Institucional:{self.correo_institucional}")
        print(f"Turno:{self.turno}")
        print(f"Estatus:{self.estatus}")
    
    def estudiar(self):
        print("El Alumno esta estudiando para su clase de Calculo Integral")
    def entregarTarea(self):
        print("El Alumno entrego la Tarea que dejaron de Ingles")
    def presentarExamen (self):
        print("El Alumno realizo el examen de Programacion")
    def graduarse (self):
        print("El Alumno se graduo de TICS")
    def revisarHorario (self):
        print("El Alumno reviso que la primera clase le toca Ingles")

alumno1 = Alumno( "1725110586", "Ariadna","Muñoz Corella", "20 años","Tercero","Ingeneria en Software","9.8","1725110586@utectulacingo.edu.mx","Matutino","Activo" )
alumno1.estudiar()
alumno1.entregarTarea()
alumno1.presentarExamen()
alumno1.graduarse()
alumno1.revisarHorario()