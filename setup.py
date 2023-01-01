#from sys import platform
from sys import platform
from cx_Freeze import setup, Executable

#tkinter, ttkbootstrap e googletrans
build_exe_options = {"includes": ['tkinter', 'ttkbootstrap', 'googletrans']}

base = None
if platform == 'win32':
    base = 'Win32GUI'


setup(
    nome = 'midnight tradutor',
    version = '0.5',
    description = 'um tradutor usando a propria API do google tradutor sem fins lucrativos!',
    options = {'build_exe': build_exe_options},
    executables =[Executable('main.py', base=base)]
)