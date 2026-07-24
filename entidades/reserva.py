"""
=========================================================
Archivo: reserva.py

Descripción:
Clase que representa una reserva realizada por un cliente.

Relaciona un Cliente con un Servicio y permite
confirmar, cancelar y procesar reservas.

Autor: Grupo de trabajo
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

    def __init__(self, cliente, servicio, duracion):

        # Validar que el objeto recibido sea un Cliente
        if not isinstance(cliente, Cliente):

            error = ReservaError(
                "El objeto recibido no corresponde a un Cliente."
            )

            Logger.registrar_error(error)

            raise error

        # Validar que el objeto recibido sea un Servicio
        if not isinstance(servicio, Servicio):

            error = ReservaError(
                "El objeto recibido no corresponde a un Servicio."
            )

            Logger.registrar_error(error)

            raise error

        # Validar la duración
        if duracion <= 0:

            error = ReservaError(
                "La duración de la reserva debe ser mayor que cero."
            )

            Logger.registrar_error(error)

            raise error

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    # ==================================================
    # GETTERS
    # ==================================================

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    # ==================================================
    # MÉTODOS
    # ==================================================

    def confirmar(self):
        """
        Confirma la reserva.
        """

        self.__estado = "Confirmada"

        Logger.registrar_evento(
            f"Reserva confirmada para el cliente {self.cliente.nombre}."
        )

    def cancelar(self):
        """
        Cancela la reserva.
        """

        self.__estado = "Cancelada"

        Logger.registrar_evento(
            f"Reserva cancelada para el cliente {self.cliente.nombre}."
        )

    def procesar(self):
        """
        Procesa la reserva.
        """

        if self.__estado == "Cancelada":

            error = ReservaError(
                "No es posible procesar una reserva cancelada."
            )

            Logger.registrar_error(error)

            raise error

        self.__estado = "Procesada"

        Logger.registrar_evento(
            f"Reserva procesada para el cliente {self.cliente.nombre}."
        )

    def mostrar_informacion(self):
        """
        Muestra toda la información de la reserva.
        """

        print("\n============= RESERVA =============")
        print(f"Cliente : {self.cliente.nombre}")
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Duración: {self.duracion}")
        print(f"Estado  : {self.estado}")
        print(
            f"Costo   : ${self.servicio.calcular_costo():,.2f}"
        )
        print("===================================")
