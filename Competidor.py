from Jugador import Jugador 
class Competidor(Jugador):
    def __init__(self, nombre, num_control, nivel, puntos, nombre_equipo):
        super().__init__(nombre, num_control, nivel, puntos)
        self.nombre_equipo = nombre_equipo
       

    def mostrar_perfil(self):
        super().mostrar_perfil(self.nombre, self.num_control, self.nivel, self.puntos)
        print(f"Nombre del Equipo: {self.nombre_equipo}")