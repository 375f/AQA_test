import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver

def test_site(driver):
    driver.get('https://www.demoblaze.com/index.html')
    galaxy_S6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_S6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'

def test_two_monitors(driver):
    driver.get('https://www.demoblaze.com/index.html')
    monitor_link = driver.find_element(By.CSS_SELECTOR, '''onclick="byCat('monitor')"''')
    monitor_link.click()
    results = driver.find_elements(By.CSS_SELECTOR, 'class="card-img-top img-fluid"')
    assert len(results) == 2