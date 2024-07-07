from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys
import io
import config
# Đặt mã hóa của luồng đầu ra tiêu chuẩn thành UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Cấu hình ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Chạy Chrome ở chế độ headless
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Đường dẫn đến ChromeDriver
service = Service(config.CHROME_DRIVER_PATH)  # Thay thế đường dẫn đến chromedriver của bạn

# Tạo đối tượng trình duyệt
driver = webdriver.Chrome(service=service, options=chrome_options)

urls = [
    # "https://edition.cnn.com/2024/07/05/europe/france-le-pen-ukraine-mbappe-intl-cmd/index.html",
    "https://edition.cnn.com/2024/07/06/climate/italy-sicily-water-shortage-drought-tourism-intl/index.html",
    # "https://edition.cnn.com/2024/07/05/entertainment/kevin-bacon-disguise-normal-person-sucked/index.html"
]

for url in urls:
    driver.get(url)
    
    # Tìm tất cả các thẻ a có class phù hợp
    elements = driver.find_elements(By.CLASS_NAME, "card.container__item.container__item--type-media-image.container__item--type-.container_list-headlines-with-read-times__item.container_list-headlines-with-read-times__item--type-")
    # In ra giá trị của thuộc tính href cho mỗi thẻ a tìm được
    for element in elements:
        href = element.get_attribute('data-open-link')
        print(href)

# Đóng trình duyệt
driver.quit()
