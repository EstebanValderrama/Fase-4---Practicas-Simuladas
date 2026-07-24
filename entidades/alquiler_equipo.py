"""
=========================================================
Archivo: alquiler_equipo.py

Descripción:
Este archivo contiene la clase AlquilerEquipo.

Representa el servicio de alquiler de equipos
tecnológicos ofrecidos por Software FJ.

Esta clase hereda de la clase abstracta Servicio e
implementa los métodos obligatorios definidos en ella.

Autor: Grupo de trabajo
=========================================================
"""

# Importamos la clase padre
from entidades.servicio import Servicio


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos.

    Atributos:
        cantidad (int): Número de equipos alquilados.
        dias (int): Cantidad de días del alquiler.
    """

    def __init__(self, codigo, nombre, precio_base, cantidad, dias):
        """
        Constructor de la clase.

        Parámetros:
            codigo (str): Código del servicio.
            nombre (str): Nombre del servicio.
            precio_base (float): Precio por equipo por día.
            cantidad (int): Número de equipos.
            dias (int): Duración del alquiler.
        """

        # Inicializamos los atributos heredados
        super().__init__(codigo, nombre, precio_base)

        self.__cantidad = 0
        self.__dias = 0

        # Validamos los datos usando los setters
        self.cantidad = cantidad
        self.dias = dias

    # ===================================================
    # GETTERS
    # ===================================================

    @property
    def cantidad(self):
        """Devuelve la cantidad de equipos."""
        return self.__cantidad

    @property
    def dias(self):
        """Devuelve la cantidad de días."""
        return self.__dias

    # ===================================================
    # SETTERS
    # ===================================================

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        """
        Valida que la cantidad de equipos sea mayor que cero.
        """

        if nueva_cantidad <= 0:
            raise ValueError("La cantidad de equipos debe ser mayor que cero.")

        self.__cantidad = nueva_cantidad

    @dias.setter
    def dias(self, nuevos_dias):
        """
        Valida que el número de días sea mayor que cero.
        """

        if nuevos_dias <= 0:
            raise ValueError("Los días deben ser mayores que cero.")

        self.__dias = nuevos_dias

    # ===================================================
    # MÉTODOS ABSTRACTOS IMPLEMENTADOS
    # ===================================================

    def calcular_costo(self):
        """
        Calcula el costo total del alquiler.

        Fórmula:
            precio_base × cantidad × días
        """

        return self.precio_base * self.cantidad * self.dias

    def descripcion(self):
        """
        Devuelve una descripción del servicio.
        """

        return (
            f"Alquiler de {self.cantidad} equipos "
            f"durante {self.dias} días."
        )

    # ===================================================
    # MOSTRAR INFORMACIÓN
    # ===================================================

    def mostrar_informacion(self):
        """
        Muestra toda la información del servicio.
        """

        print("=" * 50)
        print("SERVICIO: ALQUILER DE EQUIPOS")
        print("=" * 50)
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio por equipo: ${self.precio_base:,.2f}")
        print(f"Cantidad de equipos: {self.cantidad}")
        print(f"Días: {self.dias}")
        print(f"Costo total: ${self.calcular_costo():,.2f}")
        print("=" * 50)
