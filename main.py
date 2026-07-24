"""
=========================================================
PROYECTO
Sistema Integral de Gestión de Clientes,
Servicios y Reservas

Archivo principal del sistema.

Autor: Carlos Esteban Valderrama Monroy
=========================================================
"""

# ==================================================
# IMPORTACIONES
# ==================================================

from entidades.cliente import Cliente
from entidades.reserva_sala import ReservaSala
from entidades.alquiler_equipo import AlquilerEquipo
from entidades.asesoria import Asesoria
from entidades.reserva import Reserva

from excepciones.excepciones import ErrorSistema
from utilidades.logger import Logger

# ==================================================
# LISTAS DEL SISTEMA
# ==================================================

clientes = []
servicios = []
reservas = []

# ==================================================
# FUNCIONES
# ==================================================

def registrar_cliente():

    print("\n========== REGISTRAR CLIENTE ==========")

    try:

        id_cliente = int(input("ID: "))
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")

        cliente = Cliente(
            id_cliente,
            nombre,
            correo,
            telefono
        )

        clientes.append(cliente)

        Logger.registrar_evento(
            f"Cliente registrado: {nombre}"
        )

        print("\nCliente registrado correctamente.")

    except ErrorSistema as error:

        print("\nERROR:", error)

    except Exception as error:

        Logger.registrar_error(error)

        print("\nOcurrió un error inesperado.")

    finally:

        print("Proceso finalizado.")


# ==================================================

def registrar_servicio():

    print("\n========== REGISTRAR SERVICIO ==========")

    print("1. Reserva de Sala")
    print("2. Alquiler de Equipos")
    print("3. Asesoría")

    opcion = input("Seleccione una opción: ")

    try:

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio Base: "))

        if opcion == "1":

            capacidad = int(input("Capacidad: "))
            horas = int(input("Horas: "))

            servicio = ReservaSala(
                codigo,
                nombre,
                precio,
                capacidad,
                horas
            )

        elif opcion == "2":

            cantidad = int(input("Cantidad de equipos: "))
            dias = int(input("Días: "))

            servicio = AlquilerEquipo(
                codigo,
                nombre,
                precio,
                cantidad,
                dias
            )

        elif opcion == "3":

            especialidad = input("Especialidad: ")
            horas = int(input("Horas: "))

            servicio = Asesoria(
                codigo,
                nombre,
                precio,
                especialidad,
                horas
            )

        else:

            print("Opción inválida.")
            return

        servicios.append(servicio)

        Logger.registrar_evento(
            f"Servicio registrado: {nombre}"
        )

        print("\nServicio registrado correctamente.")

    except ErrorSistema as error:

        print("\nERROR:", error)

    except Exception as error:

        Logger.registrar_error(error)

        print("\nOcurrió un error inesperado.")

    finally:

        print("Proceso finalizado.")


# ==================================================

def crear_reserva():

    print("\n========== CREAR RESERVA ==========")

    try:

        if len(clientes) == 0:

            print("No existen clientes registrados.")
            return

        if len(servicios) == 0:

            print("No existen servicios registrados.")
            return

        print("\nCLIENTES")

        for indice, cliente in enumerate(clientes):

            print(f"{indice + 1}. {cliente.nombre}")

        cliente = clientes[
            int(input("Seleccione un cliente: ")) - 1
        ]

        print("\nSERVICIOS")

        for indice, servicio in enumerate(servicios):

            print(f"{indice + 1}. {servicio.nombre}")

        servicio = servicios[
            int(input("Seleccione un servicio: ")) - 1
        ]

        reserva = Reserva(
            cliente,
            servicio
        )

        reserva.confirmar()

        reservas.append(reserva)

        print("\nReserva creada correctamente.")

        Logger.registrar_evento(
            f"Reserva creada para {cliente.nombre}"
        )

    except ErrorSistema as error:

        print("\nERROR:", error)

    except Exception as error:

        Logger.registrar_error(error)

        print("\nOcurrió un error inesperado.")

    finally:

        print("Proceso finalizado.")


# ==================================================

def mostrar_clientes():

    print("\n========== CLIENTES ==========")

    if len(clientes) == 0:

        print("No existen clientes.")

        return

    for cliente in clientes:

        cliente.mostrar_informacion()


# ==================================================

def mostrar_servicios():

    print("\n========== SERVICIOS ==========")

    if len(servicios) == 0:

        print("No existen servicios.")

        return

    # POLIMORFISMO
    for servicio in servicios:

        servicio.mostrar_informacion()


# ==================================================

def mostrar_reservas():

    print("\n========== RESERVAS ==========")

    if len(reservas) == 0:

        print("No existen reservas.")

        return

    for reserva in reservas:

        reserva.mostrar_informacion()
# ==================================================
# MENÚ PRINCIPAL
# ==================================================

def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """

    print("\n" + "=" * 50)
    print(" SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES")
    print("=" * 50)
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Mostrar clientes")
    print("5. Mostrar servicios")
    print("6. Mostrar reservas")
    print("7. Salir")
    print("=" * 50)


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

def main():
    """
    Función principal del programa.
    """

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            registrar_cliente()

        elif opcion == "2":

            registrar_servicio()

        elif opcion == "3":

            crear_reserva()

        elif opcion == "4":

            mostrar_clientes()

        elif opcion == "5":

            mostrar_servicios()

        elif opcion == "6":

            mostrar_reservas()

        elif opcion == "7":

            print("\nGracias por utilizar el sistema.")

            Logger.registrar_evento(
                "El sistema fue cerrado correctamente."
            )

            break

        else:

            print("\nOpción inválida.")


# ==================================================
# INICIO DEL PROGRAMA
# ==================================================

if __name__ == "__main__":

    try:

        Logger.registrar_evento(
            "Sistema iniciado."
        )

        main()

    except KeyboardInterrupt:

        print("\n\nPrograma cancelado por el usuario.")

        Logger.registrar_advertencia(
            "El usuario canceló la ejecución con el teclado."
        )

    except Exception as error:

        Logger.registrar_error(error)

        print("\nHa ocurrido un error inesperado.")

    finally:

        Logger.registrar_evento(
            "Fin de la ejecución del programa."
        )
