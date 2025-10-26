
# funciones_busqueda.py
# -----------------------------------------------------
# funciones de busqueda lineal para el sistema TechStore.
# todas las búsquedas son O(n) en tiempo y O(1) en espacio
# adicional (ignorando el espacio de resultados).
# ---------------------------------------------------------

from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

Producto = Dict[str, Any]
Empleado = Dict[str, Any]


#-----------------#
# utilidades base #
#-----------------#

def _norm(x: Any) -> str:
    """Normaliza un valor a string en minúsculas sin espacios extremos."""
    return str(x).strip().lower()


def _coincide_texto(obj_val: Any, query: str, exacto: bool = False) -> bool:
    """
    Compara obj_val contra query con normalización.
    - exacto=False: coincide si query es subcadena (búsqueda parcial, case-insensitive)
    - exacto=True: coincide si son iguales (case-insensitive)
    """
    a = _norm(obj_val)
    b = _norm(query)
    return (a == b) if exacto else (b in a)


# ==================================
# ejercicio 1: busqueda basica O(n)
# ================================

def busqueda_lineal_simple(lista: Iterable[Any], elemento: Any) -> int:
    """
    Busca un elemento en una lista usando búsqueda lineal.
    Retorna el índice si lo encuentra, -1 si no.
    Complejidad: O(n) tiempo, O(1) espacio.
    """
    for i, val in enumerate(lista):
        if val == elemento:
            return i
    return -1


def busqueda_lineal_simple_con_contador(lista: Iterable[Any], elemento: Any) -> Tuple[int, int]:
    """
    Variante que además retorna el conteo de comparaciones realizadas.
    Retorna (indice| -1, comparaciones)
    """
    comparaciones = 0
    for i, val in enumerate(lista):
        comparaciones += 1
        if val == elemento:
            return i, comparaciones
    return -1, comparaciones


# ======================================
# ejercicio 2: busqueda en lista productos
# ========================================

def buscar_producto_por_nombre(productos: List[Producto], nombre: str, exacto: bool = False) -> List[Producto]:
    """retorna una lista de productos cuyo nombre coincide (parcial por defecto)."""
    resultados = []
    for p in productos:
        if _coincide_texto(p.get('nombre', ''), nombre, exacto=exacto):
            resultados.append(p)
    return resultados


def buscar_producto_por_id(productos: List[Producto], id_producto: int) -> Optional[Producto]:
    """retorna el producto con ID exacto o None si no existe."""
    for p in productos:
        if p.get('id') == id_producto:
            return p
    return None


def buscar_productos_por_categoria(productos: List[Producto], categoria: str) -> List[Producto]:
    """reetorna productos que pertenecen a la categoría (parcial y case-insensitive)."""
    resultados = []
    for p in productos:
        if _coincide_texto(p.get('categoria', ''), categoria, exacto=False):
            resultados.append(p)
    return resultados


# =================================
# ejercicio 3: busqueda de empleados
# =================================

def buscar_empleado_por_nombre_completo(empleados: List[Empleado], nombre: str, apellido: str, exacto: bool = False) -> List[Empleado]:
    """retorna empleados cuyo nombre y apellido coinciden (parcial por defecto)."""
    resultados = []
    for e in empleados:
        ok_nombre = _coincide_texto(e.get('nombre', ''), nombre, exacto=exacto)
        ok_apellido = _coincide_texto(e.get('apellido', ''), apellido, exacto=exacto)
        if ok_nombre and ok_apellido:
            resultados.append(e)
    return resultados


def buscar_empleados_por_departamento(empleados: List[Empleado], departamento: str) -> List[Empleado]:
    """retorna empleados de un departamento (parcial y case-insensitive)."""
    resultados = []
    for e in empleados:
        if _coincide_texto(e.get('departamento', ''), departamento, exacto=False):
            resultados.append(e)
    return resultados


def buscar_empleados_activos(empleados: List[Empleado], activo: bool = True) -> List[Empleado]:
    """retorna empleados activos (activo=True) o inactivos (activo=False)."""
    resultados = []
    for e in empleados:
        if bool(e.get('activo', False)) is activo:
            resultados.append(e)
    return resultados


# ======================================
# ejercicio 4:busquedas por disponibilidad
# ======================================

def buscar_disponibles(productos: List[Producto]) -> List[Producto]:
    """productos con stock > 0 (disponibles)."""
    resultados = []
    for p in productos:
        if int(p.get('stock', 0)) > 0:
            resultados.append(p)
    return resultados


def buscar_por_rango_precio(productos: List[Producto], minimo: Optional[float] = None, maximo: Optional[float] = None) -> List[Producto]:
    """retorna productos con precio dentro de [minimo, maximo]. Soportando limites abiertos."""
    resultados = []
    for p in productos:
        precio = float(p.get('precio', 0.0))
        if (minimo is None or precio >= minimo) and (maximo is None or precio <= maximo):
            resultados.append(p)
    return resultados


def buscar_por_marca(productos: List[Producto], marca: str) -> List[Producto]:
    """retorna productos que coincidan con la marca (parcial, case-insensitive)."""
    resultados = []
    for p in productos:
        if _coincide_texto(p.get('marca', ''), marca, exacto=False):
            resultados.append(p)
    return resultados


def contar_por_categoria(productos: List[Producto], categoria: str) -> int:
    """cuenta productos que pertenecen a la categoria dada."""
    conteo = 0
    for p in productos:
        if _coincide_texto(p.get('categoria', ''), categoria, exacto=False):
            conteo += 1
    return conteo


# =====================================
# actividades adicionales: analisis O(n)
# =====================================

def complejidad_busquedas() -> str:
    """devuelve un resumen corto de complejidad temporal y espacial (O-notation)."""
    return (
        "- todas las funciones basadas en busqueda lineal recorren la lista una sola vez: O(n) tiempo\n"
        "- no usan estructuras auxiliares significativas: O(1) espacio adicional\n"
        "- la eficiencia mejora cuando se detiene al encontrar el primer match (cuando aplica)\n"
        "- si se requieren muchas busquedas sobre datos estaticos y grandes, conviene indexar o usar estructuras ordenadas"
    )


# =========================================
# ayudas opcionales: formatos y presentacion
# =========================================

def formatear_productos(productos: List[Producto]) -> str:
    """devuelve un string tabular simple para imprimir productos."""
    if not productos:
        return "(sin resultados)"
    lineas = []
    for p in productos:
        lineas.append(f"[#{p.get('id')}] {p.get('nombre')} | {p.get('marca')} | {p.get('categoria')} | $ {p.get('precio')} | stock: {p.get('stock')}")
    return "\n".join(lineas)


def formatear_empleados(empleados: List[Empleado]) -> str:
    """devuelve un string tabular simple para imprimir empleados."""
    if not empleados:
        return "(sin resultados)"
    lineas = []
    for e in empleados:
        estado = "Activo" if e.get('activo') else "Inactivo"
        lineas.append(f"[#{e.get('id')}] {e.get('nombre')} {e.get('apellido')} | {e.get('departamento')} | ${e.get('salario')} | {estado}")
    return "\n".join(lineas)


# ===============================
# validaciones y manejo de errores
# ===============================

def validar_lista_no_vacia(lista: Iterable[Any]) -> bool:
    """retorna True si la lista no está vacía (para casos límite)."""
    try:
        #evita consumir iteradores; si es lista/tupla funciona directo
        return len(lista) > 0  # type: ignore[arg-type]
    except TypeError:
        #si es un iterador, peinarlo a lista (caso raro en este taller)
        return any(True for _ in lista)


