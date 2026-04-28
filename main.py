from Competidor import Competidor
from Observador import Observador

Monica = Competidor("Monica", "12345", "Avanzado", 1000, "Equipo A")
Monica.mostrar_perfil()
Monica.ganar_puntos(500)
Monica.perder_puntos(200)

Isaac = Observador("Isaac", "54321", "Principiante", 500, "Equipo B", 10)
Isaac.mostrar_perfil()  
Isaac.ver_partida()
Isaac.ganar_puntos(200)
Isaac.perder_puntos(100)