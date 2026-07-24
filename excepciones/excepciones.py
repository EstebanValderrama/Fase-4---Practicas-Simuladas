"""
=========================================================
Archivo: excepciones.py

Descripción:
Este archivo contiene todas las excepciones
personalizadas del sistema.

Las excepciones permiten identificar de manera clara
los diferentes errores que pueden ocurrir durante la
ejecución del programa.

Autor: Grupo de trabajo
=========================================================
"""


class ClienteInvalidoError(Exception):
    """
    Se genera cuando los datos de un cliente no son válidos.

    Ejemplos:
    - Correo inválido.
    - Teléfono incorrecto.
    - Nombre vacío.
    """

    def __init__(self, mensaje):
        super().__init__(mensaje)


class ServicioInvalidoError(Exception):
    """
    Se genera cuando un servicio contiene información
    incorrecta.

    Ejemplos:
    - Precio negativo.
    - Código vacío.
    - Nombre vacío.
    """

    def __init__(self, mensaje):
        super().__init__(mensaje)


class ReservaError(Exception):
    """
    Se genera cuando ocurre un problema durante
    una reserva.

    Ejemplos:
    - Reserva inexistente.
    - Reserva cancelada.
    - Datos incompletos.
    """

    def __init__(self, mensaje):
        super().__init__(mensaje)


class ServicioNoDisponibleError(Exception):
    """
    Se genera cuando un servicio solicitado
    no está disponible.
    """

    def __init__(self, mensaje):
        super().__init__(mensaje)


class CostoInvalidoError(Exception):
    """
    Se genera cuando el cálculo del costo
    produce un resultado inválido.
    """

    def __init__(self, mensaje):
        super().__init__(mensaje)
