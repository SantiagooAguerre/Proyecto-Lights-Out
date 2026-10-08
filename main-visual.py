from juego import Game
import tkinter as tk
from tkinter import messagebox, Scrollbar, RIGHT, Y
from tkinter import *

app = tk.Tk()
app.title("Lights Out")

size = { "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

juego = Game()
botones = []

def mostrar_instrucciones():
    messagebox.showinfo("¿Cómo se juega?", """
El objetivo es apagar todas las luces del tablero.
Para hacerlo, elige una fila y una columna.
Al apretar una posición:
    - La luz seleccionada cambia de estado.
    - La luz de arriba cambia de estado.
    - La luz de abajo cambia de estado.
    - La luz de la izquierda cambia de estado.
    - La luz de la derecha cambia de estado.
    
Las posiciones que están fuera del tablero simplemente no existen.
    
Verde = luz encendida
Gris = luz apagada
        
Se gana cuando todas las luces estén apagadas.
""")


def elegir_tamaño(tamaño):
    global botones
    juego.SelectSizeGame(tamaño)
    for widget in tablero_frame.winfo_children():
        widget.destroy()
    botones = []
    for i in range(tamaño):
        fila_botones = []
        for j in range(tamaño):
            boton = tk.Button(tablero_frame, width=10, height=4, command=lambda x=i, y=j: presionar(x, y))
            boton.grid(row=i, column=j, padx=2, pady=2)
            fila_botones.append(boton)
        botones.append(fila_botones)
    actualizar_tablero()


def presionar(x, y):
    juego.set_ady(x, y)
    actualizar_tablero()
    if juego.CheckWin() == 1:
        messagebox.showinfo("Lights Out", "Felicitaciones! Resolviste el puzzle!")
        app.quit()


def actualizar_tablero():
    tablero = juego.get_board()
    for i in range(juego.size):
        for j in range(juego.size):
            if tablero[i][j] == 1:
                botones[i][j].config(background="green")
            else:
                botones[i][j].config(background="lightgray")

instrucciones = tk.Button(app, text="¿Cómo se juega?", font=("Arial", 12, "bold") , command=mostrar_instrucciones)
instrucciones.pack(pady=10)

tamaño_label = tk.Label(app, text="Elige el tamaño del tablero:", font=("Arial", 14))
tamaño_label.pack(pady=5)

tamaños_frame = tk.Frame(app)
tamaños_frame.pack(pady=5)

for tamaño in size.values():
    boton = tk.Button(tamaños_frame, text=f"{tamaño}x{tamaño}", font=("Arial", 12), command=lambda t=tamaño: elegir_tamaño(t))
    boton.pack(side="left", padx=4, fill="x")

scroll_bar = tk.Scrollbar(app)
scroll_bar.pack(side="right", fill="y")

canvas = tk.Canvas(app, yscrollcommand=scroll_bar.set)
canvas.pack(fill="both", expand=True)

scroll_bar.config(command=canvas.yview)

tablero_frame = tk.Frame(canvas)

canvas.create_window((0, 0), window=tablero_frame)

def actualizar_scroll(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

tablero_frame.bind("<Configure>", actualizar_scroll)

tablero = tk.Button(app, text="Salir", font=("Arial", 13), bg="black", fg="white", command=app.quit)
tablero.pack(pady=5, padx=30, fill="x")

app.mainloop()