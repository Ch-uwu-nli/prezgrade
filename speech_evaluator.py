from audio_analysis import *
import numpy

def intonation(wdict, wobj):
    """list<int>->"""
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
    if delta_volume>1.0:
        message="You are speaking too loudly! Speak more softly; we can hear you well enough." 
    elif delta_volume<0.5:
        message="We can't hear you well. Don't be shy! Speak louder!"
    else: 
        message="The volume of your voice is perfect. Good job!" 
