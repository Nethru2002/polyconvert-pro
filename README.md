***

# 🚀 PolyConvert Pro AI
**The Ultimate Universal File Intelligence & Conversion Suite**

PolyConvert Pro AI is a modular, high-performance desktop application designed to identify, preview, and convert over 50+ file formats. Built with a **Plugin-Based Architecture**, it integrates local AI for speech-to-text, OCR for image-to-data, 3D modeling support, and professional-grade multimedia engines.

![Version](https://img.shields.io/badge/version-3.5.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)
![AI](https://img.shields.io/badge/AI-Whisper-orange.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

---

## ✨ Key Features

### 🧠 Intelligence & AI
- **🎤 Live Dictation:** Real-time voice-to-text capture using OpenAI’s Whisper AI with auto-punctuation.
- **🧠 AI Transcription:** Local processing of audio/video files into clean text transcripts.
- **🔍 Deep Identification:** Uses "Magic Bytes" (MIME) to detect file types regardless of the extension.
- **👁️ OCR Engine:** Extracts editable text from images and scanned PDF documents.

### 🔄 Multi-Format Conversions
- **📁 Office Suite:** High-fidelity conversion between **Word (.docx)**, **PDF**, **HTML**, and **TXT**.
- **🖼️ Image Studio:** Professional format shifting and web optimization for PNG, JPG, WEBP, and BMP.
- **📐 3D Engineering:** Convert between STL, OBJ, PLY, and GLB formats for 3D printing and design.
- **📦 Archive Suite:** Create or extract ZIP and 7Z archives.
- **📚 E-Book Studio:** Transition between EPUB, MOBI, and PDF formats.
- **📊 Data Engine:** Seamlessly move data between **Excel (XLSX)**, **CSV**, and **JSON**.

### 🎨 User Experience
- **SaaS-Style GUI:** A modern, dark-themed sidebar interface built with `CustomTkinter`.
- **Live Preview Panel:** Instantly view images or read code/text/CSV data before conversion.
- **Threaded Execution:** Background processing ensures the UI remains responsive during heavy tasks.

---

## 📂 Project Structure

```text
UNIVERSAL_CONVERTER/
├── converters/           # Plugin Architecture
├── core/                 # System Internals (Identifier, Recorder, Registry)
├── output/               # Default folder for converted files
├── debug_app.py          # System Diagnostic tool
├── Dockerfile            # Container config
├── fix_windows_path.py   # PATH environment utility
├── gui.py                # Main Graphical Interface
├── install_ffmpeg.py     # Automated FFmpeg installer
├── main.py               # CLI & Logic Controller
├── README.md             # Project Documentation
└── requirements.txt      # Python dependencies
```

---

## 🛠️ Setup & Installation

### 1. Python Environment
Install all required Python libraries via pip:
```bash
pip install -r requirements.txt
```

### 2. Automated FFmpeg Setup
To enable AI and Video features, run the built-in automated installer:
```bash
python install_ffmpeg.py
```
After success, run the path fixer and **restart your IDE**:
```bash
python fix_windows_path.py
```

### 3. Tesseract OCR Setup
To enable Image-to-Text (OCR):
1. Download [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki).
2. Install to `C:\Program Files\Tesseract-OCR`.

---

## 🚀 How to Use

### Desktop Graphical Interface
Launch the suite:
```bash
python gui.py
```

### Command Line Interface
```bash
python main.py <input_file> <target_extension>
```
*Note: Friendly names like `word`, `excel`, or `audio` are supported.*

---

## 🔒 Privacy & Performance
- **100% Local:** No files are uploaded to the cloud. All processing happens on your local hardware.
- **Offline AI:** After the initial download of the Whisper model (approx. 142MB), all AI features work entirely offline.

---

## 📜 Credits
Developed by **Nethru Randev Wickramasekara** and **Hiruni Hapuarachchi**.

## ⚖️ License
Distributed under the MIT License.