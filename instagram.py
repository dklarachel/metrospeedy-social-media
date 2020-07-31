from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from csv_ops import get_hashtags

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

driver.get('https://instagram.com')

# login information 
username = 'metrospeedy'
password = 'Summer2017!'

def login (username, password):
    # enter username
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    username_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    username_field.click()
    username_field.send_keys(username)

    # enter password
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    password_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    password_field.click()
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN) # enter to login

    # click "not now" for notifs
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
    not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    # driver.execute_script("arguments[0].click();", not_now)
    not_now.click()

# def search_query (search_list):
#     # enter query into search bar
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[1]')))
#     search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[1]')
#     search_bar.click()
#     search_bar_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
#     search_bar_field.send_keys('#delivery')
#     search_bar_field.send_keys(Keys.RETURN)

#     # click on hashtag that was searched
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')))
#     searched_query_link = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')
#     searched_query_link.click()
#     # add something to make sure it's the right one?

#     # get post count for search query
#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span')))
#     post_count = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span')
#     post_count = post_count.text.replace(",", "")
#     print(post_count)

def search_query (search_list):
    for x in search_list:
        # enter query into search bar
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[1]')))
        search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[1]')
        search_bar.click()
        search_bar_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar_field.send_keys(x)
        search_bar_field.send_keys(Keys.RETURN)

        # click on hashtag that was searched
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')))
        searched_query_link = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')
        searched_query_link.click()
        # add something to make sure it's the right one?

        # get post count for search query
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span')))
        post_count = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span')
        post_count = post_count.text.replace(",", "")
        print(post_count)


