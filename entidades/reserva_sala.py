"""
=========================================================
Archivo: reserva_sala.py

Descripción:
Clase que representa el servicio de reserva de salas.

Hereda de la clase abstracta Servicio.

Autor: Grupo de trabajo
=========================================================
"""

from entidades.servicio import Servicio
from excepciones.excepciones import ServicioInvalidoError
from utilidades.logger import Logger


class ReservaSala(Servicio):
    """
    Clase que representa una reserva de sala.
    """

    def __init__(self, codigo, nombre, precio_base, capacidad, horas):

        super().__init__(codigo, nombre, precio_base)

        self.__capacidad = 0
        self.__horas = 0

        self.capacidad = capacidad
        self.horas = horas

    # ==========================================
    # GETTERS
    # ==========================================

    @property
    def capacidad(self):
        return self.__capacidad

    @property
    def horas(self):
        return self.__horas

    # ==========================================
    # SETTERS
    # ==========================================

    @capacidad.setter
    def capacidad(self, nueva_capacidad):

        if nueva_capacidad <= 0:

            error = ServicioInvalidoError(
                "La capacidad de la sala debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__capacidad = nueva_capacidad

    @horas.setter
    def horas(self, nuevas_horas):

        if nuevas_horas <= 0:

            error = ServicioInvalidoError(
                "Las horas de reserva deben ser mayores que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__horas = nuevas_horas

    # ==========================================
    # MÉTODOS HEREDADOS
    # ==========================================

    def calcular_costo(self):
        """
        Calcula el costo total de la reserva.

        Fórmula:
            precio_base × horas
        """

        return self.precio_base * self.horas

    def descripcion(self):
        """
        Devuelve una descripción del servicio.
        """

        return (
            f"Reserva de una sala para "
            f"{self.capacidad} personas durante "
            f"{self.horas} horas."
        )

    # ==========================================
    # MÉTODO ADICIONAL
    # ==========================================

    def mostrar_informacion(self):
        """
        Muestra toda la información del servicio.
        """

        print("\n========== RESERVA DE SALA ==========")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Horas: {self.horas}")
        print(f"Precio Base: ${self.precio_base:,.2f}")
        print(f"Costo Total: ${self.calcular_costo():,.2f}")
        print("=====================================")
