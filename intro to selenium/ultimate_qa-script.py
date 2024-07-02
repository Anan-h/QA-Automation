from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

click_me_btn=driver.find_element(By.XPATH,"//button[contains(text(),'Click Me!')]").click()
driver.back()

raise_btn=driver.find_element(By.XPATH,"//button[@id='button2']").click()
driver.back()

driver.find_element(By.XPATH,"//a[@id='idExample']").click()
print(driver.find_element(By.XPATH,"//h1[@class='entry-title']").text)
driver.back()

name=driver.find_element(By.XPATH,"//input[@id='et_pb_contact_name_0']")
name.send_keys('Anan')
email=driver.find_element(By.XPATH,"//input[@id='et_pb_contact_email_0']")
email.send_keys('anan.hosien@gmail.com')
send_btn=driver.find_element(By.XPATH,"//div[@class='et_contact_bottom_container']//button")
send_btn.click()
driver.implicitly_wait(3)
text=driver.find_element(By.XPATH,"//div[@class='et-pb-contact-message']//p")
print(text.text)

male=driver.find_element(By.XPATH,"//input[@value='male']")
male.click()
print(male.is_selected())

car=driver.find_element(By.XPATH,"//input[@value='Car']")
car.click()
print(car.is_selected())

driver.find_element(By.XPATH,"//a[contains(text(),'Click me using this link text!')]").click()

driver.quit()