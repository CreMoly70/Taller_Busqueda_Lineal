
# busqueda_avanzada.py
# -----------------------------------------------------------------------------------------------
#busquedas avanzadas: múltiples criterios (AND/OR),
#operadores lógicos y búsqueda aproximada (tolerancia a error).
#todas las búsquedas siguen siendo O(n) sobre la longitud del conjunto de datos. No se usan índices.
# ----------------------------------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, Tuple
from difflib import SequenceMatcher

Producto = Dict[str, Any]


def _norm(x: Any) -> str:
    return str(x).strip().lower()


def _similaridad(a: str, b: str) -> float:
    """Similaridad en [0,1] usando difflib (no requiere dependencias externas)."""
    return SequenceMatcher(None, _norm(a), _norm(b)).ratio()


def coincide_aproximado(valor: Any, query: str, umbral: float = 0.75) -> bool:
    """True si la similitud >= umbral. Útil para tolerar typos/errores leves."""
    return _similaridad(str(valor), query) >= umbral


def coincide_parcial(valor: Any, query: str) -> bool:
    v = _norm(valor)
    q = _norm(query)
    return q in v


def coincide_exacto(valor: Any, query: str) -> bool:
    return _norm(valor) == _norm(query)


def match_producto(producto: Producto, campo: str, query: Any, modo: str = "parcial",
                   umbral: float = 0.75) -> bool:
    """evaluaa si un producto coincide en un campo dado segun el modo:
    - 'parcial': subcadena case-insensitive
    - 'exacto': igualdad case-insensitive
    - 'aprox': similitud >= umbral
    Si el campo no existe, retorna False.
    """
    if campo not in producto:
        return False
    val = producto[campo]
    if modo == "exacto":
        return coincide_exacto(val, query)
    elif modo == "aprox":
        return coincide_aproximado(val, str(query), umbral)
    else:
        return coincide_parcial(val, str(query))


def buscar_productos_multi(productos: List[Producto],
                           criterios: List[Tuple[str, Any, str]],
                           logica: str = "AND",
                           umbral_aprox: float = 0.75) -> List[Producto]:
    """
    busqueda por multiples criterios.
    -criterios: lista de tuplas (campo, valor, modo) donde modo ∈ {'parcial','exacto','aprox'}
    -logica: 'AND' o 'OR'
    -umbral_aprox: umbral para coincidencia aproximada
    retorna lista de productos que satisfacen la logica con todos los criterios.
    complejidad: O(n * c), con c = nmro de criterios.
    """
    logica = (logica or "AND").upper()
    res = []
    for p in productos:
        checks = []
        for campo, valor, modo in criterios:
            checks.append(match_producto(p, campo, valor, modo if modo else "parcial", umbral_aprox))
        ok = all(checks) if logica == "AND" else any(checks)
        if ok:
            res.append(p)
    return res
