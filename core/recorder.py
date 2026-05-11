import speech_recognition as sr
import os
from datetime import datetime

def record_live_audio():
    r = sr.Recognizer()
    r.energy_threshold = 50
    r.dynamic_energy_threshold = False
    
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            try:
                audio = r.listen(source, timeout=30, phrase_time_limit=30)
            except sr.WaitTimeoutError:
                raise Exception("No voice detected. Please try again and speak clearly.")

        temp_filename = f"temp_voice_{datetime.now().strftime('%H%M%S')}.wav"
        with open(temp_filename, "wb") as f:
            f.write(audio.get_wav_data())
            
        return temp_filename

    except Exception as e:
        raise Exception(str(e))