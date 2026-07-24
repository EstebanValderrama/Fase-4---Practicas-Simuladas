"""
=========================================================
Archivo: asesoria.py

Descripción:
Este archivo contiene la clase Asesoria.

Representa el servicio de asesorías especializadas que
ofrece Software FJ.

Esta clase hereda de Servicio e implementa los métodos
abstractos definidos en la clase padre.

Autor: Grupo de trabajo
=========================================================
"""

# Importamos la clase padre
from entidades.servicio import Servicio


class Asesoria(Servicio):
    """
    Representa un servicio de asesoría especializada.

    Atributos:
        especialidad (str): Área de la asesoría.
        horas (int): Cantidad de horas contratadas.
    """

    def __init__(self, codigo, nombre, precio_base, especialidad, horas):
        """
        Constructor de la clase.

        Parámetros:
            codigo (str): Código del servicio.
            nombre (str): Nombre del servicio.
            precio_base (float): Precio por hora.
            especialidad (str): Área de conocimiento.
            horas (int): Horas contratadas.
        """

        # Inicializamos los atributos heredados
        super().__init__(codigo, nombre, precio_base)

        self.__especialidad = ""
        self.__horas = 0

        # Utilizamos los setters para validar los datos
        self.especialidad = especialidad
        self.horas = horas

    # ===================================================
    # GETTERS
    # ===================================================

    @property
    def especialidad(self):
        """Devuelve la especialidad de la asesoría."""
        return self.__especialidad

    @property
    def horas(self):
        """Devuelve la cantidad de horas contratadas."""
        return self.__horas

    # ===================================================
    # SETTERS
    # ===================================================

    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        """
        Valida que la especialidad no esté vacía.
        """

        if not nueva_especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía.")

        self.__especialidad = nueva_especialidad

    @horas.setter
    def horas(self, nuevas_horas):
        """
        Valida que las horas sean mayores que cero.
        """

        if nuevas_horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        self.__horas = nuevas_horas

    # ===================================================
    # MÉTODOS ABSTRACTOS IMPLEMENTADOS
    # ===================================================

    def calcular_costo(self):
        """
        Calcula el costo de la asesoría.

        Fórmula:
            precio_base × horas
        """

        return self.precio_base * self.horas

    def descripcion(self):
        """
        Devuelve una descripción del servicio.
        """

        return (
            f"Asesoría especializada en "
            f"{self.especialidad} durante "
            f"{self.horas} horas."
        )

    # ===================================================
    # MOSTRAR INFORMACIÓN
    # ===================================================

    def mostrar_informacion(self):
        """
        Muestra toda la información del servicio.
        """

        print("=" * 50)
        print("SERVICIO: ASESORÍA ESPECIALIZADA")
        print("=" * 50)
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Precio por hora: ${self.precio_base:,.2f}")
        print(f"Horas contratadas: {self.horas}")
        print(f"Costo total: ${self.calcular_costo():,.2f}")
        print("=" * 50)
