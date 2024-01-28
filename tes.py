from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import time
from screeninfo import get_monitors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random

def get_screen_width():
    monitors = get_monitors()
    if monitors:
        return monitors[0].width
    else:
        return 800  # Default width if screen information is not available

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def wait_and_click(driver, by, value, timeout=10):
    element = wait_for_element(driver, by, value, timeout)
    ActionChains(driver).move_to_element(element).click().perform()
    time.sleep(random.uniform(1.0, 3.0))  # Increase delay

def wait_and_type(driver, by, value, text, timeout=20):
    element = wait_for_element(driver, by, value, timeout)

    # Wait for the element to be clickable
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.element_to_be_clickable((by, value)))

    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.2, 0.5))  # Increase delay

def run_chrome(window_size, window_position, email, password):
    options = Options()
    options.add_argument(f'--window-size={window_size}')
    options.add_argument(f'--window-position={window_position}')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://facebook.com")
    
    # wait_and_click(driver, By.XPATH, "//button[text()='sign up for free']")
    # wait_and_click(driver, By.XPATH, "//button[text()='Continue with VPN Free']")
    # time.sleep(2)
   
    # # wait_and_click(driver, By.XPATH, "Email address")
    # # driver.find_element(By.CLASS_NAME, "input-element").send_keys(email)
    # wait_and_click(driver, By.XPATH, "//button[text()='Start using Proton VPN']")
    # time.sleep(5)
    # driver.find_element(By.ID, "email").send_keys(email)
    # time.sleep(5)

    # wait_and_click(driver, By.XPATH, "//button[text()='Start using Proton VPN']")

    # wait_and_click(driver, By.XPATH, "//button[text()='Choose my own password']")
    wait_and_type(driver, By.ID, "email", email)

    wait_and_type(driver, By.ID, "pass", password)


    # Do whatever operations you need on this instance of Chrome
    time.sleep(100)  # For demonstration purposes, wait for 100 seconds
    
    driver.quit()

# Rest of the code remains the same

# Set the path to your ChromeDriver executable
# chrome_driver_path = '/path/to/chromedriver'

# URLs to open in each Chrome instance along with corresponding emails
url_email_pairs = [
    ('nhebpanha40@gmail.com', "JackSon@#$") # Add more URL-email pairs as needed
]

# Calculate the number of rows
browsers_per_row = 1  # Four browsers in each row
num_rows = (len(url_email_pairs) + browsers_per_row - 1) // browsers_per_row

# Get the screen width dynamically
screen_width = get_screen_width()

# Window size for each Chrome instance
window_width = screen_width // browsers_per_row
window_size = f'{window_width},600'  # You can adjust the height as needed

# Create threads for each Chrome instance
threads = []
for i, (email, password) in enumerate(url_email_pairs):
    row = i // browsers_per_row
    col = i % browsers_per_row
    window_position = f'{col * window_width},0'  # Assuming all browsers have the same height
    
    thread = threading.Thread(target=run_chrome, args=(window_size, window_position, email, password))
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()



# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import threading
# import time
# from screeninfo import get_monitors
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# import random

# def get_screen_width():
#     monitors = get_monitors()
#     if monitors:
#         return monitors[0].width
#     else:
#         return 800  # Default width if screen information is not available

# def run_chrome( window_size, window_position, email, password):
#     options = Options()
#     options.add_argument(f'--window-size={window_size}')
#     options.add_argument(f'--window-position={window_position}')
    
#     driver = webdriver.Chrome(options=options)
#     def move_mouse_to_element(driver, element):
#         ActionChains(driver).move_to_element(element).perform()
#         time.sleep(random.uniform(1.0, 3.0))  # Increase delay

#     def simulate_typing(element, text):
#         for char in text:
#             element.send_keys(char)
#             time.sleep(random.uniform(0.2, 0.5))  # Increase delay

#     def click_with_movement(element):
#         action = ActionChains(driver)
#         action.move_to_element(element).click().perform()
#         time.sleep(random.uniform(1.0, 3.0))  # Increase delay
    
#     driver.get("https://account.protonvpn.com/signup")
    
#     # Use the provided email for login or any other operations
#     # For example, you can locate the email input field and fill it with the provided email
#     # Replace the following line with your actual code
#     time.sleep(10)
#     click_with_movement(driver.find_element(By.XPATH, "//button[text()='sign up for free']"))
#     time.sleep(4)
#     click_with_movement(driver.find_element(By.XPATH, "//button[text()='Continue with VPN Free']"))
#     time.sleep(4)

#     simulate_typing(driver.find_element(By.ID, "email"), email)
#     time.sleep(4)
  
#     click_with_movement(driver.find_element(By.XPATH, "//button[text()='Start using Proton VPN']"))
#     time.sleep(4)

#     click_with_movement(driver.find_element(By.XPATH, "//button[text()='Choose my own password']"))
#     simulate_typing(driver.find_element(By.ID, "password"), password)
#     simulate_typing(driver.find_element(By.ID, "password-repeat"), password)

    
   
#     # Do whatever operations you need on this instance of Chrome
#     time.sleep(100)  # For demonstration purposes, wait for 100 seconds
    
#     driver.quit()

# # Set the path to your ChromeDriver executable
# # chrome_driver_path = '/path/to/chromedriver'

# # URLs to open in each Chrome instance along with corresponding emails
# url_email_pairs = [
#     ('nhebpanha40@gmail.com',"JackSon@#$"), # Add more URL-email pairs as needed
# ]

# # Calculate the number of rows
# browsers_per_row = 4  # Four browsers in each row
# num_rows = (len(url_email_pairs) + browsers_per_row - 1) // browsers_per_row

# # Get the screen width dynamically
# screen_width = get_screen_width()

# # Window size for each Chrome instance
# window_width = screen_width // browsers_per_row
# window_size = f'{window_width},400'  # You can adjust the height as needed

# # Create threads for each Chrome instance
# threads = []
# for i, (email, password) in enumerate(url_email_pairs):
#     row = i // browsers_per_row
#     col = i % browsers_per_row
#     window_position = f'{col * window_width},0'  # Assuming all browsers have the same height
    
#     thread = threading.Thread(target=run_chrome, args=(window_size, window_position, email, password))
#     threads.append(thread)

# # Start the threads
# for thread in threads:
#     thread.start()

# # Wait for all threads to finish
# for thread in threads:
#     thread.join()
