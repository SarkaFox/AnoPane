from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://digitalninomadstvi.cz")

sleep(5)

driver.close()
