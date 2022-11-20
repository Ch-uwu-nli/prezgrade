# from speech_evaluator import *
from audio_analysis import *
from app_ui import *

def evaluate_speech():
    wave_object = WaveFile(path)
    print(analyze_wave_file(wave_object))


if __name__ == "__main__":
    load_UI(evaluate_speech)

