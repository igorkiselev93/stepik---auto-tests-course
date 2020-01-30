from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
    
select = Select(browser.find_element_by_css_selector("#dropdown"))
select.select_by_value(str(int(browser.find_element_by_css_selector("#num1").text)+int(browser.find_element_by_css_selector("#num2").text)))
    
browser.find_element_by_css_selector(".btn").click()