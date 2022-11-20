from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

# Tkinter frame
my_doc = Tk()

# Frame Title
my_doc.title('PrezGrade')

# Frame Size
my_doc.geometry("1000x500")

# New window / destroy parent window
def new_window():
   new_window = Tk()

   new_window.title('Results')

   new_window.geometry("1000x500")

   my_doc.destroy()

# Header
label = Label(my_doc, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# File Path 
def upload_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Wave Audio Files', '*.wav')])
   if file:
      filepath = os.path.abspath(file.name)
      Label(my_doc, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()

# Upload Button
ttk.Button(my_doc, text="Upload", command=upload_file).pack(pady=20)

# Start Button
ttk.Button(my_doc, text="Start", command=new_window).pack(pady=20) #def run_program


my_doc.mainloop()