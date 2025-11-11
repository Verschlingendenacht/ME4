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
import os

#pensemos en esto como el inventario general
class Controlador:
    def __init__(self):
        # Inicializa tres listas dobles independientes
        self.__lista_objetos = double_list()
        self.__lista_hechizos = double_list()
        self.__lista_pociones = double_list()
        self.__jugador = None

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
    
    def registrar_jugador(self, jugador):
        """
        Registra al jugador que comparte las listas con el controlador.
        Llamado automáticamente desde Jugador.
        """
        self.__jugador = jugador
        return True

    # ---------------------------------------------
    # Operaciones principales del sistema
    # ---------------------------------------------
    def cargar_desde_archivo(self, ruta, tipo = None): #q es tipo?
        """
        Lee los datos iniciales desde un archivo de texto (o csv?).
        Cada línea debe contener:
        tipo, nombre, efecto, duracion, peso, usos
        """
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:

                next(archivo) #saltarnos las cabeceras

                for linea in archivo:
                    # Process each line and add to appropriate list
                    datos = linea.strip().split(',')
                    if len(datos) >= 6:
                        tipo_elemento = datos[0].lower()
                        if tipo_elemento == "hechizo":
                            hechizo = Hechizo(datos[1], datos[2], datos[3], datos[4], datos[5])
                            self.agregar_elemento("hechizo", hechizo)

                        elif tipo_elemento == "poción":
                            pocion = Pocion(datos[1], datos[2], datos[3], datos[4], datos[5])
                            self.agregar_elemento("pocion", pocion)

                        else:
                            objeto = Objeto(datos[1], datos[2], datos[3], datos[4], datos[5])
                            self.agregar_elemento("objeto", objeto)


        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta}")
        except Exception as e:
            print(f"Error al cargar el archivo: {str(e)}")


    def agregar_elemento(self, tipo : str, elemento):
        """
        Inserta un nuevo elemento a la lista indicada.
        """
        # Validar capacidad antes de insertar
        if self.__jugador and not self.__jugador.puede_agregar(elemento):
            print(f"No se puede agregar '{getattr(elemento, 'nombre', str(elemento))}': excede límite de peso del jugador.")
            return False
        
        if tipo.lower() in ("hechizo", "hechizos"):
            self.lista_hechizos.addFirst(elemento)
        elif tipo.lower() in ("pocion", "pociones"):
            self.lista_pociones.addFirst(elemento)
        elif tipo.lower() in ("objeto", "objetos"): #agregar de forma ordenada (requisito del profe)
            lista = self.lista_objetos
            #intentar convertir peso a float
            try:
                nuevo_peso = float(elemento.peso)
            except Exception:
                nuevo_peso = 0.0

            if lista.isEmpty():
                lista.addFirst(elemento)
                return
            
            current = lista.first
            while current:
                try:
                    peso_actual = float(current.data.peso)
                except Exception:
                    peso_actual = 0.0
                #insertar antes del prier nodo con peso menor que el nuevo
                if peso_actual < nuevo_peso:
                    lista.addBefore(current, elemento)
                    return
                current = current.next

            #si no se inserto (nuevo_peso <= todos), agregar al final
            lista.addLast(elemento)
            return 
        
        else:
            raise TypeError("Tipo de elemento no soportado al agregar (clase)")
            

    def buscar_por_nombre(self, tipo, nombre):
        """
        Busca un elemento en la lista según su nombre.
        Retorna el objeto si lo encuentra, None si no.
        """
        listaABuscar = self.__seleccionar_lista(tipo)
        if listaABuscar is None or listaABuscar.first is None:
            return None

        nodo = listaABuscar.first
        nombreABuscar = nombre.lower()

        while nodo is not None:
            elemento = nodo.data
            if elemento.nombre.lower() == nombreABuscar:
                return elemento
            nodo = nodo.next

        return None
    
    def eliminar_por_nombre(self, tipo, nombre):
        """
        Elimina un elemento por su nombre.
        Retorna True si fue exitoso, False si no.
        """
        listaABuscar = self.__seleccionar_lista(tipo)
        if listaABuscar is None or listaABuscar.first is None:
            print("Lista no valida o está vacia.")
            return False

        nodo = listaABuscar.first
        nombre_buscado = nombre.lower()

        #Buscar el nodo
        while nodo is not None:
            elemento = nodo.data
            if elemento.nombre.lower() == nombre_buscado:

                #Registrar el elemento eliminado
                self.generar_archivo_sin_usos(elemento, tipo)

                #Eliminarlo de la lista
                listaABuscar.remove(nodo)

                print(f"Elemento '{nombre}' eliminado correctamente de la lista '{tipo}'.")
                return True
            
            nodo = nodo.next

        #Si no se encontr
        print(f"El elemento '{nombre}' no fue encontrado en la lista de tipo '{tipo}'.")
        return False


    def listar_por_peso(self, tipo, descendente=True): #descendente= mayor a menor, ascendente=menor a mayor
        """
        Retorna una nueva double_list con los elementos de la lista seleccionada
        ordenados por peso.
        """
                
        lista_origen = self.__seleccionar_lista(tipo)
        if lista_origen is None:
            raise ValueError(f"Tipo desconocido: {tipo}")
        
        resultado = double_list() #aqui va todo
        nodo = lista_origen.first #empezamos por organizar desde la cabeza

        #para cada nodo en la lista original
        while nodo:
            elemento = nodo.data

            try:
                peso_nuevo = float(elemento.peso)
            except Exception:
                peso_nuevo = 0.0

            if resultado.isEmpty():
                resultado.addFirst(elemento)
            else:
                current = resultado.first
                inserted = False
                while current:
                    try:
                        peso_actual = float(current.data.peso)
                    except Exception:
                        peso_actual = 0.0

                    if descendente: #osea mayor a menor
                        #Insertar antes del primer elemento menor
                        if peso_actual < peso_nuevo:
                            resultado.addBefore(current, elemento)
                            inserted = True
                            break
                    else: #osea menor a mayor
                        #ascendente: insertar antse del primer elemento mayor
                        if peso_actual > peso_nuevo:
                            resultado.addBefore(current, elemento)
                            inserted = True
                            break
                    current = current.next

                #Si no se inserto va al final
                if not inserted:
                    resultado.addLast(elemento)

            nodo = nodo.next

        return resultado

    def generar_archivo_sin_usos(self, elemento, tipo, ruta="ME4 Desarrollo/recursos/sin_usos.csv"):
        """
        Escribe o genera un archivo con todos los elementos de las tres listas
        que tengan 0 usos (basicamente eliminados del inventarioo).
        """

        existe = os.path.exists(ruta)

        with open(ruta, "a", encoding="utf-8") as f:
            # Escribir encabezado solo si el archivo no existía
            if not existe:
                f.write("tipo,nombre,efecto,duracion,peso,usos\n")

            f.write(f"{tipo},{elemento.nombre},{elemento.efecto},{elemento.duracion},{elemento.peso},{elemento.usos}\n")

    # ---------------------------------------------
    # Método interno para seleccionar lista
    # ---------------------------------------------
    def __seleccionar_lista(self, tipo):
        """
        Retorna la lista doble correspondiente según tipo.
        """

        if isinstance(tipo, str):
            key = tipo.lower()
            if key in ("hechizo", "hechizos"):
                return self.lista_hechizos
            if key in ("pocion", "pociones"):
                return self.lista_pociones
            if key in ("objeto", "objetos"):
                return self.lista_objetos
            return None

