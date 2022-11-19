import librosa, librosa.display
import numpy as num
import matplotlib.pyplot as plt

class WaveFile:
    """"""
    def __init__(self, name, path):
        self.file_name = name
        self.path = path
        self.wave = []

    def load(self, rate = 8000):
        return librosa.load(self.path, rate)

def display_waveform(wave_object):
    """"""
    wave, sr = wave_object.load()
    librosa.display.waveshow(wave, sr = sr)
    plt.show()


if __name__ == "__main__":
    fig, ax = plt.subplots(nrows=3, sharex=True)
    


    test2 = WaveFile("New_Recording_102.wav", "Tests/New_Recording_102.wav")
    wave2, sr2 = test2.load(24400)
    librosa.display.waveshow(wave2, sr = 24400, ax = ax[0])


    test1 = WaveFile("New_Recording_102.wav", "Tests/New_Recording_102.wav")
    wave1, sr1 = test1.load()
    librosa.display.waveshow(wave1, sr = 8000, ax = ax[1])
        
    plt.show()