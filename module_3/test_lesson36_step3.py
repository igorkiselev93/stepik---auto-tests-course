import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAlies():
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.message = ''
    
    def teardown_method(self):
        self.browser.quit()
        print(self.message)
    
    @pytest.mark.parametrize('variable_link_part', ['895','896','897','898','899','903','904','905'])
    def test_open_link(self, variable_link_part):
        link = f'https://stepik.org/lesson/236{variable_link_part}/step/1'
        self.browser.get(link)
        #document.querySelector(".attempt__message").firstElementChild.innerText.trim()
        text_area = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
        answer = math.log(int(time.time()))
        text_area.send_keys(str(answer))
        self.browser.find_element_by_css_selector(".submit-submission").click()
        #WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".attempt-message_correct")))
        time.sleep(3)
        correct_message = self.browser.find_element_by_css_selector(".smart-hints__hint").text
        
        assert correct_message == 'Correct!', f"В уроке {variable_link_part} в опциональном фидбеке не совпадает слово Correct!"
        if not correct_message == 'Correct!':
            self.message = self.message + correct_message

        

