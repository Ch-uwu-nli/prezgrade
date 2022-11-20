from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

# Tkinter frame
my_doc = Tk()

# Frame Size
my_doc.geometry("700x350")

def upload_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Wave Audio Files', '*.wav')])
   if file:
      filepath = os.path.abspath(file.name)
      Label(my_doc, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()

# Header
label = Label(my_doc, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Button
ttk.Button(my_doc, text="Browse", command=upload_file).pack(pady=20)

my_doc.mainloop()