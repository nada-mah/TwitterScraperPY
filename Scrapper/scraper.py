import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from scraper import get_profile

def get_profile(Account_list): 
    resp = []
    options = ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    for url in Account_list:
        driver.get(url)
        # try:
        #     x = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/login'] span > span")))
        # except:
        #     x = None
        # if x:
        #     x.click()    
        #     username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
        #     username.send_keys("olive727963")
        #     username.send_keys(Keys.ENTER)

        #     password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
        #     password.send_keys("ujbnAufk%pg7!Bw")
        #     password.send_keys(Keys.ENTER)
            # time.sleep(5)   
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(5)
        resp.append(driver.page_source)
    driver.close()
    return resp

def get_data(Account_list,Ticker,Interval):
    x=0
    if Account_list:
        resp = get_profile(Account_list)
        for profile in resp:
            soup=BeautifulSoup(profile,'html.parser')

            try:
                tweets = [p.text for p in soup.findAll("article",{"data-testid":"tweet"})]
            except:
                tweets = None

            for tweet in tweets:
                x += tweet.count(Ticker)

        print(f'{Ticker} was mentioned {x} times in the last {Interval} minutes.”')