***

# 🚀 PolyConvert Pro AI
**The Ultimate Universal File Intelligence & Conversion Suite**

PolyConvert Pro AI is a modular, high-performance desktop application designed to identify, preview, and convert over 50+ file formats. Built with a **Plugin-Based Architecture**, it integrates local AI for speech-to-text, OCR for image-to-data, 3D modeling support, and professional-grade multimedia engines.

![Version](https://img.shields.io/badge/version-3.5.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)
![AI](https://img.shields.io/badge/AI-Whisper-orange.svg)
![Developers](https://img.shields.io/badge/Developed%20By-Nethru%20%26%20Hiruni-blueviolet)

---

## 👥 Developed By
This project was designed and developed by:
*   **Nethru Randev Wickramasekara**
*   **Hiruni Hapuarachchi**

---

## ✨ Key Features

### 🧠 Intelligence & AI
-   **🎤 Live Dictation:** Real-time voice-to-text capture using OpenAI’s Whisper AI with auto-punctuation.
-   **🧠 AI Transcription:** Local processing of audio/video files into clean text transcripts.
-   **🔍 Deep Identification:** Uses "Magic Bytes" (MIME) to detect file types even if the extension is missing or wrong.
-   **👁️ OCR Engine:** Extracts editable text from images (JPG, PNG) and scanned PDF documents.

### 🔄 Multi-Format Conversions
-   **📁 Office Suite:** High-fidelity conversion between **Word (.docx)**, **PDF**, **HTML**, and **TXT**.
-   **🖼️ Image Studio:** Professional format shifting and web optimization for PNG, JPG, WEBP, and BMP.
-   **📐 3D Engineering:** Convert between STL, OBJ, PLY, and GLB formats for 3D printing and design.
-   **📦 Archive Suite:** Create or extract ZIP and 7Z archives with high compression ratios.
-   **📚 E-Book Studio:** Transition between EPUB, MOBI, and PDF formats for digital reading.
-   **📊 Data Engine:** Seamlessly move data between **Excel (XLSX)**, **CSV**, and **JSON**.

### 🎨 User Experience
-   **SaaS-Style GUI:** A modern, dark-themed sidebar interface built with `CustomTkinter`.
-   **Live Preview Panel:** Instantly view images or read code/text/CSV data before you hit convert.
-   **Threaded Execution:** Background processing ensures the UI never freezes during heavy AI tasks.

---

## 📂 Project Structure

```text
UNIVERSAL_CONVERTER/
├── converters/           # Plugin Architecture family
│   ├── __init__.py       # Auto-registers all conversion plugins
│   ├── archive_conv.py   # ZIP, 7Z, TAR, GZ logic
│   ├── base.py           # Abstract Base Class for plugins
│   ├── data_conv.py      # CSV, XLSX, JSON logic
│   ├── document_conv.py  # TXT to PDF logic
│   ├── ebook_conv.py     # EPUB, MOBI, PDF logic
│   ├── image_conv.py     # PNG, JPG, WEBP, BMP logic
│   ├── ocr_conv.py       # Image-to-Text (Tesseract) engine
│   ├── office_conv.py    # Word, PDF, HTML, TXT engine
│   ├── three_d_conv.py   # OBJ, STL, PLY, GLB engine
│   ├── transcribe_conv.py# AI Speech-to-Text (Whisper) engine
│   └── video_conv.py     # MP4, AVI, MOV, MP3 engine
├── core/                 # System Internals
│   ├── __init__.py       # Package initialization
│   ├── identifier.py     # File Type Identification (MIME)
│   ├── recorder.py       # Microphone & Audio Capture logic
│   ├── registry.py       # Plugin Manager & Lookups
│   └── utils.py          # Path helpers & folder management
├── output/               # Default folder for converted files
├── debug_app.py          # System Diagnostic & Health Check tool
├── Dockerfile            # Config for containerized deployment
├── fix_windows_path.py   # Utility to fix Windows PATH permanently
├── gui.py                # Main Modern Sidebar Graphical Interface
├── install_ffmpeg.py     # Automated FFmpeg system installer
├── main.py               # Logic Controller & Extension Alias Mapper
├── README.md             # Project Documentation
└── requirements.txt      # Python library dependencies
```

---

## 🛠️ Setup & Installation

### 1. Python Environment
Install all required Python libraries via pip:
```bash
pip install -r requirements.txt
```

### 2. Automated FFmpeg Setup (Crucial for AI/Video)
To avoid `WinError 2`, use the built-in automated installer. It will download and configure FFmpeg for you:
```bash
python install_ffmpeg.py
```
After the script finishes, run the path fixer and **restart VS Code**:
```bash
python fix_windows_path.py
```

### 3. Tesseract OCR Setup
To enable Image-to-Text (OCR):
1. Download [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki).
2. Install it to `C:\Program Files\Tesseract-OCR`.

### 4. Verify System Health
Run the diagnostic tool to ensure all 10+ plugins and system tools are ready:
```bash
python debug_app.py
```

---

## 🚀 How to Use

### Desktop Graphical Interface
Launch the modern suite:
```bash
python gui.py
```

### Command Line Interface
```bash
python main.py <input_file> <target_extension>
```
*Note: You can use friendly names in the extension field like `word`, `excel`, `image`, or `audio`.*

---

## 🔒 Privacy & Performance
- **100% Local:** No files are uploaded to the cloud. All AI transcription and OCR happen on your local hardware.
- **Auto-Model Download:** On the first use of AI Transcription, the app will download the Whisper model (approx. 142MB). This is a one-time process.

---

## 📜 License
Distributed under the MIT License. 

Developed with ❤️ by **Nethru Randev Wickramasekara** and **Hiruni Hapuarachchi**.