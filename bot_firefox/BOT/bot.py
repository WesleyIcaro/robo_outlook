from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# Escolha do navegador
navegador = webdriver.Firefox()

# Acessar o outlook
navegador.get('https://login.live.com/')

# Preencher o email
navegador.find_element(By.XPATH, '//*[@id="i0116"]').send_keys('exemplo@email.com')

# Clicar no botão próximo
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()

# Preencher a senha
navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('exemplo')

# Esperar um tempo para não dar erro
sleep(1)

# Clicar no botão próximo
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()

# Clicar na opção não quero ficar logo no outlook
navegador.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()

# Esperar um tempo para não dar erro
sleep(3.5)

# Clicar no menu para abrir o outlook
navegador.find_element(By.XPATH, '//*[@id="O365_MainLink_NavMenu"]/span').click()

sleep(1)

# Clicar(Abrir) no Outlook
navegador.find_element(By.XPATH, '//*[@id="O365_AppTile_Mail"]').click()
