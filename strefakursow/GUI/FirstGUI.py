import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Witaj w Kursie python dla Zaawansowanych - Strefa Kursów")
#win.resizable(0,0)

#Label
aLabel = ttk.Label(win, text="Tekst bez zmiany")
aLabel.grid(column=0, row=0)

#Button Click Event Function
def clickMe():
    action.configure(text="** Zostałem Kliknięty! **")
    aLabel.configure(foreground='red')
    aLabel.configure(text="Tekst po zmianie")

#Adding a Button
action = ttk.Button(win, text="Kliknij mnie", command=clickMe)
action.grid(column=1, row=1)

win.mainloop()