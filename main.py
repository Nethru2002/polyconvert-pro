import os
import sys
from core.identifier import identify_file
from core.registry import registry
import converters  # This triggers the registration in converters/__init__.py

class UniversalConverter:
    def run(self, input_file, target_ext):
        # 1. Identify File
        file_info = identify_file(input_file)
        if not file_info:
            print("❌ File not found.")
            return

        source_ext = file_info['ext']
        output_file = f"output/converted_{os.path.basename(input_file).split('.')[0]}.{target_ext}"
        
        if not os.path.exists('output'):
            os.makedirs('output')

        # 2. Ask the Registry for a converter
        converter = registry.get_converter(source_ext, target_ext)
        
        if converter:
            print(f"🚀 Converting: {source_ext} ➔ {target_ext}")
            try:
                converter.convert(input_file, output_file)
                print(f"✅ Success! Saved to: {output_file}")
            except Exception as e:
                print(f"❌ Error during conversion: {e}")
        else:
            print(f"⚠️ Error: No plugin found to convert .{source_ext} to .{target_ext}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <file_path> <target_extension>")
    else:
        app = UniversalConverter()
        app.run(sys.argv[1], sys.argv[2])