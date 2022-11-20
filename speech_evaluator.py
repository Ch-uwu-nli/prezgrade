from audio_analysis import *
import numpy

def intonation(wdict):
    """list<int>->"""
    avg_list=wdict["volume"]
    standard_deviation=numpy.std(avg_list)
    if standard_deviation>0.1:
        grade=0.1/standard_deviation
    elif 0.02>standard_deviation>0:
        grade=standard_deviation/0.02
    else:
        grade=1.0
    return grade



def intonation_message(wdict):
    avg_list=wdict["volume"]
    standard_deviation=numpy.std(avg_list)
    if standard_deviation>0.1:
        message="The volume of your voice fluctuates too much! Try to maintain a more consistent speech volume."
    elif 0.02>standard_deviation>0:
        message="Your voice is too monotonous! Try to vary the volume of your voice a bit." 
    else:
        message="The intonation of your voice is perfect. Keep up the good work!"


def overall_volume(wdict, wobj):
    """list<int>->num"""
    avg_list=wdict["volume"]
    overall_silence=wobj.silent_volume
    average_volume=sum(avg_list)/len(avg_list)
    delta_volume=average_volume-overall_silence
    grade=100
    if delta_volume>1.0:
        grade=1/delta_volume
    elif delta_volume<0.5:
        grade=delta_volume/0.5
    else: 
        grade=1.0
    return grade


def volume_message(wdict,wobj):
    avg_list=wdict["volume"]
    overall_silence=wobj.silent_volume
    average_volume=sum(avg_list)/len(avg_list)
    delta_volume=average_volume-overall_silence
    if delta_volume>1.0:
        message="You are speaking too loudly! Try to speak more softly." 
    elif delta_volume<0.5:
        message="We can't hear you well. Don't be shy! Speak louder!"
    else: 
        message="The volume of your voice is perfect. Good job!" 

def blanks_grade(wobj, wdict):
    length=wobj.duration/60
    max_mistakes=5*length
    number_of_blanks=wdict["blanks"]
    grade= 1-number_of_blanks/max_mistakes
    if number_of_blanks>max_mistakes:
        grade=0
    return grade
    


def total_grade(grade1, grade2, grade3):
    return grade1/3+grade2/3+grade3/3