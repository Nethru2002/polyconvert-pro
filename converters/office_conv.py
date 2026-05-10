import os
from docx2pdf import convert as word_to_pdf
from pdf2docx import Converter as PDFToWordConverter
from .base import BaseConverter

class OfficeConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        # Handle Word to PDF
        if source_ext == 'docx' and target_ext == 'pdf':
            return True
        # Handle PDF to Word
        if source_ext == 'pdf' and target_ext == 'docx':
            return True
        return False

    def convert(self, input_path, output_path):
        source_ext = input_path.split('.')[-1].lower()
        target_ext = output_path.split('.')[-1].lower()

        if source_ext == 'docx' and target_ext == 'pdf':
            # Note: On Windows/Mac this requires Microsoft Word installed
            word_to_pdf(input_path, output_path)
        
        elif source_ext == 'pdf' and target_ext == 'docx':
            cv = PDFToWordConverter(input_path)
            cv.convert(output_path, start=0, end=None)
            cv.close()
            
        return True