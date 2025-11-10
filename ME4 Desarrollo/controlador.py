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
from elementos.objeto import Objeto
from elementos.hechizo import Hechizo
from elementos.pocion import Pocion

class Controlador:
    def __init__(self):
        # Inicializa tres listas dobles independientes
        self.__lista_objetos = double_list()
        self.__lista_hechizos = double_list()
        self.__lista_pociones = double_list()

    # ---------------------------------------------
    # Propiedades de solo lectura
    # ---------------------------------------------
    @property
    def lista_objetos(self):
        return self.__lista_objetos

    @property
    def lista_hechizos(self):
        return self.__lista_hechizos

    @property
    def lista_pociones(self):
        return self.__lista_pociones

    # ---------------------------------------------
    # Operaciones principales del sistema
    # ---------------------------------------------
    def cargar_desde_archivo(self, ruta, tipo = None): #q es tipo?
        """
        Lee los datos iniciales desde un archivo de texto.
        Cada línea debe contener:
        tipo, nombre, efecto, duracion, peso, usos
        """
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.readlines()
                for linea in contenido:
                    # Process each line and add to appropriate list
                    datos = linea.strip().split(',')
                    if len(datos) >= 6:
                        tipo_elemento = datos[0].lower()
                        if tipo_elemento == "hechizo":
                            hechizo = Hechizo(datos[0], datos[1], datos[2], datos[3], datos[4])
                            print(hechizo)
                        elif tipo_elemento == "pocion":
                            pocion = Pocion(datos[0], datos[1], datos[2], datos[3], datos[4])
                            print(pocion)
                        else:
                            objeto = Objeto(datos[0], datos[1], datos[2], datos[3], datos[4])
                            print(objeto)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta}")
        except Exception as e:
            print(f"Error al cargar el archivo: {str(e)}")


    def agregar_elemento(self, tipo, elemento):
        """
        Inserta un nuevo elemento a la lista indicada.
        """
        pass

    def buscar_por_nombre(self, tipo, nombre):
        """
        Busca un elemento en la lista según su nombre.
        Retorna el objeto si lo encuentra, None si no.
        """
        pass

    def eliminar_por_nombre(self, tipo, nombre):
        """
        Elimina un elemento por su nombre.
        """
        pass

    def listar_por_peso(self, tipo, descendente=True):
        """
        Ordena la lista seleccionada según el peso del elemento.
        """
        pass

    def generar_archivo_usos_bajos(self, ruta_salida="usos_bajos.txt"):
        """
        Genera un archivo con todos los elementos de las tres listas
        que tengan 3 usos o menos.
        """
        pass

    # ---------------------------------------------
    # Método interno para seleccionar lista
    # ---------------------------------------------
    def __seleccionar_lista(self, tipo):
        pass