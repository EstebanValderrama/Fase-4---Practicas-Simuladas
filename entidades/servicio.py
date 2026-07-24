"""
=========================================================
Archivo: servicio.py

Descripción:
Este archivo contiene la clase abstracta Servicio.

La clase Servicio representa cualquier servicio ofrecido
por la empresa Software FJ.

Es una clase abstracta, por lo tanto no puede ser
instanciada directamente.

De ella heredarán:

- ReservaSala
- AlquilerEquipo
- Asesoria

Autor: Grupo de trabajo
=========================================================
"""

from abc import ABC, abstractmethod

# Excepción personalizada
from excepciones.excepciones import ServicioInvalidoError

# Logger del sistema
from utilidades.logger import Logger


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio.

    Todo servicio posee:

    - código
    - nombre
    - precio base

    Además todas las clases hijas deberán implementar
    los métodos calcular_costo() y descripcion().
    """

    def __init__(self, codigo, nombre, precio_base):
        """
        Constructor de la clase.

        Parámetros:
            codigo (str)
            nombre (str)
            precio_base (float)
        """

        self.__codigo = ""
        self.__nombre = ""
        self.__precio_base = 0

        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base

    # ==================================================
    # GETTERS
    # ==================================================

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    # ==================================================
    # SETTERS
    # ==================================================

    @codigo.setter
    def codigo(self, nuevo_codigo):

        if not nuevo_codigo.strip():

            error = ServicioInvalidoError(
                "El código del servicio no puede estar vacío."
            )

            Logger.registrar_error(error)

            raise error

        self.__codigo = nuevo_codigo

    @nombre.setter
    def nombre(self, nuevo_nombre):

        if not nuevo_nombre.strip():

            error = ServicioInvalidoError(
                "El nombre del servicio no puede estar vacío."
            )

            Logger.registrar_error(error)

            raise error

        self.__nombre = nuevo_nombre

    @precio_base.setter
    def precio_base(self, nuevo_precio):

        if nuevo_precio <= 0:

            error = ServicioInvalidoError(
                "El precio base debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__precio_base = nuevo_precio

    # ==================================================
    # MÉTODOS ABSTRACTOS
    # ==================================================

    @abstractmethod
    def calcular_costo(self):
        """
        Calcula el costo del servicio.

        Cada clase hija implementará este método.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Devuelve una descripción del servicio.

        Cada clase hija implementará este método.
        """
        pass

    # ==================================================
    # MÉTODO CON PARÁMETRO OPCIONAL
    # ==================================================

    def calcular_costo_total(self, impuesto=0, descuento=0):
        """
        Calcula el costo total del servicio.

        Parámetros:

        impuesto (float)
            Porcentaje de impuesto.

        descuento (float)
            Porcentaje de descuento.

        Retorna:
            float
        """

        costo = self.calcular_costo()

        if descuento > 0:
            costo -= costo * (descuento / 100)

        if impuesto > 0:
            costo += costo * (impuesto / 100)

        return costo
