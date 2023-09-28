from tkinter import *
from tkinter import messagebox
import json

window = Tk()
window.title("City Informator")
window.geometry('1050x600')
window.config(background="#F8F6F0",padx=80)


def save():

    place = places.get()
    name = input_ime.get()
    surname = input_prezime.get()
    date = input_termin.get()
    new_data = {
        places.get():{
            "Ime": name,
            "Prezime": surname,
            "Termin": date
        }}

    if len(name) == 0 or len(surname) == 0:
        messagebox.showinfo(title="Oops", meessage="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
        finally:
            input_ime.delete(0, END)
            input_prezime.delete(0, END)
            input_termin.delete(0, END)


canvas = Canvas(height=220 ,width=200)
canvas.grid(row=1,column=1)
img_sabac = PhotoImage(file="sabac_grb_1_35.png")
canvas.create_image(100, 100, image=img_sabac)
canvas.config(background="#F8F6F0")

title_label = Label(text="Grad Sabac", font=("Arial", 15))
title_label.grid(row=2, column=1)
subtitle_label = Label(text="Prvo izaberite zeljeno mesto a potom unesite licne podatke i termin")
subtitle_label.grid(row=3, column=1)

places = StringVar(window)
places.set("Opstina")

decision_box = OptionMenu(window, places, "Opstina", "MUP")
decision_box.grid(row=4, column=1)

label_ime = Label(text="Unesite Vase ime:")
label_ime.grid(row=5, columnspan=1)
label_ime.config(pady=15)
input_ime = Entry()
input_ime.grid(row=5, column=1)

label_prezime = Label(text="Unesite Vase prezime:")
label_prezime.grid(row=6, columnspan=1)
label_prezime.config(pady=8)
input_prezime = Entry()
input_prezime.grid(row=6, column=1)

label_termin = Label(text="Unesite zeljeni termin u formatu (DD-MM-YYYY):")
label_termin.grid(row=7, columnspan=1)
label_termin.config(pady=8)
input_termin = Entry()
input_termin.grid(row=7, column=1)

button = Button(text="ZAKAZI", height=1, width=20, command=save)
button.config(pady=8)
button.grid(row=8, column=1)

window.mainloop()