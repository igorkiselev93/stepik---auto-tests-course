from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_css_selector("#input_value").text
y = calc(x)

input = browser.find_element_by_css_selector("#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(y)
check_box = browser.find_element_by_css_selector("#robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
check_box.click()
radio_btn = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_btn)
radio_btn.click()
btn = browser.find_element_by_css_selector(".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
btn.click()