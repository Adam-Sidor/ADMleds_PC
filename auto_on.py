import requests
import re

def checkInternetStatus():
    try:
        requests.get("http://google.com",timeout=5)
        return True
    except requests.ConnectionError:
        return False

def readIPs(filePath):
    try:
        with open(filePath,'r') as file:
            content = file.read()
            pattern = r"IP:\s*\[\s*([^\]]+)\s*\]"
            match = re.search(pattern, content)
            if match:
                ipAddresses = match.group(1)
                ipList = [ip.strip() for ip in ipAddresses.split(";")]
                return ipList
    except FileNotFoundError:
        print("File not found!")
        return []

if checkInternetStatus():
    print("Masz internet")
    IPs = readIPs("config.txt")
    print(IPs)
else:
    print("brak")