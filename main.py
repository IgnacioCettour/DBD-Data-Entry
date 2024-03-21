from customtkinter import CTk, CTkFrame
import customtkinter
import openpyxl
from time import strftime


def funcion(entry1,entry2,entry3,entry4
            ,player,checkbox,combobox):
    
    Personaje, Killer, Puntos, Mapa, = entry1.get(), entry2.get(), int(entry3.get()), entry4.get()
    Jugador, Escape, Cuelgues = player.get(), checkbox.get(), int(combobox.get())


    if Escape == 0:
        Escape = 'No'
    if Escape == 1:
        Escape = 'Si'

    Hora = strftime("%d/%m/%Y/%H:%M ")

    filepath = "C:\Programa Python-Excel\DBD-INFO.xlsx"
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([Hora,Jugador,Personaje,Escape,Killer,Mapa,Cuelgues,Puntos])
    workbook.save(filepath)


app = customtkinter.CTk()
app.geometry("600x500")
app.title("Data Entry")
app.resizable(width=False, height=False)

label = customtkinter.CTkLabel(app, text="Jugador")
label.place(x=270,y=20)

Players = customtkinter.CTkComboBox(app, values=['NachitoKujo','Martufour'],state="readonly")
Players.place(x=230, y=50)

entry1 = customtkinter.CTkEntry(app, placeholder_text="Personaje")
entry1.place(x=230,y=100)

checkbox = customtkinter.CTkCheckBox(app, text="Escape") # No = 0, Si = 1
checkbox.place(x=230,y=150)

label2 = customtkinter.CTkLabel(app, text="Cuelgues")
label2.place(x=270, y=190)

combobox = customtkinter.CTkComboBox(app, values=['0','1','2','3'],state='readonly')
combobox.place(x=230,y=220)

entry2 = customtkinter.CTkEntry(app, placeholder_text="Killer")
entry2.place(x=230,y=270)

entry3 = customtkinter.CTkEntry(app, placeholder_text="Puntos")
entry3.place(x=230,y=320)

entry4 = customtkinter.CTkEntry(app, placeholder_text="Mapa")
entry4.place(x=230,y=370)

button = customtkinter.CTkButton(app, text="Agregar", command=lambda:funcion(entry1,entry2,entry3,
                                                                             entry4,Players,checkbox,combobox))
button.place(x=230,y=430)

app.mainloop()