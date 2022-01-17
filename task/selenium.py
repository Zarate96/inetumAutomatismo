import time
from selenium import webdriver
from datetime import date
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import json
import requests
import cv2

#path= "/home/zarate/Documents/inetumAutomatismo/chromedriver"
#path= "/root/inetumAutomatismo/chromedriver"
path = 'C:\Users\INETUM\inetumAutomatismo\chromedriver'
URL = 'https://api.telegram.org/bot2114681560:AAGPlALNSj-TWi2ipYkkyJ7r6oKbKkJGdz0/sendPhoto'
URL2 = 'https://api.telegram.org/bot2114681560:AAGPlALNSj-TWi2ipYkkyJ7r6oKbKkJGdz0/sendMessage'
chat_id = 1663958489
#chat_id = -224944366
WINDOW_SIZE = "1920,1080"


def get_rstat():
    now = datetime.now()
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.get("http://10.225.245.42/Rstat/Index.htm#")

        time.sleep(5)
        elem = driver.find_element_by_id("txtUsuario")
        elem.send_keys("MRT12790")
        elem = driver.find_element_by_id("txtContrasena")
        elem.send_keys("MRT12790")
        elem = driver.find_element_by_id("btnValida")
        elem.click()
        time.sleep(3)

        botonMenu = driver.find_element_by_xpath("//*[@id='opcMPLs']/a")
        if botonMenu is not None:
            acciones = ActionChains(driver)
            acciones.move_to_element(botonMenu).perform()
            liga = driver.find_element_by_link_text("Dashboards")

            if liga is not None:
                acciones2 = ActionChains(driver)
                acciones2.move_to_element(liga).perform()
                time.sleep(3)
                elem = driver.find_element_by_xpath("//*[@id='menuDashboardsMPLs']/li[3]/div")

                if elem is not None:
                    elem.click()

        time.sleep(10)
        window = driver.window_handles[1]
        driver.switch_to.window(window)
        time.sleep(2)
        driver.fullscreen_window()
        check = "check_Rstat.png"
        driver.save_screenshot(check)

        texto = "Se envia el Monitoreo del RSTAT a las {}:{}".format(now.hour, now.minute)

        r = requests.post(URL,
                          files={'photo': ('check_Rstat.png', open('check_Rstat.png', 'rb'))},
                          data={'chat_id': chat_id, 'caption': texto})

        driver.close()
        window = driver.window_handles[0]
        driver.switch_to.window(window)
        driver.close()


    except:
        texto = "Algo Salio mal con la imagen del RSTAT a las {}:{}".format(now.hour, now.minute)
        r = requests.post(URL2,
                          data={'chat_id': chat_id, 'text': texto})
        data = json.loads(r.text)
        print(data['ok'])
        driver.close()


def get_onstar():
    now = datetime.now()
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.get("http://10.225.245.42/Rstat/Index.htm#")

        time.sleep(5)
        elem = driver.find_element_by_id("txtUsuario")
        elem.send_keys("MRT12790")
        elem = driver.find_element_by_id("txtContrasena")
        elem.send_keys("MRT12790")
        elem = driver.find_element_by_id("btnValida")
        elem.click()
        time.sleep(3)

        botonMenu = driver.find_element_by_xpath("//*[@id='opcMPLs']/a")
        if botonMenu is not None:
            acciones = ActionChains(driver)
            acciones.move_to_element(botonMenu).perform()
            liga = driver.find_element_by_link_text("Dashboards")

            if liga is not None:
                acciones2 = ActionChains(driver)
                acciones2.move_to_element(liga).perform()
                time.sleep(3)
                elem = driver.find_element_by_xpath("//*[@id='menuDashboardsMPLs']/li[8]/div")

                if elem is not None:
                    elem.click()

        time.sleep(10)
        window = driver.window_handles[1]
        driver.switch_to.window(window)
        time.sleep(2)
        driver.fullscreen_window()
        check = "check_Onstar.png"
        driver.save_screenshot(check)

        texto = "Se envia el Monitoreo de Onstar a las {}:{}".format(now.hour, now.minute)

        r = requests.post(URL,
                          files={'photo': ('check_Onstar.png', open('check_Onstar.png', 'rb'))},
                          data={'chat_id': chat_id, 'caption': texto})

        data = json.loads(r.text)
        print(data['ok'])
        driver.close()
        window = driver.window_handles[0]
        driver.switch_to.window(window)
        driver.close()


    except:
        texto = "Algo Salio mal con la imagen de Onstar a las {}:{}".format(now.hour, now.minute)
        r = requests.post(URL2,
                          data={'chat_id': chat_id, 'text': texto})
        data = json.loads(r.text)
        print(data['ok'])
        driver.close()



