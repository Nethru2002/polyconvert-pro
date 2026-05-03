import magic
import os

def identify_file(file_path):
    if not os.path.exists(file_path):
        return None
    
    # Identify MIME type (e.g., 'image/jpeg', 'application/pdf')
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    
    # Get extension
    extension = os.path.splitext(file_path)[1].lower().replace('.', '')
    
    return {
        "mime": file_type,
        "ext": extension
    }