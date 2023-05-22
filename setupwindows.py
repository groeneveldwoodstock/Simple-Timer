from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages":["tkinter"], "include_files":["timericon.ico"]}
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

# <The rest of your build script goes here.>

setup(
    name = "Classroom Timer", 
    version = "1.0",
    description="Shapes Game",
    options={"build_exe": build_exe_options},
    executables = [Executable("timer.pyw", base=base, icon = 'timericon.ico', shortcutName = 'Classroom Timer')]
)

