import customtkinter as ctk
from tkinter import filedialog, messagebox
from main import UniversalConverter
import os
import threading # Added for background processing

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class PolyConvertGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.app_logic = UniversalConverter()
        
        self.title("PolyConvert Pro")
        self.geometry("900x550")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="POLYCONVERT", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light"], command=self.change_appearance)
        self.appearance_menu.grid(row=6, column=0, padx=20, pady=(200, 20))

        # --- Main Container ---
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")
        
        self.title_label = ctk.CTkLabel(self.main_container, text="Universal Converter", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(0, 30), anchor="w")

        # Drop Zone Appearance
        self.drop_frame = ctk.CTkFrame(self.main_container, height=150, border_width=2, border_color="gray30")
        self.drop_frame.pack(fill="x", pady=10)
        self.drop_frame.pack_propagate(False)

        self.file_btn = ctk.CTkButton(self.drop_frame, text="Select File", command=self.select_file)
        self.file_btn.place(relx=0.5, rely=0.4, anchor="center")

        self.file_info_label = ctk.CTkLabel(self.drop_frame, text="No file selected", text_color="gray50")
        self.file_info_label.place(relx=0.5, rely=0.7, anchor="center")

        # Input Area
        self.ext_entry = ctk.CTkEntry(self.main_container, placeholder_text="Target Format (e.g., pdf, mp4, png)", width=400, height=45)
        self.ext_entry.pack(pady=20)

        self.convert_btn = ctk.CTkButton(self.main_container, text="Convert Now", command=self.start_conversion_thread, height=45, fg_color="#1a73e8")
        self.convert_btn.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self.main_container, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=20)

        self.status_label = ctk.CTkLabel(self.main_container, text="Ready", text_color="gray")
        self.status_label.pack()

        self.selected_path = None

    def change_appearance(self, new_appearance):
        ctk.set_appearance_mode(new_appearance)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_path = file_path
            self.file_info_label.configure(text=f"Selected: {os.path.basename(file_path)}", text_color="#1a73e8")

    def start_conversion_thread(self):
        """This launches the conversion in the background so the UI doesn't freeze"""
        target_ext = self.ext_entry.get().strip().replace(".", "").lower()

        if not self.selected_path or not target_ext:
            messagebox.showwarning("Error", "Please select a file and enter a target format.")
            return

        # Start UI feedback
        self.convert_btn.configure(state="disabled")
        self.status_label.configure(text="⚙️ Processing... Please wait.", text_color="#f1c40f")
        self.progress_bar.configure(mode="indeterminate")
        self.progress_bar.start()

        # Run the actual conversion in a separate thread
        thread = threading.Thread(target=self.run_logic, args=(self.selected_path, target_ext))
        thread.start()

    def run_logic(self, path, ext):
        try:
            # We call the logic from main.py
            self.app_logic.run(path, ext)
            
            # After finishing, update the UI back on the main thread
            self.after(0, self.on_conversion_success)
        except Exception as e:
            self.after(0, lambda: self.on_conversion_error(str(e)))

    def on_conversion_success(self):
        self.progress_bar.stop()
        self.progress_bar.configure(mode="determinate")
        self.progress_bar.set(1)
        self.convert_btn.configure(state="normal")
        self.status_label.configure(text="✅ Success! Check output folder.", text_color="#2ecc71")
        messagebox.showinfo("Done", "File converted successfully!")

    def on_conversion_error(self, err):
        self.progress_bar.stop()
        self.convert_btn.configure(state="normal")
        self.status_label.configure(text="❌ Conversion Failed", text_color="#e74c3c")
        messagebox.showerror("Error", f"Conversion failed: {err}")

if __name__ == "__main__":
    gui = PolyConvertGUI()
    gui.mainloop()