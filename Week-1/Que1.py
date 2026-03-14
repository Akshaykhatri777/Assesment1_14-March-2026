from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

driver.get("https://www.facebook.com/")
driver.maximize_window()

sleep(3)

# enter email
driver.find_element(By.CSS_SELECTOR,'input[name="email"]').send_keys("example@gmail.com")

# enter password
driver.find_element(By.CSS_SELECTOR,'input[name="pass"]').send_keys("123456")

sleep(3)

# click login
driver.find_element(By.CSS_SELECTOR,'div[aria-label="Log in"]').click()
sleep(5)
driver.quit()