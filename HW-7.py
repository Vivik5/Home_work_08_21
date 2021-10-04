from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://qasvus.wixsite.com/ca-marketing")
driver.maximize_window()

print(driver.find_element(By.XPATH, "//a[@href='https://qasvus.wixsite.com/ca-marketing'][contains(.,'CALIFORNIA MARCKETING')]").get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[contains(@src,'sq.webp')]").get_attribute("src"))

assert "Home | California Marcketing" in driver.title
print("Home | California Marcketing", driver.title)

time.sleep(2)
driver.find_element(By.XPATH, "//form[@id='comp-k00d77rh']")
driver.find_element(By.ID, "input_comp-k00d77t1").send_keys('aaa')
driver.find_element(By.ID, "input_comp-k00d77ti").send_keys("123-@gmail.com")
driver.find_element(By.ID, "input_comp-k00d77tz").send_keys("bbb")
driver.find_element(By.ID, "textarea_comp-k00d77uc").send_keys("Hi. I'm aaa.")

driver.implicitly_wait(1)
driver.find_element_by_xpath("//button[contains(.,'Submid')]").click()

time.sleep(2)
driver.find_element_by_class_name("_26OVl").click()

driver.quit()
