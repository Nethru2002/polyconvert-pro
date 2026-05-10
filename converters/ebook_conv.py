import pypandoc
from .base import BaseConverter

class EbookConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        formats = ['epub', 'mobi', 'pdf', 'docx', 'html']
        return source_ext in formats and target_ext in formats

    def convert(self, input_path, output_path):
        pypandoc.convert_file(input_path, output_path.split('.')[-1], outputfile=output_path)
        return True