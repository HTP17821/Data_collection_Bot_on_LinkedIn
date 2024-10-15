import os
import time
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Task 1: Log into LinkedIn
driver = webdriver.Chrome()  
sleep(3)  
url = 'https://www.linkedin.com/login'  
driver.get(url)  
print('- Browser initialized successfully')
sleep(3)  

# Read login information from file
with open('Login_info.txt') as credential:
    line = credential.readlines()
    username = line[0].strip()  
    password = line[1].strip()

print('- Login information successfully imported')
sleep(2)

# Enter username and password
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(username)
print('- Email entered successfully')
sleep(2)

password_field = driver.find_element(By.NAME, 'session_password')
password_field.send_keys(password)
print('- Password entered successfully')
sleep(2)

# Click the login button
signin_field = driver.find_element(By.XPATH, '//button[@type="submit"]')
signin_field.click()
sleep(2)
print('- Task 1 completed: Logged into LinkedIn')

# Task 2: Search for profiles to crawl
wait = WebDriverWait(driver, 10)  

# Fixed search keyword
search_query = 'data engineer'  # Từ khóa tìm kiếm cố định
search_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Search"]')))
search_field.send_keys(search_query)  
search_field.send_keys(Keys.RETURN)  
sleep(3)  
print('- Task 2 completed: Search performed')

# Task 3: Crawl the profile URLs found
signin_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button'))
)
signin_field.click() 
sleep(2)
print('- Task 3.0 completed: Clicked the People button')

# Task 4: Function to extract URLs from a profile page
def GetURL():
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    profiles = page_source.find_all('a', class_='app-aware-link')
    all_profile_URL = []

    for profile in profiles:
        profile_URL = profile.get('href')
        if profile_URL and "/in/" in profile_URL:
            if profile_URL not in all_profile_URL:
                all_profile_URL.append(profile_URL)
    return all_profile_URL  

# Fixed number of pages to scrape
input_page = 2  # Số trang cần cào cố định
URLs_all_page = []  

for page in range(input_page):
    URLs_one_page = GetURL()  
    sleep(2)  
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  
    sleep(1)  
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-pagination__button--next"))
    )
    driver.execute_script("arguments[0].click();", next_button)
    URLs_all_page += URLs_one_page  
    sleep(4)  

print('- Task 4 completed: Crawled URLs from all pages')
for url in URLs_all_page:
    print(url)  

# Task 5: Save data to an Excel file
excel_filename = 'profile_data.xlsx'  

if os.path.exists(excel_filename):
    os.remove(excel_filename)  
    print(f'Deleted file: {excel_filename}')
else:
    print(f'No file to delete: {excel_filename}')  

data = [] 

for linkedin_URL in URLs_all_page:
    driver.get(linkedin_URL)  
    print('- Accessing profile: ', linkedin_URL)
    time.sleep(2)  
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    name_elem = page_source.find('h1', class_='text-heading-xlarge')
    name = name_elem.get_text().strip() if name_elem else None
    print('--- Profile name: ', name)
    title_elem = page_source.find('div', class_='text-body-medium break-words')
    title = title_elem.get_text().strip() if title_elem else None
    print('--- Job title: ', title)
    location_elem = page_source.find('span', class_='text-body-small inline t-black--light break-words')
    location = location_elem.get_text().strip() if location_elem else None
    print('--- Location: ', location)
    data.append({
        'Name': name,
        'Job Title': title,
        'Location': location,
        'URL': linkedin_URL
    })
    print('\n')  

df = pd.DataFrame(data)  
df.to_excel(excel_filename, index=False)  

print('Task completed!')  
