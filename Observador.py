from Jugador import Jugador
class Observador(Jugador):
    def __init__(self, nombre, num_control, nivel, puntos, nombre_equipo, partidas_vistas):
        super().__init__(nombre, num_control, nivel, puntos)
        self.partidas_vistas = partidas_vistas

    def ver_partida(self):
        self.partidas_vistas += 1
        self.puntos += 5
        print(f"{self.nombre} lleva {self.partidas_vistas}")
       

    def mostrar_perfil(self):
        super().mostrar_perfil(self.nombre, self.num_control, self.nivel, self.puntos)
        print(f"Partidas_vistas: {self.partidas_vistas}")