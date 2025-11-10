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

class Pocion(Objeto):
    def __init__(self, nombre, efecto, duracion, peso, usos):
        super().__init__(nombre, efecto, duracion, peso, usos)

    def beber(self):
        print(f"Bebiendo la poción: {self.nombre} que tiene el efecto: {self.efecto} por {self.duracion} minutos.")