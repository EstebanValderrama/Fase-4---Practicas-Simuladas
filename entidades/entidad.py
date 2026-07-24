"""
=========================================================
Archivo: entidad.py

Descripción:
Este archivo contiene la clase abstracta Entidad.

La clase Entidad representa cualquier objeto principal
del sistema que tenga un identificador y un nombre.

No puede ser instanciada directamente; únicamente sirve
como clase base para otras clases como Cliente.

Autor: Grupo de trabajo
=========================================================
"""

# Importamos ABC y abstractmethod para crear clases abstractas
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general del sistema.

    Toda entidad tendrá:
        - Un identificador único.
        - Un nombre.

    Esta clase será heredada por otras clases.
    """

    def __init__(self, id_entidad, nombre):
        """
        Constructor de la clase.

        Parámetros:
            id_entidad (int): Identificador único.
            nombre (str): Nombre de la entidad.
        """

        # Utilizamos atributos privados para aplicar encapsulación.
        self.__id = id_entidad
        self.__nombre = nombre

    # ==========================
    # GETTERS
    # ==========================

    @property
    def id(self):
        """
        Devuelve el identificador de la entidad.
        """
        return self.__id

    @property
    def nombre(self):
        """
        Devuelve el nombre de la entidad.
        """
        return self.__nombre

    # ==========================
    # SETTERS
    # ==========================

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """
        Permite modificar el nombre de la entidad.

        Se valida que el nombre no esté vacío.
        """

        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self.__nombre = nuevo_nombre

    # ==========================
    # MÉTODO ABSTRACTO
    # ==========================

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto.

        Cada clase hija deberá implementar este método
        para mostrar su información.
        """
        pass
