from time import sleep

driver = webdriver.Chrome()
driver.get("https://digitalninomadstvi.cz")

sleep(3)
HomeURL = "https://digitalninomadstvi.cz"
driver.get(HomeURL)

sleep(1)

elementCestovani = driver.find_element_by_xpath('//*[@id="menu-item-6330"]/a')
# if(element.is_displayed())
elementCestovani.click()

sleep(1)
driver.back()
sleep(2)

elementPodcast = driver.find_element_by_xpath('//*[@id="menu-item-9441"]/a')
elementPodcast.click()

sleep(1)
driver.back()
sleep(1)
driver.close()
