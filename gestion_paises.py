import csv
import os

#Nombre del archivo CSV donde se persisten los datos
NOMBRE_ARCHIVO_CSV = "paises.csv"

#Cabeceras esperadas en el CSV
CABECERAS_CSV = ["nombre", "poblacion", "superficie", "continente"]



#Funciones de archivos CSV

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
    """
    Escribe la lista de países en el archivo CSV sobreescribiendo el contenido anterior.
    """
    try:
        with open(nombre_archivo, encoding="utf-8", newline="", mode="w") as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=CABECERAS_CSV)
            escritor.writeheader()
            escritor.writerows(lista_paises)
    except OSError as error_archivo:
        print(f"Error al guardar en '{nombre_archivo}': {error_archivo}")


#Funciones de validación de entrada


def leer_entero_positivo(mensaje_prompt):
    """
    Solicita un número entero positivo al usuario en bucle hasta obtener uno válido.
    """
    while True:
        valor_ingresado = input(mensaje_prompt).strip()
        if valor_ingresado.isdigit() and int(valor_ingresado) > 0:
            return int(valor_ingresado)
        print("Error: Ingrese un número entero mayor a 0.")

def leer_texto_no_vacio(mensaje_prompt):
    """
    Solicita texto al usuario en bucle hasta obtener una cadena no vacía.
    """
    while True:
        texto_ingresado = input(mensaje_prompt).strip()
        if texto_ingresado:
            return texto_ingresado
        print("Error: El campo no puede estar vacío.")

def leer_opcion_menu(opciones_validas, mensaje_prompt="Opción: "):
    """
    Solicita al usuario que elija una opción del menú entre las opciones válidas dadas.
    """
    while True:
        opcion_ingresada = input(mensaje_prompt).strip()
        if opcion_ingresada in opciones_validas:
            return opcion_ingresada
        print(f"Error: Opción no válida. Elija entre: {', '.join(opciones_validas)}")


#Funciones de gestión de países


def agregar_pais(lista_paises):
    """
    Solicita los datos de un nuevo país al usuario y lo agrega a la lista.
    No permite campos vacíos ni nombres duplicados (insensible a mayúsculas).
    """
    print("\n    Agregar país")
    nombre_nuevo = leer_texto_no_vacio("Nombre del país: ")
    #Verificar si el país ya existe
    if buscar_pais_exacto(lista_paises, nombre_nuevo) is not None:
        print(f"Error: Ya existe un país con el nombre '{nombre_nuevo}'.")
        return
    poblacion_nueva = leer_entero_positivo("Población: ")
    superficie_nueva = leer_entero_positivo("Superficie (km²): ")
    continente_nuevo = leer_texto_no_vacio("Continente: ")
    pais_nuevo = {
        "nombre": nombre_nuevo,
        "poblacion": poblacion_nueva,
        "superficie": superficie_nueva,
        "continente": continente_nuevo
    }
    lista_paises.append(pais_nuevo)
    print(f"País '{nombre_nuevo}' agregado correctamente.")

def actualizar_pais(lista_paises):
    """
    Busca un país por nombre exacto y permite actualizar su población y superficie.
    """
    print("\n    Actualizar país")
    nombre_buscado = leer_texto_no_vacio("Nombre del país a actualizar: ")
    indice_pais = buscar_pais_exacto(lista_paises, nombre_buscado)
    if indice_pais is None:
        print(f"Error: No se encontró ningún país con el nombre '{nombre_buscado}'.")
        return
    pais_encontrado = lista_paises[indice_pais]
    print(f"\nDatos actuales de '{pais_encontrado['nombre']}':")
    print(f"  Población : {pais_encontrado['poblacion']:,}")
    print(f"  Superficie: {pais_encontrado['superficie']:,} km²")
    poblacion_actualizada = leer_entero_positivo("Nueva población: ")
    superficie_actualizada = leer_entero_positivo("Nueva superficie (km²): ")
    lista_paises[indice_pais]["poblacion"] = poblacion_actualizada
    lista_paises[indice_pais]["superficie"] = superficie_actualizada
    print("Datos actualizados correctamente.")

