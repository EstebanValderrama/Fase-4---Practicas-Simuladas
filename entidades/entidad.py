"""
=========================================================
Archivo: entidad.py

Descripción:
Clase abstracta base para todas las entidades del sistema.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""

from abc import ABC, abstractmethod

from excepciones.excepciones import ErrorSistema


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad del sistema.
    """

    def __init__(self, id_entidad, nombre):

        self.id = id_entidad
        self.nombre = nombre

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):

        if not isinstance(valor, int):

            raise ErrorSistema(
                "El ID debe ser un número entero."
            )

        if valor <= 0:

            raise ErrorSistema(
                "El ID debe ser mayor que cero."
            )

        self.__id = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str):

            raise ErrorSistema(
                "El nombre debe ser una cadena."
            )

        valor = valor.strip()

        if not valor:

            raise ErrorSistema(
                "El nombre no puede estar vacío."
            )

        self.__nombre = valor

    # ==================================================
    # MÉTODO ABSTRACTO
    # ==================================================

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método que deberán implementar las clases hijas.
        """
        pass
