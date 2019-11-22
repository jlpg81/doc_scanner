import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Tk, StringVar, Label
import os, sys
from PIL import Image, ImageTk
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

#Functions
def fileDialog():
    global filename
    global img_var
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetype = (("All Files", "*.*"), ("png", "*.png"), ("jpeg", "*.jpg")))
    documentname = filename.split('/')[-1]
    pathlabel.config(text=documentname)
    img_var = ImageTk.PhotoImage(Image.open(filename).resize((490,490)))
    photoscreen.config(image=img_var, text="")
    return filename

def scanFile():
    image = Image.open(filename)
    content = pytesseract.image_to_string(image, lang="eng")
    textscreen.delete("1.0",END)
    textscreen.insert("1.0", content)

def saveFile():
    save_path = filedialog.asksaveasfilename(filetype = (("Text File", ".txt"),("All Files", "*.*")), initialfile="scanned-file.txt" )
    filename = os.path.basename(save_path)
    content = textscreen.get("1.0",END)
    text_file = open(save_path, "w",  encoding="utf-8")
    text_file.write(content)
    text_file.close()

def info_window():
    newwin = Toplevel(root)
    display = Label(newwin, width=25, height=10, text="Program created by Jorge Perez \n\n jorgeperezgomez.com")
    display.pack()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#GUI Start
root=tk.Tk()
root.title("Doc Scanner")
root.geometry("1015x615")
root.geometry("+50+50")

#Icons
image_size = (70,70)
open_icon = ImageTk.PhotoImage(Image.open(resource_path("open.png")).resize(image_size))
scan_icon = ImageTk.PhotoImage(Image.open(resource_path("scan.png")).resize(image_size))
save_icon = ImageTk.PhotoImage(Image.open(resource_path("save.png")).resize(image_size))
info_icon = ImageTk.PhotoImage(Image.open(resource_path("info.png")).resize(image_size))

#Left Buttons
ttk.Button(root, text = "Open", image=open_icon, command = fileDialog, compound = TOP).place(x=5, y=5, height=100, width=100)
pathlabel = Label(root, width=25, text="")
pathlabel.place(x=110, y=52, width = 300)

#Right Buttons
ttk.Button(root, text = "Scan", image=scan_icon, command = scanFile, compound = TOP).place(x=510, y=5, height=100, width=100)
ttk.Button(root, text = "Save", image=save_icon, command = saveFile, compound = TOP).place(x=615, y=5, height=100, width=100)
ttk.Button(root, text = "Info", image=info_icon, command= info_window, compound = TOP).place(x=720, y=5, height=100, width=100)

#Screens
# photoscreen = tk.Label(root, bg = "white")
photoscreen = tk.Label(root,text="Select an image", image="", bg = "white")
photoscreen.place(x=5, y=110, height=500, width=500)

textscreen = tk.Text(root)
textscreen.place(x=510, y=110, height=500, width=500)




root.mainloop()
