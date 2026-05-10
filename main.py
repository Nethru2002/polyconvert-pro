import os
import sys
from core.identifier import identify_file
from core.registry import registry
from core.utils import ensure_dir
import converters

class UniversalConverter:
    def __init__(self):
        pass

    def run(self, input_file, target_ext):
        aliases = {
            "word": "docx",
            "excel": "xlsx",
            "powerpoint": "pptx",
            "text": "txt",
            "image": "jpg",
            "audio": "mp3",
            "video": "mp4",
            "3d": "obj"
        }

        target_ext = target_ext.lower().replace(".", "").strip()
        if target_ext in aliases:
            target_ext = aliases[target_ext]

        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.")
            return

        file_info = identify_file(input_file)
        if not file_info:
            print("Error: Could not identify file type.")
            return

        source_ext = file_info['ext']
        
        output_folder = "output"
        ensure_dir(output_folder)
        
        filename_only = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(output_folder, f"converted_{filename_only}.{target_ext}")

        converter = registry.get_converter(source_ext, target_ext)
        
        if converter:
            try:
                success = converter.convert(input_file, output_file)
                if success:
                    print(f"Success: {output_file}")
                    return True
                else:
                    print("Error: Conversion failed.")
                    return False
            except Exception as e:
                print(f"Critical Error: {e}")
                return False
        else:
            print(f"Error: No plugin found to convert .{source_ext} to .{target_ext}")
            return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <file_path> <target_extension>")
    else:
        app = UniversalConverter()
        app.run(sys.argv[1], sys.argv[2])