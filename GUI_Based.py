import os
import tkinter as tk
from tkinter import filedialog
import PyInstaller.__main__

class PyToExeConverter:
    def __init__(self, master):
        self.master = master
        master.title("PyToExe Converter")

        # create label to display selected file path
        self.file_path_label = tk.Label(master, text="No file selected.")
        self.file_path_label.pack()

        # create "Browse" button to select file
        self.browse_button = tk.Button(master, text="Browse", command=self.select_file)
        self.browse_button.pack()

        # create "Convert to .exe" button
        self.convert_button = tk.Button(master, text="Convert to .exe", command=self.convert_to_exe)
        self.convert_button.pack()

    def select_file(self):
        # open a file dialog to select a .py file
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        self.file_path_label.config(text=file_path)

    def convert_to_exe(self):
        # get the path of the selected .py file
        py_file_path = self.file_path_label.cget("text")

        # open a file dialog to select the output directory and executable name
        output_dir = filedialog.askdirectory()
        executable_name = filedialog.asksaveasfilename(defaultextension='.exe')

        # use PyInstaller to create the executable file
        PyInstaller.__main__.run([
            '--name={}'.format(executable_name),
            '--onefile',
            '--windowed',
            py_file_path
        ])

        # move the output executable to the output directory
        os.makedirs(output_dir, exist_ok=True)
        os.replace('dist/{}'.format(os.path.basename(executable_name)), '{}/{}'.format(output_dir, os.path.basename(executable_name)))

        # clean up the PyInstaller build directory
        os.system('rmdir /s /q build')

        # show message box with success message
        tk.messagebox.showinfo("Conversion Complete", "The file has been converted to an executable.")

root = tk.Tk()
converter = PyToExeConverter(root)
root.mainloop()
