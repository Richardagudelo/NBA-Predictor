import tkinter
from tkinter import *
from tkinter import ttk


raiz = Tk()
raiz.title("Simulador NBA 4000 PRO 4K V1.0")
raiz.geometry("1200x1000")
raiz.config(bg="pale green")
team_list = []


def llenar_team_list(lista):
    global team_list
    team_list = lista

def graficarImagen(text):
    miFrame = Frame()
    miFrame.pack()
    miFrame.config(bg="yellow")
    miFrame.place(x=500, y=250, width=200, height=200)
    miFrame.config(bd=5)
    text += ".png"
    # aun no se como tomar la carpeta del proyecto como raiz y de ahi cargar la imagen
# r"",text,".png")
    # "/Lenna.png"

    #imagen = PhotoImage(file=r"C:\Users\andre\Desktop\NBA-Predictor\img" + "\\" + text)
    imagen = PhotoImage(file=r"C:\Users\Usuario\PycharmProjects\NBA-Predictor\img" + "\\" + text)

    label = Label(miFrame, image=imagen)
    label.pack()
    raiz.mainloop()


label2 = Label(raiz, text="Equipo Ganador")
label2.pack(anchor=CENTER)
label2.config(fg="black",  # Foreground
              font=("Verdana", 12),
              bd=4, relief="ridge")
label2.place(x=500, y=450, width=200, height=40)


