from PIL import Image
from .base import BaseConverter

class ImageConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        supported = ['jpg', 'jpeg', 'png', 'webp', 'bmp']
        return source_ext in supported and target_ext in supported

    def convert(self, input_path, output_path):
        with Image.open(input_path) as img:
            # Convert to RGB if saving as JPG (to handle transparency)
            if output_path.endswith('.jpg') or output_path.endswith('.jpeg'):
                img = img.convert('RGB')
            img.save(output_path)
        return True