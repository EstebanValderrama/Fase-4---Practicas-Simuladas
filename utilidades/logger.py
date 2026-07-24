"""
=========================================================
Archivo: logger.py

Descripción:
Clase encargada de registrar eventos y errores
del sistema en el archivo logs/errores.log

Autor: Grupo de trabajo
=========================================================
"""

from datetime import datetime
import os


class Logger:

    # Ruta del archivo de logs
    ARCHIVO_LOG = "logs/errores.log"

    @staticmethod
    def registrar_evento(mensaje):
        """
        Registra un evento del sistema.
        """

        os.makedirs("logs", exist_ok=True)

        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:

            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            archivo.write(
                f"[EVENTO] {fecha} -> {mensaje}\n"
            )

    @staticmethod
    def registrar_error(error):
        """
        Registra un error ocurrido.
        """

        os.makedirs("logs", exist_ok=True)

        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:

            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            archivo.write(
                f"[ERROR] {fecha} -> {type(error).__name__}: {error}\n"
            )

