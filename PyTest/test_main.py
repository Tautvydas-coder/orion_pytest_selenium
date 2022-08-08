import time
import pyautogui
import os
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from resources.variables import *
from driver_services.service import *
from selenium.webdriver.support import expected_conditions as EC

# driver = driver_service_mozila()
driver = driver_service_chrome()


def setup():
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(ORION_WEB)
    time.sleep(1)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, Cookies))).click()
    time.sleep(1)


# def test_HeadersDropdownButton():
#     header = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"/html/body/header")))
#     element = driver.find_element(By.ID, COMPANY)
#     dropdown = driver.find_element(By.LINK_TEXT, CAREERS)
#     ActionChains(driver).move_to_element(header).move_to_element(element).move_to_element(dropdown).click().perform()
#     web_title = driver.title
#     assert web_title == "Careers - Orion Innovation"


# def test_MajorDeliveryCentersValue():
#     MaturityAndScale = driver.find_element(By.XPATH,'//*[@id="h-maturity-scale"]')
#     ActionChains(driver).scroll_to_element(MaturityAndScale).perform()
#     element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="number-block-block_5defc5f643e72"]/div[1]')))
#     time.sleep(3)
#     number = element.text
#     assert number == "14"

# def test_countrySelection():
#     agree_field = driver.find_element(By.XPATH, '//*[@id="field_1_12"]')
#     select_element = driver.find_element(By.XPATH, '//*[@id="field_1_9"]/div/div')
#     ActionChains(driver).scroll_to_element(agree_field).perform()
#     ActionChains(driver).move_to_element(select_element).click().perform()
#     selected_country = driver.find_element(By.XPATH, '//*[@id="field_1_9"]/div/div/div[3]/div/ul/li[4]')
#     ActionChains(driver).move_to_element(selected_country).click().perform()
#     country = driver.find_element(By.XPATH,
#                                   '/html/body/main/div[2]/div/div/div/div[2]/div/form/div[2]/ul/li[7]/div/div/div[2]/span')
#     assert country.text == "Algeria"

def test_uploadCV():
    driver.get('https://www.orioninc.com/careers/job-application/?job_id=13746')
    time.sleep(2)
    save_info = driver.find_element(By.XPATH, '//*[@id="label_7_13_1"]')
    ActionChains(driver).scroll_to_element(save_info).perform()
    upload = driver.find_element(By.XPATH, '//*[@id="input_7_12"]')
    upload.send_keys("C:\\Users\\takvietk\\Desktop\\git-cheat-sheet-education.pdf")
    cv_name = driver.find_element(By.XPATH, '//*[@id="gfield_description_7_12"]')
    cv_name_text = cv_name.text
    assert cv_name_text.__contains__("git")


# def teardown():
#     driver.close()
#     driver.quit()
#     print("Test Completed")
