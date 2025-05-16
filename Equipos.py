class Equipo:
    def __init__(self, numero_parte, tipo_equipo, descripcion):
        self.numero_parte = numero_parte
        self.tipo_equipo = tipo_equipo
        self.descripcion = descripcion

    def __str__(self):
        return f"Parte: {self.numero_parte}, Tipo: {self.tipo_equipo}, Problema: {self.descripcion}"