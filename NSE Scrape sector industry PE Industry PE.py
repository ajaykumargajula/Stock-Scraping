import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#import subprocess
import warnings
warnings.filterwarnings('ignore')
import numpy as np

tickers = pd.read_csv('https://archives.nseindia.com/content/equities/EQUITY_L.csv',usecols=['SYMBOL'])

sec ={}
for i in tickers.iterrows():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome("C:/webdriver/chromedriver",options=options)
    driver.get("https://www.nseindia.com/get-quotes/equity?symbol="+i[1][0].replace("&","%26"))
    try:
        Basic_Industry = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="equityInfo"]/tbody/tr/td[6]'))).text
        
    except:
         Basic_Industry ='NA'
    try:
        Symbol_PE = driver.find_element(By.XPATH,'//*[@id="equityInfo"]/tbody/tr/td[7]').text
    except:
        Symbol_PE = 'NA'

    try:
        SectoralIndex_PE = driver.find_element(By.XPATH,'//*[@id="equityInfo"]/tbody/tr/td[8]').text
    except:
        SectoralIndex_PE ='NA'
    try:
        SectoralIndex = driver.find_element(By.XPATH,'//*[@id="equityInfo"]/tbody/tr/td[9]').text
    except:
        SectoralIndex = 'NA'
    sec[i[1][0]] = {"Basic_Industry":Basic_Industry,"Symbol_PE":Symbol_PE,"SectoralIndex_PE":SectoralIndex_PE,"SectoralIndex":SectoralIndex}
    WebDriverWait(driver, 10)
    driver.quit()
