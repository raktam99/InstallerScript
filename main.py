import os
import tkinter as tk
from tkinter import Checkbutton
from PIL import Image, ImageTk
import requests
import subprocess
import programs


# Downloader function
def download_app(application):
    print(f"{application.name}...")
    path = f"{programs.installer_path}\\{application.name}Setup.exe"

    if not os.path.isfile(path):
        try:
            response = requests.get(application.url, allow_redirects=True)
            response.raise_for_status()  # Check for HTTP errors

            with open(path, 'wb') as f:
                f.write(response.content)

            print(f"Downloaded {application.name} successfully!")
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        print("Already downloaded!")


# Installer function
def install_app(application):
    print(f"{application.name}...")
    path = f"{programs.installer_path}\\{application.name}Setup.exe"
    cmd = [path] + application.flags
    if not installed_programs.__contains__(application):
        try:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            p.wait()
            print(f"Installed {application.name} successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {application.name}: {e}")
        except FileNotFoundError:
            print(f"Installer not found at path: {path}")
    else:
        print("Already installed!")


# Install click handler function
def install_bttn_click():
    if not len(programs_to_install) == 0:
        print("Installing programs...")

        for program in programs_to_install:
            install_app(program)
            installed_programs.append(program)

        print("Everything is installed!")
    else:
        print("Nothing to install!")


# Install click handler function
def download_bttn_click():
    if not os.path.isdir(programs.installer_path):
        os.mkdir(programs.installer_path)
    print("Created directory where installers will be stored!")

    if not len(programs_to_install) == 0:
        print("Downloading Programs...")
        for program in programs_to_install:
            download_app(program)

        print("Downloaded everything!")
    else:
        print("Nothing is selected")


# region Checkbox handlers
def chrome_chckbx_changed():
    if not programs_to_install.__contains__(programs.chrome):
        programs_to_install.append(programs.chrome)
    else:
        programs_to_install.remove(programs.chrome)


def opera_chckbx_changed():
    if not programs_to_install.__contains__(programs.opera):
        programs_to_install.append(programs.opera)
    else:
        programs_to_install.remove(programs.opera)


def iobitu_chckbx_changed():
    if not programs_to_install.__contains__(programs.iobit_uninstaller):
        programs_to_install.append(programs.iobit_uninstaller)
    else:
        programs_to_install.remove(programs.iobit_uninstaller)


def asystemcare_chckbx_changed():
    if not programs_to_install.__contains__(programs.advanced_systemcare):
        programs_to_install.append(programs.advanced_systemcare)
    else:
        programs_to_install.remove(programs.advanced_systemcare)


def avast_chckbx_changed():
    if not programs_to_install.__contains__(programs.avast):
        programs_to_install.append(programs.avast)
    else:
        programs_to_install.remove(programs.avast)


def winrar_chckbx_changed():
    if not programs_to_install.__contains__(programs.winrar):
        programs_to_install.append(programs.winrar)
    else:
        programs_to_install.remove(programs.winrar)


def daemon_chckbx_changed():
    if not programs_to_install.__contains__(programs.daemon_tools):
        programs_to_install.append(programs.daemon_tools)
    else:
        programs_to_install.remove(programs.daemon_tools)


def qbit_chckbx_changed():
    if not programs_to_install.__contains__(programs.qbittorrent):
        programs_to_install.append(programs.qbittorrent)
    else:
        programs_to_install.remove(programs.qbittorrent)


def java_chckbx_changed():
    if not programs_to_install.__contains__(programs.java):
        programs_to_install.append(programs.java)
    else:
        programs_to_install.remove(programs.java)


def teams_chckbx_changed():
    if not programs_to_install.__contains__(programs.teams):
        programs_to_install.append(programs.teams)
    else:
        programs_to_install.remove(programs.teams)


def dc_chckbx_changed():
    if not programs_to_install.__contains__(programs.discord):
        programs_to_install.append(programs.discord)
    else:
        programs_to_install.remove(programs.discord)


def steam_chckbx_changed():
    if not programs_to_install.__contains__(programs.steam):
        programs_to_install.append(programs.steam)
    else:
        programs_to_install.remove(programs.steam)


def teamviewer_chckbx_changed():
    if not programs_to_install.__contains__(programs.teamviewer):
        programs_to_install.append(programs.teamviewer)
    else:
        programs_to_install.remove(programs.teamviewer)


