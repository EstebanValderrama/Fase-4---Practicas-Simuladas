"""
=========================================================
Archivo: reserva.py

Descripción:
Este archivo contiene la clase Reserva.

La clase Reserva relaciona un cliente con un servicio,
permitiendo confirmar, cancelar y procesar reservas.

Autor: Grupo de trabajo
=========================================================
"""

# Importamos las clases necesarias
from entidades.cliente import Cliente
from entidades.servicio import Servicio


class Reserva:
    """
    Representa una reserva realizada por un cliente.

    Una reserva está compuesta por:

    - Cliente
    - Servicio
    - Duración
    - Estado
    """

    def __init__(self, cliente, servicio, duracion):
        """
        Constructor de la clase.

        Parámetros:
            cliente (Cliente): Cliente que realiza la reserva.
            servicio (Servicio): Servicio solicitado.
            duracion (int): Tiempo de duración.
        """

        # Verificamos que el objeto recibido sea un Cliente
        if not isinstance(cliente, Cliente):
            raise TypeError("El objeto recibido no es un Cliente.")

        # Verificamos que el objeto recibido sea un Servicio
        if not isinstance(servicio, Servicio):
            raise TypeError("El objeto recibido no es un Servicio.")

        # Validamos la duración
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    # ===================================================
    # GETTERS
    # ===================================================

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

    # ===================================================
    # MÉTODOS DE LA RESERVA
    # ===================================================

    def confirmar(self):
        """
        Cambia el estado de la reserva a Confirmada.
        """

        self.__estado = "Confirmada"

    def cancelar(self):
        """
        Cambia el estado de la reserva a Cancelada.
        """

        self.__estado = "Cancelada"

    def procesar(self):
        """
        Procesa la reserva.

        Si la reserva fue cancelada, no podrá procesarse.
        """

        if self.__estado == "Cancelada":
            raise Exception(
                "No es posible procesar una reserva cancelada."
            )

        self.__estado = "Procesada"

    # ===================================================
    # MOSTRAR INFORMACIÓN
    # ===================================================

    def mostrar_informacion(self):
        """
        Muestra toda la información de la reserva.
        """

        print("=" * 50)
        print("INFORMACIÓN DE LA RESERVA")
        print("=" * 50)
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Duración: {self.duracion}")
        print(f"Costo: ${self.servicio.calcular_costo():,.2f}")
        print(f"Estado: {self.estado}")
        print("=" * 50)
