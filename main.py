import os
import tkinter as tk
from tkinter import Checkbutton, IntVar
from PIL import Image, ImageTk
import requests
import subprocess
import programs
import time


# Downloader function
def download_app(application):
    print(f"{application.name}...")
    path = f"{programs.installer_path}\\{application.name}Setup.exe"
    try:
        response = requests.get(application.url)
        response.raise_for_status()  # Check for HTTP errors

        with open(path, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded {application.name} successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")


# Installer function
def install_app(application):
    print(f"{application.name}...")
    path = f"{programs.installer_path}\\{application.name}Setup.exe"
    cmd = [path] + application.flags
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p.wait()
        print(f"Installed {application.name} successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {application.name}: {e}")
    except FileNotFoundError:
        print(f"Installer not found at path: {path}")


# Click handler function
def bttn_click():
    if chrome_invar.get() == 1:
        programs_to_install.append(programs.chrome)

    if opera_invar.get() == 1:
        programs_to_install.append(programs.opera)

    if iobitu_invar.get() == 1:
        programs_to_install.append(programs.iobit_uninstaller)

    if asystemcare_invar.get() == 1:
        programs_to_install.append(programs.advanced_systemcare)

    if avast_invar.get() == 1:
        programs_to_install.append(programs.avast)

    if winrar_invar.get() == 1:
        programs_to_install.append(programs.winrar)

    if daemon_invar.get() == 1:
        programs_to_install.append(programs.daemon_tools)

    if qbit_invar.get() == 1:
        programs_to_install.append(programs.qbittorrent)

    if java_invar.get() == 1:
        programs_to_install.append(programs.java)

    if teams_invar.get() == 1:
        programs_to_install.append(programs.teams)

    if dc_invar.get() == 1:
        programs_to_install.append(programs.discord)

    if steam_invar.get() == 1:
        programs_to_install.append(programs.steam)

    if teamviewer_invar.get() == 1:
        programs_to_install.append(programs.teamviewer)

    os.mkdir(programs.installer_path)
    print("Created directory where installers will be stored!")

    print("Downloading Programs...")
    for program in programs_to_install:
        download_app(program)

    print("Installing programs...")
    for program in programs_to_install:
        install_app(program)

    print("Everything is installed!")
    time.sleep(2)
    print("Removing installers...")

    print("Done!")


# List for programs that will be installed
programs_to_install = []

# Main app window
root = tk.Tk()
root.title("Installer")
root.resizable(False, False)

# Text
choose_label = tk.Label(root, text="Please choose")
choose_label.grid(row=0, column=0, padx=2, pady=2, columnspan=2)

# region Chrome
# Load image
chrome_image = Image.open(".\\Resources\\chrome.png")
chrome_image = chrome_image.resize((20, 20))
chrome_photo = ImageTk.PhotoImage(chrome_image)

# Display image
chrome_image_label = tk.Label(root, image=chrome_photo)
chrome_image_label.grid(row=1, column=0, padx=2, pady=2)

# Checkbox
chrome_invar = IntVar()
chrome_checkbox = Checkbutton(root, text="Google Chrome", variable=chrome_invar)
chrome_checkbox.grid(row=1, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Opera
# Load image
opera_image = Image.open(".\\Resources\\opera.png")
opera_image = opera_image.resize((20, 20))
opera_photo = ImageTk.PhotoImage(opera_image)

# Display image
opera_image_label = tk.Label(root, image=opera_photo)
opera_image_label.grid(row=2, column=0, padx=2, pady=2)

# Checkbox
opera_invar = IntVar()
opera_checkbox = Checkbutton(root, text="Opera", variable=opera_invar)
opera_checkbox.grid(row=2, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Iobit Uninstaller
# Load image
iobitu_image = Image.open(".\\Resources\\iobit-uninstaller.png")
iobitu_image = iobitu_image.resize((20, 20))
iobitu_photo = ImageTk.PhotoImage(iobitu_image)

# Display image
iobitu_image_label = tk.Label(root, image=iobitu_photo)
iobitu_image_label.grid(row=3, column=0, padx=2, pady=2)

# Checkbox
iobitu_invar = IntVar()
iobitu_checkbox = Checkbutton(root, text="Iobit Uninstaller", variable=iobitu_invar)
iobitu_checkbox.grid(row=3, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Advanced Systemcare
# Load image
asystemcare_image = Image.open(".\\Resources\\advenced-systemcare.png")
asystemcare_image = asystemcare_image.resize((20, 20))
asystemcare_photo = ImageTk.PhotoImage(asystemcare_image)

# Display image
asystemcare_image_label = tk.Label(root, image=asystemcare_photo)
asystemcare_image_label.grid(row=4, column=0, padx=2, pady=2)

# Checkbox
asystemcare_invar = IntVar()
asystemcare_checkbox = Checkbutton(root, text="Advanced Systemcare", variable=asystemcare_invar)
asystemcare_checkbox.grid(row=4, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Avast
# Load image
avast_image = Image.open(".\\Resources\\avast.png")
avast_image = avast_image.resize((20, 20))
avast_photo = ImageTk.PhotoImage(avast_image)

# Display image
avast_image_label = tk.Label(root, image=avast_photo)
avast_image_label.grid(row=5, column=0, padx=2, pady=2)

# Checkbox
avast_invar = IntVar()
avast_checkbox = Checkbutton(root, text="Avast", variable=avast_invar)
avast_checkbox.grid(row=5, column=1, padx=2, pady=2, sticky="w")
# endregion

# region WinRar
winrar_image = Image.open(".\\Resources\\winrar.png")
winrar_image = winrar_image.resize((20, 20))
winrar_photo = ImageTk.PhotoImage(winrar_image)

# Display image
winrar_image_label = tk.Label(root, image=winrar_photo)
winrar_image_label.grid(row=6, column=0, padx=2, pady=2)

# Checkbox
winrar_invar = IntVar()
winrar_checkbox = Checkbutton(root, text="WinRar", variable=winrar_invar)
winrar_checkbox.grid(row=6, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Daemon Tools
daemon_image = Image.open(".\\Resources\\daemon-tools.png")
daemon_image = daemon_image.resize((20, 20))
daemon_photo = ImageTk.PhotoImage(daemon_image)

# Display image
daemon_image_label = tk.Label(root, image=daemon_photo)
daemon_image_label.grid(row=7, column=0, padx=2, pady=2)

# Checkbox
daemon_invar = IntVar()
daemon_checkbox = Checkbutton(root, text="Daemon Tools", variable=daemon_invar)
daemon_checkbox.grid(row=7, column=1, padx=2, pady=2, sticky="w")
# endregion

# region qBittorent
qbit_image = Image.open(".\\Resources\\qbittorrent.png")
qbit_image = qbit_image.resize((20, 20))
qbit_photo = ImageTk.PhotoImage(qbit_image)

# Display image
qbit_image_label = tk.Label(root, image=qbit_photo)
qbit_image_label.grid(row=8, column=0, padx=2, pady=2)

# Checkbox
qbit_invar = IntVar()
qbit_checkbox = Checkbutton(root, text="qBittorrtent", variable=qbit_invar)
qbit_checkbox.grid(row=8, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Java
java_image = Image.open(".\\Resources\\java.png")
java_image = java_image.resize((20, 20))
java_photo = ImageTk.PhotoImage(java_image)

# Display image
java_image_label = tk.Label(root, image=java_photo)
java_image_label.grid(row=9, column=0, padx=2, pady=2)

# Checkbox
java_invar = IntVar()
java_checkbox = Checkbutton(root, text="Java", variable=java_invar)
java_checkbox.grid(row=9, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Teams
teams_image = Image.open(".\\Resources\\teams.png")
teams_image = teams_image.resize((20, 20))
teams_photo = ImageTk.PhotoImage(teams_image)

# Display image
teams_image_label = tk.Label(root, image=teams_photo)
teams_image_label.grid(row=10, column=0, padx=2, pady=2)

# Checkbox
teams_invar = IntVar()
teams_checkbox = Checkbutton(root, text="Teams", variable=teams_invar)
teams_checkbox.grid(row=10, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Discord
dc_image = Image.open(".\\Resources\\discord.png")
dc_image = dc_image.resize((20, 20))
dc_photo = ImageTk.PhotoImage(dc_image)

# Display image
dc_image_label = tk.Label(root, image=dc_photo)
dc_image_label.grid(row=11, column=0, padx=2, pady=2)

# Checkbox
dc_invar = IntVar()
dc_checkbox = Checkbutton(root, text="Discord", variable=dc_invar)
dc_checkbox.grid(row=11, column=1, padx=2, pady=2, sticky="w")
# endregion

# region Steam
steam_image = Image.open(".\\Resources\\steam.png")
steam_image = steam_image.resize((20, 20))
steam_photo = ImageTk.PhotoImage(steam_image)

# Display image
steam_image_label = tk.Label(root, image=steam_photo)
steam_image_label.grid(row=12, column=0, padx=2, pady=2)

# Checkbox
steam_invar = IntVar()
steam_checkbox = Checkbutton(root, text="Steam", variable=steam_invar)
steam_checkbox.grid(row=12, column=1, padx=2, pady=2, sticky="w")
# endregion

# region TeamViewer
teamviewer_image = Image.open(".\\Resources\\teamviewer.png")
teamviewer_image = teamviewer_image.resize((20, 20))
teamviewer_photo = ImageTk.PhotoImage(teamviewer_image)

# Display image
teamviewer_image_label = tk.Label(root, image=teamviewer_photo)
teamviewer_image_label.grid(row=13, column=0, padx=2, pady=2)

# Checkbox
teamviewer_invar = IntVar()
teamviewer_checkbox = Checkbutton(root, text="TeamViewer", variable=teamviewer_invar)
teamviewer_checkbox.grid(row=13, column=1, padx=2, pady=2, sticky="w")
# endregion

# Button
button = tk.Button(root, text="Install", command=bttn_click)
button.grid(row=14, column=0, padx=2, pady=2, columnspan=2)

# Main
if __name__ == '__main__':
    root.mainloop()