def mostrarTabla():
    ventana = Tk()
    ventana.title("Informacion adicional Simulacion Resultado 1000 temporadas")
    tabla = ttk.Treeview(ventana, columns=('#0', '#1', '#2', '#3', '#4'))
    tabla.grid(row=1, columns=1, columnspan=1)
    tabla.heading("#0", text="Ganador")
    tabla.heading("#1", text="Probabilidad De Ganar")
    tabla.heading("#2", text="Victorias")
    tabla.heading("#3", text="Playoff Wins")
    tabla.heading("#4", text="Season Wins")
    if len(team_list) > 0:
        for season_winner in team_list:
            tabla.insert("", tkinter.END, text=season_winner.name, values=(season_winner.win_prob,season_winner.wins,season_winner.playoffwins, season_winner.seasonwins))

    scrollbar = ttk.Scrollbar(ventana, orient=tkinter.VERTICAL, command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

    ventana.mainloop()

def update():
    global ventana
    ventana.deiconify()

butonTabla = Button(raiz, text="Mas informacion", command=mostrarTabla)
butonTabla.place(x=500, y=510, width=200, height=40)
butonTabla.config(fg="black",  # Foreground
                  font=("Verdana", 12),
                  bd=4)
butonTabla.pack(anchor=CENTER)

# lista de labels de los equipos
# ------------------------------------
labelE1 = Label(raiz, text="Equipo 1")
labelE1.pack(anchor=CENTER)
labelE1.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE1.place(x=10, y=10, width=130, height=40)

labelE2 = Label(raiz, text="Equipo 2")
labelE2.pack(anchor=CENTER)
labelE2.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE2.place(x=10, y=100, width=130, height=40)

labelE3 = Label(raiz, text="Equipo 3")
labelE3.pack(anchor=CENTER)
labelE3.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE3.place(x=10, y=190, width=130, height=40)

labelE4 = Label(raiz, text="Equipo 4")
labelE4.pack(anchor=CENTER)
labelE4.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE4.place(x=10, y=280, width=130, height=40)

labelE5 = Label(raiz, text="Equipo 5")
labelE5.pack(anchor=CENTER)
labelE5.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE5.place(x=10, y=370, width=130, height=40)

labelE6 = Label(raiz, text="Equipo 6")
labelE6.pack(anchor=CENTER)
labelE6.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE6.place(x=10, y=460, width=130, height=40)

labelE7 = Label(raiz, text="Equipo 7")
labelE7.pack(anchor=CENTER)
labelE7.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE7.place(x=10, y=550, width=130, height=40)

labelE8 = Label(raiz, text="Equipo 8")
labelE8.pack(anchor=CENTER)
labelE8.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelE8.place(x=10, y=640, width=130, height=40)

# lista de los Equipos de la derecha
# ---------------------------------------
labelW1 = Label(raiz, text="Equipo 1")
labelW1.pack(anchor=CENTER)
labelW1.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW1.place(x=1060, y=10, width=130, height=40)

labelW2 = Label(raiz, text="Equipo 2")
labelW2.pack(anchor=CENTER)
labelW2.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW2.place(x=1060, y=100, width=130, height=40)

labelW3 = Label(raiz, text="Equipo 3")
labelW3.pack(anchor=CENTER)
labelW3.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW3.place(x=1060, y=190, width=130, height=40)

labelW4 = Label(raiz, text="Equipo 4")
labelW4.pack(anchor=CENTER)
labelW4.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW4.place(x=1060, y=280, width=130, height=40)

labelW5 = Label(raiz, text="Equipo 5")
labelW5.pack(anchor=CENTER)
labelW5.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW5.place(x=1060, y=370, width=130, height=40)

labelW6 = Label(raiz, text="Equipo 6")
labelW6.pack(anchor=CENTER)
labelW6.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW6.place(x=1060, y=460, width=130, height=40)

labelW7 = Label(raiz, text="Equipo 7")
labelW7.pack(anchor=CENTER)
labelW7.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW7.place(x=1060, y=550, width=130, height=40)

labelW8 = Label(raiz, text="Equipo 8")
labelW8.pack(anchor=CENTER)
labelW8.config(fg="black",  # Foreground
               font=("Verdana", 12),
               bd=4, relief="ridge")
labelW8.place(x=1060, y=640, width=130, height=40)

# lista de los Cuartos Izquierda
# ---------------------------------------
labelE41 = Label(raiz, text="Equipo 1")
labelE41.pack(anchor=CENTER)
labelE41.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelE41.place(x=160, y=50, width=130, height=40)

labelE42 = Label(raiz, text="Equipo 2")
labelE42.pack(anchor=CENTER)
labelE42.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelE42.place(x=160, y=230, width=130, height=40)

labelE43 = Label(raiz, text="Equipo 3")
labelE43.pack(anchor=CENTER)
labelE43.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelE43.place(x=160, y=410, width=130, height=40)

labelE44 = Label(raiz, text="Equipo 4")
labelE44.pack(anchor=CENTER)
labelE44.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelE44.place(x=160, y=590, width=130, height=40)

# lista de los Cuartos Derecha
# ---------------------------------------
labelW41 = Label(raiz, text="Equipo 1")
labelW41.pack(anchor=CENTER)
labelW41.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelW41.place(x=910, y=50, width=130, height=40)

labelW42 = Label(raiz, text="Equipo 2")
labelW42.pack(anchor=CENTER)
labelW42.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelW42.place(x=910, y=230, width=130, height=40)

labelW43 = Label(raiz, text="Equipo 3")
labelW43.pack(anchor=CENTER)
labelW43.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelW43.place(x=910, y=410, width=130, height=40)

labelW44 = Label(raiz, text="Equipo 4")
labelW44.pack(anchor=CENTER)
labelW44.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelW44.place(x=910, y=590, width=130, height=40)

# lista de los SemiFinales Izq
# ---------------------------------------
labelE21 = Label(raiz, text="Equipo 1")
labelE21.pack(anchor=CENTER)
labelE21.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelE21.place(x=260, y=140, width=130, height=40)

labelE22 = Label(raiz, text="Equipo 2")
labelE22.pack(anchor=CENTER)
labelE22.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelE22.place(x=260, y=500, width=130, height=40)

# lista de los SemiFinales Der
# ---------------------------------------

labelW21 = Label(raiz, text="Equipo 1")
labelW21.pack(anchor=CENTER)
labelW21.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelW21.place(x=820, y=140, width=130, height=40)

labelW22 = Label(raiz, text="Equipo 2")
labelW22.pack(anchor=CENTER)
labelW22.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelW22.place(x=820, y=500, width=130, height=40)

# lista de los Finales Izq
# ---------------------------------------
labelEF = Label(raiz, text="Equipo 1")
labelEF.pack(anchor=CENTER)
labelEF.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
labelEF.place(x=340, y=330, width=130, height=40)

# lista de los Finales Der
# ---------------------------------------
labelWF = Label(raiz, text="Equipo 1")
labelWF.pack(anchor=CENTER)
labelWF.config(fg="black",  # Foreground
                font=("Verdana", 12),
                bd=4, relief="ridge")
#labelEF1.place(x=720, y=330, width=130, height=40)


labelWF.place(x=720, y=330, width=130, height=40)

# Mostrar en pantalla los equipos y cruces
def listOnScreen(eighth, quarter, semifinalE1, semifinalE2, semifinalW1, semifinalW2, final1, final2):
    # Octavos east (izquierda)
    labelE1.configure(text=eighth[0])
    labelE2.configure(text=eighth[1])
    labelE3.configure(text=eighth[2])
    labelE4.configure(text=eighth[3])
    labelE5.configure(text=eighth[4])
    labelE6.configure(text=eighth[5])
    labelE7.configure(text=eighth[6])
    labelE8.configure(text=eighth[7])
    # Octavos west (derecha)
    labelW1.configure(text=eighth[8])
    labelW2.configure(text=eighth[9])
    labelW3.configure(text=eighth[10])
    labelW4.configure(text=eighth[11])
    labelW5.configure(text=eighth[12])
    labelW6.configure(text=eighth[13])
    labelW7.configure(text=eighth[14])
    labelW8.configure(text=eighth[15])
    # Cuartos east (izquierda)
    labelE41.configure(text=quarter[0])
    labelE42.configure(text=quarter[1])
    labelE43.configure(text=quarter[2])
    labelE44.configure(text=quarter[3])
    # Cuartos west (derecha)
    labelW41.configure(text=quarter[4])
    labelW42.configure(text=quarter[5])
    labelW43.configure(text=quarter[6])
    labelW44.configure(text=quarter[7])
    # Semifinal east (izquierda)
    labelE21.configure(text=semifinalE1)
    labelE22.configure(text=semifinalE2)
    # Semifinal west (derecha)
    labelW21.configure(text=semifinalW1)
    labelW22.configure(text=semifinalW2)
    # # FINAL FINAL
    labelEF.configure(text=final1)
    labelWF.configure(text=final2)
