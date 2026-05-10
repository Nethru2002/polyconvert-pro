import speech_recognition as sr
import os
from datetime import datetime

def record_live_audio():
    r = sr.Recognizer()
    
    # Use the default microphone
    with sr.Microphone() as source:
        print("--- Adjusting for background noise... ---")
        r.adjust_for_ambient_noise(source, duration=1)
        print("--- Listening... (Speak now) ---")
        
        # Record until there is silence
        audio = r.listen(source)
        
    # Save the captured audio to a temporary file
    temp_filename = f"temp_voice_{datetime.now().strftime('%H%M%S')}.wav"
    with open(temp_filename, "wb") as f:
        f.write(audio.get_wav_data())
        
    return temp_filename