import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json
import requests
false = False
true = True

#rjson = {"amount":100,"createdByUser":false,"creatorName":"f2ce","creatorUserId":"4d017c4d-57e1-4bb1-ade4-473f0a3746b2","id":"ce39714e-ae74-4a15-a028-50d8db60bc00","rainEndTime":"2020-11-16T23:15:50.575Z","rainInit":"2020-11-16T23:13:50.575Z","rainStartTime":"2020-11-16T23:14:50.575Z","selectedBalanceField":"balance","status":"countdown","hasJoined":false}

id = ""
link = "https://api.roobet.com/rain/active"
linux = True

if linux == True:
    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(executable_path="/roobet/pruebas/chromedriver",
    options=chromeOptions)
else:
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")


driver.get(link)
while True:
    html = driver.page_source
    soup = bs(html, "html.parser")
    driver.refresh()
    mensajes = soup.find("pre").context[0]
    print(mensajes)
    time.sleep(10)
    #try:
    #    mensajes = soup.findAll(pre).context[0]
    #    print(1)
    #    rjson = response.json()
    #    print(2)
    #    if rjson['id'] == id: continue
    #    id = rjson['id']
    #    print('TENEMOS RAIN!!!')
    #    print(rjson)
    #    cantidad,usuario,rainEnd = rjson['amount'], rjson['createdByUser'], rjson['rainEndTime']
    #    if usuario == False: usuario = 'Roobet'
    #    msg = 'Cantidad: ' + str(cantidad) + '. Usuario creador: ' + str(usuario) + '. Rain hasta: ' + str(rainEnd)
    #    print(msg)
    #except:
    #    time.sleep(7)
       #print("no hay nada, pasamos")
    #    continue

