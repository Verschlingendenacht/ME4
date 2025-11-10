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

class double_node:
    def __init__(self, data=None, next=None, prev=None ):
        self.__data = data
        self.__next = next
        self.__prev = prev

    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @property
    def prev(self):
        return self.__prev
    
    @data.setter
    def data(self, d):
        self.__data = d

    @next.setter
    def next(self, n):
        self.__next = n

    @prev.setter
    def prev(self, p):
        self.__prev = p

    def __str__(self):
        return str(self.data)