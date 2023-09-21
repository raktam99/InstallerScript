import os

installer_path = f"{os.path.expanduser('~')}\\Downloads\\Downloaded Installers"
# Class for apps


class App:
    def __init__(self, name, url, flags):
        self.name = name
        self.url = url
        self.flags = flags


chrome = App("Chrome",
             "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B618ACBDD-3ECC-E2AE-B51C-62A89ADF533C%7D%26lang%3Dhu%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DYTUH%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe",
             ["/silent", "/install"])

opera = App("Opera",
            "https://net.geo.opera.com/opera_gx/stable/windows?utm_tryagain=yes&utm_source=google&utm_medium=ose&utm_campaign=(none)&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&",
            ["/silent", "/allusers=1", "/setdefaultbrowser=0", "/pintotaskbar=0", "/launchbrowser=0"])

iobit_uninstaller = App("Iobit_Uninstaller",
                        "https://cdn.iobit.com/dl/iobituninstaller.exe",
                        ["/VERYSILENT", "/NORESTART", "/Install"])

advanced_systemcare = App("Advanced_Systemcare",
                          "https://cdn.iobit.com/dl/advanced-systemcare-setup.exe",
                          ["/VERYSILENT", "/NORESTART"])

avast = App("Avast",
            "https://www.avast.com/hu-hu/download-thank-you.php?product=FAV-PPC&locale=hu-hu&direct=1",
            ["/silent"])

winrar = App("WinRar",
             "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-623.exe",
             ["/S"])

daemon_tools = App("Daemon_Tools",
                   "https://www.daemon-tools.cc/products/dtLite#install-dtLite",
                   ["/S"])

qbittorrent = App("qBittorrent",
                  "https://download.fosshub.com/Protected/expiretime=1695360299;badurl=aHR0cHM6Ly93d3cuZm9zc2h1Yi5jb20vcUJpdHRvcnJlbnQuaHRtbA==/3e0261725cbe8153b731ab93fec702c4c2edfa6c931c60e73afc2a4cdf751dd8/5b8793a7f9ee5a5c3e97a3b2/64ee7adf2be6f897089e8299/qbittorrent_4.5.5_x64_setup.exe",
                  ["/S"])

java = App("Java",
           "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=248737_8c876547113c4e4aab3c868e9e0ec572",
           ["/s"])

teams = App("Teams",
            "https://go.microsoft.com/fwlink/?linkid=2187327&Lmsrc=groupChatMarketingPageWeb&Cmpid=directDownloadv2Win64&clcid=0x409&culture=en-us&country=us",
            ["-s"])

discord = App("Discord",
              "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86",
              ["-s"])

steam = App("Steam",
            "https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe",
            ["/S"])

teamviewer = App("TeamViewer",
                 "https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe?utm_source=google&utm_medium=cpc&utm_campaign=restofeurope%7Cb%7Cpr%7C22%7Caug%7Ctv-core-download-sn%7Cnew%7Ct0%7C0&utm_content=Download&utm_term=teamviewer+download",
                 ["/S"])
