from PIL import Image, ImageDraw, ImageFont
from .base import BaseConverter

class ImageConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        supported = ['jpg', 'jpeg', 'png', 'webp', 'bmp']
        return source_ext in supported and target_ext in supported

    def convert(self, input_path, output_path, optimize=True, watermark_text=None):
        with Image.open(input_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            if watermark_text:
                draw = ImageDraw.Draw(img)
                draw.text((10, 10), watermark_text, fill=(255, 255, 255))

            img.save(output_path, optimize=optimize, quality=85)
        return True