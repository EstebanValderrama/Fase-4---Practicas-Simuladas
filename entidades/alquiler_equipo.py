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

        self.__cantidad = 0
        self.__dias = 0

        self.cantidad = cantidad
        self.dias = dias

    # ==================================================
    # GETTERS
    # ==================================================

    @property
    def cantidad(self):
        """Devuelve la cantidad de equipos."""
        return self.__cantidad

    @property
    def dias(self):
        """Devuelve el número de días del alquiler."""
        return self.__dias

    # ==================================================
    # SETTERS
    # ==================================================

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        """
        Valida que la cantidad de equipos sea mayor que cero.
        """

        if nueva_cantidad <= 0:

            error = ServicioInvalidoError(
                "La cantidad de equipos debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__cantidad = nueva_cantidad

    @dias.setter
    def dias(self, nuevos_dias):
        """
        Valida que la cantidad de días sea mayor que cero.
        """

        if nuevos_dias <= 0:

            error = ServicioInvalidoError(
                "La cantidad de días debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__dias = nuevos_dias

    # ==================================================
    # MÉTODOS HEREDADOS
    # ==================================================

    def calcular_costo(self):
        """
        Calcula el costo del alquiler.

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

    # ==================================================
    # MÉTODO ADICIONAL
    # ==================================================

    def mostrar_informacion(self):
        """
        Muestra toda la información del servicio.
        """

        print("\n========== ALQUILER DE EQUIPOS ==========")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de equipos: {self.cantidad}")
        print(f"Días de alquiler: {self.dias}")
        print(f"Precio Base: ${self.precio_base:,.2f}")
        print(f"Costo Total: ${self.calcular_costo():,.2f}")
        print("=========================================")
