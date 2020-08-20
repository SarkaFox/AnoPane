from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# name the URL
# HomeURL = "https://digitalninomadstvi.cz"

driver = webdriver.Chrome()
driver.get("https://digitalninomadstvi.cz")


# to wait for web to be ready for next step
#try:
#    header = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.ID, "header")))
#finally:
#    driver.quit()

# elementCestovani = driver.find_element_by_xpath('//*[@id="menu-item-6330"]/a')

elementCestovani = driver.find_element_by_xpath("//span[text()='Cestování']")
# if(element.is_displayed())
elementCestovani.click()

driver.back()

elementPraceNaDalku = driver.find_element_by_xpath('//*[@id="menu-item-7444"]/a/span')
elementPraceNaDalku.click()

driver.back()

elementInvestovani = driver.find_element_by_xpath('//*[@id="menu-item-6517"]/a/span')
elementInvestovani.click()


elementVybaveni = driver.find_element_by_xpath('//*[@id="menu-item-6271"]/a/span')
elementVybaveni.click()


elementPodcast = driver.find_element_by_xpath('//*[@id="menu-item-9441"]/a')
elementPodcast.click()

driver.back()

elementClenskaSekce = driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/div/div/div[3]/div/a/span')
elementClenskaSekce.click()


elementPrihlasit = driver.find_element_by_xpath('//*[@id="eluid27ec4dbb0"]/span')
elementPrihlasit.click()

sleep(3)

elementUserPass = driver.find_element_by_id("user_pass")
elementUserPass.send_keys("test")


elementPrihlasit = driver.find_element_by_id("wp-submit")
elementPrihlasit.click()

sleep(3)

elementUserLogin = driver.find_element_by_id("user_login")
elementUserLogin.send_keys("test")


elementPrihlasit = driver.find_element_by_id("wp-submit")
elementPrihlasit.click()

sleep(3)


elementUserPass = driver.find_element_by_id("user_pass")
elementUserPass.send_keys("test")


elementPrihlasit = driver.find_element_by_id("wp-submit")
elementPrihlasit.click()
sleep(3)

driver.close()
