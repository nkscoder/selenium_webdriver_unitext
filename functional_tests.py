# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('/Users/user8/Desktop/projects/testsgoat/geckodriver')
# browser = webdriver.Firefox(firefox_binary=binary)
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.log.level = "trace"
driver = Firefox(options=opts)








