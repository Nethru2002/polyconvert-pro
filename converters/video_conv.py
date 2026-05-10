import ffmpeg
from .base import BaseConverter

class VideoConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        vids = ['mp4', 'avi', 'mov', 'mkv']
        auds = ['mp3', 'wav']
        return source_ext in vids and (target_ext in vids or target_ext in auds)

    def convert(self, input_path, output_path):
        try:
            stream = ffmpeg.input(input_path)
            stream = ffmpeg.output(stream, output_path)
            ffmpeg.run(stream, overwrite_output=True, quiet=True)
            return True
        except Exception as e:
            print(f"Video Error: {e}")
            return False