***

# 🚀 PolyConvert Pro AI
**The Ultimate Universal File Intelligence & Conversion Suite**

PolyConvert Pro AI is a high-performance, plugin-based desktop application designed to identify, preview, and convert virtually any file format. Equipped with local AI for speech-to-text and a professional modern interface, it serves as an all-in-one "Swiss Army Knife" for digital assets.

![Version](https://img.shields.io/badge/version-3.5.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)
![AI](https://img.shields.io/badge/AI-Whisper-orange.svg)

---

## ✨ Key Features

### 🧠 AI & Intelligence
- **Local AI Transcription:** Convert Audio/Video into text using OpenAI’s Whisper model (100% offline after first run).
- **🎤 Live Dictation:** Real-time voice-to-text capture using your microphone with auto-punctuation.
- **Smart MIME Detection:** Identifies files by their "Magic Bytes," not just their extension.
- **OCR Engine:** Extract editable text from images and scanned PDFs.

### 🔄 Advanced Conversions
- **Office Suite:** High-fidelity conversion between **Word (.docx)**, **PDF**, **HTML**, and **TXT**.
- **3D Modeling:** Convert engineering/design files (OBJ, STL, PLY, GLB).
- **Multimedia:** Format shifting for Video/Audio and audio extraction (MP4 to MP3).
- **Data Engine:** Seamlessly move data between **Excel**, **CSV**, and **JSON**.
- **Archives:** Compress files into **ZIP** or **7Z** or extract existing archives.

### 🎨 User Experience
- **SaaS-Style GUI:** A modern, dark-themed sidebar interface built with `CustomTkinter`.
- **Live Preview Panel:** Instantly view images or read the first 1000 characters of code/text before converting.
- **Threaded Execution:** Conversion runs in the background to prevent UI freezing.

---

## 🛠️ System Dependencies

To unlock the full power of the "Pro" engines, the following external tools must be installed on your operating system:

| Tool | Purpose | Status |
| :--- | :--- | :--- |
| **FFmpeg** | Video/Audio & AI Transcription | Required for Media |
| **Tesseract OCR** | Image-to-Text conversion | Required for OCR |
| **Pandoc** | E-book and advanced document logic | Optional |
| **MS Word** | Best results for Word ➔ PDF | Optional |

---

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nethru2002/polyconvert-pro.git
   cd polyconvert-pro-ai
   ```

2. **Install Python Libraries:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Major libraries: `customtkinter`, `openai-whisper`, `trimesh`, `pandas`, `python-docx`, `pdf2docx`, `pillow`, `ffmpeg-python`)*

3. **Check System PATH:**
   Ensure `ffmpeg` and `tesseract` are accessible from your terminal.

---

## 🖥️ Usage

### Desktop Application
Launch the full Graphical User Interface:
```bash
python gui.py
```

### Command Line
For quick terminal-based conversion:
```bash
python main.py <path_to_file> <target_extension>
```
*Aliases supported: `word`, `excel`, `image`, `audio`.*

---

## 📂 Supported Formats (Summary)

| Category | Formats |
| :--- | :--- |
| **Images** | JPG, PNG, WEBP, BMP |
| **Documents** | DOCX, PDF, TXT, HTML |
| **Data** | CSV, XLSX, JSON |
| **3D Models** | OBJ, STL, PLY, GLB, OFF |
| **Archives** | ZIP, 7Z, TAR, GZ |
| **Audio/Video** | MP4, AVI, MOV, MP3, WAV, M4A |

---

## 👩‍💻 Project Architecture
The software follows a **Modular Plugin Registry** pattern:
- **`core/`**: The engine (Identifier, Registry, Recorder).
- **`converters/`**: Independent plugins for each format family.
- **`gui.py`**: The interface layer.
- **`main.py`**: The logical controller.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🤝 Contributing
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/NewConverter`).
3. Commit your Changes.
4. Push to the Branch.
5. Open a Pull Request.

---
*Developed for the next generation of file management.*