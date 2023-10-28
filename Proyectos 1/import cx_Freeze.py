import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"],
    "include_files": ["C:/Users/1281581/OneDrive - Jabil/Documents/Python/Python"]
}

setup(
    name="Main",
    version="1.0",
    description="Jabil program",
    options={"build_exe": build_exe_options},
    executables=[Executable("main1.py")]
)

