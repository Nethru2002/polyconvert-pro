import os
import subprocess

path_to_add = r'C:\ffmpeg\bin'

if os.path.exists(os.path.join(path_to_add, "ffmpeg.exe")):
    print("✅ Found FFmpeg at C:\\ffmpeg\\bin")
    cmd = f'setx /M PATH "%PATH%;{path_to_add}"'
    print("🚀 Attempting to fix System Path permanently...")
    try:
        subprocess.run(f'powershell -Command "Start-Process cmd -ArgumentList \'/c {cmd}\' -Verb RunAs"', shell=True)
        print("✅ SUCCESS: Restart your laptop now, then run gui.py.")
    except Exception as e:
        print(f"❌ Failed: {e}")
else:
    print("❌ ERROR: Could not find ffmpeg.exe at C:\\ffmpeg\\bin. Did you extract it there?")