import os
import urllib.request
import zipfile
import shutil

def install():
    target_dir = r"C:\ffmpeg"
    bin_dir = os.path.join(target_dir, "bin")
    zip_path = "ffmpeg.zip"
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

    print("🚀 Starting Auto-Installation of FFmpeg...")

    # 1. Create directory
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 2. Download
    print("📥 Downloading FFmpeg (this may take a minute)...")
    urllib.request.urlretrieve(url, zip_path)

    # 3. Extract
    print("📦 Extracting files...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("temp_ffmpeg")

    # 4. Find the bin folder inside the extracted files and move it
    print("🚚 Organizing folders...")
    for root, dirs, files in os.walk("temp_ffmpeg"):
        if "bin" in dirs:
            source_bin = os.path.join(root, "bin")
            if os.path.exists(bin_dir):
                shutil.rmtree(bin_dir)
            shutil.move(source_bin, bin_dir)
            break

    # 5. Cleanup
    os.remove(zip_path)
    shutil.rmtree("temp_ffmpeg")

    if os.path.exists(os.path.join(bin_dir, "ffmpeg.exe")):
        print(f"✅ SUCCESS! FFmpeg is now at: {os.path.join(bin_dir, 'ffmpeg.exe')}")
        print("👉 NOW: Restart VS Code and run gui.py")
    else:
        print("❌ Installation failed. Please check your internet connection.")

if __name__ == "__main__":
    install()