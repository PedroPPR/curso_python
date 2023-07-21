from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from selenium.webdriver.common.by import By



ser = Service("C:\\Users\\Desktop\\Projects\\auto_login\\msedgedriver.exe")
driver = webdriver.Edge(service = ser)
driver.get("https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html")


driver.find_element(By.XPATH, '//*[@id="menu-barra-brasil"]/ul/li[5]/a').click()
print(driver.title)
print(driver.current_url)




sleep(10)