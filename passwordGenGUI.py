
from passwordgenerator import randompass
import tkinter as tk
import pyperclip
import string
import random



numericos = True
punt = True
passsize = 25
textlabel = ""
app = tk.Tk()
app.title('Password generator')
app.geometry("300x200")

lbl0 = tk.Label(app)
lbl0.pack()

def randompass(digits,punt,size):
    
    if(isinstance(digits,bool) and isinstance(punt,bool) and isinstance(size,int) and size>0):
        if digits == True and punt == True:
            password = random.choices(string.punctuation+string.ascii_letters+string.digits,k=size)
        elif digits == False and punt == True:
            password = random.choices(string.punctuation+string.ascii_letters,k=size)
        elif digits == True and punt == False:
            password = random.choices(string.digits+string.ascii_letters,k=size)
        elif digits == False and punt==False:
            password = random.choices(string.ascii_letters,k=size)
        vuelta = ""
        for p in password:
            vuelta += p
    
    else:    
        vuelta = []

    return vuelta

def toggle1():
    global numericos 
    if toggle_btn1.config('relief')[-1] == 'sunken':
        toggle_btn1.config(relief="raised")
        
        numericos = True
    else:
        toggle_btn1.config(relief="sunken")
        
        numericos = False
        

def toggle2():
    global punt
    if toggle_btn2.config('relief')[-1] == 'sunken':
        toggle_btn2.config(relief="raised")
        
        punt = True
        
    else:
        toggle_btn2.config(relief="sunken")
        
        punt = False
        

def changetext():
    textlabel = randompass(numericos,punt,passsize)
    lbl.config(text=textlabel)

def copytoclip():
    pyperclip.copy(textlabel)    
  

#Botones

toggle_btn1 = tk.Button(text = "Numbers", width=15, relief="raised",command=toggle1)
toggle_btn1.pack(pady=5)
toggle_btn2 = tk.Button(text = "Punctuation", width=15, relief="raised",command=toggle2)
toggle_btn2.pack(pady=5)
generate_butt = tk.Button(text="Generate Password", width=15, relief="raised", command=changetext)
generate_butt.pack(pady=5)

copybutton = tk.Button(text="Copy to Clipboard",width=15, relief="raised", command=copytoclip)
copybutton.pack(pady=5)

#Etiquetas
    
lbl = tk.Label(app,text=textlabel)
lbl.config(fg="black", bg = "white",relief = "flat")
lbl.pack(pady=5)  


app.mainloop()
