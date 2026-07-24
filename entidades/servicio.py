"""
=========================================================
Archivo: servicio.py

Descripción:
Clase abstracta que representa cualquier servicio
ofrecido por la empresa.

Todas las clases de servicios heredan de esta clase.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""

from abc import ABC, abstractmethod

from excepciones.excepciones import ServicioInvalidoError
from utilidades.logger import Logger


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio.
    """

    def __init__(self, codigo, nombre, precio_base):

        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):

        valor = valor.strip()

        if not valor:

            error = ServicioInvalidoError(
                "El código del servicio no puede estar vacío."
            )

            Logger.registrar_error(error)

            raise error

        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        valor = valor.strip()

        if not valor:

            error = ServicioInvalidoError(
                "El nombre del servicio no puede estar vacío."
            )

            Logger.registrar_error(error)

            raise error

        self.__nombre = valor

    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor):

        if valor <= 0:

            error = ServicioInvalidoError(
                "El precio debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__precio_base = valor

    # ==================================================
    # MÉTODOS ABSTRACTOS
    # ==================================================

    @abstractmethod
    def calcular_costo(self):
        """
        Calcula el costo del servicio.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Devuelve una descripción del servicio.
        """
        pass

    @abstractmethod
    def mostrar_informacion(self):
        """
        Muestra la información del servicio.
        """
        pass

    # ==================================================
    # MÉTODO GENERAL
    # ==================================================

    def calcular_costo_total(self, impuesto=0, descuento=0):
        """
        Calcula el costo total aplicando impuestos
        y descuentos.
        """

        costo = self.calcular_costo()

        if descuento > 0:
            costo -= costo * descuento / 100

        if impuesto > 0:
            costo += costo * impuesto / 100

        return costo
