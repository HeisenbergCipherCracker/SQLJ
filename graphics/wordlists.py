import tkinter as tk
from tkinter import filedialog

# Create a window
window = tk.Tk()

def open_file_dialog():
    # Open file dialog with initial directory set to the desktop
    file_path = filedialog.askopenfilename(initialdir='~/Desktop', filetypes=[('Text Files', '*.txt')])

    # Read the contents of the selected file
    with open(file_path, 'r') as file:
        contents = file.read()

    # Print the contents of the file
    print(contents)
    return contents

# Create a button to open the file dialog
button = tk.Button(window, text="Select wordlist", command=open_file_dialog)
button.pack()

# Run the application
window.mainloop()