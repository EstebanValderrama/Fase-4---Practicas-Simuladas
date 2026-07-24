"""
=========================================================
Archivo: cliente.py

Descripción:
Clase Cliente del sistema.

Hereda de la clase abstracta Entidad y representa
a un cliente que puede realizar reservas.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""

import re

from entidades.entidad import Entidad
from excepciones.excepciones import ClienteInvalidoError
from utilidades.logger import Logger


class Cliente(Entidad):
    """
    Representa un cliente del sistema.

    Hereda:
        - id
        - nombre

    Agrega:
        - correo
        - telefono
    """

    def __init__(self, id_entidad, nombre, correo, telefono):

        super().__init__(id_entidad, nombre)

        self.correo = correo
        self.telefono = telefono

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, valor):

            error = ClienteInvalidoError(
                "Correo electrónico inválido."
            )

            Logger.registrar_error(error)

            raise error

        self.__correo = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor.isdigit():

            error = ClienteInvalidoError(
                "El teléfono solo debe contener números."
            )

            Logger.registrar_error(error)

            raise error

        if len(valor) < 7 or len(valor) > 15:

            error = ClienteInvalidoError(
                "El teléfono debe tener entre 7 y 15 dígitos."
            )

            Logger.registrar_error(error)

            raise error

        self.__telefono = valor

    # ==================================================
    # MÉTODOS
    # ==================================================

    def mostrar_informacion(self):

        print("\n========== CLIENTE ==========")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        print("=============================")
