import hashlib
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import datetime

# Function to calculate SHA-256 hash
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:  # Open in binary mode for any file type
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Save hash to a .hash file
def save_hash(file_path, hash_value):
    with open(file_path + ".hash", "w") as f:
        f.write(hash_value)

# Log results
def log_result(file_path, result):
    with open("integrity_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {file_path} - {result}\n")

# Check file integrity
def check_integrity(file_path):
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "Invalid file path!")
        return

    current_hash = calculate_hash(file_path)

    try:
        with open(file_path + ".hash", "r") as f:
            saved_hash = f.read()
    except FileNotFoundError:
        save_hash(file_path, current_hash)
        messagebox.showinfo("Hash Saved", f"No hash found for:\n{file_path}\nHash saved for future checks.")
        log_result(file_path, "Hash saved (initial)")
        return

    if current_hash == saved_hash:
        messagebox.showinfo("Integrity", f"File is intact:\n{file_path}")
        log_result(file_path, "File OK")
    else:
        messagebox.showwarning("Integrity ", f"File has been modified:\n{file_path}")
        log_result(file_path, "Modified!")

# Browse files (any type)
def browse_files():
    file_paths = filedialog.askopenfilenames(
        title="Select files",
        filetypes=[("All files", "*.*")]
    )
    for path in file_paths:
        check_integrity(path)

# GUI Setup
root = tk.Tk()
root.title("Universal File Integrity Checker")
root.geometry("500x420")
root.configure(bg="#eef4fa")

# Set icon (optional)
try:
    root.iconbitmap("icon.ico")
except:
    pass

# Logo (optional)
try:
    logo = PhotoImage(file="logo.png")
    logo_label = tk.Label(root, image=logo, bg="#eef4fa")
    logo_label.pack(pady=10)
except:
    pass

# Title
title = tk.Label(root, text="Universal File Integrity Checker", font=("Helvetica", 16, "bold"), bg="#eef4fa")
title.pack(pady=5)

# Instructions
desc = tk.Label(root, text="Select one or more files (any type) to check integrity.", font=("Helvetica", 11), bg="#eef4fa")
desc.pack(pady=5)

# Browse button
browse_btn = tk.Button(root, text="Select Files", command=browse_files, font=("Helvetica", 12), bg="#0078D7", fg="white", padx=12, pady=6)
browse_btn.pack(pady=20)

# Footer
footer = tk.Label(root, text="Created by python libraries", font=("Helvetica", 10), fg="gray", bg="#eef4fa")
footer.pack(side="bottom", pady=10)

root.mainloop()
