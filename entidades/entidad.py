"""
=========================================================
Archivo: entidad.py

Descripción:
Clase abstracta base para todas las entidades del sistema.

Autor: Grupo de trabajo
=========================================================
"""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad del sistema.

    Toda entidad posee:
    - id
    - nombre
    """

    def __init__(self, id_entidad, nombre):

        self.id = id_entidad
        self.nombre = nombre

    # ==========================================
    # PROPIEDADES
    # ==========================================

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):

        if valor <= 0:
            raise ValueError(
                "El ID debe ser mayor que cero."
            )

        self.__id = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        self.__nombre = valor.strip()

    # ==========================================
    # MÉTODO ABSTRACTO
    # ==========================================

    @abstractmethod
    def mostrar_informacion(self):
        """
        Muestra la información de la entidad.
        """
        pass
