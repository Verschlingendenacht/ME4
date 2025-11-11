class Jugador:
    def __init__(self, nombre, mana_maximo, peso_limite, controlador=None):
        self.__nombre = nombre
        self.__mana = mana_maximo
        self.__mana_maximo = mana_maximo
        self.__peso_limite = peso_limite
        self.__peso_actual = 0.0
        self.__controlador = controlador
        controlador.registrar_jugador(self) #anclamos ambas clases, de esta forma el inventario tiene conciencia de los atributos del jugador


    @property
    def nombre(self):
        return self.__nombre

    @property
    def mana(self):
        return self.__mana

    @property
    def mana_maximo(self):
        return self.__mana_maximo

    @property
    def peso_limite(self):
        return self.__peso_limite

    @property
    def peso_actual(self):
        return self.__peso_actual

    @property
    def inventario_objetos(self):
        return self.__controlador.lista_objetos if self.__controlador else None

    @property
    def inventario_hechizos(self):
        return self.__controlador.lista_hechizos if self.__controlador else None

    @property
    def inventario_pociones(self):
        return self.__controlador.lista_pociones if self.__controlador else None

    @mana.setter
    def mana(self, valor):
        if valor < 0:
            self.__mana = 0
        elif valor > self.__mana_maximo:
            self.__mana = self.__mana_maximo
        else:
            self.__mana = valor

    def calcular_peso_total(self):
        """
        Calcula el peso total del inventario desde los datos del controlador.
        """
        peso_total = 0.0
        
        # Sumar peso de objetos
        nodo = self.__controlador.lista_objetos.first
        while nodo:
            try:
                peso_total += float(nodo.data.peso)
            except Exception:
                pass
            nodo = nodo.next
        
        # Sumar peso de hechizos
        nodo = self.__controlador.lista_hechizos.first
        while nodo:
            try:
                peso_total += float(nodo.data.peso)
            except Exception:
                pass
            nodo = nodo.next
        
        # Sumar peso de pociones
        nodo = self.__controlador.lista_pociones.first
        while nodo:
            try:
                peso_total += float(nodo.data.peso)
            except Exception:
                pass
            nodo = nodo.next
        
        self.__peso_actual = round(peso_total, 2) #bendito sea no llenar la pantalla de decimales
        return peso_total

    def mostrar_inventario(self):
        """
        Muestra todos los elementos del inventario desde el controlador.
        """
        self.calcular_peso_total()
        print(f"\n=== Inventario de {self.__nombre} ===")
        print(f"Mana: {self.__mana}/{self.__mana_maximo}")
        print(f"Peso: {self.__peso_actual}/{self.__peso_limite}")
        print("\nObjetos:")
        if self.__controlador.lista_objetos.isEmpty():
            print("  (ninguno)")
        else:
            self.__controlador.lista_objetos.show()
        
        print("\nHechizos:")
        if self.__controlador.lista_hechizos.isEmpty():
            print("  (ninguno)")
        else:
            self.__controlador.lista_hechizos.show()
        
        print("\nPociones:")
        if self.__controlador.lista_pociones.isEmpty():
            print("  (ninguno)")
        else:
            self.__controlador.lista_pociones.show()

    def puede_agregar(self, elemento):
        """
        Verifica si hay capacidad para agregar 'elemento' según su peso.
        """
        try:
            peso_elemento = float(elemento.peso)
        except Exception:
            peso_elemento = 0.0

        peso_actual = self.calcular_peso_total()
        return (peso_actual + peso_elemento) <= self.__peso_limite #retorna sizas o nonas dependiendo de la condicion
    
    def __str__(self):
        self.calcular_peso_total()
        return f"Jugador: {self.__nombre} | Mana: {self.__mana}/{self.__mana_maximo} | Peso: {self.__peso_actual}/{self.__peso_limite}"