from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.naukri.com/")
driver.maximize_window()
sleep(3)
driver.get("https://www.naukri.com/registration/createAccount")
sleep(3)
driver.find_element(By.ID,"name").send_keys("Akshay Khatri")
sleep(1)
driver.find_element(By.ID,"email").send_keys("akshay123@gmail.com")
sleep(1)
driver.find_element(By.ID,"password").send_keys("Test@1234")
sleep(5)
driver.quit()