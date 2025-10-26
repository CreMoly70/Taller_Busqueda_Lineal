
# sistema_tienda.py
#Menu interactivo que integra las funciones de busqueda lineal (O(n)).

from typing import Optional
from funciones_busqueda import (
    busqueda_lineal_simple, busqueda_lineal_simple_con_contador,
    buscar_producto_por_nombre, buscar_producto_por_id, buscar_productos_por_categoria,
    buscar_disponibles, buscar_por_rango_precio, buscar_por_marca, contar_por_categoria,
    buscar_empleado_por_nombre_completo, buscar_empleados_por_departamento, buscar_empleados_activos,
    formatear_productos, formatear_empleados, complejidad_busquedas
)
from datos_ejemplo import productos, empleados


def input_entero(mensaje: str) -> Optional[int]:
    try:
        return int(input(mensaje))
    except ValueError:
        print("⚠️  Debes ingresar un número entero.")
        return None


def input_flotante(mensaje: str) -> Optional[float]:
    try:
        return float(input(mensaje))
    except ValueError:
        print("!!! Debes ingresar un numero (puede tener decimales).")
        return None


def menu_principal():
    print("\n===== TechStore: Sistema de Busqueda Lineal =====")
    print("1) Ejercicio 1: Busqueda lineal simple")
    print("2) Ejercicio 2: Busqueda en productos")
    print("3) Ejercicio 3: Busqueda en empleados")
    print("4) Ejercicio 4: Busquedas por disponibilidad/precio/marca/categoria")
    print("5) Actividades adicionales (complejidad, casos)")
    print("0) Salir")


def sub_menu_productos():
    print("\n-- Productos --")
    print("1) Buscar por nombre (parcial)")
    print("2) Buscar por ID (exacto)")
    print("3) Buscar por categoría (parcial)")
    print("0) Volver")


def sub_menu_empleados():
    print("\n-- Empleados --")
    print("1) Buscar por nombre y apellido (parcial)")
    print("2) Buscar por departamento (parcial)")
    print("3) Listar activos / inactivos")
    print("0) Volver")


def sub_menu_disp():
    print("\n-- Disponibilidad / Precio / Marca / Categoría --")
    print("1) Listar productos disponibles (stock > 0)")
    print("2) Buscar por rango de precio")
    print("3) Buscar por marca (parcial)")
    print("4) Contar por categoría")
    print("0) Volver")


def ejecutar():
    while True:
        menu_principal()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\nEjercicio 1: Búsqueda lineal simple")
            lista_demo = [64, 34, 25, 12, 22, 11, 90]
            print("Lista de ejemplo:", lista_demo)
            valor = input_entero("Valor a buscar: ")
            if valor is not None:
                idx = busqueda_lineal_simple(lista_demo, valor)
                idx2, comps = busqueda_lineal_simple_con_contador(lista_demo, valor)
                if idx != -1:
                    print(f":) Encontrado en índice {idx} (comparaciones: {comps})")
                else:
                    print(f":( No encontrado (comparaciones: {comps})")

        elif opcion == "2":
            while True:
                sub_menu_productos()
                sub = input("Opcion: ").strip()
                if sub == "1":
                    nombre = input("Nombre (o parte): ")
                    res = buscar_producto_por_nombre(productos, nombre, exacto=False)
                    print(formatear_productos(res))
                elif sub == "2":
                    pid = input_entero("ID exacto: ")
                    if pid is not None:
                        p = buscar_producto_por_id(productos, pid)
                        print(formatear_productos([p]) if p else "(no existe)")
                elif sub == "3":
                    categoria = input("Categoria (o parte): ")
                    res = buscar_productos_por_categoria(productos, categoria)
                    print(formatear_productos(res))
                elif sub == "0":
                    break
                else:
                    print("!!! Opcion no valida.")

        elif opcion == "3":
            while True:
                sub_menu_empleados()
                sub = input("Opcion: ").strip()
                if sub == "1":
                    nombre = input("Nombre (o parte): ")
                    apellido = input("Apellido (o parte): ")
                    res = buscar_empleado_por_nombre_completo(empleados, nombre, apellido, exacto=False)
                    print(formatear_empleados(res))
                elif sub == "2":
                    dep = input("Departamento (o parte): ")
                    res = buscar_empleados_por_departamento(empleados, dep)
                    print(formatear_empleados(res))
                elif sub == "3":
                    estado = input("¿Listar 'activos' o 'inactivos'? ").strip().lower()
                    activos = True if estado.startswith('a') else False
                    res = buscar_empleados_activos(empleados, activo=activos)
                    print(formatear_empleados(res))
                elif sub == "0":
                    break
                else:
                    print("!!! Opcion no valida.")

        elif opcion == "4":
            while True:
                sub_menu_disp()
                sub = input("Opcion: ").strip()
                if sub == "1":
                    res = buscar_disponibles(productos)
                    print(formatear_productos(res))
                elif sub == "2":
                    mn = input_flotante("Minimo (ENTER para ninguno): ")  # None si falla
                    mx = input_flotante("Maximo (ENTER para ninguno): ")
                    res = buscar_por_rango_precio(productos, mn, mx)
                    print(formatear_productos(res))
                elif sub == "3":
                    marca = input("Marca (o parte): ")
                    res = buscar_por_marca(productos, marca)
                    print(formatear_productos(res))
                elif sub == "4":
                    cat = input("Categoria (o parte): ")
                    c = contar_por_categoria(productos, cat)
                    print(f"Hay {c} producto(s) en esa categoria.")
                elif sub == "0":
                    break
                else:
                    print("!!! Opcion no valida.")

        elif opcion == "5":
            print("\nActividades adicionales:")
            print(complejidad_busquedas())
            print("\nCasos especiales considerados:")
            print("- Listas vacías -> retornos vacíos o -1")
            print("- Busquedas de texto son case-insensitive y aceptan coincidencias parciales")
            print("- Se incluye variante con contador de comparaciones en el ejercicio 1")

        elif opcion == "0":
            print("Hasta luego :)")
            break
        else:
            print("!!! Opcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    ejecutar()
