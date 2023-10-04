import os

installer_path = f"{os.path.expanduser('~')}\\Downloads\\Downloaded Installers"
programs_to_install = []
installed_programs = []
all_programs = []


# Class for apps
class App:
    def __init__(self, name, url, flags):
        self.name = name
        self.url = url
        self.flags = flags
        all_programs.append(self)


def get_by_name(name):
    for app in all_programs:
        if app.name == name:
            return app


chrome = App("Google Chrome",
             "https://dl.google.com/"
             "tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B618ACBDD-3ECC-E2AE-B51C-"
             "62A89ADF533C%7D%26lang%3Dhu%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome"
             "%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DYTUH%26installdataindex%3Dempty/"
             "update2/installers/ChromeSetup.exe",
             ["/silent", "/install"])

opera = App("Opera GX",
            "https://net.geo.opera.com/"
            "opera_gx/stable/windows?utm_tryagain=yes&utm_source=google&utm_medium=ose&utm_campaign=(none)&"
            "http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&",
            ["/silent", "/launchbrowser=0"])

iobit_uninstaller = App("Iobit Uninstaller",
                        "https://cdn.iobit.com/dl/iobituninstaller.exe",
                        ["/VERYSILENT", "/NORESTART", "/Install"])

advanced_systemcare = App("Advanced Systemcare",
                          "https://cdn.iobit.com/dl/advanced-systemcare-setup.exe",
                          ["/VERYSILENT", "/NORESTART", "&& TASKKILL /F /IM ASC.exe"])

avast = App("Avast",
            "https://www.avast.com/hu-hu/download-thank-you.php?product=FAV-PPC&locale=hu-hu&direct=1",
            ["/silent"])

winrar = App("WinRar",
             "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-623.exe",
             ["/S"])

daemon_tools = App("Daemon Tools",
                   "https://www.daemon-tools.cc/products/dtLite#install-dtLite",
                   ["/S"])

qbittorrent = App("qBittorrent",
                  "asd",
                  ["/S"])

java = App("Java",
           "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=248737_8c876547113c4e4aab3c868e9e0ec572",
           ["/s"])

teams = App("Teams",
            "https://go.microsoft.com/"
            "fwlink/?linkid=2187327&Lmsrc=groupChatMarketingPageWeb&Cmpid=directDownloadv2Win64&clcid="
            "0x409&culture=en-us&country=us",
            ["-s"])

discord = App("Discord",
              "https://discord.com/"
              "api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86",
              ["-s"])

steam = App("Steam",
            "https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe",
            ["/S"])

teamviewer = App("TeamViewer",
                 "https://download.teamviewer.com/"
                 "download/TeamViewer_Setup_x64.exe?utm_source=google&utm_medium=cpc&utm_campaign="
                 "restofeurope%7Cb%7Cpr%7C22%7Caug%7Ctv-core-download-sn%7Cnew%7Ct0%7C0&utm_content="
                 "Download&utm_term=teamviewer+download",
                 ["/S"])

python = App("Python",
             "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe",
             ["/quiet"])

dotnet = App("DotNet",
             "https://download.visualstudio.microsoft.com/"
             "download/pr/1c8737a4-8cf1-4251-af5f-4a9c119a2489/c42c16d1f664719564353489c2b9b8d8/"
             "dotnet-sdk-7.0.401-win-x64.exe",
             ["/q", "/norestart"])

notepad = App("Notepad++",
              "https://github.com/"
              "notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.7/npp.8.5.7.Installer.x64.exe",
              ["/S"])

vscode = App("VS Code",
             "https://az764295.vo.msecnd.net/"
             "stable/abd2f3db4bdb28f9e95536dfa84d8479f1eb312d/VSCodeUserSetup-x64-1.82.2.exe",
             ["/VERYSILENT", "/NORESTART", "/MERGETASKS=!runcode"])
