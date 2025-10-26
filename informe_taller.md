# Informe del Taller – Búsqueda Lineal (TechStore)

## 1. Introducción

El presente informe tiene como finalidad documentar el desarrollo del taller práctico de **búsqueda lineal**, aplicado al contexto de una tienda de electrónica denominada **TechStore**.
El trabajo se realizó en el marco de la asignatura **Algoritmos y Estructuras de Datos**, con el objetivo de comprender, implementar y analizar el comportamiento del algoritmo de búsqueda lineal en diferentes tipos de datos y escenarios prácticos.

## 2. Objetivos

1. Comprender el funcionamiento del algoritmo de búsqueda lineal y su aplicación en Python.
2. Implementar búsquedas sobre listas numéricas y listas de diccionarios.
3. Aplicar la búsqueda lineal en la gestión de productos y empleados de una tienda.
4. Evaluar la complejidad temporal y espacial del algoritmo.
5. Incorporar mejoras mediante búsqueda avanzada y persistencia de datos.

## 3. Marco teórico

La **búsqueda lineal** o **búsqueda secuencial** es un método elemental para localizar un elemento dentro de una estructura de datos. Consiste en recorrer la lista desde el primer hasta el último elemento, comparando en cada iteración el valor buscado con el elemento actual.
Este algoritmo es útil cuando los datos no están ordenados o el tamaño de la lista es pequeño.

- **Complejidad temporal:** O(n), donde *n* es el número de elementos en la lista.
- **Complejidad espacial:** O(1), ya que no requiere estructuras auxiliares adicionales.
- **Ventajas:** simplicidad, fácil implementación, aplicable a cualquier tipo de datos.
- **Desventajas:** bajo rendimiento en listas grandes, ineficiente para búsquedas repetidas.

## 4. Implementación general

El proyecto se desarrolló en lenguaje Python y se organizó en módulos independientes para garantizar claridad y mantenibilidad del código.
Cada módulo cumple una función específica dentro del sistema.

### 4.1 funciones_busqueda.py

Contiene las implementaciones de búsqueda lineal sobre diferentes tipos de datos:

* `busqueda_lineal_simple`: busca un elemento en una lista numérica.
* `buscar_producto_por_nombre`, `buscar_producto_por_id`, `buscar_productos_por_categoria`: búsqueda sobre listas de productos.
* `buscar_empleado_por_nombre_completo`, `buscar_empleados_por_departamento`, `buscar_empleados_activos`: búsqueda sobre listas de empleados.
* `buscar_disponibles`, `buscar_por_rango_precio`, `buscar_por_marca`, `contar_por_categoria`: búsquedas condicionales en inventario.
* `complejidad_busquedas`: análisis descriptivo de la complejidad del algoritmo.

Cada función fue diseñada con bucles iterativos simples, retornando resultados en forma de índices, objetos o listas filtradas.

### 4.2 sistema_tienda.py

Constituye el núcleo del programa. Implementa un **menú de consola (CLI)** que integra todas las funciones de búsqueda.
Incluye validaciones de entrada, submenús para productos y empleados, manejo de errores y salidas formateadas.
Su diseño modular permite ejecutar de forma independiente cada ejercicio y visualizar resultados de forma clara.

### 4.3 datos_ejemplo.py

Contiene las estructuras de datos utilizadas para pruebas:

* Lista de productos con campos: id, nombre, marca, categoría, precio, stock y disponibilidad.
* Lista de empleados con campos: id, nombre, apellido, departamento, salario y estado activo.

### 4.4 busqueda_avanzada.py

Desarrollo del **Desafío 1**.
Implementa búsqueda por múltiples criterios simultáneamente (AND / OR) y búsqueda aproximada mediante el cálculo de similitud con la librería *difflib*.
Permite tolerancia a errores tipográficos y mayor flexibilidad en la búsqueda textual.

### 4.5 persistencia.py

Desarrollo del **Desafío 3**.
Permite almacenar y recuperar datos en formato JSON, manteniendo un historial de búsquedas y generando estadísticas básicas sobre el uso del sistema (número de consultas, promedio de resultados, consultas por tipo, etc.).

## 5. Casos especiales considerados

Durante el desarrollo se consideraron los siguientes casos límite:

* Listas vacías o sin elementos válidos.
* Coincidencias parciales y búsqueda insensible a mayúsculas y minúsculas.
* Búsquedas que retornan múltiples coincidencias.
* Validación de datos numéricos (ID, precios, stock).
* Entradas de usuario inválidas o fuera de rango.
* Tolerancia a errores de escritura en modo aproximado.

## 6. Análisis de complejidad

Cada función de búsqueda lineal implementada recorre la lista de principio a fin hasta encontrar la coincidencia o finalizar el recorrido.

* **Peor caso:** el elemento no se encuentra y se recorren todos los elementos (O(n)).
* **Mejor caso:** el elemento se encuentra en la primera posición (O(1)).
* **Espacio adicional:** constante (O(1)).
* **Multi-criterio:** O(n · c), donde *c* representa el número de criterios aplicados.

El análisis experimental mostró que el rendimiento es aceptable para volúmenes pequeños de datos y se degrada linealmente conforme crece el tamaño de la lista, tal como predice la teoría.

## 7. Ejemplos de uso

**Ejemplo 1. Búsqueda numérica**
Entrada: `[64, 34, 25, 12, 22, 11, 90]`, búsqueda del número `25`.
Resultado: índice `2`.

**Ejemplo 2. Búsqueda de productos por nombre**
Entrada: `"iPhone"`.
Resultado: `iPhone 15` (marca Apple).

**Ejemplo 3. Búsqueda de empleados activos**
Entrada: estado `activo`.
Resultado: lista con los empleados activos.

**Ejemplo 4. Búsqueda por rango de precios**
Entrada: precios entre `500` y `1000`.
Resultado: productos dentro de ese rango, ordenados según aparición.

**Ejemplo 5. Conteo por categoría**
Entrada: categoría `"Smartphone"`.
Resultado: cantidad de productos en esa categoría.

**Ejemplo 6. Búsqueda multi-criterio (Desafío 1)**
Entrada: marca `"Apple"` y categoría `"Laptop"`.
Resultado: productos Apple en la categoría Laptop.

**Ejemplo 7. Persistencia de datos (Desafío 3)**
Cada búsqueda realizada genera un registro en `historial_busquedas.json` con los criterios aplicados, el tipo de búsqueda y la cantidad de resultados.

## 8. Actividades adicionales

* Implementación de contador de comparaciones en la función de búsqueda básica.
* Análisis cualitativo de eficiencia y posibles optimizaciones.
* Documentación completa de código con comentarios explicativos.
* Validación de entradas y manejo de errores comunes.

## 9. Conclusiones

El algoritmo de búsqueda lineal se caracteriza por su simplicidad y aplicabilidad general.
En el contexto del sistema *TechStore*, demostró ser suficiente para operaciones de búsqueda sobre conjuntos pequeños y medianos de datos.
El desarrollo del taller permitió comprender el comportamiento del algoritmo en términos de complejidad temporal, así como su extensión a escenarios reales mediante listas de diccionarios y filtrado condicional.

Las mejoras implementadas —como la búsqueda aproximada y la persistencia de datos— extendieron las capacidades del sistema sin alterar su naturaleza lineal.
El trabajo final cumple con los objetivos de análisis, implementación modular y documentación técnica solicitados.