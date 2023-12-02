from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': [
        "pynput.keyboard._win32",
        "pynput.mouse._win32",
    ],
    'includes': [
        "assets",
    ],
    'include_files': [
        "LICENSE",
    ],
}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'WingmanAI')
]

setup(name='WingmanAI',
      version = '1.0',
      description = 'A wingman AI',
      options = {'build_exe': build_options},
      executables = executables)

# cxfreeze main.py --target-dir dist --packages=pynput.keyboard._win32,pynput.mouse._win32 --includes=assets --include-files=LICENSE