import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .module_webaction_interface import WebsiteActions
from selenium.webdriver.support import expected_conditions as EC
from utils import WebDriverHelper

class FacebookActions(WebsiteActions):
    def perform_actions(self, driver, task_info):
        self.bot = WebDriverHelper()
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

# Add a short delay for demonstration purposes
    def login(self, driver, params):
        driver.get("https://www.facebook.com")
        time.sleep(random.uniform(0.5, 0.1))
        self.bot.wait_and_type(driver, By.ID, "email",params["email"])
        self.bot.wait_and_type(driver, By.ID, "pass",params["password"])
        self.bot.wait_and_click(driver, By.XPATH, "//button[text()='Log In']")
        time.sleep(400)
    def wait_for_content_load(self, driver, timeout=10):
        # Wait for the document.readyState to be 'complete'
        WebDriverWait(driver, timeout).until(lambda d: driver.execute_script("return document.readyState") == "complete")

    def active_on_facebook(self, driver, scrolling=True):
        # Wait for the initial content to load before starting scrolling
        driver.get("https://www.facebook.com")
        self.wait_for_content_load(driver)

        def smooth_scroll(scroll_direction, pixels_to_scroll):
            duration = random.uniform(0.8, 1.5)  # Randomize the duration of the scroll
            current_scroll_y = driver.execute_script("return window.scrollY")
            end = current_scroll_y + pixels_to_scroll if scroll_direction == "down" else current_scroll_y - pixels_to_scroll
            
            script = f"""
                var start = window.scrollY;
                var end = {end};
                var startTime = performance.now();

                function scroll() {{
                    var currentTime = performance.now();
                    var progress = (currentTime - startTime) / ({duration * 1000});

                    if (progress < 1) {{
                        window.scrollTo(0, start + progress * (end - start));
                        requestAnimationFrame(scroll);
                    }} else {{
                        window.scrollTo(0, end);
                    }}
                }}

                scroll();
            """
            driver.execute_script(script)

        while scrolling:
            # Randomly determine whether to scroll up, down, or not at all
            scroll_decision = random.choices(["up", "down", "none"], weights=[0.1, 0.5, 0.4])[0]

            if scroll_decision == "up":
                # Scroll up with a faster speed
                pixels_to_scroll = int(random.uniform(3000, 8000) / 10)
                smooth_scroll("up", pixels_to_scroll)
            elif scroll_decision == "down":
                # Scroll down with a faster speed
                pixels_to_scroll = int(random.uniform(3000, 8000) / 10)
                smooth_scroll("down", pixels_to_scroll)

            time.sleep(random.uniform(1, 2))  # Random delay between scrolls

            # Wait for content to load before continuing
            self.wait_for_content_load(driver)

            # Use WebDriverWait to wait for the stopping condition
            try:
                WebDriverWait(driver, 10).until(scrolling)
                print("Stopping condition met. Exiting scroll loop.")
                break
            except:
                pass

    def custom_action(self, driver, params):
        # Add your custom action logic here
        print(f"Executing custom action with parameters: {params}")

    # Define the mapping of actions to methods
    actions_mapping = {
        'scroll': scroll_facebook,
        'post': post_on_facebook,
        'active': active_on_facebook,
        'custom': custom_action,
        "login" : login
        # Add more actions as needed
    }