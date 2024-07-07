# Thuc hien lay cac url tu cac bai viet tren trang CNN
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import config

FILE_PATH = os.path.join(os.getcwd(), "cnn_links.txt")

def write_links_to_file(links, file_path):
    with open(file_path, 'a+', encoding='utf-8') as file:
        for link in links:
            if not link.startswith("http"):
                file.write(f"https://edition.cnn.com{link}\n")
                
                
def scrape_cnn_articles():
    service = Service(config.CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    categories = [
        '', 'health', 'us', 'world', 'politics', 'business', 'opinion', 
        'entertainment', 'style', 'travel', 'sports', 'climate', 'weather'
    ]
    links = []

    for category in categories:
        driver.get(f"https://edition.cnn.com/{category}")
        time.sleep(5)
        # Find all div elements with the attribute data-open-link
        elements = driver.find_elements(By.CSS_SELECTOR, "div[data-open-link]")
        # Extract the values of data-open-link and add them to the links list
        for element in elements:
            temp = element.get_attribute("data-open-link")
            if "video" not in temp:
                links.append(temp)

    write_links_to_file(links, FILE_PATH)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    scrape_cnn_articles()