from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("https://discord.com/login")
import creacionBot
input("presione enter: ")
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
driver.get('https://discord.com/channels/356508875505139712/765982735076425749')
codigoViejo = ''

while True:

    try:
        #time.sleep(1)
        html = driver.page_source
        soup = bs(html, "html.parser")
        mensajes = soup.findAll(class_='markup-2BOw-j')
        codeNuevo = mensajes[-2].text #esto representa el anteultimo
        if codeNuevo == codigoViejo : continue
        codigoViejo = codeNuevo
        print("codigo: ", codeNuevo)

        #mandando al otro server:
    except:
        continue
        creacionBot.mandarMensaje(codesNuevos,'CyberBot')



