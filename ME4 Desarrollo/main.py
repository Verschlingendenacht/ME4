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

from controlador import Controlador
from elementos.jugador import Jugador
from elementos.objeto import Objeto
from elementos.hechizo import Hechizo
from elementos.pocion import Pocion

print("=== INICIO DE PRUEBAS DEL SISTEMA ===\n")

controlador = Controlador()
jugador = Jugador("Héroe", mana_maximo=100, peso_limite=50.0, controlador=controlador)

# --------------------------------------------
# CARGAR DATOS DESDE ARCHIVO
# --------------------------------------------
print("\n--- Prueba 1: Carga de archivo ---")

# ✅ Caso exitoso
ruta_valida = r"ME4 Desarrollo\recursos\iniciales.csv"
controlador.cargar_desde_archivo(ruta_valida)
print("✅ Archivo cargado correctamente.")

# ❌ Caso fallido (ruta incorrecta)
ruta_invalida = r"ME4 Desarrollo\recursos\no_existe.csv"
controlador.cargar_desde_archivo(ruta_invalida)  # Debe mostrar mensaje de error

jugador.mostrar_inventario()

# --------------------------------------------
# AGREGAR ELEMENTOS
# --------------------------------------------
print("\n--- Prueba 2: Agregar elementos ---")

# ✅ Caso exitoso: agregar objeto liviano
obj1 = Objeto("Daga ligera", "Corta rápido", "∞", 5, 10)
controlador.agregar_elemento("objeto", obj1)
print("✅ Objeto agregado correctamente (peso dentro del límite).")

# ❌ Caso fallido: objeto demasiado pesado
obj2 = Objeto("Yunque de hierro", "Sirve de defensa", "∞", 200, 1)
controlador.agregar_elemento("objeto", obj2)
print("❌ No debería agregarse, excede peso máximo.")

jugador.mostrar_inventario()

# --------------------------------------------
# BUSCAR ELEMENTOS
# --------------------------------------------
print("\n--- Prueba 3: Búsqueda por nombre ---")

# ✅ Caso exitoso
resultado = controlador.buscar_por_nombre("objeto", "Daga ligera")
print(f"✅ Resultado de búsqueda: {resultado}")

# ❌ Caso fallido
resultado_fallo = controlador.buscar_por_nombre("objeto", "Espada Fantasma")
print(f"❌ Resultado esperado (None): {resultado_fallo}")

# --------------------------------------------
# USAR HECHIZOS Y POCIONES
# --------------------------------------------
print("\n--- Prueba 4: Uso de hechizos y pociones ---")

# Crear hechizo y poción de prueba
hechizo = Hechizo("Rayo", "Descarga eléctrica", 3, 20, 2)
pocion = Pocion("Curación menor", "Recupera salud", 2, 1.0, 2)
controlador.agregar_elemento("hechizo", hechizo)
controlador.agregar_elemento("pocion", pocion)

# ✅ Caso exitoso — usar hechizo con mana suficiente
jugador.usar("hechizo", "Curación Mayor")

# ❌ Caso fallido — usar hechizo sin suficiente mana
jugador.mana = 0
jugador.usar("hechizo", "Bola de Fuego")

# ✅ Caso exitoso — usar poción hasta agotarla
jugador.usar("pocion", "Elixir de Fuego")
jugador.usar("pocion", "Elixir de Fuego")
jugador.usar("pocion", "Elixir de Fuego")
jugador.usar("pocion", "Elixir de Fuego")
jugador.usar("pocion", "Elixir de Fuego")

# --------------------------------------------
# ELIMINAR ELEMENTOS
# --------------------------------------------
print("\n--- Prueba 5: Eliminación de elementos ---")

# ✅ Caso exitoso
controlador.eliminar_por_nombre("objeto", "Espada de Fuego")

# ❌ Caso fallido
controlador.eliminar_por_nombre("objeto", "Objeto inexistente")

jugador.mostrar_inventario()

# --------------------------------------------
# LISTAR POR PESO
# --------------------------------------------
print("\n--- Prueba 6: Listar por peso ---")
print("✅ Orden descendente:")
controlador.listar_por_peso("objeto", descendente=True).show()

print("\n✅ Orden ascendente:")
controlador.listar_por_peso("objeto", descendente=False).show()

print("\n=== FIN DE PRUEBAS ===")
