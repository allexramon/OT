
import rpa as r
import pyautogui as p
from selenium.webdriver import Chrome
navegador = Chrome(executable_path="/Users/macbook/PycharmProjects/OT/chromedriver")

r.init()
r.url('https://shopper.com.br/lojas/')
p.sleep(3)
r.click('//*[@id="header"]/div/div/ul[1]/li[2]/a')
p.sleep(3)
#Dados
login = [""]
senha = [""]

#clicar no campo email
#r.click('/html/body/div[3]/div/div/div/div/div[2]/div/div/div[1]/div[1]/form/div/div[1]/input')
#input = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/div/div[1]/div[1]/form/div/div[1]/input')
#input.clear()
#input.send_keys(login)
#input_place = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/div/div[1]/div[1]/form/div/div[1]/input')
input_place = navegador.find_element_by_name('email')
sleep(2)
input_place.send_keys("alexramon@gmail.com")
p.sleep(1)


#clicar no campo senha
#r.click('/html/body/div[3]/div/div/div/div/div[2]/div/div/div[1]/div[1]/form/div/div[2]/input')
input = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/div/div[1]/div[1]/form/div/div[2]/input')
input.clear()
input.send_keys(senha)
p.sleep(1)

#clicar no botao entrar
r.click('/html/body/div[3]/div/div/div/div/div[2]/div/div/div[1]/div[1]/form/button')
