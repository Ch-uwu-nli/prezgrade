import librosa, librosa.display
import numpy as num
import matplotlib.pyplot as plt

class WaveFile:
    """"""
    def __init__(self, name, path):
        self.file_name = name
        self.path = path
        self.wave = []
        self.split_wave = []
        self.synthesized_wave = []
        self.duration = 0
        self.rate = 0
        self.silent_volume = 0

    def load(self, rate = 8000):
        self.wave, self.rate = librosa.load(self.path, rate)
        self.duration = int(librosa.get_duration(self.wave, self.rate))

    def split_wave_file(self):
        self.split_wave = []
        for i in range(self.duration):
            self.split_wave.append(self.wave[self.rate * i : (i + 1) * self.rate])
        

    def synthesize_wave(self):
        synthesized_wave = []
        for sublist in self.split_wave:
            sum_of_sublist = 0
            for num in sublist:
                sum_of_sublist += num
            synthesized_wave.append(sum_of_sublist / len(sublist))
        self.synthesized_wave = synthesized_wave
        self.silent_volume = synthesized_wave[0]
            

def analyze_wave_file(wave_object, display = False):
    """"""
    wave_data = {}
    wave_object.load()
    wave_object.split_wave_file()
    wave_object.synthesize_wave()
    # wave_data["blanks"] = find_blanks(wave_object)
    wave_data["volume"] = get_loudness(wave_object)
    if display:
        display_waveform(wave_object)
    
    return wave_data


def display_waveform(wave_object):
    """"""
    librosa.display.waveshow(wave_object.wave, wave_object.rate)
    plt.show()


def find_blanks(wave_object):
    """"""
    
def get_loudness(wave_object):
    """"""
    reduced_waveform = []
    for sublist in wave_object.split_wave:
        wave_segment = []
        for value in sublist:
            if abs(value) > wave_object.silent_volume:
                wave_segment.append(value)
        reduced_waveform.append(wave_segment)
    
    loudness_list = []
    for segment in reduced_waveform:
        sum_segment_loudness = 0
        for value in segment:
            sum_segment_loudness += abs(value)
        
        loudness_list.append(sum_segment_loudness / len(segment))

    return loudness_list


if __name__ == "__main__":
    # fig, ax = plt.subplots(nrows=3, sharex=True)

    # test2 = WaveFile("New_Recording_102.wav", "Tests/New_Recording_102.wav")
    # wave2, sr2 = test2.load(24400)
    # librosa.display.waveshow(wave2, sr = 24400, ax = ax[0])


    test1 = WaveFile("New_Recording_102.wav", "Tests/New_Recording_102.wav")
    # wave1, sr1 = test1.load()
    # librosa.display.waveshow(wave1, sr = 8000, ax = ax[1])
        
    # plt.show()

    # test3 = WaveFile("New_Recording_104.wav", "Tests/New_Recording_104.wav")
    print(analyze_wave_file(test1))
    # display_waveform(test3)

    # with open("Recording104.txt", "w") as file:
    #     test3.load
    #     for num in test3.wave:
    #         file.write(str(num) + " - ")

    # test3.load()
    # test3.split_wave_file()
    # print(test3.split_wave)