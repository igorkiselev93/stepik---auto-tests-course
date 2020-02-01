from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector("input[name='firstname']").send_keys('Igor')
browser.find_element_by_css_selector("input[name='lastname']").send_keys('Kiselev')
browser.find_element_by_css_selector("input[name='email']").send_keys('df@maj.ru')

browser.find_element_by_css_selector("#file").send_keys(file_path)

btn = browser.find_element_by_css_selector(".btn")

btn.click()