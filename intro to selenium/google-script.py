from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# infra
driver= webdriver.Chrome()

# infra     logic
driver.get('https://www.google.co.il/')

# logic
# changing google to english
english=driver.find_element(By.XPATH,'//*[@id="SIvCob"]/a[2]')
english.click()
# locating the element of the searching bar and typing Python programming
search_input=driver.find_element(By.ID,'APjFqb')
search_input.send_keys('Python programming')
# pressing the return key on the keyboard
search_input.send_keys(Keys.RETURN)

# locating the element for the first search result
# me
# //a[@href='https://www.python.org/about/gettingstarted/']//h3[@class='LC20lb MBeuO DKV0Md']
# xpath
# //*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3
first_result=driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3' )
print(first_result.text)

driver.quit()