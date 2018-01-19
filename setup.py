import cx_Freeze
import os

executables = [cx_Freeze.Executable("snakeboss.py")]

os.environ['TCL_LIBRARY'] = 'C:\\Users\\eveqi\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Users\\eveqi\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6'

cx_Freeze.setup(
    name = "SnakeBoss",
    options = {"build_exe" :{"packages" : ["pygame"],"include_files":["apple2.png","snakhead3.png"]}},
    description = "Snake Game",
    executables = executables

    )
