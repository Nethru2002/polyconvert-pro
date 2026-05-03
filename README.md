***

# Universal File Converter

This is a modular, plugin-based Python tool designed to identify any file type and convert it into a different format. Unlike basic converters that rely on file extensions, PolyConvert uses **Magic Bytes (MIME detection)** to identify the true nature of a file before processing.

The project is built with a **Plugin Architecture**, allowing developers to add support for new file types (Video, Audio, 3D models, etc.) without modifying the core logic.

## 🚀 Features

-   **Deep Identification:** Uses `libmagic` to identify files even if they have no extension.
-   **Plugin-Based:** Easily extendable. Want to support Video? Just drop a new script into the `converters/` folder.
-   **Automatic Output Management:** Creates an `output/` directory automatically and renames converted files cleanly.
-   **Multi-Category Support:** Handles Images, Data (CSV/Excel/JSON), and Documents (TXT to PDF) out of the box.

---

## 📂 Project Structure

```text
universal_converter/
├── main.py                # Entry point (CLI)
├── core/
│   ├── identifier.py      # MIME-type detection logic
│   └── registry.py        # Plugin management system
├── converters/
│   ├── base.py            # Abstract Base Class for plugins
│   ├── image_conv.py      # Image processing (JPG, PNG, WebP)
│   ├── data_conv.py       # Spreadsheet processing (CSV, XLSX, JSON)
│   └── document_conv.py   # Document processing (TXT to PDF)
├── output/                # All converted files are saved here
└── requirements.txt       # Python dependencies
```

---

## 🛠️ Prerequisites

### 1. System Dependencies
The identification engine requires `libmagic`.

-   **Windows:** Automatically handled by `python-magic-bin` (see Installation).
-   **macOS:** `brew install libmagic`
-   **Linux:** `sudo apt-get install libmagic1`

### 2. Python
-   Python 3.8 or higher.

---

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Nethru2002/polyconvert.git
    cd universal_converter
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *If you don't have a requirements file yet, run:*
    `pip install python-magic python-magic-bin pillow pandas openpyxl fpdf`

---

## 🖥️ Usage

Run the tool via the command line by providing the **source file** and the **target extension**.

**General Syntax:**
```bash
python main.py <file_path> <target_extension>
```

### Examples:

**Convert Image (PNG to JPG):**
```bash
python main.py travel_photo.png jpg
```

**Convert Data (CSV to Excel):**
```bash
python main.py database.csv xlsx
```

**Convert Text to PDF:**
```bash
python main.py report.txt pdf
```

---

## 🛠️ Supported Conversions (Current)

| Category | Formats |
| :--- | :--- |
| **Images** | PNG, JPG, JPEG, WEBP, BMP |
| **Data** | CSV, XLSX (Excel), JSON |
| **Documents** | TXT to PDF |

---

## 👩‍💻 For Developers: Adding New Converters

Adding support for a new category (e.g., Audio) is simple:

1.  Create a new file in `converters/your_type_conv.py`.
2.  Inherit from `BaseConverter`.
3.  Implement `can_handle` and `convert`.
4.  Register it in `converters/__init__.py`.

```python
# Example for a hypothetical Audio Converter
class AudioConverter(BaseConverter):
    def can_handle(self, source, target):
        return source in ['wav', 'mp3'] and target in ['wav', 'mp3']

    def convert(self, input_path, output_path):
        # Your conversion logic here
        pass
```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🤝 Contributing
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewConverter`)
3. Commit your Changes (`git commit -m 'Add support for GIF to MP4'`)
4. Push to the Branch (`git push origin feature/NewConverter`)
5. Open a Pull Request

---
*Developed with ❤️ for the open-source community.*