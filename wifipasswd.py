import subprocess
from pyfiglet import Figlet
import colorama

colorama.init()
f = Figlet(font='slant')
print(colorama.Fore.GREEN + f.renderText('LEEICE - WIFIPASSWORD'))

profile = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8', errors="backslasherplace").split('\n')[1:]

profile_names = [i.split(':')[1][1:-1] for i in profile if "All User Profile" in i]

print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("---------------------------------------------------------------")

for name in profile_names:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8', errors="backslashedplace").split('\n') 
        password = [line.split(':')[1][1:-1] for line in result if "Key Content" in line][0]

        print("{:<30}| {:<}".format(name, password))

    except:print("{:<30}| {:<}".format(name, "1"))