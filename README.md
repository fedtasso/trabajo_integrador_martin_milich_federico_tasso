## Gestión de Datos de Países en Python

Trabajo Práctico Integrador – Programación 1
Tecnicatura Universitaria en Programación – UTN (Modalidad a Distancia)

## Integrantes

Milich Martín
Tasso Federico


## Descripción

Aplicación de consola desarrollada en Python 3 que permite gestionar un dataset de países almacenado en un archivo CSV. El sistema ofrece un menú interactivo con las siguientes funcionalidades:

Agregar un nuevo país
Actualizar población y superficie de un país existente
Buscar países por nombre (coincidencia parcial o exacta)
Filtrar países por continente, rango de población o rango de superficie
Ordenar países por nombre, población o superficie (ascendente o descendente)
Ver estadísticas: mayor y menor población, promedios y cantidad por continente


## Estructura del repositorio

```text
gestion-paises-tpi/
│
├── gestion_paises.py   # Código fuente principal
├── paises.csv          # Dataset base con 51 países
└── README.md           # Este archivo
```


## Requisitos

Python 3.x instalado
No requiere librerías externas (solo módulos estándar: csv y os)


## Instrucciones de uso

1. Clonar el repositorio
git clone https://github.com/fedtasso/trabajo_integrador_martin_milich_federico_tasso.git
2. Ejecutar el programa**
python gestion_paises.py

El archivo paises.csv debe estar en la misma carpeta que gestion_paises.py.


## Ejemplos de uso

- **Agregar un país (opción 1):** se ingresan nombre, población, superficie y continente. No se permiten campos vacíos ni nombres duplicados.
- **Actualizar país (opción 2):** se busca un país por nombre exacto y se modifican su población y superficie. Si el país no existe, el programa avisa.
- **Buscar por nombre (opción 3):** admite coincidencia parcial. Por ejemplo, buscar `re` devuelve Brasil, Corea del Sur y República Democrática del Congo.
- **Filtrar (opción 4):** por continente, o por rango de población/superficie. Si el valor mínimo es mayor que el máximo, el programa avisa y no aplica el filtro.
- **Ordenar (opción 5):** por nombre, población o superficie, en orden ascendente o descendente.
- **Estadísticas (opción 6):** muestra el país con mayor y menor población, los promedios de población y superficie, y la cantidad de países por continente.
- **Mostrar todos los países (opción 7):** lista completa de la base de datos cargada, incluyendo los países agregados durante la sesión.
- **Salir (opción 0):** finaliza el programa.

Ante cualquier dato inválido (texto vacío, número negativo, opción inexistente) el programa muestra un mensaje de error y vuelve a pedir el dato sin interrumpirse.


## Video demostrativo

TODO LINK VIDEO


## Documentación en PDF

TODO LINK PDF o UBICACIÓN EN EL REPOSITORIO


## Conceptos aplicados

- **Listas:** almacenamiento del dataset de países
- **Diccionarios:** representación de cada país con sus atributos
- **Funciones:** modularización con una responsabilidad por función
- **Condicionales:** validaciones de entrada y control de flujo
- **Ordenamientos:** algoritmo de burbuja (bubble sort) sobre una copia de la lista
- **Estadísticas:** acumuladores y comparaciones con bucles for
- **Archivos CSV:** lectura y escritura con el módulo csv
