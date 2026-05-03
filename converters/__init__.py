from core.registry import registry
from .image_conv import ImageConverter
from .data_conv import DataConverter
from .document_conv import DocumentConverter

# Automatically register all plugins when this package is imported
registry.register(ImageConverter())
registry.register(DataConverter())
registry.register(DocumentConverter())