def python_chckbx_changed():
    if not programs_to_install.__contains__(programs.python):
        programs_to_install.append(programs.python)
    else:
        programs_to_install.remove(programs.python)


def dotnet_chckbx_changed():
    if not programs_to_install.__contains__(programs.dotnet):
        programs_to_install.append(programs.dotnet)
    else:
        programs_to_install.remove(programs.dotnet)
# endregion


# Variables
programs_to_install = []
installed_programs = []
installed = False

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
chrome_checkbox = Checkbutton(root, text="Google Chrome")
chrome_checkbox.grid(row=1, column=1, padx=2, pady=2, sticky="w")
chrome_checkbox.bind('<Button-1>', lambda event: chrome_chckbx_changed())
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
opera_checkbox = Checkbutton(root, text="Opera")
opera_checkbox.grid(row=2, column=1, padx=2, pady=2, sticky="w")
opera_checkbox.bind('<Button-1>', lambda event: opera_chckbx_changed())
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
iobitu_checkbox = Checkbutton(root, text="Iobit Uninstaller")
iobitu_checkbox.grid(row=3, column=1, padx=2, pady=2, sticky="w")
iobitu_checkbox.bind('<Button-1>', lambda event: iobitu_chckbx_changed())
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
asystemcare_checkbox = Checkbutton(root, text="Advanced Systemcare")
asystemcare_checkbox.grid(row=4, column=1, padx=2, pady=2, sticky="w")
asystemcare_checkbox.bind('<Button-1>', lambda event: asystemcare_chckbx_changed())
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
avast_checkbox = Checkbutton(root, text="Avast")
avast_checkbox.grid(row=5, column=1, padx=2, pady=2, sticky="w")
avast_checkbox.bind('<Button-1>', lambda event: avast_chckbx_changed())
# endregion

# region WinRar
winrar_image = Image.open(".\\Resources\\winrar.png")
winrar_image = winrar_image.resize((20, 20))
winrar_photo = ImageTk.PhotoImage(winrar_image)

# Display image
winrar_image_label = tk.Label(root, image=winrar_photo)
winrar_image_label.grid(row=6, column=0, padx=2, pady=2)

# Checkbox
winrar_checkbox = Checkbutton(root, text="WinRar")
winrar_checkbox.grid(row=6, column=1, padx=2, pady=2, sticky="w")
winrar_checkbox.bind('<Button-1>', lambda event: winrar_chckbx_changed())
# endregion

# region Daemon Tools
daemon_image = Image.open(".\\Resources\\daemon-tools.png")
daemon_image = daemon_image.resize((20, 20))
daemon_photo = ImageTk.PhotoImage(daemon_image)

# Display image
daemon_image_label = tk.Label(root, image=daemon_photo)
daemon_image_label.grid(row=7, column=0, padx=2, pady=2)

# Checkbox
daemon_checkbox = Checkbutton(root, text="Daemon Tools")
daemon_checkbox.grid(row=7, column=1, padx=2, pady=2, sticky="w")
daemon_checkbox.bind('<Button-1>', lambda event: daemon_chckbx_changed())
# endregion

# region qBittorent
qbit_image = Image.open(".\\Resources\\qbittorrent.png")
qbit_image = qbit_image.resize((20, 20))
qbit_photo = ImageTk.PhotoImage(qbit_image)

# Display image
qbit_image_label = tk.Label(root, image=qbit_photo)
qbit_image_label.grid(row=8, column=0, padx=2, pady=2)

# Checkbox
qbit_checkbox = Checkbutton(root, text="qBittorrtent")
qbit_checkbox.grid(row=8, column=1, padx=2, pady=2, sticky="w")
qbit_checkbox.bind('<Button-1>', lambda event: qbit_chckbx_changed())
# endregion

# region Java
java_image = Image.open(".\\Resources\\java.png")
java_image = java_image.resize((20, 20))
java_photo = ImageTk.PhotoImage(java_image)

# Display image
java_image_label = tk.Label(root, image=java_photo)
java_image_label.grid(row=9, column=0, padx=2, pady=2)

