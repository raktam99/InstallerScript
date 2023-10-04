import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import functions as f
import programs


def change_path_bttn_click():
    folder_path = filedialog.askdirectory()
    if folder_path:
        programs.installer_path = folder_path
        download_txtbx_text.set(programs.installer_path)


def on_dowlnoad_txtbx_scrollbar_move(*args):
    download_txtbx.xview(*args)


# Main app window
root = tk.Tk()
root.title("Installer")
root.resizable(False, False)


# region Labels
choose_label = tk.Label(root, text="Please choose")
choose_label.grid(row=0, column=0, columnspan=4)

antiviruses_label = tk.Label(root, text="Antiviruses:")
antiviruses_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(5, 0))

browser_label = tk.Label(root, text="Browsers:")
browser_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=(5, 0))

utilities_label = tk.Label(root, text="Utilities:")
utilities_label.grid(row=5, column=0, columnspan=2, sticky="w", pady=(5, 0))

meeting_label = tk.Label(root, text="Meeting:")
meeting_label.grid(row=7, column=0, columnspan=2, sticky="w", pady=(5, 0))

developer_label = tk.Label(root, text="Developer tools:")
developer_label.grid(row=9, column=0, columnspan=2, sticky="w", pady=(5, 0))

other_label = tk.Label(root, text="Other:")
other_label.grid(row=13, column=0, columnspan=2, sticky="w", pady=(5, 0))

download_path_label = tk.Label(root, text="Folder, where installers will be downloaded:")
download_path_label.grid(row=17, column=0, columnspan=3, sticky="w", pady=(20, 0))
# endregion


# region Avast
# Load image
avast_image = Image.open(".\\Resources\\avast.png")
avast_image = avast_image.resize((20, 20))
avast_photo = ImageTk.PhotoImage(avast_image)

# Display image
avast_image_label = tk.Label(root, image=avast_photo)
avast_image_label.grid(row=2, column=0)

# Checkbox
avast_checkbox = tk.Checkbutton(root, text="Avast")
avast_checkbox.grid(row=2, column=1, sticky="w")
avast_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Avast"))
# endregion


# region Chrome
# Load image
chrome_image = Image.open(".\\Resources\\chrome.png")
chrome_image = chrome_image.resize((20, 20))
chrome_photo = ImageTk.PhotoImage(chrome_image)

# Display image
chrome_image_label = tk.Label(root, image=chrome_photo)
chrome_image_label.grid(row=4, column=0)

# Checkbox
chrome_checkbox = tk.Checkbutton(root, text="Google Chrome")
chrome_checkbox.grid(row=4, column=1, sticky="w")
chrome_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Google Chrome"))
# endregion


# region Opera
# Load image
opera_image = Image.open(".\\Resources\\opera.png")
opera_image = opera_image.resize((20, 20))
opera_photo = ImageTk.PhotoImage(opera_image)

# Display image
opera_image_label = tk.Label(root, image=opera_photo)
opera_image_label.grid(row=4, column=2)

# Checkbox
opera_checkbox = tk.Checkbutton(root, text="Opera GX")
opera_checkbox.grid(row=4, column=3, sticky="w")
opera_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Opera GX"))
# endregion


# region Iobit Uninstaller
# Load image
iobitu_image = Image.open(".\\Resources\\iobit-uninstaller.png")
iobitu_image = iobitu_image.resize((20, 20))
iobitu_photo = ImageTk.PhotoImage(iobitu_image)

# Display image
iobitu_image_label = tk.Label(root, image=iobitu_photo)
iobitu_image_label.grid(row=6, column=0)

# Checkbox
iobitu_checkbox = tk.Checkbutton(root, text="Iobit Uninstaller")
iobitu_checkbox.grid(row=6, column=1, sticky="w")
iobitu_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Iobit Uninstaller"))
# endregion


# region Advanced Systemcare
# Load image
asystemcare_image = Image.open(".\\Resources\\advenced-systemcare.png")
asystemcare_image = asystemcare_image.resize((20, 20))
asystemcare_photo = ImageTk.PhotoImage(asystemcare_image)

