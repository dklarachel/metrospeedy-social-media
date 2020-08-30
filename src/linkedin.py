from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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

# def search_query (search_list):
#     results = {}
#     for x in search_list:
#         # enter query into search bar
#         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember14"]')))
#         search_bar = driver.find_element_by_xpath('//*[@id="ember14"]')
#         search_bar.click()
#         search_bar_field = driver.find_element_by_xpath('//*[@id="ember16"]/input')
#         search_bar_field.clear()
#         search_bar_field.send_keys(x)
#         search_bar_field.send_keys(Keys.RETURN)

#         # get results count for search query
#         driver.get(driver.current_url)
#         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-results__total')))
#         results_count = driver.find_element_by_class_name("search-results__total")
#         results_count = results_count.text
#         for n in ["Showing ", ",", " results"]:
#             results_count = results_count.replace(n, "")
#         results[x] = results_count
#     return results
def search_query (search_list):
    results = {}
    for x in search_list:
        # enter query into search bar
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember14"]')))
        search_bar = driver.find_element_by_xpath('//*[@id="ember14"]')
        search_bar.click()
        search_bar_field = driver.find_element_by_xpath('//*[@id="ember16"]/input')
        search_bar_field.clear()
        search_bar_field.send_keys(x)
        search_bar_field.send_keys(Keys.RETURN)

        # get results count for search query
        WebDriverWait(driver, 15).until(EC.url_changes(driver.current_url))
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-results__total')))
        # results_count = driver.find_element_by_class_name("search-results__total")
        # if not results_count:
        #     print("no posts")
        #     results[x] = '0'
        #     x = next(search_list)
        #     print(x)
        # else:
        #     print("posts")
        #     results_count = results_count.text
        #     for n in ["Showing ", ",", " results"]:
        #         results_count = results_count.replace(n, "")
        #     results[x] = results_count
        try:
            results_count = driver.find_element_by_class_name("search-results__total")
        except NoSuchElementException:
            print("No element found")
            results[x] = '0'
        else:
            print("posts")
            results_count = driver.find_element_by_class_name("search-results__total").text
            for n in ["Showing ", ",", " results"]:
                results_count = results_count.replace(n, "")
            results[x] = results_count
    return results

