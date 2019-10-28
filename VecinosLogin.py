#https://medium.com/better-programming/4-basic-python-tips-to-automate-your-workflow-befabe140b83
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromedriver = "C:\Users\Nico\Documents\PYTHON\Automatizacion\chromedriver_win32"
driver = webdriver.chrome(chromedriver)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()



