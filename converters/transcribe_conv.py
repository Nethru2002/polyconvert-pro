import whisper
import os
import warnings
from .base import BaseConverter

# Suppress tiny AI warnings for a cleaner console
warnings.filterwarnings("ignore")

class TranscribeConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        # Audio formats to Text
        audio_formats = ['mp3', 'wav', 'm4a', 'flac', 'mp4']
        return source_ext in audio_formats and target_ext == 'txt'

    def convert(self, input_path, output_path):
        print(f"--- Loading AI Model... ---")
        
        model = whisper.load_model("base") 
        
        print(f"--- Transcribing: {os.path.basename(input_path)} ---")
        print("Note: This may take a few minutes depending on audio length.")
        
        # Perform the transcription
        result = model.transcribe(input_path)
        
        # Save the text to the output file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
            
        return True