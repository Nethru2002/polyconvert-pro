import pytesseract
from PIL import Image
from .base import BaseConverter

class OCRConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        return source_ext in ['png', 'jpg', 'pdf'] and target_ext == 'txt'

    def convert(self, input_path, output_path):
        text = pytesseract.image_to_string(Image.open(input_path))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return True