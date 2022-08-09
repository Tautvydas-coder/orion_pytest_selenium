import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from resources.variables import *
from driver_services.service import *
from selenium.webdriver.support import expected_conditions as EC
import pytest


# TODO kiekvienas testas suveiktu random atskirai

@pytest.fixture()
def setup():
    global driver
    driver = driver_service_chrome()
    # driver = driver_service_mozila()
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(ORION_WEB)
    time.sleep(1)
    cookies_accept = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, Cookies)))
    cookies_accept.click()
    time.sleep(1)
    yield
    driver.close()
    driver.quit()
    print("Test Completed")


@pytest.mark.smoke
def test_HeadersDropdownButton(setup):
    header = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, HEADER)))
    element = driver.find_element(By.ID, COMPANY)
    dropdown = driver.find_element(By.LINK_TEXT, CAREERS)
    ActionChains(driver).move_to_element(header).move_to_element(element).perform()
    ActionChains(driver).move_to_element(dropdown).click(dropdown).perform()
    time.sleep(2)
    web_title = driver.title
    assert web_title == CAREERS_WEB_TITLE


@pytest.mark.smoke
def test_MajorDeliveryCentersValue(setup):
    info_block = driver.find_element(By.XPATH, MATURITY_SCALE)
    ActionChains(driver).scroll_to_element(info_block).perform()
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, NUM_OF_CENTERS_ELEMENT)))
    time.sleep(2)
    number = element.text
    assert number == CORRECT_NUMBER


@pytest.mark.regression
def test_countrySelection(setup):
    field = driver.find_element(By.XPATH, AGREE_TO_COMMUNICATE)
    select_element = driver.find_element(By.XPATH, COUNTRIES)
    ActionChains(driver).scroll_to_element(field).perform()
    ActionChains(driver).move_to_element(select_element).click().perform()
    selected_country = driver.find_element(By.XPATH, COUNTRY)
    ActionChains(driver).move_to_element(selected_country).click().perform()
    country = driver.find_element(By.XPATH, SELECTED_COUNTRY)
    assert country.text == TESTING_COUNTRY


@pytest.mark.regression
def test_uploadCV(setup):
    driver.get(APPLY_FOR_JOB)
    time.sleep(2)
    save_info_check = driver.find_element(By.XPATH, SAVE_INFO)
    ActionChains(driver).scroll_to_element(save_info_check).perform()
    upload = driver.find_element(By.XPATH, RESUME)
    upload.send_keys(CV_PATH)
    cv_name = driver.find_element(By.XPATH, UPLOADED_DESCRIPTION)
    cv_name_text = cv_name.text
    assert cv_name_text.__contains__(CV_NAME)


@pytest.mark.smoke
def test_searchBar(setup):
    header = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, HEADER)))
    search_button = driver.find_element(By.XPATH, HEADER_SEARCH_BUTTON)
    ActionChains(driver).move_to_element(header).click(search_button).perform()
    driver.find_element(By.XPATH, SEARCH_INPUT).send_keys(SEARCING_NAME)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, SEARCH_BUTTON))).click()
    text = driver.find_element(By.XPATH, SEARCH_MATCHES).text
    assert text.__contains__("matches for " + SEARCING_NAME)
