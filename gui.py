import os
import os.path
os.environ["PATH"] += os.pathsep + r'C:\ffmpeg\bin'

import customtkinter as ctk
from tkinter import filedialog, messagebox
from main import UniversalConverter
from core.recorder import record_live_audio
from converters.transcribe_conv import TranscribeConverter
from PIL import Image as PILImage
import threading

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class PolyConvertPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.app_logic = UniversalConverter()
        self.title("PolyConvert Pro AI")
        self.geometry("1200x700")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="POLYCONVERT AI", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        self.btn_conv = ctk.CTkButton(self.sidebar, text="📁 File Converter", fg_color="transparent", anchor="w")
        self.btn_conv.pack(pady=5, padx=10, fill="x")

        self.btn_listen = ctk.CTkButton(self.sidebar, text="🎤 Live Dictation", fg_color="#e67e22", hover_color="#d35400", anchor="w", command=self.start_live_listening)
        self.btn_listen.pack(pady=5, padx=10, fill="x")

        ctk.CTkLabel(self.sidebar, text="ADVANCED OPTIONS", font=ctk.CTkFont(size=12, weight="bold"), text_color="gray").pack(pady=(30, 10))
        
        self.check_optimize = ctk.CTkCheckBox(self.sidebar, text="Optimize for Web")
        self.check_optimize.pack(pady=5, padx=20, anchor="w")

        self.check_watermark = ctk.CTkCheckBox(self.sidebar, text="Add Watermark")
        self.check_watermark.pack(pady=5, padx=20, anchor="w")

        self.check_cloud = ctk.CTkCheckBox(self.sidebar, text="Cloud Upload")
        self.check_cloud.pack(pady=5, padx=20, anchor="w")

        self.appearance_menu = ctk.CTkOptionMenu(self.sidebar, values=["Dark", "Light"], command=ctk.set_appearance_mode)
        self.appearance_menu.pack(side="bottom", pady=20, padx=20)

        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

        self.title_label = ctk.CTkLabel(self.main_frame, text="Ready to transform your files?", font=ctk.CTkFont(size=26, weight="bold"))
        self.title_label.pack(pady=(0, 20), anchor="w")

        self.drop_frame = ctk.CTkFrame(self.main_frame, height=200, border_width=2, border_color="gray30")
        self.drop_frame.pack(fill="x", pady=10)
        self.drop_frame.pack_propagate(False)

        self.file_btn = ctk.CTkButton(self.drop_frame, text="Select Source File", command=self.select_file, width=160, height=40)
        self.file_btn.place(relx=0.5, rely=0.4, anchor="center")

        self.file_info_label = ctk.CTkLabel(self.drop_frame, text="or drag and drop here", text_color="gray50")
        self.file_info_label.place(relx=0.5, rely=0.65, anchor="center")

        self.action_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.action_container.pack(pady=40, fill="x")

        self.ext_entry = ctk.CTkEntry(self.action_container, placeholder_text="Target Format (e.g. pdf, mp3, docx)", width=450, height=50, justify="center", font=ctk.CTkFont(size=14))
        self.ext_entry.pack(pady=(0, 20))

        self.convert_btn = ctk.CTkButton(self.action_container, text="CONVERT NOW", command=self.start_conversion_thread, width=450, height=55, fg_color="#1a73e8", hover_color="#1557b0", font=ctk.CTkFont(size=16, weight="bold"))
        self.convert_btn.pack()

        self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=450)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(10, 10))

        self.status_label = ctk.CTkLabel(self.main_frame, text="System Idle", text_color="gray50")
        self.status_label.pack()

        self.preview_frame = ctk.CTkFrame(self, width=350)
        self.preview_frame.grid(row=0, column=2, padx=(0, 20), pady=20, sticky="nsew")
        self.preview_frame.grid_propagate(False)
        
        ctk.CTkLabel(self.preview_frame, text="FILE PREVIEW", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=15)
        
        self.preview_text = ctk.CTkTextbox(self.preview_frame, fg_color="transparent", wrap="word", font=("Courier New", 12))
        self.preview_text.pack(expand=True, fill="both", padx=15, pady=(0, 15))
        
        self.preview_image_display = ctk.CTkLabel(self.preview_frame, text="")

        self.selected_path = None

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_path = file_path
            self.file_info_label.configure(text=f"Selected: {os.path.basename(file_path)}", text_color="#1a73e8")
            self.update_preview(file_path)

    def update_preview(self, path):
        ext = path.split('.')[-1].lower()
        self.preview_text.delete("1.0", "end")
        self.preview_image_display.configure(image=None, text="")

        try:
            if ext in ['png', 'jpg', 'jpeg', 'webp', 'bmp']:
                self.preview_text.pack_forget()
                self.preview_image_display.pack(expand=True, fill="both")
                
                img = PILImage.open(path)
                img.thumbnail((300, 300))
                ctk_img = ctk.CTkImage(light_image=img, size=(280, 280))
                self.preview_image_display.configure(image=ctk_img, text="")
            elif ext in ['txt', 'py', 'csv', 'json', 'js', 'html', 'md']:
                self.preview_image_display.pack_forget()
                self.preview_text.pack(expand=True, fill="both", padx=15, pady=(0, 15))
                
                with open(path, 'r', errors='ignore') as f:
                    content = f.read(2000)
                self.preview_text.insert("0.0", content)
            else:
                self.preview_text.pack(expand=True, fill="both")
                self.preview_text.insert("0.0", f"Preview not available for .{ext} files.")
        except Exception as e:
            self.preview_text.insert("0.0", "Error generating preview.")

    def start_live_listening(self):
        def task():
            try:
                self.status_label.configure(text="🎙️ Adjusting mic... speak clearly", text_color="#f1c40f")
                temp_audio = record_live_audio()
                self.status_label.configure(text="🧠 AI Transcribing...", text_color="#3498db")
                output_txt = f"output/dictation_{os.path.basename(temp_audio)}.txt"
                TranscribeConverter().convert(temp_audio, output_txt)
                if os.path.exists(temp_audio):
                    os.remove(temp_audio)
                self.status_label.configure(text="✅ Transcription Complete", text_color="#2ecc71")
                self.update_preview(output_txt)
                messagebox.showinfo("Success", "Dictation saved to output folder.")
            except Exception as e:
                self.status_label.configure(text="❌ Mic Error", text_color="red")
                messagebox.showerror("Error", str(e))

        threading.Thread(target=task).start()

    def start_conversion_thread(self):
        target = self.ext_entry.get().strip().lower()
        if not self.selected_path or not target:
            messagebox.showwarning("Error", "Please select a file and specify a target format.")
            return
        
        self.convert_btn.configure(state="disabled")
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()
        self.status_label.configure(text="⚙️ Processing conversion...", text_color="#f1c40f")
        
        threading.Thread(target=self.run_conversion, args=(target,)).start()

    def run_conversion(self, target):
        try:
            self.app_logic.run(self.selected_path, target)
            self.after(0, self.on_success)
        except Exception as e:
            self.after(0, lambda: self.on_error(str(e)))

    def on_success(self):
        self.progress_bar.stop()
        self.progress_bar.configure(mode="determinate")
        self.progress_bar.set(1)
        self.convert_btn.configure(state="normal")
        self.status_label.configure(text="✅ Conversion Successful", text_color="#2ecc71")
        messagebox.showinfo("Success", "Conversion finished successfully!")

    def on_error(self, err):
        self.progress_bar.stop()
        self.progress_bar.configure(mode="determinate")
        self.progress_bar.set(0)
        self.convert_btn.configure(state="normal")
        self.status_label.configure(text="❌ Conversion Failed", text_color="red")
        messagebox.showerror("Error", err)

if __name__ == "__main__":
    app = PolyConvertPro()
    app.mainloop()