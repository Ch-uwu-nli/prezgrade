import librosa, librosa.display
import numpy as num
import matplotlib.pyplot as plt

class WaveFile:
    """"""
    def __init__(self, path):
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
        try:
            self.silent_volume = (abs(synthesized_wave[0]) + abs(synthesized_wave[1]) + abs(synthesized_wave[2])) * 100 / 3
        except IndexError:
            self.silent_volume = abs(synthesized_wave[0]) * 100
            

class LowResWaveFile(WaveFile):
    def load(self, rate = 500):
        self.wave, self.rate = librosa.load(self.path, rate)
        self.duration = int(librosa.get_duration(self.wave, self.rate))



def analyze_wave_file(wave_object, display = False):
    """"""
    wave_data = {}
    wave_object.load()
    wave_object.split_wave_file()
    wave_object.synthesize_wave()
    wave_data["blanks"] = find_blanks(wave_object)
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
    downscaled_wave = LowResWaveFile(wave_object.path)
    number_of_pauses = 0

    downscaled_wave.load()
    downscaled_wave.split_wave_file()
    downscaled_wave.synthesize_wave()
    
    new_pause = True
    pause_frames = 0
    uncertainty_counter = 250
    for num in downscaled_wave.wave:
        if new_pause and abs(num) <= downscaled_wave.silent_volume:
            new_pause = False
            pause_frames = 1
        elif not new_pause and abs(num) <= downscaled_wave.silent_volume:
            pause_frames += 1
            if pause_frames == 500:
                number_of_pauses += 1
        elif not new_pause and abs(num) > downscaled_wave.silent_volume:
            if uncertainty_counter != 0:
                pause_frames += 1
                uncertainty_counter -= 1
            else:
                new_pause = True
                uncertainty_counter = 500
                pause_frames = 0
    return number_of_pauses
    

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
    # test2.load(24400)
    # wave2 = test2.wave
    # librosa.display.waveshow(wave2, sr = 24400, ax = ax[0])


    # test1 = WaveFile("New_Recording_102.wav", "Tests/New_Recording_102.wav")
    # test1.load()
    # wave1 = test1.wave
    # librosa.display.waveshow(wave1, sr = 8000, ax = ax[1])
    # a=500

    # test3 = WaveFile("New_Recording_102.wav", "Tests/New_Recording_102.wav")
    # test3.load(a)
    # wave3 = test3.wave
    # librosa.display.waveshow(wave3, sr = a, ax = ax[2])

    # plt.show()


    test3 = WaveFile("Tests/testv3.wav")
    print(analyze_wave_file(test3))
    # display_waveform(test3)

    # with open("Recording104.txt", "w") as file:
    #     test3.load
    #     for num in test3.wave:
    #         file.write(str(num) + " - ")

    # test3.load()
    # test3.split_wave_file()
    # print(test3.split_wave)