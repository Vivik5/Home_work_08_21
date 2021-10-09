import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_weather_chrome_1120х550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get("https://qasvus.wixsite.com/ca-marketing")
        time.sleep(3)  # simulate long running test

        print(driver_chrome.find_element(By.XPATH,
             "//a[@href='https://qasvus.wixsite.com/ca-marketing'][contains(.,'CALIFORNIA MARCKETING')]")
              .get_attribute("href"))
        print(driver_chrome.find_element(By.XPATH, "//img[contains(@src,'sq.webp')]").get_attribute("src"))

        assert "Home | California Marcketing" in driver_chrome.title
        print("Home | California Marcketing", driver_chrome.title)

        time.sleep(2)
        driver_chrome.find_element(By.XPATH, "//form[@id='comp-k00d77rh']")
        driver_chrome.find_element(By.ID, "input_comp-k00d77t1").clear()
        driver_chrome.find_element(By.ID, "input_comp-k00d77t1").send_keys('aaa')
        driver_chrome.find_element(By.ID, "input_comp-k00d77ti").clear()
        driver_chrome.find_element(By.ID, "input_comp-k00d77ti").send_keys("123-@gmail.com")
        driver_chrome.find_element(By.ID, "input_comp-k00d77tz").clear()
        driver_chrome.find_element(By.ID, "input_comp-k00d77tz").send_keys("bbb")
        driver_chrome.find_element(By.ID, "textarea_comp-k00d77uc").clear()
        driver_chrome.find_element(By.ID, "textarea_comp-k00d77uc").send_keys("Hi. I'm aaa.")
        #driver_chrome.implicitly_wait(1)
        wait = WebDriverWait(driver_chrome, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Submid')]")))

        driver_chrome.find_element_by_xpath("//button[contains(.,'Submid')]").click()
        time.sleep(2)
        driver_chrome.find_element_by_class_name("_26OVl").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()  # Close the browser.


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search_weather_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get("https://qasvus.wixsite.com/ca-marketing")
        time.sleep(5)  # simulate long running test

        print(driver_firefox.find_element(By.XPATH,
             "//a[@href='https://qasvus.wixsite.com/ca-marketing'][contains(.,'CALIFORNIA MARCKETING')]")
              .get_attribute("href"))
        print(driver_firefox.find_element(By.XPATH, "//img[contains(@src,'sq.webp')]").get_attribute("src"))

        assert "Home | California Marcketing" in driver_firefox.title
        print("Home | California Marcketing", driver_firefox.title)

        time.sleep(2)
        driver_firefox.find_element(By.XPATH, "//form[@id='comp-k00d77rh']")
        driver_firefox.find_element(By.ID, "input_comp-k00d77t1").clear()
        driver_firefox.find_element(By.ID, "input_comp-k00d77t1").send_keys('aaa')
        driver_firefox.find_element(By.ID, "input_comp-k00d77ti").clear()
        driver_firefox.find_element(By.ID, "input_comp-k00d77ti").send_keys("123-@gmail.com")
        driver_firefox.find_element(By.ID, "input_comp-k00d77tz").clear()
        driver_firefox.find_element(By.ID, "input_comp-k00d77tz").send_keys("bbb")
        driver_firefox.find_element(By.ID, "textarea_comp-k00d77uc").clear()
        driver_firefox.find_element(By.ID, "textarea_comp-k00d77uc").send_keys("Hi. I'm aaa.")

        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Submid')]")))

        driver_firefox.find_element_by_xpath("//button[contains(.,'Submid')]").click()
        time.sleep(2)
        driver_firefox.find_element_by_class_name("_26OVl").click()
        time.sleep(1)

    def test_search_weather_firefox_1250x850(self):
        driver_firefox = self.driver
        driver_firefox.set_window_size(1120, 850)
        driver_firefox.get("https://qasvus.wixsite.com/ca-marketing")
        time.sleep(5)  # simulate long running test

        print(driver_firefox.find_element(By.XPATH,
             "//a[@href='https://qasvus.wixsite.com/ca-marketing'][contains(.,'CALIFORNIA MARCKETING')]")
              .get_attribute("href"))
        print(driver_firefox.find_element(By.XPATH, "//img[contains(@src,'sq.webp')]").get_attribute("src"))

        assert "Home | California Marcketing" in driver_firefox.title
        print("Home | California Marcketing", driver_firefox.title)

        time.sleep(2)
        driver_firefox.find_element(By.XPATH, "//form[@id='comp-k00d77rh']")
        driver_firefox.find_element(By.ID, "input_comp-k00d77t1").clear()
        driver_firefox.find_element(By.ID, "input_comp-k00d77t1").send_keys('aaa')
        driver_firefox.find_element(By.ID, "input_comp-k00d77ti").clear()
        driver_firefox.find_element(By.ID, "input_comp-k00d77ti").send_keys("123-@gmail.com")
        driver_firefox.find_element(By.ID, "input_comp-k00d77tz").clear()
        driver_firefox.find_element(By.ID, "input_comp-k00d77tz").send_keys("bbb")
        driver_firefox.find_element(By.ID, "textarea_comp-k00d77uc").clear()
        driver_firefox.find_element(By.ID, "textarea_comp-k00d77uc").send_keys("Hi. I'm aaa.")

        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Submid')]")))

        driver_firefox.find_element_by_xpath("//button[contains(.,'Submid')]").click()
        time.sleep(2)
        driver_firefox.find_element_by_class_name("_26OVl").click()
        time.sleep(1)

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
