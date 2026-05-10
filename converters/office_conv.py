import os
import mammoth
from docx import Document
from docx2pdf import convert as word_to_pdf
from pdf2docx import Converter as PDFToWordConverter
from .base import BaseConverter

class OfficeConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        # Word to PDF or HTML
        if source_ext == 'docx' and target_ext in ['pdf', 'html']:
            return True
        # PDF to Word
        if source_ext == 'pdf' and target_ext == 'docx':
            return True
        # TEXT to Word (The new feature)
        if source_ext == 'txt' and target_ext == 'docx':
            return True
        return False

    def convert(self, input_path, output_path):
        source_ext = input_path.split('.')[-1].lower()
        target_ext = output_path.split('.')[-1].lower()

        # Handle TXT to DOCX
        if source_ext == 'txt' and target_ext == 'docx':
            doc = Document()
            with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    doc.add_paragraph(line.strip())
            doc.save(output_path)
            return True

        # Handle DOCX to PDF
        elif source_ext == 'docx' and target_ext == 'pdf':
            word_to_pdf(input_path, output_path)
            return True
        
        # Handle DOCX to HTML
        elif source_ext == 'docx' and target_ext == 'html':
            with open(input_path, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                with open(output_path, "w", encoding="utf-8") as html_file:
                    html_file.write(result.value)
            return True

        # Handle PDF to DOCX
        elif source_ext == 'pdf' and target_ext == 'docx':
            cv = PDFToWordConverter(input_path)
            cv.convert(output_path)
            cv.close()
            return True
            
        return False