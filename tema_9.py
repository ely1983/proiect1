import unittest
from telnetlib import EC
from time import sleep
from turtledemo.chaos import f

import self as self
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class login(unittest.TestCase):
       def setUp(self):
           self.chrome = webdriver.chrome()
           self.chrome.maximize_window()
           self.chrome.get('https://the-internet.herokuapp.com/')
           self.chrome.find_element('self.from_authentication_link').click()
           self.chrome.implicitly_wait(7)


       def tearDown(self):
           self.chrome.quit()



# test 1 verificati url
def test_url(self):
    actual = self.chrome.current_url
    expected = 'https://the-internet.herokuapp.com/'
    self.assertEqual(expected, actual, 'url-ul nu este corect')


# test 2 - verificare page title
def test_page_title(self):
    actual = self.chrome.title
    expected = 'the internet'
    self.assertEqual(expected, actual, f'titlul pagini este {actual} dar ar fi trebuit sa fie {expected}')


#test 3 - verificare element
def test_element(self):
    actual = self.chrome.find_element(self.h2_element).text
    print(f'denumirea elementului este {actual}')
    expected = 'login page'
    self.assertEqual(expected, actual,f'denumirea elementului este {actual} si ar fi trebuit sa fie {expected}')

#test 4 - verificare login button
def test_login_displayed(self):
    button = self.chrome.find_element(self.login_button)
    self.assertTrue(button.is_displayed(), 'butonul de login nu este vizibil')


# test 5 - verificare href link
def test_href_link(self):
    actual_link = self.chrome.find_element(self.href_link).get_atribute('href')
    assert actual_link == 'http://elementalselenium.com','link-ul este gresit'
    print('link-ul este corect')


#test 6 -Lasati goale user si pass
#Click login
#Verifica ca eroarea e displayed

def test_error(self):
    self.chrome.find_element(self.login_buton).clik()
    error = WebDriverWait(self.chrome,10).until(EC.presence_of_element_located
                                                (self.error_message))
    self.assertTrue(error.is_displayed(), 'eroarea nu este vizibila')


# test 7- Completeaza cu user si pass invalide
# Click login
# Verifica ca mesajul de pe eroare e corect
# Este si un x pus acolo extra asa ca vom folosi solutia de mai jos

def test_mesaj_eroare(self):
    self.chrome.find_element(self.user_name).send_keys('tom')
    self.chrome.find_element(self.password).send_keys('SuperSecretPassword')
    self.chrome.find_element(self.ligin_button).clik()
    actual = self.chrome.find_element(self.error_message).text
    expected = 'your user name is invalid'
    self.assertTrue(expected in actual, 'error mesage text is incorect')


#test 8 - verificare inchidere mesaj eroare

def test_inchidere_mesaj_eroare(self):
    self.chrome.find_element(self.login_button).clik()
    sleep(5)
    self.chrome.find_element(self.error_closed).clik()
    sleep(5)
    try:
        self.chrome.find_element(self.error_closed)
    except NoSuchElementException:
        print('the text is not vizible on the pahe! It is ok')


#test 9- verificare lista label
def test_label(self):
    x = self.chrome.find_element(By.xpath,'//label')
    actual = x[0].text
    expected = 'username'
    self.assertEqual(expected,actual, 'username not found')
    actual = x[1].text
    expected = 'password'
    self.assertEqual(expected,actual, 'password not found')


def ec_vizibility_of_element_located(XPATH, param):
    pass


def unit(param):
    pass

#test 10 - verificare elemente secure si flash succes

def test_validate(self):
    self.chrome.find_element(By.name, 'username')
    self.chrome.find_element(By.name, 'password')
    self.chrome.find_element(By.class_name, 'radius').clik()
    actual = self.chrome.current_url
    expected = 'secure'
    self.assertTrue(expected in actual, 'secure not in url')

# test 11 - verificare ligin

def test_verificatre_login_logout(self):
    self.chrome.find_element(self.user_name).send_keys('tomsmith')
    self.chrome.find_element(self.password).send_keys('SuperSecretPasword')
    self.chrome.find_element(self.login_button).clik()
    self.chrome.find_element(self.logout_button).clik()
    WebDriverWait(self.chrome, 10).until(EC.url_contains('/login'))
    url_dupa_delogare = self.chrome.current_url
    expected_url = 'https://the-internet.herokuapp.com/login'
    assert url_dupa_delogare == expected_url, f'invalid url'


