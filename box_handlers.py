import programs


def chrome_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.chrome):
        programs.programs_to_install.append(programs.chrome)
    else:
        programs.programs_to_install.remove(programs.chrome)


def opera_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.opera):
        programs.programs_to_install.append(programs.opera)
    else:
        programs.programs_to_install.remove(programs.opera)


def iobitu_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.iobit_uninstaller):
        programs.programs_to_install.append(programs.iobit_uninstaller)
    else:
        programs.programs_to_install.remove(programs.iobit_uninstaller)


def asystemcare_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.advanced_systemcare):
        programs.programs_to_install.append(programs.advanced_systemcare)
    else:
        programs.programs_to_install.remove(programs.advanced_systemcare)


def avast_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.avast):
        programs.programs_to_install.append(programs.avast)
    else:
        programs.programs_to_install.remove(programs.avast)


def winrar_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.winrar):
        programs.programs_to_install.append(programs.winrar)
    else:
        programs.programs_to_install.remove(programs.winrar)


def daemon_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.daemon_tools):
        programs.programs_to_install.append(programs.daemon_tools)
    else:
        programs.programs_to_install.remove(programs.daemon_tools)


def qbit_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.qbittorrent):
        programs.programs_to_install.append(programs.qbittorrent)
    else:
        programs.programs_to_install.remove(programs.qbittorrent)


def java_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.java):
        programs.programs_to_install.append(programs.java)
    else:
        programs.programs_to_install.remove(programs.java)


def teams_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.teams):
        programs.programs_to_install.append(programs.teams)
    else:
        programs.programs_to_install.remove(programs.teams)


def dc_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.discord):
        programs.programs_to_install.append(programs.discord)
    else:
        programs.programs_to_install.remove(programs.discord)


def steam_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.steam):
        programs.programs_to_install.append(programs.steam)
    else:
        programs.programs_to_install.remove(programs.steam)


def teamviewer_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.teamviewer):
        programs.programs_to_install.append(programs.teamviewer)
    else:
        programs.programs_to_install.remove(programs.teamviewer)


def python_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.python):
        programs.programs_to_install.append(programs.python)
    else:
        programs.programs_to_install.remove(programs.python)


def dotnet_chckbx_changed():
    if not programs.programs_to_install.__contains__(programs.dotnet):
        programs.programs_to_install.append(programs.dotnet)
    else:
        programs.programs_to_install.remove(programs.dotnet)
