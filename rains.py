import time
import json
import requests

rjson2 = dict()
# while True:
#     response = requests.get("https://httpbin.org/stream/1")
#     try:
#         rjson = response.json()
#         if rjson == rjson2: continue
#         rjson2 = rjson
#         print(rjson)
#     except:
#         time.sleep(7)
#         print(time.time())
#         #print("no hay nada, pasamos")
#         continue
response = requests.get("https://httpbin.org/stream/1")
rjson = response.json()
print(rjson)