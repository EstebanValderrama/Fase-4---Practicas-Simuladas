"""
=========================================================
Archivo: alquiler_equipo.py

Descripción:
Clase que representa el servicio de alquiler de equipos.

Hereda de la clase abstracta Servicio.

Autor: Grupo de trabajo
=========================================================
"""

from entidades.servicio import Servicio

from excepciones.excepciones import ServicioInvalidoError
from utilidades.logger import Logger


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos.
    """

    def __init__(self, codigo, nombre, precio_base, cantidad, dias):

        super().__init__(codigo, nombre, precio_base)

        self.cantidad = cantidad
        self.dias = dias

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):

        if valor <= 0:

            error = ServicioInvalidoError(
                "La cantidad de equipos debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__cantidad = valor

    @property
    def dias(self):
        return self.__dias

    @dias.setter
    def dias(self, valor):

        if valor <= 0:

            error = ServicioInvalidoError(
                "La cantidad de días debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__dias = valor

    # ==================================================
    # MÉTODOS HEREDADOS
    # ==================================================

    def calcular_costo(self):
        """
        Calcula el costo total del alquiler.
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

    def mostrar_informacion(self):
        """
        Muestra la información del servicio.
        """

        print("\n======== ALQUILER DE EQUIPOS ========")
        print(f"Código      : {self.codigo}")
        print(f"Nombre      : {self.nombre}")
        print(f"Cantidad    : {self.cantidad}")
        print(f"Días        : {self.dias}")
        print(f"Precio Base : ${self.precio_base:,.2f}")
        print(f"Costo Total : ${self.calcular_costo():,.2f}")
        print("=====================================")