def get_glpi():
    now = datetime.now()
    try:
        # Abre el driver y apertura la pagina del GLPI
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.get(
            "http://10.225.236.172/glpitemm/index.php?redirect=%2Ffront%2Fticket.php%3Fis_deleted%3D0%26search%3DBuscar%26itemtype%3DTicket%26criteria%5B0%5D%5Bfield%5D%3D12%26criteria%5B0%5D%5Bsearchtype%5D%3Dequals%26criteria%5B0%5D%5Bvalue%5D%3Dnotclosed%26criteria%5B1%5D%5Blink%5D%3DAND%2520NOT%26criteria%5B1%5D%5Bfield%5D%3D12%26criteria%5B1%5D%5Bsearchtype%5D%3Dequals%26criteria%5B1%5D%5Bvalue%5D%3D5%26reset%3Dreset&error=3")
        # Espera 3 seg
        time.sleep(3)
        # Busca el login y coloca el usuario y enter
        elem = driver.find_element_by_name("login_name")
        elem.send_keys("MRN22654")
        elem = driver.find_element_by_name("login_password")
        elem.send_keys("Roco!048")
        elem.send_keys(Keys.RETURN)

        # Espera 10 Seg para que entre a los Glpis
        time.sleep(3)

        # guarda la imagen de la captura y coloca el nombre check_GLPI
        driver.fullscreen_window()
        time.sleep(2)
        check = "check_GLPI.png"
        driver.save_screenshot(check)

        texto = "Se envia el estatus de los Glpis a las {}:{}".format(now.hour, now.minute)

        r = requests.post(URL,
                          files={'photo': ('check_GLPI.png', open('check_GLPI.png', 'rb'))},
                          data={'chat_id': chat_id, 'caption': texto})

        data = json.loads(r.text)
        print(data['ok'])
        # Cierra el navegador
        driver.close()


    except:
        texto = "Algo Salio mal con la imagen del Glpi a las {}:{}".format(now.hour, now.minute)
        r = requests.post(URL2,
                          data={'chat_id': chat_id, 'text': texto})
        data = json.loads(r.text)
        print(data['ok'])
        driver.close()



def get_santander():
    now = datetime.now()
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-certificate-errors-spki-list")
        chrome_options.add_argument("--ignore-ssl-errors")
        #chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver = webdriver.Chrome(path, chrome_options=chrome_options)
        driver.get("https://10.14.235.6/Orion/Login.aspx")
        time.sleep(5)

        elem = driver.find_element_by_id("details-button")
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_id("proceed-link")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        elem = driver.find_element_by_name("ctl00$BodyContent$Username")
        elem.send_keys("cliente_santander")
        elem = driver.find_element_by_name("ctl00$BodyContent$Password")
        elem.send_keys("fRw-O6q-5P7-EAf")
        elem.send_keys(Keys.RETURN)
        # Espera 2 Seg
        time.sleep(5)
        elem = driver.find_element_by_link_text("SANTANDER")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        # abre el navegador en pantalla completa
        driver.fullscreen_window()
        time.sleep(2)
        check = "check_santander.png"
        driver.save_screenshot(check)
        texto = "Se envia el Monitoreo del Cliente Santander a las {}:{}".format(now.hour, now.minute)

        r = requests.post(URL,
                          files={'photo': ('check_santander.png', open('check_santander.png', 'rb'))},
                          data={'chat_id': chat_id, 'caption': texto})
        driver.close()


    except:
        texto = "Algo Salio mal con la imagen del Cliente Santander a las {}:{}".format(now.hour, now.minute)
        r = requests.post(URL2,
                          data={'chat_id': chat_id, 'text': texto})
        data = json.loads(r.text)
        print(data['ok'])

        driver.close()



def get_hcInterATT():
    now = datetime.now().strftime("%H:%M")
    URL = 'https://api.telegram.org/bot2114681560:AAGPlALNSj-TWi2ipYkkyJ7r6oKbKkJGdz0/sendPhoto'
    chat_id = -396809016
    #chat_id = 1663958489
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(path, chrome_options=chrome_options)
    try:
        driver.get("http://127.0.0.1:8000/hc/interconexionATT/")
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        check = "InterATT.png"
        driver.save_screenshot(check)
        image = cv2.imread("InterATT.png")
        imageOut = image[0:1600, 0:1110]
        cv2.imwrite('InterATT.png', imageOut)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        texto = "Se envia el HC de Interconfiguración ATT {}".format(now)

        r = requests.post(URL,
                          files={'photo': ('InterATT.png', open('InterATT.png', 'rb'))},
                          data={'chat_id': chat_id, 'caption': texto})
        driver.close()

    except:
        texto = "Se tuvo un Error en obtener el HC de Interconfiguració de ATT {}:{}".format(now)
        r = requests.post(URL2,
                          data={'chat_id': chat_id, 'text': texto})

