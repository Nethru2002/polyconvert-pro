***

# 🚀 PolyConvert Pro: Universal File Conversion Suite

**PolyConvert Pro** is a high-performance, modular desktop application designed to identify and convert virtually any file type. Built with a **Plugin-Based Architecture**, it combines professional-grade libraries like FFmpeg, Tesseract OCR, and Pandas into a single, sleek, modern interface.

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

---

## ✨ Key Features

-   **🎨 Modern UI:** A professional sidebar-based interface built with `CustomTkinter` featuring Dark/Light mode support.
-   **🔍 Smart Identification:** Uses **Magic Bytes** (MIME detection) to identify files regardless of their extension.
-   **📄 Office Suite:** High-fidelity conversion between **Word (.docx)** and **PDF**.
-   **🖼️ Image Studio:** Convert and compress between PNG, JPG, WebP, and BMP.
-   **📊 Data Engine:** Seamlessly move data between **Excel (XLSX)**, **CSV**, and **JSON**.
-   **🎬 Multimedia:** Extract audio from video (MP4 to MP3) or change video formats (MOV to MP4) using FFmpeg.
-   **👁️ OCR Engine:** Convert scanned images or PDFs into editable **Text (.txt)** files.
-   **⚡ Parallel Processing:** Built to handle batch conversions efficiently.

---

## 📂 Project Structure

```text
universal_converter/
├── main.py                # CLI Entry point & Logic controller
├── gui.py                 # Modern Sidebar Graphical Interface
├── core/
│   ├── identifier.py      # MIME-type detection logic
│   ├── registry.py        # Plugin management & Parallel logic
│   └── utils.py           # System dependency checks & Path helpers
├── converters/
│   ├── base.py            # Abstract Base Class for all plugins
│   ├── image_conv.py      # Image processing
│   ├── data_conv.py       # Spreadsheets & JSON
│   ├── office_conv.py     # Word & PDF (High Fidelity)
│   ├── video_conv.py      # Video & Audio (FFmpeg)
│   └── ocr_conv.py        # Image-to-Text (Tesseract)
└── requirements.txt       # Python dependencies
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Nethru2002/polyconvert-pro.git
cd polyconvert-pro
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install System Requirements (Crucial)
To enable Video and OCR features, you must install these tools on your OS:

| Tool | Windows | macOS | Linux |
| :--- | :--- | :--- | :--- |
| **FFmpeg** | [Download](https://www.gyan.dev/ffmpeg/builds/) & add to PATH | `brew install ffmpeg` | `sudo apt install ffmpeg` |
| **Tesseract** | [Download](https://github.com/UB-Mannheim/tesseract/wiki) | `brew install tesseract` | `sudo apt install tesseract-ocr` |
| **libmagic** | `pip install python-magic-bin` | `brew install libmagic` | `sudo apt install libmagic1` |

---

## 🚀 Usage

### Graphical Interface (Recommended)
Launch the modern desktop suite:
```bash
python gui.py
```

### Command Line Interface
For quick single conversions:
```bash
python main.py <input_file> <target_extension>
```
*Example:* `python main.py resume.pdf docx`

---

## 🛠️ Supported Conversions

| Module | Supported Formats |
| :--- | :--- |
| **Documents** | DOCX ↔ PDF, TXT → PDF |
| **Images** | PNG, JPG, WEBP, BMP (Any to Any) |
| **Data** | CSV, XLSX, JSON (Any to Any) |
| **Video/Audio** | MP4, AVI, MOV, MKV, MP3, WAV |
| **OCR** | JPG, PNG, PDF → Editable TXT |

---

## 👩‍💻 For Developers: Adding Plugins
PolyConvert Pro is designed to be extended. To add a new converter:
1. Create a new file in `converters/`.
2. Inherit from `BaseConverter`.
3. Implement `can_handle()` and `convert()`.
4. Register your class in `converters/__init__.py`.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Contributing
Contributions are welcome! If you have a suggestion for a new converter or a UI improvement, please open an issue or a Pull Request.

---
*Built with ❤️ for a seamless file experience.*