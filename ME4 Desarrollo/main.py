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

from double_list import double_list
from controlador import Controlador

from elementos.objeto import Objeto
from elementos.hechizo import Hechizo
from elementos.pocion import Pocion

from elementos.jugador import Jugador

controlador = Controlador()
#controlador.cargar_desde_archivo(r"C:\Users\nilzo\Documents\programacion\proyectos\ME4\ME4 Desarrollo\recursos\iniciales.csv")

#controlador.lista_objetos.show()
print("----------")
#controlador.lista_hechizos.show()
print("------------")
#controlador.lista_pociones.show()
#controlador.listar_por_peso("objetos", False).show()


#------------------

jugador = Jugador("Héroe", mana_maximo=100, peso_limite=200.0, controlador=controlador)
print(jugador)

controlador.cargar_desde_archivo(r"C:\Users\nilzo\Documents\programacion\proyectos\ME4\ME4 Desarrollo\recursos\iniciales.csv")
jugador.mostrar_inventario()

# Prueba 1 — agregar un objeto ligero
#obj1 = Objeto("Daga de prueba", "Corta poco", "∞", 10, 5)
#controlador.agregar_elemento(Objeto, obj1)

# Ver resultado
#jugador.mostrar_inventario()

# Prueba 2 — agregar algo pesado
#obj2 = Objeto("Armadura pesada", "Protege mucho", "∞", 190, 1)
#controlador.agregar_elemento(Objeto, obj2)

# Ver resultado
#jugador.mostrar_inventario()

#------------------