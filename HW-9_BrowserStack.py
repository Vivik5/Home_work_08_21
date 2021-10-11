import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
import My_URL
import Helpers_HW_9 as HP

caps = [{
        'os_version': '10',
        'os': 'Windows',
        'browser': 'Firefox',
        'browser_version': 'latest',
        'name': 'Parallel Test2',  # test name
        'build': 'BStack-[Python] Sample Build'
    },
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'Parallel Test3',  # test name
        'build': 'BStack-[Python] Sample Build'
    },
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'Firefox',
        'browser_version': 'latest',
        'name': 'Parallel Test3',  # test name
        'build': 'BStack-[Python] Sample Build'
    }]


def run_session(desired_cap):
    driver = webdriver.Remote(
        command_executor=My_URL.key,
        desired_capabilities=desired_cap)

    driver.get("https://qasvus.wixsite.com/ca-marketing")
    driver.maximize_window()
    time.sleep(3)

    print(driver.find_element(By.XPATH, HP.elm1).get_attribute("href"))
    print(driver.find_element(By.XPATH, "//img[contains(@src,'sq.webp')]").get_attribute("src"))

    assert "Home | California Marcketing" in driver.title
    print("Home | California Marcketing", driver.title)

    time.sleep(2)
    driver.find_element(By.XPATH, "//form[@id='comp-k00d77rh']")
    driver.find_element(By.ID, "input_comp-k00d77t1").clear()
    driver.find_element(By.ID, "input_comp-k00d77t1").send_keys('aaa')
    driver.find_element(By.ID, "input_comp-k00d77ti").clear()
    driver.find_element(By.ID, "input_comp-k00d77ti").send_keys("123-@gmail.com")
    driver.find_element(By.ID, "input_comp-k00d77tz").clear()
    driver.find_element(By.ID, "input_comp-k00d77tz").send_keys("bbb")
    driver.find_element(By.ID, "textarea_comp-k00d77uc").clear()
    driver.find_element(By.ID, "textarea_comp-k00d77uc").send_keys("Hi. I'm aaa.")

    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, HP.btm1)))

    driver.find_element_by_xpath(HP.btm1).click()
    time.sleep(2)
    driver.find_element_by_class_name("_26OVl").click()
    time.sleep(1)

    driver.quit()

for cap in caps:
    Thread(target=run_session, args=(cap,)).start()
