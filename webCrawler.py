from string import ascii_letters
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
from datetime import datetime

#import text
from datetime import datetime
import sys
from sys import exit



# Set the path to the ChromeDriver executable
chromedriver_path = r'C:\Users\kasiiyer\OneDrive - Advanced Micro Devices Inc\Desktop\Sel\chromedriver.exe';
geckodriver_path = r'C:\Users\kasiiyer\OneDrive - Advanced Micro Devices Inc\Desktop\Sel\geckodriver.exe';

firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe';
# Configure Chrome options
chrome_options = Options()
firefox_options = webdriver.FirefoxOptions()
service = Service(geckodriver_path)

firefox_binary = FirefoxBinary(firefox_binary_path)
# Add any desired options here, e.g., headless mode:
# chrome_options.add_argument('--headless')
chrome_options.binary_location = chromedriver_path


with open('output.txt', 'r') as file:
    content = file.readlines()

# Initialize Chrome WebDriver with the specified options and executable path
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Firefox(service=service, options=firefox_options)

    
driver.implicitly_wait(2)
driver.maximize_window()

invite="sri"
account="srikant"
driver.maximize_window()
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
time.sleep(1)
search = driver.find_element(By.XPATH,'//*[@id="firstName"]' );
search.send_keys("Santosh")
search = driver.find_element(By.XPATH, '//*[@id="lastName"]')
search.send_keys("Iyer")
search.send_keys(Keys.ENTER);

time.sleep(15)
text="That username is taken"
text2 = "Sorry"

with open('res.txt', 'w') as file:
    for n in content:
        time.sleep(0)
        try:
            

            search = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input')
         
            search.clear()
            search.send_keys(n)

            search.send_keys(Keys.ENTER);
            time.sleep(1)
            
            
            if ('Create a strong password' in driver.page_source):
                file.write(n)
                driver.back()
                time.sleep(1)

        finally:
            pass
            