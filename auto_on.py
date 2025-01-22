import time
import requests
import re

def checkInternetStatus():
    try:
        requests.get("http://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def readIPs(filePath):
    try:
        with open(filePath, 'r') as file:
            content = file.read()
            pattern = r"IP:\s*\[\s*([^\]]+)\s*\]"
            match = re.search(pattern, content)
            if match:
                ipAddresses = match.group(1)
                ipList = [ip.strip() for ip in ipAddresses.split(";")]
                return ipList
    except FileNotFoundError:
        print("File not found!")
        with open(filePath, 'w') as file:
            file.write("IP:[]")
        input("Naciśnij dowolny przycisk, aby kontynuować...")
        return []

while not checkInternetStatus():
    print("Waiting...")

IPs = readIPs("C:\\Users\\Adam\\Documents\\ADMleds_PC\\config.txt") #You should set own file path
if IPs:
    for IP in IPs:
        try:
            print(f"Sending to {IP}")
            requests.get(f"http://{IP}/status=1", timeout=5)
        except requests.ConnectionError:
            pass  #ESP32 does not sending data back