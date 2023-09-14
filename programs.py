import os

#Class for apps
class App:
    def __init__(self, name, url, flags):
        self.name = name
        self.url = url
        self.flags = flags
        self.path = f"{os.getcwd()}/Installers/{name}Setup.exe"

chrome = App("Chrome",
             "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B618ACBDD-3ECC-E2AE-B51C-62A89ADF533C%7D%26lang%3Dhu%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DYTUH%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe",
             ["/install", "/quiet"])

opera = App("Opera",
            "https://net.geo.opera.com/opera_gx/stable/windows?utm_source=google&utm_medium=ose&utm_campaign=%28none%29&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&utm_lastpage=opera.com%2F&dl_token=58304643",
            ["/silent", "/allusers=1", "/setdefaultbrowser=0", "/pintotaskbar=0"])