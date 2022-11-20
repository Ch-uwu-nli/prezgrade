from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os
from prezgrade import evaluate_speech

# Tkinter frame
my_doc = Tk()

# Frame Title
my_doc.title('PrezGrade')

# Frame Size
my_doc.geometry("1000x500")

# New window / destroy parent window
def new_window(results):
   intonation = "Intonation: " + str(round(results["Grades"][0] * 100)) + "% ; " + results["Intonation"]
   volume = "Sound Volume: " + str(round(results["Grades"][1]*100)) + "% ; " + results["Volume"]
   tone = "Tone: "+ str(round(results["Grades"][2]*100))+"% " + "; " + results["Tone"]
   overall_grade = "Overall Grade: " + str(round(results["Grades"][3]*100))+"%"

   new_window = Tk()

   results_display = Label(new_window, text=intonation, font=('Georgia 13')).place(x = 100, y = 100)
   results_display = Label(new_window, text=volume, font=('Georgia 13')).place(x = 100, y = 200)
   results_display = Label(new_window, text=tone, font=('Georgia 13')).place(x = 100, y = 300)
   results_display = Label(new_window, text=overall_grade, font=('Georgia 13')).place(x = 100, y = 400)
   
   
   new_window.title('Results')

   new_window.geometry("1000x500")

   my_doc.destroy()


#
def process_file():
   new_window(evaluate_speech())


# Header
label = Label(my_doc, text="Prezgrade", font=('Georgia 15'))
label.pack(pady=10)

# File Path 

def upload_file():

   file = filedialog.askopenfile(mode='r', filetypes=[('Wave Audio Files', '*.wav')])
   if file:
      filepath = os.path.abspath(file.name)
      Label(my_doc, text="The File selected : " + str(filepath), font=('Aerial 11')).pack()
      with open("path.txt", "w") as reference_file:
         reference_file.write(str(filepath))

# Upload Button
ttk.Button(my_doc, text="Upload", command=upload_file).pack(pady=20)

# Start Button
ttk.Button(my_doc, text="Start", command=process_file).pack(pady=20)

label = Label(my_doc, text="User Guide:", font=('Georgia 13'))
label = Label(my_doc, text="For best results, here are some suggestions to keep in mind during the recording.\nKeep a distance of 0.5 meters from the mic.\nLeave the first 3 seconds silent for calibration purposes.", font=('Georgia 13')).place(x=200, y=400)

my_doc.mainloop()