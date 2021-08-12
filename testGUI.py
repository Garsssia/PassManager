from passwordgenerator import randompass
import tkinter as tk
win = tk.Tk()
texto = randompass(True,True,25)

def changetext():
    texto = randompass(True,True,25)
    a.config(text=texto)
    
a = tk.Label(win, text="hello world")
a.pack()
tk.Button(win, text="Change Label Text", command=changetext).pack()

win.mainloop()