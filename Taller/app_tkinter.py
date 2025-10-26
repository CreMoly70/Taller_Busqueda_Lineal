
# app_tkinter.py
# ---------------------------------------------------------
# interfaz grafica simple con tkinter.
# -búsqueda en tiempo real por nombre
# -filtros por marca y categoria (parciales)
# -tabla simple con resultados
# -------------------------------------------------

import tkinter as tk
from tkinter import ttk
from typing import List, Dict, Any
from datos_ejemplo import productos
from funciones_busqueda import buscar_producto_por_nombre, buscar_por_marca, buscar_productos_por_categoria


def filtrar(nombre: str, marca: str, categoria: str) -> List[Dict[str, Any]]:
    res = productos
    if nombre.strip():
        res = buscar_producto_por_nombre(res, nombre, exacto=False)
    if marca.strip():
        res = [p for p in res if marca.lower() in str(p.get('marca','')).lower()]
    if categoria.strip():
        res = [p for p in res if categoria.lower() in str(p.get('categoria','')).lower()]
    return res


def actualizar():
    nombre = entry_nombre.get()
    marca = entry_marca.get()
    categoria = entry_categoria.get()
    rows = filtrar(nombre, marca, categoria)
    for i in tree.get_children():
        tree.delete(i)
    for p in rows:
        tree.insert('', 'end', values=(p['id'], p['nombre'], p['marca'], p['categoria'], p['precio'], p['stock']))


root = tk.Tk()
root.title("TechStore - Búsqueda (tkinter)")
root.geometry("800x480")

frm = ttk.Frame(root, padding=10)
frm.pack(fill='both', expand=True)

ttk.Label(frm, text="Nombre:").grid(row=0, column=0, sticky='w')
entry_nombre = ttk.Entry(frm, width=30)
entry_nombre.grid(row=0, column=1, sticky='w', padx=5)

ttk.Label(frm, text="Marca:").grid(row=0, column=2, sticky='w')
entry_marca = ttk.Entry(frm, width=20)
entry_marca.grid(row=0, column=3, sticky='w', padx=5)

ttk.Label(frm, text="Categoría:").grid(row=0, column=4, sticky='w')
entry_categoria = ttk.Entry(frm, width=20)
entry_categoria.grid(row=0, column=5, sticky='w', padx=5)

btn = ttk.Button(frm, text="Buscar", command=actualizar)
btn.grid(row=0, column=6, padx=10)

cols = ('ID','Nombre','Marca','Categoría','Precio','Stock')
tree = ttk.Treeview(frm, columns=cols, show='headings', height=16)
for c in cols:
    tree.heading(c, text=c)
    tree.column(c, width=100 if c=='ID' else 140, anchor='w')
tree.grid(row=1, column=0, columnspan=7, sticky='nsew', pady=10)

frm.grid_columnconfigure(1, weight=1)
frm.grid_rowconfigure(1, weight=1)

#busqueda en tiempo real
entry_nombre.bind('<KeyRelease>', lambda e: actualizar())
entry_marca.bind('<KeyRelease>', lambda e: actualizar())
entry_categoria.bind('<KeyRelease>', lambda e: actualizar())

actualizar()
root.mainloop()
