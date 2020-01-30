from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("button")
    btn = browser.find_element_by_css_selector(".btn")
    btn.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
   
    browser.find_element_by_css_selector(".btn-primary").click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()