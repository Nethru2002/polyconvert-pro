import customtkinter as ctk
from tkinter import filedialog, messagebox
from main import UniversalConverter
import os

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

        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="POLYCONVERT", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.convert_tab = ctk.CTkButton(self.sidebar_frame, text="Converter", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.convert_tab.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.appearance_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance:", anchor="w")
        self.appearance_label.grid(row=5, column=0, padx=20, pady=(200, 0))
        self.appearance_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance)
        self.appearance_menu.grid(row=6, column=0, padx=20, pady=(10, 20))

        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")
        
        self.title_label = ctk.CTkLabel(self.main_container, text="Ready to transform your files?", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(0, 5), anchor="w")
        
        self.desc_label = ctk.CTkLabel(self.main_container, text="Select a file and specify your target format below.", text_color="gray60")
        self.desc_label.pack(pady=(0, 30), anchor="w")

        self.drop_frame = ctk.CTkFrame(self.main_container, height=200, border_width=2, border_color="gray30")
        self.drop_frame.pack(fill="x", pady=10)
        self.drop_frame.pack_propagate(False)

        self.file_btn = ctk.CTkButton(self.drop_frame, text="Select File", command=self.select_file, width=150, height=35)
        self.file_btn.place(relx=0.5, rely=0.4, anchor="center")

        self.file_info_label = ctk.CTkLabel(self.drop_frame, text="or drag and drop here", text_color="gray50")
        self.file_info_label.place(relx=0.5, rely=0.6, anchor="center")

        self.config_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.config_frame.pack(fill="x", pady=30)

        self.ext_entry = ctk.CTkEntry(self.config_frame, placeholder_text="Target Format (e.g. pdf, mp3)", width=350, height=45)
        self.ext_entry.pack(side="left", padx=(0, 20))

        self.convert_btn = ctk.CTkButton(self.config_frame, text="Convert Now", command=self.start_conversion, width=150, height=45, fg_color="#1a73e8", hover_color="#1557b0", font=ctk.CTkFont(weight="bold"))
        self.convert_btn.pack(side="left")

        self.progress_bar = ctk.CTkProgressBar(self.main_container, width=500)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10, anchor="w")

        self.status_label = ctk.CTkLabel(self.main_container, text="System Idle", text_color="gray50", font=ctk.CTkFont(size=12))
        self.status_label.pack(anchor="w")

        self.selected_path = None

    def change_appearance(self, new_appearance):
        ctk.set_appearance_mode(new_appearance)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_path = file_path
            filename = os.path.basename(file_path)
            self.file_info_label.configure(text=f"Selected: {filename}", text_color="#1a73e8")
            self.status_label.configure(text="File verified and loaded.")

    def start_conversion(self):
        target_ext = self.ext_entry.get().strip().replace(".", "").lower()

        if not self.selected_path:
            messagebox.showwarning("Missing File", "Please select a file to continue.")
            return
        
        if not target_ext:
            messagebox.showwarning("Target Format", "Specify the format you want to convert to.")
            return

        self.status_label.configure(text="Processing conversion...", text_color="#f1c40f")
        self.progress_bar.set(0.4)
        self.update_idletasks()

        try:
            self.app_logic.run(self.selected_path, target_ext)
            self.progress_bar.set(1.0)
            self.status_label.configure(text="Conversion Successful", text_color="#2ecc71")
            messagebox.showinfo("Complete", "Conversion finished. Check the output folder.")
        except Exception as e:
            self.progress_bar.set(0)
            self.status_label.configure(text="Process Failed", text_color="#e74c3c")
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    gui = PolyConvertGUI()
    gui.mainloop()