def buscar_pais_exacto(lista_paises, nombre_buscado):
    """
    Busca un país por nombre exacto (insensible a mayúsculas/minúsculas).
    Retorna el índice en la lista o None si no se encuentra.
    """
    nombre_normalizado = nombre_buscado.strip().lower()
    for indice, pais in enumerate(lista_paises):
        if pais["nombre"].lower() == nombre_normalizado:
            return indice
    return None

def buscar_paises_por_nombre(lista_paises):
    """
    Busca países cuyo nombre contenga el texto ingresado (coincidencia parcial o exacta).
    Muestra todos los resultados encontrados.
    """
    print("\n    Buscar por nombre")
    texto_buscado = leer_texto_no_vacio("Texto a buscar en el nombre: ")
    texto_normalizado = texto_buscado.lower()
    resultados = []
    for pais in lista_paises:
        if texto_normalizado in pais["nombre"].lower():
            resultados.append(pais)
    if not resultados:
        print(f"No se encontraron países que contengan '{texto_buscado}'.")
        return
    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    mostrar_tabla_paises(resultados)


#Funciones de filtrado


def filtrar_por_continente(lista_paises):
    """
    Muestra los países que pertenecen al continente ingresado por el usuario.
    """
    print("\n    Filtrar por continente")
    continente_buscado = leer_texto_no_vacio("Continente: ")
    continente_normalizado = continente_buscado.lower()
    resultados = []
    for pais in lista_paises: 
        if pais["continente"].lower() == continente_normalizado:
            resultados.append(pais)
    if not resultados:
        print(f"No se encontraron países en el continente '{continente_buscado}'.")
        return
    print(f"\nPaíses en {continente_buscado} ({len(resultados)}):")
    mostrar_tabla_paises(resultados)

def filtrar_por_rango_poblacion(lista_paises):
    """
    Muestra los países cuya población está dentro del rango mínimo-máximo ingresado.
    """
    print("\n    Filtrar por rango de población")
    poblacion_minima = leer_entero_positivo("Población mínima: ")
    poblacion_maxima = leer_entero_positivo("Población máxima: ")
    if poblacion_minima > poblacion_maxima:
        print("Error: La población mínima no puede ser mayor que la máxima.")
        return
    resultados = []
    for pais in lista_paises:
        if poblacion_minima <= pais["poblacion"] <= poblacion_maxima:
            resultados.append(pais)
    if not resultados:
        print(f"No se encontraron países con población entre {poblacion_minima:,} y {poblacion_maxima:,}.")
        return
    print(f"\nPaíses con población entre {poblacion_minima:,} y {poblacion_maxima:,} ({len(resultados)}):")
    mostrar_tabla_paises(resultados)


def filtrar_por_rango_superficie(lista_paises):
    """
    Muestra los países cuya superficie (km²) está dentro del rango mínimo-máximo ingresado.
    """
    print("\n    Filtrar por rango de superficie")
    superficie_minima = leer_entero_positivo("Superficie mínima (km²): ")
    superficie_maxima = leer_entero_positivo("Superficie máxima (km²): ")
    if superficie_minima > superficie_maxima:
        print("Error: La superficie mínima no puede ser mayor que la máxima.")
        return
    resultados = []
    for pais in lista_paises:
        if superficie_minima <= pais["superficie"] <= superficie_maxima:
            resultados.append(pais)
    if not resultados:
        print(f"No se encontraron países con superficie entre {superficie_minima:,} y {superficie_maxima:,} km².")
        return
    print(f"\nPaíses con superficie entre {superficie_minima:,} y {superficie_maxima:,} km² ({len(resultados)}):")
    mostrar_tabla_paises(resultados)

def menu_filtros(lista_paises):
    """
    Submenú para las opciones de filtrado de países.
    """
    if not lista_paises:
        print("No hay países cargados.")
        return
    print("\n    Filtrar países")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion_filtro = leer_opcion_menu(["1", "2", "3"])
    if opcion_filtro == "1":
        filtrar_por_continente(lista_paises)
    elif opcion_filtro == "2":
        filtrar_por_rango_poblacion(lista_paises)
    elif opcion_filtro == "3":
        filtrar_por_rango_superficie(lista_paises)


#Funciones de ordenamiento


