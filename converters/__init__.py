from core.registry import registry
from .image_conv import ImageConverter
from .data_conv import DataConverter
from .document_conv import DocumentConverter
from .video_conv import VideoConverter
from .ocr_conv import OCRConverter
from .office_conv import OfficeConverter

# Register all plugins
registry.register(ImageConverter())
registry.register(DataConverter())
registry.register(DocumentConverter())
registry.register(VideoConverter())
registry.register(OCRConverter())
registry.register(OfficeConverter())   