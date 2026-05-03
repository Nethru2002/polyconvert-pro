from fpdf import FPDF
from .base import BaseConverter

class DocumentConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        # We handle text to PDF conversion here
        return source_ext == 'txt' and target_ext == 'pdf'

    def convert(self, input_path, output_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        with open(input_path, "r", encoding="utf-8") as f:
            for line in f:
                pdf.cell(200, 10, txt=line, ln=True)
        
        pdf.output(output_path)
        return True