import os
import PyInstaller.__main__

# set the path to the .py file you want to convert
py_file_path = 'path/to/your/script.py'

# set the name of the output directory and executable file
output_dir = 'dist'
executable_name = 'my_script.exe'

# use PyInstaller to create the executable file
PyInstaller.__main__.run([
    '--name={}'.format(executable_name),
    '--onefile',
    '--windowed',
    '--icon=icon.ico', # optional: set the path to an icon file
    py_file_path
])

# move the output executable to the output directory
os.makedirs(output_dir, exist_ok=True)
os.replace('dist/{}'.format(executable_name), '{}/{}'.format(output_dir, executable_name))

# clean up the PyInstaller build directory
os.system('rmdir /s /q build')
