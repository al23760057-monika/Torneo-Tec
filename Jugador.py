class Jugador:
    def __init__(self, nombre, num_control, nivel, puntos):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos = puntos

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Posición: {self.posicion}")

    def ganar_puntos(self, puntos_ganados):
        self.puntos += puntos_ganados
        print(f"{self.nombre} ha ganado {puntos_ganados} puntos en total. Total de puntos: {self.puntos}")

    def perder_puntos(self, puntos_perdidos):
        
        if self.puntos >= 0:
            self.puntos -= 1
        self.puntos -= puntos_perdidos
        print(f"{self.nombre} ha perdido {puntos_perdidos} puntos. Total de puntos: {self.puntos}")

    def mostrar_perfil(self, nombre, num_control, nivel, puntos):
        print(f"Nombre: {nombre}")
        print(f"Número de Control: {num_control}")
        print(f"Nivel: {nivel}")
        print(f"Puntos: {puntos}")