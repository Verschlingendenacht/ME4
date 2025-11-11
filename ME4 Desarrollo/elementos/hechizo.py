# -----------------------------------------------------------
# MOMENTO EVALUATIVO 4 - ESTRUCTURAS DE DATOS
# INTEGRANTES:
# - Juan Pablo Salazar
# - Luz Natalia Ríos Serna
# - Nilzon Alejandro Gomez Maya
# - Julián Felipe Vélez Medina
# GRUPO: 2
# DOCENTE: Ricardo Franco Ceballos
# -----------------------------------------------------------
# NOTA IMPORTANTE:
# Este código implementa exclusivamente LISTAS DOBLES,
# sin uso de estructuras nativas de Python (como list, dict o set).
# Todas las operaciones están encapsuladas en clases,
# aplicando los principios de POO y siguiendo las directrices del curso.
# -----------------------------------------------------------

from elementos.objeto import Objeto

class Hechizo(Objeto):
    def __init__(self, nombre, efecto, duracion, peso, usos):
        super().__init__(nombre, efecto, duracion, peso, usos)

    def usar(self, jugador, objetivo=None):
        
        if self.usos <= 0:
            print(f"⚠️ El hechizo '{self.nombre}' ya no tiene usos disponibles.")
            return

        costo_mana = float(self.peso) #nota: pensemos en el peso de un hechizo como su costo de mana
        if jugador.mana < costo_mana:
            print(f"❌ No tienes suficiente maná para lanzar '{self.nombre}'. "
                  f"Requiere {costo_mana}, pero solo tienes {jugador.mana}.")
            return

        #Reducir mana y usos
        jugador.mana -= costo_mana
        self.usos -= 1

        print(f"✨ {jugador.nombre} lanza '{self.nombre}' sobre {objetivo or 'el entorno'} "
              f"→ Efecto: '{self.efecto}' (duración {self.duracion} min, costo {costo_mana} maná).")

        if self.usos == 0:
            print(f"💨 El hechizo '{self.nombre}' se ha agotado.")
