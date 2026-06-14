import csv
import os

NOMBRE_ARCHIVO_CSV = "paises.csv"

CABECERAS_CSV = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises_desde_csv(nombre_archivo):
    pass


def guardar_paises_en_csv(lista_paises, nombre_archivo):
    pass


def leer_entero_positivo(mensaje_prompt):
    pass


def leer_texto_no_vacio(mensaje_prompt):
    pass


def leer_opcion_menu(opciones_validas, mensaje_prompt="Opción: "):
    pass


def agregar_pais(lista_paises):
    pass


def actualizar_pais(lista_paises):
    pass


def buscar_pais_exacto(lista_paises, nombre_buscado):
    pass


def buscar_paises_por_nombre(lista_paises):
    pass


def filtrar_por_continente(lista_paises):
    pass


def filtrar_por_rango_poblacion(lista_paises):
    pass


def filtrar_por_rango_superficie(lista_paises):
    pass


def menu_filtros(lista_paises):
    pass


def ordenar_paises(lista_paises):
    pass


def mostrar_estadisticas(lista_paises):
    pass


def mostrar_tabla_paises(lista_paises):
    pass


def mostrar_menu_principal():
    pass


def main():
    """
    Función principal: carga los datos desde CSV, ejecuta el menú en bucle
    y guarda los cambios al salir.
    """
    print("Iniciando sistema de gestión de países...")
    lista_paises = cargar_paises_desde_csv(NOMBRE_ARCHIVO_CSV)
    print(f"{len(lista_paises)} país/es cargados desde '{NOMBRE_ARCHIVO_CSV}'.")
    opciones_principales = [ "0", "1", "2", "3", "4", "5", "6", "7"]
    while True:
        mostrar_menu_principal()
        opcion_elegida = leer_opcion_menu(opciones_principales)
        if opcion_elegida == "1":
            agregar_pais(lista_paises)
            guardar_paises_en_csv(lista_paises, NOMBRE_ARCHIVO_CSV)
        elif opcion_elegida == "2":
            actualizar_pais(lista_paises)
            guardar_paises_en_csv(lista_paises, NOMBRE_ARCHIVO_CSV)
        elif opcion_elegida == "3":
            buscar_paises_por_nombre(lista_paises)
        elif opcion_elegida == "4":
            menu_filtros(lista_paises)
        elif opcion_elegida == "5":
            ordenar_paises(lista_paises)
        elif opcion_elegida == "6":
            mostrar_estadisticas(lista_paises)
        elif opcion_elegida == "7":
            if not lista_paises:
                print("No hay países cargados.")
            else:
                mostrar_tabla_paises(lista_paises)
        elif opcion_elegida == "0":
            print("Salio del sistema")
            break


if __name__ == "_main_":
    main()