def ordenar_paises(lista_paises):
    """
    Muestra los países ordenados según el criterio y la dirección elegidos por el usuario.
    El ordenamiento no modifica la lista original; se trabaja sobre una copia.
    """
    if not lista_paises:
        print("No hay países cargados.")
        return
    print("\nOrdenar países")
    print("Ordenar por:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    criterio_opcion = leer_opcion_menu(["1", "2", "3"])
    print("\nDirección:")
    print("1. Ascendente")
    print("2. Descendente")
    direccion_opcion = leer_opcion_menu(["1", "2"])

    #Mapeo de opción a clave del diccionario
    mapa_criterio = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    clave_orden = mapa_criterio[criterio_opcion]
    orden_descendente = direccion_opcion == "2"
    lista_ordenada = lista_paises.copy()

    for i in range(len(lista_ordenada) - 1):
        for j in range(len(lista_ordenada) - 1 - i):

            valor_actual = lista_ordenada[j][clave_orden]
            valor_siguiente = lista_ordenada[j + 1][clave_orden]

            if orden_descendente:
                if valor_actual < valor_siguiente:
                    lista_ordenada[j], lista_ordenada[j + 1] = (
                        lista_ordenada[j + 1],
                        lista_ordenada[j]
                    )
            else:
                if valor_actual > valor_siguiente:
                    lista_ordenada[j], lista_ordenada[j + 1] = (
                        lista_ordenada[j + 1],
                        lista_ordenada[j]
                    )
    if orden_descendente:
        direccion_texto = "descendente"  
    else:
        direccion_texto = "ascendente" 
    print(f"\nPaíses ordenados por {clave_orden} ({direccion_texto}):")
    mostrar_tabla_paises(lista_ordenada)


#Funciones de estadísticas


def mostrar_estadisticas(lista_paises):
    """
    Calcula y muestra estadísticas clave: país con mayor/menor población,
    promedio de población, promedio de superficie y cantidad de países por continente.
    """
    if not lista_paises:
        print("No hay países cargados.")
        return
    total_paises = len(lista_paises)

    #País con mayor y menor población
    pais_mayor_poblacion = lista_paises[0]
    for pais in lista_paises:
        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais

    pais_menor_poblacion = lista_paises[0]
    for pais in lista_paises:
        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais

    #Promedio de población y superficie
    suma_poblacion = 0
    for pais in lista_paises:
        suma_poblacion += pais["poblacion"]

    suma_superficie = 0
    for pais in lista_paises:
        suma_superficie += pais["superficie"]

    promedio_poblacion = suma_poblacion // total_paises
    promedio_superficie = suma_superficie // total_paises
    
    #Cantidad de países por continente
    conteo_por_continente = {}
    for pais in lista_paises:
        nombre_continente = pais["continente"]
        if nombre_continente in conteo_por_continente:
            conteo_por_continente[nombre_continente] += 1
        else:
            conteo_por_continente[nombre_continente] = 1
    print("           ESTADÍSTICAS")
    print(f"Total de países cargados: {total_paises}")
    print(f"\nMayor población : {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']:,})")
    print(f"Menor población : {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']:,})")
    print(f"\nPromedio de población : {promedio_poblacion:,}")
    print(f"Promedio de superficie: {promedio_superficie:,} km²")
    print("\nCantidad de países por continente:")
    for nombre_continente, cantidad in conteo_por_continente.items():
        print(f"  {nombre_continente}: {cantidad}")


#Función de visualización


def mostrar_tabla_paises(lista_paises):
    """
    Muestra en consola una tabla con los datos de la lista de países recibida.
    """
    if not lista_paises:
        print("No hay países para mostrar.")
        return
    #Encabezado de tabla
    print(f"\n{'Nombre':<35} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<15}")
    print("-" * 85)
    for pais in lista_paises:
        print(f"{pais['nombre']:<35} {pais['poblacion']:>15,} {pais['superficie']:>18,} {pais['continente']:<15}")
    print("-" * 85)
    print(f"Total: {len(lista_paises)} país/es")


#Menú principal


def mostrar_menu_principal():
    """
    Imprime el menú principal con todas las opciones disponibles.
    """
    print("\n     GESTIÓN DE DATOS DE PAÍSES")
    print("1. Agregar país")
    print("2. Actualizar población y superficie")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Ver estadísticas")
    print("7. Mostrar todos los países")
    print("0. Salir")

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


#Punto de entrada del programa
if __name__ == "__main__":
    main()