from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

# open youtube
driver.get("https://www.youtube.com/")
driver.maximize_window()
sleep(3)

# locate search box using NAME locator
driver.find_element(By.NAME, "search_query").send_keys("melody hits")

sleep(5)
driver.quit()