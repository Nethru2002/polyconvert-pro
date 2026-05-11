import os
from fpdf import FPDF
from .base import BaseConverter

class DocumentConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        return source_ext == 'txt' and target_ext == 'pdf'

    def convert(self, input_path, output_path):
        # We use fpdf2 which supports UTF-8
        pdf = FPDF()
        pdf.add_page()
        
        # Use a built-in font that supports Unicode
        pdf.set_font("helvetica", size=12)
        
        try:
            with open(input_path, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    # 'encode_non_latin1' allows fpdf2 to handle characters outside Latin-1
                    pdf.write(5, line)
            
            pdf.output(output_path)
            return True
        except Exception as e:
            print(f"PDF Error: {e}")
            return False