import os
import shutil
import subprocess

def check_dependency(command):
    """
    Checks if a system command (like 'ffmpeg' or 'tesseract') is installed 
    and accessible in the system's PATH.
    """
    return shutil.which(command) is not None

def ensure_dir(directory):
    """
    Creates a directory if it doesn't already exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_safe_output_path(input_path, target_ext, output_folder="output"):
    """
    Generates a clean path for the converted file.
    Example: 'notes.txt' -> 'output/converted_notes.pdf'
    """
    ensure_dir(output_folder)
    
    # Get the file name without extension
    base_name = os.path.basename(input_path)
    file_stem = os.path.splitext(base_name)[0]
    
    # Construct new file name
    new_filename = f"converted_{file_stem}.{target_ext}"
    return os.path.join(output_folder, new_filename)

def get_system_info():
    """
    Helpful for debugging. Returns which tools are missing.
    """
    dependencies = {
        "ffmpeg": check_dependency("ffmpeg"),
        "tesseract": check_dependency("tesseract")
    }
    return dependencies