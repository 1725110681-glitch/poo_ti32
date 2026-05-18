class Transporte:
    def __init__(self, tipo, capacidad, velocidad_max, empresa, ruta, estado, id_unidad, tarifa, gasolina, ano):
        # 10 Atributos (Variables)
        self.tipo = tipo
        self.capacidad = capacidad
        self.velocidad_max = velocidad_max
        self.empresa = empresa
        self.ruta = ruta
        self.estado = estado
        self.id_unidad = id_unidad
        self.tarifa = tarifa
        self.gasolina = gasolina
        self.ano = ano

        print(f"Tipo = {self.tipo}")
        print(f"Capacidad = {self.capacidad}")
        print(f"Velocidad Máxima = {self.velocidad_max}")
        print(f"Empresa = {self.empresa}")
        print(f"Ruta = {self.ruta}")
        print(f"Estado = {self.estado}")
        print(f"Id Unidad = {self.id_unidad}")
        print(f"Tarifa = {self.tarifa}")
        print(f"Gasolina = {self.gasolina}")
        print(f"Ano = {self.ano}")

transporte1 = Transporte("Autobús", "20 pasajeros", "90 km/h", "Transportes Pachuca", "Ruta 47", "Activo", "RT47-2026", "$12.00", "Diésel", "2025")