# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('/Users/user8/Desktop/projects/testsgoat/geckodriver')
# browser = webdriver.Firefox(firefox_binary=binary)
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opt = Options()
opt.log.level = "trace"
driver = Firefox(options=opt)


# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
# She notices the page title and header mention to-do lists
# assert 'To-Do' in browser.title, "Browser title was " + browser.title

# browser.quit()




from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!')  

        # She is invited to enter a to-do item straight away

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  

# browser.quit()


