import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webactoion_interface import WebsiteActions
from selenium.webdriver.support import expected_conditions as EC

class FacebookActions(WebsiteActions):
    def perform_actions(self, driver, task_info):
        action = task_info.get("action")
        params = task_info.get("params", {})
        if action in self.actions_mapping:
            self.actions_mapping[action](self,driver, params)

    def scroll_facebook(self, driver, params):
        driver.get("https://www.facebook.com")
        time.sleep(100)

    def post_on_facebook(self, driver, params):
        print(params)
        driver.get(params["username"])
        time.sleep(100)

    def active_on_facebook(self, driver, params):
        post_like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Like']"))
        )
        post_like_button.click()
        time.sleep(2)  # Add a short delay for demonstration purposes

    def custom_action(self, driver, params):
        # Add your custom action logic here
        print(f"Executing custom action with parameters: {params}")

    # Define the mapping of actions to methods
    actions_mapping = {
        'scroll': scroll_facebook,
        'post': post_on_facebook,
        'active': active_on_facebook,
        'custom': custom_action,
        # Add more actions as needed
    }