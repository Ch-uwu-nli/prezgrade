import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile

my_doc = tk.Tk()
my_doc.geometry("1000x1000")
my_doc.title('prezGrade')

doc_font1 = ('Roboto', 20, 'bold')

header1 = tk.Label(my_doc, text='Upload File & Read', width=25, font=doc_font1)
header1.grid(row=1, column=1)

button1 = tk.Button(my_doc, text='Upload File', width=20, command=lambda:upload_file())
button1.grid(row=2, column=1)

my_doc.mainloop()