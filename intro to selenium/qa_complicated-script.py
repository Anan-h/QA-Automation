from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://ultimateqa.com/complicated-page')

buttons=driver.find_elements(By.XPATH,"//a[contains(text(),'Button')]")
for i in range(len(buttons)):
    driver.find_element(By.XPATH,f"//a[@class='et_pb_button et_pb_button_{i} et_pb_bg_layout_light']").click()

left_section=driver.find_elements(By.XPATH,"//div[@class='et_pb_column et_pb_column_1_2 et_pb_column_7  et_pb_css_mix_blend_mode_passthrough']")
name=driver.find_element(By.ID,'et_pb_contact_name_0')
name.send_keys('Anan')
email=driver.find_element(By.ID,'et_pb_contact_email_0')
email.send_keys('anan.hosien@gmail.com')
msg=driver.find_element(By.ID,'et_pb_contact_message_0')
msg.send_keys("Hello my name is anan")

driver.quit()
