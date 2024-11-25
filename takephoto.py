from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Set up Chrome options for headless operation
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/chromium-browser"  # Set the path to the Chromium binary

# Path to the ChromeDriver executable
browser_driver = Service('/usr/bin/chromedriver')

# Initialize the WebDriver with options
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Navigate to the page and perform login actions
    page_to_scrape.get("https://sip.elfak.ni.ac.rs/")


    time.sleep(5)
    responseT = page_to_scrape.find_element(By.ID, "novosti")
    
    
         # Get the size of the element
    height = responseT.size['height']
    width = responseT.size['width']

    # Set a larger window size (you can adjust these values as needed)
    # Here we set a fixed width that is larger than what might be needed.
    desired_width = max(width + 100, 1200)  # Ensure at least 1200px width
    page_to_scrape.set_window_size(desired_width, height * 0.4)  # Adding some extra space

    # Scroll to make sure the element is visible in case it's off-screen
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseT)

    # Take a screenshot of the entire element
    responseT.screenshot('sip-nova-obavestenja.png')
  

finally:
    # Clean up by quitting the driver
    page_to_scrape.quit()
