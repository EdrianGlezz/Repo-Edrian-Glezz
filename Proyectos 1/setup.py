"""
A simple setup script to create an executable using PySide2. This also
demonstrates how to use excludes to get minimal package size.
test_pyside2.py is a very simple type of PySide2 application.
Run the build process by running the command 'python setup.py build'
If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the application.
"""

from bisect import bisect
import sys

from cx_Freeze import Executable, setup

base = "Win32GUI" 

executables = [Executable("hola mundo.py", base=base)]

'''
options = {
    "build_exe": {
        # exclude packages that are not really needed
        "excludes": [
            "tkinter",
            "unittest",
            "email",
            "http",
            "xml",
            "pydoc",
        ]
    }
}'''
options = {
    "build_exe": {
        "excludes": [ 
        ],
        'includes': ['images']
    }
}

    
setup(
    name="face",
    version="0.0.1",
    description="",
    options=options,
    executables=executables,
)