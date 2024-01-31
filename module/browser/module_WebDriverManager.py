from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import threading
import os
from WebAction import FacebookActions
import utils.config as config
class WebDriverManager:
    def __init__(self):
        self.threads = []

    def initialize_webdriver(self, folder_name):
        options = webdriver.ChromeOptions()
        path = os.path.join(os.getcwd(), f'profile\\{folder_name}')
        options.add_argument(f"user-data-dir={path}")
        print(path)
        service = Service(config.env["driver"])  # Path to your chrome profile
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def run_instance(self, profile_path, website_actions, user_tasks):
        driver = self.initialize_webdriver(profile_path)
        website_actions.perform_actions(driver, user_tasks.get(profile_path, {}))
        driver.quit()

    def create_threads(self, user_tasks, website_actions):
        for profile_path in user_tasks.keys():
            thread = threading.Thread(target=self.run_instance, args=(profile_path, website_actions, user_tasks))
            self.threads.append(thread)

    def start_threads(self):
        for thread in self.threads:
            thread.start()

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()

# Example usage:
            
user_tasks = {
    "SokunPanha": {"action": "active", "params": {"email": "sokunpanha.panha@gmail.com","password":"Raksa@#$"}},
    # "john": {"action": "post", "params": {"username": "https://www.youtube.com/"}},
}

# Create an instance of the WebsiteActions class for Facebook
facebook_actions = FacebookActions()

# Create an instance of the WebDriverManager class
web_driver_manager = WebDriverManager()

# Create threads for each user and perform Facebook actions
web_driver_manager.create_threads(user_tasks, facebook_actions)

# Start the threads
web_driver_manager.start_threads()

# Wait for all threads to finish
web_driver_manager.wait_for_threads()
