from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.wait import WebDriverWait

phrase = input("Search here: ")  #get user input


def get_metrolinks(user_query):
    """This module fetches useful links for financial planning ie savings"""
    path = Service("/home/magondu/Downloads/chromedriver_linux64/chromedriver")  # set the chrome driver PATH
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # For maximizing window
    url = "https://www.metrosacco.co.ke/"
    driver.get(url)
    search = driver.find_element(By.XPATH, '//*[@id="medium-searchform"]/form/input')
    # driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
    # print("Element is visible? " + str(search.is_displayed()))
    search.send_keys(user_query)
    search.send_keys(Keys.RETURN)
    time.sleep(90)


get_metrolinks(phrase)

def co_oplinks(user_query):
    path = Service("/home/magondu/Downloads/chromedriver_linux64/chromedriver")  # set the chrome driver PATH
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # For maximizing window
    url = "https://www.co-opbank.co.ke/search"
    driver.get(url)
    search = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[4]/div[2]/div/div/form/input')
    # driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
    # print("Element is visible? " + str(search.is_displayed()))
    search.send_keys(user_query)
    search.send_keys(Keys.RETURN)
    time.sleep(90)


co_oplinks(phrase)

def bit_pesa(user_query):
    path = Service("/home/magondu/Downloads/chromedriver_linux64/chromedriver")  # set the chrome driver PATH
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()  # For maximizing window
    url = "https://help.bitpesa.co/en/"
    driver.get(url)
    search = driver.find_element(By.XPATH, '/html/body/header/div/div/form/input')
    # driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
    # print("Element is visible? " + str(search.is_displayed()))
    search.send_keys(user_query)
    search.send_keys(Keys.RETURN)
    time.sleep(90)

bit_pesa(phrase)