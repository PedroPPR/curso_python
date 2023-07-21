


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from selenium.webdriver.common.by import By



ser = Service("C:\\Users\\Desktop\\Projects\\auto_login\\msedgedriver.exe")
driver = webdriver.Edge(service = ser)
driver.get("https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp")


driver.find_element(By.XPATH, '//*[@id="btnDownloadUrl"]').click()
print(driver.title)
print(driver.current_url)

sleep(50)





