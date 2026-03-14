from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(3)
driver.find_element(By.CLASS_NAME, "desktop-searchBar").send_keys("shoes")
sleep(5)
driver.quit()