# Display image
asystemcare_image_label = tk.Label(root, image=asystemcare_photo)
asystemcare_image_label.grid(row=6, column=2)

# Checkbox
asystemcare_checkbox = tk.Checkbutton(root, text="Advanced Systemcare")
asystemcare_checkbox.grid(row=6, column=3, sticky="w")
asystemcare_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Advanced Systemcare"))
# endregion


# region Teams
teams_image = Image.open(".\\Resources\\teams.png")
teams_image = teams_image.resize((20, 20))
teams_photo = ImageTk.PhotoImage(teams_image)

# Display image
teams_image_label = tk.Label(root, image=teams_photo)
teams_image_label.grid(row=8, column=0)

# Checkbox
teams_checkbox = tk.Checkbutton(root, text="Teams")
teams_checkbox.grid(row=8, column=1, sticky="w")
teams_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Teams"))
# endregion


# region Discord
dc_image = Image.open(".\\Resources\\discord.png")
dc_image = dc_image.resize((20, 20))
dc_photo = ImageTk.PhotoImage(dc_image)

# Display image
dc_image_label = tk.Label(root, image=dc_photo)
dc_image_label.grid(row=8, column=2)

# Checkbox
dc_checkbox = tk.Checkbutton(root, text="Discord")
dc_checkbox.grid(row=8, column=3, sticky="w")
dc_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Discord"))
# endregion


# region Python
python_image = Image.open(".\\Resources\\python.png")
python_image = python_image.resize((20, 20))
python_photo = ImageTk.PhotoImage(python_image)

# Display image
python_image_label = tk.Label(root, image=python_photo)
python_image_label.grid(row=10, column=0)

# Checkbox
python_checkbox = tk.Checkbutton(root, text="Python")
python_checkbox.grid(row=10, column=1, sticky="w")
python_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Python"))
# endregion


# region DotNet
dotnet_image = Image.open(".\\Resources\\dotnet.png")
dotnet_image = dotnet_image.resize((20, 20))
dotnet_photo = ImageTk.PhotoImage(dotnet_image)

# Display image
dotnet_image_label = tk.Label(root, image=dotnet_photo)
dotnet_image_label.grid(row=10, column=2)

# Checkbox
dotnet_checkbox = tk.Checkbutton(root, text=".Net")
dotnet_checkbox.grid(row=10, column=3, sticky="w")
dotnet_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("DotNet"))
# endregion


# region Java
java_image = Image.open(".\\Resources\\java.png")
java_image = java_image.resize((20, 20))
java_photo = ImageTk.PhotoImage(java_image)

# Display image
java_image_label = tk.Label(root, image=java_photo)
java_image_label.grid(row=11, column=0)

# Checkbox
java_checkbox = tk.Checkbutton(root, text="Java")
java_checkbox.grid(row=11, column=1, sticky="w")
java_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Java"))
# endregion


# region Notepad++
notepad_image = Image.open(".\\Resources\\notepad.png")
notepad_image = notepad_image.resize((20, 20))
notepad_photo = ImageTk.PhotoImage(notepad_image)

# Display image
notepad_image_label = tk.Label(root, image=notepad_photo)
notepad_image_label.grid(row=11, column=2)

# Checkbox
notepad_checkbox = tk.Checkbutton(root, text="Notepad++")
notepad_checkbox.grid(row=11, column=3, sticky="w")
notepad_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Notepad++"))
# endregion


# region VS Code
vscode_image = Image.open(".\\Resources\\vscode.png")
vscode_image = vscode_image.resize((20, 20))
vscode_photo = ImageTk.PhotoImage(vscode_image)

# Display image
vscode_image_label = tk.Label(root, image=vscode_photo)
vscode_image_label.grid(row=12, column=0)

# Checkbox
vscode_checkbox = tk.Checkbutton(root, text="VS Code")
vscode_checkbox.grid(row=12, column=1, sticky="w")
notepad_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("VS Code"))
# endregion


# region WinRar
winrar_image = Image.open(".\\Resources\\winrar.png")
winrar_image = winrar_image.resize((20, 20))
winrar_photo = ImageTk.PhotoImage(winrar_image)

