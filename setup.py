from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': [
        "pynput.keyboard._win32",
        "pynput.mouse._win32",
        "sounddevice",
        "soundfile",
        "exceptions",
        "elevenlabs",
        "openai",
        "edge_tts",
        "pydub",
        "scipy",
        "pedalboard",
        "pydirectinput",
    ],
    "excludes": [
        "services",
        "wingmen",
    ],
    'includes': [
        "assets",
        "audio_samples",
    ],
    'include_files': [
        "LICENSE",
        "services",
        "wingmen",
        "configs",
    ],
}

import sys
# base = 'Win32GUI' if sys.platform=='win32' else None
base = 'console'

executables = [
    Executable('main.py', base=base, target_name='WingmanAI', icon='./assets/icons/wingman-ai.png',)
]

setup(name='WingmanAI',
      version = '1.0',
      description = 'A wingman AI',
      options = {'build_exe': build_options},
      executables = executables)

# cxfreeze main.py --target-dir dist --packages=pynput.keyboard._win32,pynput.mouse._win32 --includes=assets --include-files=LICENSE