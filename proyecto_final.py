import tkinter as tk
from tkinter import ttk, messagebox
import json

# ---------- Configuración ----------
ARCHIVO_DATOS = "inventario.json"
inventario = {}

# ---------- Funciones de persistencia ----------
def guardar_inventario():
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(inventario, archivo, indent=4)

def cargar_inventario():
    global inventario
    try:
        with open(ARCHIVO_DATOS, "r") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = {}

# ---------- Funciones de gestión ----------
def agregar_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    try:
        cantidad = int(entrada_cantidad.get())
        if fruta:
            inventario[fruta] = inventario.get(fruta, 0) + cantidad
            guardar_inventario()
            actualizar_lista()
            limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Ingrese el nombre de la fruta.")
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida. Ingrese un número entero.")

def eliminar_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    if fruta in inventario:
        del inventario[fruta]
        guardar_inventario()
        actualizar_lista()
        limpiar_campos()
    else:
        messagebox.showinfo("Eliminar", f"La fruta '{fruta}' no existe.")

def editar_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    try:
        cantidad = int(entrada_cantidad.get())
        if fruta in inventario:
            inventario[fruta] = cantidad
            guardar_inventario()
            actualizar_lista()
            limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", f"La fruta '{fruta}' no está registrada.")
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida.")

def disminuir_fruta():
    fruta = entrada_fruta.get().strip().capitalize()
    try:
        cantidad = int(entrada_cantidad.get())
        if fruta in inventario:
            if cantidad <= inventario[fruta]:
                inventario[fruta] -= cantidad
                guardar_inventario()
                actualizar_lista()
                limpiar_campos()
                if inventario[fruta] == 0:
                    messagebox.showinfo("Aviso", f"'{fruta}' ahora tiene 0 unidades.")
            else:
                messagebox.showwarning("Advertencia", "Cantidad mayor a la disponible.")
        else:
            messagebox.showinfo("Aviso", "Fruta no encontrada.")
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida.")

def buscar_fruta(*args):
    consulta = entrada_busqueda.get().strip().lower()
    lista_frutas.delete(0, tk.END)
    for fruta, cantidad in inventario.items():
        if consulta in fruta.lower():
            lista_frutas.insert(tk.END, f"{fruta}: {cantidad}")

def seleccionar_fruta(event):
    seleccion = lista_frutas.curselection()
    if seleccion:
        item = lista_frutas.get(seleccion[0])
        fruta, cantidad = item.split(":")
        entrada_fruta.delete(0, tk.END)
        entrada_fruta.insert(0, fruta.strip())
        entrada_cantidad.delete(0, tk.END)
        entrada_cantidad.insert(0, cantidad.strip())

def actualizar_lista():
    lista_frutas.delete(0, tk.END)
    for fruta, cantidad in inventario.items():
        lista_frutas.insert(tk.END, f"{fruta}: {cantidad}")

def limpiar_campos():
    entrada_fruta.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)

# ---------- Cargar inventario ----------
cargar_inventario()

# ---------- Ventana principal ----------
ventana = tk.Tk()
ventana.title("🍓 Inventario de Frutas")
ventana.geometry("550x550")
ventana.configure(bg="#f9f9f9")

# ---------- Estilo moderno ----------
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("TButton", padding=6, font=("Arial", 10))
estilo.configure("TLabel", background="#f9f9f9", font=("Arial", 10))
estilo.configure("TEntry", padding=5)

# ---------- Widgets ----------
ttk.Label(ventana, text="Fruta:").pack(pady=(10, 0))
entrada_fruta = ttk.Entry(ventana, width=30)
entrada_fruta.pack(pady=5)

ttk.Label(ventana, text="Cantidad:").pack()
entrada_cantidad = ttk.Entry(ventana, width=30)
entrada_cantidad.pack(pady=5)

# Botones
frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=10)

ttk.Button(frame_botones, text="Agregar", command=agregar_fruta).grid(row=0, column=0, padx=5)
ttk.Button(frame_botones, text="Editar", command=editar_fruta).grid(row=0, column=1, padx=5)
ttk.Button(frame_botones, text="Eliminar", command=eliminar_fruta).grid(row=0, column=2, padx=5)
ttk.Button(frame_botones, text="Disminuir", command=disminuir_fruta).grid(row=0, column=3, padx=5)

# Buscador
ttk.Label(ventana, text="Buscar fruta:").pack(pady=(10, 0))
entrada_busqueda = ttk.Entry(ventana, width=30)
entrada_busqueda.pack(pady=5)
entrada_busqueda.bind("<KeyRelease>", buscar_fruta)

# Lista
ttk.Label(ventana, text="Inventario actual:", font=("Arial", 10, "bold")).pack(pady=5)
lista_frutas = tk.Listbox(ventana, width=45, height=12)
lista_frutas.pack(pady=5)
lista_frutas.bind("<<ListboxSelect>>", seleccionar_fruta)

# Mostrar datos
actualizar_lista()

ventana.mainloop()