from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

# Tkinter frame
my_doc = Tk() #This is the main frame where the user will be uploading his .wav audio file.

# Frame Title
my_doc.title('PrezGrade')

# Frame Size
my_doc.geometry("1000x500") 

# New window / destroy parent window
def new_window():
   new_window = Tk()

   new_window.title('Results')

   new_window.geometry("1000x500")

   my_doc.destroy() #This will close the main frame as it displays the results

# Header
label = Label(my_doc, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# File Path 
def upload_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Wave Audio Files', '*.wav')])
   if file:
      filepath = os.path.abspath(file.name) #This retrieves the path to the file.
      
      Label(my_doc, text="The File is located at : " + str(filepath), font=('Aerial 11')).pack()

# Upload Button
ttk.Button(my_doc, text="Upload", command=upload_file).pack(pady=20) 
#The button allows the user to go to his file explorer to seek the file they wish to upload

# Start Button
ttk.Button(my_doc, text="Start", command=new_window).pack(pady=20)
#The button allows the program to evaluate the submitted file

my_doc.mainloop()