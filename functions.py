import os
import programs
import requests
import subprocess


# Install click handler function
def download_bttn_click():
    if not os.path.isdir(programs.installer_path):
        os.mkdir(programs.installer_path)
    print("Created directory where installers will be stored!")

    if not len(programs.programs_to_install) == 0:
        print("Downloading Programs...")
        for program in programs.programs_to_install:
            download_app(program)

        print("Downloaded everything!")
    else:
        print("Nothing is selected")


# Install click handler function
def install_bttn_click():
    if not len(programs.programs_to_install) == 0:
        print("Installing programs...")

        for program in programs.programs_to_install:
            install_app(program)
            programs.installed_programs.append(program)

        print("Everything is installed!")
    else:
        print("Nothing to install!")


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
    if not programs.installed_programs.__contains__(application):
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
