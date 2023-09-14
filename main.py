import os
import tkinter as tk
from tkinter import Checkbutton, IntVar
from PIL import Image
from PIL import ImageTk
import requests
import subprocess
import programs
import time
import signal


# Downloader function
def download_app(application):
    print(f"Downloading {application.name}...")
    try:
        response = requests.get(application.url)
        response.raise_for_status()  # Check for HTTP errors

        with open(application.path, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded {application.name} successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")


# Installer function
def install_app(application):
    try:
        cmd = [application.path] + application.flags
        print(f"Installing {application.name}...")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        p.wait()

    except subprocess.CalledProcessError as e:
        print(f"Error installing {application.name}: {e}")
    except FileNotFoundError:
        print(f"Installer not found at path: {application.path}")


# Click handler function
def bttn_click():
    if chrome_invar.get() == 1:
        programs_to_install.append(programs.chrome)

    if opera_invar.get() == 1:
        programs_to_install.append(programs.opera)

    if iobitu_invar.get() == 1:
        programs_to_install.append(programs.iobit_uninstaller)

    for program in programs_to_install:
        download_app(program)
        install_app(program)

    print("Everything is installed!")
    time.sleep(2)
    print("Removing installers...")

    #for program in programs_to_install:
        #os.remove(program.path)

    print("Done!")

    quit()


# List for programs that will be installed
programs_to_install = []


# Main app window
root = tk.Tk()
root.title("Installer")

# Text
choose_label = tk.Label(root, text="Please choose!")
choose_label.grid(row=0, column=0, padx=2, pady=2, columnspan=2)

# Chrome


# Load image
chrome_image = Image.open(".\\Resources\\chrome.png")  # Replace "example.png" with your image file path
chrome_image = chrome_image.resize((20, 20))  # Resize the image to your desired dimensions
chrome_photo = ImageTk.PhotoImage(chrome_image)

# Display image
chrome_image_label = tk.Label(root, image=chrome_photo)
chrome_image_label.grid(row=1, column=0, padx=2, pady=2)

# Checkbox
chrome_invar = IntVar()
chrome_checkbox = Checkbutton(root, text="Google Chrome", variable=chrome_invar)
chrome_checkbox.grid(row=1, column=1, padx=2, pady=2)

# Opera


# Load image
opera_image = Image.open(".\\Resources\\opera.png")  # Replace "example.png" with your image file path
opera_image = opera_image.resize((20, 20))  # Resize the image to your desired dimensions
opera_photo = ImageTk.PhotoImage(opera_image)

# Display image
opera_image_label = tk.Label(root, image=opera_photo)
opera_image_label.grid(row=2, column=0, padx=2, pady=2)

# Checkbox
opera_invar = IntVar()
opera_checkbox = Checkbutton(root, text="Opera", variable=opera_invar)
opera_checkbox.grid(row=2, column=1, padx=2, pady=2)

# Iobit Uninstaller


# Load image
iobitu_image = Image.open(".\\Resources\\iobit-uninstaller.png")  # Replace "example.png" with your image file path
iobitu_image = iobitu_image.resize((20, 20))  # Resize the image to your desired dimensions
iobitu_photo = ImageTk.PhotoImage(iobitu_image)

# Display image
iobitu_image_label = tk.Label(root, image=iobitu_photo)
iobitu_image_label.grid(row=3, column=0, padx=2, pady=2)

# Checkbox
iobitu_invar = IntVar()
iobitu_checkbox = Checkbutton(root, text="Iobit Uninstaller", variable=iobitu_invar)
iobitu_checkbox.grid(row=3, column=1, padx=2, pady=2)

# Button
button = tk.Button(root, text="Install", command=bttn_click)
button.grid(row=4, column=0, padx=2, pady=2, columnspan=3)

# Main
if __name__ == '__main__':
    root.mainloop()
