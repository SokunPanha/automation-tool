from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time


class WebDriverHelper:
    def wait_for_element(self, driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_and_click(self, driver, by, value, timeout=10):
        element = self.wait_for_element(driver, by, value, timeout)

        # Simulate more human-like click
        action = ActionChains(driver)
        action.move_to_element(element).click().perform()

        time.sleep(random.uniform(0, 1.0))  # Increase delay

    def wait_and_type(self, driver, by, value, text, timeout=20):
        element = self.wait_for_element(driver, by, value, timeout)

        # Wait for the element to be clickable
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.element_to_be_clickable((by, value)))

        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.2, 0.5))
        time.sleep(random.uniform(0, 1.0))  # Increase delay
          # Increase delay
