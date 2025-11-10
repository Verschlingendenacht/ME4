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

class Pocion:
    def __init__(self, nombre, efecto, duracion, peso, usos):
        self.nombre = nombre
        self.efecto = efecto
        self.duracion = duracion
        self.peso = peso
        self.usos = usos

    def beber(self):
        print(f"Bebiendo la poción: {self.nombre} que tiene el efecto: {self.efecto} por {self.duracion} minutos.")

    def __str__(self):
        return f"Hechizo: {self.nombre} | Efecto: {self.efecto} | Duración: {self.duracion} | Peso: {self.peso} | Usos: {self.usos}"