import whisper
import os
import warnings
import sys
from .base import BaseConverter

FFMPEG_PATH = r'C:\ffmpeg\bin'
os.environ["PATH"] += os.pathsep + FFMPEG_PATH

warnings.filterwarnings("ignore")

class TranscribeConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        audio_formats = ['mp3', 'wav', 'm4a', 'flac', 'mp4']
        return source_ext in audio_formats and target_ext == 'txt'

    def convert(self, input_path, output_path):
        if not os.path.exists(input_path):
            raise Exception(f"Input file not found at {input_path}")

        try:
            model = whisper.load_model("tiny") 
            
            result = model.transcribe(input_path, fp16=False)
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])
            return True
        except FileNotFoundError:
            raise Exception("SYSTEM ERROR: FFmpeg is still not recognized. Please move the ffmpeg.exe to C:\\ffmpeg\\bin\\")
        except Exception as e:
            raise Exception(f"Transcription Error: {str(e)}")