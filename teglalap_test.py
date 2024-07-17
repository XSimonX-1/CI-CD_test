from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import allure


class TestTeglalap(object):

    def setup_method(self):
        URL = 'https://high-flyer.hu/hetihazi/feladat1_teglalap.html'
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.browser.set_window_size(1600, 700)

    def teardown_method(self):
        self.browser.quit()

    def test_numbers_1(self):
        a_side = self.browser.find_element(By.ID, 'a')
        a_side.send_keys("74")
        b_side = self.browser.find_element(By.ID, 'b')
        b_side.send_keys("32")

        expected_result = str("212")
        result = self.browser.find_element(By.ID, 'result')
        assert type(str(expected_result)) is type(str(result))

    def test_non_numbers_1(self):
        a_side = self.browser.find_element(By.ID, 'a')
        a_side.send_keys("kiskutya")
        b_side = self.browser.find_element(By.ID, 'b')
        b_side.send_keys("32")

        expected_result = str("NaN")
        result = self.browser.find_element(By.ID, 'result')
        assert type(str(expected_result)) is type(str(result))

    def test_blank_1(self):
        a_side = self.browser.find_element(By.ID, 'a')
        a_side.send_keys("")
        b_side = self.browser.find_element(By.ID, 'b')
        b_side.send_keys("")

        expected_result = str("NaN")
        result = self.browser.find_element(By.ID, 'result')
        assert type(str(expected_result)) is type(str(result))

    #lehet egyszerűbben is:

    def test_numbers_2(self):
        self.browser.find_element(By.ID, 'a').send_keys("74")
        self.browser.find_element(By.ID, 'b').send_keys("32")
        result = self.browser.find_element(By.ID, 'result').text
        assert type(str(result)) is type(str("212"))

    def test_non_numbers_2(self):
        self.browser.find_element(By.ID, 'a').send_keys("kiskutya")
        self.browser.find_element(By.ID, 'b').send_keys("32")
        result = self.browser.find_element(By.ID, 'result').text
        assert type(str(result)) is type(str("NaN"))

    def test_blank_2(self):
        self.browser.find_element(By.ID, 'a').send_keys("")
        self.browser.find_element(By.ID, 'b').send_keys("")
        result = self.browser.find_element(By.ID, 'result').text
        assert type(str(result)) is type(str("NaN"))

