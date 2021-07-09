import os
import glob
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


# Get files from input folder
input_folder = 'input'
list_off_files = glob.glob(f"{os.getcwd()}/{input_folder}/*")

# Fire-up the browser

ezgif = "https://ezgif.com/video-to-webp"

browser_data_location = "browser_data"
options = webdriver.ChromeOptions()
options.add_argument(f'user-data-dir={os.getcwd()}/{browser_data_location}')

upload_box_css = "#new-image"
upload_button_xpath = '//*[@id="tool-submit-button"]/input'
convert_button_xpath = '//*[@id="tool-submit-button"]/input'
save_button_xpath = '//*[@id="output"]/table/tbody/tr[2]/td[7]/a/span/img'

with webdriver.Chrome(options=options, ) as driver:
    wait = WebDriverWait(driver, 10)
    for file in list_off_files:
        driver.get(ezgif)
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, upload_box_css))).send_keys(file)
        wait.until(ec.element_to_be_clickable((By.XPATH, upload_button_xpath))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, convert_button_xpath))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, save_button_xpath))).click()
        print(f"{list_off_files.index(file) + 1} files are converted...")
        if list_off_files[-1] == file:
            time.sleep(60)
            print("All files are downloaded!")
