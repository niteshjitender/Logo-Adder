import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
# buildOptions = dict(include_files = ['Data/','Photos'],packages = ['os','PIL','cv2','mydecoder','progressbar','time','sys'])
buildOptions = dict(include_files = ['Data/','Photos'])

# GUI applications require a different base on Windows (the default is for a
# console application).
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(  name = "Logo Adder",
        version = "1.0",
        author = "Jitender Singh Chhapola",
        description = "A logo adding utility @Copyright 2020 Jitender!",
        options = dict(build_exe = buildOptions,optimize = 2),
        executables = [Executable("image.py")])