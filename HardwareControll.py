import requests
import time

url = "http://192.168.188.25"

while True:
    for i in range(1, 16):
        requests.put(url, data=str(i), timeout=10)
        time.sleep(0.5)

        requests.put(url, data="0", timeout=10)
        time.sleep(0.5)
