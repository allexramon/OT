
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
#options.add_argument('window_size=400,800')

navegador = webdriver.Chrome(executable_path="/Users/macbook/PycharmProjects/OT/chromedriver", options=options)

navegador.get('https://shopper.com.br/lojas/')
sleep(1)
input_place = navegador.find_element_by_xpath('//*[@id="header"]/div/div/ul[1]/li[2]/a')
sleep(2)
input_place.send_keys("alexramon@gmail.com")
sleep(2)
#input_place.submit()

#    site = BeautifulSoup(navegador.page_source, 'html.parser')
#   print(site.prettify())
#teste