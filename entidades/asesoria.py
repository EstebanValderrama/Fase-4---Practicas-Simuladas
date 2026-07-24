"""
=========================================================
Archivo: asesoria.py

Descripción:
Clase que representa el servicio de asesoría.

Hereda de la clase abstracta Servicio.

Autor: Grupo de trabajo
=========================================================
"""

from entidades.servicio import Servicio
from excepciones.excepciones import ServicioInvalidoError
from utilidades.logger import Logger


class Asesoria(Servicio):
    """
    Representa el servicio de asesoría especializada.
    """

    def __init__(self, codigo, nombre, precio_base, especialidad, horas):

        super().__init__(codigo, nombre, precio_base)

        self.__especialidad = ""
        self.__horas = 0

        self.especialidad = especialidad
        self.horas = horas

    # ==================================================
    # GETTERS
    # ==================================================

    @property
    def especialidad(self):
        """Devuelve la especialidad de la asesoría."""
        return self.__especialidad

    @property
    def horas(self):
        """Devuelve la cantidad de horas contratadas."""
        return self.__horas

    # ==================================================
    # SETTERS
    # ==================================================

    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        """
        Valida que la especialidad no esté vacía.
        """

        if not nueva_especialidad.strip():

            error = ServicioInvalidoError(
                "La especialidad no puede estar vacía."
            )

            Logger.registrar_error(error)

            raise error

        self.__especialidad = nueva_especialidad

    @horas.setter
    def horas(self, nuevas_horas):
        """
        Valida que la cantidad de horas sea mayor que cero.
        """

        if nuevas_horas <= 0:

            error = ServicioInvalidoError(
                "Las horas de asesoría deben ser mayores que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__horas = nuevas_horas

    # ==================================================
    # MÉTODOS HEREDADOS
    # ==================================================

    def calcular_costo(self):
        """
        Calcula el costo del servicio.

        Fórmula:
            precio_base × horas
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

    # ==================================================
    # MÉTODO ADICIONAL
    # ==================================================

    def mostrar_informacion(self):
        """
        Muestra toda la información del servicio.
        """

        print("\n========== SERVICIO DE ASESORÍA ==========")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Horas contratadas: {self.horas}")
        print(f"Precio Base: ${self.precio_base:,.2f}")
        print(f"Costo Total: ${self.calcular_costo():,.2f}")
        print("==========================================")
