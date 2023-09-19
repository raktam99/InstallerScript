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
            "https://net.geo.opera.com/opera_gx/stable/windows?utm_source=google&utm_medium=ose&utm_campaign=%28none%29&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&utm_lastpage=opera.com%2F&dl_token=58304643",
            ["/silent", "/allusers=1", "/setdefaultbrowser=0", "/pintotaskbar=0", "/launchbrowser=0"])

iobit_uninstaller = App("Iobit_Uninstaller",
                        "https://cdn.iobit.com/dl/iobituninstaller.exe",
                        ["/VERYSILENT", "/NORESTART", "/Install"])

advanced_systemcare = App("Advanced_Systemcare",
                          "https://cdn.iobit.com/dl/advanced-systemcare-setup.exe",
                          ["/VERYSILENT", "/NORESTART"])

avast = App("Avast",
            "https://bits.avcdn.net/productfamily_ANTIVIRUS/insttype_FREE/platform_WIN/installertype_ONLINE/build_RELEASE/cookie_mmm_ava_012_999_a7i_m",
            ["/silent"])

winrar = App("WinRar",
             "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-623.exe",
             ["/S"])

daemon_tools = App("Daemon_Tools",
                   "https://file-service-default-114c67af0763a8a98e770ff3ee495371.fra1.digitaloceanspaces.com/40f7fe6349416c00d871ad7a543ae0bf784c5ed8/DTLite1120-2105.exe?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=Z42SJEYMLCPREOBRVPTN%2F20230919%2Ffra1%2Fs3%2Faws4_request&X-Amz-Date=20230919T121516Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=3491c3aae14f06129f054c5a3a70497b28a00eedb1bf62a4b6cfc2f0a138a3b7",
                   ["/S"])

qbittorrent = App("qBittorrent",
                  "https://download.fosshub.com/Protected/expiretime=1694821705;badurl=aHR0cHM6Ly93d3cuZm9zc2h1Yi5jb20vcUJpdHRvcnJlbnQuaHRtbA==/5112b8d37ed0e9e2068afa2ac242901e18f229b6162764f1b9f16ea05519bd8b/5b8793a7f9ee5a5c3e97a3b2/64ee7adf2be6f897089e8299/qbittorrent_4.5.5_x64_setup.exe",
                  ["/S"])

java = App("Java",
           "https://sdlc-esd.oracle.com/ESD6/JSCDL/jdk/8u381-b09/8c876547113c4e4aab3c868e9e0ec572/jre-8u381-windows-i586.exe?GroupName=JSC&FilePath=/ESD6/JSCDL/jdk/8u381-b09/8c876547113c4e4aab3c868e9e0ec572/jre-8u381-windows-i586.exe&BHost=javadl.sun.com&File=jre-8u381-windows-i586.exe&AuthParam=1695127012_c76fab073fce2a404d4e4b4647ce7992&ext=.exe",
           ["/s"])

teams = App("Teams",
            "https://statics.teams.cdn.office.net/production-windows/1.6.00.24078/TeamsSetup.exe?sv=2019-07-07&sr=b&sig=kYc6Nj5Jp6%2F%2FBEImeNhqv6IHiC10LbO8Npl8ty3pEzk%3D&se=2023-09-19T13%3A14%3A08Z&sp=r&rscd=attachment%3B%20filename%3D%22TeamsSetup_c_w_.exe%22",
            ["-s"])

discord = App("Discord",
              "https://dl.discordapp.net/distro/app/stable/win/x86/1.0.9017/DiscordSetup.exe",
              ["-s"])

steam = App("Steam",
            "https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe",
            ["/S"])

teamviewer = App("TeamViewer",
                 "https://dl.teamviewer.com/download/version_15x/TeamViewer_Setup_x64.exe?utm_source=google&utm_medium=cpc&utm_campaign=restofeurope%7Cb%7Cpr%7C22%7Caug%7Ctv-core-brand-only-exact-sn%7Cnew%7Ct0%7C0&utm_content=Exact&utm_term=teamviewer&ref=https%3A%2F%2Fwww.teamviewer.com%2Fen%2Fdownload%2Fwindows%2F%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Drestofeurope%257Cb%257Cpr%257C22%257Caug%257Ctv-core-brand-only-exact-sn%257Cnew%257Ct0%257C0%26utm_content%3DExact%26utm_term%3Dteamviewer",
                 ["/S"])
