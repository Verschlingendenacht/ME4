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

#Esta clase actua como superclase para hechizo y pocion
class Objeto:
    def __init__(self, nombre, efecto, duracion, peso, usos):
        self.__nombre = nombre
        self.__efecto = efecto
        self.__duracion = duracion
        self.__peso = float(peso)
        self.__usos = int(usos)

    def usar(self):
        print(f"Usando el objeto: {self.nombre}")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} | Efecto: {self.efecto} | Duración: {self.duracion} | Peso: {self.peso} | Usos: {self.usos}"

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def efecto(self):
        return self.__efecto
    
    @property
    def duracion(self):
        return self.__duracion
    
    @property
    def peso(self):
        return self.__peso
    
    @property
    def usos(self):
        return self.__usos
    
    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    @efecto.setter
    def efecto(self, e):
        self.__efecto = e

    @duracion.setter
    def duracion(self, d):
        self.__duracion = d

    @peso.setter
    def peso(self, p):
        self.__peso = p

    @usos.setter
    def usos(self, u):
        self.__usos = u