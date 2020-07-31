from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from csv_ops import get_hashtags

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

driver.get('https://linkedin.com')

def login (email, password):
    # enter email
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
    email_field = driver.find_element_by_xpath('//*[@id="session_key"]')
    email_field.click()
    email_field.send_keys(email)

    # enter password
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))
    password_field = driver.find_element_by_xpath('//*[@id="session_password"]')
    password_field.click()
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN) # enter to login

    # # click "skip now" for phone number confirmation
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ember512']/button[2]")))
    # not_now = driver.find_element_by_xpath('//*[@id="ember512"]/button[2]')
    # not_now.click()

def search_query ():
    # for x in search_list:
        # enter query into search bar
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember14"]')))
    search_bar = driver.find_element_by_xpath('//*[@id="ember14"]')
    search_bar.click()
    search_bar_field = driver.find_element_by_xpath('//*[@id="ember16"]/input')
    search_bar_field.send_keys('#nyc')
    search_bar_field.send_keys(Keys.RETURN)

    # get results count for search query
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ember563"]/div/h3')))
    # results_count = driver.find_element_by_xpath('//*[@id="ember563"]/div/h3')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-results__total')))
    results_count = driver.find_element_by_class_name("search-results__total")
    results_count = results_count.text
    for x in ["Showing ", ",", " results"]:
        results_count = results_count.replace(x, "")
    print(results_count)



