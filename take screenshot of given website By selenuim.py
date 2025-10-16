from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


URL = input("Enter URL: ")

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


driver.get(URL)

filename =input("enter your screenshot name")
driver.save_screenshot(filename)
print(f"Screenshot saved as {filename}")

driver.quit()