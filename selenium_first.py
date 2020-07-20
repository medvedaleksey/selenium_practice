import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selenium_beginners(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(executable_path='C:\Program Files\geckodriver\geckodriver.exe')
        self.driver.maximize_window()
    
    
    def test_newtours(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        username=driver.find_element_by_name("userName")
        username.send_keys("test")
        password=driver.find_element_by_name("password")
        password.send_keys("test")
        password.submit()
        time.sleep(3)
        registration=driver.find_element_by_link_text("registration form")
        registration.click()
       
    def test_begginers_guide_first(self):
        driver=self.driver
        driver.get("http://book.theautomatedtester.co.uk/")
        chapter1=driver.find_element_by_link_text("Chapter1")
        chapter1.click()
        text_assert=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"divontheleft")))
        assert text_assert.text=="Assert that this text is on the page"
        button_assert=driver.find_element_by_id("verifybutton")
        assert button_assert.get_attribute('value')=="Verify this button he here"
        radiobutton=driver.find_element_by_id("radiobutton")
        radiobutton.click()
        selecttype=Select(driver.find_element_by_id("selecttype"))
        selecttype.select_by_value("Selenium Code")
        button=driver.find_element_by_id("secondajaxbutton")
        button.click()
        text_field=driver.find_element_by_id("html5div")
        text_equal="To be used after the AJAX section of the book"+"\n"+"I have been added with a timeout"
        assert text_equal==text_field.text
        new_window=driver.find_element_by_id("multiplewindow")
        new_window.click()
        driver.switch_to.window("popupwindow")
        popuptext=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"popuptext")))
        assert popuptext.text=="Text within the pop up window"
        time.sleep(3)
        driver.close()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        time.sleep(3)
        new_text_button=driver.find_element_by_class_name("loadajax")
        new_text_button.click()
        new_text=driver.find_element_by_class_name("wind")
        print(new_text.text)
        home=driver.find_element_by_link_text("Home Page")
        home.click()
    
    def test_begginers_guide_fourth(self):
        driver=self.driver
        driver.get("http://book.theautomatedtester.co.uk/")
        chapter2=driver.find_element_by_link_text("Chapter4")
        chapter2.click()
        hoverOver=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"hoverOver")))
        action=ActionChains(driver)
        action.move_to_element(hoverOver)
        action.perform()
        alert=driver.switch_to_alert()
        time.sleep(1)
        assert alert.text=="on MouseOver worked"
        alert.accept()
        text_field=driver.find_element_by_id("blurry")
        text_field.send_keys("qwerty")
        button=driver.find_element_by_id("selectLoad")
        button.click()
        alert_text=driver.switch_to_alert()
        assert alert.text=="qwerty"
        time.sleep(1)
        alert_text.accept()
        driver.back()
        time.sleep(3)


    def test_first(self):
        driver = self.driver
        driver.get("https://account.habr.com/register/?state=b199323cdfd588e465cfa4b24b07078f&consumer=habr&hl=ru_RU")
        self.assertIn("Регистрация", driver.title)
        mail= driver.find_element_by_name("email")
        print(mail.get_attribute("value"))
        mail.send_keys("1234")
        login=driver.find_element_by_name("login")
        login.send_keys("#@!")
        login.submit()
        password_1=driver.find_element_by_id("password_field")
        password_1.send_keys("123456")
        password_1=driver.find_element_by_id("password_repeat")
        password_1.send_keys("654321")
        '''
        hover=ActionChains(driver).move_to_element(elem1)
        hover.perform()
        driver.back()
        '''
        button=driver.find_element_by_id("registration_button")
        button.click()
        message_error=driver.find_element_by_id("global_notices")
        time.sleep(5)       

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)       


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
