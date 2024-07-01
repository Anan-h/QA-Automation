from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()

driver.get('https://www.google.co.il/')

search_input=driver.find_element(By.ID,'APjFqb')
search_input.send_keys('Python programming')
search_input.send_keys(Keys.RETURN)

driver.quit()