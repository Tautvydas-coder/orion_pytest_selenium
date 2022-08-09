import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from resources.variables import *
from driver_services.service import *
from selenium.webdriver.support import expected_conditions as EC
import pytest


# pytest -rA --random-order

@pytest.fixture()
def setup():
    global driver
    driver = driver_service_chrome()
    # driver = driver_service_mozila()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(ORION_WEB)
    time.sleep(2)
    cookies_accept = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, Cookies)))
    cookies_accept.click()
    time.sleep(1)
    yield
    driver.close()
    driver.quit()
    print("Test Completed")


@pytest.mark.smoke
def test_headersDropdownButton(setup):
    header = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, HEADER)))
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, COMPANY)))
    dropdown = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, CAREERS)))
    ActionChains(driver).move_to_element(header).move_to_element(element).perform()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(dropdown).perform()
    ActionChains(driver).click(dropdown).perform()
    time.sleep(3)
    web_title = driver.title
    assert web_title == CAREERS_WEB_TITLE


@pytest.mark.smoke
def test_majorDeliveryCentersValue(setup):
    info_block = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, MATURITY_SCALE)))
    ActionChains(driver).scroll_to_element(info_block).perform()
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, NUM_OF_CENTERS_ELEMENT)))
    time.sleep(2)
    number = element.text
    assert number == CORRECT_NUMBER


@pytest.mark.regression
def test_countrySelection(setup):
    field = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, AGREE_TO_COMMUNICATE)))
    select_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, COUNTRIES)))
    ActionChains(driver).scroll_to_element(field).perform()
    ActionChains(driver).move_to_element(select_element).click().perform()
    selected_country = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, COUNTRY)))
    ActionChains(driver).move_to_element(selected_country).click().perform()
    country = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, SELECTED_COUNTRY)))
    assert country.text == TESTING_COUNTRY


@pytest.mark.regression
def test_uploadCV(setup):
    driver.get(APPLY_FOR_JOB)
    time.sleep(2)
    save_info_check = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, SAVE_INFO)))
    ActionChains(driver).scroll_to_element(save_info_check).perform()
    upload = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, RESUME)))
    upload.send_keys(CV_PATH)
    cv_name = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, UPLOADED_DESCRIPTION)))
    cv_name_text = cv_name.text
    assert cv_name_text.__contains__(CV_NAME)


@pytest.mark.smoke
def test_searchBar(setup):
    header = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, HEADER)))
    search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, HEADER_SEARCH_BUTTON)))
    ActionChains(driver).move_to_element(header).click(search_button).perform()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, SEARCH_INPUT))).send_keys(SEARCING_NAME)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON))).click()
    # time.sleep(2)
    matches = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, SEARCH_MATCHES)))
    matches_for = matches.text
    assert matches_for.__contains__("matches for " + SEARCING_NAME)
