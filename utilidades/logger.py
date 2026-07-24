"""
=========================================================
Archivo: logger.py

Descripción:
Clase encargada de registrar los eventos, advertencias
y errores del sistema en el archivo errores.log.

Autor: Grupo de trabajo
=========================================================
"""

from datetime import datetime
import os


class Logger:
    """
    Clase encargada de registrar información en el archivo
    de log del sistema.
    """

    ARCHIVO_LOG = "logs/errores.log"

    @staticmethod
    def __escribir(tipo, mensaje):
        """
        Método privado que escribe la información en el log.
        """

        # Crear la carpeta logs si no existe
        os.makedirs("logs", exist_ok=True)

        # Obtener fecha y hora actual
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Escribir en el archivo
        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{tipo}] {fecha} -> {mensaje}\n")

    @staticmethod
    def registrar_evento(mensaje):
        """
        Registra un evento normal del sistema.
        """
        Logger.__escribir("EVENTO", mensaje)

    @staticmethod
    def registrar_advertencia(mensaje):
        """
        Registra una advertencia.
        """
        Logger.__escribir("ADVERTENCIA", mensaje)

    @staticmethod
    def registrar_error(error):
        """
        Registra un error del sistema.
        """

        mensaje = f"{type(error).__name__}: {error}"

        Logger.__escribir("ERROR", mensaje)
