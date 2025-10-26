# Proyecto: Sistema de Búsqueda Lineal – TechStore

## Descripción general

Este proyecto implementa un sistema de consola para la gestión y consulta de información en una tienda de electrónica denominada **TechStore**.
El propósito principal es aplicar y analizar el algoritmo de **búsqueda lineal (O(n))** en diferentes contextos, utilizando estructuras de datos en Python.
El sistema permite realizar búsquedas sobre listas de productos y empleados, aplicar filtros, y realizar un análisis básico de complejidad y rendimiento.

## Objetivos del proyecto

1. Comprender el funcionamiento y la estructura del algoritmo de búsqueda lineal.
2. Implementar funciones de búsqueda aplicadas a listas de datos heterogéneos (diccionarios).
3. Analizar la complejidad temporal y espacial del algoritmo en distintos casos.
4. Aplicar la búsqueda lineal en un contexto práctico y realista (sistema de tienda).
5. Integrar desafíos adicionales como búsqueda avanzada y persistencia de datos.

## Estructura del proyecto

````
Taller_Busqueda_Lineal/
│
├── sistema_tienda.py           # Menú principal de consola (CLI)
├── funciones_busqueda.py       # Implementación de funciones de búsqueda lineal
├── datos_ejemplo.py            # Conjunto de datos de productos y empleados
├── busqueda_avanzada.py        # Búsqueda por múltiples criterios y modo aproximado
├── persistencia.py             # Historial de búsquedas y estadísticas en JSON
├── README.md                   # Documento de presentación y guía del proyecto
└── informe_taller.md           # Informe técnico y académico del taller
````

## Requisitos técnicos

* Python 3.10 o superior
* No requiere dependencias externas
* Se recomienda ejecutar el proyecto en Visual Studio Code o cualquier entorno con soporte para Python

## Ejecución

1. Abrir una terminal en la carpeta del proyecto.

2. Ejecutar el siguiente comando:

   ```
   python sistema_tienda.py
   ```
   o
   ```
   py sistema_tienda.py
   ```

4. Se mostrará un menú interactivo con las siguientes opciones:

   ```
   1) Búsqueda lineal simple
   2) Búsqueda en lista de productos
   3) Búsqueda en lista de empleados
   4) Búsqueda por disponibilidad, precio, marca y categoría
   5) Actividades adicionales (complejidad y casos especiales)
   0) Salir
   ```

5. Seguir las instrucciones de cada opción para ejecutar las pruebas de búsqueda y análisis.

## Funcionalidades principales

* Búsqueda de productos por nombre, marca, categoría, ID o rango de precios.
* Búsqueda de empleados por nombre, apellido, departamento o estado (activo/inactivo).
* Filtrado por disponibilidad (stock).
* Conteo de productos por categoría.
* Análisis de complejidad O(n) con contador de comparaciones.
* Registro de búsquedas y estadísticas mediante persistencia en archivos JSON.
* Búsquedas por múltiples criterios y coincidencias aproximadas (modo avanzado).

## Cobertura de ejercicios

**Ejercicio 1:**
Implementación de búsqueda lineal básica sobre una lista de números.
Archivo principal: `funciones_busqueda.py`.

**Ejercicio 2:**
Búsqueda de productos en listas de diccionarios.
Archivo principal: `funciones_busqueda.py`.

**Ejercicio 3:**
Búsqueda de empleados en listas de diccionarios.
Archivo principal: `funciones_busqueda.py`.

**Ejercicio 4:**
Búsqueda condicional de productos por disponibilidad, marca, rango de precios y categoría.
Archivo principal: `funciones_busqueda.py`.

**Ejercicio 5:**
Sistema integrado con menú de navegación y validaciones de entrada.
Archivo principal: `sistema_tienda.py`.

**Actividades adicionales:**
Análisis de complejidad, manejo de casos especiales, y optimizaciones del algoritmo.
Archivo principal: `funciones_busqueda.py`.

**Desafíos adicionales:**
Implementación de búsqueda multi-criterio, coincidencia aproximada y persistencia de datos.
Archivos: `busqueda_avanzada.py` y `persistencia.py`.

## Criterios de evaluación

**1. Funcionalidad (40%)**

* Implementación completa de búsqueda lineal simple y sobre estructuras de diccionarios.
* Correcto manejo de casos límite y entradas inválidas.
* Sistema de menú funcional y navegable.

**2. Calidad del código (30%)**

* Código modular, documentado y con nombres descriptivos.
* Cumplimiento de estándares de legibilidad y organización.
* Validación de entradas y manejo de excepciones básicas.

**3. Comprensión (20%)**

* Análisis de complejidad temporal en `complejidad_busquedas()`.
* Explicaciones teóricas en el informe del taller.
* Correcta diferenciación entre búsqueda exacta, parcial y aproximada.

**4. Creatividad (10%)**

* Inclusión de desafíos opcionales (búsqueda avanzada y persistencia).
* Extensión de funcionalidades más allá de los requerimientos mínimos.

## Checklist de entrega

* [x] `sistema_tienda.py` (funcionalidad principal del sistema)
* [x] `funciones_busqueda.py` (funciones O(n) documentadas)
* [x] `datos_ejemplo.py` (dataset de prueba)
* [x] `busqueda_avanzada.py` (búsqueda multi-criterio y aproximada)
* [x] `persistencia.py` (historial de búsquedas y estadísticas)
* [x] `README.md` (documento de referencia y guía)
* [x] `informe_taller.md` (informe académico del proyecto)

## Autor

Sebastian García Cruz
Taller2 – Analisis y Diseño de Algoritmos
Universidad del Valle
