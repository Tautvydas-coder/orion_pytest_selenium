from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FoxService
from resources.variables import CHROME_DRIVER_PATH, FFOX_DRIVER_PATH


def driver_service_mozila():
    ser = FoxService(FFOX_DRIVER_PATH)
    mozila_driver = webdriver.Firefox(service=ser)
    return mozila_driver


def driver_service_chrome():
    ser = Service(CHROME_DRIVER_PATH)
    chrome_driver = webdriver.Chrome(service=ser)
    return chrome_driver
