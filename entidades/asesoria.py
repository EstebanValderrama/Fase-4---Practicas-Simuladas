"""
=========================================================
Archivo: asesoria.py

Descripción:
Clase que representa el servicio de asesoría.

Hereda de la clase abstracta Servicio.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""

from entidades.servicio import Servicio

from excepciones.excepciones import ServicioInvalidoError
from utilidades.logger import Logger


class Asesoria(Servicio):
    """
    Representa un servicio de asesoría especializada.
    """

    def __init__(self, codigo, nombre, precio_base, especialidad, horas):

        super().__init__(codigo, nombre, precio_base)

        self.especialidad = especialidad
        self.horas = horas

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):

        valor = valor.strip()

        if not valor:

            error = ServicioInvalidoError(
                "La especialidad no puede estar vacía."
            )

            Logger.registrar_error(error)

            raise error

        self.__especialidad = valor

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
        Calcula el costo del servicio.
        """

        return self.precio_base * self.horas

    def descripcion(self):
        """
        Devuelve una descripción del servicio.
        """

        return (
            f"Asesoría especializada en "
            f"{self.especialidad} durante "
            f"{self.horas} horas."
        )

    def mostrar_informacion(self):
        """
        Muestra la información del servicio.
        """

        print("\n========== SERVICIO DE ASESORÍA ==========")
        print(f"Código       : {self.codigo}")
        print(f"Nombre       : {self.nombre}")
        print(f"Especialidad : {self.especialidad}")
        print(f"Horas        : {self.horas}")
        print(f"Precio Base  : ${self.precio_base:,.2f}")
        print(f"Costo Total  : ${self.calcular_costo():,.2f}")
        print("==========================================")
