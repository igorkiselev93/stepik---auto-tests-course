from selenium import webdriver
import time 
import math

i = 1
while i < 3:
  link = f"http://suninjuly.github.io/registration{i}.html"
  try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(0.5)

    input1 = browser.find_element_by_css_selector('.first_block  .form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block  .form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block  .form-control.third')
    input3.send_keys("hah@ru")
    input4 = browser.find_element_by_css_selector('.second_block  .form-control.first')
    input4.send_keys("+7777")
    input5 = browser.find_element_by_css_selector('.second_block  .form-control.second')
    input5.send_keys("Smolensk")
    button = browser.find_element_by_css_selector('.btn')
    button.click()
    print("Тест прошел успешно")
    
  finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    i = i + 1

# не забываем оставить пустую строку в конце файла