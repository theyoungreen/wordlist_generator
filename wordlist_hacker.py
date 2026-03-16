import random
import string
import threading
import tkinter as tk
from tkinter import filedialog

running = False
lineas_generadas = []

simbolos = ["!", "@", "#", "$", "%", "&", "*", "_", "-", "+"]
numeros_tipicos = ["123", "1234", "12345", "2024", "2025", "007", "69", "666"]
palabras_extra = ["admin", "root", "user", "login", "pass", "love", "god", "master"]

def generar_linea(base):

    opcion = random.randint(1, 8)

    if opcion == 1:
        return base + random.choice(numeros_tipicos)

    elif opcion == 2:
        return base.capitalize() + random.choice(simbolos)

    elif opcion == 3:
        return random.choice(palabras_extra) + base

    elif opcion == 4:
        return base.upper() + str(random.randint(0, 99999))

    elif opcion == 5:
        return base + random.choice(simbolos) + str(random.randint(0, 9999))

    elif opcion == 6:
        mezcla = list(base)
        random.shuffle(mezcla)
        return "".join(mezcla) + random.choice(numeros_tipicos)

    elif opcion == 7:
        return base + str(random.randint(1900, 2030))

    else:
        extra = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        return base + extra


def proceso():

    global running
    base = entrada.get()
    contador = 0

    while running:
        linea = generar_linea(base)
        lineas_generadas.append(linea)
        contador += 1

        if contador % 5000 == 0:
            texto.insert(tk.END, f"Generadas: {contador}\n")
            texto.see(tk.END)


def iniciar():
    global running
    if not running:
        running = True
        hilo = threading.Thread(target=proceso)
        hilo.start()


def detener():
    global running
    running = False
    guardar_archivo()


def guardar_archivo():

    ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivo de texto", "*.txt")],
        title="Guardar wordlist"
    )

    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            for linea in lineas_generadas:
                f.write(linea + "\n")

        texto.insert(tk.END, f"\n✅ Guardado en: {ruta}\n")
        texto.see(tk.END)


# ===== INTERFAZ =====

ventana = tk.Tk()
ventana.title("Hacker Wordlist Generator")
ventana.configure(bg="black")
ventana.geometry("700x500")

titulo = tk.Label(
    ventana,
    text="WORDLIST GENERATOR",
    fg="lime",
    bg="black",
    font=("Courier", 22)
)
titulo.pack(pady=10)

entrada = tk.Entry(
    ventana,
    font=("Courier", 16),
    bg="black",
    fg="lime",
    insertbackground="lime"
)
entrada.pack(pady=10)

btn_start = tk.Button(
    ventana,
    text="START",
    command=iniciar,
    bg="black",
    fg="lime",
    font=("Courier", 14)
)
btn_start.pack(pady=5)

btn_stop = tk.Button(
    ventana,
    text="STOP & SAVE",
    command=detener,
    bg="black",
    fg="red",
    font=("Courier", 14)
)
btn_stop.pack(pady=5)

texto = tk.Text(
    ventana,
    bg="black",
    fg="lime",
    font=("Courier", 10)
)
texto.pack(expand=True, fill="both", pady=10)

ventana.mainloop()
