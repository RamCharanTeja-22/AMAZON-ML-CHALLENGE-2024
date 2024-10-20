from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# Chrome options setup
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=your_user_agent_here")

# Set download directory preferences
download_dir = r"C:\Users\NL Swathi\Desktop\INFOSYS_PROJECT\downloads"
prefs = {
    "download.default_directory": os.path.abspath(download_dir),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# Specify Chrome WebDriver path
service = Service(r"C:\chrome\chromedriver-win64\chromedriver.exe") 
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.nseindia.com/all-reports")
    time.sleep(20)  # Adjust time for page to load

    # Locate the report section
    report_div = driver.find_element(By.XPATH, "//div[@id='cr_equity_daily_Current']")
    report_divs = report_div.find_elements(By.XPATH, ".//div[contains(@class, 'reportsDownload')]")

    for report in report_divs:
        data_link = report.get_attribute("data-link")
        print(f"Downloading from: {data_link}")
        driver.get(data_link)
        time.sleep(5)  # Allow time for the download to complete

finally:
    driver.quit()
