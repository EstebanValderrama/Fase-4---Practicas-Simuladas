"""
=========================================================
Archivo: reserva.py

Descripción:
Clase que representa una reserva realizada por un cliente.

Relaciona un Cliente con un Servicio.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""

from entidades.cliente import Cliente
from entidades.servicio import Servicio

from excepciones.excepciones import ReservaError
from utilidades.logger import Logger


class Reserva:
    """
    Representa una reserva realizada por un cliente.
    """

    ESTADOS_VALIDOS = [
        "Pendiente",
        "Confirmada",
        "Cancelada"
    ]

    def __init__(self, cliente, servicio):

        if not isinstance(cliente, Cliente):

            error = ReservaError(
                "Debe proporcionar un cliente válido."
            )

            Logger.registrar_error(error)

            raise error

        if not isinstance(servicio, Servicio):

            error = ReservaError(
                "Debe proporcionar un servicio válido."
            )

            Logger.registrar_error(error)

            raise error

        self.__cliente = cliente
        self.__servicio = servicio
        self.estado = "Pendiente"

    # ==================================================
    # PROPIEDADES
    # ==================================================

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):

        if valor not in self.ESTADOS_VALIDOS:

            error = ReservaError(
                "Estado de reserva no válido."
            )

            Logger.registrar_error(error)

            raise error

        self.__estado = valor

    # ==================================================
    # MÉTODOS
    # ==================================================

    def confirmar(self):
        """
        Confirma la reserva.
        """

        self.estado = "Confirmada"

        Logger.registrar_evento(
            f"Reserva confirmada para {self.cliente.nombre}"
        )

    def cancelar(self):
        """
        Cancela la reserva.
        """

        self.estado = "Cancelada"

        Logger.registrar_evento(
            f"Reserva cancelada para {self.cliente.nombre}"
        )

    def costo_total(self):
        """
        Devuelve el costo total del servicio reservado.
        """

        return self.servicio.calcular_costo()

    def mostrar_informacion(self):
        """
        Muestra la información de la reserva.
        """

        print("\n============= RESERVA =============")
        print(f"Cliente : {self.cliente.nombre}")
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Estado  : {self.estado}")
        print(f"Costo   : ${self.costo_total():,.2f}")
        print("===================================")
