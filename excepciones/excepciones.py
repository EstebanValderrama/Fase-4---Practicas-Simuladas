"""
=========================================================
Archivo: excepciones.py

Descripción:
Contiene todas las excepciones personalizadas utilizadas
en el Sistema Integral de Gestión de Clientes,
Servicios y Reservas.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""


class ErrorSistema(Exception):
    """
    Clase base para todas las excepciones del sistema.
    """

    pass


class ClienteInvalidoError(ErrorSistema):
    """
    Se produce cuando los datos del cliente
    son inválidos.
    """

    pass


class ServicioInvalidoError(ErrorSistema):
    """
    Se produce cuando los datos de un servicio
    son inválidos.
    """

    pass


class ReservaError(ErrorSistema):
    """
    Se produce cuando ocurre un problema
    relacionado con una reserva.
    """

    pass


class ServicioNoDisponibleError(ErrorSistema):
    """
    Se produce cuando un servicio
    no se encuentra disponible.
    """

    pass


class CostoInvalidoError(ErrorSistema):
    """
    Se produce cuando el costo calculado
    es inválido.
    """

    pass
