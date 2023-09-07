import sys
import getpass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def init():
    options = FirefoxOptions()
    options.headless = True
    options.add_argument("--headless")

    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver = webdriver.Firefox(executable_path = './geckodriver',options=options)

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver = webdriver.Chrome('./chromedriver', options=options)
    return driver

def login():
    driver = init()

    Tredir='https://detectportal.firefox.com/canonical.html'  # Firefox installed
    # Tredir='https://www.gstatic.com/generate_204'               # if Chrome installed
    driver.get(Tredir)
    print(driver.page_source)
    

    username = input('IIT Mandi LDAP username: ')
    driver.find_element(By.NAME, 'username').send_keys(username)
    
    password = getpass.getpass('IIT Mandi LDAP password: ')
    driver.find_element(By.NAME, 'password').send_keys(password)

    login_form = driver.find_element(By.TAG_NAME, 'form')
    login_form.submit()

    driver.close()
    
    check()

def check():
    
    driver = init()
    driver.get('https://login.iitmandi.ac.in:1003/portal?')
    check='Authentication Successful'
    if(check in driver.page_source):
        print(check)
    else:
        print('ERRRRRROR occurred')

    driver.close()

def logout():
    driver=init()
    driver.get("https://login.iitmandi.ac.in:1003/logout?")
    driver.close()

if __name__ == "__main__":

    if len(sys.argv) < 2:
        login()
    else:
        # if(sys.argv[1]=='logout'):
        logout()
