import requests
import time

url = "http://192.168.188.25"

def main():
    while True:
        for i in range(1, 16):
            requests.put(url, data=str(i), timeout=10)
            print("Send Request")
            time.sleep(0.5)

            requests.put(url, data="0", timeout=10)
            time.sleep(0.5)
            print("Set system to 0")

try:
    main()
except KeyboardInterrupt:
    requests.put(url, data="0", timeout=10)
