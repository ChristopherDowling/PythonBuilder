import os
import sys
import subprocess
import shutil

for arg in sys.argv[1:]:
    print(arg)
    if not arg.endswith('.py'): # Exit if a zip file wan't specified as an argument
        print('Error: Please choose a .py file to compile')
        sys.exit()

file = arg
path = arg.split(".py")[0]

if os.path.isdir(path):
    shutil.rmtree(path)
os.mkdir(path)

os.system('pyinstaller "' + file + '" --distpath "' + path + '" -y -F')

shutil.rmtree("./build")
shutil.rmtree("./__pycache__")
os.remove('"./' + path + '.spec')

input("Press Enter to exit")