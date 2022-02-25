
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('window_size=400,800')

navegador = webdriver.Chrome(executable_path="/Users/macbook/PycharmProjects/OT/chromedriver", options=options)

navegador.get('https://www.airbnb.com')
sleep(1)

input_place = navegador.find_element_by_xpath('//*[@id="bigsearch-query-location-input"]')
sleep(2)
input_place.send_keys("São Paulo")
sleep(2)
input_place.submit()

#    site = BeautifulSoup(navegador.page_source, 'html.parser')
#   print(site.prettify())