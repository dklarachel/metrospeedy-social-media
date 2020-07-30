from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.interactions import Actions

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

# # options = webdriver.Options()
# # options.add_argument('--ignore-certificate-errors')
# # options.add_argument("--test-type")
# # options.binary_location = "/usr/bin/chromium"
# # driver = webdriver.Chrome(chrome_options=options)
# driver.get('https://instagram.com')

driver.get('https://instagram.com')

# login information 
username = 'metrospeedy'
password = 'Summer2017!'

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
password_field.send_keys(Keys.RETURN)

# click login button
# login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
# login_button.click()

# click "not now" for notifs
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
# driver.execute_script("arguments[0].click();", not_now)
not_now.click()

# enter query into search bar
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[1]')))
search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[1]')
search_bar.click()
search_bar_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar_field.send_keys('#delivery')
search_bar_field.send_keys(Keys.RETURN)



