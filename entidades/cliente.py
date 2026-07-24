"""
=========================================================
Archivo: cliente.py

Descripción:
Este archivo contiene la clase Cliente.

La clase Cliente hereda de Entidad y representa a una
persona que puede realizar reservas de los servicios
ofrecidos por Software FJ.

Incluye validaciones para:
- Nombre
- Correo electrónico
- Teléfono

Autor: Grupo de trabajo
=========================================================
"""

# Importamos la clase Entidad
from entidades.entidad import Entidad

# Librería para validar correos electrónicos mediante expresiones regulares
import re


class Cliente(Entidad):
    """
    Representa un cliente del sistema.

    Hereda los atributos:
        - id
        - nombre

    Agrega:
        - correo
        - telefono
    """

    def __init__(self, id_entidad, nombre, correo, telefono):
        """
        Constructor de la clase Cliente.

        Parámetros:
            id_entidad (int): Identificador del cliente.
            nombre (str): Nombre del cliente.
            correo (str): Correo electrónico.
            telefono (str): Número telefónico.
        """

        # Llamamos al constructor de la clase padre
        super().__init__(id_entidad, nombre)

        # Inicializamos los atributos privados
        self.__correo = ""
        self.__telefono = ""

        # Utilizamos los setters para validar los datos
        self.correo = correo
        self.telefono = telefono

    # ===================================================
    # GETTERS
    # ===================================================

    @property
    def correo(self):
        """Devuelve el correo del cliente."""
        return self.__correo

    @property
    def telefono(self):
        """Devuelve el teléfono del cliente."""
        return self.__telefono

    # ===================================================
    # SETTERS
    # ===================================================

    @correo.setter
    def correo(self, nuevo_correo):
        """
        Valida que el correo tenga un formato correcto.

        Ejemplo válido:
            usuario@gmail.com
        """

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, nuevo_correo):
            raise ValueError("El correo electrónico no es válido.")

        self.__correo = nuevo_correo

    @telefono.setter
    def telefono(self, nuevo_telefono):
        """
        Valida que el teléfono contenga únicamente números
        y tenga entre 7 y 15 dígitos.
        """

        if not nuevo_telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números.")

        if len(nuevo_telefono) < 7 or len(nuevo_telefono) > 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos.")

        self.__telefono = nuevo_telefono

    # ===================================================
    # MÉTODO HEREDADO DE LA CLASE ABSTRACTA
    # ===================================================

    def mostrar_informacion(self):
        """
        Muestra toda la información del cliente.

        Este método implementa el método abstracto
        definido en la clase Entidad.
        """

        print("=" * 40)
        print("INFORMACIÓN DEL CLIENTE")
        print("=" * 40)
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        print("=" * 40)
