import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "sys"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Win32GUI"

setup(  name = "psyanimal",
        version = "0.1",
        description = "psyanimal",
        options = {"build_exe": build_exe_options},
        executables = [Executable("psyanimal.py", base=base, icon="unicorn.ico")])