# Display image
winrar_image_label = tk.Label(root, image=winrar_photo)
winrar_image_label.grid(row=14, column=0)

# Checkbox
winrar_checkbox = tk.Checkbutton(root, text="WinRar")
winrar_checkbox.grid(row=14, column=1, sticky="w")
winrar_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("WinRar"))
# endregion


# region Daemon Tools
daemon_image = Image.open(".\\Resources\\daemon-tools.png")
daemon_image = daemon_image.resize((20, 20))
daemon_photo = ImageTk.PhotoImage(daemon_image)

# Display image
daemon_image_label = tk.Label(root, image=daemon_photo)
daemon_image_label.grid(row=14, column=2)

# Checkbox
daemon_checkbox = tk.Checkbutton(root, text="Daemon ToolsXXXX")
daemon_checkbox.grid(row=14, column=3, sticky="w")
daemon_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Daemon Tools"))
# endregion


# region qBittorent
qbit_image = Image.open(".\\Resources\\qbittorrent.png")
qbit_image = qbit_image.resize((20, 20))
qbit_photo = ImageTk.PhotoImage(qbit_image)

# Display image
qbit_image_label = tk.Label(root, image=qbit_photo)
qbit_image_label.grid(row=15, column=0)

# Checkbox
qbit_checkbox = tk.Checkbutton(root, text="qBittorrtentXXXX")
qbit_checkbox.grid(row=15, column=1, sticky="w")
qbit_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("qBittorrent"))
# endregion


# region Steam
steam_image = Image.open(".\\Resources\\steam.png")
steam_image = steam_image.resize((20, 20))
steam_photo = ImageTk.PhotoImage(steam_image)

# Display image
steam_image_label = tk.Label(root, image=steam_photo)
steam_image_label.grid(row=15, column=2)

# Checkbox
steam_checkbox = tk.Checkbutton(root, text="Steam")
steam_checkbox.grid(row=15, column=3, sticky="w")
steam_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("Steam"))
# endregion


# region TeamViewer
teamviewer_image = Image.open(".\\Resources\\teamviewer.png")
teamviewer_image = teamviewer_image.resize((20, 20))
teamviewer_photo = ImageTk.PhotoImage(teamviewer_image)

# Display image
teamviewer_image_label = tk.Label(root, image=teamviewer_photo)
teamviewer_image_label.grid(row=16, column=0)

# Checkbox
teamviewer_checkbox = tk.Checkbutton(root, text="TeamViewer")
teamviewer_checkbox.grid(row=16, column=1, sticky="w")
teamviewer_checkbox.bind('<Button-1>', lambda event: f.chckbx_changed("TeamViewer"))
# endregion


# region Textbox
download_txtbx_scrollbar = tk.Scrollbar(root, orient="horizontal")
download_txtbx_scrollbar.grid(row=19, column=0, columnspan=4, sticky="ew")
download_txtbx_scrollbar.config(command=on_dowlnoad_txtbx_scrollbar_move)

download_txtbx_text = tk.StringVar()
download_txtbx_text.set(programs.installer_path)
download_txtbx = tk.Entry(root, textvariable=download_txtbx_text,
                          state="readonly", xscrollcommand=download_txtbx_scrollbar.set)
download_txtbx.grid(row=18, column=0, columnspan=4, sticky="ew")
# endregion


# region Buttons
change_path_bttn = tk.Button(root, text="Change download path", command=change_path_bttn_click)
change_path_bttn.grid(row=20, column=0, columnspan=4, sticky="ew")

# Download button
download_bttn = tk.Button(root, text="Download", width=25, command=f.download_bttn_click)
download_bttn.grid(row=21, column=0, columnspan=2, sticky="ew", pady=(20, 0))

# Install button
install_bttn = tk.Button(root, text="Install", width=25, command=f.install_bttn_click)
install_bttn.grid(row=21, column=2, columnspan=2, sticky="ew", pady=(20, 0))

# Download & Install button
auto_bttn = tk.Button(root, text="Download & Install", command=f.auto_bttn_click)
auto_bttn.grid(row=22, column=0, columnspan=4, sticky="ew")
# endregion


# Main
if __name__ == '__main__':
    root.mainloop()
