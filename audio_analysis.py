import librosa, librosa.display
import matplotlib.pyplot as plt

class WaveFile:
    """A class to represent the wave properties of .wav files"""
    def __init__(self, path):
        self.path = path
        self.wave = []
        self.split_wave = []
        self.synthesized_wave = []
        self.duration = 0
        self.rate = 0
        self.silent_volume = 0

    def load(self, rate = 8000):
        """Loads the waveform and updates the self.wave, self.rate, and self.duration
        of the .wav file at a given path."""
        self.wave, self.rate = librosa.load(self.path, rate)
        self.duration = int(librosa.get_duration(self.wave, self.rate))

    def split_wave_file(self):
        """Splits the self.wave list into sublists containing one second worth of data
        each."""
        self.split_wave = []
        for i in range(self.duration):
            self.split_wave.append(self.wave[self.rate * i : (i + 1) * self.rate])
        

    def synthesize_wave(self):
        """Reduces the self.split_wave sublists by taking their average. Uses the 
        mean of the first three values and sets their mean multiplied by 100 as the
        self.silent_volume. If the wave file lasts less than 3 seconds, uses the first value
        multiplied by 100 as the self.silent_volume instead."""
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
    """A child class of WaveFile that stores the same
    attributes but with a lower sampling frequency."""
    def load(self, rate = 500):
        self.wave, self.rate = librosa.load(self.path, rate)
        self.duration = int(librosa.get_duration(self.wave, self.rate))



def analyze_wave_file(wave_object, display = False):
    """Loads all of the wave_object's attributes and
    returns a dictionary containing the number of long silences
    in the wave file and a list indicating the average volume every second.
    If display is set to true, displayes the waveform of the audio."""
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
    """Displays the waveform on a graph."""
    librosa.display.waveshow(wave_object.wave, wave_object.rate)
    plt.show()


def find_blanks(wave_object):
    """Returns the number of unusually long pauses in the wave file."""
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
    """Returns a list containing the average sound volume at every second
    while disregarding silences."""
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
        
        try:
            loudness_list.append(sum_segment_loudness / len(segment))
        except:
            pass

    return loudness_list



