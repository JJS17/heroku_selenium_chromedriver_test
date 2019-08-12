import os
from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.binary_location=os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')

driver=webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'),chrome_options=chrome_options)

driver.get("https://www.airbnb.co.uk/s/rawai/all?refinement_paths%5B%5D=%2Ffor_you&place_id=ChIJJdeIwxnXTzAR3POh80EtQlI")

print(driver.page_source)
