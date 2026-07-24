"""
=========================================================
Archivo: servicio.py

Descripción:
Este archivo contiene la clase abstracta Servicio.

La clase Servicio representa cualquier servicio que ofrece
la empresa Software FJ.

No puede ser utilizada directamente; únicamente sirve como
base para crear servicios específicos como:

- Reserva de salas
- Alquiler de equipos
- Asesorías especializadas

Autor: Grupo de trabajo
=========================================================
"""

# Importamos las herramientas necesarias para crear una clase abstracta
from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio general.

    Todos los servicios del sistema tendrán:

    - Código
    - Nombre
    - Precio base

    Además, cada servicio deberá implementar su propia
    forma de calcular el costo y mostrar su descripción.
    """

    def __init__(self, codigo, nombre, precio_base):
        """
        Constructor de la clase Servicio.

        Parámetros:
            codigo (str): Código único del servicio.
            nombre (str): Nombre del servicio.
            precio_base (float): Precio inicial del servicio.
        """

        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio_base = 0

        # Utilizamos el setter para validar el precio
        self.precio_base = precio_base

    # ===================================================
    # GETTERS
    # ===================================================

    @property
    def codigo(self):
        """Devuelve el código del servicio."""
        return self.__codigo

    @property
    def nombre(self):
        """Devuelve el nombre del servicio."""
        return self.__nombre

    @property
    def precio_base(self):
        """Devuelve el precio base del servicio."""
        return self.__precio_base

    # ===================================================
    # SETTERS
    # ===================================================

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """
        Permite modificar el nombre del servicio.

        El nombre no puede estar vacío.
        """

        if not nuevo_nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        self.__nombre = nuevo_nombre

    @precio_base.setter
    def precio_base(self, nuevo_precio):
        """
        Valida que el precio base sea mayor que cero.
        """

        if nuevo_precio <= 0:
            raise ValueError("El precio base debe ser mayor que cero.")

        self.__precio_base = nuevo_precio

    # ===================================================
    # MÉTODOS ABSTRACTOS
    # ===================================================

    @abstractmethod
    def calcular_costo(self):
        """
        Cada servicio calculará su costo de manera diferente.

        Este método deberá implementarse en las clases hijas.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Devuelve una descripción del servicio.

        Cada servicio tendrá una descripción distinta.
        """
        pass

    # ===================================================
    # MÉTODO SOBRECARGADO (mediante parámetro opcional)
    # ===================================================

    def calcular_costo_total(self, impuesto=0):
        """
        Calcula el costo total del servicio.

        Parámetros:
            impuesto (float): Porcentaje de impuesto.
                              Ejemplo: 19 representa el 19%.

        Retorna:
            float: Valor final del servicio.
        """

        costo = self.calcular_costo()

        if impuesto > 0:
            costo += costo * (impuesto / 100)

        return costo
