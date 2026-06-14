import csv
import os

NOMBRE_ARCHIVO_CSV = "paises.csv"

CABECERAS_CSV = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises_desde_csv(nombre_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios con los datos de cada país.
    Valida que el archivo tenga las cabeceras correctas y que los campos numéricos sean válidos.
    Retorna una lista vacía si el archivo no existe o está vacío.
    """
    lista_paises = []

    if not os.path.exists(nombre_archivo):
        print(f"Aviso: No se encontró '{nombre_archivo}'. Se iniciará con lista vacía.")
        return lista_paises
    try:
        with open(nombre_archivo, encoding="utf-8", newline="") as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            #Verificar que las cabeceras sean las correctas
            if lector.fieldnames is None or list(lector.fieldnames) != CABECERAS_CSV:
                print(f"Error: El archivo '{nombre_archivo}' no tiene las cabeceras correctas.")
                print(f"Se esperaban: {CABECERAS_CSV}")
                return lista_paises
            numero_fila = 1
            for fila in lector:
                numero_fila += 1
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    }
                    #Validar que ningún campo esté vacío
                    campos_completos = True

                    for valor in pais.values():
                        if str(valor) == "":
                            campos_completos = False

                    if not campos_completos:
                        print(f"Aviso: Fila {numero_fila} con campos vacíos ignorada.")
                        continue

                    lista_paises.append(pais)
                except (ValueError, KeyError) as error_fila:
                    print(f"Aviso: Fila {numero_fila} ignorada por error de formato: {error_fila}")
    except OSError as error_archivo:
        print(f"Error al leer el archivo '{nombre_archivo}': {error_archivo}")
    return lista_paises



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