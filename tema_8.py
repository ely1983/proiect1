from time import sleep

import button as button
import click as click
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/autocomplete')
sleep(5)

addres = chrome.find_element(By.ID, 'autocomplete')
addres.send_keys("Constanta")
sleep(5)


Street_adrees = chrome.find_elements(By.CLASS_NAME, 'form-control')
Street_adrees[1].send_keys('saturn')
sleep(5)

chrome.find_element(By.XPATH, '//input[@id="route"]'). send_keys('mineri')
sleep(5)

chrome.find_element(By.CSS_SELECTOR, 'input#locality.form-control'). send_keys('Ovidiu')
sleep(5)


chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
sleep(5)

first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys("elisabeta")
sleep(5)

last_name = chrome.find_elements(By.CLASS_NAME, 'form-control')
last_name[1].send_keys('chiciuc')
sleep(5)


sex = chrome.find_element(By.ID, 'checkbox-2')
sex.click()
sleep(2)

#first_name = chrome.find_element(By.ID, 'datepicker')
#first_name.send_keys("08/08/2022")
#sleep(5)

chrome.find_element(By.XPATH, '//input[@data-provide="datepicker"]').send_keys('05/11/2022')
sleep(5)

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Submit'). click()
sleep(5)



