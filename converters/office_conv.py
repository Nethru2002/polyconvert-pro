import os
import mammoth
from docx import Document
from docx2pdf import convert as word_to_pdf
from pdf2docx import Converter as PDFToWordConverter
from .base import BaseConverter

class OfficeConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        if source_ext == 'docx' and target_ext in ['pdf', 'html']:
            return True
        if source_ext == 'pdf' and target_ext == 'docx':
            return True
        if source_ext == 'txt' and target_ext == 'docx':
            return True
        return False

    def convert(self, input_path, output_path):
        source_ext = input_path.split('.')[-1].lower()
        target_ext = output_path.split('.')[-1].lower()

        if source_ext == 'txt' and target_ext == 'docx':
            doc = Document()
            with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    doc.add_paragraph(line.strip())
            doc.save(output_path)
            return True

        elif source_ext == 'docx' and target_ext == 'pdf':
            try:
                word_to_pdf(input_path, output_path)
                return True
            except Exception as e:
                print(f"Word to PDF Error: {e}")
                return False
        
        elif source_ext == 'docx' and target_ext == 'html':
            with open(input_path, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                with open(output_path, "w", encoding="utf-8") as html_file:
                    html_file.write(result.value)
            return True

        elif source_ext == 'pdf' and target_ext == 'docx':
            try:
                cv = PDFToWordConverter(input_path)
                cv.convert(output_path)
                cv.close()
                return True
            except Exception as e:
                print(f"PDF to Word Error: {e}")
                return False
            
        return False