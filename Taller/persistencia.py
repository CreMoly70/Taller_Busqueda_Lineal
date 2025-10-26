
# persistencia.py
# ---------------------------------------------------------
#persistencia en JSON de datos, historial de busquedas y estadisticas simples.
# ---------------------------------------------------------

import json
from typing import Any, Dict, List
from datetime import datetime
from collections import Counter, defaultdict
from pathlib import Path


def guardar_json(ruta: str, objeto: Any) -> None:
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(objeto, f, ensure_ascii=False, indent=2)


def cargar_json(ruta: str, por_defecto: Any = None) -> Any:
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return por_defecto


def registrar_busqueda(ruta_historial: str, tipo: str, criterios: Dict[str, Any], resultados: int) -> None:
    hist = cargar_json(ruta_historial, por_defecto=[])
    evento = {
        "fecha": datetime.now().isoformat(timespec='seconds'),
        "tipo": tipo,                   #'producto' / 'empleado' / 'multi' / etc.
        "criterios": criterios,
        "resultados": resultados
    }
    hist.append(evento)
    guardar_json(ruta_historial, hist)


def estadisticas_desde_historial(ruta_historial: str) -> Dict[str, Any]:
    hist = cargar_json(ruta_historial, por_defecto=[])
    por_tipo = Counter(h['tipo'] for h in hist) if hist else Counter()
    total_consultas = len(hist)
    promedio_resultados = sum(h['resultados'] for h in hist) / total_consultas if total_consultas else 0.0
    return {
        "total_consultas": total_consultas,
        "consultas_por_tipo": dict(por_tipo),
        "promedio_resultados": round(promedio_resultados, 2),
        "ultimas_5": hist[-5:] if total_consultas >= 1 else []
    }
