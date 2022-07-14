import requests
import time
import string
import random
import threading

def generate_payload():
    parcel_code = ''.join(random.choices(string.digits,k=11))
    payload = """{"size": "A",\n
    "customerPhone": "888000002",\n
    "onDeliveryAmount": 0,\n
    "openCode": 295403,\n
    "parcelCode": "%s",\n
    "payCode": 12345,\n
    "status": "CUSTOMER_DELIVERING",\n
    "boxMachine": "CHO10N",\n
    "senderBoxMachine": "KRA03N",\n
    "directParcel": false,\n
    "parcelAttributes": [],\n
    "endOfWeekCollection": false\n
    }""" % parcel_code
    return payload

parcel_url = 'http://192.168.0.1:93/v1/parcelstationservice/parcel'
health_url = 'http://192.168.0.1:93/scl/api/health'

err_cnt = 0
try_cnt = 0

class RequestPOST:
    def request(self):
        requests.post(parcel_url,data = generate_payload(),timeout=5)
    def __init__(self):
        t = threading.Thread(target=self.request)
        t.start()

class RequestGET:
    def request(self):
        global err_cnt
        try:
            res = requests.get(health_url,timeout=5)
        except requests.exceptions.ConnectionError:
            err_cnt = err_cnt+1
            print(f"GET Connection error: {err_cnt}")
        else:
            data = res.json()
            memory = data['mng']['device']['memory']
            print(f"L2: {memory['freeMemory_L2']}")
            print(f"L3 Cached: {memory['freeMemory_L3_Cached']}")
            print(f"L3 Uncached: {memory['freeMemory_L3_Uncached']}")
            print("\r\n")

    def __init__(self):
        t = threading.Thread(target=self.request)
        t.start()

for i in range(500):
    try_cnt = try_cnt + 1
    print(f"Try no: {try_cnt}")
    for i in range(10):
        RequestGET()
    time.sleep(2)



