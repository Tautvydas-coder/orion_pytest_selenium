from selenium.webdriver.common.by import By
from resources.variables import *
from driver_services.service import *

# driver = driver_service_mozila()
driver = driver_service_chrome()


def setup():
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(ORION_WEB)
    driver.find_element(By.ID, Cookies).click()



def teardown():
    driver.close()
    driver.quit()
    print("Test Completed")
