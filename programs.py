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
                   "https://file-service-default-114c67af0763a8a98e770ff3ee495371.fra1.digitaloceanspaces.com/40f7fe6349416c00d871ad7a543ae0bf784c5ed8/DTLite1120-2105.exe?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=Z42SJEYMLCPREOBRVPTN%2F20230915%2Ffra1%2Fs3%2Faws4_request&X-Amz-Date=20230915T153032Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Signature=67a4350688f51b72f3f36090ed4d5eded1de067f9591509c7230f52eb446cf91",
                   ["/S"])

qbittorrent = App("qBittorrent",
                  "https://download.fosshub.com/Protected/expiretime=1694821705;badurl=aHR0cHM6Ly93d3cuZm9zc2h1Yi5jb20vcUJpdHRvcnJlbnQuaHRtbA==/5112b8d37ed0e9e2068afa2ac242901e18f229b6162764f1b9f16ea05519bd8b/5b8793a7f9ee5a5c3e97a3b2/64ee7adf2be6f897089e8299/qbittorrent_4.5.5_x64_setup.exe",
                  ["/S"])
