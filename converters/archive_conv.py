import shutil
import py7zr
import os
from .base import BaseConverter

class ArchiveConverter(BaseConverter):
    def can_handle(self, source_ext, target_ext):
        archives = ['zip', '7z', 'tar', 'gz']
        # Handle compression or extraction
        return source_ext in archives or target_ext in archives

    def convert(self, input_path, output_path):
        source_ext = input_path.split('.')[-1].lower()
        target_ext = output_path.split('.')[-1].lower()

        # CASE: COMPRESSING (e.g., txt -> zip)
        if target_ext in ['zip', 'tar', 'gz'] and source_ext not in ['zip', '7z', 'tar']:
            shutil.make_archive(output_path.replace(f'.{target_ext}', ''), target_ext, os.path.dirname(input_path), os.path.basename(input_path))
        
        elif target_ext == '7z':
            with py7zr.SevenZipFile(output_path, 'w') as archive:
                archive.write(input_path, os.path.basename(input_path))

        # CASE: EXTRACTING (e.g., zip -> folder)
        elif source_ext == 'zip':
            shutil.unpack_archive(input_path, output_path.replace('.zip', ''))
            
        return True