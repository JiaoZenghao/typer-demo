import PyInstaller.__main__
import sys
import os

def build():
    # Determine the appropriate file extension based on the OS
    ext = '.exe' if sys.platform.startswith('win') else ''
    
    PyInstaller.__main__.run([
        'typer_demo/main.py',
        '--onefile',
        '--name=typer-demo' + ext,
        '--add-data=typer_demo:typer_demo',
        '--exclude-module=pytest',
        '--exclude-module=tests'
    ])

if __name__ == "__main__":
    build()