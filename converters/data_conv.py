import pandas as pd
import json
from .base import BaseConverter

class DataConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        supported = ['csv', 'xlsx', 'json']
        return source_ext in supported and target_ext in supported

    def convert(self, input_path, output_path):
        source_ext = input_path.split('.')[-1].lower()
        target_ext = output_path.split('.')[-1].lower()

        # Load Data
        if source_ext == 'csv':
            df = pd.read_csv(input_path)
        elif source_ext == 'xlsx':
            df = pd.read_excel(input_path)
        elif source_ext == 'json':
            df = pd.read_json(input_path)

        # Save Data
        if target_ext == 'csv':
            df.to_csv(output_path, index=False)
        elif target_ext == 'xlsx':
            df.to_excel(output_path, index=False)
        elif target_ext == 'json':
            df.to_json(output_path, indent=4)
        
        return True