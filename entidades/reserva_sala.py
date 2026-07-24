"""
=========================================================
Archivo: reserva_sala.py

Descripción:
Este archivo contiene la clase ReservaSala.

Representa el servicio de alquiler de una sala por un
determinado número de horas.

Esta clase hereda de la clase abstracta Servicio e
implementa los métodos obligatorios definidos en ella.

Autor: Grupo de trabajo
=========================================================
"""

# Importamos la clase padre
from entidades.servicio import Servicio


class ReservaSala(Servicio):
    """
    Representa el servicio de reserva de una sala.

    Atributos:
        capacidad (int): Número máximo de personas.
        horas (int): Cantidad de horas reservadas.
    """

    def __init__(self, codigo, nombre, precio_base, capacidad, horas):
        """
        Constructor de la clase.

        Parámetros:
            codigo (str)
            nombre (str)
            precio_base (float)
            capacidad (int)
            horas (int)
        """

        # Llamamos al constructor de la clase padre
        super().__init__(codigo, nombre, precio_base)

        self.__capacidad = 0
        self.__horas = 0

        # Usamos setters para validar
        self.capacidad = capacidad
        self.horas = horas

    # ===================================================
    # GETTERS
    # ===================================================

    @property
    def capacidad(self):
        """Devuelve la capacidad de la sala."""
        return self.__capacidad

    @property
    def horas(self):
        """Devuelve la cantidad de horas reservadas."""
        return self.__horas

    # ===================================================
    # SETTERS
    # ===================================================

    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        """
        Valida que la capacidad sea mayor que cero.
        """

        if nueva_capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")

        self.__capacidad = nueva_capacidad

    @horas.setter
    def horas(self, nuevas_horas):
        """
        Valida que las horas sean mayores que cero.
        """

        if nuevas_horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        self.__horas = nuevas_horas

    # ===================================================
    # MÉTODOS ABSTRACTOS IMPLEMENTADOS
    # ===================================================

    def calcular_costo(self):
        """
        Calcula el costo de la reserva.

        Fórmula:
            precio_base × horas
        """

        return self.precio_base * self.horas

    def descripcion(self):
        """
        Devuelve una descripción del servicio.
        """

        return (
            f"Reserva de sala con capacidad para "
            f"{self.capacidad} personas durante "
            f"{self.horas} horas."
        )

    # ===================================================
    # MOSTRAR INFORMACIÓN
    # ===================================================

    def mostrar_informacion(self):
        """
        Muestra toda la información del servicio.
        """

        print("=" * 50)
        print("SERVICIO: RESERVA DE SALA")
        print("=" * 50)
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio por hora: ${self.precio_base:,.2f}")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"Horas: {self.horas}")
        print(f"Costo total: ${self.calcular_costo():,.2f}")
        print("=" * 50)
