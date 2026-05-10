from core.registry import registry
from .image_conv import ImageConverter
from .data_conv import DataConverter
from .document_conv import DocumentConverter
from .video_conv import VideoConverter
from .ocr_conv import OCRConverter
from .office_conv import OfficeConverter
from .three_d_conv import ThreeDConverter
from .archive_conv import ArchiveConverter
from .transcribe_conv import TranscribeConverter
from .ebook_conv import EbookConverter

registry.register(ImageConverter())
registry.register(DataConverter())
registry.register(DocumentConverter())
registry.register(VideoConverter())
registry.register(OCRConverter())
registry.register(OfficeConverter())
registry.register(ThreeDConverter())
registry.register(ArchiveConverter())
registry.register(TranscribeConverter())
registry.register(EbookConverter())