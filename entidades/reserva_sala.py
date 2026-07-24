"""
=========================================================
Archivo: reserva_sala.py

Descripción:
Clase que representa el servicio de reserva de salas.

Hereda de la clase abstracta Servicio.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""

from entidades.servicio import Servicio

from excepciones.excepciones import ServicioInvalidoError
from utilidades.logger import Logger


class ReservaSala(Servicio):
    """
    Servicio de reserva de una sala.
    """

    def __init__(self, codigo, nombre, precio_base, capacidad, horas):

        super().__init__(codigo, nombre, precio_base)

        self.capacidad = capacidad
        self.horas = horas

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):

        if valor <= 0:

            error = ServicioInvalidoError(
                "La capacidad debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__capacidad = valor

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, valor):

        if valor <= 0:

            error = ServicioInvalidoError(
                "Las horas deben ser mayores que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__horas = valor

    # ==================================================
    # MÉTODOS HEREDADOS
    # ==================================================

    def calcular_costo(self):
        """
        Calcula el costo de la reserva.
        """

        return self.precio_base * self.horas

    def descripcion(self):

        return (
            f"Reserva de sala para "
            f"{self.capacidad} personas "
            f"durante {self.horas} horas."
        )

    def mostrar_informacion(self):

        print("\n========== RESERVA DE SALA ==========")
        print(f"Código       : {self.codigo}")
        print(f"Nombre       : {self.nombre}")
        print(f"Capacidad    : {self.capacidad} personas")
        print(f"Horas        : {self.horas}")
        print(f"Precio Base  : ${self.precio_base:,.2f}")
        print(f"Costo Total  : ${self.calcular_costo():,.2f}")
        print("=====================================")
