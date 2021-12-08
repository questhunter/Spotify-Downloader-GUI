from tkinter import filedialog

def get_path():  # Gets the download location(path)
    path = filedialog.askdirectory()
    f = open(r"path\path.txt", "w")
    f.write(path)
    f.close()