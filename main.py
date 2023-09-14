import threading
import tkinter as tk
from tkinter import Checkbutton, IntVar
from PIL import Image
from PIL import ImageTk
import requests
import subprocess
import os

#Downloader
def download_app(url, download_path, app_name, flags):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        with open(download_path, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded {app_name} successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

    run_installer(download_path, app_name, flags)

#Install app
def run_installer(path, name, flags):
    try:
        cmd = [path] + flags
        print(cmd)
        subprocess.run(cmd, shell=True, check=True)
        print(f"Installing {name}...")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {name}: {e}")
    except FileNotFoundError:
        print(f"Installer not found at path: {path}")

#Click handler
def bttn_click():
    if chrome_invar.get() == 1:
        print("Downloading Chrome...")
        download_app("https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B618ACBDD-3ECC-E2AE-B51C-62A89ADF533C%7D%26lang%3Dhu%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DYTUH%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe",
                     f"{os.getcwd()}/Installers/ChromeSetup.exe", "Chrome",
                     ["/install", "/quiet"])

    if opera_invar.get() == 1:
        print("Downloading Opera...")
        download_app("https://net.geo.opera.com/opera_gx/stable/windows?utm_source=google&utm_medium=ose&utm_campaign=%28none%29&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&utm_lastpage=opera.com%2F&dl_token=58304643",
                     f"{os.getcwd()}/Installers/OperaSetup.exe", "Opera",
                     ["/silent", "/allusers=1", "/setdefaultbrowser=0", "/pintotaskbar=0"])

    print("Everything is done!")

#Main app window
root = tk.Tk()
root.title("Installer")

#Text
choose_label = tk.Label(root, text="Please choose!")
choose_label.grid(row=0, column=0, padx=2, pady=2, columnspan=2)


#Chrome


#Load image
chrome_image = Image.open("./Resources/chrome.png")  # Replace "example.png" with your image file path
chrome_image = chrome_image.resize((20, 20))  # Resize the image to your desired dimensions
chrome_photo = ImageTk.PhotoImage(chrome_image)

#Display image
chrome_image_label = tk.Label(root, image=chrome_photo)
chrome_image_label.grid(row=1, column=0, padx=2, pady=2)

#Checkbox
chrome_invar = IntVar()
chrome_checkbox = Checkbutton(root, text="Chrome", variable=chrome_invar)
chrome_checkbox.grid(row=1, column=1, padx=2, pady=2)


#Opera


#Load image
opera_image = Image.open("./Resources/opera.png")  # Replace "example.png" with your image file path
opera_image = opera_image.resize((20, 20))  # Resize the image to your desired dimensions
opera_photo = ImageTk.PhotoImage(opera_image)

#Display image
opera_image_label = tk.Label(root, image=opera_photo)
opera_image_label.grid(row=2, column=0, padx=2, pady=2)

#Checkbox
opera_invar = IntVar()
opera_checkbox = Checkbutton(root, text="Opera", variable=opera_invar)
opera_checkbox.grid(row=2, column=1, padx=2, pady=2)



#Button
button = tk.Button(root, text="Install", command=bttn_click)
button.grid(row=3, column=0, padx=2, pady=2, columnspan=3)

#Main
if __name__ == '__main__':
    root.mainloop()