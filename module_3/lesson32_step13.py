from selenium import webdriver
import time 
import unittest


class TestAbs(unittest.TestCase):
    def test_regisrtation_1(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        browser.quit()
    
    def test_regisrtation_2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        browser.quit()

if __name__ == "__main__":
    unittest.main()
