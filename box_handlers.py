import programs


def chrome_chckbx_changed():
    if programs.chrome not in programs.programs_to_install:
        programs.programs_to_install.append(programs.chrome)
    else:
        programs.programs_to_install.remove(programs.chrome)


def opera_chckbx_changed():
    if programs.opera not in programs.programs_to_install:
        programs.programs_to_install.append(programs.opera)
    else:
        programs.programs_to_install.remove(programs.opera)


def iobitu_chckbx_changed():
    if programs.iobit_uninstaller not in programs.programs_to_install:
        programs.programs_to_install.append(programs.iobit_uninstaller)
    else:
        programs.programs_to_install.remove(programs.iobit_uninstaller)


def asystemcare_chckbx_changed():
    if programs.advanced_systemcare not in programs.programs_to_install:
        programs.programs_to_install.append(programs.advanced_systemcare)
    else:
        programs.programs_to_install.remove(programs.advanced_systemcare)


def avast_chckbx_changed():
    if programs.avast not in programs.programs_to_install:
        programs.programs_to_install.append(programs.avast)
    else:
        programs.programs_to_install.remove(programs.avast)


def winrar_chckbx_changed():
    if programs.winrar not in programs.programs_to_install:
        programs.programs_to_install.append(programs.winrar)
    else:
        programs.programs_to_install.remove(programs.winrar)


def daemon_chckbx_changed():
    print("Currently not working:(")
    if programs.daemon_tools not in programs.programs_to_install:
        programs.programs_to_install.append(programs.daemon_tools)
    else:
        programs.programs_to_install.remove(programs.daemon_tools)


def qbit_chckbx_changed():
    print("Currently not working:(")
    if programs.qbittorrent not in programs.programs_to_install:
        programs.programs_to_install.append(programs.qbittorrent)
    else:
        programs.programs_to_install.remove(programs.qbittorrent)


def java_chckbx_changed():
    if programs.java not in programs.programs_to_install:
        programs.programs_to_install.append(programs.java)
    else:
        programs.programs_to_install.remove(programs.java)


def teams_chckbx_changed():
    if programs.teams not in programs.programs_to_install:
        programs.programs_to_install.append(programs.teams)
    else:
        programs.programs_to_install.remove(programs.teams)


def dc_chckbx_changed():
    if programs.discord not in programs.programs_to_install:
        programs.programs_to_install.append(programs.discord)
    else:
        programs.programs_to_install.remove(programs.discord)


def steam_chckbx_changed():
    if programs.steam not in programs.programs_to_install:
        programs.programs_to_install.append(programs.steam)
    else:
        programs.programs_to_install.remove(programs.steam)


def teamviewer_chckbx_changed():
    if programs.teamviewer not in programs.programs_to_install:
        programs.programs_to_install.append(programs.teamviewer)
    else:
        programs.programs_to_install.remove(programs.teamviewer)


def python_chckbx_changed():
    if programs.python not in programs.programs_to_install:
        programs.programs_to_install.append(programs.python)
    else:
        programs.programs_to_install.remove(programs.python)


def dotnet_chckbx_changed():
    if programs.dotnet not in programs.programs_to_install:
        programs.programs_to_install.append(programs.dotnet)
    else:
        programs.programs_to_install.remove(programs.dotnet)


def notepad_chckbx_changed():
    if programs.notepad not in programs.programs_to_install:
        programs.programs_to_install.append(programs.notepad)
    else:
        programs.programs_to_install.remove(programs.notepad)


def vscode_chckbx_changed():
    if programs.vscode not in programs.programs_to_install:
        programs.programs_to_install.append(programs.vscode)
    else:
        programs.programs_to_install.remove(programs.vscode)
