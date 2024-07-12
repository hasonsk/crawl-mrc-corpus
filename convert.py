from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from config import CHROME_DRIVER_PATH

service = Service(CHROME_DRIVER_PATH)

links = []
urls = []
error_links = []
CNN_LINKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'new_urls.txt')
ARCHIVED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archived_urls.txt')

with open(CNN_LINKS_FILE, 'r') as file:
    for line in file:
        links.append(line.strip())  # Strip any extra whitespace

driver = webdriver.Chrome(service=service)
i = 0

try:
    for link in links[1850:2000]:
        driver.get("https://web.archive.org/save/")

        try:
            input_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "web-save-url-input"))
            )
            input_element.clear()
            input_element.send_keys(link)
            input_element.send_keys(Keys.ENTER)

            time.sleep(5)
            element = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.XPATH, ".//div[@id='spn-result']//a"))
            )
            href_value = element.get_attribute("href")
            urls.append(href_value)
            i += 1
            print(i)

        except Exception as e:
            print(f"Error processing link {link}")
            error_links.append(link)
            continue

except KeyboardInterrupt:
    print("Process interrupted by user. Saving progress...")

finally:
    driver.quit()

    # Save the results to a file
    with open(ARCHIVED_FILE, 'a+') as file:
        for url in urls:
            file.write(url + "\n")
    print(f"{len(urls)} URLs saved to file.")
