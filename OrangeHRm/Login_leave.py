from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup ChromeDriver
serv_obj = Service("D:/Webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

try:
    # Open the URL and maximize the window
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    # Wait for the page to load and elements to appear
    wait = WebDriverWait(driver, 10)

    # Enter username
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
    username_field.send_keys("admin")

    # Enter password
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
    password_field.send_keys("admin123")

    # Click the Login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
    login_button.click()

    # Verify the page title
    wait.until(EC.title_is("OrangeHRM"))
    act_title = driver.title
    exp_title = "OrangeHRM"

    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login Test Failed")

except TimeoutException as e:
    print(f"Test Failed due to TimeoutException: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
