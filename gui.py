import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import threading
from PIL import Image as PILImage
from main import UniversalConverter
from core.recorder import record_live_audio
from converters.transcribe_conv import TranscribeConverter

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class PolyConvertStudio(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.app_logic = UniversalConverter()
        self.title("PolyConvert Studio Pro")
        self.geometry("1150x700")

        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(self.sidebar, text="POLYCONVERT", font=("Arial", 22, "bold")).pack(pady=30)

        self.nav_mic = ctk.CTkButton(self.sidebar, text="🎤 Live Dictation", fg_color="#e67e22", hover_color="#d35400", anchor="w", height=40, command=self.start_live_listening)
        self.nav_mic.pack(pady=5, padx=20, fill="x")

        ctk.CTkLabel(self.sidebar, text="APPEARANCE", font=("Arial", 12, "bold"), text_color="gray50").pack(pady=(40, 10))
        self.mode_switch = ctk.CTkOptionMenu(self.sidebar, values=["Dark", "Light"], command=ctk.set_appearance_mode)
        self.mode_switch.pack(pady=10, padx=20)
        
        ctk.CTkLabel(self.sidebar, text="Developed by Nethru & Hiruni", font=("Arial", 10), text_color="gray40").pack(side="bottom", pady=20)

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(side="left", fill="both", expand=True, padx=30, pady=30)

        self.step1_label = ctk.CTkLabel(self.container, text="1. Pick your file", font=("Arial", 18, "bold"))
        self.step1_label.pack(anchor="w", pady=(0, 10))

        self.drop_zone = ctk.CTkFrame(self.container, height=180, border_width=2, border_color="#3498db")
        self.drop_zone.pack(fill="x", pady=(0, 30))
        self.drop_zone.pack_propagate(False)

        self.select_btn = ctk.CTkButton(self.drop_zone, text="Choose File", command=self.select_file, width=140, height=40)
        self.select_btn.place(relx=0.5, rely=0.4, anchor="center")

        self.file_display = ctk.CTkLabel(self.drop_zone, text="Click to browse your computer", text_color="gray60")
        self.file_display.place(relx=0.5, rely=0.65, anchor="center")

        self.step2_label = ctk.CTkLabel(self.container, text="2. Choose target format", font=("Arial", 18, "bold"))
        self.step2_label.pack(anchor="w")

        self.suggestion_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.suggestion_frame.pack(fill="x", pady=10)
        
        self.suggestion_info = ctk.CTkLabel(self.suggestion_frame, text="Select a file to see smart suggestions.", text_color="gray50")
        self.suggestion_info.pack(pady=20)

        self.manual_entry = ctk.CTkEntry(self.container, placeholder_text="Or type format manually...", width=450, height=45, justify="center")
        
        self.convert_btn = ctk.CTkButton(self.container, text="CONVERT NOW", state="disabled", command=self.start_thread, height=55, font=("Arial", 16, "bold"), fg_color="#1a73e8")
        self.convert_btn.pack(side="bottom", fill="x", pady=20)

        self.status_bar = ctk.CTkLabel(self.container, text="System Ready", text_color="gray50")
        self.status_bar.pack(side="bottom")

        self.preview_panel = ctk.CTkFrame(self, width=320)
        self.preview_panel.pack(side="right", fill="y", padx=20, pady=20)
        self.preview_panel.pack_propagate(False)
        
        ctk.CTkLabel(self.preview_panel, text="FILE PREVIEW", font=("Arial", 12, "bold")).pack(pady=20)
        self.preview_box = ctk.CTkTextbox(self.preview_panel, fg_color="transparent", wrap="word", font=("Courier New", 12))
        self.preview_box.pack(expand=True, fill="both", padx=10, pady=10)

        self.target_format = None
        self.selected_path = None

    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.selected_path = path
            ext = path.split('.')[-1].lower()
            self.file_display.configure(text=f"📄 {os.path.basename(path)}", text_color="#3498db")
            self.show_suggestions(ext)
            self.update_preview(path)

    def show_suggestions(self, ext):
        for widget in self.suggestion_frame.winfo_children():
            widget.destroy()

        options = []
        if ext in ['png', 'jpg', 'jpeg', 'webp']:
            options = [("To JPG", "jpg"), ("To PNG", "png"), ("To WebP", "webp")]
        elif ext == 'pdf':
            options = [("To Word", "docx"), ("To Text", "txt")]
        elif ext == 'docx':
            options = [("To PDF", "pdf"), ("To HTML", "html")]
        elif ext == 'txt':
            options = [("To Word", "docx"), ("To PDF", "pdf")]
        elif ext in ['csv', 'xlsx']:
            options = [("To Excel", "xlsx"), ("To CSV", "csv"), ("To JSON", "json")]
        elif ext in ['mp4', 'mov', 'wav', 'mp3']:
            options = [("Extract MP3", "mp3"), ("To MP4", "mp4"), ("To Text", "txt")]

        if options:
            btn_container = ctk.CTkFrame(self.suggestion_frame, fg_color="transparent")
            btn_container.pack(fill="x")
            for label, fmt in options:
                btn = ctk.CTkButton(btn_container, text=label, width=120, height=35, fg_color="gray30", 
                                    command=lambda f=fmt: self.set_format(f))
                btn.pack(side="left", padx=5)
            self.manual_entry.pack(pady=10, anchor="w")
        else:
            self.manual_entry.pack(pady=20, fill="x")

    def set_format(self, fmt):
        self.target_format = fmt
        self.convert_btn.configure(state="normal", text=f"CONVERT TO {fmt.upper()}")
        self.status_bar.configure(text=f"Format set to: {fmt}")

    def update_preview(self, path):
        self.preview_box.delete("1.0", "end")
        try:
            with open(path, 'r', errors='ignore') as f:
                self.preview_box.insert("0.0", f.read(2000))
        except:
            self.preview_box.insert("0.0", "Preview not available.")

    def start_thread(self):
        fmt = self.target_format if self.target_format else self.manual_entry.get().strip()
        if not fmt: return
        self.convert_btn.configure(state="disabled", text="PROCESSING...")
        self.status_bar.configure(text="⚙️ Converting... please wait.")
        threading.Thread(target=self.run_conv, args=(fmt,)).start()

    def run_conv(self, fmt):
        try:
            self.app_logic.run(self.selected_path, fmt)
            self.after(0, lambda: messagebox.showinfo("Success", "Finished! Check the 'output' folder."))
            self.after(0, lambda: self.status_bar.configure(text="✅ Conversion Successful", text_color="#2ecc71"))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Error", str(e)))
        self.after(0, lambda: self.convert_btn.configure(state="normal", text="CONVERT NOW"))

    def start_live_listening(self):
        def task():
            try:
                self.status_bar.configure(text="🎙️ Adjusting mic... speak now", text_color="#f1c40f")
                temp_audio = record_live_audio()
                self.status_bar.configure(text="🧠 AI Transcribing...", text_color="#3498db")
                output_txt = f"output/dictation_{os.path.basename(temp_audio)}.txt"
                TranscribeConverter().convert(temp_audio, output_txt)
                os.remove(temp_audio)
                self.after(0, lambda: self.update_preview(output_txt))
                self.after(0, lambda: messagebox.showinfo("Success", "Voice saved to output folder."))
                self.after(0, lambda: self.status_bar.configure(text="✅ Transcription Complete", text_color="#2ecc71"))
            except Exception as e:
                self.after(0, lambda: self.status_bar.configure(text="❌ Mic Error", text_color="red"))
                self.after(0, lambda: messagebox.showerror("Error", str(e)))

        threading.Thread(target=task).start()

if __name__ == "__main__":
    app = PolyConvertStudio()
    app.mainloop()