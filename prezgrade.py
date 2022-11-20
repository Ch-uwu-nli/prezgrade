from audio_analysis import *

def evaluate_speech():
    with open("path.txt", "r") as path_file:
        path = path_file.read().strip()
    wave_object = WaveFile(path)
    wave_data = analyze_wave_file(wave_object)

    score1 = intonation(wave_data)
    score2 = overall_volume(wave_data, wave_object)
    score3 = blanks_grade(wave_object, wave_data)
    final_grade = total_grade(score1, score2, score3)

    intonation_review = intonation_message(wave_data)
    volume_review = volume_message(wave_data, wave_object)
    flow_review = blanks_comment(wave_data)
    
    return {"Grades": [score1, score2, score3, final_grade], "Intonation" : intonation_review, "Volume" : volume_review, "Tone" : flow_review}