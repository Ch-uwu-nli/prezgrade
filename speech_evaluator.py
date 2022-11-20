import audio_analysis as *
import numpy

def intonation(wdict, wobj):
    """list<int>->"""
    avg_list=wdict["volume"]
    standard_deviation=numpy.std(avg_list)


def overall_volume(wdict, wobj):
    """list<int>->num"""
    avg_list=wdict["volume"]
    overall_silence=wobj.silent_volume
    average_volume=sum(avg_list)/len(avg_list)
    delta_volume=average_volume-overall_silence

