from selenium import webdriver
from selenium.webdriver.common.keys import Keys

msg = input('Enter the message : ')
count = int(input('Enter the count : '))

driver = webdriver.Chrome("chromedriver.exe")

driver.get('http://web.whatsapp.com')

# Scan the code before proceeding further
input('Press any key after scanning QR code')

input("Click on the user and then press any key")

msg_box = driver.find_element_by_xpath(
    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.ENTER)

driver.close()