# Checkbox
java_checkbox = Checkbutton(root, text="Java")
java_checkbox.grid(row=9, column=1, padx=2, pady=2, sticky="w")
java_checkbox.bind('<Button-1>', lambda event: java_chckbx_changed())
# endregion

# region Teams
teams_image = Image.open(".\\Resources\\teams.png")
teams_image = teams_image.resize((20, 20))
teams_photo = ImageTk.PhotoImage(teams_image)

# Display image
teams_image_label = tk.Label(root, image=teams_photo)
teams_image_label.grid(row=10, column=0, padx=2, pady=2)

# Checkbox
teams_checkbox = Checkbutton(root, text="Teams")
teams_checkbox.grid(row=10, column=1, padx=2, pady=2, sticky="w")
teams_checkbox.bind('<Button-1>', lambda event: teams_chckbx_changed())
# endregion

# region Discord
dc_image = Image.open(".\\Resources\\discord.png")
dc_image = dc_image.resize((20, 20))
dc_photo = ImageTk.PhotoImage(dc_image)

# Display image
dc_image_label = tk.Label(root, image=dc_photo)
dc_image_label.grid(row=11, column=0, padx=2, pady=2)

# Checkbox
dc_checkbox = Checkbutton(root, text="Discord")
dc_checkbox.grid(row=11, column=1, padx=2, pady=2, sticky="w")
dc_checkbox.bind('<Button-1>', lambda event: dc_chckbx_changed())
# endregion

# region Steam
steam_image = Image.open(".\\Resources\\steam.png")
steam_image = steam_image.resize((20, 20))
steam_photo = ImageTk.PhotoImage(steam_image)

# Display image
steam_image_label = tk.Label(root, image=steam_photo)
steam_image_label.grid(row=12, column=0, padx=2, pady=2)

# Checkbox
steam_checkbox = Checkbutton(root, text="Steam")
steam_checkbox.grid(row=12, column=1, padx=2, pady=2, sticky="w")
steam_checkbox.bind('<Button-1>', lambda event: steam_chckbx_changed())
# endregion

# region TeamViewer
teamviewer_image = Image.open(".\\Resources\\teamviewer.png")
teamviewer_image = teamviewer_image.resize((20, 20))
teamviewer_photo = ImageTk.PhotoImage(teamviewer_image)

# Display image
teamviewer_image_label = tk.Label(root, image=teamviewer_photo)
teamviewer_image_label.grid(row=13, column=0, padx=2, pady=2)

# Checkbox
teamviewer_checkbox = Checkbutton(root, text="TeamViewer")
teamviewer_checkbox.grid(row=13, column=1, padx=2, pady=2, sticky="w")
teamviewer_checkbox.bind('<Button-1>', lambda event: teamviewer_chckbx_changed())
# endregion

# region Python
python_image = Image.open(".\\Resources\\python.png")
python_image = python_image.resize((20, 20))
python_photo = ImageTk.PhotoImage(python_image)

# Display image
python_image_label = tk.Label(root, image=python_photo)
python_image_label.grid(row=14, column=0, padx=2, pady=2)

# Checkbox
python_checkbox = Checkbutton(root, text="Python")
python_checkbox.grid(row=14, column=1, padx=2, pady=2, sticky="w")
python_checkbox.bind('<Button-1>', lambda event: python_chckbx_changed())
# endregion

# region DotNet
dotnet_image = Image.open(".\\Resources\\dotnet.png")
dotnet_image = dotnet_image.resize((20, 20))
dotnet_photo = ImageTk.PhotoImage(dotnet_image)

# Display image
dotnet_image_label = tk.Label(root, image=dotnet_photo)
dotnet_image_label.grid(row=15, column=0, padx=2, pady=2)

# Checkbox
dotnet_checkbox = Checkbutton(root, text=".Net")
dotnet_checkbox.grid(row=15, column=1, padx=2, pady=2, sticky="w")
dotnet_checkbox.bind('<Button-1>', lambda event: dotnet_chckbx_changed())
# endregion

# Install button
install_bttn = tk.Button(root, text="Install", command=install_bttn_click)
install_bttn.grid(row=16, column=0, padx=2, pady=2)

# Download button
download_bttn = tk.Button(root, text="Download", command=download_bttn_click)
download_bttn.grid(row=16, column=1, padx=2, pady=2)

# Main
if __name__ == '__main__':
    root.mainloop()
