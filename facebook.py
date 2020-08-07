from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from csv_ops import get_hashtags
from math_ops import numerize

import time

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

driver = webdriver.Chrome(options=option, executable_path='chromedriver.exe')
driver.maximize_window()

driver.get('https://facebook.com')

def login (email, password):
    # enter email
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    email_field = driver.find_element_by_xpath('//*[@id="email"]')
    email_field.click()
    email_field.send_keys(email)

    # enter password
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
    password_field = driver.find_element_by_xpath('//*[@id="pass"]')
    password_field.click()
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN) # enter to login

def search_query (search_list):
    results = {}
    for x in search_list:
        # enter query into search bar
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, '_1frb')))
        search_bar = driver.find_element_by_class_name('_1frb')
        search_bar.click()
        search_bar_field = driver.find_element_by_class_name('_1frb')
        #search_bar_field.clear()
        search_bar_field.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        search_bar_field.send_keys(x)

        # find the right link to click
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, '_19bs')))
        query_list = driver.find_elements_by_class_name('_19bs')
        for query in query_list:
            if query.text == x:
                query_link = query
                break

        # click on hashtag link
        query_link.click()

        # get results for search query 
        driver.refresh()
        query_link_selector = '#content > div > div > div > div:nth-child(1) > div > div > div > div > div > div > div > div.dsne8k7f > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.ihqw7lf3.cddn0xzi > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.on77hlbc.buofh1pr.g5gj957u.hpfvmrgz.o8rfisnq.ph5uu5jm.b3onmgus.ihqw7lf3.ecm0bbzt > div > div > div:nth-child(2) > span'
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, query_link_selector)))
            results_count = driver.find_element_by_css_selector(query_link_selector)
        except NoSuchElementException:
            print("No element found")
            results_count = 0
        else:
            print("we have posts!")
            results_count = driver.find_element_by_css_selector(query_link_selector).text
            if "Explore" in results_count:
                results_count = 0
            else: 
                results_count = results_count.replace(" people are talking about this", "")
                if not results_count.isdigit():
                    results_count = numerize(results_count)
        results[x] = results_count
        print(results_count)
    return results

login(
    email = "rachlin232@gmail.com",
    password = "pastelepix4"
)

search_query(
    search_list = get_hashtags()
)