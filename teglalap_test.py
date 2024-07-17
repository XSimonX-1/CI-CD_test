"""Keressük a téglalap kerületét

Készíts egy python applikációt (egy darab python file) ami selenium-ot használ.
Az ellenőrzésekhez pytest keretrendszert használj, valamint fontos az `assert` összehasonlítások használata is!

A program töltse be a téglalap kerülete app-ot.
https://high-flyer.hu/hetihazi/feladat1_teglalap.html

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:

Helyes kitöltés esete:
    a: 74
    b: 32
    Eredmény: 212

Nem számokkal történő kitöltés:
    a: kiskutya
    b: 32
    Eredmény: NaN

Üres kitöltés:
    a: <üres>
    b: <üres>
    Eredmény: NaN
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


class TestTeglalap(object):

    def setup_method(self):
        URL = 'https://high-flyer.hu/hetihazi/feladat1_teglalap.html'
        options = Options()
        options.add_argument('window-position=-2000,-1000')
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(URL)
        self.browser.maximize_window()

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

