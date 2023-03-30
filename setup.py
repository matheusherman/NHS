import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os",  "boto3",  "google", "PIL", "googleapiclient", "s3transfer", "csv"],
                     "includes": ["tkinter"],
                     "include_files": ["credentials.json", "NHS.png", "token.json", "pucpr.png"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Teste Online",
    version = 1.0,
    description = "teste",
    options={"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, icon="NHS.ico")]
)