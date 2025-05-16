class Cliente:
    def __init__(self, apellidos, nombres, telefono):
        self._apellidos = apellidos
        self._nombres = nombres
        self._telefono = telefono
        self._equipos = []

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self._apellidos = valor

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, valor):
        self._nombres = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    @property
    def equipos(self):
        return self._equipos

    def agregar_equipo(self, equipo):
        self._equipos.append(equipo)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - Tel: {self.telefono} - Equipos: {len(self.equipos)}"