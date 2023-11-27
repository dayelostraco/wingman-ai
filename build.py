import os
import subprocess
from pathlib import Path
import shutil

cmd = [
    "pyinstaller",
    "main.py",  # your main file with ui.run()
    "--name",
    "WingmanAI",  # name of your app
    # "--onefile",
    #'--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
    "--noconfirm",
    "--hidden-import",
    "edge_tts",
    "--hidden-import",
    "whisper",
    "--add-data",
    f"services{os.pathsep}services",
    "--add-data",
    f"wingmen{os.pathsep}wingmen",
    "--add-data",
    f"audio_samples{os.pathsep}audio_samples",
]
subprocess.call(cmd)

shutil.copy2("config.example.yaml", "dist/WingmanAI/config.yaml")
